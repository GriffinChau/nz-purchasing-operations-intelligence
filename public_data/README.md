# Public procurement data: separate real-data extension

**Status as at 31 October 2026:** The ETL script and source documentation are available. Automatic access from GitHub Actions was blocked by the publisher's HTTP 403, so no public-data analysis has completed or been published. Do not present any output as downloaded and validated until `public_data/gets/source_manifest.json` is present and the run has succeeded.

## Official source and provenance

- **Publisher:** New Zealand Ministry of Business, Innovation and Employment (MBIE)
- **Dataset:** Government Electronic Tender Service (GETS) award notice and supplier open data
- **Source page:** https://www.mbie.govt.nz/cross-government-functions/new-zealand-government-procurement-and-property/open-data
- **Official downloads:** On the MBIE source page, use **GETS award notices [CSV]** and **GETS supplier data [CSV]**. The older fixed `/assets/Data-Files/...` URLs published in some third-party indexes did not work in our test (HTTP 404). The script attempts to discover current download URLs from the publisher's page.
- **Publisher's reported coverage:** 1 July 2019 through 30 June 2026 (page updated 13 August 2026, quarterly publication).
- **Data-grain:** One RFx / published contract award notice, linked via RFx ID to zero or more published supplier names.

This is a new **real public procurement dataset**, NOT a replacement for the original synthetic PO/GR study. It must not be joined to the original fictional supplier names or assigned the original OTIF, ETA, inventory or payment values.

## Reproduce the public-data extraction

No private login, API key or third-party scraper is needed. Directly request the official CSV download rather than scraping HTML.

```bash
python3 scripts/get_gets_public_data.py --download
```

If the MBIE website blocks automated downloads, obtain the two official CSVs using a browser from the source page, place them under `data/gets_raw/` with the official filenames, then run:

```bash
python3 scripts/get_gets_public_data.py
```

Successful processing creates:

| File | Content |
|---|---|
| `public_data/gets/source_manifest.json` | Publisher URL, download date, raw SHA-256 hashes, record counts, scope, completeness controls |
| `public_data/gets/award_notices_sample.csv` | First 250 included real published awards, with RFx identifier, agency, supplier names, published value and URL |
| `public_data/gets/agency_summary.csv` | Award-notice counts and sum of disclosed values by publishing agency |
| `public_data/gets/supplier_summary.csv` | Supplier-name appearances per award notice, **not** supplier spend |

The optional [GitHub Actions workflow](../.github/workflows/refresh-gets-public-data.yml) runs only when manually initiated and may fail while the official site blocks automated access. To proceed reliably, download official CSV files in a browser and run the local command above. A script existing in the repository does **not** prove that the website was fetched successfully. Check the output manifest.

## Key business / analytical controls

1. **Reported contract values are not paid spend**. Awards can represent expected contract value rather than invoices or transactions.
2. **Missing or zero awards are not treated as zero procurement spend**. Value coverage is reported.
3. **Multi-supplier / panel awards:** One RFx is counted once; award value is not multiplied by the number of named suppliers.
4. **Supplier ID reliability:** Supplier names are published labels, not validated legal entities or an authenticated EDI mapping. NZBN might be missing or represented inconsistently.
5. **No delivery performance measurement:** There are no original delivery promises, receipt events, latest confirmed ETAs or OTIF denominators in GETS.
6. **No claim of complete NZ government procurement:** GETS is published notice coverage and does not capture all government activity or real purchasing cash outflow.

This portfolio independently examines public procurement award notices. It is not affiliated with MBIE, GETS or any listed agency or supplier.

**Interview-safe description:** \"I sourced publicly available New Zealand procurement award notices and supplier records directly from MBIE GETS CSV releases. My script joins supplier names to award notices using RFx ID, checks disclosed values, and calculates award counts and agency-level totals. This is public contract award data, not purchase-order execution or supplier delivery performance data.\"
