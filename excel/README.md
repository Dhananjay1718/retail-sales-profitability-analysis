# Excel

Open retail_analysis.xlsx and select Dashboard.
Download the file first; GitHub does not execute Excel formulas.

- Orders: formatted data table with filters and conditional profit formatting.
- Dashboard: SUM, COUNTA, IFERROR, KPI cards and two charts.
- Customers: COUNTIF measures orders per customer.
- Region_Formulas: SUMIFS computes region revenue/profit and IFERROR computes margin.
- Numbered summary sheets: SQL result snapshots.

Cached formula results are included and verified by the build with openpyxl.
This verifies the stored values and formula presence, not Excel's calculation
engine or visual layout. Recalculate and inspect in desktop Excel before presenting.

Customer and region lists reflect the built dataset. Rebuild after replacing data.
The numbered sheets and monthly chart are build-time snapshots.
Practice: create a PivotTable from Orders with category in Rows and revenue/profit
in Values; compare totals to SQL. No native PivotTable is prebuilt.
