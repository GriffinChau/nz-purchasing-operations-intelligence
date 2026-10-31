# Sources, provenance and assumptions

## Data origin

All suppliers, buyers, products, PO prices, order lines, warehouses, receipt dates and business figures were **synthetically generated** for the fictional organisation **Kauri Industrial Distribution NZ**.

## Professional references

The analytical design uses the following public references to inform purchasing terminology and KPI choices. These are **inspiration for domain framing**, not the provenance of individual PO records.

- [SAP supplier evaluation guidance](https://learning.sap.com/courses/purchasing-in-sap-s-4hana/evaluating-suppliers-using-logistics-information-system) - purchasing and vendor analysis terminology.
- [SAP Help](https://help.sap.com/) - references for receipt/delivery-date logic.
- [Microsoft procurement analysis sample](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-procurement) - general procurement reporting examples; this project does **not** use Power BI.

## Explicit scenario assumptions

- Snapshot is **30 Sep 2026** and remains fixed.
- Purchase commitments and receipts are valued in NZD excluding GST at original PO prices.
- Purchase orders may have multiple partial goods receipts.
- Domestic/import supplier lead times and delivery behaviours are illustrative.
- Priority thresholds are hypothetical buyer triage rules.
- There is no observed business implementation, realised savings, stock-out prevention or independently sourced supplier performance.

## Reproducibility

The original Excel prototype contains transaction-level data and formula-based internal checks but is not publicly distributed. Publicly available evidence consists of [aggregated CSV files](../evidence/2026_kpi_snapshot.csv), [technical documentation](02_technical_implementation.md), and [reported validation results](08_evidence_and_reproducibility.md). These do not enable independent row-level reproduction.
