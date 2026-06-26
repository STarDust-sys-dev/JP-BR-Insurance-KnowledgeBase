#!/usr/bin/env python3
"""Project validation for JP-BR Insurance Knowledge Base."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODE_RE = re.compile(
    r"\b(?:AUTO|VIDA|MED|FAQ-(?:AUTO|VIDA|MED)|DIALOGUE-(?:AUTO|VIDA|MED)|CASE-(?:AUTO|VIDA|MED))-\d{4}\b"
)
ROMAJI_RE = re.compile(
    r"\b(?:hoken|keiyaku|hoshou|shiharai|kyuufukin|menseki|kokuchi|uketori|moushikomi)\b",
    re.IGNORECASE,
)


REQUIRED = {
    "term": [
        "## Código",
        "## Categoria",
        "## Termo Japonês",
        "## Tradução Português",
        "## Definição Técnica",
        "## Explicação Simplificada",
        "## Como explicar ao cliente brasileiro",
        "## Frases utilizadas",
        "## Perguntas frequentes",
        "## Termos relacionados",
        "## Referências cruzadas",
        "## Tags",
        "## Histórico de revisão",
    ],
    "dialogue": [
        "## Código",
        "## Situação de atendimento",
        "## Participantes",
        "## Versão em japonês",
        "## Versão em português brasileiro",
        "## Notas culturais ou comerciais",
        "## Termos relacionados",
        "## Referências cruzadas",
    ],
    "case": [
        "## Código",
        "## Produto ou categoria",
        "## Situação",
        "## Problema",
        "## Análise",
        "## Orientação ao corretor",
        "## Como explicar ao cliente brasileiro",
        "## Termos relacionados",
        "## FAQs relacionadas",
        "## Referências cruzadas",
        "## Histórico de revisão",
    ],
    "notebook": [
        "## Título",
        "## Resumo",
        "## Palavras-chave",
        "## Categorias",
        "## Conteúdo",
        "## Referências",
        "## Veja também",
    ],
}


def read_markdown_files() -> list[Path]:
    return sorted(
        p
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.name != "CHANGELOG.md"
    )


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    files = read_markdown_files()
    texts = {p: p.read_text(encoding="utf-8") for p in files}

    h1_codes: Counter[str] = Counter()
    defined: set[str] = set()
    for path, text in texts.items():
        defined.add(path.stem)
        match = re.match(r"#\s+([^\s]+)", text)
        if match:
            code = match.group(1)
            h1_codes[code] += 1
            defined.add(code)

    missing_refs: list[tuple[str, str]] = []
    for path, text in texts.items():
        for code in CODE_RE.findall(text):
            if code not in defined:
                missing_refs.append((rel(path), code))

    duplicate_h1 = {code: count for code, count in h1_codes.items() if count > 1}

    missing_sections: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for path, text in texts.items():
        path_rel = rel(path)
        if path_rel.startswith("02_MasterDictionary/"):
            for section in REQUIRED["term"]:
                if section not in text:
                    missing_sections["term"].append((path_rel, section))
        elif path_rel.startswith("13_Dialogues/") and path.name != "DIALOGUE_TEMPLATE.md":
            for section in REQUIRED["dialogue"]:
                if section not in text:
                    missing_sections["dialogue"].append((path_rel, section))
        elif path_rel.startswith("15_CaseStudies/") and path.name != "CASE_TEMPLATE.md":
            for section in REQUIRED["case"]:
                if section not in text:
                    missing_sections["case"].append((path_rel, section))
        elif path_rel.startswith("16_NotebookLM/"):
            for section in REQUIRED["notebook"]:
                if section not in text:
                    missing_sections["notebook"].append((path_rel, section))

    romaji_hits = [
        (rel(path), match.group(0))
        for path, text in texts.items()
        for match in ROMAJI_RE.finditer(text)
    ]

    md_stems = {p.stem for p in (ROOT / "19_Markdown").glob("*/*.md")}
    notebook_stems = {p.stem for p in (ROOT / "16_NotebookLM").glob("*.md")}
    expected_format_stems = md_stems | notebook_stems
    docx_stems = {p.stem for p in (ROOT / "18_DOCX").glob("*.docx")}
    pdf_stems = {p.stem for p in (ROOT / "17_PDF").glob("*.pdf")}

    summary = {
        "markdown_files": len(files),
        "missing_cross_references": len(missing_refs),
        "missing_cross_reference_samples": missing_refs[:20],
        "duplicate_h1_codes": duplicate_h1,
        "missing_sections": {k: len(v) for k, v in missing_sections.items()},
        "missing_section_samples": {k: v[:20] for k, v in missing_sections.items()},
        "romaji_hits": len(romaji_hits),
        "romaji_samples": romaji_hits[:20],
        "missing_docx": sorted(expected_format_stems - docx_stems),
        "missing_pdf": sorted(expected_format_stems - pdf_stems),
    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))

    hard_fail = (
        summary["missing_cross_references"]
        or summary["duplicate_h1_codes"]
        or summary["romaji_hits"]
        or summary["missing_docx"]
        or summary["missing_pdf"]
    )
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
