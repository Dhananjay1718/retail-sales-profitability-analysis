"""Exercise real browser filters against Pandas and capture desktop/mobile views."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import numpy as np
import pandas as pd
from playwright.sync_api import sync_playwright

root=Path(__file__).resolve().parents[1]
df=pd.read_csv(root/'data/orders_clean.csv')
errors=[]
def check(page,rows):
    revenue=float(rows.revenue.sum());profit=float(rows.profit.sum())
    counts=rows.groupby('customer_id').size()
    expected={'revenue':revenue,'profit':profit,'orders':len(rows),
      'margin':profit/revenue if revenue else None,
      'aov':revenue/len(rows) if len(rows) else None,
      'repeat':float(counts.ge(2).mean()) if len(counts) else None}
    actual=page.evaluate('window.currentMetrics')
    for key,value in expected.items():
        if value is None:assert actual[key] is None
        else:np.testing.assert_allclose(actual[key],value,atol=.01)
    plotted=page.evaluate("document.getElementById('products').data[0]")
    products=rows.groupby('product').profit.sum().to_dict()
    assert set(plotted['y'])==set(products)
    for name,value in zip(plotted['y'],plotted['x']):np.testing.assert_allclose(value,products[name],atol=.01)

def select(page,key,value):
    before=page.evaluate('window.renderVersion')
    page.select_option('#'+key,value)
    page.wait_for_function('v => window.renderVersion > v',arg=before)

with sync_playwright() as pw:
    browser=pw.chromium.launch()
    page=browser.new_page(viewport={'width':1440,'height':1000})
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((root/'dashboard/dashboard.html').as_uri(),wait_until='load')
    page.wait_for_function('window.renderVersion >= 1')
    check(page,df)
    assert page.locator('.js-plotly-plot').count()==5
    page.screenshot(path=str(root/'reports/dashboard_desktop.png'),full_page=True)
    select(page,'region','North');check(page,df[df.region.eq('North')])
    select(page,'category','Electronics');select(page,'month','2025-04')
    check(page,df[df.region.eq('North')&df.category.eq('Electronics')&df.month.eq('2025-04')])
    empty=None
    for region in sorted(df.region.unique()):
        for category in sorted(df.category.unique()):
            for month in sorted(df.month.unique()):
                if df[df.region.eq(region)&df.category.eq(category)&df.month.eq(month)].empty:
                    empty=(region,category,month);break
            if empty:break
        if empty:break
    assert empty is not None
    for key,value in zip(['region','category','month'],empty):select(page,key,value)
    check(page,df.iloc[:0])
    before=page.evaluate('window.renderVersion');page.click('#reset')
    page.wait_for_function('v => window.renderVersion > v',arg=before);check(page,df)
    page.set_viewport_size({'width':390,'height':844})
    page.evaluate("Promise.all(Array.from(document.querySelectorAll('.chart')).map(d=>Plotly.Plots.resize(d)))")
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    page.screenshot(path=str(root/'reports/dashboard_mobile.png'),full_page=True)
    assert not errors,errors
    browser.close()

checked=0
for md in root.rglob('*.md'):
    if '.git' in md.parts:continue
    for link in re.findall(r'\]\(([^)]+)\)',md.read_text()):
        if '://' in link or link.startswith('#'):continue
        assert (md.parent/link.split('#')[0]).exists(),(str(md),link)
        checked+=1
report={'status':'passed','viewports':[[1440,1000],[390,844]],'local_links_checked':checked,
 'checks':['Full-data and filtered KPI/Pandas agreement','Plotted product profit agreement',
 'Region/category/month filters','Empty selection and reset','Five charts','No page errors','No horizontal overflow at phone width'],
 'limits':['No human visual signoff','Native Power BI and desktop Excel rendering not tested']}
(root/'reports/browser_validation.json').write_text(json.dumps(report,indent=2))
v=json.loads((root/'reports/validation.json').read_text());v['checks']+=report['checks']
v['not_validated']=['Native Power BI PBIX','Desktop Excel rendering','Human visual signoff of browser screenshots']
(root/'reports/validation.json').write_text(json.dumps(v,indent=2))
files=[p for p in sorted(root.rglob('*')) if p.is_file() and not any(s in {'.git','.venv','__pycache__','dist'} for s in p.relative_to(root).parts) and p.name!='manifest.json']
manifest={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(root/'reports/manifest.json').write_text(json.dumps(manifest,indent=2))
with zipfile.ZipFile(root/'dist/retail-analytics.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in files+[root/'reports/manifest.json']:z.write(p,str(p.relative_to(root)))
print(json.dumps(report,indent=2))
