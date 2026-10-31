# KPI dictionary

**Reporting cut-off:** 2026-09-30. **Currency:** NZD excluding GST. Data is synthetic.

| KPI | Definition | Key caveat |
|---|---|---|
| PO Committed Value | Sum of ordered quantity × PO unit price for non-cancelled eligible lines | Commitments, not paid spend |
| Received Value | Accepted receipt quantity × associated PO unit price | Not invoiced value or cash outflow |
| Open PO Value | Sum of max(ordered − accepted units, 0) × PO price for active lines | Not all open value is overdue |
| Outstanding Units | Sum of open PO quantities | Units across SKUs are not interchangeable |
| PO-line Completion Rate | Eligible fully received lines / eligible non-cancelled PO lines | A recent issue-year cohort can still be open |
| Completed-line OTIF | Completed lines with last accepted receipt on/before original due date / completed eligible lines | Open overdue lines excluded: do not present as overall service level |
| Overdue Open Lines | Active incomplete PO lines with original due date before as-of date | Original commitment; revised ETA may differ |
| Due Within 14 Days | Incomplete, active lines with due date from as-of through day 14 | An operational watchlist, not forecast demand |
| Supplier Open Value | Remaining open commitment by supplier | Exposure is not a verdict on supplier quality |
| Category Open Value | Remaining open commitment by product category | No on-hand stock or urgency available |

## Additional reliability flags and definitions

| Flag or measure | Definition | Limitation |
|---|---|---|
| Stale latest ETA | Active incomplete PO line with latest recorded ETA before the fixed snapshot date | Does not prove date was originally supplier-confirmed; latest update timestamp not available |
| Long-aged overdue | Open PO line more than 90 days past its *original* due date | Escalation threshold is illustrative; 2025 long-aged items should be reviewed separately |
| Receipt supplier identity check | Match each GR supplier ID against the PO's supplier name via supplier master | Internal synthetic-data linkage only; no EDI party verification |
| Reliability_Assumption | Synthetic supplier master parameter | **Not** observed or verified supplier performance; should not be used as a scored KPI |
| Completed-line OTIF | On-time and in-full completed eligible PO lines / all completed eligible lines | Excludes unfinished lines, including overdue lines |
| Original Due vs Latest ETA | Original due date is for historical commitment assessment; latest ETA for current planning follow-up | No timestamped ETA revision history or supplier acknowledgement events |

For the simulated **2026 PO issue-year** cohort, **206 of 234** eligible completed lines met original due dates (88.03%). There were **58 incomplete eligible** lines, including **19 overdue**. Refer to [Data reliability and ETA controls](09_data_reliability_and_risk_controls.md).

## Classification policy

The follow-up worklist contains illustrative priorities: P1 for lines **at least 30 days overdue**, or **at least 10 days overdue and NZ$12k+ open**; P2 for other overdue lines; P3 for due-soon lines. These are **illustrative thresholds**, not a company's approved SLA.

## Excluded metrics

The data cannot establish paid procurement spend, realised purchase-price savings, stockouts, lost sales, actual fill rate, stock turnover, landed cost or supplier defect rate. These are intentionally not presented as measured outcomes.

See [technical implementation](02_technical_implementation.md) and [validation](04_validation_and_limitations.md).
