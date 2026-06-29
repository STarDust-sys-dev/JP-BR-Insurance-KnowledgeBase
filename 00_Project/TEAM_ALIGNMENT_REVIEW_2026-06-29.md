# TEAM_ALIGNMENT_REVIEW_2026-06-29 - Revisão de propósito e sintonia da equipe

## Controle

- Versão: 0.1
- Data: 2026-06-29
- Autor: JP-BR Insurance Knowledge Base
- Histórico: Revisão editorial do fluxo de produção, subagentes e camada ACC.

## Objetivo da revisão

Verificar se a produção recente e a estrutura de trabalho da equipe estão alinhadas ao objetivo maior do projeto: permitir que um corretor japonês consulte o conteúdo, principalmente pelo NotebookLM, e consiga interagir com um cliente brasileiro residente no Japão para esclarecer dúvidas, explicar cláusulas, conduzir atendimento e evitar promessas indevidas.

## Diagnóstico geral

A direção editorial está correta: os documentos recentes já separam explicação técnica em japonês, fala ao cliente em português brasileiro, leitura em katakana e limite comercial.

O ponto fraco identificado foi de orquestração: a categoria ACC já tinha verbetes, FAQs, diálogos e casos, mas ainda não possuía uma camada NotebookLM própria nem um briefing único para manter subagentes e LLMs externas sincronizados com o propósito maior.

## Correções aplicadas

- Criação de `01_Editorial/AGENT_ALIGNMENT_BRIEF.md` como briefing permanente para agente principal, subagentes e LLMs externas.
- Criação de `16_NotebookLM/ACC_INDEX_0001.md` para navegação da categoria ACC no NotebookLM.
- Criação de `16_NotebookLM/ACC_NOTEBOOKLM_PACK_0001.md` para consulta operacional do corretor japonês.
- Criação de `10_Accident/ACC_NAVIGATION_GUIDE.md` como guia de navegação por produto.
- Atualização do fluxo de subagentes para exigir leitura do briefing de alinhamento.
- Inclusão de `.gitignore` para impedir ruído local de `.DS_Store`.
- Ajuste do CHANGELOG para separar entregas ACC na data correta.

## Critério de sintonia da equipe

Toda pessoa, subagente ou LLM externa que participar do projeto deve trabalhar sob a mesma pergunta editorial:

```text
Este conteúdo ajuda o corretor japonês a entender, consultar e explicar ao cliente brasileiro com segurança?
```

Se a resposta for parcial, o conteúdo deve ser normalizado antes de entrar na base oficial.

## Pareceres da equipe

### Especialista japonês técnico e NotebookLM

Decisão editorial: aplicar agora.

Achados incorporados:

- a falta de `ACC_INDEX_0001` e `ACC_NOTEBOOKLM_PACK_0001` era bloqueio P0 para uso efetivo no NotebookLM
- o pacote ACC precisa conter perguntas naturais em japonês e termos obrigatórios como `傷害保険`, `労災保険`, `通勤災害`, `事故通知`, `請求書類`, `診断書`, `診療明細書`, `領収書`, `事故証明書`, `入院保険金`, `通院保険金`, `手術保険金`, `死亡保険金`, `後遺障害保険金`, `免責日数`, `免責事由`, `急激`, `偶然`, `外来`, `支払査定`, `保険証券` e `約款`
- os verbetes ACC ainda devem ser aprofundados porque parte deles está excessivamente padronizada

### Especialista em português brasileiro de atendimento

Decisão editorial: aplicar parcialmente agora e registrar backlog.

Achados incorporados:

- as frases em português do dicionário mestre ACC precisam ficar menos genéricas
- FAQs e casos devem incluir mais frases de próximo passo em português para o cliente
- diálogos ACC devem crescer para 6 a 8 turnos em lotes futuros
- objeções reais devem entrar no próximo lote ACC

### Especialista de seguros no Japão e risco comercial

Decisão editorial: parecer indisponível por limite de uso da ferramenta. A revisão de risco foi suprida pelo agente principal com base em `EDITORIAL_RULES.md` e nos limites de compliance já existentes.

## Lacunas ainda relevantes

- A categoria ACC ainda precisa de expansão gradual de verbetes, FAQs, diálogos e casos para cobrir mais situações de sinistro e pós-venda.
- Os 10 verbetes ACC devem ser reescritos com definições técnicas mais específicas por termo, reduzindo fórmulas genéricas.
- As próximas FAQs ACC devem incluir objeções reais do cliente brasileiro e próximo passo em português.
- As próximas expansões ACC devem cobrir `通院保険金`, `死亡保険金`, `後遺障害保険金`, `保険金請求書`, `事故証明書`, `領収書`, esporte, lazer, acidente doméstico, acidente de trânsito fora do seguro auto, criança, autônomo e trabalhador terceirizado.
- As próximas categorias BUS, SALES e SERVICE devem nascer já com pacote NotebookLM desde o primeiro lote.
- O validador pode evoluir para verificar automaticamente o padrão `ポルトガル語で伝える内容` + `カタカナ読み` em documentos novos.
- As saídas de LLMs externas devem continuar sendo tratadas como rascunho, não como fonte final.

## Decisão editorial

A produção continuará incremental, mas todo novo lote deverá nascer com a camada de consulta correspondente ou com justificativa clara para adiamento.

O foco principal passa a ser:

- utilidade em atendimento real
- recuperação no NotebookLM
- português brasileiro falável
- japonês técnico claro
- compliance operacional
- referências cruzadas

## Referências

- `README.md`
- `EDITORIAL_RULES.md`
- `01_Editorial/AGENT_ALIGNMENT_BRIEF.md`
- `01_Editorial/SUBAGENT_EDITORIAL_WORKFLOW.md`
- `16_NotebookLM/ACC_INDEX_0001.md`
- `16_NotebookLM/ACC_NOTEBOOKLM_PACK_0001.md`

## Veja também

- `10_Accident/ACC_NAVIGATION_GUIDE.md`
- `19_Markdown/ACC/ACC_TERMS_0001_0010.md`
- `19_Markdown/ACC/ACC_FAQ_0001_0005.md`
- `19_Markdown/ACC/ACC_FAQ_0006_0010.md`
- `19_Markdown/ACC/ACC_DIALOGUES_0001_0002.md`
- `19_Markdown/ACC/ACC_CASES_0001_0002.md`
