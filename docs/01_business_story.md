# Business story - Purchasing decisions

> **Independent, fictional scenario:** Kauri Industrial Distribution NZ. All transactions and entities are synthetic.

## Why this project exists

Purchasing staff often need to reconcile orders with multiple goods receipts while managing open quantities and delayed shipments. A single company-wide scorecard can distract from buyer-specific actions.

**Key business question:** Which purchase-order lines need a supplier follow-up, and what purchasing exposure remains?

## Intended readers

| Stakeholder | Decision supported |
|---|---|
| Purchasing Manager | Review total commitments, remaining exposure, delivery reliability |
| Purchasing Team Leader | Compare supplier backlogs and distribute buyer follow-up |
| Purchasing Coordinator | Identify overdue PO lines, confirm revised ETAs and next steps |
| Category/Purchasing Lead | Investigate category concentration and upcoming commitments |

## Workbook experience

- **DASHBOARD:** annual PO commitment, received and open value, completion and completed-line OTIF.
- **FOLLOW_UP_QUEUE:** PO-line worklist with priority, original due date, overdue days and suggested next action. It covers **all years** and has independent filters.
- **SUPPLIER_SCORECARD:** supplier delivery and backlog comparisons.
- **CATEGORY_SPEND:** purchasing commitment and open value by product category.
- **DATA_QA:** controls validating the transaction logic.

## Management walkthrough

1. Identify the **2026 open PO value of approximately NZ$552k**, based on a historical snapshot of 30 September 2026.
2. Separate **19 overdue open PO lines** from orders that are not yet due.
3. Use supplier and category views to find concentrations, then open the buyer worklist.
4. Contact suppliers to verify shipment status, revised arrival dates and partial receipt details; do not infer stock-outs without demand/on-hand data.
5. Document actions and refresh exceptions in a real operating setting.

## Acceptance criteria for this prototype

- All KPIs have defined scope, timing and exclusions.
- Goods receipts reconcile to received quantities and values at PO-line level.
- Users can select PO issue year, buyer and product category in the main dashboard.
- Supplier performance is contextualised alongside open and overdue backlog.
- Data limitations and synthetic assumptions are prominent.

**Outcome:** A functioning Excel purchasing decision-support *prototype*, not a measured improvement implemented in a real purchasing department.
