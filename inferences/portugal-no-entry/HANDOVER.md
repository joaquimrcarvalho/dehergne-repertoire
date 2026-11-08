# Handover — «Portugal no entry»

**Data:** 2026-11-01 · **Sessão:** DeepSeek Harness (lead + subagentes) · **Objectivo deste ficheiro:** permitir recomeçar o trabalho noutra sessão, sem depender do histórico da conversa.

## TL;DR

- **Tarefa:** determinar o **lugar de entrada na Companhia** (atributo Timelink `jesuita-entrada`) dos **110 missionários portugueses da China** a quem o Dehergne deixa `E. <ano>` **sem lugar**.
- **Estado:** ver contagem no `Índice - Portugal no entry.md` (actualizada a cada lote; última: 44 alta · 38 média · 14 baixa · 14 não determinados).
- **Fonte de verdade:** esta pasta — `results/<id>.json` (uma ficha por pessoa), 110 notas `deh-<id>.md` geradas a partir delas, `tools/` (pipeline) e `Índice - Portugal no entry.md` (gerado).
- **Cópia de leitura:** vault `04 Biographies/dehergne/portugal_noentry/` — **gerada** por `tools/vault_copy.py`; não editar à mão lá.
- **Estado do plano:** os **30 casos do §7 estão todos revistos** (2026‑11‑01): 24 com lugar atribuído (directo ou por inferência) e 10 sem lugar (Abreu, Inácio Lobo, António Simões I, Marques, Teles, Leitão, Ribeiro júnior + os três bloqueados de 1727‑1734). Próximo passo: rever/consolidar (ver abaixo) — deixou de haver casos «a ler».
- **Próximo passo (novo):** — revistos 1649 (Couceiro), 1651 (Sotomaior), 1652 (Pinto II), 1678 (Costa fechado, Simões em aberto), 1685‑1694 (Pereira e Cardoso fechados; Duarte, Sousa, Marques, Teles em aberto). Seguem-se os restantes (1630, 1635, 1647, 1663, 1666, 1673, 1675, 1685, 1686, 1699, 1700, 1707, 1709, 1710) e os três bloqueados de 1727‑1734. Já fechados em 1711: **Sequeira** (Lisboa, alta) e **Francisco Alberto** (Coimbra, alta); **André Pereira** ficou em Évora (inferido, baixa).

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
| Relatório de fólios em falta | vault `01 Notes/ARSI Lusitania - fólios em falta - Portugal no entry.md`; cópia canónica em `/Volumes/ARSI/ARSI Lusitania/INDICE-folios-em-falta-Portugal-no-entry.md` |
| Digitalizações ARSI (**SSD externo «ARSI»**, antes iCloud) | `/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/` — índice em `indexes/INDICE-cronologico.md` (274 catálogos, 1548‑1795, com tipo/volume/fólios); cópia antiga em `~/Library/Mobile Documents/com~apple~CloudDocs/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19/` (não é a de referência) |
| **Índice dos catálogos ARSI** (no SSD) | `/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/indexes/` — 274 catálogos, 12 volumes: `_data/LUS-NN.json` (fonte de verdade: ano, tipo, casa, fólios, nota, evidência, correcções), `INDICE-cronologico.md`, `INDICE-sistematico-por-volume.md`, `catalogos/<nota>.md` (com as imagens), `reports/` (por volume + `CORRECTIONS.md`), `tools/check_index.py`. Consultar com `python3 tools/arsi_index.py --year 1655` (ver `tools/RECIPE.md` §2 bis‑A) |
| Instruções do pacote de índice | `/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/AGENTS.md` — ler no início da sessão; regras em §6–§8 (nunca editar as imagens `LUS. NN/`, nunca inventar fólios, corrigir pelo circuito `CORRECTIONS.md` + `_data` + nota) |

⚠️ **O directório `~/mhk-home/sources/dehergne` é hoje um stub** (só `extras/ARSI-catalogs-indexes`). O repositório vivo é **este**: `~/develop/dehergne-repertoire-mbook-air` (git, branch `main`); existe um gémeo em `~/develop/dehergne-repertoire`.

## 3. Pipeline — comandos

```bash
cd /Users/jrc/develop/dehergne-repertoire-mbook-air/inferences/portugal-no-entry

python3 tools/packet.py <id> [<id> ...]      # packet: notícia Dehergne + cronologia + linha da tabela
python3 tools/packet.py --list               # lista das 110 pessoas
python3 tools/arsi_index.py --year 1655      # ÍNDICE ARSI: que catálogo em que fólios (--note, --gaps, --volume)
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

- **«Não está no pha» ≠ «não existe».** Os catálogos ARSI estão em disco (SSD «ARSI», `/Volumes/ARSI`), fora do pha. Foi este erro que gerou o relatório de fólios errado (Lus. 44 II ff. 350‑440 existem).
- **SSD «ARSI»:** desde 2026‑11 as digitalizações estão no **SSD externo «ARSI»** — `/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/`. **Não há paginação iCloud, logo não é preciso aquecer as imagens.** Se o volume não estiver montado, **montá‑lo** antes de ler: a ausência do volume não é prova de que o fólio não existe. A cópia antiga em iCloud ainda existe (mesmos nomes de ficheiro), mas já não se cita por ela; os `comando` dos JSON foram migrados para o caminho do SSD.
- **iCloud (legado):** nas cópias antigas as imagens podiam estar «paginadas»; aquecer com `cat "<ficheiro>" > /dev/null`. Só relevante se se voltar a ler a cópia iCloud.
- **Lus. 41** = *Catalogus Assistentiae* de **1768** (422 imagens, +41a/+41b): dá a data de entrada e a residência 30+ anos depois — **não** a casa do noviciado.
- **pha doc 157** = registo impresso 1711‑1758, mas **só A‑E** (n.os 1‑351). O F‑J impresso não está no pha; o M‑Z não existe nos scans; a única cópia completa é o **BNP Pombalina 231** (<https://purl.pt/47525>), a que **falta o f. 106v** (maio de 1734).
- **Cabeçalhos:** «Collegium Conimbricense» ≠ «Missio Conimbricense» (Lus. 47 f. 120) — **ampliar e confirmar** o cabeçalho antes de o transcrever.
- **Numeração:** a imagem, o fólio impresso e o fólio antigo divergem (ex.: imagem `419.jpg` = f. 419v actual = f. 219v antigo = p. 420 impressa). Confirmar sempre pelo número impresso na página.
- **Notas `catalogos/*.md` do projecto**: só **duas** têm transcrição nominal (1617 e 1566); as restantes são galerias de imagens.
- **O índice do pacote vem antes de tudo.** Já existe um índice completo das digitalizações — `indexes/` no SSD, com `AGENTS.md` próprio. `indexes/_data/LUS-NN.json` dá, por catálogo, ano/tipo/casa/fólios/nota/evidência; `indexes/catalogos/<nota>.md` traz as imagens. **Não voltar a ler os índices dactilografados à mão nem varrer fólios às cegas**: usar `python3 tools/arsi_index.py --year …` e só depois abrir as imagens. Ver `tools/RECIPE.md` §2 bis‑A.
- **Divisão por casas dentro de um catálogo** não está no `_data` (que dá o intervalo do catálogo): está no índice dactilografado do volume (`LUS. NN/000i*.jpg`) e nos relatórios `indexes/reports/LUS-NN.md`. Ex.: Lus. 45 — 1649: Domus Professa f. 8, Coimbra f. 10, Évora f. 13, Colégio de Lisboa f. 18, **Domus Probationis f. 20**, Porto f. 22; trans‑tagano de 1651: Évora f. 57, Vila Viçosa f. 62v, Faro f. 63, Portalegre f. 63v, Elvas f. 65v.
- **As listas de noviços podem ocupar DUAS páginas.** No catálogo de 1654 a lista «Novitij» do Colégio de Coimbra vai do f. 79 (nn. 161‑176) ao **f. 79v** (nn. 177‑191) — a sessão anterior leu só o recto e concluiu (mal) que Manuel Pinto II não estava nela. Ler sempre recto **e** verso até ao cabeçalho da casa seguinte.
- **O catálogo de 1696 (Lus. 46, imagens 314‑343v = fólios carimbados 319‑349) regista datas de entrada**: cada assento traz «**Ing.** <dia> <mês> <ano>» (ex.: «Ing. 4 Sept. 626»), ao contrário dos catálogos habituais. É a fonte provável das datas exactas que Dehergne dá para entrantes do século XVII — a explorar caso a caso (atenção ao desvio imagem↔fólio deste volume: +5/+6 no fim).
- **Lacunas declaradas no próprio índice** (checar antes de dizer «não existe»): LUS. 47 ff. 253‑349 não digitalizados; sem Catalogus II no LUS. 46 para 1693; sem Catalogus III no LUS. 47 para 1717; LUS. 43 sem índice dactilografado (segmentos inferidos ⚠️); LUS. 46a é variante do catálogo de 1700.
- **T6 enganadores:** o «T6» de 1678 (Lus. 46 f. 22) é o *Supplementa* com os «Excierunt» (saídas), não entrantes; o «T6» de 1700 (Lus. 47 f. 1) é o *Catalogus Missionariorum* 1696‑1700 (partidas para a Índia).
- **Regra do noviciado único em Lisboa, de Junho de 1685 ao fim de 1690** (António Franco, *Imagem da virtude… Évora*, doc 52, **p. 49-50**): em 1685 o Geral mandou reduzir «a hum só Noviciado de Lisboa os tres da Provincia» (Coimbra, Lisboa, Évora), com execução em Junho de 1685; «Persistio esta mudança … até o anno de 1690», e a **restituição dos noviciados a Coimbra e Évora começou a executar-se em Janeiro de 1691** («nella se persevera até o dia de hoje»). Logo: **entradas de Junho de 1685 a Dezembro de 1690 ⇒ Lisboa** (prova institucional, média se faltar a lista nominal); **a partir de 1691 voltou a haver três noviciados** e o lugar tem de vir das listas nominais (em 1711 há listas em Coimbra ff. 127v‑128, Évora f. 135 e Lisboa ff. 142v‑143v). Os catálogos de 1685/1686 confirmam a fase única (noviços só na Domus Probationis; Lus. 39, T4 de 1686, ff. 140‑143v).
- **O «T1 1651» (Lus. 45 ff. 57‑64v) é o caderno trans‑tagano** («Pro Domo & Collegiis Transtaganis»), não a província inteira.
- **Erros já corrigidos (não reverter):** doc 28 p. 20 (Luís da Gama → «Luiz da Gama … Évora»); Zuzarte (Abrantes/Guarda em 1636, «de Lx.ª» em 1639, Loures em Dehergne); «Missio» → «Collegium» em Lus. 47 f. 120; Lus. 41 disponível; ff. 350‑440 do Lus. 44 II existem.

## 7. Os casos em aberto (ordem de ataque)

Os fólios da coluna «Próximo catálogo a ler» vêm do índice do pacote (`indexes/_data`, ver §2 bis‑A e `tools/arsi_index.py`), não de estimativas. Atalho: `python3 tools/arsi_index.py --year 1678`.

| Entrada | Pessoa | Próximo catálogo a ler | Estado |
|---|---|---|---|
| 1624 | Inácio Lobo | 1625 T1 | verificado: **ausente** (só Luís Lobo); Dehergne diz que saiu da Companhia — provável impossibilidade |
| 1630 | Manoel Soares | 1633 T1 (Lus. 44 II ff. 481‑511) | **fechado (2026‑11‑01)**: «Fr. Manoel Soares de Póvoa, bispado de Portalegre, 19 anos, 3 de Companhia, humanista» (f. 500 n.º 426), no bloco de **Évora** (não Coimbra: Coimbra = n.º 162‑341 = os 180 do T3) ⇒ **Évora, média** (Évora tinha noviciado: «Irmãos noviços» n.º 460‑477; falta a lista de 1630‑32) |
| 1635 | Luís de Moura | 1636 T1 (Lus. 44 II ff. 529‑554) | **fechado (2026‑11‑01)**: «Fr. Luis de Moura, N. de Lx.ª, 20 anos, 10 meses de Companhia, coadjutor espiritual» (f. 535v n.º 135), na lista «Irmãos Nouiços» da «Casa da Prouaçaõ» ⇒ **Lisboa (Casa de Provação), alta** |
| 1647 | Manuel Carvalho I | 1649 T1 (Lus. 45 ff. 8‑28v) | **fechado (2026‑11‑01; leitura corrigida em 2026‑11‑07)**: «Fr. Emmanuel de Carvalho, Ulyssip., an. 16; Societ. Mens. 11» (f. 21 n.º 438 — o copista escreve o 11 numa forma que parece «ij»; a sequência da lista, 13‑12‑11, confirma-o), na lista «Novitij» da **Domus Probationis Ulyssiponensis** ⇒ **Lisboa (Casa de Provação), alta** |
| 1648 | João de Abreu | 1651 trans‑tagano (Lus. 45 f. 61v n.º 99) | **lido e corrigido (2026‑11‑07)**: «Fr. Ioannes d'Abreu Elvensis, annorum 17, vires mediocres, habet societatis annos duos cum dimidio, Rhetoricus» — o catálogo de 1651 é uma lista contínua por graus de estudo (sem casas), e a linha «Philosophus primi anni» pertence ao n.º 89 (não é secção). Confirmados Elvas, 17 anos e 2,5 de Companhia (entrada 1648/49); **sem casa** ⇒ lugar **em aberto** |
| 1649 | João Couceiro | cote *Lus. 45, 180* (caderno de 1655) | **fechado (2026‑11‑01)**: f. 180 n.º 111 do «Catalogus primus Collegii Conimbricensis 1655» — 22 anos, 6 de Companhia, 2.º ano de filosofia ⇒ entrada 1649 confirmada; **Coimbra (inferido), média**; Lisboa não excluída |
| 1651 | Diogo de Sotomaior | 1654/55 T1 trans‑tagano (Lus. 45 f. 116v) e T5 (índice, f. 100v); 1661 T2 (f. 290) | **fechado como alta (2026‑11‑08)**: noviço da **Casa de Provação de Lisboa** no catálogo trans‑tagano de 1654/55, f. 116v, n.º 22: «Fr. Jacobus de Sottomayor, ex oppido Vianna, an. 19, **Admisus 15 Martij an. 1654**»; o **índice** do mesmo catálogo (T5, «Irmãos Estudantes», f. 100v) regista «Fr. **Diogo** de Sottomayor» (o «Jacobus» é lapso ou segundo nome — não há outro Sottomayor no índice). Em 1661 estava no Colégio de Évora com os votos simples (f. 290, n.º 143). A data do Dehergne (**E. 1651**) está errada: entrou em **Março de 1654** ⇒ **Lisboa (Casa de Provação), alta** |
| 1652 | Manuel Pinto II | 1654 T1 (Lus. 45 ff. 75‑84v) e 1696 T1 (Lus. 46 ff. 314‑343v) | **reaberto e fechado como não determinado (2026‑11‑08)**: a cota da notícia do Dehergne («Lus. 46, 322») é do catálogo de **1696**, não de 1652 — o n.º 56 (f. 322 carimbado, imagem 317) é um «P. Manoel Pinto Conimbricensis», docente do Colégio de Coimbra, com «Ing. 14 Mart. 652»; um homem vivo num catálogo de 1696 não pode ter morrido em 1692 (HS 49, 66v, não possuída), e a naturalidade difere (Porto vs. Coimbra). A entrada de 1654 que eu tomara por ele (f. 79v, n.º 182) é «Fr. Manoel **Glz**» (Gonçalves). ⇒ **não determinado; informação inconsistente no Dehergne** |
| 1663 | João Fernandes Fou | 1665 T1 (Lus. 45 ff. 309‑332v) | **revisto (2026‑11‑01)**: em 1665 o único noviciado é a Domus Probationis de Lisboa (f. 322; «Novitij» f. 322v‑323, ingressos de 1663‑64) ⇒ **Lisboa (Casa de Provação), baixa** (inferência; revisão de 2026‑11‑02: a «unicidade» do noviciado em 1665 não está provada por Franco — que só documenta a supressão do de Évora — embora os blocos de Coimbra/Évora examinados não tenham lista de noviços); identificação nominal não resolvida (candidato n.º 417 com apelido ilegível; f. 394 de 1672 tem outro nome) |
| 1666 | Francisco Simões | 1669 T1 (Lus. 45 ff. 362‑376v) | **revisto (2026‑11‑01)**: noviciado começado em Portugal e interrompido (embarcou em 1668 «avant la fin de son noviciat», Pfister); em 1665/1669 o único noviciado é a Domus Probationis de Lisboa ⇒ **Lisboa (Casa de Provação), baixa** |
| 1673 | José Soares | 1675 T1 (Lus. 45 ff. 444‑463v) e catálogos de 1678‑1685 (Lus. 46) | **reaberto e fechado como não determinado (2026‑11‑08)**: a identificação com «Frat. Josephus Teixeyra, ex oppido S. Combadão» (noviço de Coimbra em 1675, f. 451 n.º 213) caiu — esse noviço tinha **13 meses** de Companhia em 1675 (entrada em 1674), e José Soares entrou em **Março de 1673**; em 1678 os Teixeiras de Coimbra têm **10‑11 anos** (outros homens) e continuam em 1681 e 1685, depois do embarque de 1680. O próprio Dehergne escreve «E. (nous ne le trouvons pas aux catal. de Lus, ni de Goa)». ⇒ **não determinado; sem assento de noviço** |
| 1675 | Simão Pinto | 1675 T1 (Lus. 45 ff. 444‑463v) | **revisto (2026‑11‑01)**: o catálogo de 1678 inscreve-o como escolar de humanidades com 24 anos e «fuit 3» (Lus. 46, f. 16, n.º 523) — confirma a entrada em 1675, mas é residência; **Coimbra (inferido), baixa** |
| 1678 | André da Costa | 1678 T1 (Lus. 46 ff. 1‑21v; o f. 22 é o T6) | **fechado (2026‑11‑01)**: noviço da **Domus Probationis de Lisboa** no catálogo de 1681 — «Fr. Andreas da Costa. Bracharensis, an. 18 et 3 menses. Societ. 21 menses» (f. 70v, n.º 446) ⇒ **Lisboa (Casa de Provação), alta** |
| 1678 | António Simões I | 1678 T1 (Lus. 46 ff. 1‑21v; o f. 22 é o T6) | **revisto (2026‑11‑01)**: ausente das quatro listas de noviços (Lisboa e Coimbra, 1678 e 1681) ⇒ entrou depois do catálogo de 1678; noviciado em 1678‑80, sem catálogo; **em aberto** (Lisboa ou Coimbra) |
| 1685 | António Freire | 1685 T1 (Lus. 46 ff. 118‑151v); ver 1685 T4 (Lus. 39 ff. 136‑139v) | **fechado (2026‑11‑01)**: «Fr. Antonius Freyre» na lista «Novitii Scholastici» da **Domus Probationis** no T4 de Dez. 1685 (Lus. 39, f. 140 carimbo = imagem `LUS. 39/138.jpg`) ⇒ **Lisboa, alta**; a cote de Dehergne (Lus. 46, 198v) é residência de 1690 |
| 1686 | Francisco Barbosa | 1686 breve (Lus. 39 f. 144), 1693 T1 (Lus. 46 f. 255v), W 1329 e 1696 (Lus. 46 ff. 314‑343v) | **fechado como alta (2026‑11‑08)**: noviço nomeado na «Domus Probationis Ulyssiponensis» do catálogo breve de Nov. 1686 (Lus. 39, f. 144 carimbado = imagem 142): «Fr. **Felix Barbosa**»; o catálogo de 1693 (Lus. 46, f. 255v carimbado, n.º 132) dá «ingressus 21 Jan. 1686»; **W 1329** chama-lhe «P. Francisco Barbosa» (117.ª expedição, 1694); e no catálogo de **1696** desaparece do bloco de Coimbra (continuam José de Freitas e Domingos de Cabo, seus vizinhos de 1693) ⇒ embarque em 1694 confirmado. Cota do Dehergne «225v» = gralha por 255v; o «Felix» do índice de 1696 é «Felix **Barreto**». ⇒ **Lisboa (Casa de Provação), alta**; reserva única: prenome Félix vs Francisco |
| 1690 | Félix‑José Pereira | 1690 T1 (Lus. 46 ff. 192‑218v) | **fechado (2026‑11‑01)**: noviço da **Domus Probationis de Lisboa** no catálogo de 1690 — «Fr. Josephus Pereira … initi Societ. 14 Januarii an. 1690» (f. 208, n.º 412; data exacta do Dehergne) ⇒ **Lisboa (Casa de Provação), alta** |
| 1690 | João Duarte | 1690 T1 (Lus. 46 ff. 192‑218v) | **fechado por inferência (2026‑11‑01); corrigido em 2026‑11‑08**: entrou a 17 Jul. 1690, dentro do período de noviciado único em Lisboa (Jun. 1685‑Dez. 1690) ⇒ **Lisboa (Casa de Provação), média** (regra institucional; sem lista nominal de 1690). O assento do catálogo de **1700** (Lus. 46 a, f. 19, n.º 339) que eu usara para «confirmar» a data é de um **homónimo**: «Fr. Ioannes Duarte, ex opp. Monte major… natus 29 Nov. 1671… Rhetoricus» — o nosso embarcou em 1696 (W 1361) e estava na China em 22 Abr. 1700 |
| 1692 | João Francisco Cardoso | 1693 T1 (Lus. 46 f. 272v) e 1696 T1 (Lus. 46 f. 326) | **fechado como alta (2026‑11‑08)**: noviço da **Domus Probationis de Lisboa** no catálogo de 1693 (f. 272v, n.º 420): «Fr. Franciscus Cardozo, ex oppido Porto de Mós, Leiriensis, ingressus Societ. 22 Decembris an. 692» — nome, naturalidade e data coincidem com o Dehergne, e o prenome é o que ele próprio usava («Franciscus (sans João) Cardozo»). A cota «Lus. 46, 326» é o catálogo de **1696**, onde está no bloco de Coimbra (n.º 162, mesma data) — residência posterior ⇒ **Lisboa, alta**. Idade divergente (cat. 1673 vs Dehergne 1677) registada |
| 1693 | Manuel Marques | 1693 T1 (Lus. 46 ff. 242‑295v) | **revisto (2026‑11‑01/02)**: entrou a 25 Nov. 1693 — já depois da restituição dos noviciados (Jan. 1691), fora da regra do noviciado único; sem lista nominal do biénio ⇒ **em aberto** |
| 1693 | Manuel Teles | 1693 T1 (Lus. 46 ff. 242‑295v) | **revisto (2026‑11‑01/02)**: entrou a 24 Ago. 1693, fora da regra do noviciado único (restituição em Jan. 1691); sem lista nominal ⇒ **em aberto** (Dehergne anota a variante «E. 25 set. 1697, Évora») |
| 1694 | Manuel de Sousa | 1696 T1 (Lus. 46 ff. 314‑343v) | **fechado por inferência (2026‑11‑01)**: entrou a 6 Set. 1690 ⇒ **Lisboa (Casa de Provação), média** (noviciado único desde Jun. 1685); sem confirmação nominal (lacuna de 1691‑92) |
| 1699 | Teotónio Leitão | 1700 T1 (Lus. 47 ff. 8‑33v; variante Lus. 46 a ff. 1‑39v) | **revisto (2026‑11‑01/02)**: não figura nas listas de noviços de 1700; a regra de 1685 já não se aplica (restituição em 1691) e falta a lista dos noviços coadjutores ⇒ **em aberto** |
| 1700 | Manuel Ribeiro júnior | 1700 T1 (Lus. 47 ff. 8‑33v; variante Lus. 46 a ff. 1‑39v) | **revisto (2026‑11‑01/02)**: não está nas listas de noviços de 1700 (nn. 393‑436); a regra de 1685 já não se aplica ⇒ **em aberto** |
| 1707 | André Pereira | 1711 T1 (Lus. 47 ff. 118‑151) | **revisto (2026‑11‑01)**: assento em Évora (f. 133v n.º 363; «ingressus 17 Jun. 1707», fase de filosofia) — residência, não noviciado; as listas de noviços de 1711 só cobrem admissões desde 1/1/1709 e não há catálogo de 1708 ⇒ **Évora (inferido), baixa** |
| 1709 | Luís de Sequeira | 1711 T1 (Lus. 47 ff. 118‑151) | **fechado (2026‑11‑01)**: noviço da **Domus Probationis de Lisboa** no catálogo de 1711 — «Fr. Ludovicus de Sequeira … natus 17 Jan. 1694. ingressus Societ. 1 Sept. 1709» (f. 143, n.º 585) ⇒ **Lisboa (Casa de Provação), alta** |
| 1710 | Francisco Alberto | 1711 T1 (Lus. 47 ff. 118‑151) | **fechado (2026‑11‑01)**: noviço no **noviciado anexo ao Colégio de Coimbra** no catálogo de 1711 — «Fr. Franciscus Albertus Brigantinus Dioec. Mirandensis … ingressus Societ. 3 Mart. 1710» (f. 128, n.º 228, lista «Novitij Scholastici pertinentes ad Provinciam») ⇒ **Coimbra, alta** |
| 1727 | João de Seixas | BNP 231 / Lus. 48 | bloqueado (Lus. 48 ausente; J do BNP lido sem ele) |
| 1729 | Manuel José | BNP 231 / Lus. 48 | bloqueado (M do BNP lido sem ele) |
| 1734 | João Simões | BNP 231 (falta f. 106v) / Lus. 48 | bloqueado |

## 8. Como recomeçar (passo a passo)

> [!important] **Ramo e PRs.** O trabalho desta revisão vive no ramo **`portugal-no-entry-review`**; o `main` local acompanha o `origin/main` (que só muda por PR). **Não abrir PR sem instrução explícita do investigador** — o PR só se cria quando a revisão dos lugares de entrada estiver concluída.

1. `cd /Users/jrc/develop/dehergne-repertoire-mbook-air && git status` (deve estar no ramo `portugal-no-entry-review`; o `main` fica intacto).
2. Ler `tools/RECIPE.md` (método detalhado e variantes de nomes) e o `AGENTS.md` do pacote de índice do SSD
   (`/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/AGENTS.md`); localizar o catálogo com `tools/arsi_index.py`.
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
- **2026-11-01 (2.ª sessão)** — pasta `inferences/portugal-no-entry/` retirada do `.gitignore` e versionada (commit inicial, 312 ficheiros); **digitalizações ARSI migradas para o SSD externo «ARSI»** (`/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/`) — caminhos dos JSON e documentação actualizados. Casos do §7 revistos: **Couceiro** (Coimbra inferido, média; cote f. 180 n.º 111 localizado) e **Abreu** (Évora 1651 = residência; ausente dos noviciados de 1649 ⇒ entrada provavelmente 1649, lugar em aberto); depois **Sotomaior** (Lisboa/Casa de Provação, baixa) e **Pinto II** (noviço em Coimbra em 1654, f. 79v n.º 182 ⇒ Coimbra, média); **André da Costa** (noviço da Domus Probationis de Lisboa em 1681, f. 70v n.º 446 ⇒ Lisboa, alta), **Félix‑José Pereira** (idem em 1690, f. 208 n.º 412 — número e fólio corrigidos em 2026‑11‑07 ⇒ Lisboa, alta) e **João Francisco Cardoso** (idem em 1693, f. 272v n.º 420 ⇒ Lisboa, média); revistos sem resultado Duarte, Sousa, Marques, Teles e António Simões I (lacunas de catálogo). Estado: 44 alta · 38 média · 14 baixa · 14 não determinados. Registado o **pacote de índice das digitalizações** (`indexes/` + `AGENTS.md` no SSD, 274 catálogos) e criado o atalho `tools/arsi_index.py`.

## 10. Ligações úteis

- Viewer pha: `http://127.0.0.1:8765/doc/<slug>/p<NNN>`; exemplos: Dehergne `reference-works-joseph-dehergne-1973-repertoire-des-jesuites-de-chine-de-1542-a-1800`, Wicki `reference-works-wicki-liste-jesuiten-indienfahrer-1967`, Pfister `pfister-notices-notices-biographiques-et-bibliographiques-sur-pfister-louis-t1` (e `-t2`), François `franco-imagens-franco-imagem-virtude-coimbra-1719-v1`, catálogo 1625 `jesuit-catalogues-jesuit-cat-type1-portugal-1625-t1-lus-44ii-410`.
- BNP Pombalina 231: <https://purl.pt/47525>.
- Índice dos catálogos (pacote completo): `/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/indexes/` —
  `INDICE-cronologico.md`, `INDICE-sistematico-por-volume.md`, `catalogos/`, `reports/`, `_data/`;
  instruções em `.../AGENTS.md`; atalho de consulta `tools/arsi_index.py`.
- Nota de tarefa: `01 Notes/Portugal-no-entry.md` (quadro de tarefas).
- Relatório de fólios: `01 Notes/ARSI Lusitania - fólios em falta - Portugal no entry.md`.
- Nota de método: `Determining college or noviciate from catalog reference 2026-10-19.md`.
- Inventário dos catálogos da Documenta Indica: `01 Notes/Documenta Indica - catálogos.md`.
