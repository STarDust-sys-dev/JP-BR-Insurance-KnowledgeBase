# AGENT_ALIGNMENT_BRIEF - Propósito comum da equipe editorial

## Controle

- Versão: 0.1
- Data: 2026-06-29
- Autor: JP-BR Insurance Knowledge Base
- Histórico: Criação do briefing permanente de alinhamento para agente principal, subagentes e LLMs externas.

## Propósito maior

Toda produção deste projeto deve servir a uma cena concreta: um corretor japonês consulta a base, entende o tema em japonês e consegue explicar em português brasileiro simples para um cliente brasileiro residente no Japão, sem prometer cobertura, aceitação, pagamento, prazo, culpa, imposto ou decisão da seguradora.

O objetivo não é apenas criar volume. O objetivo é criar material consultável, seguro e útil durante atendimento real.

## Usuário principal

O usuário principal é o corretor japonês.

Ele precisa encontrar rapidamente:

- o termo japonês correto
- a explicação técnica em japonês
- a frase em português brasileiro que pode dizer ao cliente
- a leitura em katakana como apoio de pronúncia
- o próximo passo seguro
- o limite comercial ou de compliance
- documentos relacionados para aprofundamento

## Interlocutor final

O interlocutor final é o cliente brasileiro residente no Japão.

Ele precisa receber explicações:

- em português brasileiro simples
- sem tradução literal confusa
- com exemplos práticos
- com próximos passos claros
- sem promessas indevidas

## Regra de ouro

Cada documento deve responder claramente a três perguntas:

1. O que o corretor japonês precisa entender?
2. O que ele pode dizer ao cliente brasileiro?
3. O que ele não pode prometer?

Se uma resposta não ajuda essas três perguntas, ela deve ser revisada, reduzida ou movida para backlog.

## Papel do agente principal

O agente principal atua como editor-chefe.

Responsabilidades:

- proteger README.md e EDITORIAL_RULES.md
- consolidar pareceres de subagentes
- decidir o que entra no projeto
- corrigir inconsistências antes de produzir volume
- gerar Markdown, DOCX e PDF quando aplicável
- validar referências, romaji, seções obrigatórias e renderização
- atualizar CHANGELOG.md a cada entrega
- sincronizar com GitHub após validação

## Papel dos subagentes

Subagentes ajudam com lentes especializadas, mas não definem a direção final.

Papéis recomendados:

- Arquiteto editorial: estrutura, padrões e consistência.
- Especialista japonês técnico e NotebookLM: recuperação em japonês e clareza para corretor nativo japonês.
- Especialista em português brasileiro de atendimento: fala natural ao cliente brasileiro.
- Especialista de seguros no Japão e risco comercial: limites, sinistro, aceitação, exclusões e promessas indevidas.
- Auditor de estrutura e validação: códigos, referências, seções, formatos e renderização.

## Papel de LLMs externas

ChatGPT, Claude, Gemini, Perplexity, Copilot ou outras ferramentas externas podem ser usadas apenas como fontes auxiliares de rascunho, revisão ou comparação.

Nenhuma saída externa entra diretamente no projeto.

Toda saída externa deve passar por:

- remoção de romaji
- revisão terminológica
- revisão de compliance
- adaptação ao padrão de português brasileiro explícito
- inclusão de leitura em katakana quando for fala ao cliente
- referências cruzadas internas
- validação final pelo agente principal

## Padrão obrigatório de fala ao cliente

Sempre que houver fala ao cliente brasileiro, usar:

```text
### ポルトガル語で伝える内容

Frase em português brasileiro simples.

### カタカナ読み

Leitura aproximada em katakana.

日本語確認用: sentido da frase em japonês.
```

O português deve aparecer antes da leitura em katakana.

## Critério de qualidade

Um documento só está pronto quando:

- pode ser encontrado por consulta natural em japonês
- contém português brasileiro utilizável pelo corretor
- separa explicação técnica e fala ao cliente
- inclui limite comercial quando o tema é sensível
- possui referências cruzadas reais
- tem Markdown, DOCX e PDF quando aplicável
- passa no validador do projeto

## Antipadrões

Evitar:

- produzir volume sem camada NotebookLM
- usar português apenas como tradução isolada de termo
- deixar o corretor sem frase pronta para falar com o cliente
- misturar seguro público, seguro privado e decisão da seguradora
- prometer pagamento, cobertura, prazo, aceitação ou resultado
- aceitar rascunho externo sem normalização editorial
- criar documentos sem referências cruzadas

## Decisão editorial permanente

Quando houver conflito entre produtividade e alinhamento ao objetivo final, prevalece o alinhamento ao objetivo final.

Produzir menos documentos, mas com melhor uso real pelo corretor, é preferível a produzir muitos documentos que o NotebookLM recupere mal ou que não ajudem a conversa com o cliente brasileiro.

## Referências

- `README.md`
- `EDITORIAL_RULES.md`
- `01_Editorial/JAPANESE_BROKER_NOTEBOOKLM_STANDARD.md`
- `01_Editorial/SUBAGENT_EDITORIAL_WORKFLOW.md`

## Veja também

- `00_Project/TEAM_ALIGNMENT_REVIEW_2026-06-29.md`
- `16_NotebookLM/ACC_NOTEBOOKLM_PACK_0001.md`
