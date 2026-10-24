# LUS. 42 (nova aquisição) — índice dos catálogos

**Data:** 2026-10-22
**Pasta:** `…/ARSI Lusitania/v2-2025-01-19/LUS. 42 nova aquisição` (46 imagens)
**Fonte:** inspeção direta da pasta (não há índice dactilografado). Nenhuma imagem foi movida ou alterada.

## 1. Conteúdo da pasta

| imagem | conteúdo |
|---|---|
| `0000a.jpg` | capa/lombada: etiqueta «LUS. 42» e inscrição «Cat. Lusit. 1577» |
| `0000b.jpg` | fólio de guarda em branco |
| `0001.jpg` | **f.1** — «Padres é Irmãos desta Prouincia de Portugal em Agosto de 1577»; começa por P. Ant.º de Aguiar |
| `0001v-0002.jpg` … `0041v-0042.jpg` | continuação do catálogo, com imagens de dois fólios (verso + recto seguinte) por fotografia |
| `0042v.jpg` | **f.42v** — fim do catálogo |
| `9999.jpg` | fólio de guarda final em branco |

As imagens de nome duplo (`0001v-0002.jpg`, etc.) juntam o verso de um fólio e o recto do seguinte numa única fotografia. O total de imagens de texto é 42 (f.1 a f.42v).

## 2. Catálogos encontrados

**Um único catálogo.**

| ano | tipo | ficheiros | fólio | nota | estado | evidência |
|---|---|---|---|---|---|---|
| 1577 | T1S | 0001–0042v | 1–42v | `1577-T1S-LUS-42-f1` | existente (01 Notes) — não tocada | `0001.jpg`: «Padres é Irmãos desta Prouincia de Portugal em Agosto de 1577», com apreciação individual; `0042v.jpg` = f.42v, seguido de guarda em branco (`9999.jpg`) |

Catálogo alfabético (ordem pela inicial do nome), sem divisão por comunidades mas com apreciação de cada religioso; não permite detectar a entrada. Tipo 1S (lista sem divisão de comunidades com avaliação).

## 3. Verificação de que não há mais catálogos

- Início: capa + dois fólios de guarda antes do título de 1577 (não há índice nem segundo título).
- Meio: `0020v-0021.jpg` é continuação da série alfabética, sem novo cabeçalho nem mudança de data.
- Fim: `0042v.jpg` termina o catálogo; `9999.jpg` é guarda em branco.
- Não foi encontrado qualquer outro cabeçalho datado nem outro tomo na pasta.

## 4. Notas existentes / reconciliação

- `1577-T1S-LUS-42-f1` já existia em `01 Notes`; foi marcada `already_existed` e **não foi alterada nem duplicada**.
- **Desvio a resolver pelo Lead:** os 45 links `file://` dessa nota apontam para a cópia antiga
  `…/Project-UC-China-Livro/1-Project Support/Broteria recover/broteria_recover_2024-12-28/folderB_0 ARSI 42/`
  e não para a pasta `v2-2025-01-19/LUS. 42 nova aquisição`. Todos os 45 links resolvem (0 quebrados), mas a nota não embebe a digitalização atual. Não a alterei por não ser permitido sobrescrever notas existentes; se o Lead quiser, a nota pode ser re-apontada para a pasta nova (os ficheiros correspondentes existem: `0000a/0000b`, `0001`, `0001v-0002` … `0042v`, `9999`).

## 5. Gaps / decisões

- Não se criou nenhuma nota nova (não há catálogos em falta).
- `gen_notes.py` não gera nada para este volume (a única entrada tem `note: null` e `existing_note`), pelo que `data/LUS-42.json` serve de registo/cobertura; o `validate.py` mostra 0 catálogos para LUS-42 por essa razão.
- Decisão do Lead: (a) manter a nota antiga como está; ou (b) re-apontar os links da nota para `v2-2025-01-19/LUS. 42 nova aquisição` (trabalho de uma linha por link, mas é edição de nota existente).

## 6. Ficheiros

- `extras/ARSI-catalogs-indexes/data/LUS-42.json`
- este relatório
