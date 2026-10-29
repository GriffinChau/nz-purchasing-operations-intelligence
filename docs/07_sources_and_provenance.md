# Sources, provenance and assumptions

## Data origin

All suppliers, buyers, products, PO prices, order lines, warehouses, receipt dates and business figures were **synthetically generated** for the fictional organisation **Kauri Industrial Distribution NZ**.

## Professional references

The workbook's `SOURCES` sheet includes public references used to shape plausible purchasing terminology and KPI choices. These are **inspiration for domain framing**, not the provenance of individual PO records.

- [SAP supplier evaluation guidance](https://learning.sap.com/courses/purchasing-in-sap-s-4hana/evaluating-suppliers-using-logistics-information-system) — purchasing and vendor analysis terminology.
- [SAP Help](https://help.sap.com/) — references for receipt/delivery-date logic.
- [Microsoft procurement analysis sample](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-procurement) — general procurement reporting examples; this project does **not** use Power BI.

## Explicit scenario assumptions

- Snapshot is **30 Sep 2026** and remains fixed.
- Purchase commitments and receipts are valued in NZD excluding GST at original PO prices.
- Purchase orders may have multiple partial goods receipts.
- Domestic/import supplier lead times and delivery behaviours are illustrative.
- Priority thresholds are hypothetical buyer triage rules.
- There is no observed business implementation, realised savings, stock-out prevention or independently sourced supplier performance.

## Reproducibility

The Excel workbook contains line-level records, receipt journal, master tables, calculated metrics and formula-based QA checks. It is the main inspectable artifact. See [technical documentation](02_technical_implementation.md).
