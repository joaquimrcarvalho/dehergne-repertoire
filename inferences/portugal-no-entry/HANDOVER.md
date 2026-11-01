# Handover — «Portugal no entry»

**Data:** 2026-11-01 · **Sessão:** DeepSeek Harness (lead + subagentes) · **Objectivo deste ficheiro:** permitir recomeçar o trabalho noutra sessão, sem depender do histórico da conversa.

## TL;DR

- **Tarefa:** determinar o **lugar de entrada na Companhia** (atributo Timelink `jesuita-entrada`) dos **110 missionários portugueses da China** a quem o Dehergne deixa `E. <ano>` **sem lugar**.
- **Estado:** **110 tratados — 37 confiança alta · 33 média · 10 baixa · 30 não determinados.**
- **Fonte de verdade:** esta pasta — `results/<id>.json` (uma ficha por pessoa), 110 notas `deh-<id>.md` geradas a partir delas, `tools/` (pipeline) e `Índice - Portugal no entry.md` (gerado).
- **Cópia de leitura:** vault `04 Biographies/dehergne/portugal_noentry/` — **gerada** por `tools/vault_copy.py`; não editar à mão lá.
- **Próximo passo:** atacar os **30 em aberto** pela ordem da tabela §7 (começar por **1649 T1** — João de Abreu / João Couceiro; depois **1651/1654** — Diogo de Sotomaior / Manuel Pinto II; **1678 T1** — André da Costa / António Simões; etc.).

## 1. Contexto

O Dehergne, *Répertoire des Jésuites de Chine* (1973), regista para estes missionários a entrada (`E.`) sem lugar. A tabela Obsidian «0 Portugal no entry» acrescentou, num primeiro passo manual, um lugar provisório depois de 37 nomes. O projecto: **validar essas sugestões e resolver as restantes**, com prova documental (catálogos ARSI, registo BNP, pha), uma nota por pessoa e confiança graduada.

Casas de formação mais frequentes: **Coimbra** (Real Colégio de Jesus / noviciado), **Lisboa** (Casa de S. Roque, Colégio de Santo Antão e a **Casa de Provação do Monte Olivete** — «Santo Antão» é o colégio de Lisboa, não a ilha de Cabo Verde), **Évora**, **Braga**, **Bragança**, **Porto**; e, para quem entrou já no Oriente, **Goa** ou **Macau**.

## 2. Mapa dos ficheiros e sítios

| O quê | Onde |
|---|---|
| Fichas de resultado (fonte de verdade) | `results/<id>.json` (110) |
| Notas geradas | `deh-<id>.md` (110) + `Índice - Portugal no entry.md` |
| Pipeline e método | `tools/` — `RECIPE.md`, `assemble.py`, `index_note.py`, `vault_copy.py`, `packet.py`, `hints.py`, `pha_research.py`, `read_page.py`, `fts.py`, `packets.json` |
| Cópia no vault | `~/jrc-notes/04 Biographies/dehergne/portugal_noentry/` (114 ficheiros; front matter `source_note`/`source_repo`/`copied`; comandos `pha page` convertidos em links vivos) |
| Tabela de trabalho (bandeiras 🟢/🟡/🔴) | vault `04 Biographies/dehergne/portugal_noentry/0 Portugal no entry.md` |
| Nota de tarefa do quadro | vault `01 Notes/Portugal-no-entry.md` (com `status`/`next`/`log`; aparece em [[Agents - tasks - ongoing]]) |
| Relatório de fólios em falta | vault `01 Notes/ARSI Lusitania - fólios em falta - Portugal no entry.md`; cópia canónica em `~/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19/INDICE-folios-em-falta-Portugal-no-entry.md` |
| Digitalizações ARSI (iCloud) | `~/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19/` — índice cronológico em `INDICE-cronologico.md` (270 catálogos, 1548‑1795, com tipo/volume/fólios) |
| pha (arquivo digital) | `~/jesuit-archive`; viewer `http://127.0.0.1:8765/doc/<slug>/p<NNN>` (página com 3 dígitos) |

⚠️ **O directório `~/mhk-home/sources/dehergne` é hoje um stub** (só `extras/ARSI-catalogs-indexes`). O repositório vivo é **este**: `~/develop/dehergne-repertoire-mbook-air` (git, branch `main`); existe um gémeo em `~/develop/dehergne-repertoire`.

## 3. Pipeline — comandos

```bash
cd /Users/jrc/develop/dehergne-repertoire-mbook-air/inferences/portugal-no-entry

python3 tools/packet.py <id> [<id> ...]      # packet: notícia Dehergne + cronologia + linha da tabela
python3 tools/packet.py --list               # lista das 110 pessoas
python3 tools/assemble.py <id> [<id> ...]    # (re)gera deh-<id>.md a partir de results/<id>.json
python3 tools/index_note.py                  # (re)gera «Índice - Portugal no entry.md»
python3 tools/vault_copy.py --check          # simula a cópia para o vault
python3 tools/vault_copy.py                  # copia notas + índice para o vault (precisa de acesso ao vault)
```

Fluxo de fecho de um caso: **editar `results/<id>.json`** → `assemble.py <id>` → `index_note.py` → `vault_copy.py` → registar no `log` da nota de tarefa.

## 4. Esquema de `results/<id>.json`

Chaves: `id`, `name`, `lugar`, `data`, `confianca` (`alta|média|baixa|nenhuma`), `sugestao_tabela`, `validacao`, `resumo`, `biografia`, `analise` (lista de `{titulo, texto}`), `evidencias` (lista de `{citacao, comando, o_que_prova, forca}`), `nao_encontrado`, `refs_obsidian`.

Nas `evidencias`, `comando` é normalmente `open "<imagem ARSI>"` e/ou `pha page <doc> <página> --edited` — o `vault_copy.py` transforma os comandos `pha page` em links do viewer.

## 5. Método (resumo operativo)

1. **Dehergne** (pha doc 65): `E.` ano, cote (`Lus. xx, ff.`), alias, naturalidade, embarque.
2. **Wicki** *Liste der Jesuiten-Indienfahrer* (pha doc 66): data de partida — útil para fixar cronologia, não a casa.
3. **Pfister** (pha docs 47/50) e **Documenta Indica** (docs 19, 68‑92): biografia e, na DI, catálogos de casas indianas (entradas em Goa).
4. **Catálogo do ano da entrada (ou +1)** — localizar em `INDICE-cronologico.md`; ler o assento e **ler para trás até ao cabeçalho da casa** (limite prático ~50 páginas).
5. **Residência ≠ noviciado.** Um catálogo de casa a N anos da entrada prova a residência. Para valer como casa de entrada: (a) a pessoa tem poucos anos de Companhia, e (b) a casa é de noviciado.
6. **Regra do noviciado único:** de 1619 a Abril de 1630 todos os noviços da província estavam na **Casa de Provação do Monte Olivete (Lisboa)** (Franco, doc 54, p. 25). Qualquer entrada nesse intervalo ⇒ **Lisboa**.
7. **T6/T7** são suplementos dos entrados no ano — mas **confirmar o conteúdo do fólio** (ver armadilhas).
8. **Confiança:** `alta` = registo de noviciado ou declaração explícita; `média` = residência na casa de noviciado poucos anos depois; `baixa` = inferência estrutural; `nenhuma` = não estabelecido (registar os fólios negativos).

## 6. Armadilhas conhecidas (não repetir)

- **«Não está no pha» ≠ «não existe».** Os catálogos ARSI estão em disco (iCloud), fora do pha. Foi este erro que gerou o relatório de fólios errado (Lus. 44 II ff. 350‑440 existem).
- **iCloud:** as imagens podem estar «paginadas»; aquecer antes de ler com `cat "<ficheiro>" > /dev/null` (o `brctl` não corre no sandbox). Depois a leitura é rápida.
- **Lus. 41** = *Catalogus Assistentiae* de **1768** (422 imagens, +41a/+41b): dá a data de entrada e a residência 30+ anos depois — **não** a casa do noviciado.
- **pha doc 157** = registo impresso 1711‑1758, mas **só A‑E** (n.os 1‑351). O F‑J impresso não está no pha; o M‑Z não existe nos scans; a única cópia completa é o **BNP Pombalina 231** (<https://purl.pt/47525>), a que **falta o f. 106v** (maio de 1734).
- **Cabeçalhos:** «Collegium Conimbricense» ≠ «Missio Conimbricense» (Lus. 47 f. 120) — **ampliar e confirmar** o cabeçalho antes de o transcrever.
- **Numeração:** a imagem, o fólio impresso e o fólio antigo divergem (ex.: imagem `419.jpg` = f. 419v actual = f. 219v antigo = p. 420 impressa). Confirmar sempre pelo número impresso na página.
- **Notas `catalogos/*.md` do projecto**: só **duas** têm transcrição nominal (1617 e 1566); as restantes são galerias de imagens.
- **T6 enganadores:** o «T6» de 1678 (Lus. 46 f. 22) é o *Supplementa* com os «Excierunt» (saídas), não entrantes; o «T6» de 1700 (Lus. 47 f. 1) é o *Catalogus Missionariorum* 1696‑1700 (partidas para a Índia).
- **O «T1 1651» (Lus. 45 ff. 57‑64v) é o caderno trans‑tagano** («Pro Domo & Collegiis Transtaganis»), não a província inteira.
- **Erros já corrigidos (não reverter):** doc 28 p. 20 (Luís da Gama → «Luiz da Gama … Évora»); Zuzarte (Abrantes/Guarda em 1636, «de Lx.ª» em 1639, Loures em Dehergne); «Missio» → «Collegium» em Lus. 47 f. 120; Lus. 41 disponível; ff. 350‑440 do Lus. 44 II existem.

## 7. Os 30 em aberto (ordem de ataque)

| Entrada | Pessoa | Próximo catálogo a ler | Estado |
|---|---|---|---|
| 1624 | Inácio Lobo | 1625 T1 | verificado: **ausente** (só Luís Lobo); Dehergne diz que saiu da Companhia — provável impossibilidade |
| 1630 | Manoel Soares | 1633 T1 | a ler |
| 1635 | Luís de Moura | 1636 T1 | a ler |
| 1647 | Manuel Carvalho I | 1649 T1 | a ler |
| 1648 | João de Abreu | 1651 trans‑tagano | **lido**: Lus. 45 f. 61v n.º 99 — estudante de filosofia, 2,5 anos; residência |
| 1649 | João Couceiro | cote *Lus. 45, 180* (caderno de 1655) | não localizado no f. 180; ver f. 179‑181 e variantes Couceiro/Couceyro/Coceiro |
| 1651 | Diogo de Sotomaior | 1654/1655 T1 | a ler (o «1651 T1» é trans‑tagano) |
| 1652 | Manuel Pinto II | 1654 T1/T4 | a ler |
| 1663 | João Fernandes Fou | 1665 T1 | a ler |
| 1666 | Francisco Simões | 1669 T1 | a ler |
| 1673 | José Soares | 1675 T1 | a ler |
| 1675 | Simão Pinto | 1675 T1 | a ler |
| 1678 | André da Costa | 1678 T1 (não o f. 22) | a ler |
| 1678 | António Simões I | 1678 T1 (não o f. 22) | a ler |
| 1685 | António Freire | 1685 T1 | a ler |
| 1686 | Francisco Barbosa | 1690 T1 | a ler |
| 1690 | Félix‑José Pereira | 1690 T1 | a ler |
| 1690 | João Duarte | 1690 T1 | a ler |
| 1692 | João Francisco Cardoso | 1693 T1 | a ler |
| 1693 | Manuel Marques | 1693 T1 | a ler |
| 1693 | Manuel Teles | 1693 T1 | a ler |
| 1694 | Manuel de Sousa | 1696 T1 | a ler |
| 1699 | Teotónio Leitão | 1700 T1 | a ler |
| 1700 | Manuel Ribeiro júnior | 1700 T1 | a ler |
| 1707 | André Pereira | 1711 T1 (Lus. 47 ff. 118‑151) | a ler |
| 1709 | Luís de Sequeira | 1711 T1 | a ler |
| 1710 | Francisco Alberto | 1711 T1 | a ler |
| 1727 | João de Seixas | BNP 231 / Lus. 48 | bloqueado (Lus. 48 ausente; J do BNP lido sem ele) |
| 1729 | Manuel José | BNP 231 / Lus. 48 | bloqueado (M do BNP lido sem ele) |
| 1734 | João Simões | BNP 231 (falta f. 106v) / Lus. 48 | bloqueado |

## 8. Como recomeçar (passo a passo)

1. `cd /Users/jrc/develop/dehergne-repertoire-mbook-air && git status` (branch `main`; há alterações locais em `.kleio.json`).
2. Ler `tools/RECIPE.md` (método detalhado e variantes de nomes).
3. Escolher o próximo caso da tabela §7 e abrir `results/<id>.json` + `tools/packet.py <id>`.
4. Localizar o catálogo em `INDICE-cronologico.md`, aquecer as imagens e ler (assento → cabeçalho da casa).
5. Actualizar o JSON (lugar, data, confiança, evidência com fólio/página, análise, não encontrado) e correr o pipeline (§3).
6. Actualizar o `log` da nota de tarefa (`01 Notes/Portugal-no-entry.md`) e, se o estado mudar, este handover.
7. Manutenção: se o repositório mudar de sítio, actualizar o `path` na nota de tarefa e o `source_repo` no front matter das cópias do vault (`tools/vault_copy.py`).

## 9. Histórico resumido

- **2026-10-16** — relatório de fólios em falta; primeira cópia das notas para o vault.
- **2026-10-19** — criação das 110 notas, `results/`, índice e ferramentas.
- **2026-10-22** — Lus. 41 esclarecido; pha doc 157 (A‑E); correcção da transcrição de doc 28 p. 20.
- **2026-10-23** — índice cronológico dos 270 catálogos; lista dos casos com «look‑back»; verificações Caetano Lopes, Zuzarte (1636/1639), Lucas Correa (1633, f. 490v).
- **2026-10-24/25** — Inácio da Costa = Inácio Nunes (1625 f. 419v n.º 288) ⇒ Lisboa (Monte Olivete); Lucas Correa revisto para Lisboa; estado fixado em 37/33/10/30.
- **2026-11-01** — nota de tarefa preenchida e movida para `01 Notes`; este handover criado.

## 10. Ligações úteis

- Viewer pha: `http://127.0.0.1:8765/doc/<slug>/p<NNN>`; exemplos: Dehergne `reference-works-joseph-dehergne-1973-repertoire-des-jesuites-de-chine-de-1542-a-1800`, Wicki `reference-works-wicki-liste-jesuiten-indienfahrer-1967`, Pfister `pfister-notices-notices-biographiques-et-bibliographiques-sur-pfister-louis-t1` (e `-t2`), François `franco-imagens-franco-imagem-virtude-coimbra-1719-v1`, catálogo 1625 `jesuit-catalogues-jesuit-cat-type1-portugal-1625-t1-lus-44ii-410`.
- BNP Pombalina 231: <https://purl.pt/47525>.
- Índice cronológico dos catálogos: `.../v2-2025-01-19/INDICE-cronologico.md` (e `.html`).
- Nota de tarefa: `01 Notes/Portugal-no-entry.md` (quadro de tarefas).
- Relatório de fólios: `01 Notes/ARSI Lusitania - fólios em falta - Portugal no entry.md`.
- Nota de método: `Determining college or noviciate from catalog reference 2026-10-19.md`.
- Inventário dos catálogos da Documenta Indica: `01 Notes/Documenta Indica - catálogos.md`.
