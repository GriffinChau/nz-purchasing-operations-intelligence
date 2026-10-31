#!/usr/bin/env python3
"""Build a reproducible, *real public* NZ procurement award analysis from MBIE GETS CSVs.

This is NOT a PO, goods receipt, inventory, EDI or supplier delivery-performance feed.
Uses only the Python standard library. No scraping of login-only websites.
"""
import argparse
import csv
import hashlib
import io
import json
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urljoin
from decimal import Decimal, InvalidOperation
from pathlib import Path

BASE = "https://www.mbie.govt.nz/assets/Data-Files/NZGPP-GETS-Open-Data/"
FILES = ["GETS-award-notices.csv", "GETS-supplier-data.csv"]
SOURCE_PAGE = "https://www.mbie.govt.nz/cross-government-functions/new-zealand-government-procurement-and-property/open-data"


def find_official_link(name):
    """Resolve the current CSV file link from the publisher's HTML page."""
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.links, self.href, self.label = [], None, []
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                self.href = dict(attrs).get("href")
                self.label = []
        def handle_data(self, text):
            if self.href is not None:
                self.label.append(text)
        def handle_endtag(self, tag):
            if tag == "a" and self.href is not None:
                self.links.append((self.href, " ".join(self.label)))
                self.href, self.label = None, []

    request = urllib.request.Request(SOURCE_PAGE, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        html = response.read(4_000_000).decode("utf-8", errors="replace")
    parser = Links()
    parser.feed(html)
    desired = "gets award notices" if "award" in name.lower() else "gets supplier data"
    for href, label in parser.links:
        text = " ".join(label.lower().split())
        if desired in text and "historic" not in text:
            url = urljoin(SOURCE_PAGE, href)
            print("Resolved current MBIE CSV: " + url, flush=True)
            return url
    raise ValueError("No CSV link found for " + desired + "; check the publisher's page manually.")


RESOLVED_LINKS = {}


def fetch_csv(name, folder):
    url = find_official_link(name)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (NZ public procurement research)", "Accept": "text/csv,*/*"})
    with urllib.request.urlopen(req, timeout=120) as response:
        payload = response.read(65_000_001)
        final_url = response.url
    if len(payload) > 65_000_000 or not payload or payload[:80].lstrip().lower().startswith((b"<html", b"<!doctype")):
        raise ValueError("Official source returned an empty/HTML/oversized file: " + final_url)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_bytes(payload)
    RESOLVED_LINKS[name] = final_url


def load_csv(path):
    b = path.read_bytes()
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            s = b.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    reader = csv.DictReader(io.StringIO(s))
    if not reader.fieldnames:
        raise ValueError("No header: " + str(path))
    rows = list(reader)
    if any(None in r for r in rows):
        raise ValueError("Malformed source CSV: " + str(path))
    return rows


def get(row, key):
    normalize = lambda x: re.sub("[^a-z0-9]", "", x.lower())
    canonical = normalize(key)
    return next(((v or "").strip() for k, v in row.items() if normalize(k) == canonical), "")


def date_value(s):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d-%b-%Y"):
        try:
            return datetime.strptime(s[:10], fmt).date()
        except ValueError:
            pass
    return None


def amount_value(s):
    s = s.replace(",", "").replace("$", "").replace("NZD", "").strip()
    try:
        n = Decimal(s)
        return n if n.is_finite() and n > 0 else None
    except (InvalidOperation, ValueError):
        return None


def export_csv(path, columns, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        w.writerows(records)


def run(input_dir, output_dir, first_year, last_year):
    awards = load_csv(input_dir / FILES[0])
    suppliers = load_csv(input_dir / FILES[1])
    for data, fields in [(awards, ["RFx ID", "Posting Agency", "Awarded Date", "Award Type", "Awarded Amount"]),
                         (suppliers, ["RFx ID", "Business Name"])]:
        if not data:
            raise ValueError("Empty official source")
        existing = {re.sub("[^a-z0-9]", "", k.lower()) for k in data[0]}
        if any(re.sub("[^a-z0-9]", "", key.lower()) not in existing for key in fields):
            raise ValueError("Official source header changed: " + str(list(data[0])))
    supplier_names = defaultdict(set)
    for r in suppliers:
        if get(r, "RFx ID") and get(r, "Business Name"):
            supplier_names[get(r, "RFx ID")].add(get(r, "Business Name"))
    by_rfx = {}
    invalid_dates = 0
    excluded = 0
    for r in awards:
        d, rf = date_value(get(r, "Awarded Date")), get(r, "RFx ID")
        if not d or not rf:
            invalid_dates += 1
            continue
        if not first_year <= d.year <= last_year:
            continue
        if get(r, "Award Type").lower() in ("not awarded", "cancelled", "canceled", "withdrawn"):
            excluded += 1
            continue
        prev = by_rfx.get(rf)
        if prev is None or get(r, "Report Date") > get(prev, "Report Date"):
            by_rfx[rf] = r

    agency_n, agency_val, supplier_n = Counter(), defaultdict(lambda: Decimal("0")), Counter()
    included = []
    value_count, value_total, multi_supplier, missing_supplier = 0, Decimal("0"), 0, 0
    for rfx, r in sorted(by_rfx.items(), key=lambda x: (get(x[1], "Awarded Date"), x[0]), reverse=True):
        agency = get(r, "Posting Agency") or "Undisclosed agency"
        val = amount_value(get(r, "Awarded Amount"))
        names = sorted(supplier_names[rfx], key=str.casefold)
        agency_n[agency] += 1
        if val is not None:
            value_count += 1
            value_total += val
            agency_val[agency] += val
        if len(names) > 1:
            multi_supplier += 1
        if not names:
            missing_supplier += 1
        for name in names:
            supplier_n[name] += 1
        included.append({
            "rfx_id": rfx, "awarded_date": get(r, "Awarded Date"),
            "posting_agency": agency, "title": get(r, "Title"),
            "award_type": get(r, "Award Type"),
            "published_award_amount_nzd": f"{val:.2f}" if val is not None else "",
            "supplier_count": len(names), "suppliers_as_published": " | ".join(names),
            "source_url": SOURCE_PAGE,
        })
    out = output_dir
    export_csv(out / "award_notices_sample.csv",
               ["rfx_id","awarded_date","posting_agency","title","award_type","published_award_amount_nzd","supplier_count","suppliers_as_published","source_url"],
               included[:250])
    export_csv(out / "agency_summary.csv", ["agency","award_notices","disclosed_award_values_nzd"],
               [{"agency": a, "award_notices": n, "disclosed_award_values_nzd": f"{agency_val[a]:.2f}"} for a, n in agency_n.most_common(100)])
    export_csv(out / "supplier_summary.csv", ["supplier_as_published","associated_award_notices"],
               [{"supplier_as_published": n, "associated_award_notices": c} for n,c in supplier_n.most_common(100)])
    manifest = {
        "publisher": "New Zealand Ministry of Business, Innovation and Employment (MBIE)",
        "source_page": SOURCE_PAGE, "source_type": "REAL public GETS contract award notices",
        "downloaded_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "year_filter": [first_year,last_year],
        "raw_sources": [{"url": RESOLVED_LINKS.get(fn, BASE + fn), "sha256": hashlib.sha256((input_dir / fn).read_bytes()).hexdigest(), "rows": len(awards if i == 0 else suppliers)}
                        for i,fn in enumerate(FILES)],
        "unique_award_notices_in_scope": len(included), "notices_with_positive_disclosed_values": value_count,
        "disclosed_value_coverage_pct": round(100 * value_count / len(included), 2) if included else None,
        "sum_disclosed_award_notice_values_nzd": str(value_total),
        "notices_with_multiple_suppliers": multi_supplier, "notices_with_no_named_supplier": missing_supplier,
        "excluded_not_awarded_rows": excluded, "missing_or_unparsed_award_dates": invalid_dates,
        "rules": [
            "Aggregate published contract award notice values by RFx ID, not real cash expenditure.",
            "Undisclosed or nonpositive amounts are unknown, not zero spend.",
            "Keep supplier counts separate: a multi-supplier notice is counted once by RFx ID and no value is allocated to individual suppliers.",
            "Supplier names are published labels; they are not verified supplier legal identities.",
            "No PO lines, goods receipts, ETA history, OTIF, stock or invoice data are present.",
            "A sampled extract is committed for inspection; full raw CSVs remain at the original publisher."
        ]
    }
    (out / "source_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"notices":len(included),"disclosed_values":value_count,"published_values_nzd":str(value_total)},indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--download", action="store_true", help="Download official MBIE CSV files")
    p.add_argument("--input-dir", type=Path, default=Path("data/gets_raw"))
    p.add_argument("--output-dir", type=Path, default=Path("public_data/gets"))
    p.add_argument("--start-year", type=int, default=2023)
    p.add_argument("--end-year", type=int, default=2026)
    args = p.parse_args()
    try:
        if args.download:
            for filename in FILES:
                print("Fetching " + BASE + filename, flush=True)
                fetch_csv(filename, args.input_dir)
        run(args.input_dir, args.output_dir, args.start_year, args.end_year)
    except Exception as e:
        p.exit(1, "Processing FAILED: " + str(e) + "\nDo not label outputs verified unless this succeeds.\n")
