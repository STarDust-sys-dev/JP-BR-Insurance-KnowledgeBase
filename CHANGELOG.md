# CHANGELOG

## 2026-06-27

### Adicionado

- Correção integral do padrão de atendimento ao cliente brasileiro: frases em português brasileiro agora aparecem explicitamente antes da leitura em katakana nos verbetes, FAQs MED/FIRE/HOME, diálogos FIRE/HOME e estudos de caso FIRE/HOME; remoção de marcação `ruby` nos conteúdos de atendimento; reforço do validador para bloquear português escondido e ausência de bloco português ao cliente.

- Padronização das 60 FAQs MED: estrutura em japonês para consulta do corretor, resposta ao cliente em português brasileiro com leitura em katakana, reforço de compliance médico e regeneração dos pacotes `MED_FAQ_0001_0020`, `MED_FAQ_0021_0040` e `MED_FAQ_0041_0060`.

- Padronização dos guias e pacotes NotebookLM FIRE/HOME: mapas de consulta em japonês para o corretor, fluxo recomendado de busca, orientação de uso de FAQ/DIALOGUE/CASE e regeneração de DOCX/PDF de `FIRE_INDEX_0001`, `FIRE_NOTEBOOKLM_PACK_0001`, `FIRE_NAVIGATION_GUIDE`, `HOME_INDEX_0001`, `HOME_NOTEBOOKLM_PACK_0001` e `HOUSING_NAVIGATION_GUIDE`.

- Padronização dos estudos de caso FIRE e HOME: estrutura em japonês, análise e orientação para o corretor japonês, explicação ao cliente em português brasileiro com leitura em katakana e regeneração dos pacotes `FIRE_CASES_0001_0008` e `HOME_CASES_0001_0008`.

- Padronização dos diálogos FIRE e HOME: estrutura interna em japonês, orientação para o corretor japonês, falas em português brasileiro com leitura em katakana e regeneração dos pacotes `FIRE_DIALOGUES_0001_0005` e `HOME_DIALOGUES_0001_0005`.

- Padronização das FAQs FIRE e HOME: títulos internos em japonês, resposta técnica em japonês, resposta ao cliente em português brasileiro com leitura em katakana, reforço de compliance e regeneração dos pacotes `FIRE_FAQ_0001_0020` e `HOME_FAQ_0001_0020`.
- Ampliação do validador para reconhecer códigos e referências das categorias FIRE, HOME, BUS, ACC, SALES, SERVICE, FAQ, CASE, LEG e TERM, com aliases japoneses para seções de FAQ.

- Padronização linguística dos verbetes do dicionário mestre: títulos internos em japonês, `技術的定義` e `簡単な説明` em japonês, e `ブラジル人顧客への説明方法` com frase em português brasileiro acompanhada de leitura em katakana para uso pelo corretor japonês.

- Abertura da categoria HOME/Housing: criação dos primeiros 20 verbetes, 20 FAQs, 5 diálogos, 8 estudos de caso, guia de navegação, índice NotebookLM e pacote NotebookLM, com versões Markdown, DOCX e PDF.

- Abertura da categoria FIRE: criação dos primeiros 20 verbetes, 20 FAQs, 5 diálogos, 8 estudos de caso, guia de navegação, índice NotebookLM e pacote NotebookLM, com versões Markdown, DOCX e PDF.

- Normalizacao dos dialogos MED iniciais: inclusao de pontos de atencao para o corretor e casos relacionados em `DIALOGUE-MED-0001` a `DIALOGUE-MED-0005`, com regeneracao do pacote `MED_DIALOGUES_0001_0005`.

## 2026-06-26

### Adicionado

- Auditoria estrutural `00_Project/PROJECT_AUDIT_2026-06-26.md` com riscos, decisoes editoriais e proximos passos para uso no NotebookLM.
- Padrao `01_Editorial/JAPANESE_BROKER_NOTEBOOKLM_STANDARD.md` para consulta por corretor japones e atendimento a cliente brasileiro.
- Glossario mestre `03_Glossary/MASTER_TERMINOLOGY.md` para termos recorrentes entre categorias.
- Validador `00_Project/validate_project.py` para referencias cruzadas, secoes obrigatorias, romaji e existencia de formatos finais.
- Pacotes praticos `AUTO_NOTEBOOKLM_PACK_0001.md` e `VIDA_NOTEBOOKLM_PACK_0001.md` para consulta do corretor japones no atendimento a brasileiros.
- Primeiro pacote pratico `MED_NOTEBOOKLM_PACK_0001.md` para consulta do corretor japones sobre seguro medico no atendimento a brasileiros.
- Guias de navegacao por produto em `04_Automobile`, `05_Life` e `06_Medical`, conectando pacotes NotebookLM, indices, verbetes, FAQs, dialogos e casos.
- Fluxo editorial `01_Editorial/SUBAGENT_EDITORIAL_WORKFLOW.md` para uso controlado de subagentes como equipe de revisao especializada.
- Relatorio `00_Project/SUBAGENT_PILOT_REPORT_2026-06-26.md` consolidando achados do primeiro piloto com subagentes.
- Revisao `00_Project/SUBAGENT_STRUCTURE_REVIEW_2026-06-26.md` avaliando o resultado do piloto e transformando warnings em backlog editorial.
- Templates de FAQ, dialogo e estudo de caso reforcados com consulta natural em japones, proximo passo e limite comercial/compliance quando aplicavel.
- Primeiro ciclo de normalizacao de FAQs sensiveis AUTO: `FAQ-AUTO-0002`, `FAQ-AUTO-0004`, `FAQ-AUTO-0006`, `FAQ-AUTO-0007`, `FAQ-AUTO-0008`, `FAQ-AUTO-0009`, `FAQ-AUTO-0010`, `FAQ-AUTO-0020`, `FAQ-AUTO-0025` e `FAQ-AUTO-0028`.
- Primeiro ciclo de normalizacao de FAQs sensiveis VIDA: `FAQ-VIDA-0018`, `FAQ-VIDA-0041`, `FAQ-VIDA-0042`, `FAQ-VIDA-0044`, `FAQ-VIDA-0045`, `FAQ-VIDA-0049`, `FAQ-VIDA-0050`, `FAQ-VIDA-0053`, `FAQ-VIDA-0085` e `FAQ-VIDA-0094`.
- Primeiro ciclo de normalizacao de FAQs sensiveis MED: `FAQ-MED-0008`, `FAQ-MED-0019`, `FAQ-MED-0034`, `FAQ-MED-0037`, `FAQ-MED-0038`, `FAQ-MED-0046`, `FAQ-MED-0048`, `FAQ-MED-0049`, `FAQ-MED-0051` e `FAQ-MED-0053`.
- Segundo ciclo de normalizacao de FAQs sensiveis AUTO: `FAQ-AUTO-0029`, `FAQ-AUTO-0030`, `FAQ-AUTO-0031`, `FAQ-AUTO-0032`, `FAQ-AUTO-0033`, `FAQ-AUTO-0034`, `FAQ-AUTO-0035`, `FAQ-AUTO-0036`, `FAQ-AUTO-0038` e `FAQ-AUTO-0039`.
- Terceiro ciclo de normalizacao de FAQs sensiveis AUTO: `FAQ-AUTO-0040` a `FAQ-AUTO-0049`, cobrindo culpa, acordo, danos, reparo, avaliacao, perda total/parcial, guincho, oficina e decisao da seguradora.
- Quarto ciclo de normalizacao de FAQs sensiveis AUTO: `FAQ-AUTO-0050` a `FAQ-AUTO-0059`, cobrindo papel da corretora, proposta, declaracoes, alteracoes, apolice, renovacao, interrupcao e exclusoes.
- Quinto ciclo de normalizacao de FAQs sensiveis AUTO: `FAQ-AUTO-0060` a `FAQ-AUTO-0077`, cobrindo exclusoes graves, desastres naturais, roubo/furto, vandalismo, uso do veiculo, restricoes de condutor e coberturas adicionais.
- Sexto ciclo de normalizacao de FAQs AUTO: `FAQ-AUTO-0078` a `FAQ-AUTO-0097`, cobrindo revisao de coberturas, condicoes contratuais, informacoes importantes, dados cadastrais, documentos, sinistro, cancelamento, renovacao e pos-venda.
- Fechamento dos avisos de consulta japonesa em FAQs AUTO antigas: normalizacao de 19 arquivos entre `FAQ-AUTO-0001` e `FAQ-AUTO-0037` e regeneracao dos pacotes `AUTO_FAQ_0001_0010`, `AUTO_FAQ_0011_0020`, `AUTO_FAQ_0021_0027` e `AUTO_FAQ_0028_0037`.
- Segundo ciclo de normalizacao de FAQs MED: `FAQ-MED-0001` a `FAQ-MED-0020`, cobrindo fundamentos do seguro medico, internacao, cirurgia, valor diario, limites, tratamento avancado, cancer, doencas graves, gravidez, saude mental, doenca preexistente e inicio de cobertura.
- Terceiro ciclo de normalizacao de FAQs MED: `FAQ-MED-0021` a `FAQ-MED-0040`, cobrindo solicitacao de beneficio, diagnostico, recibos, comprovantes, prazos, documentos, dados bancarios, analise de pagamento, pendencias, reanalise, deposito e beneficiario.
- Quarto ciclo de normalizacao de FAQs MED: `FAQ-MED-0041` a `FAQ-MED-0060`, cobrindo proposta, segurado, contratante, premio, pagamento, exame medico, aceitacao, condicoes especiais, exclusoes, adiamento, formacao contratual, apolice, cancelamento no prazo legal, retirada de proposta e alteracao contratual.
- Segundo ciclo de normalizacao de FAQs VIDA: `FAQ-VIDA-0001` a `FAQ-VIDA-0020`, cobrindo fundamentos do seguro de vida, morte, seguros temporario/vitalicio/misto, cancer, incapacidade, papeis contratuais, beneficiario, premio, periodo de pagamento, vigencia, resgate, declaracao de saude, carencia e inicio de cobertura.
- Terceiro ciclo de normalizacao de FAQs VIDA: `FAQ-VIDA-0021` a `FAQ-VIDA-0040`, cobrindo invalidez grave, tres doencas graves, cancer, internacao, cirurgia, tratamento ambulatorial, tratamento avancado, doencas femininas, estilo de vida, cuidados de longa duracao, demencia, renda futura, previdencia, seguro educacional, garantia de renda, valor segurado, planejamento de vida e revisao por eventos familiares.
- Quarto ciclo de normalizacao de FAQs VIDA: `FAQ-VIDA-0041` a `FAQ-VIDA-0060`, cobrindo proposta, declaracao de saude, historico medico, internacoes, cirurgias, exame de saude, analise de aceitacao, condicoes especiais, adicional de premio, exclusoes, recusa, nao formacao do contrato, cancelamento, perda de validade, reativacao, reducao, seguro pago e seguro temporario prorrogado.
- Quinto ciclo de normalizacao de FAQs VIDA: `FAQ-VIDA-0061` a `FAQ-VIDA-0080`, cobrindo pedido de indenizacao e beneficio, formularios, relatorio medico, documentos de falecimento, registro familiar, residencia, identificacao, conta bancaria, analise de pagamento, decisao da seguradora, nao pagamento, prazo, documentos adicionais, confirmacao de fatos, investigacao, representante designado, solicitacao por terceiro, beneficiario menor de idade e herdeiros.
- Sexto ciclo de normalizacao de FAQs VIDA: `FAQ-VIDA-0081` a `FAQ-VIDA-0100`, cobrindo conferencia contratual, alteracoes, endereco, nome, beneficiario, representante, apolice, segunda via, comprovante de deducao, impostos, ajuste de fim de ano, declaracao final, tratamento fiscal, resgate, My Number, protecao de dados, pos-venda, revisao periodica e registro do atendimento.
- Normalizacao de compliance em estudos de caso AUTO: inclusao de limite comercial/compliance nos casos `CASE-AUTO-0001` a `CASE-AUTO-0044` quando ausente e regeneracao dos pacotes consolidados `AUTO_CASES`.
- Normalizacao de compliance em estudos de caso MED: inclusao de limite comercial/compliance em `CASE-MED-0001` a `CASE-MED-0024` e regeneracao dos pacotes consolidados `MED_CASES`.
- Normalizacao de compliance em estudos de caso VIDA: inclusao de limite comercial/compliance em `CASE-VIDA-0001` a `CASE-VIDA-0040` e regeneracao dos pacotes consolidados `VIDA_CASES`.
- Documento `00_Project/RENDERING_QA.md` com registro da correção definitiva do ambiente de renderização DOCX e regra permanente de QA visual.
- Auditoria completa de renderização DOCX concluída com 71 arquivos testados, 71 aprovados e 0 falhas.
- Terceiro ciclo MED com 20 verbetes (`MED-0041` a `MED-0060`), 20 FAQs (`FAQ-MED-0041` a `FAQ-MED-0060`), 5 diálogos (`DIALOGUE-MED-0011` a `DIALOGUE-MED-0015`) e 8 estudos de caso (`CASE-MED-0017` a `CASE-MED-0024`).
- Índice `MED_INDEX_0003.md` para NotebookLM com foco em proposta, declaração de saúde, análise de aceitação, condições especiais, apólice e alteração contratual.
- Documentos consolidados do terceiro ciclo MED em Markdown, DOCX e PDF.
- Segundo ciclo MED com 20 verbetes (`MED-0021` a `MED-0040`), 20 FAQs (`FAQ-MED-0021` a `FAQ-MED-0040`), 5 diálogos (`DIALOGUE-MED-0006` a `DIALOGUE-MED-0010`) e 8 estudos de caso (`CASE-MED-0009` a `CASE-MED-0016`).
- Índice `MED_INDEX_0002.md` para NotebookLM com foco em solicitação de benefício, documentos médicos, análise de pagamento, pendências e reanálise.
- Documentos consolidados do segundo ciclo MED em Markdown, DOCX e PDF.
- Abertura da categoria MED com estrutura editorial dedicada em dicionário mestre, FAQ, diálogos, estudos de caso e consolidados.
- Primeiro ciclo MED com 20 verbetes (`MED-0001` a `MED-0020`), 20 FAQs (`FAQ-MED-0001` a `FAQ-MED-0020`), 5 diálogos (`DIALOGUE-MED-0001` a `DIALOGUE-MED-0005`) e 8 estudos de caso (`CASE-MED-0001` a `CASE-MED-0008`).
- Índice inicial `MED_INDEX_0001.md` para NotebookLM e documentos consolidados MED em Markdown, DOCX e PDF.
- Quinto ciclo VIDA com 20 verbetes (`VIDA-0081` a `VIDA-0100`), 20 FAQs (`FAQ-VIDA-0081` a `FAQ-VIDA-0100`), 5 diálogos (`DIALOGUE-VIDA-0021` a `DIALOGUE-VIDA-0025`) e 8 estudos de caso (`CASE-VIDA-0033` a `CASE-VIDA-0040`).
- Atualização do índice `VIDA_INDEX_0001.md` com pós-venda, alterações contratuais, beneficiários, documentos fiscais e registro de atendimento.
- Documentos consolidados do quinto ciclo VIDA em Markdown, DOCX e PDF.
- Quarto ciclo VIDA com 20 verbetes (`VIDA-0061` a `VIDA-0080`), 20 FAQs (`FAQ-VIDA-0061` a `FAQ-VIDA-0080`), 5 diálogos (`DIALOGUE-VIDA-0016` a `DIALOGUE-VIDA-0020`) e 8 estudos de caso (`CASE-VIDA-0025` a `CASE-VIDA-0032`).
- Atualização do índice `VIDA_INDEX_0001.md` com solicitação de indenização, documentos, análise de pagamento e representantes.
- Documentos consolidados do quarto ciclo VIDA em Markdown, DOCX e PDF.
- Terceiro ciclo VIDA com 20 verbetes (`VIDA-0041` a `VIDA-0060`), 20 FAQs (`FAQ-VIDA-0041` a `FAQ-VIDA-0060`), 5 diálogos (`DIALOGUE-VIDA-0011` a `DIALOGUE-VIDA-0015`) e 8 estudos de caso (`CASE-VIDA-0017` a `CASE-VIDA-0024`).
- Atualização do índice `VIDA_INDEX_0001.md` com contratação, aceitação, condições especiais e manutenção do contrato.
- Documentos consolidados do terceiro ciclo VIDA em Markdown, DOCX e PDF.
- Segundo ciclo VIDA com 20 verbetes (`VIDA-0021` a `VIDA-0040`), 20 FAQs (`FAQ-VIDA-0021` a `FAQ-VIDA-0040`), 5 diálogos (`DIALOGUE-VIDA-0006` a `DIALOGUE-VIDA-0010`) e 8 estudos de caso (`CASE-VIDA-0009` a `CASE-VIDA-0016`).
- Atualização do índice `VIDA_INDEX_0001.md` e correção do histórico inicial do índice VIDA.
- Documentos consolidados do segundo ciclo VIDA em Markdown, DOCX e PDF.

### Corrigido

- Normalizados `DIALOGUE-MED-0006` a `DIALOGUE-MED-0015` com participantes, versao japonesa, versao em portugues brasileiro, notas culturais/comerciais e pontos de atencao para o corretor.
- Reforcados `FAQ-VIDA-0018`, `FAQ-MED-0037`, `DIALOGUE-MED-0012` e `CASE-AUTO-0038` com consulta japonesa, linguagem mais natural, proximo passo ou limite comercial/compliance.
- Normalizado controle de versao das FAQs AUTO e VIDA alteradas nos ciclos de compliance para alinhar campo `Versao` e historico de revisao.
- Corrigida referência cruzada inexistente `CASE-MED-0025` em `DIALOGUE-MED-0015`, direcionando para `CASE-MED-0024` e ampliando o caso relacionado com `MED-0058` a `MED-0060`.

### Definido

- `EDITORIAL_RULES.md` atualizado para exigir camada NotebookLM orientada ao corretor japones, controle de termos recorrentes e validacao automatica antes de entregas grandes.
- `README.md` e `EDITORIAL_RULES.md` atualizados com aviso de uso, limites comerciais e regras de compliance para conteudos sensiveis.
- `SUBAGENT_EDITORIAL_WORKFLOW.md` atualizado para definir entradas, saidas por papel, consolidacao pelo editor-chefe e criterio de uso dos subagentes.

## 2026-06-25

### Adicionado

- Abertura da categoria VIDA com estrutura editorial dedicada em dicionário mestre, FAQ, diálogos, estudos de caso e consolidados.
- Primeiro ciclo VIDA com 20 verbetes (`VIDA-0001` a `VIDA-0020`), 20 FAQs (`FAQ-VIDA-0001` a `FAQ-VIDA-0020`), 5 diálogos (`DIALOGUE-VIDA-0001` a `DIALOGUE-VIDA-0005`) e 8 estudos de caso (`CASE-VIDA-0001` a `CASE-VIDA-0008`).
- Índice inicial `VIDA_INDEX_0001.md` para NotebookLM e documentos consolidados VIDA em Markdown, DOCX e PDF.
- Nono e décimo lotes AUTO com 20 verbetes no dicionário mestre (`AUTO-0081` a `AUTO-0100`).
- Nono e décimo lotes AUTO com 20 FAQs (`FAQ-AUTO-0078` a `FAQ-AUTO-0097`), 6 diálogos (`DIALOGUE-AUTO-0027` a `DIALOGUE-AUTO-0032`) e 8 estudos de caso (`CASE-AUTO-0037` a `CASE-AUTO-0044`).
- Documentos consolidados de fechamento da primeira fase AUTO em Markdown, DOCX e PDF.
- Sétimo e oitavo lotes AUTO com 20 verbetes no dicionário mestre (`AUTO-0061` a `AUTO-0080`).
- Sétimo e oitavo lotes AUTO com 20 FAQs (`FAQ-AUTO-0058` a `FAQ-AUTO-0077`), 6 diálogos (`DIALOGUE-AUTO-0021` a `DIALOGUE-AUTO-0026`) e 8 estudos de caso (`CASE-AUTO-0029` a `CASE-AUTO-0036`).
- Documentos consolidados dos lotes AUTO de exclusões, riscos de cobertura e coberturas adicionais especiais em Markdown, DOCX e PDF.
- Plano de produção autônoma `AUTONOMOUS_PRODUCTION_PLAN.md`, com regra de ciclos maiores e baixa dependência de interação.
- Versões DOCX e PDF do plano de produção autônoma.
- Quinto e sexto lotes AUTO com 20 verbetes no dicionário mestre (`AUTO-0041` a `AUTO-0060`).
- Quinto e sexto lotes AUTO com 20 FAQs (`FAQ-AUTO-0038` a `FAQ-AUTO-0057`), 6 diálogos (`DIALOGUE-AUTO-0015` a `DIALOGUE-AUTO-0020`) e 8 estudos de caso (`CASE-AUTO-0021` a `CASE-AUTO-0028`).
- Documentos consolidados dos lotes AUTO de sinistro, documentos e atendimento em Markdown, DOCX e PDF.
- Quarto lote de 10 verbetes AUTO no dicionário mestre (`AUTO-0031` a `AUTO-0040`).
- Documento consolidado do quarto lote AUTO em Markdown, DOCX e PDF.
- Quarto lote de 10 FAQs AUTO (`FAQ-AUTO-0028` a `FAQ-AUTO-0037`) com referências cruzadas aos verbetes AUTO.
- Documento consolidado do quarto lote de FAQs AUTO em Markdown, DOCX e PDF.
- Quarto lote de 3 diálogos AUTO (`DIALOGUE-AUTO-0012` a `DIALOGUE-AUTO-0014`) e 4 estudos de caso AUTO (`CASE-AUTO-0017` a `CASE-AUTO-0020`).
- Documentos consolidados do quarto lote de diálogos e estudos de caso AUTO em Markdown, DOCX e PDF.
- Atualização do índice `AUTO_INDEX_0001.md` com o quarto lote AUTO.
- Terceiro lote de 7 FAQs AUTO (`FAQ-AUTO-0021` a `FAQ-AUTO-0027`) com referências cruzadas aos verbetes AUTO.
- Documento consolidado do terceiro lote de FAQs AUTO em Markdown, DOCX e PDF.
- Terceiro lote de 3 diálogos AUTO (`DIALOGUE-AUTO-0009` a `DIALOGUE-AUTO-0011`) e 4 estudos de caso AUTO (`CASE-AUTO-0013` a `CASE-AUTO-0016`).
- Documentos consolidados do terceiro lote de diálogos e estudos de caso AUTO em Markdown, DOCX e PDF.
- Atualização do índice `AUTO_INDEX_0001.md` com o terceiro lote AUTO.
- Terceiro lote de 10 verbetes AUTO no dicionário mestre (`AUTO-0021` a `AUTO-0030`).
- Documento consolidado do terceiro lote AUTO em Markdown, DOCX e PDF.
- Segundo lote de 4 diálogos AUTO (`DIALOGUE-AUTO-0005` a `DIALOGUE-AUTO-0008`) e 4 estudos de caso AUTO (`CASE-AUTO-0009` a `CASE-AUTO-0012`).
- Documentos consolidados do segundo lote de diálogos e estudos de caso AUTO em Markdown, DOCX e PDF.
- Atualização do índice `AUTO_INDEX_0001.md` com o segundo lote AUTO.
- Segundo lote de 10 FAQs AUTO (`FAQ-AUTO-0011` a `FAQ-AUTO-0020`) com referências cruzadas aos verbetes AUTO.
- Documento consolidado do segundo lote de FAQs AUTO em Markdown, DOCX e PDF.
- Segundo lote de 10 verbetes AUTO no dicionário mestre (`AUTO-0011` a `AUTO-0020`).
- Documento consolidado do segundo lote AUTO em Markdown, DOCX e PDF.
- Roteiro editorial `AUTO_ROADMAP_0001.md` com próximos verbetes, FAQs, diálogos e estudos de caso recomendados.
- Índice inicial `AUTO_INDEX_0001.md` para NotebookLM, conectando verbetes, FAQs, diálogos e estudos de caso AUTO.
- Primeiro lote de 8 estudos de caso AUTO (`CASE-AUTO-0001` a `CASE-AUTO-0008`) conectados aos verbetes, FAQs e diálogos iniciais.
- Primeiro lote de 4 diálogos AUTO (`DIALOGUE-AUTO-0001` a `DIALOGUE-AUTO-0004`) conectados aos verbetes e FAQs iniciais.
- Primeiro lote de 10 FAQs AUTO (`FAQ-AUTO-0001` a `FAQ-AUTO-0010`) com referências cruzadas aos verbetes AUTO.
- Documentos consolidados dos lotes AUTO de FAQs, diálogos e estudos de caso em Markdown, DOCX e PDF.
- Primeiro lote de 10 verbetes AUTO no dicionário mestre (`AUTO-0001` a `AUTO-0010`).
- Documento consolidado do primeiro lote AUTO em Markdown, DOCX e PDF.
- Modelos oficiais `TERM_TEMPLATE.md`, `FAQ_TEMPLATE.md`, `DIALOGUE_TEMPLATE.md` e `CASE_TEMPLATE.md`.
- Versões DOCX e PDF dos modelos oficiais.
- Documento `EDITORIAL_RULES.md` com regras editoriais operacionais alinhadas ao README oficial.
- Estrutura oficial de pastas do projeto conforme especificação do README.
- Arquivos `.gitkeep` para preservar diretórios editoriais vazios no Git.

### Definido

- O `EDITORIAL_RULES.md` passa a funcionar como constituição editorial permanente do projeto.
- O README.md passa a ser tratado como especificação oficial do projeto.
- O desenvolvimento editorial deverá manter consistência terminológica, referências cruzadas e entregas incrementais em Markdown, DOCX e PDF.
