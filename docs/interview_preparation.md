# Interview preparation

## Explain it in 60 seconds
This is an AI-assisted retail analytics portfolio project using synthetic order
data. It answers five questions about growth, products, discounts, repeat buying
and regions. Python cleans and validates the data; SQLite implements reusable
business queries; Excel and a browser dashboard present the results. I reconcile
SQL with independent Pandas calculations. The Power BI source kit contains
measures and model instructions. Recommendations are hypotheses, not measured
business improvements.

Use that explanation only after reviewing the code and findings yourself.

## Questions and answers

1. What is the grain? One single-product order per row; order_id is unique.
2. What was cleaned? Exact duplicates, region whitespace/case, missing regions.
3. Why Unknown? It preserves sales totals instead of silently dropping records.
4. Why keep negative profit? It is a valid signal to investigate.
5. How is profit defined? Discounted revenue minus product and shipping costs;
   fixed overhead, tax, returns and marketing are outside scope.
6. Why weighted margin? SUM(profit)/SUM(revenue) gives the portfolio ratio;
   mean row margin gives tiny orders the same weight as large ones.
7. Why SQL and Python? SQL expresses business aggregation; Python handles data
   preparation, automation, validation and exports.
8. WHERE versus HAVING? WHERE filters rows; HAVING filters aggregated groups.
9. Why NULL in first-month growth? There is no previous month for comparison.
10. How can a JOIN inflate revenue? One fact row can match multiple dimension rows.
11. What is repeat customer rate? Customers with >=2 orders divided by observed
    customers inside the analysis window. It is not cohort retention.
12. Do discounts cause lower profit? Discounts reduce revenue algebraically,
    but group comparisons cannot measure incremental demand or causal campaign effect.
13. How do you validate? Keys, ranges, foreign keys, independent Pandas vs SQL
    totals and ratios, plus workbook formula/cache checks.
14. Power BI measure versus column? A measure evaluates in filter context;
    a calculated column stores row-level values.
15. How would you test a recommendation? Randomized treatment/control with a
    predefined outcome, margin guardrails and uncertainty estimates.
16. What would you improve? Real data, multiple line items, returns, cohort analysis,
    a fuller star schema and a tested native Power BI report.
17. What did AI contribute? Initial code, documentation and setup assistance.
    Explain the parts you have personally studied, tested and modified.

## 45-minute study sequence
- 10 minutes: data dictionary and executive summary.
- 10 minutes: SQL 01, 02, 04; explain each clause aloud.
- 10 minutes: Excel SUMIFS/COUNTIF and metric denominators.
- 10 minutes: Python pipeline and validation.
- 5 minutes: explain findings, limitations and one next experiment.

## Practice tasks
Change the loss-product query to show five weakest products.
Calculate category margins independently.
Explain why regional profit rank is not a fair measure of sales-team skill.
Build and check the Power BI report before claiming it is implemented.
