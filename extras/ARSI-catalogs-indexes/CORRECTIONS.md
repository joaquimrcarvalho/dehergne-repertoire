# Correções registadas

> Registo cronológico das correções feitas ao índice dos catálogos. Cada correção
> é aplicada primeiro na tabela JSON do volume (`data/LUS-XX.json`, campo
> `corrections`) e depois propagada às notas, aos índices (Markdown/HTML/Obsidian)
> e aos relatórios.
>
> Como registar uma correção (exemplo):
>
> ```bash
> cd /Users/jrc/mhk-home/sources/dehergne
> python3 extras/ARSI-catalogs-indexes/tools/correct_entry.py \
>   --volume LUS-45 --note 1658-T1-LUS-45-251 \
>   --field folio_end --value 266v \
>   --reason "o intervalo incluía a primeira página do catálogo seguinte" \
>   --evidence "f.267 mostra o título do catálogo seguinte (imagem lida)"
> ```
>
> O comando altera o JSON, acrescenta o histórico `corrections` à entrada,
> acrescenta uma linha a esta tabela e regenera: a nota do catálogo, o pacote
> Markdown (`catalogos/`, índices), as notas-índice do Obsidian, a secção do
> master list, os relatórios e as páginas HTML.
>
> Para só registar a correção (sem propagar): `--no-refresh`.
> Para pré-visualizar: `--dry-run`.
>
> **Registo humano (Obsidian):** «Correções ao índice dos catálogos (entrada)» (nota Obsidian) — uma linha por correção, em linguagem corrente; ver `CORRECTIONS-WORKFLOW.md` para o procedimento do agente.

| Data | Volume | Nota | Campo | Antes | Depois | Motivo | Evidência |
|---|---|---|---|---|---|---|---|
| 2026-10-24 | LUS-44 | 1625-T5-LUS-44II-430 | image_end_file | (11 imagens) | 0432v-0433.jpg | nota antiga juntava T5 + T3 1625 + Rol 1627 + início do T1 1628 | leitura de 0432v-0433, 0433v-0434, 0437v-0438 |
| 2026-10-24 | LUS-44 | 1627-T10-LUS-44II-438 | folio_end | 438 | 438v | faltava a última página do rol (f.438v); imagem 0438v-0439 é partilhada com o início do T1 de 1628 | leitura de 0438v-0439 |
