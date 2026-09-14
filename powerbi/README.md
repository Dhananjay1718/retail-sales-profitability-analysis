# Power BI

This page is a setup guide, not a report viewer.

For an existing dashboard, [download the Excel workbook](https://raw.githubusercontent.com/Dhananjay1718/retail-sales-profitability-analysis/main/excel/retail_analysis.xlsx)
or [download the browser dashboard](https://raw.githubusercontent.com/Dhananjay1718/retail-sales-profitability-analysis/main/dashboard/dashboard.html).

**Deliverable status: import-ready data, DAX and build instructions. No native
PBIX has been created or visually validated.** The HTML dashboard is separate.

1. In Power BI Desktop choose Get data > Text/CSV and select ../data/orders_clean.csv.
2. Name the imported table Orders. Set order_date to Date, IDs to Text,
   quantity to Whole number and financial fields/discount to Decimal number.
3. Create Calendar using calendar.dax, and mark it as a date table using Date.
4. Create a one-to-many relationship Calendar[Date] → Orders[order_date],
   with single-direction filtering from Calendar to Orders.
5. Add each definition from measures.dax separately using New measure.
6. Format Profit Margin, Repeat Customer Rate and MoM Growth as percentages.
7. Add cards: Revenue, Profit, Profit Margin, Order Count, Repeat Customer Rate.
8. Add a line chart with Calendar[Month] on X and Revenue on Y.
9. Add product/Profit and region/Profit bar charts.
10. Add discount_band/Profit Margin columns and a customer-count card.
11. Add region, category and Calendar[Date] slicers.
12. Clear slicers and reconcile KPIs against ../reports/executive_summary.md.
13. Save retail_analysis.pbix in this folder and upload it to the repository.

Month uses YYYY-MM for chronological text sorting. Use Calendar fields for date
filtering so time-intelligence measures work. Repeat customer rate recalculates
inside the selected period, category and region; it is not cohort retention.

The model is a simple Orders fact table plus Calendar. Future work: separate
Customer, Product and Region dimensions into a fuller star schema.

Learn: row vs filter context, measures vs columns, CALCULATE, DIVIDE, relationships,
date tables and slicers.

Reference:
https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tutorial-create-measures
