"""Inventory placeholder, blank, and vacuous executable files and ratchet them down.

Scans tracked files on the scripting, automation, and data-processing surfaces
(scripts, tools, pipelines, pipeline specs, connectors, packages, apps, tests,
workflows) and the schema, contract, and policy surfaces they validate against for files that look implemented but are not:

* ``EMPTY_FILE``            zero-byte file other than ``__init__.py``/``.gitkeep``/``py.typed``
* ``PLACEHOLDER_MARKER``    non-Markdown file whose header declares a greenfield/PROPOSED
                            placeholder, scaffold, or stub
* ``STUB_MODULE``           Python module (not ``__init__``/``conftest``) with no statements,
                            or only ``pass``/``...``/``raise NotImplementedError`` bodies
* ``VACUOUS_TEST``          test module whose every test only asserts a constant or passes
* ``TODO_ECHO_SCRIPT``      shell script whose only action is echoing a TODO (false success)
* ``UNRESOLVED_DESCRIPTOR`` connector descriptor with ``TBD`` field values

``--check`` compares findings with the reviewed baseline: a new finding fails
(scaffolding must not grow silently) and a baseline entry that no longer occurs
also fails until the baseline is regenerated, so the count only ratchets down.
Output is a review aid; it grants no readiness, release, or publication authority.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ROOT / "tools" / "qa" / "scaffold_baseline.json"
SCHEMA_VERSION = "kfm.scaffold-inventory/v1"
SURFACES = ("scripts", "tools", "pipelines", "pipeline_specs", "connectors", "packages",
            "apps", "tests", ".github/workflows", "schemas", "contracts", "policy")
EMPTY_ALLOWED = frozenset({"__init__.py", ".gitkeep", ".keep", "py.typed"})
TEXT_SUFFIXES = frozenset({".py", ".sh", ".yaml", ".yml", ".toml", ".json", ".js", ".mjs",
                           ".ts", ".tsx", ".rego", ".sql", ".cfg", ".ini"})
MARKER = re.compile(r"\b(?:greenfield|PROPOSED)\s+(?:placeholder|scaffold)\b"
                    r"|\bgreenfield\s+[\w-]+\s+stub\b", re.IGNORECASE)
TBD_FIELD = re.compile(r"^\s*[A-Za-z_][\w-]*\s*:\s*['\"]?TBD['\"]?\s*$", re.MULTILINE)
TODO_ECHO = re.compile(r"""^echo\s+(['"])TODO\b.*\1\s*$""")
HEADER_LINES = 6
SHELL_NOISE = re.compile(r"^(?:set\s+-[euxo\s\w]+|#.*|)$")


def tracked_files(root: Path) -> list[str]:
    completed = subprocess.run(["git", "ls-files", "-z", "--", *SURFACES], cwd=root,
                               capture_output=True, check=True)
    return sorted(p for p in completed.stdout.decode("utf-8").split("\0") if p)


def _is_constant_test(node: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    body = [stmt for stmt in node.body
            if not (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant))]
    if not body:
        return True
    return all(isinstance(stmt, ast.Pass)
               or (isinstance(stmt, ast.Assert) and isinstance(stmt.test, ast.Constant))
               for stmt in body)


_INTERFACE_BASES = frozenset({"Protocol", "ABC", "ABCMeta", "TypedDict", "NamedTuple"})


def _is_docstring(stmt: ast.stmt) -> bool:
    return isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant)


def _is_empty_statement(stmt: ast.stmt) -> bool:
    """``pass``, ``...``, a docstring, or ``raise NotImplementedError[(...)]``."""
    if isinstance(stmt, ast.Pass) or _is_docstring(stmt):
        return True
    if isinstance(stmt, ast.Raise) and stmt.exc is not None:
        target = stmt.exc.func if isinstance(stmt.exc, ast.Call) else stmt.exc
        return isinstance(target, ast.Name) and target.id == "NotImplementedError"
    return False


def _is_stub_definition(stmt: ast.stmt) -> bool:
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return all(_is_empty_statement(inner) for inner in stmt.body)
    if isinstance(stmt, ast.ClassDef):
        bases = {base.id if isinstance(base, ast.Name) else getattr(base, "attr", "")
                 for base in stmt.bases}
        if bases & _INTERFACE_BASES:
            return False  # Interface declarations legitimately use ``...`` bodies.
        return all(_is_empty_statement(inner) or _is_stub_definition(inner)
                   for inner in stmt.body)
    return _is_empty_statement(stmt)


def _is_main_guard(stmt: ast.stmt) -> bool:
    return (isinstance(stmt, ast.If) and isinstance(stmt.test, ast.Compare)
            and isinstance(stmt.test.left, ast.Name) and stmt.test.left.id == "__name__")


def _is_pass_only_module(body: list[ast.stmt]) -> bool:
    """True when every non-import, non-guard statement is an empty body or stub definition."""
    remaining = [stmt for stmt in body
                 if not isinstance(stmt, (ast.Import, ast.ImportFrom)) and not _is_main_guard(stmt)]
    return bool(remaining) and all(_is_stub_definition(stmt) for stmt in remaining)


def _python_kinds(path: str, text: str) -> list[str]:
    name = Path(path).name
    try:
        module = ast.parse(text, filename=path)
    except (SyntaxError, ValueError):
        return []
    body = [stmt for stmt in module.body
            if not (isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant))]
    if not body or _is_pass_only_module(body):
        return [] if name in {"__init__.py", "conftest.py"} else ["STUB_MODULE"]
    if name.startswith("test_") or name.endswith("_test.py"):
        tests = [node for node in ast.walk(module)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                 and node.name.startswith("test")]
        if tests and all(_is_constant_test(node) for node in tests):
            return ["VACUOUS_TEST"]
    return []


def _shell_is_todo_echo(text: str) -> bool:
    commands = [line.strip() for line in text.splitlines()]
    actions = [line for line in commands if not SHELL_NOISE.match(line)]
    return bool(actions) and all(TODO_ECHO.match(line) for line in actions)


def classify(path: str, data: bytes) -> list[str]:
    name, suffix = Path(path).name, Path(path).suffix.lower()
    if not data:
        return [] if name in EMPTY_ALLOWED else ["EMPTY_FILE"]
    if suffix not in TEXT_SUFFIXES:
        return []
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return []
    kinds: list[str] = []
    # Placeholders declare themselves in their header; guards that quote the
    # marker further down (workflow assertions, validators) are not scaffolding.
    if MARKER.search("\n".join(text.splitlines()[:HEADER_LINES])):
        kinds.append("PLACEHOLDER_MARKER")
    if suffix == ".py":
        kinds.extend(_python_kinds(path, text))
    if suffix == ".sh" and _shell_is_todo_echo(text):
        kinds.append("TODO_ECHO_SCRIPT")
    if name.startswith("descriptor.") and suffix in {".yaml", ".yml"} and TBD_FIELD.search(text):
        kinds.append("UNRESOLVED_DESCRIPTOR")
    return kinds


def inventory(root: Path = ROOT, paths: list[str] | None = None) -> list[dict[str, str]]:
    findings = []
    for path in tracked_files(root) if paths is None else sorted(paths):
        file_path = root / path
        if not file_path.is_file() or file_path.is_symlink():
            continue
        for kind in classify(path, file_path.read_bytes()):
            findings.append({"path": path, "kind": kind})
    return findings


def _surface(path: str) -> str:
    for surface in SURFACES:
        if path == surface or path.startswith(surface + "/"):
            return surface
    return "other"


def summarize(findings: list[dict[str, str]]) -> dict[str, object]:
    return {"schema_version": SCHEMA_VERSION, "total": len(findings),
            "files": len({f["path"] for f in findings}),
            "by_kind": dict(sorted(Counter(f["kind"] for f in findings).items())),
            "by_surface": dict(sorted(Counter(_surface(f["path"]) for f in findings).items())),
            "authority_boundary": "Review aid only; not readiness, release, or publication "
                                  "evidence."}


def load_baseline(path: Path = BASELINE) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION or not isinstance(
            payload.get("findings"), list):
        raise ValueError("scaffold baseline has an unexpected shape")
    return payload["findings"]


def compare(findings: list[dict[str, str]], baseline: list[dict[str, str]]) -> dict[str, list]:
    current = {(f["path"], f["kind"]) for f in findings}
    accepted = {(f["path"], f["kind"]) for f in baseline}
    return {"new": [{"path": p, "kind": k} for p, k in sorted(current - accepted)],
            "resolved": [{"path": p, "kind": k} for p, k in sorted(accepted - current)]}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="fail on findings added to or resolved from the baseline")
    mode.add_argument("--write-baseline", action="store_true",
                      help="rewrite tools/qa/scaffold_baseline.json from current findings")
    parser.add_argument("--list", action="store_true", help="include every finding in output")
    args = parser.parse_args(argv)
    findings = inventory()
    report: dict[str, object] = summarize(findings)
    if args.write_baseline:
        header = json.dumps({"schema_version": SCHEMA_VERSION,
                             "summary": {k: report[k] for k in
                                         ("total", "files", "by_kind", "by_surface")}},
                            indent=1, sort_keys=True)
        # One finding per line keeps baseline diffs reviewable as the ratchet tightens.
        rows = ",\n".join("  " + json.dumps(f, sort_keys=True) for f in findings)
        BASELINE.write_text(header[:-2] + ',\n "findings": [\n' + rows + "\n ]\n}\n",
                            encoding="utf-8")
        print(f"wrote {BASELINE.relative_to(ROOT)} with {len(findings)} findings")
        return 0
    status = 0
    if args.check:
        delta = compare(findings, load_baseline())
        report.update(delta)
        if delta["new"]:
            status = 1
            print("New scaffolding detected. Implement the file, make it fail closed with a "
                  "named HOLD, or remove it; do not add it to the baseline to pass.",
                  file=sys.stderr)
        if delta["resolved"]:
            status = 1
            print("Baseline entries were resolved. Run `python tools/qa/scaffold_inventory.py "
                  "--write-baseline` so the ratchet tightens.", file=sys.stderr)
    if args.list:
        report["findings"] = findings
    print(json.dumps(report, indent=2, sort_keys=True))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
