# «Catalogo dos Sogeitos, que entrarão em a Comp.ª de Jesus na Provincia de Portugal»

**Fonte nova (primária):** BNP, Pombalina 231 — «Catalogo dos Sogeitos, que entrarão em a Comp.ª de Jesus
na Provincia de Portugal: Começa em Jan.º de 1711. Tem folhas 247» — digitalização em https://purl.pt/47525
(510 imagens de trabalho em `results/_scratch/bnp47525/hires_NNNNNN.jpg`).
Cada assento dá: nome, naturalidade e diocese, filiação, data e lugar do baptismo e, em especial,
**«Entrou no Noviciado de Coimbra / Évora / Lx.ª … aos <dia> de <mês> de <ano>»** — exactamente o dado
que o Dehergne omite.

**Testemunho alternativo (impresso):** o mesmo catálogo, com coluna **NOVICIADO**, publicado como apêndice ao
*Catalogus Provinciae Lusitanae* de 1910 (n.os 1-351, primeiros nomes A-E) e de 1911 (n.os 352-940, F-J).
Texto extraído em `results/_scratch/app1910.txt` (1910) e `results/_scratch/appendix.txt` (1911);
PDF em `results/_scratch/LUSITANIAE_1910.pdf` e `LUSITANIAE_1911.pdf`.

## Calibração das imagens (verificada)

- O fólio de título é a imagem `hires_000009.jpg`.
- Fólio **f** (numeração no canto superior direito) ↔ imagem: `imagem = 2f + 9` para f ≤ 41;
  `imagem = 2f + 7` para f ≥ 42 (há duas páginas ausentes/duplicadas por volta dos ff. 37-41, o que
  desloca o offset em -2). Exemplos verificados: p. 172 = `hires_000351.jpg`; f. 131r = `hires_000269.jpg`.
- As imagens pares são, em regra, versos (muitas vezes em branco); a paginação impressa no canto
  superior direito foi conferida numa amostra (11→1, 91→42, 201→97, 251→122, 351→172, 451→223).

## Estrutura do volume (verificada por leitura de imagem)

O registo **não está ordenado por data de entrada**: está ordenado **alfabeticamente pelo primeiro nome**
(Antonio/Agostinho/Amaro → Bento/Bernardo → Caetano → Diogo/Domingos/Duarte → Estevão/Estanislau →
Felipe/Felix/Fernando/Francisco → Gabriel/Gaspar → Hieronimo/Hilario → Ignacio/Inacio →
Joaquim/João/José → Lourenço/Luís → Manuel/Martim/Matheus/Miguel → …), e **dentro de cada nome,
em ordem cronológica** (1711 → 1758). Muitos cadernos ficaram em branco:

| secção | fólios | imagens |
|---|---|---|
| A (Antonio, Agostinho, Amaro, André…) | ff. 1-27 (início) | 11-… |
| B (Bento, Bernardo, Basílio, Brás) | ff. 28-30 | 65-69 |
| C (Caetano) | ff. ~41-44 | 89-94 |
| D (Diogo, Domingos, Duarte, Diniz) | ff. 51-54 | 109-116 |
| E (Estevão, Estanislau, Eusébio, Eleutério) | ff. 65 | 137-138 |
| F (Felipe, Félix, Fernando, Francisco) | ff. 69-72 | 145-151 |
| I/J (Ignacio, Inacio, Joaquim, João, José) | ff. 94-107 | 197-222 |
| L (Lourenço, Luís) | ff. ~119-121 | 245-250 |
| M (Manuel, Martinho, Matheus, Miguel, Matias) | ff. 130-141 | 267-289 |
| N-O-P… (Pedro, Paulo, Policarpo…) | ff. 143-247 | 293-… |

**Lacunas da digitalização:** a imagem `hires_000220.jpg` é uma segunda digitalização do f. 105v
(confirmado por comparação de imagem: mesmo texto, incluindo a nota marginal «Bonavires»), pelo que o
**f. 106v não existe no conjunto** — é justamente o fólio onde cairia a entrada de João Simões (17-V-1734).
Há ainda duplicações em (102,104), (163,165), (208,210), (337,343), (342,344) e (469,471).

## Resultado (14 pessoas)

| id | lugar de entrada | data | conf. | prova |
|---|---|---|---|---|
| deh-andre-pereira | **não encontrado** | 1707-06-17 | nenhuma | entrada anterior a Jan.º 1711 — fora do âmbito do registo (fólio de título) |
| deh-caetano-lopes | **não encontrado** | 1707-02-17 | nenhuma | idem; apêndice impresso (A-E) não tem nenhum «Caetano Lopes» |
| deh-francisco-da-costa | **não encontrado** | 1707-02-09 | nenhuma | idem; o único homónimo do apêndice entrou em 1716 (Fatauncos/Coimbra) |
| deh-luis-de-sequeira | **não encontrado** | 1709-09-01 | nenhuma | idem; o apêndice só publica os primeiros nomes A-J (nenhum «Luís») |
| deh-francisco-alberto | **não encontrado** | 1710-03-01 | nenhuma | idem; apêndice sem «Francisco Alberto» |
| deh-martim-correa | **Lisboa** (Noviciado de Lisboa) | 1720-08-15 | alta | f. 131r (`hires_000269.jpg`): «Martinho Correa n.º de Lx.ª Ocidental … entrou para estudante no Noviciado de Lx.ª aos 15 de Agosto de 1720» |
| deh-joao-de-lemos | **Coimbra** (Noviciado de Coimbra) | 1726-06-02 | alta | f. 103v (`hires_000214.jpg`): «Joam de Lemos n.º de Quintella Bispado de Lamego entrou no Noviciado de Coimbra aos 2 de Junho de 1726»; apêndice n.º 654 |
| deh-joao-de-seixas | **não encontrado** | 1727-11-25 ou 1729-11-25 | nenhuma | secção J, ff. 103v-105r (1726-1731) sem nenhum João de Seixas; apêndice n.os 640-760 também não; Wicki: falta nos catálogos portugueses de 1737 e 1740 |
| deh-felix-da-rocha | **Lisboa** (Noviciado de Lisboa) | 1728-05-01 | alta | f. 72r (`hires_000151.jpg`): «Felis da Rocha n.º de Lisboa entrou no Noviciado da mesma Cidade aos 1.º de Maio de 1728»; apêndice n.º 406 |
| deh-manuel-jose | **não encontrado** | 1729-08-20 (ou 08-02) | nenhuma | secção M (Manoel), ff. 130r-135v — as folhas de 1729 não o contêm; o único «Manoel Jozé» do registo é de 1721 (f. 131v); apêndice impresso não cobre M |
| deh-manuel-viegas | **Évora** (Noviciado de Évora) | 1729-07-31 | alta | f. 134v (`hires_000276.jpg`): «Manoel Viegas n.º de Marvam Bispado de Portalegre entrou no Noviciado de Évora para estudante aos 31 de Julho de 1729» |
| deh-bento-monteiro | **Coimbra** (Noviciado de Coimbra) | 1732-06-27 | alta | f. 29r (`hires_000067.jpg`): «Bento Monteyro n.º de Coimbra … Entrou no Nov.º de Coimbra a 27 de Junho de 1732»; apêndice n.º 212 |
| deh-joao-de-loureiro | **Lisboa** (Noviciado de Lisboa) | 1732-05-03 | alta | f. 105v (`hires_000218.jpg`): «Joam Loureiro n.º de Lx.ª entrou p.º Estud.º no Nov.º de Lx.ª aos 3 de Maio de 1732»; apêndice n.º 716 |
| deh-joao-simoes | **não encontrado** | 1734-05-17 | nenhuma | o f. 106v (Abril 1734-Maio 1735) **falta na digitalização** (a imagem 220 duplica o f. 105v); apêndice (1734-1735) não o regista |

## Notas de método

- Todas as citações do registo são de **imagem lida directamente** (`read_image`), nunca de OCR:
  o OCR (tesseract/Vision) é inutilizável neste manuscrito.
- O apêndice impresso foi usado como testemunho alternativo e **verificado** contra o manuscrito em
  quatro casos (Félix da Rocha n.º 406 = f. 72r; Bento Monteiro n.º 212 = f. 29r; João de Lemos n.º 654 =
  f. 103v; João de Loureiro n.º 716 = f. 105v) — coincidência perfeita.
- **Lugar de entrada ≠ residência posterior**: os noviciados de Lisboa (Monte Olivete, depois Santo Antão),
  Coimbra e Évora; o Noviciado das Missões de Arroios só abre a 27 de Abril de 1735.
