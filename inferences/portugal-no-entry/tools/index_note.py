#!/usr/bin/env python3
"""Build the overview note «Índice - Portugal no entry» from results/*.json.

    python3 tools/index_note.py
"""

from __future__ import annotations

import json
import os
from datetime import date

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(HERE, "tools")
RESULTS = os.path.join(HERE, "results")

CONF_ORDER = {"alta": 0, "média": 1, "baixa": 2, "nenhuma": 3}


def main() -> int:
    packets = json.load(open(os.path.join(TOOLS, "packets.json"), encoding="utf-8"))
    rows = []
    for fn in sorted(os.listdir(RESULTS)):
        if not fn.endswith(".json") or fn.startswith("_"):
            continue
        pid = fn[:-5]
        res = json.load(open(os.path.join(RESULTS, fn), encoding="utf-8"))
        p = packets.get(pid, {})
        sug = (p.get("obsidian_rows", [{}])[0].get("suggestion") or "").strip()
        lugar = res.get("lugar")
        conf = (res.get("confianca") or "nenhuma").strip().lower()
        rows.append(
            dict(
                pid=pid,
                name=p.get("name") or res.get("name") or pid,
                deh=p.get("dehergne_no"),
                entrada=p.get("current_jesuita_entrada", [{}])[0].get("d") if p.get("current_jesuita_entrada") else "",
                sug=sug,
                lugar=lugar or "— não determinado —",
                data=res.get("data") or "—",
                conf=conf,
                validacao=res.get("validacao") or "",
                tem_sug=bool(sug),
            )
        )
    rows.sort(key=lambda r: (CONF_ORDER.get(r["conf"], 9), r["name"]))

    n = len(rows)
    n_alta = sum(1 for r in rows if r["conf"] == "alta")
    n_media = sum(1 for r in rows if r["conf"] == "média")
    n_baixa = sum(1 for r in rows if r["conf"] == "baixa")
    n_none = sum(1 for r in rows if r["conf"] == "nenhuma")
    n_sug = sum(1 for r in rows if r["tem_sug"])
    n_sug_ok = sum(1 for r in rows if r["tem_sug"] and r["lugar"] != "— não determinado —")
    lugares: dict[str, int] = {}
    for r in rows:
        if r["lugar"] != "— não determinado —":
            key = r["lugar"].split("(")[0].strip()
            lugares[key] = lugares.get(key, 0) + 1

    out: list[str] = []
    out.append("---")
    out.append("title: Índice - Portugal no entry")
    out.append(f"created: {date.today().isoformat()}")
    out.append("tags: [dehergne, jesuita-entrada, portugal, china, indice]")
    out.append('source: "[[0 Portugal no entry]]"')
    out.append("---")
    out.append("")
    out.append("# Portugal no entry — lugar de entrada na Companhia")
    out.append("")
    out.append(
        "Notas de inferência para os missionários portugueses da China cujo "
        "`jesuita-entrada` o Dehergne deixou sem lugar. Uma nota por pessoa "
        "(esta pasta), com a proposta de lugar, a data, o grau de confiança e as "
        "referências (pha e Obsidian)."
    )
    out.append("")
    out.append("## Resumo")
    out.append("")
    out.append(f"- pessoas tratadas: **{n}**")
    out.append(f"- lugar proposto com confiança **alta**: **{n_alta}** · **média**: **{n_media}** · **baixa**: **{n_baixa}** · **não determinado**: **{n_none}**")
    out.append(f"- vinham com sugestão na tabela [[0 Portugal no entry]]: **{n_sug}** (das quais **{n_sug_ok}** ficaram com lugar fundamentado)")
    out.append("")
    if lugares:
        out.append("### Lugares propostos")
        out.append("")
        out.append("| lugar | nº de pessoas |")
        out.append("|---|---:|")
        for k, v in sorted(lugares.items(), key=lambda kv: (-kv[1], kv[0])):
            out.append(f"| {k} | {v} |")
        out.append("")

    out.append("## Achados transversais")
    out.append("")
    out.append("- **Um só noviciado, 1619-1630.** Franco, *Imagem da virtude… Coimbra* I (doc 54), p. 25: em 1619 cessaram os noviciados de Coimbra e Évora e todos os noviços da província foram reunidos na **Casa de Provação do Monte Olivete, em Lisboa**, até Abril de 1630. Qualquer entrada portuguesa nesse intervalo é de Lisboa — nunca Coimbra ou Évora. Isto corrige as sugestões «Coimbra/Évora» de vários casos (Roboredo, Luís da Gama, José Estêvão de Almeida, Francisco Pereira).")
    out.append("- **Noviciado do Oriente (Arroios, Lisboa), 1735-1759.** O catálogo de 1737 do noviciado (ARSI Lus. 48, f. 168), transcrito por Francisco Rodrigues, *História da Companhia de Jesus na Assistência de Portugal* t. IV/1 (doc 64), pp. 163-167 e 197, dá os noviços com o dia da entrada — foi assim que Bartolomeu de Azevedo e Xavier Duarte ficaram provados.")
    out.append("- **Registo de entrantes da província, 1711-1758 (BNP, Pombalina 231).** O «Catalogo dos Sogeitos, que entrarão em a Comp.ª de Jesus na Provincia de Portugal» (<https://purl.pt/47525>) dá, para cada entrada, «Entrou no Noviciado de Coimbra / Évora / Lx.ª … aos …». Fechou 9 casos deste lote, incluindo **Félix da Rocha — Lisboa, 1 de Maio de 1728**, o caso que motivou o trabalho. Está ordenado por primeiro nome; exclui os noviços de Arroios. Ver `results/NOTA-imagens-registo-BNP.md`.")
    out.append("- **Santo Antão = colégio de Lisboa** (não a ilha de Cabo Verde, nem Coimbra). Em vários casos «Santo Antão» era a casa de residência/estudos, não o noviciado.")
    out.append("- **Limite das fontes.** O pha não tem catálogos portugueses depois de 1625. As digitalizações ARSI em disco cobrem Lus. 39 (1579-1623), 43 II (1540-1578), 44 I (1587-1611), 44 II (1614-1655), 45 (1649-1675), 46 (1678-1696), 46a (1700) e 47 (1700-1720) — **faltam o Lus. 48 (1726-1745) e as folhas 253-349 do Lus. 47**, que são decisivos para muitos casos de 1707-1740 que ficaram por determinar.")
    out.append("- **Onde se prova o lugar:** só nas listas de noviços («Novitii», «Novitii Scholastici», «Fratres Novitii») dentro da secção de cada casa, ou numa vida de Franco / notícia de Pfister ou Backer-Sommervogel que diga «entrou no noviciado de …». Os catálogos trienais dão a **data** e os «anni Societatis», nunca a casa.")
    out.append("")
    out.append("## Discrepâncias e erros encontrados (para revisão no projecto)")
    out.append("")
    out.append("- **`deh-luis-da-gama`** — a transcrição pha de doc 28, p. 20 (ARSI Lus. 44 II, f. 415v) lia «Luiz da Sylva», «Arcebispado de Braga»; **corrigida em 2026-10-22** (`pha review` → `pha edit` → `pha reindex`) para «Luiz da Gama … Arcebispado de Évora». Fica a rever a leitura «Laure» por «Lavre».")
    out.append("- **`deh-manuel-de-azevedo`** — o ano na BD/`.cli` (`15870000`) é gralha por **1597**; o noviciado de Lisboa deu-lhe entrada a 10 de Maio de 1597 (ARSI Lus. 44 I, f. 116). A sugestão «Évora 1611» é a residência/profissão, não a entrada.")
    out.append("- **`deh-antonio-rodrigues`** — a base tem entrada em 1567 (identificação alternativa de Dehergne, nascido em Lisboa); o homem da ficha (Montemor-o-Novo) entrou em **Évora a 18 de Fevereiro de 1571** (Franco, Évora, doc 52, p. 674; *Documenta Indica* XII).")
    out.append("- **`deh-baltasar-diego-da-rocha`** — entrada em **16 de Fevereiro de 1650** (Franco e Pfister), não 1649.")
    out.append("- **`deh-aleixo-coelho`** — entrada em **20 de Novembro de 1643** (Franco, Évora), não 1645.")
    out.append("- **`deh-pedro-de-francisco`** — entrada **c. 1581**, não 1588 (catálogo de Coimbra de 1587: «cinco anos e meio» de Companhia).")
    out.append("- **`deh-manuel-camello`** — entrada em **28 de Maio de 1699** (catálogo de 1700), não 1700.")
    out.append("- **`deh-luis-de-moura`** — a tabela Obsidian tem `jesuita-entrada.date` = 1735; a BD e o texto de Dehergne dizem **1635**.")
    out.append("- **`deh-jeronimo-rodrigues-senior`** — a sugestão «Évora 1585» da tabela não se confirma: o noviço de Monforte está na secção de **Coimbra** dos catálogos de 1586-1587.")
    out.append("- **`deh-joao-nunes`** — as duas hipóteses são **duas pessoas distintas**, ambas documentadas (o professo de Montemor-o-Velho e o escolar de Lisboa); o missionário da China é o segundo, e o lugar de entrada não está declarado em nenhum fólio.")
    out.append("")

    out.append("## Tabela geral")
    out.append("")
    out.append("| id | nome | Dehergne | sugestão da tabela | **lugar proposto** | data | confiança |")
    out.append("|---|---|---|---|---|---|---|")
    for r in rows:
        pid = r["pid"]
        out.append(
            f"| [[{pid}]] | {r['name']} | {r['deh']} | {r['sug'] or '—'} | **{r['lugar']}** | {r['data']} | {r['conf']} |"
        )
    out.append("")
    out.append("## Casos não determinados")
    out.append("")
    pend = [r for r in rows if r["lugar"] == "— não determinado —"]
    if pend:
        for r in pend:
            out.append(f"- [[{r['pid']}]] — {r['name']} (entrada {r['entrada'] or '?'}): ver a nota para o que foi procurado e o que falta.")
    else:
        out.append("_nenhum._")
    out.append("")
    out.append("## Referências")
    out.append("")
    out.append("- [[0 Portugal no entry]] — tabela de partida (ids, nomes, embarques e sugestões).")
    out.append("- [[Coimbra Entry Changes]] — alterações ao `jesuita-entrada` feitas com prova de catálogo antes deste trabalho.")
    out.append("- Notas pha citadas em cada ficha: *Documenta Indica* (docs 19, 68-92), *Documentação para a história das missões do padroado português do Oriente* (docs 17, 20-26, 38-41), Franco, *Imagem da virtude* (docs 52-55), Pfister (docs 47, 50), Wicki (doc 66), Dehergne (doc 65), e os catálogos jesuítas digitalizados (docs 1, 2, 4, 27-37).")
    out.append("- Digitalizações ARSI *Lusitania* (LUS 39, 43 II, 44 I-II, 45-47) lidas em imagem: ver `tools/RECIPE.md`, §2 bis.")
    out.append("")
    path = os.path.join(HERE, "Índice - Portugal no entry.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"wrote {path}: {n} people ({n_alta} alta, {n_media} média, {n_baixa} baixa, {n_none} não determinado)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
