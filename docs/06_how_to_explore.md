# How to explore the purchasing case study

This repository is designed to be understood **without downloading Excel**. It describes an independently developed synthetic purchasing analytics scenario and documents its calculations, data checks and limitations.

## Five-minute walkthrough for recruiters and purchasing managers

1. Start with the [project overview](../README.md), then the [business story](01_business_story.md).
2. Read the six headline KPIs: commitments, receipts, outstanding value, overdue PO lines, completed-line share and completed-line OTIF.
3. Review the [supplier scorecard screenshot](../assets/Purchasing_Supplier_Scorecard.png) and [buyer follow-up worklist screenshot](../assets/Purchasing_Follow_Up.png).
4. Open [business insights and actions](05_insights_and_recommendations.md) to understand why open PO exposure and overdue exceptions require different follow-up.
5. Check [sources and data provenance](07_sources_and_provenance.md). All business data is synthetic and no operational outcomes are claimed.

## Ten-minute walkthrough for technical reviewers

1. Open the [technical implementation](02_technical_implementation.md) to understand one PO line versus multiple receipt events.
2. Examine the formula examples and explain why joining receipts to PO lines without first aggregating them could double-count ordered value.
3. Use the [KPI dictionary](03_kpi_dictionary.md) to review inclusion rules, timing, units and the completed-line OTIF denominator.
4. Open the [KPI snapshot CSV](../evidence/2026_kpi_snapshot.csv), [supplier summary](../evidence/2026_supplier_exposure.csv) and [category summary](../evidence/2026_category_exposure.csv).
5. Check the [eight reported QA outcomes](../evidence/validation_summary.csv) and the [evidence limitations](08_evidence_and_reproducibility.md).

## Scope of the publication

This is a **static GitHub case study** with synthetic aggregate numbers, screenshots and calculation explanations. The original line-level Excel workbook is not distributed. The public evidence supports summary consistency checks and a review of analytical reasoning; it does not permit independent transaction-level replay.

No production ERP integration, live purchasing data, independently measured savings or verified operational improvement is claimed.
