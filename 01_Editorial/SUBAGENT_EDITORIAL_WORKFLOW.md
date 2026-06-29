# SUBAGENT_EDITORIAL_WORKFLOW - Fluxo editorial com subagentes

## Controle

- Versao: 0.2
- Data: 2026-06-26
- Autor: JP-BR Insurance Knowledge Base
- Historico: Criacao inicial; reforco do modelo operacional.

## Finalidade

Este documento define como usar subagentes no projeto JP-BR Insurance Knowledge Base sem comprometer consistencia, qualidade editorial, referencias cruzadas ou padrao NotebookLM.

Subagentes devem aumentar qualidade por revisao especializada. Eles nao devem funcionar como fabrica paralela de conteudo sem consolidacao editorial.

## Principio central

O agente principal atua como editor-chefe.

Subagentes entregam pareceres, revisoes ou propostas delimitadas. A consolidacao final, alteracao de arquivos, geracao de DOCX/PDF, validacao e sincronizacao com GitHub permanecem sob responsabilidade do editor-chefe.

## Equipe recomendada

Cada ciclo pode usar todos os papeis abaixo ou apenas os papeis necessarios para o risco do lote. O criterio nao e quantidade de agentes, mas cobertura das lentes editoriais que o conteudo exige.

### 1. Arquiteto editorial

Responsavel por:

- estrutura oficial do projeto
- README
- EDITORIAL_RULES
- padroes de documento
- consistencia entre categorias

### 2. Especialista japones tecnico e NotebookLM

Responsavel por:

- japones corporativo
- perguntas naturais em japones
- recuperacao no NotebookLM
- adequacao do conteudo ao corretor japones

### 3. Especialista em portugues brasileiro de atendimento

Responsavel por:

- clareza para cliente brasileiro
- frases prontas
- dialogos naturais
- objecoes comerciais

### 4. Especialista de seguros no Japao e risco comercial

Responsavel por:

- promessa indevida
- aceitacao
- sinistro
- pagamento
- exclusoes
- declaracao de saude
- documentos e impostos

### 5. Auditor de estrutura e validacao

Responsavel por:

- referencias cruzadas
- codigos duplicados
- romaji
- secoes obrigatorias
- formatos Markdown/DOCX/PDF
- renderizacao quando aplicavel

## Regras de delegacao

- Cada subagente deve ter tarefa concreta e escopo limitado.
- Subagentes nao devem editar arquivos diretamente no fluxo normal de revisao.
- Se houver edicao por subagente, o escopo de arquivos deve ser exclusivo e previamente definido.
- Nenhum parecer de subagente entra automaticamente no projeto.
- Toda recomendacao deve ser consolidada pelo editor-chefe.
- Toda entrega deve atualizar `CHANGELOG.md`.
- Toda entrega deve passar por `00_Project/validate_project.py`.

## Modelo operacional dos agentes

### Entrada minima para cada subagente

Cada subagente deve receber:

- briefing de alinhamento `01_Editorial/AGENT_ALIGNMENT_BRIEF.md`
- objetivo do ciclo
- arquivos ou pastas em escopo
- papel editorial esperado
- tipo de saida esperada
- proibicoes relevantes, como nao alterar traducao existente, nao usar romaji e nao prometer cobertura, aceitacao ou pagamento

### Saida esperada por papel

O arquiteto editorial deve entregar:

- problemas de estrutura
- conflitos com README ou EDITORIAL_RULES
- impacto em templates, indices, pacotes NotebookLM e CHANGELOG

O especialista japones tecnico e NotebookLM deve entregar:

- consultas naturais em japones
- termos japoneses que precisam aparecer para recuperacao
- risco de ambiguidade para corretor nativo japones
- sugestoes de agrupamento para NotebookLM

O especialista em portugues brasileiro de atendimento deve entregar:

- frases que soam pouco naturais
- respostas mais claras para cliente brasileiro
- objecoes provaveis
- proximo passo concreto de atendimento

O especialista de seguros no Japao e risco comercial deve entregar:

- risco de promessa indevida
- trechos que precisam de limite comercial/compliance
- separacao entre explicacao do corretor e decisao da seguradora
- temas que exigem confirmacao em documentos oficiais

O auditor de estrutura e validacao deve entregar:

- referencias quebradas ou fracas
- padroes ausentes
- lacunas de DOCX/PDF
- warnings que devem virar backlog editorial

### Consolidacao pelo editor-chefe

O editor-chefe deve transformar os pareceres em uma decisao unica:

- aplicar agora
- registrar como backlog
- rejeitar por conflito com a especificacao
- pedir decisao do usuario quando houver mudanca de escopo, risco juridico ou alteracao estrutural relevante

Quando dois subagentes divergirem, prevalece a decisao que melhor protege o objetivo do projeto: o corretor japones deve consultar o NotebookLM, entender rapidamente o tema e explicar ao cliente brasileiro sem promessa indevida.

## Quando usar subagentes

Usar subagentes em ciclos que envolvam:

- pacotes NotebookLM
- normalizacao de FAQs em lote
- conteudo sensivel, como sinistro, pagamento, aceitacao, imposto ou declaracao de saude
- mudanca em regras editoriais
- abertura de nova categoria de produto
- auditoria de qualidade antes de grande expansao
- revisao periodica de sintonia entre producao, NotebookLM, portugues de atendimento e compliance

Nao e necessario usar subagentes para:

- correcao ortografica pequena
- ajuste pontual de referencia cruzada
- geracao mecanica de DOCX/PDF ja validada
- atualizacao simples de CHANGELOG

## Backlog gerado por warnings

Warnings do validador devem ser tratados como fila editorial, nao como falha operacional.

Prioridade recomendada:

1. FAQs e casos sensiveis sem `## Limite comercial/compliance`.
2. FAQs sem `## Consulta natural em japonês`.
3. Dialogos sem objecao real ou sem proximo passo concreto.
4. Indices NotebookLM pouco conversacionais.
5. Termos recorrentes sem alinhamento explicito com o glossario mestre.

Cada ciclo de normalizacao deve reduzir a fila de warnings ou justificar no relatorio por que a fila permaneceu igual.

## Fluxo recomendado

1. Definir objetivo do ciclo.
2. Reconfirmar o briefing `01_Editorial/AGENT_ALIGNMENT_BRIEF.md`.
3. Dividir analise em lentes especializadas.
4. Rodar subagentes em paralelo.
5. Consolidar convergencias e conflitos.
6. Aplicar somente mudancas de alto valor.
7. Gerar Markdown, DOCX e PDF quando aplicavel.
8. Rodar validador.
9. Renderizar DOCX/PDF quando houver alteracao de formato.
10. Atualizar CHANGELOG.
11. Fazer commit e sincronizar com GitHub.

## Revisao periodica autonoma

O projeto deve executar revisoes periodicas de sintonia editorial para evitar que a producao se transforme apenas em volume.

Frequencia recomendada:

- a cada semana de trabalho editorial intenso
- antes de abrir nova categoria
- depois de cada lote relevante com NotebookLM, FAQs, dialogos ou casos
- sempre que uma ferramenta externa ou subagente produzir material bruto em quantidade

A revisao periodica deve verificar:

- se a categoria possui camada NotebookLM
- se o corretor japones encontra o conteudo por perguntas naturais em japones
- se ha portugues brasileiro falavel para o cliente
- se ha proximo passo operacional para o atendimento
- se ha limite comercial/compliance em temas sensiveis
- se referencias cruzadas apontam para documentos realmente relacionados
- se Markdown, DOCX e PDF estao sincronizados

Resultado esperado:

- relatorio curto em `00_Project`
- correcoes aplicadas quando forem seguras
- backlog quando a correcao exigir expansao maior
- validacao objetiva antes do commit

## Criterios para aceitar recomendacao de subagente

Uma recomendacao deve ser aceita quando:

- melhora o uso pelo corretor japones
- melhora clareza para o cliente brasileiro
- reduz risco comercial ou juridico
- melhora recuperacao no NotebookLM
- aumenta consistencia terminologica
- pode ser validada objetivamente

Uma recomendacao deve ser rejeitada ou adiada quando:

- contradiz README ou EDITORIAL_RULES
- altera traducao existente sem justificativa
- duplica conteudo tecnico
- aumenta complexidade sem ganho claro
- exige decisao de negocio ainda nao autorizada

## Piloto inicial

O primeiro piloto deve usar subagentes para revisar:

- pacotes NotebookLM AUTO, VIDA e MED
- guias de navegacao AUTO, VIDA e MED
- glossario mestre
- validador do projeto

O objetivo do piloto nao e produzir volume novo. O objetivo e medir se a revisao especializada melhora a qualidade da base.

## Resultado do primeiro piloto

O primeiro piloto confirmou que a estrategia e util quando usada como revisao especializada.

Pontos convergentes dos subagentes:

- a camada NotebookLM esta bem estruturada, mas FAQs individuais precisam receber consultas naturais em japones gradualmente
- a linguagem em portugues e adequada, mas alguns dialogos e casos ainda precisam de objecoes mais naturais e proximo passo concreto
- temas sensiveis precisam de aviso de limite comercial/compliance mais padronizado
- o validador deve evoluir para checar FAQ, secoes vazias, links internos e alertas editoriais
- subagentes devem continuar como revisores e nao como produtores paralelos sem consolidacao

Decisao editorial:

- manter o modelo de subagentes como equipe de revisao
- aplicar recomendacoes por ciclos pequenos, com validacao e changelog
- nao permitir que subagentes facam commit direto no fluxo normal

## Historico de revisao

| Data | Versao | Autor | Alteracao |
| --- | --- | --- | --- |
| 2026-06-26 | 0.2 | JP-BR Insurance Knowledge Base | Reforco do modelo operacional, saidas por papel e tratamento de warnings como backlog editorial. |
| 2026-06-26 | 0.1 | JP-BR Insurance Knowledge Base | Criacao do fluxo editorial com subagentes. |
