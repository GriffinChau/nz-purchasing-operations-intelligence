# Sources, provenance and assumptions

## Data origin

All suppliers, buyers, products, PO prices, order lines, warehouses, receipt dates and business figures were **synthetically generated** for the fictional organisation **Kauri Industrial Distribution NZ**.

## Professional references

The analytical design uses the following public references to inform purchasing terminology and KPI choices. These are **inspiration for domain framing**, not the provenance of individual PO records.

- [SAP supplier evaluation guidance](https://learning.sap.com/courses/purchasing-in-sap-s-4hana/evaluating-suppliers-using-logistics-information-system) - purchasing and vendor analysis terminology.
- [SAP Help](https://help.sap.com/) - references for receipt/delivery-date logic.
- [Microsoft procurement analysis sample](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-procurement) - general procurement reporting examples; this project does **not** use Power BI.

## Date and supplier-evaluation references

The distinction between historical committed delivery dates and current operational delivery expectations is informed by [SAP On-Time Delivery Performance](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/af9ef57f504840d2b81be8667206d485/4478b6535fe6b74ce10000000a174cb4.html) and [SAP Logistics Vendor Evaluation](https://learning.sap.com/courses/purchasing-in-sap-s-4hana/setting-up-vendor-evaluation-using-logistics-information-system). These sources guide **terminology and analytical design only**, not the origin or validity of the synthetic data.

External EDI trading-partner messages, legal identifiers and system mappings are **not included**. See the [data reliability controls](09_data_reliability_and_risk_controls.md).

## Explicit scenario assumptions

- Snapshot is **30 Sep 2026** and remains fixed.
- Purchase commitments and receipts are valued in NZD excluding GST at original PO prices.
- Purchase orders may have multiple partial goods receipts.
- Domestic/import supplier lead times and delivery behaviours are illustrative.
- Priority thresholds are hypothetical buyer triage rules.
- There is no observed business implementation, realised savings, stock-out prevention or independently sourced supplier performance.

## Reproducibility

The original Excel prototype contains transaction-level data and formula-based internal checks but is not publicly distributed. Publicly available evidence consists of [aggregated CSV files](../evidence/2026_kpi_snapshot.csv), [technical documentation](02_technical_implementation.md), and [reported validation results](08_evidence_and_reproducibility.md). These do not enable independent row-level reproduction.
