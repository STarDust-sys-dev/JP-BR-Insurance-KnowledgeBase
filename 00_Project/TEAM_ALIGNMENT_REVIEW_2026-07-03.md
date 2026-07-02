# TEAM_ALIGNMENT_REVIEW_2026-07-03 - Revisao editorial diaria ACC

## Controle

- Versao: 0.1
- Data: 2026-07-03
- Autor: JP-BR Insurance Knowledge Base
- Historico: Revisao diaria com lentes de NotebookLM, portugues de atendimento, japones tecnico, seguro/risco no Japao e auditoria estrutural.

## Objetivo da revisao

Verificar se a producao ACC recente continua alinhada ao objetivo central do projeto: o corretor japones consulta a base, entende o tema em japones e consegue explicar em portugues brasileiro simples para cliente brasileiro residente no Japao, sem prometer cobertura, aceitacao, pagamento, prazo, culpa, imposto ou decisao da seguradora.

## Resultado executivo

A validacao estrutural passou sem erros, sem romaji, sem referencias quebradas e sem DOCX/PDF faltante. A revisao editorial encontrou dois pontos principais:

- A navegacao ACC para NotebookLM precisava expor de forma mais clara os lotes `ACC-0021` a `ACC-0040`, `FAQ-ACC-0021` a `FAQ-ACC-0040` e os dialogos/casos `0011-0014`.
- A frase de `口座情報確認` podia soar como pagamento ja aprovado; foi ajustada para condicionar o risco de atraso a aprovacao do pagamento.

## Correcoes aplicadas

- `16_NotebookLM/ACC_INDEX_0001.md`: ampliado para `ACC-0001` a `ACC-0040`, com perguntas naturais em japones sobre prazo, tratamento, sintomas, notificacoes, documentos adicionais, dados bancarios e traducao.
- `10_Accident/ACC_NAVIGATION_GUIDE.md`: ampliado para cobrir os lotes recentes e os dialogos/casos `0011-0014`.
- `02_MasterDictionary/ACC/ACC-0038.md` e `14_FAQ/ACC/FAQ-ACC-0038.md`: frase ao cliente ajustada para "Se o pagamento for aprovado, os dados bancarios precisam estar corretos para evitar atraso."
- `19_Markdown/ACC/ACC_TERMS_0031_0040.md` e `19_Markdown/ACC/ACC_FAQ_0031_0040.md`: consolidados sincronizados com a correcao de compliance.
- DOCX/PDF finais de ACC afetados foram verificados por renderizacao.

## Backlog editorial

1. Normalizar a familia tecnica `急激`, `偶然`, `外来` para uma decisao terminologica documentada, avaliando `急激性`, `偶然性` e `外来性` sem alterar traducoes aprovadas sem justificativa.
2. Reforcar `労災保険` como sistema publico/empresa de acidente de trabalho e trajeto quando aparecer fora de contexto, para evitar leitura como seguro privado.
3. Reavaliar `整骨院` em portugues brasileiro, evitando equivalencia direta com clinica medica brasileira.
4. Melhorar frases repetitivas de "proximo passo" nas FAQs ACC `0021-0040`, substituindo respostas genericas por orientacao pratica especifica por tema.
5. Considerar consolidados ACC amplos ou um mapa de consulta unico para reduzir risco de chunking no NotebookLM.
6. Transformar `FIRE_NOTEBOOKLM_PACK_0001.md` e `HOME_NOTEBOOKLM_PACK_0001.md` em pacotes praticos, nao apenas indices semelhantes.

## Validacao

- `python3 00_Project/validate_project.py`: aprovado.
- Renderizacao DOCX para PNG/PDF: aprovada por folhas de contato para `ACC_INDEX_0001`, `ACC_NAVIGATION_GUIDE`, `ACC_NOTEBOOKLM_PACK_0001`, `ACC_TERMS_0031_0040`, `ACC_FAQ_0031_0040`, `ACC_DIALOGUES_0011_0014` e `ACC_CASES_0011_0014`.

## Referencias

- `README.md`
- `EDITORIAL_RULES.md`
- `01_Editorial/AGENT_ALIGNMENT_BRIEF.md`
- `01_Editorial/SUBAGENT_EDITORIAL_WORKFLOW.md`
- `16_NotebookLM/ACC_INDEX_0001.md`
- `16_NotebookLM/ACC_NOTEBOOKLM_PACK_0001.md`
- `10_Accident/ACC_NAVIGATION_GUIDE.md`

## Veja tambem

- `19_Markdown/ACC/ACC_TERMS_0031_0040.md`
- `19_Markdown/ACC/ACC_FAQ_0031_0040.md`
- `19_Markdown/ACC/ACC_DIALOGUES_0011_0014.md`
- `19_Markdown/ACC/ACC_CASES_0011_0014.md`
