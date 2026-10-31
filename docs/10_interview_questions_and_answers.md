# Interview preparation: tough questions about the purchasing project

This is an independent, **synthetic Excel case study**, not an ERP implementation. Use these answers as prompts to explain what you actually understand and can verify.

## 1. "How do you know which supplier delivered a PO?"

**Answer:** PO lines have a supplier name and a PO-line ID. Goods receipt events reference the PO-line ID and contain a supplier ID. The supplier master maps IDs to names. In this simulated data, no mismatched supplier IDs were found among goods receipts. However, this is an **internal linkage check**, not external supplier identity verification. In production I would use stable supplier IDs and a reviewed trading-partner crosswalk.

## 2. "Is this connected to EDI or SAP?"

**Answer:** No. It is an Excel analysis of a synthetic PO/GR dataset. It illustrates concepts relevant to purchasing but does not ingest EDI messages, run inside SAP or verify any real trading partners. A future implementation would require authorised ERP/EDI extraction and validated supplier master data.

## 3. "Why would the latest ETA still be in the past?"

**Answer:** It means the recorded estimate is stale relative to the report cut-off. I found **18 of 59** active open lines in all years with an ETA earlier than 30 September 2026; **17 of 58** in the 2026 PO issue cohort. I would flag them for buyer confirmation and retain the old value for the audit trail rather than silently replacing it. The dataset lacks ETA update timestamps, so I cannot verify whether a supplier actually reconfirmed the date.

## 4. "Your dashboard says 88% OTIF. Isn't that misleading with overdue orders?"

**Answer:** The measure is explicitly **completed-line OTIF**, not overall on-time fulfilment. It is **206 on-time completed lines divided by 234 completed eligible lines** issued in 2026. The 58 incomplete lines are not included, and 19 of those are overdue against the original due date. Both must be shown together to avoid selection bias.

## 5. "Why is there a 535-day overdue PO?"

**Answer:** The fictional source contains one PO line from 2025 with an original due date of 13 April 2025 and an ETA of 6 May 2025, but no completed receipts by the snapshot. I have **flagged it as a long-aged exception rather than editing it away**. In a real purchasing team, I would verify whether it was open, received without posting, cancelled outside the extract or subject to an undocumented amendment.

## 6. "Can we trust the supplier reliability assumptions in the supplier master?"

**Answer:** No, not as measured performance. `Reliability_Assumption` is a synthetic scenario parameter. It is not based on actual supplier acknowledgements, delivery results or a verified historical sample. I use transaction-derived completed-line OTIF and overdue backlog to discuss the simulated outcomes, with clear denominators and limitations.

## 7. "How do you avoid double-counting purchase orders when a PO is delivered in several batches?"

**Answer:** Goods receipts are at receipt-event level while ordered quantities belong to the PO-line level. I reconcile and aggregate accepted receipts to each PO line before calculating completion or open value; otherwise joining multiple receipts directly can inflate ordered values.

## 8. "Is this real purchasing spend or a cost-saving calculation?"

**Answer:** Neither. The reported figures are PO commitments and goods receipt quantities valued at PO unit prices in NZD excluding GST. There are no supplier invoice payments, freight/FX landed costs or negotiation baselines in the sample, so no actual expenditure or savings are claimed.

## 9. "Why does the 2026 report not include every 2026 goods receipt?"

**Answer:** The main report filters **POs issued in 2026**. Receipts are linked to that PO cohort, potentially across different posting periods up to the fixed snapshot. That is not the same metric as all receipts *posted during calendar 2026*. The date basis should always be made explicit.

## 10. "What happens if a supplier ID is incorrect or a supplier changes legal name?"

**Answer:** This simulation has a 1-to-1 supplier master and no observed receipt ID mismatches. Real systems would need immutable internal keys, effective-dated records, EDI party IDs, exceptions for unmatched data, and ownership for authorised master-data corrections.

## 11. "How do you prove the numbers if the Excel file is not publicly hosted?"

**Answer:** The repository shows aggregated CSV snapshots, formulas and QA results, and arithmetic checks such as commitments less receipts equalling open value. This supports **aggregate consistency**, not complete independent reproduction of all PO lines. I can walk through the private workbook in an interview, but the static public evidence alone is not a transaction-level audit.

## 12. "What business action would you take first?"

**Answer:** Start with the **19 overdue open 2026 lines** (approximately NZ$182k open value). Within the 2026 cohort, **17 open lines have an ETA earlier than the snapshot** (approximately NZ$157k); verify fresh supplier commitments and assess operational urgency. Separately investigate the long-aged 2025 exception. Priorities are illustrative and should be aligned with a real team's SLA and stock availability.

## 13. "Why did you use synthetic data?"

**Answer:** This portfolio is an independent exercise to show how purchasing data can be structured, reconciled and converted into decision-support measures without using confidential company records. I do not claim to have delivered actual savings, fixed a live process or evaluated real suppliers.

## 14. "What would you improve next?"

**Answer:** Preserve original due dates and a timestamped series of revised ETAs, connect buyer ownership to stable supplier master keys, add supplier acknowledgements and exception resolution codes, then validate performance over clearly defined PO/receipt cohorts. In a real deployment, implement refresh monitoring and escalation rules only after the upstream data controls are reliable.

## 15. "How was the work developed?"

**Answering principle:** Describe your genuine contributions and any tools or AI assistance accurately. Be ready to explain calculations, choices, tests and limitations without representing generated examples as implemented client work.
