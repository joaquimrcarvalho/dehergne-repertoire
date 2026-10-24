# LUS. 46 — índice dos catálogos (1678, 1681, 1685, 1690, 1693, 1696)

**Volume:** `LUS. 46` — 742 imagens (000–370v), 6 anos de catálogos trienais.
**Índice dactilografado:** `LUS. 46/000v.jpg` (uma página).
**Nota de volume:** [[ARSI Lusitania 46]] / [[ARSI Lusitania 46 "1678 - 1696"]].
**Ficheiros de dados:** `data/LUS-46.json`, `data/LUS-46a.json`.
**Notas criadas:** 19 (LUS. 46) + 1 (LUS. 46a). **Nenhuma nota pré-existente** para este volume (o vault não tinha catálogos do LUS. 46).

## 1. O índice dactilografado

Cabeçalho transcrito:

> **Lus.46, 1–376 — Catalogi triennales Lus. Prov.ae — 1678, 1681, 1685, 1690, 1693, 1696**

A grelha dá, por ano, o fólio inicial de cada casa no **Catálogo I** e, em linhas próprias,
as gamas de **Index alph. Personarum**, **Supplementa**, **Catalogus II** e **Catalogus III**.
O índice usa a **numeração carimbada** (canto inferior direito). O *star* junto a 1690 tem a nota
«* ultim. in gr. 1690» e há uma anotação a lápis «208 v .416».

### ⚠ Desvio ficheiro ↔ fólio carimbado

Os nomes dos ficheiros **não coincidem** com os fólios carimbados a partir do fólio 42:

| Zona | ficheiro → carimbo | desvio |
|---|---|---|
| 001–041 | 001→1 … 041→41 | 0 |
| 042–193 | 042→43, 084→85, 110→111, 119→120, 153→154, 163→164, 193→194 | +1 |
| ~219–239 | 221→223, 239→242 | +2 / +3 |
| ~245–302 | 245→248, 299→302 | +3 |
| ~305–306 | 305→309, 306→310 | +4 |
| ~319–366 | 319→324, 350→356, 366→372 | +5 / +6 |

Isto corresponde a folhas do volume **não filmadas** (em branco / de título) ao longo da
digitalização — o volume tem 376 fólios e a digitalização termina no ficheiro 370 (= f. 376, «Finis»).
**Consequência prática:** as notas embutem imagens pela numeração dos **ficheiros** (é o que o
gerador faz), mas os nomes das notas e as gamas do relatório seguem a **numeração do índice**
(como pedido). O campo `index_folio_*` do JSON guarda o valor do índice; `folio_start/end` guarda
o ficheiro.

## 2. Tabela dos catálogos

`fólios` = gama de **ficheiros/imagens** (a que a nota embute). `fólio (índice)` = valor do índice dactilografado.
Todas as páginas de início foram lidas com `read_image` (evidência transcrita).

| Ano | Tipo | Ficheiros | Fólio (índice) | Nota | Verif. | Evidência (1.º fólio) |
|---|---|---|---|---|---|---|
| 1678 | T1 | 1–21v | 1–21v | `1678-T1-LUS-46-1` | ✔ | f.1: «Catalogus Primus Provinciae Lusitanae Anno 1678. Domus Professa Ulyssiponensis» |
| 1678 | T2 | 23–41v | 23–41 | `1678-T2-LUS-46-23` | ✔ | f.23: «Catalogus 2us Provinciae Lusitanae Anno 1678» |
| 1678 | T3 | 42–45v | 43–46 | `1678-T3-LUS-46-42` | ✔ | f.42: «Catalogus 3us Provinciae Lusitanae Anno 1678»; f.43 continua «Collegium Eborense/Portuense/Scalabitanum/Brigantinum» |
| 1678 | T6 (suppl.) | 22 | 22 | — (sem nota) | ✔ | f.22: entradas 699–706 + «Excierunt… In Collegio Conimbricensi exiit…» |
| 1678 | T5 (índice) | 46–50 | 47–51 | — (sem nota) | — | limites do índice |
| 1681 | T1 | 51–82v | 52–83 | `1681-T1-LUS-46-52` | ✔ | f.51: «Catalogus 1us Provinciae Lusitanae anni 1681. Domus Professa Ulyssiponensis» |
| 1681 | T2 | 83–108v | 84–109 | `1681-T2-LUS-46-84` | ✔ | f.83: «Catalogus 2us Provinciae Lusitanae anni 1681» |
| 1681 | T3 | 109–112v | 110–113 | `1681-T3-LUS-46-110` | ✔ | f.109: «Catalogus 3us Provinciae Lusitanae anni 1681» |
| 1681 | T6 (suppl.) | 82v | 83v | — (sem nota) | — | índice: «Supplementa 83v» |
| 1681 | T5 (índice) | 113–117 | 114–118 | — (sem nota) | — | índice |
| 1685 | T1 | 118–151v | 119–152 | `1685-T1-LUS-46-119` | ✔ | f.118: «Catalogus 1us Provinciae Lusitanae anni 1685. Domus Professa Ulyssiponensis» |
| 1685 | T3 | 152–156v | 153–157 | `1685-T3-LUS-46-153` | ✔ | f.152: «Catalogus 3us Provinciae Lusitanae Anni 1685» (encadernado **antes** do índice e do Cat. II) |
| 1685 | T5 (índice) | 157–161 | 158–162 | — (sem nota) | — | índice: «158/62» (leitura conjectural) |
| 1685 | T2 | 162–185v | 163–186 | `1685-T2-LUS-46-163` | ✔ | f.162: «Catalogus 2us Provinciae Lusitanae Anni 1685» |
| 1685 | T6 (suppl.) | — | — | — | — | índice marca «.» (sem suplemento) |
| 1690 | T5 (índice) | 186–191 | 187–192 | — (sem nota) | — | índice (índice **antes** do Cat. I) |
| 1690 | T1 | 192–218v | 193–220 | `1690-T1-LUS-46-193` | ✔ | f.192: «Catalogus 1us Provinciae Lusitanae Anno 1690. Domus Professa Ulyssiponensis» |
| 1690 | T2 | 219–235v | 221–237 | `1690-T2-LUS-46-221` | ✔ | f.219: «Catalogus 2us Provinciae Lusitanae Anno 1690» |
| 1690 | T3 | 236–238v | 239–242 | `1690-T3-LUS-46-239` | ✔ | f.236: «Catalogus 3us Provinciae Lusitanae anno 1690» |
| 1690 | T6 (suppl.) | 239–240 | 209; 243 | — (sem nota) | — | índice: «Supplementa 209;243»; 1.º suplemento inserido no Cat. I (f.208) |
| 1693 | T1 | 242–295v | 245–298v | `1693-T1-LUS-46-245` | ✔ | f.242: «Catalogus Primus Provinciae Lusitanae Anno 1693. Domus Professa Ulyssiponensis» |
| 1693 | T3 | 296–299v | 299–302 | `1693-T3-LUS-46-299` | ✔ | f.296: «Catalogus 3us Rerum Provinciae Lusitanae anno 1693» |
| 1693 | **T8** | 300–300v | (não no índice) | `1693-T8-LUS-46-300` | ✔ | f.300: «Catalogus 4us Defunctorum in Lusitana Provincia a Congregatione Provinciali habita Mense Aprili an. 1690 usq. ad Congregationem… an. 1693» |
| 1693 | **T8** | 301–302v | (não no índice) | `1693-T8-LUS-46-301` | ✔ | f.301: «Catalogus 5us Dimissorum in Lusitana Provincia… 1690 usq. … 1693» |
| 1693 | T5 (índice) | 303–308 | 307–312 | — (sem nota) | ✔ | ficheiros 303–308 = índice alfabético (letras até P); f.309 inicia o índice de 1696 («A.» + «1696» a lápis) |
| 1693 | T6 | — | 304 | — | — | o índice chama «Supplementa 304» ao catálogo dos defuntos (f.300) |
| 1693 | **T2** | — | — | — | **ausente** | linha «Catalogus II» vazia no índice; nenhum catálogo secreto entre f.299 e f.300 |
| 1696 | T5 (índice) | 309–313 | 313–317 | — (sem nota) | ✔ | ficheiros 309–313 = índice alfabético (A, D, E/F, S/T) |
| 1696 | T1 | 314–343v | 319–349 | `1696-T1-LUS-46-319` | ✔ | f.314: «Catalogus Primus Provinciae Lusitanae ann. 1696» |
| 1696 | T2 | 344–358v | 350–364 | `1696-T2-LUS-46-350` | ✔ | f.344: «Catalogus Secretus Provinciae Lusitanae anns 1696» |
| 1696 | T3 | 360–363v | 366–369v | `1696-T3-LUS-46-366` | ✔ | f.360: «Catalogus 3us Provinciae Lusitanae anns 1696» |
| 1696 | T6 (suppl.) | 364–369 | 370–375 | — (sem nota) | — | índice «Supplementa 370-375»; ficheiro 370 = f.376 «Finis» |

**Totais:** 6 anos; 17 catálogos com nota (6×T1, 5×T2, 6×T3) + 2 catálogos T8 descobertos em 1693.
Suplementos e índices alfabéticos ficam **registados na tabela/JSON mas sem nota dedicada**, seguindo
o critério do ensaio do LUS. 45 (T1/T2/T3).

## 3. LUS. 46 a — o que é (e porque ganhou nota)

`LUS. 46 a` (92 imagens = capa + nota + 45 fólios) **não é um suplemento do LUS. 46**: é um
**catálogo trienal de 1700**, autónomo. A capa diz «LUS. 46a. CAT. TRIE. 1700» e o verso da capa
(`000v.jpg`) tem a nota manuscrita:

> «Hic catalogus anno 1693 compositus additamentis posterioribus pro anno 1700 adaptatus est. T.»

Conteúdo verificado: **Catálogo I de 1700, ff. 1–39** («Catalogus 1us Provinciae Lusitanae anno
1700. Domus Professa Ulyssiponensis», f.1; numeração de pessoas até ~660) + **índice alfabético,
ff. 40–45** («Index … Anni …», letras A–V).

- **Nota criada:** `1700-T1-LUS-46a-1` (78 imagens embutidas).
- **Duplicado parcial** do Catálogo I de 1700 do LUS. 47 (ff. 8–33v): mesma província e ano, mas
  versão mais desenvolvida (45 fólios contra ~26). O Lead deve decidir qual é a ligação canónica
  no master list; sugiro manter as **duas** (são cópias distintas, uma «composta em 1693»).
- `data/LUS-46a.json` foi criado para além dos dois ficheiros pedidos porque o gerador precisa de
  um `volume_folder` próprio (as gamas de fólios colidem com as do LUS. 46).

## 4. Notas pré-existentes / nomes

- **Nenhuma** nota de catálogo do LUS. 46 existia na vault.
- Notas de volume usadas no link: `01 Notes/ARSI Lusitania 46.md`, `01 Notes/ARSI Lusitania 46 "1678 - 1696".md`, `01 Notes/ARSI Lusitania 46a.md` (não editadas).

## 5. Gaps, duplicados, ambiguidades

1. **1693 sem Catalogus II (secretus)** — a linha do índice está vazia e não há catálogo secreto
   entre o Cat. III (f.299) e os catálogos de defuntos/despedidos (f.300). Registado como gap, não inventado.
2. **Catálogos T8 de 1693 não constam do índice dactilografado** (ff. 300–302): «Catalogus 4us
   Defunctorum 1690-1693» e «5us Dimissorum 1690-1693». Foram indexados por leitura directa.
3. **1690**: o índice põe o índice alfabético (187-192) **antes** do Cat. I; o «Supplementa» tem
   duas localizações (209 e 243) e o primeiro cai dentro do Cat. I.
4. **1685**: Catálogo III encadernado antes do índice e do Catálogo II; a célula do índice
   alfabético («158/62») está corrigida à máquina e é pouco legível — gama 158–162 deduzida.
5. **1678**: o índice dá Cat. III como 43–46, mas a página de título está no f.42 (carimbo 42/43);
   a nota começa no ficheiro 042. Desvio de 1 fólio documentado.
6. **Desvio ficheiro↔carimbo** (secção 1): as gamas das notas embutem os ficheiros certos, mas
   quem citar fólios do índice deve aplicar o desvio. Sem folhas em falta na digitalização
   (001–370v contínuos); as folhas não filmadas são páginas em branco/título.
7. **Suplementos e índices alfabéticos** não têm nota dedicada (decisão de granularidade);
   estão integralmente descritos no JSON para uma segunda passagem, se o Lead quiser.

## 6. Validação

`python3 tools/validate.py` (só as entradas deste volume):
`LUS-46.json — 19 catalogues | verified 19 | notes existing 19 | image links 652 | 0 problems`;
`LUS-46a.json — 1 catalogue | verified 1 | notes existing 1 | image links 78 | 0 problems`.
(O relatório global do validador mostra 13 problemas, todos do `LUS-41.json` de outro agente,
em curso; não são deste volume.)

## 7. Para decisão do Lead

1. Granularidade: mantive T1/T2/T3 (como no ensaio do LUS. 45) + os dois T8 de 1693; suplementos
   e índices alfabéticos sem nota. Criar notas para T5/T6 também?
2. Nomenclatura: em LUS. 46 os nomes das notas usam o fólio **do índice** (`1678-T3-LUS-46-42`
   usa o ficheiro 042 mas o índice diz 43). Alternativa: renomear para o fólio do ficheiro.
3. LUS. 46 a: manter nota própria (sugerido) e ligar no master list; é duplicado parcial do 1700 do LUS. 47.
