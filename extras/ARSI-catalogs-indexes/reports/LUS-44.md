# LUS. 44 — índice dos catálogos (1587-1645, ff. 1-655)

Volume: **ARSI Lusitania 44** — *Catalogi triennales et Breves 1587-1645, ff. 1-655*, em três pastas de digitalização:
`LUS. 44 I` (597 imagens, ff. 1-300), `LUS. 44 II` (241 imagens, ff. 301-420v) e
`LUS. 44 II_continuação pedida no ARSI_Gato de Pinho, Inês` (240 imagens, ff. 420v-655).

## 1. Fontes do índice

- `LUS. 44 I/000a.jpg` — página 1 do índice dactilografado (cabeçalho «Lus.44 Catalogi triennales et Breves 1587-1645 ff.1-655»), colunas «Quales Catal.? Tempus ff»; cobre **1587-1619** e marca a divisão LUS.44-I / LUS.44-II a meio da coluna direita (depois dos ff. 299-300).
- `LUS. 44 I/001.jpg` — página 2 do índice (cabeçalho «Lus.44», numeração «2»), cobre **1622-1645** e termina com «Finis». Não está órfã: é o ficheiro `001.jpg` da pasta `LUS. 44 I` (confirmado por hash: idêntico ao attachment da vault `001 2.jpg` / `001 5.jpg`). As duas páginas do índice foram lidas com `read_image` (não OCR).
- A pasta `LUS. 44 II` **não** tem página de índice: `000v.jpg` é a lombada do volume («LUSITANIA CATALOGI TRIENNAL. 1614-1645, 44 II»).

Transcrição: 61 entradas de catálogo, de 1587 a 1645, com ano, tipo, fólios inicial/final e notas do próprio índice (vacat, suplementos, «non bene compactus», etc.). Tipos usados: T1 = Catalogus I; T3 = Catalogus III / brevis; T4 = Catalogus brevis; T5/T5b = Index alphabeticus; T6T7 = Supplementa I & II; T10 = catálogos especiais (admissões, eclesiásticos, missionários, noviços); T1S = catálogo I sem separação de comunidades.

## 2. Mapa ficheiro ↔ fólio (ESSENCIAL para LUS. 44 I)

Ao contrário de LUS. 45, **em `LUS. 44 I` o nome do ficheiro não é o número do fólio carimbado**. A digitalização (Brotéria) numerou as imagens por ordem de digitalização, com desvios que mudam em função de folhas inseridas, fólios com sufixo alfabético e ff. vacat:

| Fólios carimbados | Ficheiro do fólio recto | Observações |
|---|---|---|
| 1-25 | `001v.jpg` … `025v.jpg` | desvio 0 (`f. n` = `0nnv.jpg`) |
| entre 25 e 26 | `026v.jpg`–`044v.jpg` (19 folhas) | folhas inseridas sem carimbo = antigos ff. 85-104 (catálogo I de 1590 «non bene compactus») |
| 26-85 | `045v.jpg` … `104v.jpg` | desvio +19 (`f. n` = `0(n+19)v.jpg`) |
| 86-105 | — | **não digitalizados** (marcados «vacat»: nota marginal em `104v.jpg`: «vide 25 da 1ª = 25ª / ff. 85-104 vacat») |
| 106-207 | `105v.jpg` … `206v.jpg` | desvio -1 (`f. n` = `0(n-1)v.jpg`) |
| 207a-213 | `207v.jpg`–`214v.jpg` | folha inserida 207a (Cat. III 1606) e desvio +1 nos ff. 208-213 |
| 214-236 + 236a-236h | `215v.jpg` … `244.jpg` | desvio +1; as folhas inseridas 236a-236h (= antigos ff. 257-264) são os suplementos de 1608 |
| 237-256 | `244v.jpg` … `264.jpg` | desvio +7 |
| 267-300 | `264v.jpg` … `298.jpg` | desvio -3 |

Consequência: `gen_notes.py` foi **estendido de forma retrocompatível** com os campos opcionais `image_start_file` / `image_end_file` / `image_folder`, usados pelas entradas do LUS. 44 I (o intervalo de imagens é o que está verificado; o campo `folio_start/end` mantém o fólio carimbado/do índice).

Nas pastas `LUS. 44 II` e continuação o nome do ficheiro **é** o fólio: `301.jpg` = f. 301 (carimbo 301 confirmado), `420v.jpg` = f. 420v; na continuação cada imagem cobre duas páginas (`0420v-0421.jpg` = f. 420v + f. 421, confirmado pelo carimbo 421). O f. 420v está duplicado nas duas pastas (sobreposição mínima, não é erro do índice).

## 3. Catálogos

| Ano | Tipo | Fólios (índice dact.) | Ficheiro inicial | Nota | Verif. |
|---|---|---|---|---|---|
| 1587 | T1 | 1-20 | 001v.jpg | 1587-T1-LUS-44-I-1 | sim |
| 1587 | T5 | 21-24 | 021v.jpg | 1587-T5-LUS-44-I-21 | sim |
| 1590 | T1 | 25-25v | 025v.jpg | 1590-T1-LUS-44I-25 | sim |
| 1590 | T3 | 26-27 | 045v.jpg | 1590-T3-LUS-44-I-26 | sim |
| 1590 | T5b | 28-31 | 047v.jpg | 1590-T5b-LUS-44-I-28 | sim |
| 1591 | T6T7 | 34-37 | 053v.jpg | 1591-T6T7-LUS-44-I-34 | sim |
| 1592 | T4 | 38-44 | 057v.jpg | 1592-T4-LUS-44-I-38 | sim |
| 1593 | T4 | 45-53 | 064v.jpg | 1593-T4-LUS-44-I-45 | sim |
| 1593 | T3 | 54-58 | 073v.jpg | 1593-T3-LUS-44-I-54 | sim |
| 1593 | T5 | 59-64 | 078v.jpg | 1593-T5-LUS-44-I-59 | sim |
| 1593 | T1 | 65-84 | 084v.jpg | 1593-T1-LUS-44-65 | sim |
| 1594 | T6T7 | 105-108 | 104v.jpg | 1594-T6T7-LUS-44-I-105 | sim |
| 1597 | T4 | 109-114 | 108v.jpg | 1597-T4-LUS-44-I-109 | sim |
| 1597 | T6T7 | 115-118 | 114v.jpg | 1597-T6T7-LUS-44-I-115 | sim |
| 1597 | T4 | 119-123 | 118v.jpg | 1597-T4-LUS-44-I-119 | sim |
| 1597 | T5 | 125-128 | 124v.jpg | 1597-T5-LUS-44-I-125 | sim |
| 1597 | T1 | 129-150 | 128v.jpg | 1597-T1-LUS-44-I-129 | sim |
| 1601 | T10 | 151-156 | 150v.jpg | 1601-T10-LUS-44-I-151 | sim |
| 1603 | T3 | 157-160 | 156v.jpg | 1603-T3-LUS-44-I-157 | sim |
| 1603 | T5 | 161-167 | 160v.jpg | 1603-T5-LUS-44-I-161 | sim |
| 1603 | T1 | 168-198 | 167v.jpg | 1603-T1-LUS-44-I-168 | sim |
| 1604 | T4 | 199-202 | 198v.jpg | 1604-T4-LUS-44-I-199 | sim |
| 1604 | T6T7 | 203-207 | 202v.jpg | 1604-T6T7-LUS-44-I-203 | sim |
| 1606 | T3 | 207a-207a | 207v.jpg | 1606-T3-LUS-44-I-207a | sim |
| 1606 | T5 | 208-213 | 209v.jpg | 1606-T5-LUS-44-I-208 | sim |
| 1606 | T1 | 214-236 | 215v.jpg | 1606-T1-LUS-44-214 | sim |
| 1608 | T6T7 | 257-264 | 238v.jpg | 1608-T6T7-LUS-44-I-236a | sim |
| 1610 | T4 | 237-256 |  | (nota em `04 Biographies/dehergne/1610-T4-LUS-44-I-c237.md`) | sim |
| 1611 | T5 | 267-272 | 264v.jpg | 1611-T5-LUS-44-I-c267 | sim |
| 1611 | T1 | 273-298 | 270v.jpg | 1611-T1-LUS-44-I-273 | sim |
| 1611 | T3 | 299-300 | 296v.jpg | 1611-T3-LUS-44-I-299 | sim |
| 1614 | T1 | 301-327 |  | 1614-T1-LUS-44II-302 | sim |
| 1614 | T3 | 328-340 |  | 1614-T4-LUS-44II-328 | sim |
| 1614 | T5 | 341-346 |  | 1614-T5-LUS-44II-341 | sim |
| 1615 | T10 | 347-348 |  | 1615-T10-LUS-44I-347 | sim |
| 1619 | T1 | 350-376v |  | 1619-T1-LUS-44II-349 | sim |
| 1619 | T5 | 377-381 |  | 1619-T5-LUS-44II-377v | sim |
| 1622 | T1 | 383-404 |  | 1622-T1-LUS-44II-383 | sim |
| 1622 | T5 | 405-409 |  | 1622-T5-LUS-44II-405 | sim |
| 1625 | T1 | 412-429 |  | 1625-T1-LUS-44II-410 | sim |
| 1625 | T5 | 430-433 |  | 1625-T5-LUS-44II-430 | sim |
| 1625 | T3 | 434-437 |  | 1625-T3-LUS-44II-434 | sim |
| 1627 | T10 | 438-438 |  | 1627-T10-LUS-44II-438 | sim |
| 1628 | T1 | 439-466v |  | 1628-T1-LUS-44II-441 | sim |
| 1628 | T5 | 467-472 |  | 1628-T5A-LUS-44II-468 | sim |
| 1628 | T3 | 473-480 |  | 1628-T3-LUS-44II-474 | sim |
| 1633 | T1 | 481-511 |  | 1633-T1-LUS-44II-481 | sim |
| 1633 | T3 | 512-519 |  | 1633-T3-LUS-44II-512 | sim |
| 1633 | T10 | 520-521 |  | 1633-T10-LUS-44II-520 | sim |
| 1633 | T5 | 522-528 |  | 1633-T5-LUS-44II-520 | sim |
| 1636 | T1 | 529-554 |  | 1636-T1-LUS-44II-529 | sim |
| 1636 | T5 | 555-558 |  | 1636-T5-LUS-44II-555 | sim |
| 1636 | T3 | 559-562 |  | 1636-T3-LUS-44II-559 | sim |
| 1639 | T5 | 563-569 |  | 1639-T5-LUS-44II-564 | sim |
| 1639 | T1 | 570-592v |  | 1639-T1-LUS-44II-570 | sim |
| 1639 | T3 | 593-597 |  | 1639-T3-LUS-44II-594 | sim |
| 1642 | T5 | 598-603 |  | 1642-T5-LUS-44II-598 | sim |
| 1642 | T1 | 604-623 |  | 1642-T1S-LUS-44II-604 | sim |
| 1645 | T5 | 624-629 |  | 1645-T5-LUS-44II-624 | sim |
| 1645 | T1 | 630-650 |  | 1645-T1-LUS-44II-630 | sim |
| 1645 | T3 | 651-655 |  | 1645-T3-LUS-44II-652 | sim |

### Evidência de verificação (primeiro fólio lido)

- **1587 T1 1-20** — f. 1 (001v.jpg), carimbo 1: «Primero Catalogo de los Padres y Hermanos dela Provincia de Portugal … 1 de Abril de 1587»
- **1587 T5 21-24** — f. 21 (021v.jpg), carimbo 21: «1587. praesentes in domo» — índice alfabético por letras
- **1590 T1 25-25v** — f. 25 (025v.jpg), carimbo 25: «Catalogo Primero de los Padres y Hermanos de la provincia de Portugal hecho en Mayo de 1590»; f. 85 (104v.jpg) com nota marginal «ff. 85-104 vacat»
- **1590 T3 26-27** — f. 26 (045v.jpg), carimbo 26: «Catalogo General de las casas y Colegios y rentas dela Provincia de Portugal. Sebso en Mayo de 1590»
- **1590 T5b 28-31** — f. 28 (047v.jpg), carimbo 28: «Indice del Catalogo primero … Sebso en Mayo de 1590»
- **1591 T6T7 34-37** — f. 34 (053v.jpg), carimbo 34: «Supplemento del primer Catalogo … Sebso en principio de Enero de 1591»
- **1592 T4 38-44** — f. 38 (057v.jpg), carimbo 38: «Catalogo dos Padres e Irmãos da Provincia de Portugal … em outubro de 1592»
- **1593 T4 45-53** — f. 45 (064v.jpg), carimbo 45: «Catalogo dos Padres e Irmãos da Provincia de Portugal feito no principio de Janrº de 1592»
- **1593 T3 54-58** — f. 54 (073v.jpg), carimbo 54: «Catalogo breve da Provincia de Portugal Sebso en Abril de 1593»
- **1593 T5 59-64** — f. 59 (078v.jpg), carimbo 59: «Catalogo Alfabetico delos P.es y Sermanos dela Provincia de Portugal Sebso en Abril de 1593»
- **1593 T1 65-84** — f. 65 (084v.jpg), carimbo 65: «CATALOGO PRIMERO de los Padres y Hermanos dela Provincia de Portugal fecho en Abril de 1593»
- **1594 T6T7 105-108** — f. 85 (104v.jpg), carimbo 85: «Supplemento del Catalogo 1º de Coimbra del año de 1594»; continua em 105.jpg; f. 106 (105v.jpg): suplemento do catálogo 2º de Coimbra (Jan. 1594)
- **1597 T4 109-114** — f. 109 (108v.jpg), carimbo 109: «Catalogo da Provincia de Portugal do anno de 97»
- **1597 T6T7 115-118** — f. 115 (114v.jpg), carimbo 115: «Suplemento do primeiro Catalago da Provincia do Collegio d'Évora de 97»
- **1597 T4 119-123** — f. 119 (118v.jpg), carimbo 119: «Catalogo dos Padres e Irmãos da provincia de Portugal do Anno de 1597»
- **1597 T5 125-128** — f. 125 (124v.jpg), carimbo 125: «Catalogo Alfabetico delos P.es y Sermanos … y es index del 1º Catalogo Secho en Abril de 1597»
- **1597 T1 129-150** — f. 129 (128v.jpg), carimbo 129: «CATALOGO PRIMERO de los Padres y Hermanos dela Provincia de Portugal hecho en Abril de 1597»
- **1601 T10 151-156** — f. 151 (150v.jpg), carimbo 151: «Catalogus admissorum ad Selectistas in Lusitania Provincia ab anno 1601 usque ad mensem Maji an. 1628 …»
- **1603 T3 157-160** — f. 157 (156v.jpg), carimbo 157: «Catalogo da Provincia de Portugal. 1603» (informação de casas)
- **1603 T5 161-167** — f. 161 (160v.jpg), carimbo 161: «Index alfabetico del Catalogo 1º trienal dela Provincia de Portugal Secho en Abril de 1603»
- **1603 T1 168-198** — f. 168 (167v.jpg), carimbo 168: «Catalogo primero de los P.es y hermanos dela Provincia de Portugal Secho en Abril de 1603»
- **1604 T4 199-202** — f. 199 (198v.jpg), carimbo 199: «Catalogo dos P.es y Irmãos da Prov.ª de Portugal Secho Ê Janeiro de 604»
- **1604 T6T7 203-207** — f. 203 (202v.jpg), carimbo 203: «Parte do suplemento dos Catalogos da Prou.ª de Portugal do Ano de 1603. Feitos Ê Janrº de 1604»
- **1606 T3 207a-207a** — f. 207a (207v.jpg), carimbo «207a» (com «208» riscado): «Catalogus Provinciae Lusitaniae, qui dicitur rerum. 1606»
- **1606 T5 208-213** — f. 208 (209v.jpg), carimbo 208: «Indice do 1º Catalogo dos P.es e Irmãos da Provincia de Portugal feito Ê Março do ano de 1606»
- **1606 T1 214-236** — f. 214 (215v.jpg), carimbo 214: «Primeiro Catalogo trienal da Provincia de Portugal feito no principio do mes de Março do Ano de 1606»
- **1608 T6T7 257-264** — f. 236e (239v.jpg), carimbo «236 e 259»: «Suplemento do segundo catalogo do Colle de Coimbra Primeiro de Janeiro de 608»; f. 236g (242v.jpg), carimbo «236g 260»: «Suplemento do Catalogo do Collegio de Évora … 1608»; f. 236h (243v.jpg), carimbo «236h 261»: defuntos e despedidos de 1608
- **1610 T4 237-256** — f. 237 (244v.jpg), carimbo 237: «Catalogo da Provincia de Portugal. 1610» (só nomes e ofícios)
- **1611 T5 267-272** — f. 267 (264v.jpg), carimbo 267: «Indice alphabetico do prim.º Catalogo — 1611»
- **1611 T1 273-298** — f. 273 (270v.jpg), carimbo 273: «Primeiro Catalogo da Provincia de Portugal do anno de 1611»
- **1611 T3 299-300** — f. 299 (296v.jpg), carimbo 299: continuação do catálogo das casas; f. 300 (297v.jpg), carimbo 300: receitas dos colégios; 298.jpg = f. 300v com as residências
- **1614 T1 301-327** — f. 301 (301.jpg), carimbo 301: capa «Catalogos da Provincia de Portugal com seu indice do anno de 1614»; f. 302 (302.jpg), carimbo 302: «Primeiro Catalogo da Provincia de Portugal feito em Janeyro de 1614»
- **1614 T3 328-340** — f. 328 (328.jpg), carimbo 328: «Catalogo breve …» (casas e nomes, sem informação pessoal)
- **1614 T5 341-346** — f. 341 (341.jpg), índice alfabético de 1614 (nota pré-existente 1614-T5-LUS-44II-341)
- **1615 T10 347-348** — f. 347 (347.jpg), carimbo 347: lista nominal «Sacerdotes… que ora…» (nota pré-existente 1615-T10-LUS-44I-347)
- **1619 T1 350-376v** — f. 350 (350.jpg), carimbo 350: «Primeiro catalogo da Provincia de Portugal feito no anno de 1619»
- **1619 T5 377-381** — f. 377 (377.jpg), índice alfabético de 1619 (nota pré-existente 1619-T5-LUS-44II-377v)
- **1622 T1 383-404** — f. 383 (383.jpg), carimbo/página «2»: continuação do catálogo I de 1622 (título no f. 382; nota pré-existente 1622-T1-LUS-44II-383)
- **1622 T5 405-409** — f. 405 (405.jpg), índice alfabético de 1622 (nota pré-existente 1622-T5-LUS-44II-405)
- **1625 T1 412-429** — f. 412 (412.jpg): continuação do catálogo I de 1625 (itens 6-16; nota pré-existente 1625-T1-LUS-44II-410)
- **1625 T5 430-433** — f. 430 (0430v-0431.jpg, f. 430v-431), índice alfabético de 1625 (nota pré-existente)
- **1625 T3 434-437** — f. 434 (0433v-0434.jpg), carimbo 434: «Catalogo da Provincia de Portugal do Anno de 16…» (só casas, sem informação pessoal)
- **1627 T10 438-438** — f. 438 (0437v-0438.jpg), carimbo 438: «Rol dos Missionarios q vão … de 27 …»
- **1628 T1 439-466v** — f. 439 (0438v-0439.jpg), carimbo 439: «1º Catalogo da Provincia de Portugal do anno de 1628»
- **1628 T5 467-472** — f. 467 (0467v-0468.jpg), índice alfabético de 1628 (nota pré-existente)
- **1628 T3 473-480** — f. 473 (0472v-0473.jpg), catálogo terceiro de 1628 (nota pré-existente)
- **1633 T1 481-511** — f. 481 (0480v-0481.jpg), «Primeiro Catalogo da Provincia de Portugal feito em Mayo de 1633» (nota pré-existente)
- **1633 T3 512-519** — f. 512 (0511v-0512.jpg), catálogo terceiro de 1633 (nota pré-existente)
- **1633 T10 520-521** — f. 520 (0519v-0520.jpg), carimbo 520: «INDEX 1633» com listas de noviços por região (Beirenses/Interamnenses/Transmontani)
- **1633 T5 522-528** — f. 522 (0521v-0522.jpg), índice alfabético de 1633 (nota pré-existente 1633-T5-LUS-44II-520)
- **1636 T1 529-554** — f. 529 (0528av-0529.jpg), catálogo I de 1636 (nota pré-existente)
- **1636 T5 555-558** — f. 555 (0554v-0555.jpg), índice alfabético de 1636 (nota pré-existente)
- **1636 T3 559-562** — f. 559 (0558v-0559.jpg), catálogo terceiro de 1636 (nota pré-existente)
- **1639 T5 563-569** — f. 563 (0563v-0564.jpg), índice alfabético de 1639 (nota pré-existente)
- **1639 T1 570-592v** — f. 570 (0569v-0570.jpg), catálogo I de 1639 (nota pré-existente)
- **1639 T3 593-597** — f. 593 (0592v-0593.jpg), carimbo 593: «Madrid» — início do catálogo das casas fora da Província (Cat. III 1639)
- **1642 T5 598-603** — f. 598 (0597av-0598.jpg), índice alfabético de 1642 (nota pré-existente)
- **1642 T1 604-623** — f. 604 (0603v-0604.jpg), catálogo I de 1642 (nota pré-existente 1642-T1S-LUS-44II-604)
- **1645 T5 624-629** — f. 624 (0623v-0624.jpg), índice alfabético de 1645 (nota pré-existente)
- **1645 T1 630-650** — f. 630 (0629v-0630.jpg), catálogo I de 1645 (nota pré-existente)
- **1645 T3 651-655** — f. 651 (0651v-0652.jpg), catálogo terceiro de 1645 (nota pré-existente 1645-T3-LUS-44II-652)

## 4. Notas

- **Notas novas criadas: 26** em `/Users/jrc/jrc-notes/03 Projectos/`.
- **Notas pré-existentes reutilizadas: 34** (não reescritas; marcadas `already_existed` / `skip` no JSON):

  - `1587-T1-LUS-44-I-1` (1587 T1, ff. 1-20) — pasta `01 Notes`
  - `1590-T1-LUS-44I-25` (1590 T1, ff. 25-25v) — pasta `01 Notes`
  - `1592-T4-LUS-44-I-38` (1592 T4, ff. 38-44) — pasta `01 Notes`
  - `1593-T1-LUS-44-65` (1593 T1, ff. 65-84) — pasta `01 Notes`
  - `1606-T1-LUS-44-214` (1606 T1, ff. 214-236) — pasta `01 Notes`
  - `1611-T5-LUS-44-I-c267` (1611 T5, ff. 267-272) — pasta `03 Projectos`
  - `1611-T1-LUS-44-I-273` (1611 T1, ff. 273-298) — pasta `01 Notes`
  - `1614-T1-LUS-44II-302` (1614 T1, ff. 301-327) — pasta `01 Notes`
  - `1614-T4-LUS-44II-328` (1614 T3, ff. 328-340) — pasta `01 Notes`
  - `1614-T5-LUS-44II-341` (1614 T5, ff. 341-346) — pasta `01 Notes`
  - `1615-T10-LUS-44I-347` (1615 T10, ff. 347-348) — pasta `01 Notes`
  - `1619-T1-LUS-44II-349` (1619 T1, ff. 350-376v) — pasta `01 Notes`
  - `1619-T5-LUS-44II-377v` (1619 T5, ff. 377-381) — pasta `01 Notes`
  - `1622-T1-LUS-44II-383` (1622 T1, ff. 383-404) — pasta `01 Notes`
  - `1622-T5-LUS-44II-405` (1622 T5, ff. 405-409) — pasta `01 Notes`
  - `1625-T1-LUS-44II-410` (1625 T1, ff. 412-429) — pasta `01 Notes`
  - `1625-T5-LUS-44II-430` (1625 T5, ff. 430-433) — pasta `01 Notes`
  - `1628-T1-LUS-44II-441` (1628 T1, ff. 439-466v) — pasta `01 Notes`
  - `1628-T5A-LUS-44II-468` (1628 T5, ff. 467-472) — pasta `01 Notes`
  - `1628-T3-LUS-44II-474` (1628 T3, ff. 473-480) — pasta `01 Notes`
  - `1633-T1-LUS-44II-481` (1633 T1, ff. 481-511) — pasta `01 Notes`
  - `1633-T3-LUS-44II-512` (1633 T3, ff. 512-519) — pasta `01 Notes`
  - `1633-T5-LUS-44II-520` (1633 T5, ff. 522-528) — pasta `01 Notes`
  - `1636-T1-LUS-44II-529` (1636 T1, ff. 529-554) — pasta `01 Notes`
  - `1636-T5-LUS-44II-555` (1636 T5, ff. 555-558) — pasta `01 Notes`
  - `1636-T3-LUS-44II-559` (1636 T3, ff. 559-562) — pasta `01 Notes`
  - `1639-T5-LUS-44II-564` (1639 T5, ff. 563-569) — pasta `01 Notes`
  - `1639-T1-LUS-44II-570` (1639 T1, ff. 570-592v) — pasta `01 Notes`
  - `1639-T3-LUS-44II-594` (1639 T3, ff. 593-597) — pasta `01 Notes`
  - `1642-T5-LUS-44II-598` (1642 T5, ff. 598-603) — pasta `01 Notes`
  - `1642-T1S-LUS-44II-604` (1642 T1, ff. 604-623) — pasta `01 Notes`
  - `1645-T5-LUS-44II-624` (1645 T5, ff. 624-629) — pasta `01 Notes`
  - `1645-T1-LUS-44II-630` (1645 T1, ff. 630-650) — pasta `01 Notes`
  - `1645-T3-LUS-44II-652` (1645 T3, ff. 651-655) — pasta `01 Notes`

- Sem nota própria: **1610-T4-LUS-44-I-c237** já existe em `04 Biographies/dehergne/` (não duplicada); e a entrada 1606 T3 (ff. 265/266 do índice) é a mesma folha inserida 207a, documentada em `1606-T3-LUS-44-I-207a`.

### Nomes que se desviam da convenção (mantidos, conforme METHOD)

- `1587-T1-LUS-44-I-1`, `1590-T1-LUS-44I-25`, `1593-T1-LUS-44-65`, `1606-T1-LUS-44-214`, `1611-T1-LUS-44-I-273`, `1611-T5-LUS-44-I-c267`, `1615-T10-LUS-44I-347` — sem o separador `-I-`/`-II-` uniforme ou com prefixo `c`.
- `1614-T4-LUS-44II-328` — o índice dactilografado chama-lhe *Catalogus III* (T3); mantém-se o nome antigo T4.
- `1619-T1-LUS-44II-349`, `1625-T1-LUS-44II-410`, `1628-T1-LUS-44II-441`, `1628-T3-LUS-44II-474`, `1639-T3-LUS-44II-594`, `1645-T3-LUS-44II-652`, `1633-T5-LUS-44II-520` — o fólio inicial do nome não coincide com o fólio inicial do índice dactilografado (a nota antiga inclui folhas de capa/índice adjacentes).
- `1587-T1-LUS-44-1` (primeira nota, em `01 Notes`) é duplicado de `1587-T1-LUS-44-I-1`; não foi mexido — decisão para o Lead.
- Nomes novos com tipo composto `T6T7` = *Supplementa I & II* (entradas combinadas no índice dactilografado).

## 5. Lacunas, duplicados e ambiguidades

- **ff. 86-105 não digitados** (marcados *vacat* no próprio volume; ver nota marginal em `104v.jpg`). O índice dactilografado inclui-os na entrada do catálogo I de 1590 («25/26 & 85/104»), mas as ff. antigas 85-104 estão encadernadas entre os ff. 25 e 26 (`026v.jpg`–`044v.jpg`).
- **ff. 257-266**: NÃO são um intervalo em falta — são as folhas inseridas 236a-236h (suplementos de 1608) e 207a (Catalogus III 1606?), todas digitalizadas.
- **ff. 299-300** (Cat. III 1611) estão no fim do `LUS. 44 I` (`296v.jpg`–`298.jpg`), não no `LUS. 44 II` (que começa em `301.jpg`). Não há lacuna aí.
- **Fólios vacat confirmados**: 32-33, 58, 60, 64, 167, 197-198, 298, 340, 382, 649-650.
- **Sobreposições do próprio índice**: 1590 Cat I/Cat III nos ff. 25-26 (resolvida no JSON: Cat I 25-25v); 1619 Cat I/Index no f. 377 e 1628 Cat I/Index no f. 467 e 1639 Cat I/Cat III no f. 593 (JSON usa 350-376v, 439-466v, 570-592v para o catálogo I, deixando o fólio de fronteira ao índice/catálogo seguinte).
- **Duplicado 420v** entre `LUS. 44 II/420v.jpg` e continuação `0420v-0421.jpg`.
- **Fólio 207a** e fólios com sufixo alfabético (236a-236h) não são representáveis no esquema `n`/`nv` do validador; por isso 207a é registado como `207a` (o validador ignora o intervalo) e as evidências citam os carimbos.

## 6. Decisões para o Lead

1. **Duplicado 1587**: `1587-T1-LUS-44-1.md` (01 Notes) é cópia de `1587-T1-LUS-44-I-1.md`; propor eliminar a primeira ou mantê-la com alias. Não foi tocada.
2. **Notas antigas com fólio inicial desviado** (lista em §4): manter nomes (METHOD) — mas se o Lead quiser uniformizar os nomes, é uma alteração manual.
3. **Master list** (só o Lead edita): as 26 notas novas e as 34 reutilizadas estão prontas a ligar; ver `data/LUS-44.json` (campo `note`) e a secção §3 deste relatório. A lista de `03.03.01.01` continua com entradas em falta para 1587-1611.
4. **Extensão de `gen_notes.py`** com `image_start_file`/`image_end_file`/`image_folder` (retrocompatível); ver diff no repositório.
5. **1615-T10-LUS-44I-347** tem `-44I-` no nome mas pertence materialmente ao vol. II (ff. 347-348); mantido o nome antigo.

## 7. Validação

`python3 extras/ARSI-catalogs-indexes/tools/validate.py` (validador já actualizado para procurar notas em `03 Projectos` **e** `01 Notes`):

```
=== LUS-44.json — ARSI Lusitania 44 ===
catalogues: 60 | verified: 60 | notes existing: 60 | image links: 1030
TOTAL PROBLEMS: 0
```

(As 61 entradas do JSON incluem uma sem nota própria — 1610 T4, que existe apenas em `04 Biographies` — e todas as restantes resolvem para uma nota real; todos os links `file://` resolvem.)


## Correções (2026-10-24)

- **1625-T5-LUS-44II-430**: a nota pré-existente em `01 Notes` embebia 11 imagens
  (0429v-0430 … 0439v-0440), juntando o índice T5 de 1625, o catálogo T3 de 1625,
  o Rol de missionários de 1627 e o início do catálogo de 1628. O T5 termina em
  **f.433** (imagem `0432v-0433.jpg`; f.433 em branco) e f.434 inicia o T3. Nota
  regenerada em `03 Projectos` com **4 imagens**.
- **1627-T10-LUS-44II-438**: o rol «Rol dos Missionarios que este anno de 627 vão
  pª a India Oriental e Angola» termina em **f.438v** (imagem `0438v-0439.jpg`);
  `folio_end` corrigido de 438 para **438v** (nota passa a ter **2 imagens**; a imagem 0438v-0439 é partilhada com o início do T1 de 1628).
- **1625-T3-LUS-44II-434**: intervalo explicitado (`0433v-0434.jpg` a
  `0436v-0437.jpg`), 4 imagens; verificado que f.438 já é o Rol de 1627.
