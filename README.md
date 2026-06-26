# Arquitetura do Projeto

## Nome do Projeto

JP-BR Insurance Knowledge Base (JB-IKB)

## Nome em japonês

日伯保険営業実務マニュアル

## Subtítulo

Base de conhecimento profissional para corretores japoneses que atendem clientes brasileiros residentes no Japão.

## Missão

Desenvolver a maior biblioteca técnica bilíngue (Japonês ↔ Português) sobre seguros no Japão.

A obra deverá servir simultaneamente para:

- treinamento de corretores japoneses
- consulta rápida durante o atendimento
- documentação técnica
- base para IA (NotebookLM)
- chatbot especializado
- futuras traduções

## Objetivos

Produzir aproximadamente:

- 5.000 verbetes técnicos
- 5.000 frases
- 500 diálogos
- 1.000 FAQs
- centenas de estudos de caso
- dezenas de fluxogramas
- milhares de referências cruzadas

## Público

### Principal

Corretor japonês

↓

Cliente brasileiro residente no Japão

## Idioma

### Idioma principal

Japonês

### Idioma secundario

Português brasileiro

Nunca usar romaji.

## Estrutura

```text
JP-BR-Insurance-KnowledgeBase

00_Project
01_Editorial
02_MasterDictionary
03_Glossary
04_Automobile
05_Life
06_Medical
07_Fire
08_Housing
09_Business
10_Accident
11_Sales
12_Service
13_Dialogues
14_FAQ
15_CaseStudies
16_NotebookLM
17_PDF
18_DOCX
19_Markdown
20_Assets

README.md
CHANGELOG.md
```

## Padrão dos verbetes

Cada verbete deverá conter:

- Código
- Categoria
- Termo Japonês
- Tradução Português
- Definição Técnica
- Explicação Simplificada
- Como explicar ao cliente brasileiro
- Frases utilizadas
- Perguntas frequentes
- Termos relacionados
- Referências cruzadas
- Tags
- Histórico de revisão

## Códigos

- AUTO
- VIDA
- MED
- FIRE
- HOME
- BUS
- ACC
- SALES
- SERVICE
- FAQ
- CASE
- LEG
- TERM

## Estrutura NotebookLM

Todos os documentos deverao possuir:

- Titulo
- Resumo
- Palavras-chave
- Categorias
- Conteúdo
- Referências
- Veja também

Assim o NotebookLM recuperará melhor as informações.

## Regras

- Nunca alterar traducoes existentes.
- Nunca duplicar verbetes.
- Sempre criar referencias cruzadas.
- Sempre utilizar linguagem natural.
- Sempre pensar no atendimento.

## Estilo

- Japonês corporativo.
- Português simples.
- Sem traduções literais quando prejudicarem a compreensão.

## Formatos

Sempre gerar:

```text
Markdown
↓
DOCX
↓
PDF
```

## Controle

Cada documento terá:

- Versão
- Data
- Histórico
- Autor

## Glossário

Meta: 5.000 verbetes.

## Diálogos

Meta: 500 diálogos.

## FAQ

Meta: 1.000.

## Casos

Meta: centenas de estudos de caso.

## Objetivo Final

Criar a melhor base de conhecimento existente para corretores japoneses venderem seguros para brasileiros.

## Aviso de uso

Este projeto e material educativo, editorial e de apoio ao atendimento.

O conteudo nao substitui:

- apolice
- proposta
- explicacao de informacoes importantes
- documentos oficiais da seguradora
- analise formal da seguradora
- orientacao fiscal, juridica ou regulatoria especifica

Cobertura, aceitacao, exclusao, valor, prazo, imposto e pagamento dependem das condicoes do contrato, documentos apresentados, situacao concreta do cliente e decisao formal da seguradora ou autoridade competente.

O corretor deve usar este material para explicar, orientar, organizar informacoes e reduzir mal-entendidos, mas nao deve prometer aceitacao, cobertura, culpa, valor, prazo, imposto, pagamento ou reversao de decisao.
