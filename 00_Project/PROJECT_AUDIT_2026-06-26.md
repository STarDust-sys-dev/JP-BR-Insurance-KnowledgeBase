# PROJECT_AUDIT_2026-06-26 - Auditoria estrutural e editorial

## Controle

- Versao: 0.1
- Data: 2026-06-26
- Autor: JP-BR Insurance Knowledge Base
- Historico: Criacao inicial.

## Objetivo

Registrar os principais achados da auditoria estrutural e editorial do projeto, considerando o objetivo final:

> O corretor de seguros nativo japones deve consultar o conteudo pelo NotebookLM e conseguir interagir com um brasileiro, esclarecendo duvidas, explicando clausulas e fechando contratos.

## Estado observado

- Documentos editoriais principais em Markdown: 701
- Verbetes tecnicos: 260
- FAQs: 257
- Dialogos: 72
- Estudos de caso: 108
- Indices NotebookLM: 5
- DOCX finais: 71
- PDFs finais: 71

## Achados principais

### 1. Conteudo ainda pouco orientado a busca em japones

O corpus possui termos japoneses, mas a superficie de consulta ainda e majoritariamente em portugues. Para NotebookLM, o corretor japones precisa encontrar respostas com perguntas naturais em japones.

Risco:

- recuperacao fraca quando o corretor perguntar em japones
- respostas menos uteis em atendimento real
- dependencia excessiva de conhecimento externo da IA

Acao recomendada:

- criar pacotes NotebookLM por categoria com perguntas naturais em japones
- adicionar frases de busca em japones nas FAQs e nos casos principais

### 2. Dialogos MED parcialmente fora do padrao

AUTO e VIDA possuem dialogos com versao japonesa, versao portuguesa, participantes e notas culturais. Parte de MED foi gerada em formato mais simples.

Risco:

- material menos util para treinamento do corretor
- dificuldade de uso direto em atendimento

Acao recomendada:

- normalizar `DIALOGUE-MED-0006` a `DIALOGUE-MED-0015`

### 3. FAQ possui dois modelos concorrentes

O modelo antigo usa `Resposta curta` e `Resposta explicada`. O modelo recente usa `Resposta tecnica` e `Como responder ao cliente brasileiro`.

Risco:

- inconsistencia editorial
- menor previsibilidade para NotebookLM

Acao tomada:

- `EDITORIAL_RULES.md` atualizado para reconhecer o modelo recente e exigir respostas adicionais quando houver treinamento rapido, objecao ou clausula sensivel.

### 4. Termos recorrentes sem autoridade central

Termos como `保険料`, `契約者`, `保険証券`, `申込書`, `告知義務` e `支払査定` aparecem em mais de uma categoria.

Risco:

- traducao divergente no futuro
- duplicacao nao controlada
- perda de confianca da base

Acao tomada:

- criado `03_Glossary/MASTER_TERMINOLOGY.md`

### 5. Referencia cruzada quebrada

Foi encontrada uma referencia para um caso MED ainda inexistente em `DIALOGUE-MED-0015`.

Acao tomada:

- corrigido para `CASE-MED-0024`
- consolidados Markdown/DOCX/PDF afetados foram regenerados
- validacao posterior encontrou 0 referencias quebradas nos documentos editoriais

## Decisoes editoriais

- As pastas por produto devem funcionar como guias de navegacao, nao como duplicacao do dicionario mestre.
- O glossario mestre passa a ser referencia para termos recorrentes entre categorias.
- Dialogos sem versao japonesa e portuguesa separadas devem ser considerados incompletos para uso NotebookLM.
- Problemas recorrentes devem ser resolvidos pela causa raiz e validados.

## Proximos passos recomendados

1. Normalizar os dialogos MED incompletos.
2. Criar `MED_NOTEBOOKLM_PACK_0001.md` com consultas naturais em japones.
3. Criar validador automatizado permanente.
4. Criar guias de navegacao em `04_Automobile`, `05_Life` e `06_Medical`.
5. Expandir o glossario mestre sempre que novos termos compartilhados aparecerem.

## Historico de revisao

| Data | Versao | Autor | Alteracao |
| --- | --- | --- | --- |
| 2026-06-26 | 0.1 | JP-BR Insurance Knowledge Base | Registro da primeira auditoria estrutural e editorial completa. |
