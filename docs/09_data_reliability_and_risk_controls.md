# Data reliability, supplier identity and ETA controls

> **Portfolio-specific audit:** These findings were recomputed from the synthetic `Purchasing_Operations_Dashboard.xlsx` source file as at **30 September 2026**. They refer to the scenario only. The public repository includes aggregate evidence, but not an independent supplier ERP feed or transaction-level audit export.

## What does "reliable supplier data" mean here?

Three separate topics must not be conflated:

1. **Data integrity:** Can PO lines, receipt events and supplier master records be joined and reconciled without errors?
2. **Delivery performance:** Does the dataset show that eligible *completed* PO lines were received by their original committed date?
3. **Forecast reliability:** Can the most recent supplier ETA be trusted today, and is there a history of revisions / acknowledgements?

The source records support the first two questions **within a synthetic dataset**. They cannot establish real supplier trustworthiness or independently validate ETA forecasts against a live supplier feed.

## What the additional audit found

| Control or exception | Finding | Interpretation |
|---|---:|---|
| PO line records | **1,159** | Full 2024-2026 synthetic population |
| Receipt events | **1,394** | Receipt-event grain; multiple receipts can match one line |
| Unique supplier master IDs | **14** | 14 distinct supplier IDs |
| Receipt supplier ID mismatches | **0** | Every receipt ID matches the master supplier assigned to its PO line |
| Receipt records without a PO line | **0** | All GR references resolve |
| PO-line quantity reconciliation failures | **0** | Accepted units agree with sum of GR units |
| Open PO lines, all years | **59** | Active incomplete order lines |
| Open lines whose latest ETA is already past | **18** | **Needs supplier confirmation**; do not treat the ETA as a current promise |
| Open PO lines issued in 2026 | **58** | Main annual issue cohort |
| 2026 open lines with outdated ETA | **17** | These account for approximately **NZ$156,985** in open value |
| 2026 overdue open PO lines | **19** | Approximately **NZ$182,445** still open on these lines |
| 2026 open lines overdue by over 90 days | **10** | Requires an ageing / escalation review |
| Old 2025 overdue line | **1 line** | **535 days** overdue, approximately **NZ$4,410** of open value |

See [machine-readable audit results](../evidence/data_reliability_review_2026-09-30.csv).

### Example: a long-aged purchasing exception

The synthetic PO line `POL00883` was due on **13 April 2025**. Its latest recorded ETA is **6 May 2025**, yet it remains open as at **30 September 2026**. The resulting ageing is **535 days** beyond the original due date.

**Buyer action:** Confirm whether the order is genuinely still outstanding, received but not posted, cancelled outside the current dataset or awaiting an amendment. Verify against the supplier and receiving team before changing the PO. A production workflow would likely flag it for special exception review. The original synthetic data have **not** been silently rewritten.

## Date governance: original promise versus latest ETA

| Date | Purpose | How to use it |
|---|---|---|
| `PO_Date` | When the order was placed | Issue-year cohort, lead-time context |
| `Original_Due` | Original agreed due date in this scenario | Historical late/OTIF evaluation; do not overwrite with latest ETA |
| `Latest_ETA` | Latest recorded planning estimate | Buyer follow-up, potential arrival plan; not independently confirmed |
| `GR_Date` | Recorded goods receipt date | Receipt timing / observed delivery in this simplified scenario |
| `ETA_Updated_At` | **Not collected** | Without it, ETA freshness and change frequency cannot be verified |
| `Supplier_Confirmed_At` / acknowledgement | **Not collected** | Without it, confirmation history cannot be independently assessed |

**Stale ETA flag** for an active incomplete line:

```text
IF(Open_Units > 0 AND Latest_ETA < 2026-09-30, "STALE - CONFIRM ETA", "NO STALE ETA FLAG")
```

This is a **snapshot rule**, not a real-time alert. A future ETA alone does not prove that a supplier confirmed it. Similarly, an original due date in the past and a revised ETA in the future still represent a missed *original* commitment.

SAP guidance distinguishes a date retained for supplier performance assessment from an updated delivery date used for planning. [SAP On-Time Delivery Performance](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/4478b6535fe6b74ce10000000a174cb4.html) and [SAP purchasing evaluation](https://learning.sap.com/courses/purchasing-in-sap-s-4hana/setting-up-vendor-evaluation-using-logistics-information-system) are domain references, not systems integrated into this case study.

## Supplier identity and EDI

- The PO line stores **supplier name**.
- The goods receipt stores **Supplier_ID** and PO-line reference.
- The supplier master maps **Supplier_ID** to name.
- In the synthetic dataset, the master mapping produces **zero observed mismatches** for existing goods receipts.

**Do not claim:** that an external EDI trading partner was authenticated, that legal-entity mapping was checked, or that vendor master data were verified against real companies. EDI messages, external IDs (e.g. GLN), PO acknowledgement identifiers, vendor merge history and API logs are **not** available in the portfolio data.

**If this were deployed in a real environment:** assign immutable internal supplier keys to PO headers/lines, maintain a controlled external trading-partner crosswalk, use approved master-data changes with effective dates, and quarantine unmatched EDI documents rather than automatically joining on business names.

## Supplier "reliability" must be evidence-based

The `SUPPLIERS` master includes a column named `Reliability_Assumption`. It is a **synthetic data-generation parameter**, **not a measured supplier reliability score**. It should never be presented as historical evidence of supplier quality, confirmed ETA accuracy, or overall supplier ranking.

This project does support a **completed-line OTIF** calculation for its simulated records:

- 2026 eligible non-cancelled PO lines: **292**
- Completed eligible lines: **234**
- Completed lines delivered fully by original due date: **206**
- Completed-line OTIF: **206 / 234 = 88.03%**

The **58 incomplete eligible lines**, including **19 overdue**, are excluded from that OTIF denominator. Do not label 88.03% an all-orders service level or combine it with synthetic quality scores.

## Quality assurance and remaining limits

The [audit controls CSV](../evidence/data_reliability_review_2026-09-30.csv) captures new checks for supplier mapping, quantity reconciliation, dates, stalled ETAs and aged backlog. Existing [internal QA outcomes](../evidence/validation_summary.csv) are reported separately.

**Still not testable without additional data:**

- EDI message correctness, supplier legal identity or external trading-partner identifiers
- ETA revision frequency, freshness timestamp and actual supplier acknowledgements
- Stockouts, customer service impact, inventory carrying cost or actual negotiated savings
- Supplier quality, invoice reconciliation and freight / FX adjusted landed cost

**Recommended next-stage data requirements:** immutable supplier ID on purchase orders, external party ID / mapping, acknowledgement date, revision timestamp, revised confirmed date, shipment reference, goods receipt posting and transaction reversal identifiers, receiving exception status and order closure reason.

**Release principle:** A clean formula is not proof of reliable source data. Report only what the dataset supports, flag stale fields, and record unresolved limitations.
