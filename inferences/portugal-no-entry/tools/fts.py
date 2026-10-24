#!/usr/bin/env python3
"""FTS search helper: python3 tools/fts.py "phrase" ["phrase2" ...] [--docs=1,2,28] [--limit=N]"""
import sqlite3,sys,re,argparse
DB='/Users/jrc/jesuit-archive/archive.db'
ap=argparse.ArgumentParser()
ap.add_argument('phrases',nargs='+')
ap.add_argument('--docs')
ap.add_argument('--limit',type=int,default=20)
ap.add_argument('--ctx',type=int,default=220)
ap.add_argument('--raw',action='store_true')
a=ap.parse_args()
c=sqlite3.connect(f'file:{DB}?mode=ro&immutable=1',uri=True); c.row_factory=sqlite3.Row
docf=''
params=[]
if a.docs:
    ids=[int(x) for x in a.docs.split(',')]
    docf=' and d.id in (%s)'%','.join('?'*len(ids))
for ph in a.phrases:
    print("="*72); print("PHRASE:",ph)
    q=f"""select d.id doc,d.filename fn,p.page_no pg,d.page_count pc,ch.variant var,ch.text txt
      from chunks_fts f join chunks ch on ch.id=f.rowid
      join pages p on p.id=ch.page_id join documents d on d.id=ch.document_id
      where chunks_fts match ? {docf} order by rank limit 400"""
    try: rows=c.execute(q,[f'"{ph}"']+([int(x) for x in a.docs.split(',')] if a.docs else [])).fetchall()
    except Exception as e: print("  FTS error",e); continue
    n=0
    for r in rows:
        if not a.raw and r['var']!='edited': continue
        m=re.search(re.escape(ph),r['txt'],re.I)
        if not m: continue
        s=max(0,m.start()-a.ctx); e=min(len(r['txt']),m.end()+a.ctx)
        print(f"-- doc {r['doc']} {r['fn'][:45]} p.{r['pg']}/{r['pc']} [{r['var']}]")
        print("   ",r['txt'][s:e].replace("\n"," "))
        n+=1
        if n>=a.limit: break
    if n==0: print("   (no hits)")
