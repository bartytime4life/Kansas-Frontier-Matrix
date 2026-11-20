"""List the ``tests/`` modules that no CI workflow step executes.

Most workflows run explicit slices of the suite, and the full-suite job in
``python-dependency-lock.yml`` only collects tests. This tool reads every
workflow step's ``run:`` text (never ``on.paths`` filters), plus the recipes of
the Makefile targets those steps invoke, and resolves the test modules each
command executes:

* explicit file paths, ``path::node`` ids and globs under ``tests/``;
* ``pytest`` directory arguments under ``tests/``;
* ``unittest discover`` with ``-s``/``--start-directory`` and ``-p``/``--pattern``;
* dotted ``tests.x.y`` module or package names passed to ``unittest``;
* ``python tests/.../test_x.py`` direct execution.

``pytest --collect-only`` runs nothing and is ignored, as are shell comments. A
path that appears only as an argument to some other command (for example inside
an ``echo``) still counts as executed, so the result can under-report unexecuted
modules but does not invent one. The output is a review and
scheduling aid; it grants no readiness or release authority.

``--unexecuted`` prints one path per line for the ``unwired-python-tests``
workflow, which runs exactly that list.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import shlex
import sys
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import yaml

ROOT = Path(__file__).resolve().parents[2]
MAKE_INVOCATION = re.compile(r"\bmake\s+((?:-[\w-]+\s+)*)([\w.-]+(?:[ \t]+[\w.-]+)*)")
SUBMAKE = re.compile(r"\$\(MAKE\)\s+(?:-[\w-]+\s+)*([\w.-]+)")
MAKE_TARGET = re.compile(r"^([\w.-]+)\s*:(?!=)")
DOTTED_TESTS = re.compile(r"tests(?:\.\w+)+")


def test_modules(root: Path) -> list[str]:
    return sorted(p.relative_to(root).as_posix() for p in (root / "tests").rglob("test_*.py")
                  if "__pycache__" not in p.parts)


def workflow_run_steps(root: Path) -> list[tuple[str, str]]:
    steps = []
    for path in sorted((root / ".github" / "workflows").glob("*.y*ml")):
        try:
            document = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            continue
        jobs = document.get("jobs") if isinstance(document, Mapping) else None
        for job in (jobs or {}).values():
            for step in (job or {}).get("steps") or []:
                if isinstance(step, Mapping) and isinstance(step.get("run"), str):
                    steps.append((path.name, step["run"]))
    return steps


def makefile_recipes(text: str) -> dict[str, list[str]]:
    recipes: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        match = MAKE_TARGET.match(line)
        if match:
            current = match.group(1)
            recipes.setdefault(current, [])
        elif current and line.startswith("\t"):
            recipes[current].append(line[1:])
    return recipes


def invoked_make_recipes(runs: Iterable[str], recipes: Mapping[str, list[str]]) -> list[tuple[str, str]]:
    pending = []
    for text in runs:
        for match in MAKE_INVOCATION.finditer(text):
            pending.extend(match.group(2).split())
    seen: set[str] = set()
    found = []
    while pending:
        target = pending.pop()
        if target in seen or target not in recipes:
            continue
        seen.add(target)
        body = "\n".join(recipes[target])
        found.append((f"Makefile:{target}", body))
        pending.extend(SUBMAKE.findall(body))
    return found


def _tokens(line: str) -> list[str]:
    try:
        return shlex.split(line, comments=True)
    except ValueError:
        return line.split()


def executed_modules(commands: Iterable[str], modules: Sequence[str], root: Path) -> set[str]:
    module_set = set(modules)
    executed: set[str] = set()

    def mark_directory(directory: str, pattern: str = "test*.py") -> None:
        prefix = directory.rstrip("/") + "/"
        executed.update(m for m in modules
                        if m.startswith(prefix) and fnmatch.fnmatch(Path(m).name, pattern))

    for text in commands:
        for line in text.replace("\\\n", " ").splitlines():
            tokens = _tokens(line)
            if not tokens or "--collect-only" in tokens or "--co" in tokens:
                continue
            for token in tokens:
                path = token.split("::", 1)[0]
                if path in module_set:
                    executed.add(path)
                elif "*" in path and path.startswith("tests/"):
                    executed.update(m for m in modules if fnmatch.fnmatch(m, path))
            if any("pytest" in token for token in tokens):
                for token in tokens:
                    if token.startswith("tests") and (root / token).is_dir():
                        mark_directory(token)
            if any(token == "unittest" or token.endswith(".unittest") for token in tokens) \
                    or "unittest" in tokens:
                if "discover" in tokens:
                    start, pattern = ".", "test*.py"
                    for index, token in enumerate(tokens[:-1]):
                        if token in ("-s", "--start-directory"):
                            start = tokens[index + 1]
                        elif token in ("-p", "--pattern"):
                            pattern = tokens[index + 1]
                    if start in (".", "tests") or start.startswith("tests/"):
                        mark_directory("tests" if start == "." else start, pattern)
                for token in tokens:
                    if DOTTED_TESTS.fullmatch(token):
                        relative = token.replace(".", "/")
                        if f"{relative}.py" in module_set:
                            executed.add(f"{relative}.py")
                        elif (root / relative).is_dir():
                            mark_directory(relative)
    return executed


def inventory(root: Path = ROOT) -> dict[str, object]:
    modules = test_modules(root)
    steps = workflow_run_steps(root)
    makefile = root / "Makefile"
    recipes = makefile_recipes(makefile.read_text(encoding="utf-8")) if makefile.is_file() else {}
    commands = [text for _, text in steps]
    commands += [text for _, text in invoked_make_recipes(commands, recipes)]
    executed = executed_modules(commands, modules, root)
    unexecuted = [m for m in modules if m not in executed]
    return {"test_modules": len(modules), "executed": len(executed),
            "unexecuted": unexecuted, "authority": "SCHEDULING_AID_ONLY"}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--unexecuted", action="store_true",
                        help="print one unexecuted test module path per line")
    args = parser.parse_args(argv)
    result = inventory(ROOT)
    if args.unexecuted:
        sys.stdout.write("".join(f"{path}\n" for path in result["unexecuted"]))
    else:
        summary = {k: v for k, v in result.items() if k != "unexecuted"}
        summary["unexecuted"] = len(result["unexecuted"])
        print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
