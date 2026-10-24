# TGAZ (CHGIS) check of the iloc-issues

Working directory for the CHGIS **Temporal Gazetteer (TGAZ)** verification of
the 34 location-identification issues in `../` and the 24 comment drafts in
`../comments/`.

Start with:

* **[../TGAZ-RESOLUTION.md](../TGAZ-RESOLUTION.md)** — consolidated report:
  method, verdict for every issue, notable findings, caveats.
* **[PROTOCOL.md](PROTOCOL.md)** — how the check was done: what TGAZ covers,
  query strategy, verdict vocabulary, section/JSON conventions.
* **Each issue file** (`../NN-*.md`) and **each comment draft**
  (`../comments/*.md`) carries a `## TGAZ (CHGIS) check` section with the exact
  queries run and the evidence.
* **[../comments/TGAZ-COMMENTS.md](../comments/TGAZ-COMMENTS.md)** — the same
  report for the comment drafts (GitHub issues #2-#68).

Tooling (standard library only; plain `python3` works):

```bash
python3 tgaz_tool.py query "呂家莊"            # search TGAZ
python3 tgaz_tool.py get hvd_135137 --full     # canonical record
python3 tgaz_tool.py wd Q1015480               # Wikidata labels + P625
python3 tgaz_tool.py dist 37.94665 115.43684 37.94231 115.21181
python3 replay.py --limit 10                   # re-run recorded queries
python3 build_report.py                        # rebuild the main report
python3 build_comments.py                      # comment drafts: queries + sections
python3 build_comments_report.py               # rebuild the comments report
```

Data:

* `data/<NN>.json` — per-issue evidence record (queries, hits, best match,
  Wikidata anchor, distance, verdict);
* `comments-data/<GH>.json` — the same for the 24 comment drafts in
  `../comments/` (GitHub issues #2-#68); report:
  `../comments/TGAZ-COMMENTS.md`;
* `tgaz-results.csv` — one row per issue (generated);
* `comments-results.csv` — one row per comment draft (generated);
* `comments-query-log.json` — queries of the comments pass, for replay;
* `query-log.json` — all 226 recorded queries of the main pass, for replay (generated);
* `HIGHLIGHTS.md` — hand-written analysis included in the main report;
* `HIGHLIGHTS-COMMENTS.md` — analysis included in the comments report.

The CHGIS TGAZ service: <https://chgis.hudci.org/tgaz> (docs
<https://chgis.hudci.org/tgw/#usage>). The project's general TGAZ client and
notebook live in `notebooks/dehergne_util.py` and `notebooks/chgis-tgaz.ipynb`.
