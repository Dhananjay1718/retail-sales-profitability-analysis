# Excel dashboard

[Download the latest workbook](https://raw.githubusercontent.com/Dhananjay1718/retail-sales-profitability-analysis/main/excel/retail_analysis.xlsx).

**On a phone:** open the **Mobile Summary** tab for large labels and concise
findings. On a computer, start with **Dashboard**, which opens first.

## What changed
The dashboard now has a full-width title, taller KPI rows, hidden gridlines,
formatted values and five vertically stacked charts. Chart axes label INR millions
where used. Download a fresh copy: an older downloaded workbook will not update.

## Sheets
- Dashboard: six formula KPIs and charts for all five business questions.
- Mobile Summary: compact formula KPIs and five findings for phone viewing.
- Orders: formatted source table, filters and profit conditional formatting.
- Customers: COUNTIF calculates orders per customer.
- Region_Formulas: SUMIFS revenue/profit and weighted margin.
- Numbered sheets: SQL output snapshots.

SUM, COUNTA, COUNTIF, SUMIFS and IFERROR are used. Cached formula results let
previewers display the initial calculations. The build verifies these values,
the merged title, sheet order and five charts. Desktop Excel and mobile viewers
can render differently; visual rendering is not tested automatically.

Rebuild after changing the input data: summary snapshots, customer lists and
chart source ranges reflect the generated dataset. This is not a live dashboard.
Practice: build a PivotTable from Orders by category and compare its sums with
SQL. A native PivotTable is not prebuilt.
