# Receita de investigação — «Portugal no entry» (lugar de entrada na Companhia)

Objetivo: para cada pessoa indicada, determinar (e justificar com o arquivo) o
**lugar de entrada na Companhia de Jesus** — o valor do atributo Timelink
`jesuita-entrada`, que o Dehergne deixou em falta (ou que a tabela Obsidian
sugere provisoriamente).

## 0. Contexto do problema

- O Dehergne, *Répertoire des Jésuites de Chine* (1973), regista para estas
  personagens `E. <ano>` (entrada) **sem dizer onde**.
- A tabela Obsidian «[[0 Portugal no entry]]» acrescentou, depois de uma
  primeira verificação manual, um lugar provisório **no fim do nome** de 37
  pessoas (ex.: «Coimbra», «Évora», «Santo Antão», «Goa?»). Essas sugestões
  precisam de validação; as restantes não têm sugestão.
- As respostas mais frequentes são as casas de formação portuguesas:
  **Coimbra** (Real Colégio de Jesus / noviciado), **Lisboa** (Casa de S. Roque
  e **Colégio de Santo Antão** — «Santo Antão» é o colégio de Lisboa, **não** a
  ilha de Cabo Verde), **Évora** (colégio e noviciado), **Braga**, **Bragança**,
  **Porto**, e, para quem entrou já no Oriente, **Goa** ou **Macau**. Nos anos
  de fusão dos noviciados (1619-1630) a atribuição pode ser ambígua.

## 1. Dados já reunidos (não repetir trabalho)

Para cada pessoa há um *packet* com a notícia do Dehergne (texto integral, tal
como está na base Timelink), a cronologia de atributos da base (nascimento,
estatuto, entrada, embarque, wicky, estadias, morte), a linha da tabela Obsidian
e o caminho da ficha Obsidian:

```bash
cd /Users/jrc/develop/dehergne-repertoire-mbook-air/inferences/portugal-no-entry
python3 tools/packet.py <id> [<id> ...]     # packets completos
python3 tools/packet.py --list              # lista de todas as pessoas
python3 tools/arsi_index.py --year 1655     # ÍNDICE ARSI: que catálogo em que fólios (§2 bis‑A)
```

## 2. Pesquisa no arquivo pha

O arquivo está em `/Users/jrc/jesuit-archive` (136 documentos, 82 mil páginas).
O índice de pesquisa (SQLite FTS, só leitura) é consultado com:

```bash
cd /Users/jrc/develop/dehergne-repertoire-mbook-air/inferences/portugal-no-entry

# procurar variantes do nome (português, castelhano, italiano, latim)
python3 tools/pha_research.py --name "Diogo Pinto" \
    --variant "Diego Pinto" --variant "Didacus Pintus" --limit 8

# restringir por anos
python3 tools/pha_research.py --name "Amador da Costa" --year 1550-1580

# mapa dos documentos do arquivo (id, filename, coleção)
python3 tools/pha_research.py --docs
```

Cada resultado indica **documento, página, variante e trecho**. Antes de usar
qualquer resultado, **ler a página completa** (é o comando que vai na citação):

```bash
python3 - <<'PY'                     # ou usar o MCP pha_page
import sqlite3
c=sqlite3.connect('file:/Users/jrc/jesuit-archive/archive.db?mode=ro&immutable=1',uri=True)
doc,page=81,50
for r in c.execute("""select d.id,d.filename,p.page_no,ch.variant,ch.text
    from chunks ch join pages p on p.id=ch.page_id join documents d on d.id=ch.document_id
    where d.id=? and p.page_no=? and ch.variant='edited'""",(doc,page)):
    print(r[4])
PY
```

(Alternativa equivalente: `pha page <doc> <page> [--edited]` a partir de
`/Users/jrc/jesuit-archive` com `PHA_ARCHIVE_DIR` definido, ou o MCP
`pha_page`.)

### Variantes de nome a experimentar

- português moderno e antigo: `Diogo`/`Diego`/`Didaco`; `Rodrigues`/`Roiz`/
  `Ruis`/`Ruiz`/`Rodericus`; `Francisco`/`Fran.co`; `Manuel`/`Manoel`/`Emanuel`;
  `Coelho`/`Coello`; `António`/`Antônio`/`Antonio`/`Ant.onio`.
- latim: terminações `-us` (`Didacus Pintus`, `Emanuel Alvarez`), genitivo
  (`Didaci Pinti`), ou o nome em latim macarrónico dos catálogos
  (`Petrus Jusarte` por Pedro Zuzarte).
- castelhano/italiano: `Diego`, `Juan`/`Giovanni`, `Pedro`/`Pero`/`Pierre`.

### Onde procurar (por ordem de valor)

1. **Catálogos jesuítas** (`collections/jesuit-catalogues/`, docs 1, 2, 4, 27-37):
   type4 = catálogos de casa (1566, 1567-Coimbra, 1576, 1577, 1586, 1587, 1601,
   1601-nov, 1602, 1610); type1 = catálogos trienais (1587, 1606, 1625). Um
   noviço nomeado numa casa de noviciado no ano do `jesuita-entrada` é a prova
   mais direta. Um catálogo **posterior** só mostra onde a pessoa estava, não
   onde entrou.
2. **Notícias editoriais modernas** — *Documenta Indica* (docs 19, 68-71, 77-84,
   89-92), *Documentação para a história das missões do padroado português do
   Oriente* (docs 17, 20-26, 38-41), *Monumenta Brasiliae* (docs 85-88),
   Pfister (docs 47, 50), Wicki *Liste der Jesuiten-Indienfahrer* (doc 66).
   Estas edições dão muitas vezes «entrou na Companhia em … a …» na introdução
   biográfica de cada documento.
3. **António Franco, *Imagem da virtude*…** — noviciado de **Coimbra** (docs 54,
   55), **Évora** (doc 52) e **Lisboa** (doc 53): as vidas declaram o noviciado
   e a data de entrada. Há índices já extraídos nas notas do arquivo
   (`/Users/jrc/jesuit-archive/notes/novicos-de-coimbra.md`,
   `coimbra-jesuitas.md`, `franco-coimbra-indice-nomes.md`,
   `franco-evora-indice-nomes.md`, `franco-lisboa-indice-nomes.md`) — consultar
   primeiro, é muito mais rápido do que varrer os volumes.
4. **Dehergne** (doc 65), *Relatio anual* de Fernão Guerreiro (docs 101-103),
   Bartoli (docs 130-137), cartas e *litterae quadrimestres* (docs 105-120).

## 2 bis. As digitalizações do ARSI (Lusitania) estão em disco — usar SEMPRE

> [!important] Os catálogos digitais estão agora no **SSD externo «ARSI»**
> (volume montado em `/Volumes/ARSI`). O caminho de trabalho — o que deve ir nas
> citações e no campo `comando` dos JSON (`open "…"`) — é
> **`/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/`**. A cópia antiga em iCloud
> (`~/Library/Mobile Documents/com~apple~CloudDocs/Documents/RSD_Active_System/PROJECTS/Project-UC-China/ARSI Lusitania/v2-2025-01-19/`)
> ainda existe, mas já não é a cópia de referência: não citar por ela.
> No SSD **não é preciso «aquecer» imagens** (não há paginação iCloud). Se
> `/Volumes/ARSI` não estiver montado, **montar o disco antes de ler** — a
> ausência do volume não é prova de que o fólio não existe.
> A pasta traz ainda `AGENTS.md` (instruções do pacote para agentes) e o **índice
> completo dos 274 catálogos** em `indexes/` (`INDICE-cronologico`,
> `INDICE-sistematico-por-volume`, `catalogos/`, `reports/`, `_data/`) — ver
> **§2 bis‑A**, que é o primeiro sítio a consultar antes de abrir fólios.

O arquivo pha **não tem** os códices ARSI *Lus*. 39/42-47 que o Dehergne cita
(`Lus. 43`, `Lus. 44 I/II`, `Lus. 45`, `Lus. 47`) nem qualquer catálogo
português posterior a 1625. Mas o investigador tem as **digitalizações de
trabalho** em:

```
/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/
├── LUS. 39/                 (289 imgs, fólios 0-143v) — catálogos breves 1579-1608
├── LUS. 42 nova aquisição/  (47 imgs)
├── LUS. 43 II a/            (234 imgs, ff. 270-385v)
├── LUS. 43 II b/            (307 imgs, ff. 386-...)
├── LUS. 44 I/               (598 imgs, ff. 0-298)
├── LUS. 44 II/              (242 imgs, ff. 0-420v)
├── LUS. 44 II_continuação pedida no ARSI_Gato de Pinho, Inês/   (240 imgs, ff. 420v-655)
├── LUS. 45/                 (979 imgs, ff. 0-487v)
├── LUS. 46/, LUS. 46 a/, LUS. 47/  (743/93/505 imgs)
└── LUS.<ano>-<mês>-<dia>.arsi.<vol>.<fólio>.<tipo>.pdf   (catálogos soltos: 1566, 1579, 1586-1588, 1599, 1601-1608…)
```

**Os nomes dos ficheiros são o número do fólio**, com o offset indicado dentro
de cada JSON (ex.: `LUS. 44 II/315v.jpg` = fólio 315v; na pasta
`LUS. 44 II_continuação…` os nomes vêm colados: `0588v-0589.jpg` = ff.
588v-589; `0619v-0620.jpg` = ff. 619v-620). **Ler a imagem** com a ferramenta de
imagem (`read_image`) — é leitura de manuscrito, não OCR, e é a prova primária.
Para manuscrito denso, recortar e ampliar com
`tools/crop.sh "<imagem>" x y w h <nome> [zoom]` (coordenadas na imagem original
2250x3000; a saída vai para `_scratch/crops/`, ignorada pelo git).

Citações destes fólios fazem-se assim:

```
ARSI Lus. 44 II, f. 315v (imagem LUS. 44 II/315v.jpg) — leitura direta da imagem
```

e o campo `comando` fica `open "/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/LUS. 44 II/315v.jpg"`.
Indicar sempre no JSON que a prova é **manuscrito ARSI lido em imagem** (não
`pha page`), para que a citação seja honesta.

Os catálogos trienais/breves organizam-se **por casa** (Casa de S. Roque,
Casa de Provação, Colégio de Coimbra, Évora, Porto, Braga, Bragança…) e dão, por
pessoa: naturalidade, idade, **anos de Companhia**, tempo de noviciado e
estudos. Regra de ouro: **ano de entrada = ano do catálogo − anos de Companhia**;
um noviço listado numa casa é prova de que fez lá o noviciado.

## 2 bis‑A. O ÍNDICE dos catálogos que acompanha as digitalizações — consultar PRIMEIRO

O SSD «ARSI» traz, dentro da pasta das imagens, um **pacote de índice completo**
(274 catálogos, 12 volumes/partes), construído a partir dos **índices
dactilografados** de cada volume (LUS. 45 `000i1‑i3.jpg`, LUS. 46/47 `000v.jpg`,
LUS. 44 I `000a.jpg`, …) e da leitura da primeira página de cada catálogo:

```
/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/
├── AGENTS.md                       ← instruções do pacote para agentes (ler no início)
├── index.html                      ← entrada do índice no browser
└── indexes/
    ├── INDICE-cronologico.md/.html            todos os catálogos por ano
    ├── INDICE-sistematico-por-volume.md/.html por volume (ano, tipo, fólios)
    ├── TIPOLOGIA.md                           o que é T1…T11 (tipologia de trabalho)
    ├── catalogos/<nota>.md                    uma nota por catálogo, com as imagens embutidas
    ├── reports/LUS-NN.md, SUMMARY, CORRECTIONS  relatórios por volume e registo de correcções
    ├── _data/LUS-NN.json                      ★ A FONTE DE VERDADE DO ÍNDICE (12 tabelas)
    └── tools/                                 validação/render (check_index.py, render_notes.py)
```

**Como usar (antes de varrer fólios):** consultar `indexes/_data/LUS-NN.json`
(ou o nosso atalho `tools/arsi_index.py`) para saber **que catálogo existe em que
fólios**, e abrir `indexes/catalogos/<nota>.md` para a nota correspondente. Campos
de cada catálogo: `year`, `type`, `local`, `folio_start`, `folio_end`,
`image_start_file`/`image_end_file` (quando o nome do ficheiro não é o fólio),
`note` (→ nota), `verified`, `evidence` (o que se leu na 1.ª página) e
`corrections` (histórico).

```bash
cd /Users/jrc/develop/dehergne-repertoire-mbook-air/inferences/portugal-no-entry
python3 tools/arsi_index.py --year 1655                 # catálogos de 1655
python3 tools/arsi_index.py --year 1649 1651 --volume 45
python3 tools/arsi_index.py --type T1 --local Transstagana
python3 tools/arsi_index.py --note 1655-T1-LUS-45-177   # ficha completa
python3 tools/arsi_index.py --gaps --volume 45          # lacunas do volume
```

O índice dá o **catálogo** e o **intervalo de fólios**, mas **não** a divisão
interna por casas: essa está no **índice dactilografado** do volume (imagens
`000i*.jpg`) e nos relatórios `indexes/reports/LUS-NN.md`. É aí que se lê, p. ex.,
que no Lus. 45 a coluna de 1649 tem Domus Professa f. 8, Coimbra f. 10, Évora
f. 13, Colégio de Lisboa f. 18, **Domus Probationis f. 20**… e que o catálogo
trans‑tagano de 1651 tem Évora f. 57, Vila Viçosa f. 62v, Faro f. 63, Portalegre
f. 63v, Elvas f. 65v.

**Regras do pacote (AGENTS.md §6–§8):**

- **Nunca** mover, renomear ou editar as imagens `LUS. NN/`; **nunca inventar um
  fólio** — ler a página e citá‑la.
- Se o índice estiver errado (intervalo de fólios, tipo, ano), corrigir pelo
  circuito do pacote: `indexes/reports/CORRECTIONS.md` + `indexes/_data/LUS-NN.json`
  (campo + `corrections[]`) + a nota em `indexes/catalogos/`, e depois
  `python3 indexes/tools/check_index.py`. Não é nosso sítio para editar, mas
  registar a correcção é o procedimento correcto.
- **Lacunas conhecidas** (verificar antes de dizer «não existe»): LUS. 47
  ff. 253‑349 não digitalizados; sem Catalogus II no LUS. 46 para 1693; sem
  Catalogus III no LUS. 47 para 1717; LUS. 43 sem índice dactilografado
  (segmentos inferidos, marcados ⚠️); LUS. 46a é variante do catálogo de 1700.
- Os nomes das pastas com acento foram normalizados para **NFC** em 2026‑10‑30;
  cópias antigas podem reintroduzir NFD (re‑correr `check_index.py --strict-nfc`).
- O índice é **estático**: não precisa de servidor; abre‑se com `index.html` (ou
  `python3 -m http.server` na raiz das imagens).

## 2 ter. O registo de entrantes da província (BNP, Pombalina 231)

Para **entradas de 1711 a 1758** existe uma fonte directa e decisiva: o
«**Catalogo dos Sogeitos, que entrarão em a Comp.ª de Jesus na Provincia de
Portugal: Começa em Jan.º de 1711**» — BNP, Pombalina 231, 247 fólios,
digitalizado em <https://purl.pt/47525>. Cada assento diz o nome, a
naturalidade/diocese, os pais, o baptismo e, sobretudo:

> «Entrou no Noviciado de **Coimbra** / **Évora** / **Lx.ª** … aos <dia> de <mês> de <ano>»

Cópia local (imagens descarregadas) — **já não existe em `results/_scratch/`
(limpeza de 2026-11): re-descarregar** com a skill `bnp-digital-download`:
`results/_scratch/bnp47525/hires_NNNNNN.jpg`. Calibração verificada:
**página N (número impresso no canto superior direito) = imagem N+10**
(a p. 1 = imagem 11; a imagem 351 = p. 172). O registo está ordenado por data
de entrada; o ano vem na margem direita. Alternativa impressa: o mesmo catálogo
saiu, com coluna NOVICIADO, como apêndice dos *Catalogus Provinciae Lusitanae*
de 1910 (n.os 1-351, letras A-E) e 1911 (352-940, F-J) nas digitalizações do
ARSI.

Citação: `BNP, Pombalina 231, «Catalogo dos Sogeitos…», p. <N> (imagem hires_NNNNNN.jpg) — leitura directa · open "…/hires_NNNNNN.jpg"`.


> [!warning] «Não está no pha» ≠ «não existe»
> Os códices Lus. 43‑47 **não** estão no arquivo pha, mas as digitalizações de trabalho
> em `/Volumes/ARSI/ARSI Lusitania/v2-2025-01-19/` estão **completas** (Lus. 44 I ff. 0‑298; Lus. 44 II ff. 0‑655;
> Lus. 45 ff. 0‑487v; Lus. 46 ff. 0‑376), excepto o **Lus. 47, ff. 253‑349** e o
> **Lus. 48** (inexistente). Antes de escrever «fólio não existe», verificar a pasta —
> e confirmar a correspondência imagem↔fólio no pé da página.

### Como citar (formato pha)

Cada facto leva a citação no formato em uso no arquivo:

```
<Autor/Título>, *<referência bibliográfica se disponível>* (doc <id>), p. <página> — <raw|edited> (<editor/variant>) · `pha page <id> <página> [--edited]`
```

Exemplos:

- *Documenta Indica* vol. XI (doc 81), p. 50 — edited (`documenta-indica-ocr`) · `pha page 81 50 --edited`
- *Catálogo da província de Portugal, 1566* (doc 29), f. 271v — edited (`jesuit-cat4`) · `pha page 29 4`
- Franco, *Imagem da virtude… Coimbra* II (doc 55), p. 505 — edited (`franco-imagem-virtude`) · `pha page 55 505 --edited`

Usar `pha bib <doc>` (ou o MCP `pha_bib`) quando precisar da referência
bibliográfica completa do documento.

## 3. Regras de decisão

- **Prova direta** (o documento diz que entrou em X, ou nomeia-o noviço em X no
  ano da entrada) → `confianca: alta`.
- **Prova indireta forte** (o catálogo da casa X no ano da entrada inclui-o
  entre os noviços; ou a notícia editorial diz «entrou em X») → `alta` ou
  `média`.
- **Inferência** (aparece em X em data próxima; a casa era a do noviciado da sua
  região; etc.) → `média` ou `baixa`.
- **Nada encontrado** → não inventar: registar `lugar: null`,
  `confianca: nenhuma` e dizer exactamente o que se procurou e o que falta
  (p. ex. «Lus. 43 não existe neste arquivo»).
- Distinguir sempre **lugar de entrada** de **casa de residência posterior**. Um
  catálogo de 1610 não prova entrada em 1610.
- Se a sugestão da tabela Obsidian estiver confirmada, dizê-lo; se estiver
  errada (lugar ou ano), corrigi-la com a prova.
- Se houver conflito entre a data de Dehergne e a do arquivo, registar ambos.
- Nunca citar uma página que não tenha sido lida; a citação é verificável e
  outro agente vai abri-la.

## 4. Resultado a produzir

Um ficheiro JSON por pessoa em
`inferences/portugal-no-entry/results/<id>.json`, com este formato exacto:

```json
{
  "id": "deh-diogo-pinto",
  "name": "Diogo Pinto",
  "lugar": "Lisboa (Santo Antão)",
  "data": "1561 (provável)",
  "confianca": "média",
  "sugestao_tabela": "Santo Antão",
  "validacao": "confirmada quanto ao lugar (Lisboa), corrigido o ano",
  "resumo": "1-3 frases com a conclusão.",
  "biografia": "2-6 frases de biografia (Dehergne + arquivo).",
  "analise": [
    {"titulo": "A entrada na Companhia", "texto": "prosa com a prova, citações em bloco (> …) e a referência no fim."}
  ],
  "evidencias": [
    {"citacao": "*Documenta Indica* vol. XI (doc 81), p. 50 — edited (`documenta-indica-ocr`)", "comando": "pha page 81 50 --edited", "o_que_prova": "entrada em Portugal em 1561, provavelmente em Lisboa", "forca": "direta"}
  ],
  "nao_encontrado": "o que se procurou e não existe no arquivo (opcional)",
  "refs_obsidian": ["[[0 Portugal no entry]]", "[[deh-diogo-pinto]]"]
}
```

`confianca`: `alta` | `média` | `baixa` | `nenhuma`.
Salvar também um `results/<id>.md` (rascunho livre) se ajudar, mas o JSON é o
que será usado para montar a nota final.
