# AUTONOMOUS_PRODUCTION_PLAN - Plano de ciclos autônomos de produção

## Controle

- Versão: 0.1
- Data: 2026-06-25
- Autor: JP-BR Insurance Knowledge Base
- Histórico: Criação inicial.

## Finalidade

Definir um modelo de produção editorial em ciclos maiores, com baixa dependência de interação do usuário, respeitando sempre o README.md, o EDITORIAL_RULES.md, a estrutura oficial do projeto e a consistência terminológica.

## Regra geral

Cada ciclo autônomo deverá produzir um bloco editorial completo, com:

- 20 verbetes técnicos
- 20 FAQs
- 6 diálogos
- 8 estudos de caso
- documentos consolidados em Markdown, DOCX e PDF
- atualização do índice NotebookLM correspondente
- atualização do CHANGELOG.md
- commit e sincronização com GitHub

## Critérios para escolher o próximo ciclo

O próximo ciclo deve continuar a categoria em andamento quando houver coerência editorial.

Na categoria AUTO, a sequência recomendada é:

1. fundamentos de cobertura
2. contratação e renovação
3. pagamento e alteração contratual
4. sinistro e atendimento
5. documentos, responsabilidade e reparo
6. casos especiais e exceções
7. encerramento da primeira fase AUTO

Quando a categoria AUTO atingir massa crítica inicial, iniciar a categoria VIDA seguindo a mesma lógica.

## Padrão de entrega por ciclo

### Verbetes

Criar códigos sequenciais sem lacunas.

Cada verbete deve conter:

- código
- categoria
- termo japonês
- tradução em português
- definição técnica
- explicação simplificada
- como explicar ao cliente brasileiro
- frases em japonês
- frases em português brasileiro
- FAQs relacionadas
- termos relacionados
- referências cruzadas
- referências
- tags
- veja também
- histórico de revisão

### FAQs

Cada FAQ deve corresponder a uma dúvida real de atendimento e apontar para pelo menos:

- 1 verbete
- 1 diálogo ou estudo de caso quando aplicável

### Diálogos

Cada diálogo deve agrupar de 3 a 5 termos relacionados e simular conversa prática entre:

- corretor japonês
- cliente brasileiro residente no Japão

### Estudos de caso

Cada estudo de caso deve transformar o bloco técnico em decisão prática de atendimento.

## Formatos obrigatórios

Para cada bloco consolidado, gerar:

- Markdown em `19_Markdown`
- DOCX em `18_DOCX`
- PDF em `17_PDF`

## Sincronização

Ao final de cada ciclo:

1. verificar estado do repositório
2. conferir arquivos criados
3. atualizar CHANGELOG.md
4. fazer commit com mensagem objetiva
5. enviar para GitHub

## Limites editoriais

- Não alterar traduções já existentes sem justificativa registrada.
- Não duplicar verbetes.
- Não usar romaji.
- Não quebrar a estrutura oficial.
- Não deixar referências cruzadas pendentes quando o documento relacionado já existir.

## Próximos ciclos recomendados

### AUTO-0061 a AUTO-0080

Tema: casos especiais, exceções de cobertura, exclusões e situações de risco.

Termos sugeridos:

- 免責事項
- 補償対象外
- 飲酒運転
- 無免許運転
- 重大な過失
- 故意
- 地震
- 台風
- 洪水
- 盗難
- いたずら
- 飛び石
- 自然災害
- 使用者
- 記名被保険者
- 家族限定
- 夫婦限定
- 他車運転特約
- ファミリーバイク特約
- 個人賠償責任特約

### AUTO-0081 a AUTO-0100

Tema: fechamento da primeira fase AUTO, revisão de cobertura, atendimento recorrente e preparação para treinamento.

### VIDA-0001 a VIDA-0020

Tema: fundamentos de seguro de vida no Japão para atendimento a brasileiros.

## Histórico de revisão

| Data | Versão | Autor | Alteração |
| --- | --- | --- | --- |
| 2026-06-25 | 0.1 | JP-BR Insurance Knowledge Base | Criação inicial. |
