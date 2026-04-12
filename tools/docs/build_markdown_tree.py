#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "artifacts" / "markdown-tree"
EXCLUDE_GLOBS = [
    ".git/**",
    "node_modules/**",
    "dist/**",
    "build/**",
    "coverage/**",
    "vendor/**",
    ".next/**",
    ".venv/**",
    "target/**",
    "artifacts/markdown-tree/**",
]

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


@dataclass
class Doc:
    path: str
    abs_path: Path
    front_matter: dict[str, Any]
    title: str
    headings: list[dict[str, Any]]
    links: list[str]
    resolved_links: list[str]
    unresolved_links: list[str]
    parent: str | None = None
    relation_source: str = ""
    uncertain: bool = False


def run_rg_files() -> list[str]:
    cmd = ["rg", "--files"]
    for g in EXCLUDE_GLOBS:
        cmd.extend(["-g", f"!{g}"])
    out = subprocess.check_output(cmd, cwd=ROOT, text=True)
    files = [line.strip() for line in out.splitlines() if line.strip()]
    result = []
    for f in files:
        p = Path(f)
        name = p.name.lower()
        if p.suffix.lower() in {".md", ".mdx"} or name.startswith("readme"):
            result.append(f)
    return sorted(set(result))


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end() :]
    raw = m.group(1)
    fm: dict[str, Any] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip("\"'")
    return fm, body


def extract_title(fm: dict[str, Any], body: str, path: str) -> str:
    if isinstance(fm.get("title"), str) and fm["title"].strip():
        return fm["title"].strip()
    for m in HEADING_RE.finditer(body):
        if len(m.group(1)) == 1:
            return m.group(2).strip()
    return Path(path).stem


def normalize_link_target(src: Path, raw_target: str, all_docs: set[str]) -> tuple[str | None, str | None]:
    t = raw_target.strip()
    if not t or t.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None, None

    t = t.split("#", 1)[0].split("?", 1)[0].strip()
    if not t:
        return None, None

    cand = (src.parent / t).resolve()
    rel = cand.relative_to(ROOT).as_posix() if str(cand).startswith(str(ROOT)) else None
    if rel and rel in all_docs:
        return rel, None

    if cand.suffix == "":
        cands = [cand.with_suffix(".md"), cand.with_suffix(".mdx"), cand / "README.md", cand / "README.mdx"]
    else:
        cands = [cand]
    for c in cands:
        if str(c).startswith(str(ROOT)):
            rp = c.relative_to(ROOT).as_posix()
            if rp in all_docs:
                return rp, None

    return None, raw_target


def load_docs(paths: list[str]) -> dict[str, Doc]:
    all_docs = set(paths)
    docs: dict[str, Doc] = {}
    for path in paths:
        abs_path = ROOT / path
        text = abs_path.read_text(encoding="utf-8")
        fm, body = parse_front_matter(text)
        headings = [{"level": len(m.group(1)), "text": m.group(2).strip()} for m in HEADING_RE.finditer(body)]
        links = [m.group(1).strip() for m in LINK_RE.finditer(body)]
        resolved, unresolved = [], []
        for link in links:
            target, unres = normalize_link_target(abs_path, link, all_docs)
            if target:
                resolved.append(target)
            elif unres:
                unresolved.append(unres)
        docs[path] = Doc(
            path=path,
            abs_path=abs_path,
            front_matter=fm,
            title=extract_title(fm, body, path),
            headings=headings,
            links=links,
            resolved_links=sorted(set(resolved)),
            unresolved_links=sorted(set(unresolved)),
        )
    return docs


def pick_explicit_parent(doc: Doc, all_docs: set[str]) -> tuple[str | None, str | None, bool]:
    fm = doc.front_matter
    parent_keys = ["parent", "doc_parent", "parent_path"]
    for key in parent_keys:
        val = fm.get(key)
        if isinstance(val, str) and val.strip():
            raw = val.strip()
            cand = (doc.abs_path.parent / raw).resolve() if not raw.startswith("/") else (ROOT / raw.lstrip("/"))
            if str(cand).startswith(str(ROOT)):
                rp = cand.relative_to(ROOT).as_posix()
                if rp in all_docs:
                    return rp, f"front_matter:{key}", False
            if raw in all_docs:
                return raw, f"front_matter:{key}", False
            return None, f"front_matter:{key}", True
    return None, None, False


def directory_parent(path: str, all_docs: set[str]) -> str | None:
    p = Path(path)
    if p.name.lower().startswith("readme"):
        for anc in p.parents:
            if anc == Path("."):
                break
            for name in ("README.md", "README.mdx"):
                cand = (anc / name).as_posix()
                if cand in all_docs and cand != path:
                    return cand
        if path != "README.md" and "README.md" in all_docs:
            return "README.md"
        return None
    for name in ("README.md", "README.mdx"):
        cand = (p.parent / name).as_posix()
        if cand in all_docs:
            return cand
    return None


def link_based_parent(path: str, backlinks: dict[str, list[str]], existing_parent: str | None) -> tuple[str | None, bool]:
    if existing_parent:
        return existing_parent, False
    inbound = sorted(set(backlinks.get(path, [])))
    if len(inbound) == 1:
        return inbound[0], False
    if len(inbound) > 1:
        return None, True
    return None, False


def build(docs: dict[str, Doc]) -> tuple[dict[str, Any], dict[str, list[str]], list[str]]:
    all_docs = set(docs)
    backlinks: dict[str, list[str]] = defaultdict(list)
    for src, doc in docs.items():
        for dst in doc.resolved_links:
            backlinks[dst].append(src)

    unplaced = []
    for path in sorted(docs):
        doc = docs[path]
        parent, source, uncertain = pick_explicit_parent(doc, all_docs)
        if parent:
            doc.parent, doc.relation_source, doc.uncertain = parent, source or "", uncertain
            continue
        if source and uncertain:
            doc.parent, doc.relation_source, doc.uncertain = "_unplaced", source, True
            unplaced.append(path)
            continue

        dir_parent = directory_parent(path, all_docs)
        if dir_parent:
            doc.parent = dir_parent
            doc.relation_source = "directory"
            continue
        if Path(path).parent == Path("."):
            doc.parent = "_root"
            doc.relation_source = "directory:root"
            continue

        link_parent, amb = link_based_parent(path, backlinks, None)
        if link_parent:
            doc.parent = link_parent
            doc.relation_source = "relative_links"
            continue

        if amb:
            doc.parent = "_unplaced"
            doc.relation_source = "relative_links:ambiguous"
            doc.uncertain = True
            unplaced.append(path)
        else:
            doc.parent = "_root"
            doc.relation_source = "directory:root"

    branches: dict[str, list[str]] = defaultdict(list)
    for path, doc in docs.items():
        if doc.parent in docs:
            parent = doc.parent
        elif doc.parent == "_unplaced":
            parent = "_unplaced"
        else:
            parent = "_root"
        branches[parent].append(path)
    for k in list(branches):
        branches[k] = sorted(branches[k])

    def render_node(path: str) -> dict[str, Any]:
        d = docs[path]
        return {
            "path": d.path,
            "title": d.title,
            "parent": d.parent,
            "uncertain": d.uncertain,
            "relation_source": d.relation_source,
            "heading_count": len(d.headings),
            "headings": d.headings,
            "link_count": len(d.resolved_links),
            "resolved_links": d.resolved_links,
            "unresolved_links": d.unresolved_links,
            "children": [render_node(c) for c in branches.get(path, [])],
        }

    root_children = [render_node(c) for c in branches.get("_root", [])]
    unplaced_nodes = [render_node(c) for c in branches.get("_unplaced", [])]

    tree = {
        "meta": {
            "total_markdown_files": len(docs),
            "top_level_branches": [n["path"] for n in root_children],
            "unplaced_count": len(unplaced_nodes),
        },
        "tree": root_children,
        "_unplaced": unplaced_nodes,
    }

    return tree, branches, sorted(unplaced)


def write_outputs(docs: dict[str, Doc], tree: dict[str, Any], branches: dict[str, list[str]]) -> dict[str, Path]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tree_json = OUTPUT_DIR / "tree.json"
    tree_md = OUTPUT_DIR / "tree.md"
    index_csv = OUTPUT_DIR / "index.csv"

    tree_json.write_text(json.dumps(tree, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def md_lines(path: str, indent: int = 0) -> list[str]:
        d = docs[path]
        mark = " ?" if d.uncertain else ""
        line = f"{'  ' * indent}- `{d.path}` — {d.title}{mark}"
        out = [line]
        for child in sorted(branches.get(path, [])):
            out.extend(md_lines(child, indent + 1))
        return out

    lines = ["# Markdown Documentation Tree", "", "## Root", ""]
    for top in sorted(branches.get("_root", [])):
        lines.extend(md_lines(top, 0))
    lines.extend(["", "## _unplaced", ""])
    for up in sorted(branches.get("_unplaced", [])):
        lines.extend(md_lines(up, 0))
    tree_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    with index_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["path", "title", "parent", "heading_count", "link_count"])
        for path in sorted(docs):
            d = docs[path]
            w.writerow([d.path, d.title, d.parent or "", len(d.headings), len(d.resolved_links)])

    return {"tree_json": tree_json, "tree_md": tree_md, "index_csv": index_csv}


def main() -> None:
    paths = run_rg_files()
    docs = load_docs(paths)
    tree, branches, unplaced = build(docs)
    outputs = write_outputs(docs, tree, branches)

    unresolved = sorted({u for d in docs.values() for u in d.unresolved_links})
    top_level = tree["meta"]["top_level_branches"]

    print("Markdown tree build summary")
    print(f"- total markdown files processed: {len(docs)}")
    print(f"- top-level branches: {', '.join(top_level) if top_level else '(none)'}")
    print(f"- unresolved links: {len(unresolved)}")
    if unresolved:
        for u in unresolved[:20]:
            print(f"  - {u}")
        if len(unresolved) > 20:
            print(f"  - ... ({len(unresolved) - 20} more)")
    print(f"- ambiguous/unplaced nodes: {len(unplaced)}")
    if unplaced:
        for p in unplaced[:20]:
            print(f"  - {p}")
        if len(unplaced) > 20:
            print(f"  - ... ({len(unplaced) - 20} more)")
    print("- output paths:")
    for key, path in outputs.items():
        print(f"  - {key}: {path.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
