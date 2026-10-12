"""Bounded static checks for connector-owned output paths.

The scanner is intentionally conservative for recognized sinks and intentionally
does not claim runtime confinement. It never executes connector code or shell
commands and uses only the Python standard library.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
import os
from pathlib import Path
import posixpath
import re
import shlex
import textwrap
from urllib.parse import unquote, urlparse


CONNECTOR_ROOT = Path("connectors")
LEGACY_ROOTS = (CONNECTOR_ROOT, Path("pipelines"))
SOURCE_GLOBS = ("*.py", "*.sh", "*.yaml", "*.yml")
EXCLUDED_SOURCE_PARTS = {
    "test",
    "tests",
    "fixture",
    "fixtures",
    "example",
    "examples",
}

# DIR-PLACE-003 is an allowlist for connector-owned repository outputs. Receipt
# correspondence, symlink safety, and runtime effects require separate checks.
CONNECTOR_ALLOWED_ROOTS = (
    "data/raw",
    "data/quarantine",
    "data/receipts",
)

# Preserve the earlier connector/pipeline publication-target canary. Pipeline
# stages have actor-specific output lanes, so the connector allowlist must not be
# applied to the entire pipelines/ root.
LEGACY_FORBIDDEN_TARGETS = ("data/catalog", "data/published", "release/")
PY_WRITE_CALL_PATTERN = re.compile(
    r"\b(write_text|write_bytes|open\s*\(|to_csv\s*\(|to_parquet\s*\(|dump\s*\()"
)
SHELL_WRITE_PATTERN = re.compile(r"\b(cp|mv|rsync|cat\s+.*>|tee)\b")

PATH_CONSTRUCTORS = {
    "pathlib.Path",
    "pathlib.PurePath",
    "pathlib.PurePosixPath",
}
PATH_RECEIVER_SINKS = {"mkdir", "touch", "write_bytes", "write_text"}
PATH_DESTINATION_SINKS = {"rename", "replace"}
EXPORT_SINKS = {
    "to_csv",
    "to_excel",
    "to_feather",
    "to_json",
    "to_parquet",
    "to_pickle",
}
COPY_MOVE_SINKS = {
    "os.rename",
    "os.replace",
    "shutil.copy",
    "shutil.copy2",
    "shutil.copyfile",
    "shutil.copytree",
    "shutil.move",
}
DIRECT_PATH_SINKS = {"os.makedirs", "os.mkdir"}
SUBPROCESS_SINKS = {
    "os.system",
    "subprocess.call",
    "subprocess.check_call",
    "subprocess.check_output",
    "subprocess.Popen",
    "subprocess.run",
}
RECOGNIZED_ALIAS_TARGETS = (
    PATH_CONSTRUCTORS
    | COPY_MOVE_SINKS
    | DIRECT_PATH_SINKS
    | SUBPROCESS_SINKS
    | {"builtins.open", "io.open", "os.path.join", "posixpath.join"}
)
RECOGNIZED_ALIAS_ROOTS = {
    "builtins",
    "io",
    "os",
    "pathlib",
    "posixpath",
    "shutil",
    "subprocess",
}
LOCAL_ALIAS_PREFIX = "<local>:"
AMBIGUOUS_SINK_ALIAS = "<ambiguous-sink>"
YAML_COMMAND_KEYS = {"command", "run", "script", "shell"}
YAML_OUTPUT_KEYS = {"destination", "output_path", "sink"}
TEMPLATE_MARKERS = ("${", "$(", "`", "{{", "{%")
SHELL_ASSIGNMENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=.*$", re.DOTALL)
SHELL_VARIABLE = re.compile(r"\$(?:[A-Za-z_][A-Za-z0-9_]*|[0-9?@*#!-])")


@dataclass(frozen=True, order=True)
class Violation:
    source: str
    line: int
    sink: str
    target: str
    reason: str

    def render(self) -> str:
        return (
            f"{self.source}:{self.line}: {self.sink} -> {self.target}: "
            f"{self.reason}"
        )


@dataclass(frozen=True)
class _ResolvedPath:
    value: str | None
    path_object: bool = False


@dataclass(frozen=True)
class _ScopeInfo:
    locals: frozenset[str]
    aliases: dict[str, str]


def _iter_source_files(root: Path):
    for pattern in SOURCE_GLOBS:
        yield from root.rglob(pattern)


def _is_selected_connector_source(path: Path, source_root: Path) -> bool:
    try:
        relative = path.relative_to(source_root)
    except ValueError:
        return False
    return not any(part.lower() in EXCLUDED_SOURCE_PARTS for part in relative.parts)


def iter_connector_source_files(repository_root: Path) -> tuple[Path, ...]:
    """Return connector sources after deterministic path-component exclusions."""

    connector_root = repository_root / CONNECTOR_ROOT
    if not connector_root.is_dir():
        return ()
    return tuple(
        sorted(
            {
                path
                for path in _iter_source_files(connector_root)
                if _is_selected_connector_source(path, connector_root)
            }
        )
    )


def _static_string(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
                return None
            parts.append(value.value)
        return "".join(parts)
    return None


class _BindingCollector(ast.NodeVisitor):
    """Collect bindings for one lexical scope without descending into children."""

    def __init__(self) -> None:
        self.locals: set[str] = set()
        self.aliases: dict[str, str] = {}

    def visit_Import(self, node: ast.Import) -> None:
        for item in node.names:
            local = item.asname or item.name.split(".", 1)[0]
            qualified = item.name if item.asname else item.name.split(".", 1)[0]
            self.locals.add(local)
            self.aliases[local] = qualified

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module is None:
            return
        for item in node.names:
            if item.name == "*":
                continue
            local = item.asname or item.name
            self.locals.add(local)
            self.aliases[local] = f"{node.module}.{item.name}"

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, (ast.Store, ast.Del)):
            self.locals.add(node.id)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.locals.add(node.name)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.locals.add(node.name)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.locals.add(node.name)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        return

    def visit_ListComp(self, node: ast.ListComp) -> None:
        return

    def visit_SetComp(self, node: ast.SetComp) -> None:
        return

    def visit_DictComp(self, node: ast.DictComp) -> None:
        return

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        return


def _scope_info(node: ast.AST) -> _ScopeInfo:
    collector = _BindingCollector()
    if isinstance(node, ast.Module):
        statements = node.body
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        arguments = (
            list(node.args.posonlyargs)
            + list(node.args.args)
            + list(node.args.kwonlyargs)
        )
        if node.args.vararg:
            arguments.append(node.args.vararg)
        if node.args.kwarg:
            arguments.append(node.args.kwarg)
        collector.locals.update(argument.arg for argument in arguments)
        statements = node.body
    elif isinstance(node, ast.ClassDef):
        statements = node.body
    elif isinstance(node, ast.Lambda):
        arguments = (
            list(node.args.posonlyargs)
            + list(node.args.args)
            + list(node.args.kwonlyargs)
        )
        if node.args.vararg:
            arguments.append(node.args.vararg)
        if node.args.kwarg:
            arguments.append(node.args.kwarg)
        collector.locals.update(argument.arg for argument in arguments)
        statements = []
    else:
        statements = []
    for statement in statements:
        collector.visit(statement)
    return _ScopeInfo(frozenset(collector.locals), collector.aliases)


def _is_recognized_alias(value: str) -> bool:
    return value in RECOGNIZED_ALIAS_TARGETS or value in RECOGNIZED_ALIAS_ROOTS


class _ModuleAliasPossibilityCollector(ast.NodeVisitor):
    """Collect possible module-level sink aliases without entering child scopes."""

    def __init__(self) -> None:
        self.possibilities: dict[str, set[str]] = {}
        self.path_possibilities: dict[str, set[_ResolvedPath | None]] = {}

    def _expression_aliases(self, node: ast.AST | None) -> set[str]:
        if isinstance(node, ast.Name):
            return set(
                self.possibilities.get(
                    node.id,
                    {"builtins.open" if node.id == "open" else node.id},
                )
            )
        if isinstance(node, ast.Attribute):
            return {
                f"{parent}.{node.attr}"
                for parent in self._expression_aliases(node.value)
            }
        if isinstance(node, ast.NamedExpr):
            return self._expression_aliases(node.value)
        if isinstance(node, ast.IfExp):
            return self._expression_aliases(node.body) | self._expression_aliases(
                node.orelse
            )
        if isinstance(node, ast.BoolOp):
            return set().union(*(self._expression_aliases(value) for value in node.values))
        return set()

    def _expression_paths(self, node: ast.AST | None) -> set[_ResolvedPath]:
        literal = _static_string(node)
        if literal is not None:
            return {_ResolvedPath(literal)}
        if isinstance(node, ast.Name):
            return {
                path
                for path in self.path_possibilities.get(node.id, set())
                if path is not None
            }
        if isinstance(node, ast.NamedExpr):
            return self._expression_paths(node.value)
        if isinstance(node, ast.IfExp):
            return self._expression_paths(node.body) | self._expression_paths(
                node.orelse
            )
        if isinstance(node, ast.BoolOp):
            return set().union(*(self._expression_paths(value) for value in node.values))
        if isinstance(node, ast.Call):
            aliases = self._expression_aliases(node.func)
            if aliases & PATH_CONSTRUCTORS and len(node.args) == 1:
                inner = self._expression_paths(node.args[0])
                return {
                    _ResolvedPath(path.value, path_object=True) for path in inner
                } or {_ResolvedPath(None, path_object=True)}
            if aliases & {"os.path.join", "posixpath.join"} and node.args:
                parts = [self._expression_paths(argument) for argument in node.args]
                if all(len(part) == 1 for part in parts):
                    selected = [next(iter(part)) for part in parts]
                    if all(path.value is not None for path in selected):
                        return {
                            _ResolvedPath(
                                posixpath.join(
                                    *(
                                        path.value
                                        for path in selected
                                        if path.value is not None
                                    )
                                ),
                                path_object=any(path.path_object for path in selected),
                            )
                        }
            return set()
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            left = self._expression_paths(node.left)
            right = self._expression_paths(node.right)
            paths: set[_ResolvedPath] = set()
            for left_path in left:
                if not left_path.path_object:
                    continue
                for right_path in right:
                    if left_path.value is not None and right_path.value is not None:
                        paths.add(
                            _ResolvedPath(
                                posixpath.join(left_path.value, right_path.value),
                                path_object=True,
                            )
                        )
                    else:
                        paths.add(_ResolvedPath(None, path_object=True))
            return paths
        return set()

    def _target_names(self, target: ast.AST) -> set[str]:
        if isinstance(target, ast.Name):
            return {target.id}
        if isinstance(target, (ast.Tuple, ast.List)):
            return set().union(*(self._target_names(item) for item in target.elts))
        return set()

    def _record(
        self,
        target: ast.AST,
        aliases: set[str],
        paths: set[_ResolvedPath] | None = None,
    ) -> None:
        for name in self._target_names(target):
            recognized = {alias for alias in aliases if _is_recognized_alias(alias)}
            self.possibilities.setdefault(name, set()).update(
                recognized or {f"{LOCAL_ALIAS_PREFIX}{name}"}
            )
            self.path_possibilities.setdefault(name, set()).update(paths or {None})

    def visit_Import(self, node: ast.Import) -> None:
        for item in node.names:
            local = item.asname or item.name.split(".", 1)[0]
            qualified = item.name if item.asname else item.name.split(".", 1)[0]
            self._record(ast.Name(id=local), {qualified})

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for item in node.names:
            if item.name == "*":
                continue
            local = item.asname or item.name
            qualified = f"{node.module}.{item.name}" if node.module else item.name
            self._record(ast.Name(id=local), {qualified})

    def visit_Assign(self, node: ast.Assign) -> None:
        for target in node.targets:
            self._record_assignment(target, node.value)
        self.visit(node.value)

    def _record_assignment(self, target: ast.AST, value: ast.AST) -> None:
        if (
            isinstance(target, (ast.Tuple, ast.List))
            and isinstance(value, (ast.Tuple, ast.List))
            and len(target.elts) == len(value.elts)
        ):
            for target_item, value_item in zip(target.elts, value.elts):
                self._record_assignment(target_item, value_item)
            return
        self._record(
            target,
            self._expression_aliases(value),
            self._expression_paths(value),
        )

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self._record(
            node.target,
            self._expression_aliases(node.value),
            self._expression_paths(node.value),
        )
        if node.value is not None:
            self.visit(node.value)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self._record(
            node.target,
            self._expression_aliases(node.value),
            self._expression_paths(node.value),
        )
        self.visit(node.value)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self._record(node.target, set())
        self.visit(node.value)

    def visit_Delete(self, node: ast.Delete) -> None:
        for target in node.targets:
            self._record(target, set())

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._record(ast.Name(id=node.name), set())

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._record(ast.Name(id=node.name), set())

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._record(ast.Name(id=node.name), set())

    def visit_Lambda(self, node: ast.Lambda) -> None:
        return

    def visit_ListComp(self, node: ast.ListComp) -> None:
        return

    def visit_SetComp(self, node: ast.SetComp) -> None:
        return

    def visit_DictComp(self, node: ast.DictComp) -> None:
        return

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        return


def _module_possibilities(
    tree: ast.Module,
) -> tuple[
    dict[str, frozenset[str]],
    dict[str, frozenset[_ResolvedPath | None]],
]:
    collector = _ModuleAliasPossibilityCollector()
    binding_count = sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.NamedExpr, ast.Import, ast.ImportFrom))
    )
    for _ in range(max(2, binding_count + 2)):
        before_aliases = {
            name: frozenset(values) for name, values in collector.possibilities.items()
        }
        before_paths = {
            name: frozenset(values)
            for name, values in collector.path_possibilities.items()
        }
        collector.visit(tree)
        after_aliases = {
            name: frozenset(values) for name, values in collector.possibilities.items()
        }
        after_paths = {
            name: frozenset(values)
            for name, values in collector.path_possibilities.items()
        }
        if after_aliases == before_aliases and after_paths == before_paths:
            return after_aliases, after_paths
    # Path expressions such as ``target = target / "child"`` can grow without
    # reaching a finite literal set. Preserve the sink/path identity but degrade
    # the value so deferred lookups fail closed instead of hanging the scanner.
    for name, possibilities in collector.possibilities.items():
        if any(_is_recognized_alias(value) for value in possibilities):
            possibilities.add(AMBIGUOUS_SINK_ALIAS)
    for possibilities in collector.path_possibilities.values():
        resolved = [possibility for possibility in possibilities if possibility]
        if resolved:
            possibilities.add(
                _ResolvedPath(
                    None,
                    path_object=any(possibility.path_object for possibility in resolved),
                )
            )
    return (
        {
            name: frozenset(values)
            for name, values in collector.possibilities.items()
        },
        {
            name: frozenset(values)
            for name, values in collector.path_possibilities.items()
        },
    )


def _keyword(call: ast.Call, *names: str) -> ast.AST | None:
    for item in call.keywords:
        if item.arg in names:
            return item.value
    return None


def _has_template(value: str) -> bool:
    return any(marker in value for marker in TEMPLATE_MARKERS) or bool(
        SHELL_VARIABLE.search(value)
    )


def _target_violation(
    source: str,
    line: int,
    sink: str,
    target: _ResolvedPath | None,
    *,
    repository_root: Path,
    local_path_semantics: bool = False,
) -> Violation | None:
    value = target.value if target else None
    if value is None or _has_template(value):
        return Violation(
            source,
            line,
            sink,
            "<unresolved>",
            "DIR-PLACE-003 requires a statically resolvable connector output target",
        )

    candidate = value.strip().replace("\\", "/")
    if not candidate:
        return Violation(
            source,
            line,
            sink,
            "<empty>",
            "DIR-PLACE-003 does not permit an empty connector output target",
        )

    parsed = urlparse(candidate)
    if parsed.scheme == "file":
        if parsed.netloc not in {"", "localhost"}:
            return Violation(
                source,
                line,
                sink,
                candidate,
                "DIR-PLACE-003 cannot classify a non-local file URI",
            )
        candidate = unquote(parsed.path)
    elif parsed.scheme and "://" in candidate:
        if not local_path_semantics:
            return None
        # pathlib/open treat URI-looking strings as local path text. Preserve
        # that behavior rather than silently exempting the target as remote.
        candidate = candidate.replace("://", ":/", 1)

    if candidate == "~" or candidate.startswith("~/"):
        candidate = os.path.expanduser(candidate).replace("\\", "/")

    parts = tuple(part for part in candidate.split("/") if part not in {"", "."})
    if ".." in parts:
        return Violation(
            source,
            line,
            sink,
            candidate,
            "DIR-PLACE-003 cannot prove a traversal-bearing target safe",
        )

    repository = repository_root.resolve()
    windows_absolute = bool(re.match(r"^[A-Za-z]:/", candidate))
    if candidate.startswith("/"):
        absolute = Path(candidate).resolve(strict=False)
        try:
            candidate = absolute.relative_to(repository).as_posix()
        except ValueError:
            return None
    elif windows_absolute:
        return None

    normalized = posixpath.normpath(candidate)
    if normalized in {"", ".", ".."} or normalized.startswith("../"):
        return Violation(
            source,
            line,
            sink,
            normalized,
            "DIR-PLACE-003 cannot prove the repository-relative target safe",
        )
    if any(
        normalized == allowed or normalized.startswith(allowed + "/")
        for allowed in CONNECTOR_ALLOWED_ROOTS
    ):
        return None
    return Violation(
        source,
        line,
        sink,
        normalized,
        "DIR-PLACE-003 allows connector repository outputs only under "
        "data/raw, data/quarantine, or data/receipts",
    )


def _shell_tokens(command: str) -> list[str]:
    lexer = shlex.shlex(command, posix=True, punctuation_chars="|&;<>()")
    lexer.whitespace_split = True
    lexer.commenters = "#"
    return list(lexer)


def _command_tokens(node: ast.AST | None) -> list[str | None] | None:
    literal = _static_string(node)
    if literal is not None:
        return _shell_tokens(literal)
    if isinstance(node, (ast.List, ast.Tuple)):
        return [_static_string(item) for item in node.elts]
    return None


def _unwrap_shell_command(segment: list[str | None]) -> int | None:
    index = 0
    while index < len(segment) and segment[index] is not None:
        token = segment[index] or ""
        if token.isdigit() or token in {">", ">>", ">|", "&>", "&>>"}:
            index += 1
            continue
        if SHELL_ASSIGNMENT.match(token):
            index += 1
            continue
        break
    if index >= len(segment):
        return None
    if segment[index] is None:
        return index

    while index < len(segment):
        token = segment[index]
        if token is None:
            return index
        command = posixpath.basename(token)
        if command == "env":
            env_index = index
            index += 1
            while index < len(segment):
                token = segment[index]
                if token is None:
                    return index
                if token == "--":
                    index += 1
                    break
                if token in {"-S", "--split-string"} or token.startswith(
                    ("-S", "--split-string=")
                ):
                    # env --split-string contains another command line in one
                    # argument. Let the caller parse that payload recursively.
                    return env_index
                if token in {"-u", "--unset"}:
                    index += 2
                    continue
                if token in {"-C", "--chdir"}:
                    index += 2
                    continue
                if token.startswith("--chdir="):
                    index += 1
                    continue
                if token.startswith("--unset=") or token in {
                    "-i",
                    "--ignore-environment",
                }:
                    index += 1
                    continue
                if token.startswith("-") or SHELL_ASSIGNMENT.match(token):
                    index += 1
                    continue
                break
            continue
        if command in {"command", "exec", "nohup"}:
            index += 1
            while index < len(segment):
                token = segment[index]
                if token is None:
                    return index
                if command == "command" and token in {"-v", "-V"}:
                    return None
                if command == "nohup" and token in {"--help", "--version"}:
                    return None
                if command == "exec" and token == "-a":
                    index += 2
                    continue
                if token == "--":
                    index += 1
                    break
                if token.startswith("-"):
                    index += 1
                    continue
                break
            continue
        if command == "timeout":
            index += 1
            while index < len(segment):
                token = segment[index]
                if token is None:
                    return index
                if token == "--":
                    index += 1
                    break
                if token in {"-k", "--kill-after", "-s", "--signal"}:
                    index += 2
                    continue
                if token.startswith(("--kill-after=", "--signal=")):
                    index += 1
                    continue
                if token.startswith("-"):
                    index += 1
                    continue
                break
            if index >= len(segment):
                return None
            if segment[index] is None:
                return index
            index += 1  # duration
            continue
        if command == "nice":
            index += 1
            while index < len(segment):
                token = segment[index]
                if token is None:
                    return index
                if token in {"--help", "--version"}:
                    return None
                if token == "--":
                    index += 1
                    break
                if token in {"-n", "--adjustment"}:
                    index += 2
                    continue
                if (
                    token.startswith("--adjustment=")
                    or re.fullmatch(r"-n[+-]?\d+", token)
                    or re.fullmatch(r"-[0-9]+", token)
                ):
                    index += 1
                    continue
                break
            continue
        break
    return index if index < len(segment) else None


def _shell_operands(arguments: list[str | None]) -> list[str | None]:
    operands: list[str | None] = []
    after_options = False
    for argument in arguments:
        if argument == "--" and not after_options:
            after_options = True
            continue
        if not after_options and argument is not None and argument.startswith("-"):
            continue
        operands.append(argument)
    return operands


def _operands_with_value_options(
    arguments: list[str | None],
    value_options: set[str],
) -> list[str | None]:
    operands: list[str | None] = []
    after_options = False
    index = 0
    while index < len(arguments):
        argument = arguments[index]
        if argument == "--" and not after_options:
            after_options = True
            index += 1
            continue
        if not after_options and argument in value_options:
            index += 2
            continue
        if not after_options and argument is not None and argument.startswith("-"):
            index += 1
            continue
        operands.append(argument)
        index += 1
    return operands


def _target_directory_options(arguments: list[str | None]) -> list[str | None]:
    targets: list[str | None] = []
    for index, argument in enumerate(arguments):
        if argument in {"-t", "--target-directory"} and index + 1 < len(arguments):
            targets.append(arguments[index + 1])
        elif argument and argument.startswith("-t") and len(argument) > 2:
            targets.append(argument[2:])
        elif argument and argument.startswith("--target-directory="):
            targets.append(argument.split("=", 1)[1])
    return targets


def _install_operands(arguments: list[str | None]) -> list[str | None]:
    """Return install operands while omitting common option arguments."""

    value_options = {
        "-B",
        "-f",
        "-g",
        "-M",
        "-m",
        "-N",
        "-o",
        "-S",
        "--group",
        "--mode",
        "--owner",
        "--strip-program",
        "--suffix",
        "--target-directory",
    }
    operands: list[str | None] = []
    after_options = False
    index = 0
    while index < len(arguments):
        argument = arguments[index]
        if argument == "--" and not after_options:
            after_options = True
            index += 1
            continue
        if not after_options and argument in value_options:
            index += 2
            continue
        if not after_options and argument is not None and argument.startswith("-"):
            index += 1
            continue
        operands.append(argument)
        index += 1
    return operands


def _scan_shell_tokens(
    tokens: list[str | None],
    *,
    source: str,
    line: int,
    repository_root: Path,
) -> list[Violation]:
    violations: list[Violation] = []
    separators = {"|", "||", "&&", ";", "&"}
    segments: list[list[str | None]] = []
    current: list[str | None] = []
    for token in tokens:
        if token in separators:
            if current:
                segments.append(current)
                current = []
        else:
            current.append(token)
    if current:
        segments.append(current)

    for segment in segments:
        while segment and segment[0] == "(":
            segment = segment[1:]
        while segment and segment[-1] == ")":
            segment = segment[:-1]
        if not segment:
            continue
        for index, token in enumerate(segment[:-1]):
            if token in {">", ">>", ">|", "&>", "&>>"}:
                destination = segment[index + 1]
                if destination is not None and destination.startswith("&"):
                    continue
                violation = _target_violation(
                    source,
                    line,
                    "shell-redirection",
                    _ResolvedPath(destination) if destination is not None else None,
                    repository_root=repository_root,
                )
                if violation:
                    violations.append(violation)

        command_index = _unwrap_shell_command(segment)
        if command_index is None:
            continue
        command_token = segment[command_index]
        if command_token is None or _has_template(command_token):
            violations.append(
                Violation(
                    source,
                    line,
                    "shell-command",
                    "<unresolved>",
                    "DIR-PLACE-003 cannot classify a dynamic shell command",
                )
            )
            continue

        command = posixpath.basename(command_token)
        arguments = segment[command_index + 1 :]
        if command == "env":
            payload: str | None = None
            remainder: list[str | None] = []
            for index, argument in enumerate(arguments):
                if argument in {"-S", "--split-string"}:
                    if index + 1 < len(arguments):
                        payload = arguments[index + 1]
                        remainder = arguments[index + 2 :]
                    break
                if argument and argument.startswith("--split-string="):
                    payload = argument.split("=", 1)[1]
                    remainder = arguments[index + 1 :]
                    break
                if argument and argument.startswith("-S") and len(argument) > 2:
                    payload = argument[2:]
                    remainder = arguments[index + 1 :]
                    break
            if payload is None or _has_template(payload):
                violations.append(
                    Violation(
                        source,
                        line,
                        "shell-env-split-string",
                        "<unresolved-command>",
                        "DIR-PLACE-003 cannot classify a dynamic env split-string command",
                    )
                )
                continue
            try:
                nested_tokens = _shell_tokens(payload)
            except ValueError:
                nested_tokens = []
                violations.append(
                    Violation(
                        source,
                        line,
                        "shell-env-split-string",
                        "<unresolved-command>",
                        "DIR-PLACE-003 requires deterministic env split-string parsing",
                    )
                )
            expanded = [*nested_tokens, *remainder]
            if expanded:
                violations.extend(
                    _scan_shell_tokens(
                        ["env", *expanded],
                        source=source,
                        line=line,
                        repository_root=repository_root,
                    )
                )
            continue
        if command in {"bash", "dash", "ksh", "sh", "zsh"}:
            payload_index: int | None = None
            for index, argument in enumerate(arguments):
                if argument == "-c" or (
                    argument is not None
                    and re.match(r"^-[^-]*c", argument) is not None
                ):
                    payload_index = index + 1
                    break
            if payload_index is not None:
                payload = (
                    arguments[payload_index]
                    if payload_index < len(arguments)
                    else None
                )
                if payload is None or _has_template(payload):
                    violations.append(
                        Violation(
                            source,
                            line,
                            f"shell-{command}-c",
                            "<unresolved>",
                            "DIR-PLACE-003 cannot classify a dynamic nested shell command",
                        )
                    )
                else:
                    try:
                        nested_tokens = _shell_tokens(payload)
                    except ValueError:
                        nested_tokens = []
                        violations.append(
                            Violation(
                                source,
                                line,
                                f"shell-{command}-c",
                                "<unresolved>",
                                "DIR-PLACE-003 requires deterministic nested shell parsing",
                            )
                        )
                    if nested_tokens:
                        violations.extend(
                            _scan_shell_tokens(
                                nested_tokens,
                                source=source,
                                line=line,
                                repository_root=repository_root,
                            )
                        )
            continue
        destinations: list[str | None] = []
        if command == "tee":
            destinations = _shell_operands(arguments)
        elif command in {"cp", "mv"}:
            destinations = _target_directory_options(arguments)
            if not destinations:
                operands = _shell_operands(arguments)
                if operands:
                    destinations = [operands[-1]]
        elif command == "rsync":
            operands = _shell_operands(arguments)
            if operands:
                destinations = [operands[-1]]
        elif command == "install":
            destinations = _target_directory_options(arguments)
            if not destinations:
                directory_mode = any(
                    argument == "--directory"
                    or bool(
                        argument
                        and re.fullmatch(r"-[bcCdDpstvTUZ]*d[bcCdDpstvTUZ]*", argument)
                    )
                    for argument in arguments
                )
                operands = (
                    _install_operands(arguments)
                    if directory_mode
                    else _shell_operands(arguments)
                )
                if operands:
                    destinations = operands if directory_mode else [operands[-1]]
        elif command in {"curl", "wget"}:
            for index, argument in enumerate(arguments):
                if argument in {"-o", "--output"} and index + 1 < len(arguments):
                    destinations.append(arguments[index + 1])
                elif argument and argument.startswith("--output="):
                    destinations.append(argument.split("=", 1)[1])
                elif command == "wget" and argument and argument.startswith(
                    "--output-document="
                ):
                    destinations.append(argument.split("=", 1)[1])
                elif command == "wget" and argument == "--output-document" and index + 1 < len(arguments):
                    destinations.append(arguments[index + 1])
                elif command == "curl" and argument in {"-O", "--remote-name", "--remote-name-all"}:
                    destinations.append(None)
                elif command == "curl" and argument and argument.startswith("-") and not argument.startswith("--") and "O" in argument[1:]:
                    destinations.append(None)
                elif command == "curl" and argument and argument.startswith("-") and not argument.startswith("--") and "o" in argument[1:]:
                    output_index = argument.find("o", 1)
                    destinations.append(
                        argument[output_index + 1 :]
                        or (arguments[index + 1] if index + 1 < len(arguments) else None)
                    )
                elif command == "wget" and argument == "-O" and index + 1 < len(arguments):
                    destinations.append(arguments[index + 1])
                elif command == "wget" and argument and argument.startswith("-") and not argument.startswith("--") and "O" in argument[1:]:
                    output_index = argument.find("O", 1)
                    destinations.append(
                        argument[output_index + 1 :]
                        or (arguments[index + 1] if index + 1 < len(arguments) else None)
                    )
        elif command == "mkdir":
            destinations = _operands_with_value_options(
                arguments,
                {"-m", "--mode"},
            )
        elif command == "truncate":
            destinations = _operands_with_value_options(
                arguments,
                {"-o", "-r", "-s", "--reference", "--size"},
            )
        elif command == "touch":
            destinations = _shell_operands(arguments)
        elif command == "dd":
            destinations = [
                argument.split("=", 1)[1]
                for argument in arguments
                if argument is not None and argument.startswith("of=")
            ]

        for destination in destinations:
            violation = _target_violation(
                source,
                line,
                f"shell-{command}",
                _ResolvedPath(destination) if destination is not None else None,
                repository_root=repository_root,
            )
            if violation:
                violations.append(violation)
    return violations


def scan_shell_source(
    text: str,
    *,
    source: str,
    repository_root: Path,
    first_line: int = 1,
) -> list[Violation]:
    """Inspect selected shell destinations without executing the source."""

    violations: list[Violation] = []
    for offset, command in enumerate(text.splitlines()):
        if not command.strip():
            continue
        try:
            tokens = _shell_tokens(command)
        except ValueError:
            violations.append(
                Violation(
                    source,
                    first_line + offset,
                    "shell-parse",
                    "<unresolved>",
                    "DIR-PLACE-003 requires deterministic shell target parsing",
                )
            )
            continue
        violations.extend(
            _scan_shell_tokens(
                tokens,
                source=source,
                line=first_line + offset,
                repository_root=repository_root,
            )
        )
    return sorted(set(violations))


class _PythonScanner(ast.NodeVisitor):
    def __init__(self, *, source: str, repository_root: Path, tree: ast.Module) -> None:
        self.source = source
        self.repository_root = repository_root
        (
            self.module_alias_possibilities,
            self.module_path_possibilities,
        ) = _module_possibilities(tree)
        self.scope_stack: list[_ScopeInfo] = []
        self.binding_stack: list[dict[str, _ResolvedPath | None]] = []
        self.alias_stack: list[dict[str, str]] = []
        self.scope_kind_stack: list[str] = []
        self.violations: list[Violation] = []

    def _push_scope(self, node: ast.AST) -> None:
        if isinstance(node, ast.Module):
            kind = "module"
        elif isinstance(node, ast.ClassDef):
            kind = "class"
        elif isinstance(node, ast.Lambda):
            kind = "lambda"
        else:
            kind = "function"
        self._push_custom_scope(_scope_info(node), kind)

    def _push_custom_scope(self, scope: _ScopeInfo, kind: str) -> None:
        self.scope_stack.append(scope)
        self.binding_stack.append({})
        self.alias_stack.append({})
        self.scope_kind_stack.append(kind)

    def _pop_scope(self) -> None:
        self.scope_kind_stack.pop()
        self.alias_stack.pop()
        self.binding_stack.pop()
        self.scope_stack.pop()

    def _qualified_name(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.NamedExpr):
            return self._qualified_name(node.value)
        if isinstance(node, ast.IfExp):
            return self._alias_value(node)
        if isinstance(node, ast.Name):
            deferred_lookup = any(
                kind in {"function", "lambda"}
                for kind in self.scope_kind_stack[1:]
            )
            for index in reversed(range(len(self.scope_stack))):
                if index == 0 and deferred_lookup:
                    possibilities = self.module_alias_possibilities.get(node.id)
                    if possibilities:
                        recognized = {
                            value
                            for value in possibilities
                            if _is_recognized_alias(value)
                        }
                        if recognized:
                            if len(possibilities) == 1:
                                return next(iter(recognized))
                            return AMBIGUOUS_SINK_ALIAS
                if node.id in self.alias_stack[index]:
                    return self.alias_stack[index][node.id]
                kind = self.scope_kind_stack[index]
                if kind in {"function", "lambda", "comprehension"}:
                    if node.id in self.scope_stack[index].locals:
                        return node.id
                elif node.id in self.binding_stack[index]:
                    return node.id
            return "builtins.open" if node.id == "open" else node.id
        if isinstance(node, ast.Attribute):
            parent = self._qualified_name(node.value)
            if parent == AMBIGUOUS_SINK_ALIAS:
                return AMBIGUOUS_SINK_ALIAS
            return f"{parent}.{node.attr}" if parent else None
        return None

    def _alias_value(self, node: ast.AST | None) -> str | None:
        if isinstance(node, (ast.Name, ast.Attribute)):
            return self._qualified_name(node)
        if isinstance(node, ast.NamedExpr):
            return self._alias_value(node.value)
        if isinstance(node, ast.IfExp):
            alternatives = [
                self._alias_value(node.body),
                self._alias_value(node.orelse),
            ]
            if alternatives[0] == alternatives[1]:
                return alternatives[0]
            if any(
                alternative == AMBIGUOUS_SINK_ALIAS
                or bool(alternative and _is_recognized_alias(alternative))
                for alternative in alternatives
            ):
                return AMBIGUOUS_SINK_ALIAS
        if isinstance(node, ast.BoolOp):
            alternatives = [self._alias_value(value) for value in node.values]
            if alternatives and all(
                alternative == alternatives[0] for alternative in alternatives
            ):
                return alternatives[0]
            if any(
                alternative == AMBIGUOUS_SINK_ALIAS
                or bool(alternative and _is_recognized_alias(alternative))
                for alternative in alternatives
            ):
                return AMBIGUOUS_SINK_ALIAS
        return None

    def _binding(self, name: str) -> _ResolvedPath | None:
        deferred_lookup = any(
            kind in {"function", "lambda"} for kind in self.scope_kind_stack[1:]
        )
        for index in reversed(range(len(self.scope_stack))):
            if index == 0 and deferred_lookup:
                possibilities = self.module_path_possibilities.get(name)
                if possibilities:
                    resolved = [
                        possibility
                        for possibility in possibilities
                        if possibility is not None
                    ]
                    if resolved:
                        if None in possibilities:
                            return _ResolvedPath(
                                None,
                                path_object=any(
                                    possibility.path_object
                                    for possibility in resolved
                                ),
                            )
                        if all(possibility == resolved[0] for possibility in resolved):
                            return resolved[0]
                        if all(
                            possibility.value is not None
                            and _target_violation(
                                self.source,
                                1,
                                "deferred-path",
                                possibility,
                                repository_root=self.repository_root,
                                local_path_semantics=True,
                            )
                            is None
                            for possibility in resolved
                        ):
                            return _ResolvedPath(
                                resolved[0].value,
                                path_object=any(
                                    possibility.path_object
                                    for possibility in resolved
                                ),
                            )
                        return _ResolvedPath(
                            None,
                            path_object=any(
                                possibility.path_object for possibility in resolved
                            ),
                        )
            if name in self.binding_stack[index]:
                return self.binding_stack[index][name]
            if (
                self.scope_kind_stack[index]
                in {"function", "lambda", "comprehension"}
                and name in self.scope_stack[index].locals
            ):
                return None
        return None

    def _resolve_path(self, node: ast.AST | None) -> _ResolvedPath | None:
        literal = _static_string(node)
        if literal is not None:
            return _ResolvedPath(literal)
        if isinstance(node, ast.Name):
            return self._binding(node.id)
        if isinstance(node, ast.NamedExpr):
            return self._resolve_path(node.value)
        if isinstance(node, ast.IfExp):
            alternatives = [
                self._resolve_path(node.body),
                self._resolve_path(node.orelse),
            ]
            if alternatives[0] == alternatives[1]:
                return alternatives[0]
            if all(
                alternative is not None
                and alternative.value is not None
                and _target_violation(
                    self.source,
                    1,
                    "conditional-path",
                    alternative,
                    repository_root=self.repository_root,
                    local_path_semantics=True,
                )
                is None
                for alternative in alternatives
            ):
                resolved_alternatives = [
                    alternative for alternative in alternatives if alternative
                ]
                return _ResolvedPath(
                    resolved_alternatives[0].value,
                    path_object=any(
                        alternative.path_object
                        for alternative in resolved_alternatives
                    ),
                )
            if any(
                alternative is not None and alternative.path_object
                for alternative in alternatives
            ):
                return _ResolvedPath(None, path_object=True)
            return None
        if isinstance(node, ast.BoolOp):
            alternatives = [
                alternative
                for value in node.values
                if (alternative := self._resolve_path(value)) is not None
            ]
            if not alternatives:
                return None
            if all(alternative == alternatives[0] for alternative in alternatives):
                return alternatives[0]
            if all(
                alternative.value is not None
                and _target_violation(
                    self.source,
                    1,
                    "boolean-path",
                    alternative,
                    repository_root=self.repository_root,
                    local_path_semantics=True,
                )
                is None
                for alternative in alternatives
            ):
                return _ResolvedPath(
                    alternatives[0].value,
                    path_object=any(
                        alternative.path_object for alternative in alternatives
                    ),
                )
            return _ResolvedPath(
                None,
                path_object=any(
                    alternative.path_object for alternative in alternatives
                ),
            )
        if isinstance(node, ast.Attribute) and node.attr == "parent":
            parent = self._resolve_path(node.value)
            if parent and parent.path_object:
                value = posixpath.dirname(parent.value) if parent.value is not None else None
                return _ResolvedPath(value or "." if value is not None else None, True)
        if isinstance(node, ast.Call):
            name = self._qualified_name(node.func)
            if name in {"pathlib.Path.cwd", "pathlib.Path.home"}:
                return _ResolvedPath(None, path_object=True)
            if name in PATH_CONSTRUCTORS and len(node.args) == 1:
                inner = self._resolve_path(node.args[0])
                return _ResolvedPath(inner.value if inner else None, path_object=True)
            if name in {"os.path.join", "posixpath.join"} and node.args:
                parts = [self._resolve_path(arg) for arg in node.args]
                if all(part is not None and part.value is not None for part in parts):
                    return _ResolvedPath(
                        posixpath.join(
                            *(part.value for part in parts if part and part.value)
                        ),
                        path_object=any(part.path_object for part in parts if part),
                    )
            if isinstance(node.func, ast.Attribute) and node.func.attr == "joinpath":
                parent = self._resolve_path(node.func.value)
                parts = [self._resolve_path(arg) for arg in node.args]
                if parent and parent.path_object:
                    if parent.value is not None and all(
                        part is not None and part.value is not None for part in parts
                    ):
                        return _ResolvedPath(
                            posixpath.join(
                                parent.value,
                                *(part.value for part in parts if part and part.value),
                            ),
                            path_object=True,
                        )
                    return _ResolvedPath(None, path_object=True)
            if isinstance(node.func, ast.Attribute) and node.func.attr in {
                "absolute",
                "expanduser",
                "resolve",
            }:
                parent = self._resolve_path(node.func.value)
                if parent and parent.path_object:
                    value = parent.value
                    if value is not None and node.func.attr == "expanduser":
                        value = os.path.expanduser(value)
                    return _ResolvedPath(value, path_object=True)
            return None
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            left = self._resolve_path(node.left)
            right = self._resolve_path(node.right)
            if left and left.path_object:
                if left.value is not None and right and right.value is not None:
                    return _ResolvedPath(
                        posixpath.join(left.value, right.value), path_object=True
                    )
                return _ResolvedPath(None, path_object=True)
        return None

    def _add_target(
        self,
        call: ast.Call,
        sink: str,
        target_node: ast.AST | None,
        *,
        local_path_semantics: bool = False,
    ) -> None:
        violation = _target_violation(
            self.source,
            call.lineno,
            sink,
            self._resolve_path(target_node),
            repository_root=self.repository_root,
            local_path_semantics=local_path_semantics,
        )
        if violation:
            self.violations.append(violation)

    @staticmethod
    def _open_mode(call: ast.Call, positional_index: int) -> str:
        mode_node = _keyword(call, "mode")
        if mode_node is None and len(call.args) > positional_index:
            mode_node = call.args[positional_index]
        if mode_node is None:
            return "read"
        mode = _static_string(mode_node)
        if mode is None:
            return "unresolved"
        return "write" if any(flag in mode for flag in "wax+") else "read"

    def visit_Module(self, node: ast.Module) -> None:
        self._push_scope(node)
        for statement in node.body:
            self.visit(statement)
        self._pop_scope()

    def _bind_name(
        self,
        name: str,
        value: _ResolvedPath | None,
        alias: str | None = None,
    ) -> None:
        self.alias_stack[-1][name] = alias or f"{LOCAL_ALIAS_PREFIX}{name}"
        self.binding_stack[-1][name] = value

    def visit_Import(self, node: ast.Import) -> None:
        for item in node.names:
            local = item.asname or item.name.split(".", 1)[0]
            qualified = item.name if item.asname else item.name.split(".", 1)[0]
            self.binding_stack[-1][local] = None
            self.alias_stack[-1][local] = qualified

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for item in node.names:
            if item.name == "*":
                continue
            local = item.asname or item.name
            self.binding_stack[-1][local] = None
            if node.module is None:
                self.alias_stack[-1].pop(local, None)
            else:
                self.alias_stack[-1][local] = f"{node.module}.{item.name}"

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        for decorator in node.decorator_list:
            self.visit(decorator)
        for default in node.args.defaults:
            self.visit(default)
        for default in node.args.kw_defaults:
            if default is not None:
                self.visit(default)
        resolved_defaults = self._resolved_argument_defaults(node.args)
        self._push_scope(node)
        self._bind_argument_defaults(resolved_defaults)
        for statement in node.body:
            self.visit(statement)
        self._pop_scope()
        self._bind_name(node.name, None)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        for decorator in node.decorator_list:
            self.visit(decorator)
        for base in node.bases:
            self.visit(base)
        self._push_scope(node)
        for statement in node.body:
            self.visit(statement)
        self._pop_scope()
        self._bind_name(node.name, None)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        for default in node.args.defaults:
            self.visit(default)
        for default in node.args.kw_defaults:
            if default is not None:
                self.visit(default)
        resolved_defaults = self._resolved_argument_defaults(node.args)
        self._push_scope(node)
        self._bind_argument_defaults(resolved_defaults)
        self.visit(node.body)
        self._pop_scope()

    def _resolved_argument_defaults(
        self,
        arguments: ast.arguments,
    ) -> list[tuple[str, _ResolvedPath | None, str | None]]:
        resolved: list[tuple[str, _ResolvedPath | None, str | None]] = []
        positional = [*arguments.posonlyargs, *arguments.args]
        offset = len(positional) - len(arguments.defaults)
        for argument, default in zip(positional[offset:], arguments.defaults):
            resolved.append(
                (
                    argument.arg,
                    self._resolve_path(default),
                    self._alias_value(default),
                )
            )
        for argument, default in zip(arguments.kwonlyargs, arguments.kw_defaults):
            if default is not None:
                resolved.append(
                    (
                        argument.arg,
                        self._resolve_path(default),
                        self._alias_value(default),
                    )
                )
        return resolved

    def _bind_argument_defaults(
        self,
        defaults: list[tuple[str, _ResolvedPath | None, str | None]],
    ) -> None:
        for name, value, alias in defaults:
            self._bind_name(name, value, alias)

    def _bind_target(
        self,
        target: ast.AST,
        value: _ResolvedPath | None,
        alias: str | None = None,
    ) -> None:
        if isinstance(target, ast.Name):
            self._bind_name(target.id, value, alias)
            return
        if isinstance(target, (ast.Tuple, ast.List)):
            for item in target.elts:
                self._bind_target(item, None)

    def visit_Assign(self, node: ast.Assign) -> None:
        self.visit(node.value)
        for target in node.targets:
            self._bind_assignment_target(target, node.value)

    def _bind_assignment_target(self, target: ast.AST, value: ast.AST) -> None:
        if (
            isinstance(target, (ast.Tuple, ast.List))
            and isinstance(value, (ast.Tuple, ast.List))
            and len(target.elts) == len(value.elts)
        ):
            for target_item, value_item in zip(target.elts, value.elts):
                self._bind_assignment_target(target_item, value_item)
            return
        self._bind_target(
            target,
            self._resolve_path(value),
            self._alias_value(value),
        )

    def _resolved_assignment_bindings(
        self,
        target: ast.AST,
        value: ast.AST,
    ) -> list[tuple[str, _ResolvedPath | None, str | None]]:
        if (
            isinstance(target, (ast.Tuple, ast.List))
            and isinstance(value, (ast.Tuple, ast.List))
            and len(target.elts) == len(value.elts)
        ):
            bindings: list[tuple[str, _ResolvedPath | None, str | None]] = []
            for target_item, value_item in zip(target.elts, value.elts):
                bindings.extend(
                    self._resolved_assignment_bindings(target_item, value_item)
                )
            return bindings
        if isinstance(target, ast.Name):
            return [
                (
                    target.id,
                    self._resolve_path(value),
                    self._alias_value(value),
                )
            ]
        if isinstance(target, (ast.Tuple, ast.List)):
            return [
                (item.id, None, None)
                for item in ast.walk(target)
                if isinstance(item, ast.Name)
            ]
        return []

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value is not None:
            self.visit(node.value)
        self._bind_target(
            node.target,
            self._resolve_path(node.value),
            self._alias_value(node.value),
        )

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.visit(node.value)
        value = self._resolve_path(node.value)
        if self.scope_kind_stack[-1] != "comprehension":
            self._bind_target(node.target, value, self._alias_value(node.value))
            return
        for index in range(len(self.scope_kind_stack) - 2, -1, -1):
            if self.scope_kind_stack[index] != "comprehension":
                if isinstance(node.target, ast.Name):
                    self.alias_stack[index][node.target.id] = (
                        self._alias_value(node.value)
                        or f"{LOCAL_ALIAS_PREFIX}{node.target.id}"
                    )
                    self.binding_stack[index][node.target.id] = value
                return

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self.visit(node.value)
        value: _ResolvedPath | None = None
        if isinstance(node.target, ast.Name) and isinstance(node.op, ast.Div):
            left = self._binding(node.target.id)
            right = self._resolve_path(node.value)
            if left and left.path_object:
                if left.value is not None and right and right.value is not None:
                    value = _ResolvedPath(
                        posixpath.join(left.value, right.value), path_object=True
                    )
                else:
                    value = _ResolvedPath(None, path_object=True)
        self._bind_target(node.target, value)

    def visit_Delete(self, node: ast.Delete) -> None:
        for target in node.targets:
            self._bind_target(target, None)

    def _merge_bindings(
        self,
        *environments: dict[str, _ResolvedPath | None],
    ) -> dict[str, _ResolvedPath | None]:
        missing = object()
        merged: dict[str, _ResolvedPath | None] = {}
        names = set().union(*(environment.keys() for environment in environments))
        for name in names:
            candidates = [environment.get(name, missing) for environment in environments]
            first = candidates[0]
            if first is not missing and all(candidate == first for candidate in candidates):
                merged[name] = first
            elif all(
                isinstance(candidate, _ResolvedPath)
                and candidate.value is not None
                and _target_violation(
                    self.source,
                    1,
                    "merged-path",
                    candidate,
                    repository_root=self.repository_root,
                    local_path_semantics=True,
                )
                is None
                for candidate in candidates
            ):
                resolved_candidates = [
                    candidate
                    for candidate in candidates
                    if isinstance(candidate, _ResolvedPath)
                ]
                merged[name] = _ResolvedPath(
                    resolved_candidates[0].value,
                    path_object=any(
                        candidate.path_object for candidate in resolved_candidates
                    ),
                )
            elif any(
                isinstance(candidate, _ResolvedPath) and candidate.path_object
                for candidate in candidates
            ):
                merged[name] = _ResolvedPath(None, path_object=True)
            else:
                merged[name] = None
        return merged

    def _outer_alias(self, name: str) -> str:
        for index in range(len(self.scope_stack) - 2, -1, -1):
            if name in self.alias_stack[index]:
                return self.alias_stack[index][name]
            if (
                self.scope_kind_stack[index]
                in {"function", "lambda", "comprehension"}
                and name in self.scope_stack[index].locals
            ) or name in self.binding_stack[index]:
                return f"{LOCAL_ALIAS_PREFIX}{name}"
        return "builtins.open" if name == "open" else name

    def _merge_aliases(
        self,
        environments: list[
            tuple[dict[str, _ResolvedPath | None], dict[str, str]]
        ],
    ) -> dict[str, str]:
        names = set().union(
            *(set(bindings) | set(aliases) for bindings, aliases in environments)
        )
        merged: dict[str, str] = {}
        for name in names:
            candidates = [
                aliases.get(
                    name,
                    f"{LOCAL_ALIAS_PREFIX}{name}"
                    if name in bindings
                    else self._outer_alias(name),
                )
                for bindings, aliases in environments
            ]
            if all(candidate == candidates[0] for candidate in candidates[1:]):
                merged[name] = candidates[0]
                continue
            recognized = {
                candidate
                for candidate in candidates
                if candidate in RECOGNIZED_ALIAS_TARGETS
                or candidate in RECOGNIZED_ALIAS_ROOTS
                or candidate == AMBIGUOUS_SINK_ALIAS
            }
            merged[name] = (
                AMBIGUOUS_SINK_ALIAS
                if recognized
                else f"{LOCAL_ALIAS_PREFIX}{name}"
            )
        return merged

    def _set_environment(
        self,
        bindings: dict[str, _ResolvedPath | None],
        aliases: dict[str, str],
    ) -> None:
        self.binding_stack[-1] = dict(bindings)
        self.alias_stack[-1] = dict(aliases)

    def _visit_branch(
        self,
        statements: list[ast.stmt],
        bindings: dict[str, _ResolvedPath | None],
        aliases: dict[str, str],
    ) -> tuple[dict[str, _ResolvedPath | None], dict[str, str]]:
        self._set_environment(bindings, aliases)
        for statement in statements:
            self.visit(statement)
        return dict(self.binding_stack[-1]), dict(self.alias_stack[-1])

    def _merge_environments(
        self,
        environments: list[
            tuple[dict[str, _ResolvedPath | None], dict[str, str]]
        ],
    ) -> None:
        self.binding_stack[-1] = self._merge_bindings(
            *(bindings for bindings, _ in environments)
        )
        self.alias_stack[-1] = self._merge_aliases(environments)

    def visit_If(self, node: ast.If) -> None:
        self.visit(node.test)
        before = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
        after_body = self._visit_branch(node.body, *before)
        after_else = self._visit_branch(node.orelse, *before)
        self._merge_environments([after_body, after_else])

    def _visit_loop(
        self,
        node: ast.For | ast.AsyncFor,
    ) -> None:
        self.visit(node.iter)
        before = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
        item_value: _ResolvedPath | None = None
        item_alias: str | None = None
        if isinstance(node.iter, (ast.List, ast.Tuple, ast.Set)) and len(
            node.iter.elts
        ) == 1:
            item_value = self._resolve_path(node.iter.elts[0])
            item_alias = self._alias_value(node.iter.elts[0])
        loop_head = before
        while True:
            self._set_environment(*loop_head)
            self._bind_target(node.target, item_value, item_alias)
            for statement in node.body:
                self.visit(statement)
            after_body = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
            self._merge_environments([before, after_body])
            next_head = (
                dict(self.binding_stack[-1]),
                dict(self.alias_stack[-1]),
            )
            if next_head == loop_head:
                break
            loop_head = next_head
        after_else = self._visit_branch(node.orelse, *loop_head)
        self._merge_environments([loop_head, after_else])

    def visit_For(self, node: ast.For) -> None:
        self._visit_loop(node)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        self._visit_loop(node)

    def visit_While(self, node: ast.While) -> None:
        self.visit(node.test)
        before = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
        loop_head = before
        while True:
            self._set_environment(*loop_head)
            self.visit(node.test)
            for statement in node.body:
                self.visit(statement)
            after_body = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
            self._merge_environments([before, after_body])
            next_head = (
                dict(self.binding_stack[-1]),
                dict(self.alias_stack[-1]),
            )
            if next_head == loop_head:
                break
            loop_head = next_head
        after_else = self._visit_branch(node.orelse, *loop_head)
        self._merge_environments([loop_head, after_else])

    def visit_Try(self, node: ast.Try) -> None:
        before = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
        self._set_environment(*before)
        body_states = [before]
        for statement in node.body:
            self.visit(statement)
            body_states.append(
                (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
            )
        after_body = body_states[-1]
        after_success = self._visit_branch(node.orelse, *after_body)
        self._merge_environments(body_states)
        handler_start = (
            dict(self.binding_stack[-1]),
            dict(self.alias_stack[-1]),
        )
        branches = [after_success]
        for handler in node.handlers:
            self._set_environment(*handler_start)
            if handler.type is not None:
                self.visit(handler.type)
            if handler.name:
                self._bind_name(handler.name, None)
            for statement in handler.body:
                self.visit(statement)
            branches.append(
                (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
            )
        self._merge_environments(branches)
        for statement in node.finalbody:
            self.visit(statement)

    def visit_TryStar(self, node: ast.TryStar) -> None:
        self.visit_Try(node)

    def _bind_match_pattern(self, pattern: ast.pattern) -> None:
        for item in ast.walk(pattern):
            if isinstance(item, (ast.MatchAs, ast.MatchStar)) and item.name:
                self._bind_name(item.name, None)
            elif isinstance(item, ast.MatchMapping) and item.rest:
                self._bind_name(item.rest, None)

    def visit_Match(self, node: ast.Match) -> None:
        self.visit(node.subject)
        before = (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
        exhaustive = any(
            case.guard is None
            and isinstance(case.pattern, ast.MatchAs)
            and case.pattern.pattern is None
            for case in node.cases
        )
        branches = [] if exhaustive else [before]
        for case in node.cases:
            self._set_environment(*before)
            self._bind_match_pattern(case.pattern)
            if case.guard is not None:
                self.visit(case.guard)
            for statement in case.body:
                self.visit(statement)
            branches.append(
                (dict(self.binding_stack[-1]), dict(self.alias_stack[-1]))
            )
        self._merge_environments(branches)

    @staticmethod
    def _comprehension_locals(generators: list[ast.comprehension]) -> frozenset[str]:
        names: set[str] = set()
        for generator in generators:
            names.update(
                item.id
                for item in ast.walk(generator.target)
                if isinstance(item, ast.Name) and isinstance(item.ctx, ast.Store)
            )
        return frozenset(names)

    def _visit_comprehension(
        self,
        node: ast.ListComp | ast.SetComp | ast.DictComp | ast.GeneratorExp,
    ) -> None:
        generators = node.generators
        if not generators:
            return
        self.visit(generators[0].iter)
        first_bindings: list[tuple[str, _ResolvedPath | None, str | None]] = []
        if isinstance(generators[0].iter, (ast.List, ast.Tuple, ast.Set)) and len(
            generators[0].iter.elts
        ) == 1:
            first_bindings = self._resolved_assignment_bindings(
                generators[0].target,
                generators[0].iter.elts[0],
            )
        scope = _ScopeInfo(self._comprehension_locals(generators), {})
        self._push_custom_scope(scope, "comprehension")
        for index, generator in enumerate(generators):
            if index:
                self.visit(generator.iter)
            if index == 0 and first_bindings:
                for name, value, alias in first_bindings:
                    self._bind_name(name, value, alias)
            elif isinstance(generator.iter, (ast.List, ast.Tuple, ast.Set)) and len(
                generator.iter.elts
            ) == 1:
                self._bind_assignment_target(
                    generator.target,
                    generator.iter.elts[0],
                )
            else:
                self._bind_target(generator.target, None)
            for condition in generator.ifs:
                self.visit(condition)
        if isinstance(node, ast.DictComp):
            self.visit(node.key)
            self.visit(node.value)
        else:
            self.visit(node.elt)
        self._pop_scope()

    def visit_ListComp(self, node: ast.ListComp) -> None:
        self._visit_comprehension(node)

    def visit_SetComp(self, node: ast.SetComp) -> None:
        self._visit_comprehension(node)

    def visit_DictComp(self, node: ast.DictComp) -> None:
        self._visit_comprehension(node)

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        self._visit_comprehension(node)

    def visit_Call(self, call: ast.Call) -> None:
        name = self._qualified_name(call.func)
        method = call.func.attr if isinstance(call.func, ast.Attribute) else None

        if name == AMBIGUOUS_SINK_ALIAS:
            self.violations.append(
                Violation(
                    self.source,
                    call.lineno,
                    "python-call",
                    "<unresolved-sink>",
                    "DIR-PLACE-003 cannot classify a control-flow-dependent output sink",
                )
            )
            self.generic_visit(call)
            return

        if name in {"builtins.open", "io.open"}:
            mode = self._open_mode(call, 1)
            if mode == "unresolved":
                self.violations.append(
                    Violation(
                        self.source,
                        call.lineno,
                        name,
                        "<unresolved-mode>",
                        "DIR-PLACE-003 cannot classify a dynamic file-open mode",
                    )
                )
            elif mode == "write":
                target = call.args[0] if call.args else _keyword(call, "file")
                self._add_target(call, name, target, local_path_semantics=True)
        elif method == "open":
            receiver = self._resolve_path(call.func.value)
            if receiver and receiver.path_object:
                mode = self._open_mode(call, 0)
                if mode == "unresolved":
                    self.violations.append(
                        Violation(
                            self.source,
                            call.lineno,
                            "pathlib.Path.open",
                            "<unresolved-mode>",
                            "DIR-PLACE-003 cannot classify a dynamic Path.open mode",
                        )
                    )
                elif mode == "write":
                    violation = _target_violation(
                        self.source,
                        call.lineno,
                        "pathlib.Path.open",
                        receiver,
                        repository_root=self.repository_root,
                        local_path_semantics=True,
                    )
                    if violation:
                        self.violations.append(violation)
        elif method in PATH_RECEIVER_SINKS:
            receiver = self._resolve_path(call.func.value)
            if receiver is None or receiver.path_object:
                violation = _target_violation(
                    self.source,
                    call.lineno,
                    f"pathlib.Path.{method}",
                    receiver,
                    repository_root=self.repository_root,
                    local_path_semantics=True,
                )
                if violation:
                    self.violations.append(violation)
        elif method in PATH_DESTINATION_SINKS:
            receiver = self._resolve_path(call.func.value)
            if receiver and receiver.path_object:
                destination = (
                    call.args[0] if call.args else _keyword(call, "target")
                )
                self._add_target(
                    call,
                    f"pathlib.Path.{method}",
                    destination,
                    local_path_semantics=True,
                )
        elif method in EXPORT_SINKS:
            target = (
                call.args[0]
                if call.args
                else _keyword(call, "path", "path_or_buf", "fname")
            )
            if target is not None:
                self._add_target(call, method, target)
        elif name in DIRECT_PATH_SINKS:
            target = call.args[0] if call.args else _keyword(call, "name", "path")
            self._add_target(call, name, target, local_path_semantics=True)
        elif name in COPY_MOVE_SINKS:
            target = call.args[1] if len(call.args) > 1 else _keyword(call, "dst")
            self._add_target(call, name, target, local_path_semantics=True)
        elif name in SUBPROCESS_SINKS:
            command_node = call.args[0] if call.args else _keyword(call, "args", "command")
            try:
                tokens = _command_tokens(command_node)
            except ValueError:
                tokens = None
            if tokens is None:
                self.violations.append(
                    Violation(
                        self.source,
                        call.lineno,
                        name,
                        "<unresolved-command>",
                        "DIR-PLACE-003 cannot classify a dynamic subprocess command",
                    )
                )
            else:
                self.violations.extend(
                    _scan_shell_tokens(
                        tokens,
                        source=self.source,
                        line=call.lineno,
                        repository_root=self.repository_root,
                    )
                )

        self.generic_visit(call)


def scan_python_source(
    text: str,
    *,
    source: str,
    repository_root: Path,
) -> list[Violation]:
    """Inspect selected Python filesystem/export/subprocess sinks."""

    try:
        tree = ast.parse(text, filename=source)
    except SyntaxError as error:
        return [
            Violation(
                source,
                error.lineno or 1,
                "python-parse",
                "<unresolved>",
                "DIR-PLACE-003 scanner cannot classify invalid Python source",
            )
        ]
    scanner = _PythonScanner(source=source, repository_root=repository_root, tree=tree)
    scanner.visit(tree)
    return sorted(set(scanner.violations))


def _strip_yaml_comment(value: str) -> str:
    """Strip a YAML comment marker only when it is outside a quoted scalar."""

    in_single = False
    in_double = False
    escaped = False
    index = 0
    while index < len(value):
        character = value[index]
        if in_double:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_double = False
        elif in_single:
            if character == "'" and index + 1 < len(value) and value[index + 1] == "'":
                index += 1
            elif character == "'":
                in_single = False
        elif character == '"':
            in_double = True
        elif character == "'":
            in_single = True
        elif character == "#" and (index == 0 or value[index - 1].isspace()):
            return value[:index]
        index += 1
    return value


def _yaml_unquoted_index(value: str, expected: str) -> int | None:
    """Find one structural character outside YAML-style quoted text."""

    in_single = False
    in_double = False
    escaped = False
    index = 0
    while index < len(value):
        character = value[index]
        if in_double:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                in_double = False
        elif in_single:
            if character == "'" and index + 1 < len(value) and value[index + 1] == "'":
                index += 1
            elif character == "'":
                in_single = False
        elif character == '"':
            in_double = True
        elif character == "'":
            in_single = True
        elif character == expected:
            return index
        index += 1
    return None


def _yaml_scalar(value: str) -> str | None:
    value = _strip_yaml_comment(value).strip()
    if not value or value[0] in "[{&*!":
        return None
    if value[0:1] == value[-1:] and value.startswith(("'", '"')):
        return value[1:-1].replace("''", "'")
    return value


def _scan_yaml_scalar_value(
    key: str,
    value: str,
    *,
    source: str,
    line: int,
    repository_root: Path,
) -> list[Violation]:
    if key in YAML_COMMAND_KEYS:
        scalar = _yaml_scalar(value)
        if scalar is None or _has_template(scalar):
            return [
                Violation(
                    source,
                    line,
                    f"yaml-{key}",
                    "<unresolved-command>",
                    "DIR-PLACE-003 cannot classify the YAML command value",
                )
            ]
        return scan_shell_source(
            scalar,
            source=source,
            repository_root=repository_root,
            first_line=line,
        )
    target = _yaml_scalar(value)
    violation = _target_violation(
        source,
        line,
        f"yaml-{key}",
        _ResolvedPath(target) if target is not None else None,
        repository_root=repository_root,
    )
    return [violation] if violation else []


def scan_yaml_source(
    text: str,
    *,
    source: str,
    repository_root: Path,
) -> list[Violation]:
    """Inspect bounded YAML command/output keys without loading YAML objects."""

    violations: list[Violation] = []
    lines = text.splitlines()
    index = 0
    key_pattern = re.compile(
        r'''^(?P<indent>\s*)(?:-\s*)?(?P<key>"[A-Za-z_][\w-]*"|'[A-Za-z_][\w-]*'|[A-Za-z_][\w-]*)\s*:\s*(?P<value>.*)$'''
    )
    flow_key_pattern = re.compile(
        r'''["']?(?:command|run|script|shell|destination|output[_-]path|sink)["']?\s*:''',
        re.IGNORECASE,
    )
    # Keep escaped and ordinary double-quoted characters disjoint. Allowing a
    # backslash through both alternatives makes rejection of an unterminated
    # scalar exponentially expensive (CodeQL py/redos).
    flow_pair_pattern = re.compile(
        r'''(?:^|[{,]\s*)(?P<key>"[A-Za-z_][\w-]*"|'[A-Za-z_][\w-]*'|[A-Za-z_][\w-]*)\s*:\s*(?P<value>"(?:\\.|[^"\\])*"|'(?:''|[^'])*'|[^,}]+)'''
    )
    block_pattern = re.compile(r"^[|>](?:[1-9])?[+-]?$|^[|>][+-](?:[1-9])?$")
    while index < len(lines):
        structural_line = _strip_yaml_comment(lines[index]).strip()
        flow_fragment: str | None = None
        structural_value = (
            structural_line[2:].lstrip()
            if structural_line.startswith("- ")
            else structural_line
        )
        if structural_value.startswith("{"):
            flow_fragment = structural_value
        else:
            outer = key_pattern.match(structural_line)
            if outer:
                outer_value = outer.group("value").strip()
                if outer_value.startswith("{"):
                    flow_fragment = outer_value
                elif outer_value.startswith("["):
                    brace_index = _yaml_unquoted_index(outer_value, "{")
                    if brace_index is not None:
                        flow_fragment = outer_value[brace_index:]
        if flow_fragment is not None and flow_key_pattern.search(flow_fragment):
            recognized = False
            for pair in flow_pair_pattern.finditer(flow_fragment):
                flow_key = pair.group("key").strip("'\"").lower().replace("-", "_")
                if flow_key not in YAML_COMMAND_KEYS | YAML_OUTPUT_KEYS:
                    continue
                recognized = True
                violations.extend(
                    _scan_yaml_scalar_value(
                        flow_key,
                        pair.group("value"),
                        source=source,
                        line=index + 1,
                        repository_root=repository_root,
                    )
                )
            if not recognized:
                violations.append(
                    Violation(
                        source,
                        index + 1,
                        "yaml-flow-mapping",
                        "<unresolved>",
                        "DIR-PLACE-003 cannot classify a recognized key in a YAML flow mapping",
                    )
                )
            index += 1
            continue
        match = key_pattern.match(lines[index])
        if not match:
            index += 1
            continue
        key = match.group("key").strip("'\"").lower().replace("-", "_")
        value = match.group("value").strip()
        line = index + 1
        if key in YAML_COMMAND_KEYS:
            block_value = _strip_yaml_comment(value).strip()
            if block_pattern.match(block_value):
                parent_indent = len(match.group("indent"))
                block: list[str] = []
                index += 1
                while index < len(lines):
                    raw = lines[index]
                    if raw.strip() and len(raw) - len(raw.lstrip()) <= parent_indent:
                        break
                    block.append(raw)
                    index += 1
                command = textwrap.dedent("\n".join(block))
                if block_value.startswith(">"):
                    command = " ".join(part.strip() for part in command.splitlines())
                if not command.strip():
                    violations.append(
                        Violation(
                            source,
                            line,
                            f"yaml-{key}",
                            "<unresolved-command>",
                            "DIR-PLACE-003 cannot classify an empty YAML command block",
                        )
                    )
                else:
                    violations.extend(
                        scan_shell_source(
                            command,
                            source=source,
                            repository_root=repository_root,
                            first_line=line + 1,
                        )
                    )
                continue
            parent_indent = len(match.group("indent"))
            continuation: list[str] = []
            next_index = index + 1
            while next_index < len(lines):
                raw = lines[next_index]
                if not raw.strip():
                    next_index += 1
                    continue
                indent = len(raw) - len(raw.lstrip())
                if indent <= parent_indent or key_pattern.match(raw):
                    break
                continuation.append(_strip_yaml_comment(raw).strip())
                next_index += 1
            if continuation:
                violations.extend(
                    _scan_yaml_scalar_value(
                        key,
                        " ".join([value, *continuation]),
                        source=source,
                        line=line,
                        repository_root=repository_root,
                    )
                )
                index = next_index
                continue
            violations.extend(
                _scan_yaml_scalar_value(
                    key,
                    value,
                    source=source,
                    line=line,
                    repository_root=repository_root,
                )
            )
        elif key in YAML_OUTPUT_KEYS:
            violations.extend(
                _scan_yaml_scalar_value(
                    key,
                    value,
                    source=source,
                    line=line,
                    repository_root=repository_root,
                )
            )
        index += 1
    return sorted(set(violations))


def scan_connector_file(path: Path, repository_root: Path) -> list[Violation]:
    """Scan one connector source file and fail visibly on unreadable/symlink input."""

    try:
        source = path.relative_to(repository_root).as_posix()
    except ValueError:
        source = path.as_posix()
    if path.is_symlink():
        return [
            Violation(
                source,
                1,
                "source-symlink",
                "<unresolved>",
                "DIR-PLACE-003 scanner does not follow connector source symlinks",
            )
        ]
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return [
            Violation(
                source,
                1,
                "source-read",
                "<unresolved>",
                "DIR-PLACE-003 scanner could not read connector source as UTF-8",
            )
        ]
    if path.suffix == ".py":
        return scan_python_source(text, source=source, repository_root=repository_root)
    if path.suffix == ".sh":
        return scan_shell_source(text, source=source, repository_root=repository_root)
    return scan_yaml_source(text, source=source, repository_root=repository_root)


def legacy_publish_target_violations(repository_root: Path) -> list[str]:
    """Run the preserved lexical connector/pipeline publication-target canary."""

    violations: list[str] = []
    for relative_root in LEGACY_ROOTS:
        root = repository_root / relative_root
        if not root.is_dir():
            continue
        for file_path in _iter_source_files(root):
            text = file_path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for index, line in enumerate(lines, start=1):
                is_write_context = bool(
                    PY_WRITE_CALL_PATTERN.search(line)
                    or SHELL_WRITE_PATTERN.search(line)
                )
                if not is_write_context:
                    continue
                window = "\n".join(
                    lines[max(0, index - 3) : min(len(lines), index + 2)]
                )
                for target in LEGACY_FORBIDDEN_TARGETS:
                    if target in window:
                        relative = file_path.relative_to(repository_root)
                        violations.append(
                            "Forbidden publish-target write context in "
                            f"{relative}:{index} -> {target}"
                        )
    return sorted(violations)
