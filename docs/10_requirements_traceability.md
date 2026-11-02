# Business requirements and evidence traceability

> **Portfolio scope:** Independent, fictional NZ purchasing case study, fixed at **30 September 2026**. All entities and transactions are synthetic. The links below connect the *documented* business needs, workbook capabilities, acceptance checks and published evidence; they are **not** a signed-off requirement baseline or a claim of production acceptance testing.

## Business objective and key stakeholders

**Business objective:** Help a purchasing team identify undelivered purchase-order commitments, spot supplier-delivery exceptions and prioritise buyer follow-up without confusing commitments with invoice-paid spend or assuming open value is overdue value.

**Stakeholders:** Purchasing Manager (oversight), Purchasing Team Leader (supplier priorities), Purchasing Coordinator (line-level follow-up), Category Lead (category exposure) and Analyst/Reviewer (data integrity). See the [business story](01_business_story.md).

## Business need → requirement → acceptance check → evidence

| ID / business need | Stakeholder requirement and user | Acceptance check for this synthetic snapshot | Published evidence and boundary |
|---|---|---|---|
| **R-01 — Understand commitments** | As a Purchasing Manager, compare eligible PO committed, received and open values using consistent scope. | With dashboard filters **2026 / All buyers / All categories**, reported committed = **NZ$3,293,324**, received = **NZ$2,740,838**, open = **NZ$552,486**; committed minus received equals open at reported precision. | [KPI snapshot CSV](../evidence/2026_kpi_snapshot.csv), [calculation notes](08_evidence_and_reproducibility.md), [workbook](../workbook/NZ_Purchasing_Operations_Dashboard.xlsx). Aggregate arithmetic is checkable; source data are fictional. |
| **R-02 — Avoid receipt double-counting** | As an Analyst, calculate accepted receipts at **goods-receipt event grain**, aggregated back to the relevant PO line before comparing values. | A PO line can have multiple receipts; receipt unit/value reconciliation checks are recorded as PASS in `DATA_QA` and should be inspected in Excel. | [Technical implementation](02_technical_implementation.md), [recorded QA checks](../evidence/validation_summary.csv). The published check outcomes have not been independently rerun for this documentation update. |
| **R-03 — Prioritise overdue work** | As a Purchasing Coordinator, identify incomplete PO lines due for follow-up and distinguish overdue from merely open. | The 2026 dashboard cohort reports **19 overdue open lines** at the cutoff. The `FOLLOW_UP_QUEUE` has independent filtering and covers **all issue years**, so raw queue counts must not be compared to the filtered dashboard without aligning scope. | [KPI dictionary](03_kpi_dictionary.md), [business story](01_business_story.md), [workbook instructions](../workbook/README.md). Priority thresholds are illustrative, not an approved company SLA. |
| **R-04 — Review suppliers by exposure** | As a Team Leader, compare open PO value and delivery context across suppliers before directing buyers to follow up. | Top three named supplier open positions total approximately **NZ$346,233** (**62.7%** of 2026 open value); this is an exposure concentration, **not** evidence of supplier misconduct. | [Supplier exposure CSV](../evidence/2026_supplier_exposure.csv), [insights](05_insights_and_recommendations.md). Supplier names and amounts are synthetic. |
| **R-05 — Review category concentration** | As a Category Lead, compare purchase commitments and open values by category. | Power Tools (**NZ$171,168**) plus Chemicals & Adhesives (**NZ$138,636**) total approximately **NZ$309,804** (**56.1%** of 2026 open value). | [Category CSV](../evidence/2026_category_exposure.csv), [insights](05_insights_and_recommendations.md). `CATEGORY_SPEND` is a legacy sheet name; values are **not paid spend**. |
| **R-06 — Interpret completed-line delivery** | As a Purchasing Manager, see both completed-line OTIF and unfinished/overdue exceptions rather than treating OTIF as an all-order service level. | **206 / 234 = 88.03%** eligible completed lines were received fully by original due date; **58** eligible 2026 lines remain incomplete and are excluded from this OTIF denominator. | [KPI dictionary](03_kpi_dictionary.md), [reliability review](09_data_reliability_and_risk_controls.md), [audit CSV](../evidence/data_reliability_review_2026-09-30.csv). |
| **R-07 — Flag unreliable planning dates** | As a Coordinator, identify stale latest-ETA records and aged open orders for confirmation rather than silently overwriting dates. | **17** 2026 open lines have latest ETA before the snapshot; one 2025 open line is **535 days** overdue. These are scenario exceptions, not verified supplier promises. | [Data reliability review](09_data_reliability_and_risk_controls.md), [audit CSV](../evidence/data_reliability_review_2026-09-30.csv). No timestamped ETA-change or supplier-acknowledgement history is available. |
| **R-08 — State decision limits** | As a Reviewer, distinguish PO-price commitments, synthetic source checks and hypothetical recommendations from real operational outcomes. | Documentation must not claim live ERP/EDI integration, paid invoices, verified stock-outs, realised savings or externally audited supplier performance. | [README](../README.md), [provenance](07_sources_and_provenance.md), [limitations](04_validation_and_limitations.md). |

## Evidence status and review method

- **Documented:** The requirements, KPI scope, formulas, published outputs and internal QA observations have traceable links in this repository.
- **Reviewable in Excel:** The [published synthetic workbook](../workbook/NZ_Purchasing_Operations_Dashboard.xlsx) permits inspection of source rows, formulas, filtered dashboards and the `DATA_QA` tab. Follow the [Excel walkthrough](../workbook/README.md).
- **Not independently established:** Transaction-level accuracy against any real enterprise, third-party supplier identity, live ETA reliability, actual savings and impact on customers.
- **Not an automated test suite:** The acceptance checks above describe expected behaviour and known simulated snapshot values. They do **not** assert that every workbook formula or interaction has been re-tested during the present GitHub documentation update.

## Sensible next iteration (not delivered in the current prototype)

Add persistent supplier IDs on PO records, timestamped supplier ETA acknowledgements and change history, receiving exceptions, inventory-on-hand and demand, and a formal BA sign-off / UAT log. If renaming `CATEGORY_SPEND`, first check any workbook formulas, defined names and references before shipping.

*This mapping is an explanatory BA portfolio artifact, not an operational requirements baseline.*
