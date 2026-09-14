# Repository review

## Corrections
- Replaced the clipped Excel title with a merged, taller heading.
- Added product, discount and customer charts so Excel covers all five questions.
- Added a compact Mobile Summary tab and moved dashboard sheets before raw data.
- Removed dashboard gridlines and redundant chart legends; labelled financial axes.
- Completed and executed the Python notebook's discount and regional analyses.
- Added a check for the negative-profit-product SQL result, including empty results.
- Added direct download links and clarified preview, Excel, HTML and Power BI status.

## Checks
The build validates independent SQL/Pandas totals, margins, counts and growth;
Excel KPI caches, five charts, merged title and sheet order; and notebook execution.
The regenerated validation.json is authoritative for the build that produced it.

## Remaining limitations
Native Power BI PBIX has not been built. Desktop Excel/mobile visual rendering
and browser rendering have not been inspected automatically.
Synthetic findings are not real company results. Excel charts and summary lists
refresh through a rebuild, not a connection to a live business database.
