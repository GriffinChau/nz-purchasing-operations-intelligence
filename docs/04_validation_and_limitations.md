# Validation and limitations

## Reconciliation controls

Eight controls in the submitted workbook's `DATA_QA` sheet displayed **PASS**:

| Control | Result |
|---|---|
| Receipt units reconcile to PO received units | PASS |
| Receipt value reconciles to PO received value | PASS |
| PO line count is 1,159 | PASS |
| Goods receipt count is 1,394 | PASS |
| OTIF successes do not exceed completed lines | PASS |
| Cancelled PO lines have no active commitment | PASS |
| No receipts after snapshot cutoff | PASS |
| Sampled PO-to-GR allocation reconciles | PASS |

The whole included receipt history shows **1,116,418 accepted units** and approximately **NZ$11,498,958 receipt value**. These are all-year figures and should not be confused with the filtered 2026 dashboard cohort.

The workbook inspection found no cached common Excel formula errors. **PASS is internal consistency, not verification against a real ERP.**

## Scope boundaries

- Snapshot as at **30 September 2026**; not a real-time report.
- Dashboard uses **PO issue year**, not receipt year.
- Follow-up queue operates on **all years** and is independent of dashboard filters.
- Completed-line OTIF excludes open overdue items; review it with open and overdue counts.
- Value reflects PO unit prices, excludes tax, freight, supplier invoices, FX conversion and landed costs.
- Some older simulated worklist exceptions may need cleanup in a real operational dataset.

## Verification boundary

The workbook used to generate these figures is not published in the repository. Eight recorded `PASS` results describe internal controls, not a third-party audit or independently reproducible transaction-level validation. The public CSV files provide aggregate numerical evidence only.


## Source limitations

All PO, vendor, product, receipt and buyer records are **synthetic**. Suggested supplier conversations, bottlenecks and follow-up priorities are a scenario exploration. No real sales uplift, cost reduction or operational impact is claimed.
