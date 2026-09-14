# Python

From the repository root run:
```bash
python -m pip install -r requirements.txt
python python/build_project.py
```

Pipeline: generate raw data → clean → derive metrics → load SQLite → run SQL →
reconcile with independent Pandas calculations → export Excel/charts/report → ZIP.

analysis.ipynb is an exploration notebook. Its cells are initially unexecuted;
the build pipeline, rather than the notebook, performs the automated checks.
Start with read_csv, dtypes, fillna, drop_duplicates, groupby, and vectorized math.
Then study assertions, pathlib, SQLite, exports and packaging.

Exact duplicates are removed. Conflicting duplicate order IDs fail validation.
Missing regions become Unknown. Negative profit remains as valid business data.
The script overwrites only its generated output paths on rebuild.
