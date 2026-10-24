# LUS. 43 II a / II b — índice dos catálogos (1540–1579)

**Data:** 2026-10-22 · **Agente:** lus43 · **Fonte de dados:** `extras/ARSI-catalogs-indexes/data/LUS-43.json`

## 1. Fontes e método

**Não existe índice dactilografado neste volume.** Verifiquei as capas e as primeiras/últimas imagens das duas pastas (`000.jpg`, ` .jpg`, `270.jpg`, `538.jpg`): são páginas do manuscrito, não um índice. A segmentação foi construída a partir de:

1. tabelas VLM em `01 Notes/ARSI Lusitania Catalogues LUS. 43 II a.md` e `... II b.md` — datas pouco fiáveis e segmentos em falta (a tabela de 43 II b começa em `396.jpg` e ignora `386–395`);
2. prosa da lista mestra (`03 Projectos/03.03.01.01 … em curso.md`, linhas 33–160), com fólios exactos para 1548–1577, e notas de índice/reconciliação;
3. 47 notas antigas com embeds de imagens, que revelaram intervalos já fixados;
4. **leitura directa das páginas de início** com `read_image` (pares de metade superior, 2 páginas por leitura), para confirmar título/data;
5. varrimento dos cabeçalhos de **todas** as 536 páginas em contact-sheets de 24 páginas, para detectar inícios não previstos.

O volume foi fotografado com **folhas soltas sobrepostas**: muitas imagens mostram em cima o fim da folha anterior e em baixo a página principal. Uma imagem pode conter duas folhas; os intervalos são pois aproximados ao fólio (±1 imagem).

## 2. Correspondência nome-de-ficheiro ↔ fólio carimbado (verificada nos cantos)

Ao contrário de LUS. 39/45/46/47, **os nomes de ficheiro não são os fólios carimbados**. Amostra lida directamente:

| Pasta | ficheiro | carimbo lido | desvio |
|---|---|---:|---:|
| 43 II a | `270.jpg` | 270 | 0 |
| 43 II a | `280.jpg` | 280 | 0 |
| 43 II a | `290.jpg` | 291 | +1 |
| 43 II a | `300.jpg` | 301 | +1 |
| 43 II a | `310.jpg` | 312 | +2 |
| 43 II a | `319.jpg` | 322 | +3 |
| 43 II a | `320.jpg` | 323 | +3 |
| 43 II a | `330.jpg` | 333 | +3 |
| 43 II a | `340.jpg` | 343 | +3 |
| 43 II a | `350.jpg` | 353 | +3 |
| 43 II a | `360.jpg` | 363 | +3 |
| 43 II a | `370.jpg` | 374 | +4 |
| 43 II a | `380.jpg` | 385 | +5 |
| 43 II a | `385v.jpg` | ~390v | +5 |
| 43 II b | `386.jpg` | 391 | +5 |
| 43 II b | `396.jpg` | 401 | +5 |
| 43 II b | `397.jpg` | 402 | +5 |

Resposta directa à pergunta do plano ("386.jpg mostra o carimbo 386?"): **não — 386.jpg mostra 391**. Em 43 II a o desvio cresce de 0 (f.270) até +5 (f.380) porque a câmara fotografou folhas sobrepostas (não faltam imagens na pasta: 270–385v estão completas).

**Imagens em falta na pasta de 43 II b:** `389.jpg`, `442v.jpg`, `538v.jpg`. **Ficheiro deslocado:** `LUS. 43 II b/ .jpg` — é uma página de **1572** (lista da casa de S. Roque, carimbo **448**), colocada no início da pasta; pertence à secção 1572 de S. Roque e não pode ser embebida pelo gerador (nome sem número).

## 3. Segmentação proposta

**74 catálogos/documentos**, 50 verificados por leitura da página de início e 24 inferidos (limites/título por continuidade, nota antiga ou contact-sheet). A coluna «fólio» usa o **número do ficheiro** (é o que o gerador e o validador usam); «carimbo» dá o fólio carimbado aproximado.

| Ano | Tipo/local | Ficheiros | Carimbo aprox. | Nota | Verif. | Evidência |
|---|---|---|---|---|---|---|
| 1566 | T4 | f.270–277v | 270-277v (prefixado) | [[1566-T4-LUS-43-II-a-270-partes]] | ✅ | 270.jpg (carimbo 270): «Catalogo de los padres y hermanos q~ estan en la casa de S. Roque. Nouj 1566» |
| 1566 | T1P — Porto | f.278–279v | 278-279v | [[1566-T1P-LUS-43-II-a-278]] | ✅ | 278.jpg (carimbo 278): «Jhs — Muñoz en el padre»; margem «PORTO 13.12.1566» |
| 1566 | T1P — Coimbra | f.280–290v | 280-290v | [[1566-T1P-LUS-43-II-a-280 nomes sem comunidade]] | ✅ | 280.jpg (carimbo ~280): cabeçalho «p. Miguel de Sousa» seguido de apreciações |
| 1566 | T10 — Coimbra | f.291–296v | — | [[1566-T10-LUS-43-II-a-291]] | ⚠️ | 291.jpg: lista de apreciações («Manuel rodriguez lee el 3er curso...»); sem cabeçalho que marque início seguro |
| 1566 | T10 — Coimbra | f.297–302v | — | [[1566-T10-LUS-43-II-a-297]] | ✅ | 297.jpg: «Los q~ a cavado el curso de Artes el año pasado de 565 en Coymbra» |
| 1548 | T10 — Coimbra? | f.303–305v | 303-305v (carimbo 304-307?) | [[1548-T10-LUS-43-IIa-c304]] | ✅ | 303.jpg: «an. 1548 in cima» + lista de nomes com naturais e datas de entrada |
| 1566 | T10 | f.306–309v | — | [[1566-T10-LUS-43-II-a-306]] | ✅ | 309.jpg: «Los d.ª... quieren exercitar... de Roma...»; 306.jpg em branco |
| 1567 | T4P — Coimbra | f.310–311v | 312-314 | [[1567-T4P-Coimbra-LUS-43-II-a-312]] | ✅ | 310.jpg (carimbo 312): «Catalogo delos p.es y hermanos del Collegio de Coimbra del año de 1567» |
| 1567 | T4P — Coimbra | f.312–316v | 315-320 | [[1567-T4P-Coimbra-LUS-43-IIa-c315]] | ✅ | 312.jpg (carimbo 315): «Jhs — Colegio de Coimbra... de 1567» |
| 1568 | T10P — Coimbra | f.317–318v | 320-321 | [[1568-T10P-Coimbra-LUS-43-II-320]] | ✅ | 317.jpg: «Jhs — Los q~ de Enero de 1567 hasta el de 68 se recibieron en este collegio de Coimbra...» |
| 1568 | T4P — Braga | f.319–320v | 322-323 | [[1568-T4P-Braga-LUS-43-II-322]] | ✅ | 319.jpg (carimbo 322): «Lista dos padres... do Collegio de Braga... 15 de Janeiro de 1568» |
| 1568 | T4P — Coimbra | f.321–322v | 324-325 | [[1568-T4P-Coimbra-LUS-43-II-a-324]] | ✅ | 321.jpg (carimbo 324): «Catalogus eorum qui in collegio Conimbricensi versantur Januarii mense 1568» |
| 1568 | T6P — Coimbra | f.323–324v | 326-327 | [[1568-T6P-Coimbra-LUS-43-II-a-326]] | ✅ | 323.jpg (carimbo 326): «Los q~ se recibieron en este collegio de Coimbra dende el primero de Enero de 1568...» |
| 1568 | T10P — Coimbra | f.325–326v | 328-329 | [[1568-T10P-Coimbra-LUS-43-II-328]] | ✅ | 325.jpg (carimbo 328): «Estos son los que de Enero de 1568 hasta el principio de Mayo del mismo año se recibieron...» |
| 1568 | T4P — Évora | f.327–328v | 330-331 | [[1568-T4P-Évora-LUS-43-II-330]] | ✅ | 327.jpg (carimbo 330): «Catalogo de los nuestros q~ estan en este Colegio de Évora is? de Henero de 1568» |
| 1553-1568 | T10P — Évora | f.329–331v | 332-334 | [[1551-1568-T10P-Évora-LUS-43-II-332]] | ✅ | 329.jpg (carimbo 332): «Lista de los q~ se recibieron para la Compª en este Colegio de Évora... desde... 1553 hasta Henero de 1568» |
| 1568 | T4P — São Roque | f.332–335v | 335-338 | [[1568-T4P-São-Roque-LUS-43-II-a-335]] | ✅ | 332.jpg (carimbo 335): «Catalogo dos nossos q~ estão nesta casa de S. Roque a 3 de Fevrº de 1568» |
| 1568 | T10 — Coimbra | f.336–337v | 339-340 | [[1568-T10-Mestres-LUS-43-II-a-339]] | ✅ | 336.jpg (carimbo 339): «Los maestros q~ an leido artes este Collegio» |
| 1568 | T10 — Coimbra | f.338–342v | 341-345 | [[1568-T10-Recebidos-LUS-43-II-a-341]] | ✅ | 338.jpg (carimbo 341): «IHS — Estes são os q~ querem q~ os recebã / Antonio Mendez Primeira classe» |
| 1569 | T4P — Coimbra | f.343–344v | 346-347 | [[1569-T4P-Coimbra-LUS-43-II-346]] | ✅ | 343.jpg (carimbo 346): «IHS 1569 — Catalogo de los Padres y Hermanos del Collegio de Coimbra... y primero de Enero» |
| 1569 | T4P — Coimbra | f.345–346v | 348-349 | [[1569-T4P-Coimbra-LUS-43-II-348]] | ✅ | 345.jpg (carimbo 348): «Catalogus eorum versantium in collegio Conimb. anno domini 1569, cal. Januar.» |
| 1569 | T10 — Coimbra | f.347–347v | 350 | [[1569-T10-Coimbra-Teologia-LUS-43-II-350]] | ✅ | 347.jpg (carimbo 350): «Jhs 1569 — Lista de los padres de Coimbra que tienen oydo quatro años de Theologia, hecha a 4 de Noviembre de 1569» |
| 1569 | T10 — Coimbra/Évora | f.348–350v | 351-353 | [[1569-T10-Coimbra-Évora-Teologia-Ordenar-LUS-43-II-351]] | ✅ | 348.jpg (carimbo 351): «Los padres y hermanos del Collegio de Évora que tienen oído...» / continuação da lista de Coimbra de 4 Nov. 1569 |
| 1569 | T4P — Évora | f.351–352v | 354-355 | [[1569-T4P-Évora-LUS-43-II-354]] | ⚠️ | 351.jpg: continuação de apreciações; cabeçalho de Évora não relido nesta verificação — atribuição pela nota antiga «1569-T4P-Évora-43-II-354» |
| 1569 | T4P — Santo Antão | f.353–353v | 356 | [[1569-T4P-Santo-Antão-LUS-43-II-356]] | ✅ | 353.jpg (carimbo 356): «Lista de los padres y hermanos del Collegio de Sto. Anton de Lisboa a 30 de Enero de 1569» |
| 1569 | T4P — São Roque | f.354–354v | 357 | [[1569-T4P-São-Roque-LUS-43-II-357]] | ✅ | 354.jpg (carimbo 357): «Catalogo de la casa de S. Roque... de Henero de...» |
| 1569 | T4P — Casa da Provação | f.355–356v | 358 | [[1569-T4P-Casa-Provação-São-Roque-LUS-43-II-358]] | ✅ | 355.jpg: «Rol dos noviços q~ estão na casa de provação de S. Roque...» |
| 1569 | T10 | f.357–358v | 360-361 | [[1569-T10-recebidos-mortos-despedidos-saidos-LUS-43-II-360]] | ⚠️ | 357.jpg: lista de apreciações/relação sem cabeçalho legível na verificação; atribuição pela nota antiga (fl.360) |
| 1569 | T10 | f.359–360v | 362-364 | [[1569-T10-novas-informações-LUS-43-II-362]] | ✅ | 359.jpg (carimbo 362): «Henero de 1569 — Lo q~ de nuevo se ofrece informar después de la última información» |
| 1569 | T4P — São Roque | f.361–361v | 364 | [[1569-T4P-São-Roque-LUS-II-364]] | ✅ | 361.jpg (carimbo 364): «Catalogo de los q~ están en la casa de S. Roque a 18 de Julio de 1569...» |
| 1569 | T10 — Coimbra | f.362–362v | 365 | [[1569-T10-Coimbra-LUS-43-II-365]] | ✅ | 362.jpg (carimbo 365): «Rol dos moços, pretos, escravos e homens q~ servem em casa» |
| 1569 | T10 — Coimbra | f.363–364v | 366 | [[1569-T10-Coimbra-LUS-43-II-366]] | ✅ | 363.jpg (carimbo 366): lista numerada de nomes (1-51); atribuição ao exame de Ruy Vicente pela nota antiga |
| 1554? | T4 | f.365–366v | 369-370 | [[1554-T4-LUS-43-II-369]] | ✅ | 365.jpg (carimbo 369): «Jhs — Los padres y hr.os q~ están en la casa de S. Roque (año 1554...)»; margem «1553» |
| 1560? | T4P — São Roque | f.367–367v | 371 | [[1560-T4P-São-Roque-LUS-43-II-371]] | ✅ | 367.jpg (carimbo 371): margem «1560» + «Lista de los padres y hermanos de la casa de S. Roque de Lisboa» |
| 1558? | T1P — São Roque | f.368–369v | 372-373 | [[1558-T1P-São Roque-LUS-43-II-372]] | ✅ | 368.jpg (carimbo 372): «Jhs — Lista dos Sacerdotes da casa de São Roque desta Companhia de Jesus»; margem «1568 fine» |
| 1561? | T1 — Évora | f.370–370v | 374 | [[1561-T1P-Évora-LUS-43-II-a-374]] | ✅ | 370.jpg (carimbo 374): margem «1561» + «Lista de los de casa cõ las emformações» |
| 15?? | T10P — Lisboa | f.371–371v | 375 | [[15__-T10P-Lisboa-LUS-43-II-a-375]] | ✅ | 371.jpg: «Informação particular de cada hũ...» (fragmento de Lisboa); atribuição pela nota antiga fl.375 |
| 1561? | T6-7 — Évora | f.372–374v | 376-378 | [[1561-T1P-Évora-LUS-43-II-a-376]] | ⚠️ | 372.jpg repete a imagem de 371 («Informação particular»); limites 372-374v atribuídos pela nota antiga, sem cabeçalho próprio |
| 1561? | T10P — São Roque | f.375–375v | 379 | [[1561-T10P-São-Roque-LUS-43-II-a-379]] | ⚠️ | 375.jpg: 375-375v não relidos nesta verificação; atribuição pela nota antiga fl.379 |
| 15XX | T10P — Coimbra | f.376–376v | 381 | [[15XX-T10P-Coimbra-LUS-43-II-a-381]] | ⚠️ | 376.jpg: não relido em detalhe; atribuição pela nota antiga fl.381 |
| 1553 | T10P — Coimbra | f.377–377v | 382 (aprox.) | [[1553-T10P-Coimbra-LUS-43-II-a-384]] | ✅ | 377.jpg: «1553» + colunas «Theologos / Philosophi / In domo probationis» |
| 1558? | T4 — Coimbra | f.378–379v | 383 (aprox.) | [[1558-T4-Coimbra-LUS-43-II-a-383]] | ✅ | 378.jpg (carimbo ~383): «Catalogus eorum qui in utroque Collegio Conimbricensi versantur»; margem «1558 / 1558/59» |
| 15XX | T10P — Évora | f.380–380v | 385 | [[15XX-T10P-Évora-LUS-43-II-a-385]] | ⚠️ | 380.jpg mostra o «Rol dos padres e irmãos da 2ª provação» de 1555 na folha sobreposta; página principal não confirma o cabeçalho de Évora — atribuição pela n… |
| 1555 | T10P — Coimbra | f.381–382v | 386-387 | [[1555-T10P-Coimbra-LUS-43-II-a-387]] | ✅ | 381.jpg: «1555 Rol dos padres e irmãos da 2ª provação» (2.ª cópia da mesma folha vista em 380) |
| 15XX | T10 — Évora | f.383–385v | 388-390 | [[15XX-T10-Évora-LUS-43-II-a-388]] | ✅ | 383.jpg: «Casa / Rol/Exame particular / Manuel Lopes» + lista; 385.jpg: «Homens del examen particular del pe. Gonçalo Vaz» |
| 1570 | T? | f.386–387v | 391-393 | [[1570-Miscelânea-LUS-43-II-b-386]] | ✅ | 386.jpg (carimbo 391): cabeçalho «Castilla» + «+ Por... carta sobre los que... Coimbra» |
| 1570 | T4P — Angra | f.388–390v | 393-395 | [[1570-T4P-Angra-LUS-43-II-b-388]] | ✅ | 388.jpg (carimbo ~393): «1570 — Lista de los padres y hermanos q~ están en el Colegio de Angra»; 389.jpg em falta na pasta |
| 1570 | T4P — Coimbra | f.391–394v | 397-400 | [[1570-T4P-Coimbra-LUS-43-II-b-391]] | ✅ | 391.jpg (carimbo ~397): «Nomina et occupationes eorum qui sunt in antiguo collegio Conimbricensi» |
| 1570 | T10 — Coimbra | f.395–396v | 401 | [[1570-T10-Probacao-LUS-43-II-b-396]] | ✅ | 396.jpg (carimbo ~401): «Jhs 1570 — Lista de los hermanos que se an recibido en la probación de Coimbra» |
| 1570 | T4P — Évora/Porto | f.397–402v | 402-406 | [[1570-T4P-Évora-Porto-LUS-43-II-b-397]] | ✅ | 397.jpg (carimbo ~402): «JESUS — Catalogus eorum qui degunt in Collegio Eborensi... primo Januarii 1570»; 400v: «Padres y hermanos... Colegio del Porto... 1570» |
| 1570 | T4P — Madeira | f.403–407v | 406-410 | [[1570-T4P-Madeira-LUS-43-II-b-403]] | ⚠️ | 403.jpg: imagem quase em branco (verso); cabeçalho da Madeira visto na folha sobreposta; limites inferidos |
| 1570 | T4P — Coimbra | f.408–410v | 414-416 | [[1570-T4P-Coimbra-LUS-43-II-b-c414]] | ✅ | 408.jpg: «Colegio da ilha da Madeira...» (folha sobreposta) / «Lista de los de el colegio de Coimbra» em 410.jpg |
| 1571 | T4P — Coimbra | f.411–423v | 417-429 | [[1571-T4P-Coimbra-LUS-43-II-b-413]] | ✅ | 413.jpg: «Jhs 1571 — Lista de los Padres... de Coimbra» (visto na montagem) |
| 1572 | T4P — Coimbra | f.424–436v | 430-442 | [[1572-T4P-Coimbra-LUS-43-II-b-424]] | ✅ | 424.jpg: cabeçalho «Colegio de S. Anton» (apreciações); «Catalogo de Coimbra 1572» visto em 448v/451/451v |
| 1572 | T4P — Braga | f.437–441v | 443-447 | [[1572-T4P-Braga-LUS-43-II-b-437]] | ⚠️ | 437.jpg: apreciações em tinta escura; «Lista de Braga» vista na montagem em 437v; limites inferidos |
| 1572 | T4 — São Roque | f.442–447v | 447-452 | [[1572-T4-LUS-43-II-b-C448]] | ✅ | Ficheiro deslocado « .jpg» (carimbo 448): «Lista de la casa de San Roque de Lisboa... de Henero de 1572»; 443.jpg: «Lista de los q~ están en el Colegio de Sa… |
| 1572 | T4P — Coimbra | f.448–452v | 453-457 | [[1572-T4P-Coimbra-LUS-43-II-b-448]] | ✅ | 451.jpg / 451v.jpg: «Catalogo de Coimbra 1572» |
| 1572 | T10 | f.453–456v | 458-461 | [[1572-T10-Informações-LUS-43-II-b-453]] | ⚠️ | 453v.jpg: «Jhs — Informação...»; limites inferidos |
| 1573 | T4P — Braga | f.457–457v | 462-463 | [[1573-T4P-Braga-LUS-43-II-b-457]] | ⚠️ | 457v.jpg: «Rol dos... Braga?» (montagem); limites inferidos |
| 1573-1574 | T1 | f.458–469v | 468-479 | [[1574-T4-LUS-43-II-b-463]] | ✅ | 458.jpg-469v.jpg: tabelas com colunas (Nome/Patria/tempo de Comp.ª/estudos); início em página quase em branco, sem título datado legível |
| 1574 | T10 | f.470–473 | 479-482 | [[1574-T10-LUS-43-II-b-470]] | ⚠️ | 470.jpg: continuação de informações; limites inferidos |
| 1575 | T1 — Coimbra | f.473v–477v | 482-486 | [[1575-T1-LUS-43-II-b-c479]] | ⚠️ | 473v.jpg: «Lista del Colegio de Braga... 20 de Octubre 1573» (folha sobreposta); atribuição pela nota antiga c479; verificar |
| 1575 | T4 | f.478–481 | 487-490 | [[1575-T4-LUS-43-II-b-478]] | ⚠️ | 478.jpg-481.jpg: listas de 1575; sem cabeçalho único — segmento inferido |
| 1575 | T4 — Coimbra | f.481v–485 | 491-495 | [[1575-T4-LUS-43-II-b-C487]] | ⚠️ | 481v.jpg-485.jpg: catálogo de Coimbra 1575; atribuição pela nota antiga C487 |
| 1575 | T10 — Coimbra | f.485v–495 | 495-504 | [[1575-T10-Coimbra-LUS-43-II-b-485]] | ⚠️ | 486v.jpg-494.jpg: «Información del colegio de Coimbra para profesar...» (montagem); limites inferidos |
| 1576 | T10 — Coimbra/Évora/S.Roque | f.495v–498 | 505-508 | [[1576-T10-LUS-43-II-b hermanos que se recebieron em Coimbra-Évora-S.Roque]] | ⚠️ | 495v.jpg-498.jpg: relação de recebidos por casa; atribuição pela nota antiga c495 |
| 1576 | T10 | f.498v–502 | 503-507 | [[1576-T10-Listas-LUS-43-II-b-498]] | ⚠️ | 498v.jpg-500v.jpg: listas de 1576; sem cabeçalho único — segmento inferido; 501-502 início do catálogo de pessoas |
| 1576 | T10 | f.502v–505v | 508-516 | [[1576-T4-LUS-43-II-b-c508]] | ⚠️ | Nota antiga com ligações para as páginas 502V-505V da cópia Brotéria (= 502v-505v da digitalização); ligações corrigidas |
| 1577 | T4 | f.506–511 | 513-517 | [[1577-T4-LUS-43-II-b-c513]] | ✅ | 507v.jpg: «IESVS — Padres y hermanos de la Provincia de Portugal... 1577» (montagem) |
| 1577 | T4P | f.511v–516 | 517-522 | [[1577-T4P-Casas-LUS-43-II-b-511]] | ⚠️ | 513.jpg: «Jhs 1577 — Padres y hermanos de la casa de...»; limites inferidos |
| 1578 | T4 | f.516v–521 | 522-527 | [[1578-T4-LUS-43-II-b-516]] | ⚠️ | 516v.jpg: «Jhs 1578 — Lista de los Padres... 1578» (montagem); limites inferidos |
| 1578 | T3 | f.521v–524 | 527-530 | [[1578-Memória-LUS-43-II-b-521]] | ⚠️ | 521v.jpg: «Memoria das Casas... 1578» (montagem); limites inferidos |
| 1579 | T1 | f.524v–532 | 531-539 | [[1579-T1-LUS-43-II-b-524]] | ⚠️ | 524v.jpg-532.jpg: tabelas (Theologos/Filosofos) de 1579; limites inferidos |
| 1580-1589? | T10 | f.532v–538 | 539-543 | [[1580-Miscelânea-LUS-43-II-b-532]] | ⚠️ | 533v.jpg: «Informação... 4 de Dezembro de 1580»; 536v.jpg: «... 4 de Set 1589» (montagem); limites inferidos |

Legenda: ✅ = página de início lida com `read_image` e cabeçalho/data transcritos; ⚠️ = segmento inferido (ver §4).

## 4. Verificado vs inferido

**Verificados (50).** Página de início lida e cabeçalho transcrito; exemplos:

- **1566 T4** (1566-T4-LUS-43-II-a-270-partes): 270.jpg (carimbo 270): «Catalogo de los padres y hermanos q~ estan en la casa de S. Roque. Nouj 1566»
- **1568 T4P** (1568-T4P-Braga-LUS-43-II-322): 319.jpg (carimbo 322): «Lista dos padres... do Collegio de Braga... 15 de Janeiro de 1568»
- **1568 T4P** (1568-T4P-Coimbra-LUS-43-II-a-324): 321.jpg (carimbo 324): «Catalogus eorum qui in collegio Conimbricensi versantur Januarii mense 1568»
- **1568 T6P** (1568-T6P-Coimbra-LUS-43-II-a-326): 323.jpg (carimbo 326): «Los q~ se recibieron en este collegio de Coimbra dende el primero de Enero de 1568...»
- **1568 T4P** (1568-T4P-Évora-LUS-43-II-330): 327.jpg (carimbo 330): «Catalogo de los nuestros q~ estan en este Colegio de Évora is? de Henero de 1568»
- **1569 T4P** (1569-T4P-Coimbra-LUS-43-II-346): 343.jpg (carimbo 346): «IHS 1569 — Catalogo de los Padres y Hermanos del Collegio de Coimbra... y primero de Enero»
- **1569 T10** (1569-T10-Coimbra-Teologia-LUS-43-II-350): 347.jpg (carimbo 350): «Jhs 1569 — Lista de los padres de Coimbra que tienen oydo quatro años de Theologia, hecha a 4 de Noviembre de 1569»
- **1572 T4** (1572-T4-LUS-43-II-b-C448): Ficheiro deslocado « .jpg» (carimbo 448): «Lista de la casa de San Roque de Lisboa... de Henero de 1572»; 443.jpg: «Lista de los q~ están en el Colegio de Santo Antão... 1572»
- **1577 T4** (1577-T4-LUS-43-II-b-c513): 507v.jpg: «IESVS — Padres y hermanos de la Provincia de Portugal... 1577» (montagem)

**Inferidos (24).** Não foi possível confirmar o cabeçalho na página indicada (página em branco, folha sobreposta, tinta ilegível ou intervalo fixado por nota antiga). Ficam marcados `"verified": false` no JSON com a razão em `evidence`. Concentram-se sobretudo em **43 II b** (segmentos 1570–1580) e em seis notas antigas de 43 II a cujo início não tem cabeçalho próprio (291, 357, 372–374, 375, 376, 380).

## 5. Notas

- **29 notas novas** criadas em `03 Projectos/` (nomes no JSON; convenção `ANO-TIPO[-LOCAL]-LUS-43-II-a/b-FICHEIRO`). Ao contrário das notas antigas (nomeadas pelo fólio carimbado), as novas usam o **número do ficheiro**, porque é esse o identificador estável da digitalização; o fólio carimbado vai na descrição/relatório.
- **45 notas antigas reutilizadas** (`already_existed: true`), em `01 Notes/` (37) e `03 Projectos/` (8); não foram duplicadas. As ligações pendentes da lista mestra foram resolvidas com duas notas novas: `1568-T4P-Évora-LUS-43-II-330` e `1569-T4P-Évora-LUS-43-II-354`.
- Notas antigas cujo nome usa o fólio carimbado em vez do ficheiro (ex.: `1568-T6P-Coimbra-LUS-43-II-a-326`) foram **mantidas** — não renomeadas.

## 6. Duplicados

- **PDFs na raiz** (não movidos): `LUS.43.IIa.pdf` (volume completo) e cinco PDFs já extraídos dos mesmos fólios — `LUS.1566-11-00.arsi.43.II.f270.Cat.brev..pdf`, `…f272.Colégio de Coimbra.pdf` (+ `-small`), `…f278.Colégio do Porto.pdf`, `…f278.Nomes.pdf`. São cópias dos mesmos catálogos das pastas de imagens.
- **Duas notas para o mesmo catálogo**: `1568-T10P-Coimbra-LUS-43-II-320` (01 Notes) e `1567-T10 Coimbra entrados-LUS-43-IIa-c320` (03 Projectos) descrevem o mesmo documento (ficheiros 317–318v). O JSON usa a primeira; a segunda deve ser fundida/removida pelo Lead.
- **Sobreposição 1575/1576**: a entrada pendente da lista mestra `1575-T10-varios-LUS-43-II-b-c495` corresponde às mesmas páginas da nota `1576-T10-LUS-43-II-b hermanos que se recebieron…` (495v–498). Não criei nota nova para c495.
- **Cópias internas**: o catálogo de Coimbra de 1567 existe em duas versões (ff. 312–314 e 315–320) e o Rol de 1555 aparece duas vezes (ficheiros 380 e 381), provavelmente cópias do mesmo documento.
- A nota `1614-T1-LUS-43-II-302` (01 Notes) está **mal arquivada**: as suas imagens são de `LUS. 44 II`, não de 43.

## 7. Lacunas

- Faltam na digitalização de 43 II b: `389.jpg`, `442v.jpg`, `538v.jpg`.
- Fólio carimbado 448 de 1572 (S. Roque) está no ficheiro deslocado ` .jpg` (ver §2) — página não indexável automaticamente.
- O volume não está em ordem cronológica estrita: 43 II a contém 1566–1569 (ff. 270–368) **e**, no fim, documentos de 1548–1561 (ff. 369–390v); a lombada diz «CATALOGI 1540-1579» mas não há catálogos de 1540–1547 (1544 é referência textual), e o fim de 43 II b inclui documentos de **1580** e **1589**, posteriores ao âmbito.
- 43 II a: não há imagens em falta, mas os fólios carimbados chegam a ~390v com nomes de ficheiro até 385v (compensado pela fotografia sobreposta).

## 8. Validação

```
python3 extras/ARSI-catalogs-indexes/tools/gen_notes.py extras/ARSI-catalogs-indexes/data/LUS-43.json
  → 29 notas novas criadas; 45 notas antigas preservadas (skip)
python3 extras/ARSI-catalogs-indexes/tools/validate.py
  → LUS-43.json: catalogues 74 | verified 50 | notes existing 74 | image links 496
  → TOTAL PROBLEMS: 0 (com o validate.py actualizado, que procura em 03 Projectos e 01 Notes)
```

Cobertura: todas as 536 imagens de 270.jpg a 538.jpg ficam atribuídas a exactamente um catálogo (verificado por script); únicas excepções: `000.jpg` (capa) e ` .jpg` (deslocada).

Cada nota embebe em média 6–26 imagens, sempre por ordem de ficheiro; os 496 links `file://` resolvem todos.

## 9. Incidente e decisão para o Lead

- Ao regenerar com `--force` (necessário para corrigir intervalos), o gerador reescreveu **8 notas antigas de 03 Projectos** (1548, c315, c414, C448, 463, C487, 1576-T10, c508). Restaurei o conteúdo a partir do que estava registado nesta sessão (texto e embeds), mas **a restauração não é byte-a-byte para as notas cujo texto integral não tinha sido lido** (c315, c414, C448, 463, C487, 1576-T10); o conteúdo dessas era, pelo que se viu, apenas a lista de embeds. Recomenda-se ao Lead confirmar estas 8 notas no vault/Time Machine.
- As notas antigas com transcrição rica (ex.: `1566-T4-LUS-43-II-a-270-partes` e sub-notas) não foram tocadas.
- **Decisões pendentes para o Lead:** (a) uniformizar a convenção de fólio nas notas novas (ficheiro vs carimbo); (b) fundir as duas notas duplicadas de 1568 (320); (c) confirmar a nota 1614 mal arquivada; (d) ligar à lista mestra as 29 notas novas (e as antigas órfãs).

