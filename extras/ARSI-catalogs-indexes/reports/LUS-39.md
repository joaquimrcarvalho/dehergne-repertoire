# LUS. 39 — índice dos catálogos (ARSI Lusitania 39)

**Data:** 2026-10-22
**Pasta:** `…/ARSI Lusitania/v2-2025-01-19/LUS. 39` (288 imagens)
**Fonte do índice:** `LUS.39.0.index.pdf`, p. 2 — «Index ad codicem ARSI "Lus.39"»; existe também uma fotografia do mesmo índice em `LUS. 39/ .jpg`. Nenhuma imagem da pasta foi movida ou alterada.

## 1. Leitura do índice dactilografado

O índice tem duas colunas de números: a **foliação** (f.1, f.7, … f.142) e, à direita, em vermelho, o **número de «jpg»** do scan antigo do ARSI (3, 15, 24, 36, … 282); os números vermelhos servem para localizar os suplementos (ex.: «Suppl.: 18 **38**» = fólio 18, imagem antiga 38). Transcreveram-se as 23 entradas:

| # | fólio | tipo | data | observações |
|---|---|---|---|---|
| 1 | 1 | Cat.brev. | 12.1.1579 | Suppl.: 5 |
| 2 | 7 | Cat.brev. | 1.1.1586 | Suppl. post singulas domos, ubi res fert |
| 3 | 11 | Cat.brev. | 1.1.1587 | |
| 4 | 17 | Cat.brev. | 1.1.1588 | Suppl.: 18 |
| 5 | 19 | Cat.rerum | Oct. 1599 | |
| 6 | 23 | Cat.brev. | 1.1.1601 | Suppl. (et ingressor. aetas, patria etc): 29 |
| 7 | 35 | Cat.brev. | Nov. 1601 | |
| 8 | 41 | Cat.brev. | [Jan.] 1602 | Suppl.: 46v |
| 9 | 51 | Cat.brev. | Nov. 1603 | |
| 10 | 55 | Cat.brev. | Ian. 1605 | |
| 11 | 61 | Cat.rerum | Apr. 1606 | |
| 12 | 63 | Cat.brev. | Ian. 1608 | |
| 13 | 69 | Cat.brev. | Aest. 1612 | |
| 14 | 75 | — | — | Novitii Beirenses et Interamnenses recepti 1610-1613 |
| 15 | 77 | Cat.brev. | cca Aug. 1613 | (pro "1614") — 81r: obiit iam fr. Franc. Rodriguez, ergo post 12.7.1613; sed 83r: vivit adhuc fr. Balthas. Monteiro, qui obiit 30.8.1613 |
| 16 | 85 | Cat.brev. | [Nov.] 1615 | (Cfr. 86v, 89r) |
| 17 | 95 | Cat.brev. | Oct/Nov. 1616 | (pro "1617") — P. Ant. de Moraes vivit 95v, obiit 29-11-1616; ingressi oct. 1616, 98v |
| 18 | 103 | — | — | Elenchus Missionariorum, circa annos 1628-1633 (anotação a vermelho: «in império sinensis 225 412v») |
| 19 | 114 | Cat.brev. | Ian. 1621 | |
| 20 | 122 | Cat.brev. | [Ian.] 1622 | Ian.; comparando ingr. et mort. — Suppl.: 128v |
| 21 | 130 | Cat.brev. | Ian. 1623 | Suppl.: 136v |
| 22 | 138 | Cat.brev. | cca Dec. 1685 | (sec. ingress. novit.) Inscribitur pro "1686". |
| 23 | 142 | Cat.brev. | cca Nov. 1686 | (idem) Inscribitur pro "1687". |

A lápis, no fim da página: «grande catálogo 1623-1686».

## 2. Correspondência fólio ↔ ficheiro (importante)

A pasta tem **uma imagem por lado de página**: `NNN.jpg` = recto do fólio NNN, `NNNv.jpg` = verso. Até f.41 o nome do ficheiro coincide com o carimbo. **A partir de f.51 a foliação carimbada está +1 (e +2 a partir de f.83) em relação ao nome do ficheiro** (a foliação antiga saltou números que a digitalização não reproduziu; p.ex. `050.jpg` tem carimbo 51, `083.jpg` tem carimbo 85, `140.jpg` tem carimbo 142). Por isso:

- `folio_start`/`folio_end` no JSON são **números de imagem da pasta** (é o que o `gen_notes.py` usa para escolher as imagens);
- `folio_stamped_start`/`folio_stamped_end` guardam a **foliação carimbada / do índice**, usada no nome da nota.

Isto foi verificado ficheiro a ficheiro nos inícios de todos os 23 catálogos (ver tabela seguinte). O **fólio 84 não existe** na numeração carimbada (salta de 83v para 85), pelo que o catálogo de 1614 termina em 83v.

## 3. Catálogos, notas e verificação

Nota = nome no vault. «Nova» = criada nesta passagem; «existente» = já existia e **não foi tocada**.

| ano | tipo | ficheiros | fólio carimbado | nota | estado | 1.º fólio verificado / evidência |
|---|---|---|---|---|---|---|
| 1579 | T4 | 001–006v | 1–6v | `1579-T4-LUS-39-1` | existente (01 Notes) | 001.jpg, carimbo 1: «CATALOGO. DELOS. PADRES y hermanos dela Prouincia de Portugal a 12. de Enero. de 1579» |
| 1586 | T4 | 007–010v | 7–10v | `1586-T4-LUS-39-7` | existente (01 Notes) | 007.jpg: «Catalogo de los padres y hermanos de la Provincia de Portugal, hecho a primero de Enero del año de 1586» |
| 1587 | T4 | 011–016v | 11–16v | `1587-T4-LUS-39-11` | existente (01 Notes) | 011.jpg: «CATALOGO DELOS PES y HERMANOS DE LA Prouincia de Portugal, hecho al primero de Enero de 87» |
| 1588 | T1P | 017–018v | 17–18v | `1588-T1P-Évora-Coimbra-LUS-39-c17` | existente (01 Notes) | 017.jpg: «Suplemento de las visitas … desta provincia de Portugal, que embia a Roma en Abril de 1587, recebido a 1.º de Enero de 1588» |
| 1599 | T3 | 019–022v | 19–22v | `1599-T3-LUS-39-c19` | existente (01 Notes) | 019.jpg, carimbo 19: «Catalogo 3.º que llaman de casas dela Prou.ª de Portugal hecho en Oct. de 1599» |
| 1601 jan | T4 | 023–034v | 23–34v | `1601-jan-T4-LUS-39-c23` | existente (03 Projectos) | 023.jpg, carimbo 23: «Catalogo breue de los P.es y Hermanos de la Prouincia de Portugal, al 1.º de Henero de 1601» |
| 1601 nov | T4 | 035–040v | 35–40v | `1601-nov-T4-LUS-39-C35` | existente (03 Projectos) | 035.jpg, carimbo 35: «Catalogo da Prouincia de Portugal Em Nouembro de 1601» |
| 1602 | T4 | 041–049v | 41–50v | `1602-T4-LUS-39-C41` | existente (03 Projectos) | 041.jpg, carimbo 41: «Catalogo breue delos Padres y Hermanos de la Prouincia de Portug. del año de 1602» |
| 1603 | T4 | 050–053v | 51–54v | `1603-T4-LUS-39-51` | **nova** | 050.jpg, carimbo 51: «Catalogo breue de los P.es y Hermanos de la Prouincia de Portugal, feito em Nou.º de 1603» |
| 1605 | T4 | 054–059v | 55–60v | `1605-T4-LUS-39-55` | **nova** | 054.jpg, carimbo 55: «Catalogo breue da Prouincia de Portugal feito no principio de Janeiro do ano de 1605» |
| 1606 | T3 | 060–061v | 61–62v | `1606-T3-LUS-39-61` | **nova** | 060.jpg, carimbo 61: «Catalogo 3.º da Prouincia de Portugal feito Em abril do Ano de 1606» |
| 1608 | T4 | 062–067v | 63–68v | `1608-T4-LUS-39-63` | **nova** | 062.jpg, carimbo 63: «Catalogo breue da Prouincia de Portugal feito no principio de Jan.º de 1608» |
| 1612 | T4 | 068–073v | 69–74v | `1612-T4-LUS-39-69` | existente (01 Notes) | 068.jpg, carimbo 69: «Terçeyro Catalogo da Prouincia de Portugal. Em Janr.º de 1612» |
| 1610-13 | T10 | 074–075v | 75–76v | `1610-T10-LUS-39-75` | **nova** | 074.jpg, carimbo 75: «Noviços Beirenses et Interamnenses, que neste anno se receberam em Coimbra…» |
| 1614 | T4 | 076–082v | 77–83v | `1614-T4-LUS-39-77` | **nova** | 076.jpg, carimbo 77: «Terçeiro Catalogo da Prouincia de Portugal do anno de 1614» |
| 1615 | T4 | 083–092v | 85–94v | `1615-T4-LUS-39-85` | **nova** | 083.jpg, carimbo 85: «Catalogo 3.º da Prouincia de Portugal do anno de 1615» |
| 1617 | T4 | 093–100v | 95–102v | `1617-T4-LUS-39-95` | existente (01 Notes) | 093.jpg, carimbo 95: «Catalogo da Prouincia de Portugal anno 1617» |
| 1628-33 | T10 | 101–111 | 103–113 | `1628-1633-T10-LUS-39-103` | existente (01 Notes) | 101.jpg/103.jpg: nota moderna «Hic Compactus omnium Missionariorum… ff. 103-113» + «Catalogus eorum qui sunt in ministeriis…» (carimbo 104) |
| 1621 | T4 | 112–120v | 114–121v | `1621-T4-LUS-39-114` | **nova** | 112.jpg: «Catalogo dos Padres, e Irmãos da Prou. de Portugal, feito em Jan. de 1621» |
| 1622 | T4 | 121–127v | 122–128v | `1622-T4-LUS-39-122` | **nova** | 121.jpg, carimbo 122: «Catalogo dos Padres e Irmãos … da Prouincia de Portugal de 622, a 10 de Janeiro de 622» |
| 1623 | T4 | 128–135v | 130–137v | `1623-T4-LUS-39-c130` | existente (03 Projectos) | 128.jpg, carimbo 130: «Catalogo da Prouincia de Portugal feito em Janr.º de 1623. Casa de S. Roque» |
| 1685 | T4 | 136–139v | 138–141v | `1685-T4-LUS-39-138` | **nova** | 136.jpg, carimbo 138: «Catalogus Patrum, ac Fratrum Prouinciae Lusitanae» (índice: cca Dec. 1685, pro «1686») |
| 1686 | T4 | 140–143v | 142–145v | `1686-T4-LUS-39-142` | **nova** | 140.jpg, carimbo 142: «Catalogus Patrum ac Fratrum Prouinciae Lusitanae anno …» (índice: cca Nov. 1686, pro «1687») |

**Resultado:** 23 catálogos; **11 notas novas**, **12 notas já existentes** (8 em `01 Notes`, 4 em `03 Projectos`) marcadas `already_existed` e não sobrescritas; **0 notas em falta**. Todas as 23 notas têm os links `file://` a resolver (283 links, 0 em falta).

Cobertura de imagens: os 286 ficheiros regulares `001.jpg … 143v.jpg` estão todos dentro de exactamente um intervalo. Não atribuídos: `000.jpg` (capa/lombada «LUS. 39 CAT. BREV. INTER ANNOS 1579 & 1687») e ` .jpg` (fotografia do próprio índice dactilografado).

## 4. Notas existentes — reconciliação

- Mantiveram-se todos os nomes antigos (não se renomeou nada): prefixos `c`/`C` em `c17`, `c19`, `c23`, `C35`, `C41`, `c130`; variantes `1612-T4`, `1617-T4`, `1628-1633-T10`.
- `1602-T4-LUS-39-C41` **já existia** (a tarefa dava-o como provável em falta). Está na `03 Projectos`; não foi duplicado.
- `1617-T4-LUS-39-95`: a nota antiga descreve «fl.93v – 101v (img 093v –100v)», ou seja, usa números de imagem como se fossem fólios. O cabeçalho está de facto em `093.jpg` (carimbo 95 = f.95 do índice). O intervalo da nota antiga omite a imagem do cabeçalho (`093.jpg`) e começa em `093v.jpg`.
- `1612-T4-LUS-39-69`: o título é «Terçeyro Catalogo», mas o conteúdo é um catálogo breve por casas; manteve-se o tipo T4 da nota antiga (o projecto já aceita «Catalogo 3.º» como T4 — ver a tipologia, exemplo do f.85).
- `1588-T1P-…-c17`: a nota antiga classifica-o como T1P (parcial); o conteúdo é um «Suplemento das visitas» com noviços recebidos (semelhante ao tipo T6). Não foi alterada.
- `1628-1633-T10-LUS-39-103`: nota antiga cobre o «Elenchus Missionariorum» e começa em `101v`; o intervalo de ficheiros do JSON (101–111) inclui a nota manuscrita (101), a folha de reparação em branco (102) e o texto (103-111).

## 5. Gaps, ambiguidades e decisões para o Lead

1. **Deslocamento da foliação** (ver §2): o índice lista fólios, a pasta usa números sequenciais; a nota nova mantém o fólio do índice, os embeds usam o número de imagem. Não há conflito, mas quem comparar «fólio» com «nome de ficheiro» deve ter isto em conta.
2. **Fólio 84 inexistente** na foliação carimbada (salta 83v → 85). O índice também não o lista; não se inventou entrada.
3. **Suplementos internos** indicados pelo índice dentro dos intervalos: 1579 f.5; 1588 f.18; 1601 f.29; 1602 f.46v; 1622 f.128v; 1623 f.136v. Ficam incluídos nos embeds, sem nota própria (são continuações, não catálogos autónomos).
4. **«pro 1614/1617/1686/1687»**: a nota de 1614 usa o ano de inscrição (1614) como as notas antigas de 1617; para 1685/1686 usei os anos do índice e da master list (1685, 1686), embora os catálogos estejam inscritos «pro 1686» e «pro 1687». Decisão do Lead: manter 1685/1686 (como está) ou alinhar com a convenção «pro» (1686/1687).
5. **Elenchus 1628-1633**: é um maço (nota moderna + folhas em branco + texto), não um catálogo com cabeçalho datado; a data 1628-1633 vem do índice e da nota manuscrita. Fica `verified: true` com essa evidência, mas a datação é aproximada.
6. **Pasta raiz**: existem PDFs soltos por catálogo (ex.: `LUS.1602-01-00.arsi.39.fl.41.Cat.brev..pdf`), úteis como evidência complementar; não foram usados para os embeds (embeds usam sempre as imagens da pasta, como pedido).
7. **Notas antigas fora de `03 Projectos`**: 8 notas de LUS.39 estão em `01 Notes` e não são vistas pelo `validate.py` (que só olha para `03 Projectos`); validei-as à parte — 0 links quebrados. O `validate.py` conta 15 catálogos (11 novas + 4 existentes em `03 Projectos`) e reporta **0 problemas** para os JSON de LUS-39 e LUS-42.

## 6. Ficheiros

- `extras/ARSI-catalogs-indexes/data/LUS-39.json`
- 11 notas novas em `/Users/jrc/jrc-notes/03 Projectos/`: `1603-T4-LUS-39-51`, `1605-T4-LUS-39-55`, `1606-T3-LUS-39-61`, `1608-T4-LUS-39-63`, `1610-T10-LUS-39-75`, `1614-T4-LUS-39-77`, `1615-T4-LUS-39-85`, `1621-T4-LUS-39-114`, `1622-T4-LUS-39-122`, `1685-T4-LUS-39-138`, `1686-T4-LUS-39-142`
- este relatório
