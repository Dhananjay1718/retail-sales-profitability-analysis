# Interactive dashboard

[Download HTML](https://raw.githubusercontent.com/Dhananjay1718/retail-sales-profitability-analysis/main/dashboard/dashboard.html)
and open it in a browser. Data and Plotly are embedded for offline use.

Region, category and month filters update all six KPI cards and five charts.
Reset restores the full dataset. Empty selections show zero counts and undefined
ratios as dashes. Repeat rate is calculated within the current filters.

- [Desktop screenshot](../reports/dashboard_desktop.png)
- [Phone-width screenshot](../reports/dashboard_mobile.png)
- [Browser validation](../reports/browser_validation.json)

template.html is the editable presentation source. python/portfolio.py inserts
the data. python/check_dashboard.py checks interactions against Pandas and captures
screenshots in Chromium. Screenshots do not constitute human visual signoff.

This browser dashboard is separate from Excel and the unfinished Power BI report.
