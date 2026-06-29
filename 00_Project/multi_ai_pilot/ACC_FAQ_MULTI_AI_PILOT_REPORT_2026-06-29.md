# ACC FAQ Multi-AI Pilot Report

## 管理情報

- Data: 2026-06-29
- Categoria: ACC
- Entrega testada: 10 FAQs
- Ferramentas testadas: Claude, Gemini, Perplexity, Copilot, ChatGPT
- Status: piloto concluído; conteúdo não aprovado para publicação direta

## Objetivo

Testar se contas gratuitas de LLMs abertas no Chrome podem acelerar a produção editorial do projeto JP-BR Insurance Knowledge Base sem comprometer o padrão oficial.

## Fluxo executado

1. Claude gerou um rascunho inicial de 10 FAQs ACC.
2. Gemini revisou lacunas, compliance, romaji e riscos.
3. Perplexity levantou ressalvas e fontes recomendadas.
4. Copilot foi acionado para frases alternativas em PT-BR, mas não respondeu no tempo útil.
5. ChatGPT produziu parecer editorial final sobre o piloto.

## Resultado por ferramenta

### Claude

Resultado: útil como gerador de rascunho.

Pontos positivos:

- Gerou rapidamente um conjunto amplo de FAQs.
- Cobriu temas relevantes: acidente no trabalho, fratura, hospitalização, cirurgia, documentos, incapacidade temporária, prazo, cobertura fora do Japão e exclusões.
- Criou material aproveitável como base de edição.

Problemas:

- Usou romaji/romanização proibida, como `romanização de 労災保険`, `romanização de 国民健康保険`, `romanização de 診断書`, `romanização de 入院証明書` e `romanização de 海外旅行保険`.
- Gerou conteúdo longo demais para um piloto.
- Incluiu frases com risco de promessa implícita.
- A rascunho ACC 0010 saiu incompleta.

Decisão: manter como redator de rascunho, mas com prompt mais restritivo.

### Gemini

Resultado: muito útil como revisor.

Pontos positivos:

- Detectou romaji.
- Apontou riscos de promessa.
- Recomendou separar `労災保険` de `傷害保険` privado.
- Alertou sobre `約款`, `免責日数`, documentos médicos, prazos e compliance.
- Classificou rascunho ACC 0001 a rascunho ACC 0009 como corrigir e rascunho ACC 0010 como rejeitar.

Decisão: manter como auditor técnico/editorial.

### Perplexity

Resultado: útil para ressalvas e fontes.

Pontos positivos:

- Reforçou uso de fontes públicas japonesas para temas sensíveis.
- Indicou `厚生労働省` e páginas de `労働局` para `労災保険` e `通勤災害`.
- Indicou `金融庁`, associações setoriais, condições gerais da seguradora e formulários de sinistro para seguro privado.
- Reforçou que cobertura, documentos, território, exclusões e prazos dependem de apólice e produto.

Decisão: manter como verificador de fontes e ressalvas.

### Copilot

Resultado: falha operacional no piloto.

Problema:

- A mensagem foi enviada, mas não houve resposta no tempo útil.

Decisão: remover do fluxo principal por enquanto. Pode ser retestado depois apenas para variações curtas de linguagem.

### ChatGPT

Resultado: útil como parecer editorial final.

Pontos positivos:

- Confirmou que o fluxo multi-IA aumenta produtividade.
- Recomendou manter Claude, Gemini e Perplexity.
- Recomendou remover Copilot do fluxo principal.
- Recomendou lotes menores de 5 FAQs.
- Recomendou corrigir rascunho ACC 0001 a rascunho ACC 0009 e descartar rascunho ACC 0010.

Decisão: manter como revisor final de processo, quando útil.

## Decisão editorial sobre as 10 FAQs geradas

Não publicar diretamente.

Decisão por bloco:

- rascunho ACC 0001 a rascunho ACC 0009: corrigir antes de qualquer integração.
- rascunho ACC 0010: descartar e reescrever do zero.

Motivos:

- presença de romaji;
- mistura de `労災保険`, `健康保険` e `傷害保険` sem separação suficiente;
- risco de promessa de cobertura;
- necessidade de fontes para prazos, documentos e temas trabalhistas;
- excesso de extensão;
- FAQ final incompleta.

## Processo recomendado para a próxima rodada

### Etapa 1: Claude

Gerar apenas 5 FAQs por vez.

Regras novas:

- Proibir romaji com exemplos explícitos de termos proibidos.
- Limitar cada FAQ a estrutura curta.
- Exigir frase de compliance em cada FAQ.
- Exigir que `労災保険`, `健康保険` e `傷害保険` sejam separados.

### Etapa 2: Gemini

Auditar cada FAQ com decisão:

- aprovar;
- corrigir;
- rejeitar.

Checklist obrigatório:

- romaji;
- promessa implícita;
- confusão entre produtos;
- termo técnico mal explicado;
- lacuna documental;
- lacuna de compliance;
- referência cruzada insuficiente.

### Etapa 3: Perplexity

Verificar apenas:

- fontes públicas;
- legislação ou órgão responsável;
- dependência de contrato;
- pontos que não podem ser afirmados universalmente.

### Etapa 4: Editor central

Consolidar internamente no padrão oficial do projeto:

- títulos principais em japonês;
- conteúdo técnico em japonês;
- PT-Br simples;
- JP（ふりがな）;
- leitura de apoio sem romaji;
- referências cruzadas;
- compliance;
- validação automática;
- Markdown, DOCX e PDF.

## Ajustes de prompt obrigatórios

Adicionar nos próximos prompts:

```text
PROIBIDO utilizar romaji sob qualquer circunstância.

Use apenas:
- kanji;
- hiragana;
- katakana;
- português brasileiro.

Exemplos proibidos:
- romanização de 労災保険
- romanização de 国民健康保険
- romanização de 診断書
- romanização de 入院
- romanização de 証明書
- romanização de 海外旅行保険
```

Adicionar limite:

```text
Produza apenas 5 FAQs.
Cada FAQ deve ter no máximo:
- pergunta: 1 linha;
- resposta técnica: 120 palavras;
- fala ao cliente: 2 frases;
- compliance: 2 linhas.
```

Adicionar linguagem de segurança:

```text
Nunca usar:
- sempre;
- garantido;
- com certeza;
- será pago;
- tem direito.

Preferir:
- pode depender do contrato;
- é necessário confirmar;
- a seguradora avaliará;
- consulte as condições contratuais;
- depende da apólice.
```

## Conclusão

A estratégia multi-IA é recomendada para aumentar produtividade, desde que as LLMs sejam tratadas como geradoras e revisoras de rascunho, nunca como fonte final.

Fluxo aprovado para próxima rodada:

Claude -> Gemini -> Perplexity -> Editor central.

Copilot fica fora do fluxo principal até novo teste.

Estimativa qualitativa: o fluxo pode acelerar produção de rascunhos em 2 a 4 vezes, mas exige revisão central para evitar romaji, promessa indevida, confusão técnica e inconsistência com o padrão do projeto.

## Arquivos brutos do piloto

- `CLAUDE_ACC_FAQ_RAW.txt`
- `GEMINI_ACC_FAQ_REVIEW.txt`
- `PERPLEXITY_ACC_FAQ_SOURCES.txt`
- `COPILOT_ACC_FAQ_PTBR_ALTERNATIVES.txt`
- `CHATGPT_ACC_FAQ_FINAL_REVIEW.txt`
- `ACC_FAQ_PILOT_PROMPTS.md`

