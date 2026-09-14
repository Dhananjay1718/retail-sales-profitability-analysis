# Python

From the repository root run:
```bash
python -m pip install -r requirements.txt
python python/build_project.py
```

Pipeline: generate raw data → clean → derive metrics → load SQLite → run SQL →
reconcile with independent Pandas calculations → export Excel/charts/report → ZIP.

analysis.ipynb covers all five analyses and is executed during the build so
GitHub displays actual outputs. The pipeline also performs SQL/Pandas and workbook checks.
Start with read_csv, dtypes, fillna, drop_duplicates, groupby, and vectorized math.
Then study assertions, pathlib, SQLite, exports and packaging.

Exact duplicates are removed. Conflicting duplicate order IDs fail validation.
Missing regions become Unknown. Negative profit remains as valid business data.
The script overwrites only its generated output paths on rebuild.

## Modules
- build_project.py: data cleaning, SQL, Excel, executed notebook and ZIP.
- portfolio.py: product-discount and 90-day diagnostics, dashboard and business case.
- check_dashboard.py: browser interaction tests, screenshots, links and file hashes.
Install requirements-browser.txt and Playwright Chromium for the browser stage.
GitHub Actions runs both stages before publishing the final package.
