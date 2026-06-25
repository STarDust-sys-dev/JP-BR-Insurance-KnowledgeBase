# Constituição Editorial do Projeto

## Finalidade

Este documento consolida as regras permanentes do projeto JP-BR Insurance Knowledge Base (JB-IKB).

Ele funciona como a constituição editorial do projeto e deve orientar todas as decisões de produção, tradução, numeração, redação, revisão, referências cruzadas e publicação.

## Especificação oficial

O `README.md` é a especificação oficial do projeto. Nenhum documento deve contrariar sua estrutura, missão, padrões de verbetes, regras de idioma ou fluxo de formatos.

O `EDITORIAL_RULES.md` define como a especificação será aplicada no trabalho editorial diário.

## Regras principais

- Nunca alterar traduções existentes sem justificativa documentada.
- Nunca duplicar verbetes.
- Sempre criar referências cruzadas entre documentos relacionados.
- Sempre utilizar linguagem natural.
- Sempre escrever pensando no atendimento entre corretor japonês e cliente brasileiro residente no Japão.
- Nunca usar romaji.

## Escopo permanente

Este arquivo deverá concentrar regras permanentes sobre:

- como traduzir cada termo
- como numerar verbetes
- como escrever títulos
- como fazer referências
- como escrever FAQs
- como escrever diálogos
- como escrever estudos de caso
- como criar e manter referências cruzadas
- como controlar versões, datas, autores e histórico editorial
- como manter consistência terminológica entre todos os documentos

## Estilo linguístico

- Japonês: corporativo, claro e adequado ao contexto profissional de seguros.
- Português brasileiro: simples, natural e orientado à compreensão do cliente.
- Evitar traduções literais quando elas prejudicarem a compreensão.

## Regras de tradução

Cada termo técnico deverá ter uma tradução principal e, quando necessário, notas de uso.

A tradução deverá priorizar:

- precisão técnica
- compreensão pelo cliente brasileiro
- naturalidade no atendimento
- consistência com traduções já aprovadas
- adequação ao mercado de seguros no Japão

Quando uma tradução literal causar confusão, deverá ser usada uma explicação funcional em português brasileiro.

## Numeração de verbetes

Cada verbete deverá receber um código único, formado por:

```text
CATEGORIA-NÚMERO
```

Exemplos:

```text
AUTO-0001
VIDA-0001
MED-0001
FAQ-0001
CASE-0001
```

O número deverá ter quatro dígitos e nunca deverá ser reutilizado.

## Títulos

Os títulos devem ser claros, objetivos e consistentes.

Padrão recomendado:

```text
Código - Termo Japonês - Tradução em Português
```

Exemplo:

```text
AUTO-0001 - 自動車保険 - Seguro de automóvel
```

Títulos de FAQ devem ser escritos como perguntas reais de atendimento.

Títulos de diálogos devem indicar o contexto prático da conversa.

Títulos de estudos de caso devem indicar situação, produto e problema central.

## Consistência terminológica

Todo novo conteúdo deve respeitar os termos já definidos no glossário, no dicionário mestre e nos documentos anteriores. Quando um novo termo técnico for criado, ele deverá ser registrado com código, categoria, definição, explicação simplificada e referências cruzadas.

## Referências

Referências devem indicar a origem técnica da informação sempre que houver fonte, norma, documento interno, termo relacionado ou conteúdo já existente.

Quando não houver fonte externa, a referência deve apontar para os documentos internos relacionados.

## FAQs

Cada FAQ deverá conter:

- Código
- Pergunta
- Resposta curta
- Resposta explicada
- Termos relacionados
- Referências cruzadas
- Tags

A pergunta deve refletir uma dúvida real de atendimento.

A resposta deve ser clara, direta e adequada ao cliente brasileiro.

## Diálogos

Cada diálogo deverá conter:

- Código
- Situação de atendimento
- Participantes
- Versão em japonês
- Versão em português brasileiro
- Notas culturais ou comerciais, quando necessário
- Termos relacionados
- Referências cruzadas

Os diálogos devem representar conversas naturais entre corretor japonês e cliente brasileiro residente no Japão.

## Estudos de caso

Cada estudo de caso deverá conter:

- Código
- Produto ou categoria
- Situação
- Problema
- Análise
- Orientação ao corretor
- Como explicar ao cliente brasileiro
- Termos relacionados
- FAQs relacionadas
- Referências cruzadas
- Histórico de revisão

O estudo de caso deve ajudar o corretor a tomar decisão prática durante o atendimento.

## Formatos de entrega

Cada entrega editorial deverá ser preparada, quando aplicável, nos seguintes formatos:

```text
Markdown
↓
DOCX
↓
PDF
```

## Controle editorial

Cada documento deverá conter:

- Versão
- Data
- Histórico
- Autor
- Referências
- Veja também

## Referências cruzadas

Todo documento deve indicar documentos relacionados na seção `Veja também`. Verbete, FAQ, diálogo e estudo de caso devem se conectar sempre que tratarem do mesmo termo, produto, situação de atendimento ou regra prática.

## Alterações desta constituição

Este arquivo só deve ser alterado quando houver necessidade real de consolidar uma regra permanente do projeto.

Toda alteração deverá ser registrada no `CHANGELOG.md` com data e justificativa breve.
