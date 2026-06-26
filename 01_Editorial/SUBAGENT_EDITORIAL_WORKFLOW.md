# SUBAGENT_EDITORIAL_WORKFLOW - Fluxo editorial com subagentes

## Controle

- Versao: 0.1
- Data: 2026-06-26
- Autor: JP-BR Insurance Knowledge Base
- Historico: Criacao inicial.

## Finalidade

Este documento define como usar subagentes no projeto JP-BR Insurance Knowledge Base sem comprometer consistencia, qualidade editorial, referencias cruzadas ou padrao NotebookLM.

Subagentes devem aumentar qualidade por revisao especializada. Eles nao devem funcionar como fabrica paralela de conteudo sem consolidacao editorial.

## Principio central

O agente principal atua como editor-chefe.

Subagentes entregam pareceres, revisoes ou propostas delimitadas. A consolidacao final, alteracao de arquivos, geracao de DOCX/PDF, validacao e sincronizacao com GitHub permanecem sob responsabilidade do editor-chefe.

## Equipe recomendada

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

## Fluxo recomendado

1. Definir objetivo do ciclo.
2. Dividir analise em lentes especializadas.
3. Rodar subagentes em paralelo.
4. Consolidar convergencias e conflitos.
5. Aplicar somente mudancas de alto valor.
6. Gerar Markdown, DOCX e PDF quando aplicavel.
7. Rodar validador.
8. Renderizar DOCX/PDF quando houver alteracao de formato.
9. Atualizar CHANGELOG.
10. Fazer commit e sincronizar com GitHub.

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
| 2026-06-26 | 0.1 | JP-BR Insurance Knowledge Base | Criacao do fluxo editorial com subagentes. |
