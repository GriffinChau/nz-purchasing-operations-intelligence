# Excel purchasing dashboard

This folder contains the **published synthetic Excel deliverable** accompanying the public [Purchasing Operations and Supplier Performance Intelligence case study](../README.md). It is not a real company export.

**Workbook filename:** `NZ_Purchasing_Operations_Dashboard.xlsx`

## What the workbook contains

- Purchasing overview and operational KPI calculations
- Supplier scorecard and buyer follow-up queue
- Purchase order lines, goods receipt events and reference data
- KPI dictionary, audit summary and internal data-quality checks
- An Excel-only working prototype with formulas, filters, three charts and three tables

## How to review

Download [NZ_Purchasing_Operations_Dashboard.xlsx](NZ_Purchasing_Operations_Dashboard.xlsx) and open it in Microsoft Excel desktop. The dashboard uses a fixed **30 September 2026** reporting cut-off and a fictional industrial distribution scenario in New Zealand.

1. Start on `DASHBOARD`; set PO issue year to **2026**, buyer to **All**, and category to **All** (selector cells `B5`, `F5` and `J5`). Compare headline values to the [published KPI CSV](../evidence/2026_kpi_snapshot.csv).
2. Check `PO_LINES` and `GOODS_RECEIPTS`: the grain is one PO line vs. one receipt event; multiple receipts may belong to a single PO line. Do not duplicate ordered value through a direct one-to-many join.
3. Open `SUPPLIER_SCORECARD` for open commitments, then `FOLLOW_UP_QUEUE` for buyer actions. The follow-up queue contains **33 static exception rows across all PO issue years** and is filtered independently of the dashboard. It does **not** automatically regenerate when new goods receipts are appended.
4. Open `CATEGORY_SPEND` for **category commitments and outstanding value**. Its sheet name does **not** mean actual invoices paid; such data is absent.
5. Review `DATA_QA` and compare its eight *recorded* control outcomes with the [QA summary](../evidence/validation_summary.csv). The reviewed workbook includes **20 stratified PO-to-GR samples across 2024–2026** (open, partial, cancelled and multi-receipt examples), a non-cancelling absolute mismatch check, and additional over-receipt flags. The status cells are genuine Excel formulas, not manually typed `PASS` labels. All eight recorded checks display PASS in the published snapshot; these are internal synthetic-data checks, not an external audit.
6. Read the [KPI dictionary](../docs/03_kpi_dictionary.md) and [evidence notes](../docs/08_evidence_and_reproducibility.md) for formula scope and limitations. The revised `SUPPLIER_SCORECARD` Action formula combines overdue lines, open NZD and completed-line OTIF under [illustrative thresholds](../docs/03_kpi_dictionary.md#supplier-scorecard-action--illustrative-triage-not-a-vendor-rating). The supplier screenshot in `assets/` predates these labels.

The workbook's transaction-level data is **synthetic**, not sourced from a real business. The eight recorded QA checks and additional checks reflect internal consistency rather than an independent audit or deployment. The PO-line receipt quantity, final-receipt date and delivery-status flags are **snapshot fields**: adding records to `GOODS_RECEIPTS` alone is not a complete refresh process.

For reviewers who prefer not to download the file, the main [project README](../README.md) contains KPI results, charts and business interpretation, while [evidence notes](../docs/08_evidence_and_reproducibility.md) provide calculation definitions and data limitations.

> The public case study is complete without opening Excel. The workbook is an optional supporting artifact to demonstrate how the calculations and reporting interface were built.

## Data reliability review

Before interpreting any supplier performance, also read the [source-data risk controls](../docs/09_data_reliability_and_risk_controls.md). The original simulated data have stale ETA exceptions and one long-aged open order; do not silently change those dates or treat synthetic supplier reliability assumptions as measured performance. The public case study does not constitute an EDI integration or a verification of real trading partners.
