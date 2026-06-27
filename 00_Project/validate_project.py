#!/usr/bin/env python3
"""Project validation for JP-BR Insurance Knowledge Base."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES_RE = r"(?:AUTO|VIDA|MED|FIRE|HOME|BUS|ACC|SALES|SERVICE|FAQ|CASE|LEG|TERM)"
CODE_RE = re.compile(
    rf"\b(?:{CATEGORIES_RE}|FAQ-{CATEGORIES_RE}|DIALOGUE-{CATEGORIES_RE}|CASE-{CATEGORIES_RE})-\d{{4}}\b"
)
ROMAJI_RE = re.compile(
    r"\b(?:hoken|keiyaku|hoshou|shiharai|kyuufukin|menseki|kokuchi|uketori|moushikomi)\b",
    re.IGNORECASE,
)
INTERNAL_LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+\.md(?:#[^)]+)?)\)")
SENSITIVE_TERMS = (
    "aceitação",
    "recusa",
    "não pagamento",
    "pagamento",
    "sinistro",
    "declaração de saúde",
    "imposto",
    "exclusão",
    "franquia",
    "culpa",
    "beneficiário",
    "告知",
    "支払",
    "不支払",
    "引受",
    "免責",
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
    "faq": [
        "## Código",
        "## Categoria",
        "## Pergunta",
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

SECTION_ALIASES = {
    "## Código": ["## コード"],
    "## Categoria": ["## カテゴリー"],
    "## Pergunta": ["## 質問"],
    "## Consulta natural em japonês": ["## 日本語での自然な検索"],
    "## Situação de atendimento": ["## 対応場面"],
    "## Participantes": ["## 参加者"],
    "## Objetivo do diálogo": ["## 対話の目的"],
    "## Versão em japonês": ["## 日本語版"],
    "## Versão em português brasileiro": ["## ブラジルポルトガル語版"],
    "## Notas culturais ou comerciais": ["## 文化・営業上の注意"],
    "## Pontos de atenção para o corretor": ["## 募集人の注意点"],
    "## Casos relacionados": ["## 関連ケース"],
    "## FAQs relacionadas": ["## 関連FAQ"],
    "## Produto ou categoria": ["## 商品・カテゴリー"],
    "## Situação": ["## 状況"],
    "## Problema": ["## 問題"],
    "## Análise": ["## 分析"],
    "## Orientação ao corretor": ["## 募集人への対応方針"],
    "## Resultado esperado": ["## 期待される結果"],
    "## Diálogos relacionados": ["## 関連対話"],
    "## Resposta técnica": ["## 技術的回答"],
    "## Como responder ao cliente brasileiro": ["## ブラジル人顧客への回答"],
    "## Próximo passo seguro": ["## 安全な次のステップ"],
    "## Limite comercial/compliance": ["## コンプライアンス上の注意"],
    "## Termo Japonês": ["## 日本語用語"],
    "## Tradução Português": ["## ポルトガル語訳"],
    "## Definição Técnica": ["## 技術的定義"],
    "## Explicação Simplificada": ["## 簡単な説明"],
    "## Como explicar ao cliente brasileiro": ["## ブラジル人顧客への説明方法"],
    "## Frases utilizadas": ["## 使用フレーズ"],
    "## Perguntas frequentes": ["## よくある質問"],
    "## Termos relacionados": ["## 関連用語"],
    "## Referências cruzadas": ["## 相互参照"],
    "## Referências": ["## 参考資料"],
    "## Tags": ["## タグ"],
    "## Veja também": ["## 関連項目"],
    "## Histórico de revisão": ["## 改訂履歴"],
}


def read_markdown_files() -> list[Path]:
    return sorted(
        p
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and p.name != "CHANGELOG.md"
    )


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def section_body(text: str, section: str) -> str | None:
    candidates = [section, *SECTION_ALIASES.get(section, [])]
    match = None
    for candidate in candidates:
        match = re.search(rf"^{re.escape(candidate)}\s*$", text, re.MULTILINE)
        if match:
            break
    if not match:
        return None
    start = match.end()
    next_section = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_section.start() if next_section else len(text)
    return text[start:end].strip()


def has_japanese(text: str) -> bool:
    return bool(re.search(r"[ぁ-んァ-ン一-龥]", text))


def resolve_internal_link(source: Path, raw_link: str) -> bool:
    link_path = raw_link.split("#", 1)[0].replace("%20", " ")
    candidates = []
    if link_path.startswith("/"):
        candidates.append(Path(link_path))
    else:
        candidates.append((source.parent / link_path).resolve())
        candidates.append((ROOT / link_path).resolve())
    return any(path.exists() for path in candidates)


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
    empty_sections: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for path, text in texts.items():
        path_rel = rel(path)
        kind = None
        if path_rel.startswith("02_MasterDictionary/"):
            kind = "term"
        elif path_rel.startswith("14_FAQ/") and path.name != "FAQ_TEMPLATE.md":
            kind = "faq"
        elif path_rel.startswith("13_Dialogues/") and path.name != "DIALOGUE_TEMPLATE.md":
            kind = "dialogue"
        elif path_rel.startswith("15_CaseStudies/") and path.name != "CASE_TEMPLATE.md":
            kind = "case"
        elif path_rel.startswith("16_NotebookLM/"):
            kind = "notebook"
        if not kind:
            continue
        for section in REQUIRED[kind]:
            body = section_body(text, section)
            if body is None:
                missing_sections[kind].append((path_rel, section))
            elif not body:
                empty_sections[kind].append((path_rel, section))
        if kind == "faq":
            has_new_answer = (
                section_body(text, "## Resposta técnica") is not None
                and section_body(text, "## Como responder ao cliente brasileiro") is not None
            )
            has_old_answer = "## Resposta curta" in text and "## Resposta explicada" in text
            if not (has_new_answer or has_old_answer):
                missing_sections["faq"].append((path_rel, "answer model: Resposta técnica + cliente OR Resposta curta + explicada"))

    romaji_hits = [
        (rel(path), match.group(0))
        for path, text in texts.items()
        for match in ROMAJI_RE.finditer(text)
    ]

    broken_links: list[tuple[str, str]] = []
    for path, text in texts.items():
        for raw_link in INTERNAL_LINK_RE.findall(text):
            if not resolve_internal_link(path, raw_link):
                broken_links.append((rel(path), raw_link))

    warnings: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for path, text in texts.items():
        path_rel = rel(path)
        if path_rel.startswith("14_FAQ/") and section_body(text, "## Consulta natural em japonês") is None:
            warnings["faq_without_japanese_query"].append((path_rel, "missing ## Consulta natural em japonês"))
        if path_rel.startswith(("14_FAQ/", "15_CaseStudies/")):
            lower = text.lower()
            if any(term.lower() in lower for term in SENSITIVE_TERMS) and section_body(text, "## Limite comercial/compliance") is None:
                warnings["sensitive_doc_without_compliance_limit"].append((path_rel, "missing ## Limite comercial/compliance"))
        if path_rel.startswith("16_NotebookLM/") and not has_japanese(text):
            warnings["notebook_without_japanese"].append((path_rel, "no Japanese text found"))
        if path_rel.startswith(("02_MasterDictionary/", "14_FAQ/", "13_Dialogues/", "15_CaseStudies/")):
            if "<ruby>" in text or "<rt>" in text:
                warnings["customer_portuguese_hidden_in_ruby"].append((path_rel, "customer Portuguese should be explicit, not hidden in ruby markup"))
        if path_rel.startswith(("02_MasterDictionary/", "14_FAQ/", "13_Dialogues/", "15_CaseStudies/")):
            if (
                "ブラジル人顧客" in text
                and "Português brasileiro:" not in text
                and "## ブラジルポルトガル語版" not in text
                and "### PT-Br" not in text
                and "### ポルトガル語で伝える内容" not in text
            ):
                warnings["customer_portuguese_block_missing"].append((path_rel, "missing explicit Portuguese customer-facing text"))

    md_stems = {p.stem for p in (ROOT / "19_Markdown").glob("*/*.md")}
    notebook_stems = {p.stem for p in (ROOT / "16_NotebookLM").glob("*.md")}
    governance_stems = {
        p.stem
        for folder in ("00_Project", "01_Editorial", "03_Glossary", "04_Automobile", "05_Life", "06_Medical")
        for p in (ROOT / folder).glob("*.md")
    }
    expected_format_stems = md_stems | notebook_stems | governance_stems
    docx_stems = {p.stem for p in (ROOT / "18_DOCX").glob("*.docx")}
    pdf_stems = {p.stem for p in (ROOT / "17_PDF").glob("*.pdf")}

    summary = {
        "markdown_files": len(files),
        "missing_cross_references": len(missing_refs),
        "missing_cross_reference_samples": missing_refs[:20],
        "duplicate_h1_codes": duplicate_h1,
        "missing_sections": {k: len(v) for k, v in missing_sections.items()},
        "missing_section_samples": {k: v[:20] for k, v in missing_sections.items()},
        "empty_sections": {k: len(v) for k, v in empty_sections.items()},
        "empty_section_samples": {k: v[:20] for k, v in empty_sections.items()},
        "broken_internal_links": len(broken_links),
        "broken_internal_link_samples": broken_links[:20],
        "warnings": {k: len(v) for k, v in warnings.items()},
        "warning_samples": {k: v[:20] for k, v in warnings.items()},
        "romaji_hits": len(romaji_hits),
        "romaji_samples": romaji_hits[:20],
        "missing_docx": sorted(expected_format_stems - docx_stems),
        "missing_pdf": sorted(expected_format_stems - pdf_stems),
    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))

    hard_fail = (
        summary["missing_cross_references"]
        or summary["duplicate_h1_codes"]
        or summary["missing_sections"]
        or summary["empty_sections"]
        or summary["broken_internal_links"]
        or summary["romaji_hits"]
        or summary["missing_docx"]
        or summary["missing_pdf"]
    )
    return 1 if hard_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
