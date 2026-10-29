# How to explore this Excel portfolio

## Five-minute business walkthrough

1. Read the [business case](01_business_story.md).
2. Open the workbook in **desktop Microsoft Excel**.
3. On `DASHBOARD`, choose **2026**, **All buyers**, **All categories**.
4. Review PO commitments, receipts, open value, overdue lines and completed-line OTIF.
5. Open `FOLLOW_UP_QUEUE`, check `Priority`, `Open_Value_NZD`, `Overdue_Days` and `Suggested_Next_Action`.
6. Use `SUPPLIER_SCORECARD` to distinguish exposure concentration from delivery reliability.

## Ten-minute technical walkthrough

1. Identify the PO-line grain of `PO_LINES` and the receipt-event grain of `GOODS_RECEIPTS`.
2. Find receipt events sharing `PO_Line_ID`; explain why a flat join can duplicate ordered values.
3. Inspect formulas in `PO_LINES!T:AC`, including open units and line value.
4. Change dashboard filter cells `B5`, `F5`, and `J5` and observe derived KPIs.
5. Verify denominator rules in `KPI_DICTIONARY`.
6. Review `DATA_QA` PASS statuses and discuss the limits of simulated validation.

## What was not built

There is no production ERP pipeline, SAP connection, Power BI dashboard or measured commercial improvement. This is a standalone Excel analytics portfolio project.
