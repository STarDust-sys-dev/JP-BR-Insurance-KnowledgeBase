# Rendering QA

## Controle

- Versao: 0.1
- Data: 2026-06-26
- Autor: JP-BR Insurance Knowledge Base
- Historico: Criacao inicial.

## Objetivo

Este documento registra o padrao de qualidade para renderizacao visual dos arquivos DOCX e PDF do projeto.

O projeto deve tratar problemas persistentes de renderizacao como problema de ambiente ou cadeia de producao, nao como detalhe isolado de um arquivo.

## Diagnostico resolvido

Em 2026-06-26, a renderizacao DOCX falhava durante a conversao pelo LibreOffice headless porque bibliotecas dinamicas esperadas em caminhos do Homebrew nao estavam presentes:

- `/opt/homebrew/opt/little-cms2/lib/liblcms2.2.dylib`
- `/opt/homebrew/opt/fontconfig/lib/libfontconfig.1.dylib`
- `/opt/homebrew/opt/freetype/lib/libfreetype.6.dylib`

O Homebrew local tambem nao conseguia reinstalar os pacotes porque nao reconhecia a versao do macOS reportada pelo sistema.

## Solucao aplicada

Foram criados vinculos simbolicos nos caminhos esperados pelo LibreOffice, apontando para bibliotecas ja existentes no runtime local do Codex:

- `little-cms2` -> runtime Poppler
- `fontconfig` -> runtime Poppler
- `freetype` -> runtime Poppler

Esta correcao atua no ambiente de renderizacao e vale para documentos DOCX antigos e novos.

## Validacao executada

Apos a correcao, foi executada uma auditoria completa de renderizacao em todos os arquivos DOCX existentes em `18_DOCX`.

Resultado:

- Total de DOCX testados: 71
- DOCX renderizados com sucesso: 71
- Falhas: 0

Arquivos temporarios da auditoria:

- `/private/tmp/jpbr_docx_full_render_audit`

## Regra permanente

Antes de considerar uma entrega DOCX/PDF como final, quando houver tempo operacional, executar pelo menos uma das validacoes abaixo:

1. Renderizacao visual do DOCX final para PNG.
2. Renderizacao visual do PDF final para PNG.
3. Auditoria em lote quando houver mudanca no ambiente de conversao.

Problemas recorrentes devem ser resolvidos pela causa raiz:

- dependencia ausente
- fonte ausente
- conversor quebrado
- script de geracao inconsistente
- formato de saida divergente

Nao tratar erro recorrente apenas com excecao manual por documento.

## Comando de referencia

Usar o renderizador oficial do ambiente:

```bash
/Users/mariomatsuda/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  /Users/mariomatsuda/.codex/plugins/cache/openai-primary-runtime/documents/26.623.12021/skills/documents/render_docx.py \
  18_DOCX/MED_INDEX_0003.docx \
  --output_dir /private/tmp/docx_render_check \
  --emit_pdf
```

## Historico de revisao

| Data | Versao | Autor | Alteracao |
| --- | --- | --- | --- |
| 2026-06-26 | 0.1 | JP-BR Insurance Knowledge Base | Registro da correcao de ambiente e regra de QA de renderizacao. |
