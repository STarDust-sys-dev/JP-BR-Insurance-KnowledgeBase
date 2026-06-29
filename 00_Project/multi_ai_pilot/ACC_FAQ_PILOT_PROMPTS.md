# Piloto Multi-IA - ACC FAQs

## Controle

- Data: 2026-06-29
- Categoria: ACC
- Entrega piloto: 10 FAQs
- Status: rascunho controlado

## Objetivo

Testar o uso coordenado de ChatGPT, Claude, Gemini, Perplexity e Copilot para gerar rascunhos de FAQs sobre seguro de acidentes, mantendo revisão editorial central antes de qualquer publicação oficial.

## Prompt Claude - rascunho inicial

Voce e redator editorial do projeto JP-BR Insurance Knowledge Base.

Crie 10 FAQs bilíngues para a categoria ACC, seguro de acidentes, destinadas a corretores japoneses que atendem clientes brasileiros residentes no Japao.

Regras obrigatorias:
- Títulos principais e seções estruturais em japones.
- Conteudo tecnico principal em japones.
- Portugues brasileiro simples e natural para fala ao cliente.
- Nunca usar romaji.
- Incluir para cada FAQ:
  - codigo sugerido rascunho ACC 0001 a rascunho ACC 0010
  - pergunta pratica do cliente brasileiro
  - resposta tecnica em japones
  - resposta ao cliente com blocos PT-Br, JP（ふりがな） e Leitura de apoio para o corretor
  - proximo passo seguro
  - limite comercial/compliance
  - termos relacionados sugeridos
  - referencias cruzadas sugeridas
  - tags
- Nao prometer cobertura, indenizacao, aceitacao, aprovacao ou resultado.
- Condicionar sempre a contrato, documentos, acidente, datas relevantes e avaliacao da seguradora.
- Foque em situacoes reais de brasileiros no Japao: acidente no trabalho, acidente fora do trabalho, fratura, hospitalizacao, cirurgia, incapacidade temporaria, documentos medicos, prazo de solicitacao, diferenca entre seguro de acidente e seguro medico, exclusoes.

Produza em Markdown estruturado, pronto para revisao editorial.

## Prompt Gemini - revisao de lacunas

Voce e revisor de cobertura tematica do projeto JP-BR Insurance Knowledge Base.

Analise o rascunho abaixo de 10 FAQs ACC e identifique:
1. lacunas tecnicas;
2. pontos confusos para brasileiros no Japao;
3. riscos de compliance;
4. trechos que podem soar como promessa de cobertura ou pagamento;
5. termos japoneses que precisam de explicacao melhor em portugues brasileiro;
6. referencias cruzadas recomendadas;
7. FAQs que devem ser aprovadas, corrigidas ou rejeitadas.

Regras do projeto:
- Titulos principais em japones.
- Sem romaji.
- Conteudo tecnico em japones.
- Portugues brasileiro simples.
- Foco em corretor japones atendendo brasileiro no Japao.
- Blocos obrigatorios na resposta ao cliente: PT-Br, JP（ふりがな）, Leitura de apoio para o corretor.

Responda em checklist editorial.

## Prompt Perplexity - ressalvas e fontes

Voce e assistente de pesquisa para o projeto JP-BR Insurance Knowledge Base.

Analise as 10 FAQs ACC abaixo e aponte:
1. quais afirmacoes exigem fonte ou confirmacao;
2. quais pontos dependem de contrato, seguradora, produto ou legislacao;
3. quais temas devem evitar resposta definitiva;
4. fontes publicas japonesas ou tipos de fonte que poderiam ser consultadas para seguro de acidentes no Japao;
5. alertas de compliance.

Nao reescreva tudo. Responda como lista objetiva de riscos, ressalvas e fontes recomendadas.

## Prompt Copilot - frases alternativas PT-BR

Voce e revisor de linguagem em portugues brasileiro para atendimento de seguros.

Com base nas 10 FAQs ACC abaixo, sugira frases alternativas curtas em portugues brasileiro para o corretor japones dizer ao cliente brasileiro.

Regras:
- Portugues brasileiro simples.
- Frases curtas.
- Nao prometer cobertura, pagamento, aprovacao ou resultado.
- Usar linguagem calma e profissional.
- Para cada FAQ, sugerir 2 alternativas de fala ao cliente.
- Nao usar romaji.

## Prompt ChatGPT - revisao final

Voce e editor final de consistencia e compliance do projeto JP-BR Insurance Knowledge Base.

Revise o rascunho das 10 FAQs ACC usando:
- rascunho inicial;
- checklist do Gemini;
- ressalvas/fontes do Perplexity;
- frases alternativas do Copilot.

Tarefas:
1. Reescreva as 10 FAQs no padrao final do projeto.
2. Mantenha titulos principais em japones.
3. Mantenha conteudo tecnico em japones.
4. Em cada resposta ao cliente, inclua PT-Br, JP（ふりがな） e Leitura de apoio para o corretor.
5. Remova romaji.
6. Remova promessas de cobertura, pagamento, aceitacao ou resultado.
7. Inclua limite comercial/compliance.
8. Sugira termos relacionados e referencias cruzadas.
9. Liste pendencias que exigem validacao humana.
10. Decida: aprovado, aprovado com ressalvas ou rejeitado.

