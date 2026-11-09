# Handover — «Portugal in China»

**Data:** 2026-11-07 · **Sessão:** DeepSeek Harness · **Objectivo deste ficheiro:** permitir recomeçar este trabalho noutra sessão, sem depender do histórico da conversa.

## TL;DR

- **Pergunta:** dos missionários portugueses do *Répertoire* de Dehergne, quantos **estiveram efectivamente na China** (excluindo os que morreram a caminho ou que apenas estavam destinados à China)?
- **Resposta:** **246 de 346** (189 com pelo menos um lugar na China continental + 57 só Macau). 100 excluídos.
- **Entradas na Companhia** (dos 246): Coimbra 57 · Lisboa 26 · Évora 19 · Goa 12 · Macau 3 · Japão 2 · Ormuz 1 · Índia 1; **104** com lugar `?` e **21** sem atributo `jesuita-entrada`. Ver a folha `entry_distribution`.
- **Fonte de verdade:** `portugal_china.xlsx` (folhas descritas abaixo) + `build_portugal_china.py` (regenera tudo a partir da base de dados).
- **Estado:** análise fechada e reproduzível; pendente apenas a decisão sobre os 13 casos da folha `review` e a importação dos veredictos do projecto «Portugal no entry».

## 1. Como foi feito (método)

Lido `AGENTS.md`. A base SQLite do projecto foi aberta **directamente com timelink** (não é preciso o Kleio server/Docker):

```python
from timelink.api.database import TimelinkDatabase
db = TimelinkDatabase(db_name="dehergne_repertoire_mbook_air", db_type="sqlite",
                      db_path="../database/sqlite")          # run from notebooks/
```

Passos (tudo em `build_portugal_china.py`):

1. **População:** 346 pessoas com `groupname='n'` e `nacionalidade='Portugal'` (`entities_with_attribute`).
2. **Atributos de presença:** `estadia, chegada, partida, morte, jesuita-votos-local,
   jesuita-ordenacao-padre, residencia, trajeto` (+ variantes `-x`). **Excluídos** `jesuita-entrada`,
   `baptizado`, `jesuita-fundador` (origem, não presença) e valores entre parênteses rectos
   (`[No mar, a caminho da China]` = morte na viagem, nunca «presença»).
3. **Lugar → país:** `extract_wikidata_id` (`notebooks/dehergne_util.py`) + cache
   `inferences/wikidata-references/locations_wikidata_info.xlsx` (`country_label`, P17).
   China = `People's Republic of China` (inclui Macau), `Qing dynasty`, `Ming dynasty`,
   `Republic of China`, `Yuan dynasty`. Topónimos chineses **sem Q-id** (`China`, `Cantão`, …)
   resolvidos por nome; valores entre `[ ]` nunca.
4. **Exclusão:** para os 100 sem lugar chinês, o `obs` do atributo `dehergne` (a notícia do
   Dehergne) foi usado para atribuir o motivo (ver folha `reasons`).

## 2. Resultado

| | pessoas |
|---|---:|
| missionários portugueses (`nacionalidade=Portugal`, `groupname='n'`) | 346 |
| **com presença documentada na China** | **246** |
| — com lugar na China continental | 189 |
| — só Macau | 57 |
| — com um único atributo de presença na China (evidência fina) | 63 |
| sem evidência de China (excluídos) | 100 |

Excluídos (folha `reasons`): 30 ficaram na Índia/Goa · 20 destinados mas sem prova de chegada · 18 morreram na viagem/em trânsito · 11 do lote de embarque 1755-58 sem estadia na China (presos/exilados na Europa) · 9 sem dados de lugar · 7 noutra missão asiática (Japão/Tonquim/Sião/Malaca) · 5 ficaram na Europa.

**Entradas na Companhia (246):** Coimbra 57 (23,2% de 246; **47,1% dos 121 com lugar de entrada conhecido**), Lisboa 26 (21,5%), Évora 19 (15,7%), Goa 12 (9,9%), Macau 3 (2,5%), Japão 2, Ormuz 1, Índia 1. Sem lugar: `?` 104 + sem atributo 21.

## 3. Ficheiros e folhas do livro

| ficheiro / folha | conteúdo |
|---|---|
| `portugal_china.xlsx` → `china_residents` | os **246**, com lugar(es) na China, datas, tipo de atributo, evidência linha a linha, `jesuita_entrada` |
| `…` → `excluded` | os **100**, com presença registada, país, lugar de morte, motivo e o `obs` do Dehergne |
| `…` → `review` | **13** excluídos cuja biografia sugere possível presença (homonímia/identificação incerta) |
| `…` → `reasons`, `summary` | contagens por motivo e indicadores gerais |
| `…` → `entry_distribution` | distribuição por lugar de entrada, com as duas bases (246 e 121) e a projecção pós-veredictos (186) |
| `…` → `notes` | definição de cada coluna e das duas populações (246 vs 121) |
| `build_portugal_china.py` | regenera o livro a partir da base (`~/venvs/timelink/bin/python`, correr a partir de `notebooks/`) |

## 4. Armadilhas e decisões (não repetir)

- **Os `.xlsx` antigos de `inferences/` estão desactualizados** (24 Out) face à base (1 Nov): `deh-jose-de-espinha`
  já tem `jesuita-entrada` (Lisboa, Arroios, 1739-06-04) e `joao-cardoso` foi renomeado para `deh-joao-cardoso`
  (por isso parecia faltar a nacionalidade). **Ler a base, não os xlsx.**
- **`entities_with_attribute(..., more_attributes=[...])` faz produto cartesiano:** um segundo `embarque`
  (ou `nascimento` duplicado) duplica linhas — o ficheiro antigo tinha 334 linhas para 307 pessoas (312 atributos).
  Contar sempre por id/`attr_id`.
- **`referido` dentro de uma entrada `n$` é sempre outra pessoa** — nunca conta para o `n` (mesmo com
  `obs="é provavelmente o mesmo"`); não há nenhum `rel$identification` que ligue os 12 casos homónimos.
- **38 missionários portugueses não têm `jesuita-entrada` nenhum** (26 sem nada no texto, 12 só em `referido`).
  Não confundir com os 104 (residentes) que têm entrada com lugar `?`.
- **Macau conta como China** (P17 = PRC). Se se quiser só China continental: 189. Só 57 são «só Macau».
- **Casos de entrada `?`:** os veredictos do projecto «Portugal no entry» estão em
  `inferences/portugal-no-entry/results/*.json`; para os 75 residentes desse lote de 110 propõem
  Coimbra 28 / Lisboa 26 / Évora 11 / indeterminado 10 — **ainda não importados** para a base.
  Se importados, Coimbra passa de 57 para 85 (45,7% de 186 com lugar conhecido).

## 5. Próximos passos possíveis

1. Decidir os **13 casos** de `review` (ler as fontes; vários são homónimos que o Dehergne não distingue).
2. Importar os veredictos de «Portugal no entry» (editar `results/*.json` → `assemble.py`/`index_note.py`
   no projecto irmão, depois `pha edit`/`reindex` ou re-import dos `.cli`) e regenerar este livro.
3. Opcional: distribuição por **lugar de estadia** na China (Pequim, Cantão, Macau, Fukien, Kiangsi, …) —
   está tudo na coluna `evidence` de `china_residents`.
4. Opcional: escrever os 246 num CSV/Nomisma para uso externo.

## 6. Ligações

- `AGENTS.md` (repositório) — regras, como abrir a base com timelink, ambiente `~/venvs/timelink`.
- `notebooks/dehergne_util.py` — `extract_wikidata_id`, `locations_wikidata_info_file`.
- `notebooks/people-by-country.ipynb` — a mesma lógica país↔Wikidata, generalizada a qualquer país.
- `inferences/portugal-no-entry/` — o projecto de investigação do lugar de entrada dos 110 casos portugueses.
