# Evidence, metric logic and reproducibility

This is a **static, no-download-required evidence page** for an **independent, synthetic** Excel purchasing analytics project. It shows published aggregate results and methodology rather than requiring a reviewer to open the workbook. It is designed for *explainability*, not independent audit of every simulated transaction.

## 1. Evidence scope

- **Reporting snapshot:** 30 September 2026; not current, live purchasing data.
- **Main cohort:** Purchase orders **issued in 2026**, all buyers, all categories.
- **Monetary basis:** NZD excluding GST, valued at PO unit prices (not supplier invoice / cash paid).
- **Input scenario:** Fictional NZ industrial distributor, 14 suppliers, 95 SKUs, 5 buyers; 2024–2026 dataset with **1,159 PO lines and 1,394 receipt events**.
- **Follow-up worklist:** All issue years, separately filtered from main 2026 dashboard.

## 2. KPI snapshot evidence

All values below are transcribed from the recorded simulated dashboard figures. The machine-readable summary is [2026 KPI snapshot](../evidence/2026_kpi_snapshot.csv).

| Metric | Result |
|---|---:|
| PO commitments | **NZ$3,293,324** |
| Accepted receipts at PO price | **NZ$2,740,838** |
| Outstanding PO value | **NZ$552,486** |
| Open share of commitments | **16.8%** |
| Overdue open PO lines | **19** |
| Completed PO line share | **80.1%** |
| OTIF among completed eligible lines | **88.0%** |
| Outstanding units | **52,057** (mixed SKUs) |
| Open lines due in next 14 days | **13** |

**Arithmetic cross-check:**

```text
PO commitments            3,293,324 NZD
Minus: received at PO     2,740,838 NZD
------------------------------------------------
Open PO value               552,486 NZD

Open value share = 552,486 / 3,293,324 = 16.78%, approximately 16.8%
```

This demonstrates consistency among the **reported aggregates**, not independent verification of source transactions.

## 3. Concentration evidence

[Supplier exposure CSV](../evidence/2026_supplier_exposure.csv) and [category exposure CSV](../evidence/2026_category_exposure.csv) contain selected approximate aggregates.

| Supplier | Open value, approx. NZD |
|---|---:|
| Euro Industrial Products | 130,921 |
| Continental Abrasives | 125,102 |
| Northern Automotive Parts | 90,210 |
| **Named supplier subtotal** | **346,233 (62.7% of open value)** |

| Category | Open value, approx. NZD |
|---|---:|
| Power Tools | 171,168 |
| Chemicals & Adhesives | 138,636 |
| **Named category subtotal** | **309,804 (56.1% of open value)** |

Remaining values in CSV files are **calculated residuals from rounded headline values**, not supplier/category records extracted individually. Open value alone does not establish poor supplier performance or stockout risk.

## 4. Calculation design

At **PO line grain**, let **Q** be ordered units, **R** accepted received units, and **P** the PO unit price.

```text
PO committed value = SUM(Q * P) across eligible non-cancelled lines
Received value     = SUM(R * P) across the same eligible lines
Open units         = MAX(0, Q - R) per active line
Open value         = SUM(Open units * P)
```

Goods receipts are recorded at **receipt-event grain**. A single PO line may have multiple receipts. Receipt quantities must be **aggregated to PO-line level first**: joining order lines directly to multiple receipts and summing ordered values would double-count commitments.

- **Completed-line OTIF**: eligible fully received lines with last accepted delivery on/before original due date, divided by all eligible fully received lines. It deliberately **excludes open overdue lines**.
- **Overdue open lines**: incomplete non-cancelled lines past original due date at the fixed snapshot.
- **Buyer priority**: illustrative thresholds for triage; not a real corporate-approved SLA.

See the [technical implementation](02_technical_implementation.md) and [KPI dictionary](03_kpi_dictionary.md).

## 5. Quality control evidence

Eight checks were recorded as **PASS** in the original workbook's `DATA_QA` tab. They cover unit/value reconciliation, population counts, cancellation exclusions, a time cutoff, sampled allocations and OTIF eligibility. Full list: [validation summary CSV](../evidence/validation_summary.csv).

**Limitations of this evidence:** These are reported outcomes of a synthetic workbook's internal checks, not independently rerun validations against the underlying line-level dataset. A public static summary cannot prove every transaction was correct. For fully reproducible audit-level verification, a de-identified transaction extract or executable reproducibility script plus the corresponding data would be needed.

## 6. What is not claimed

No real company or Würth NZ data; no live ERP/SAP integration; no independently observed procurement cost savings, vendor quality, inventory shortages, delayed customer fulfilment or business impact. The portfolio demonstrates **reporting design, KPI governance, purchasing analysis and decision-support storytelling**, not a deployed production system.
