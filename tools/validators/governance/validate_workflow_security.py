#!/usr/bin/env python3
"""Ratcheted, standard-library security checks for GitHub Actions workflows.

The scanner is deliberately local and static: it reads workflow bytes, never
loads actions, never contacts GitHub, and never executes workflow content.  Its
baseline is an implementation waiver list keyed by exact finding fingerprints;
it cannot define rules, waive invariant rules, or authorize repository writes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

REPORT_VERSION = "kfm.workflow-security-report.v1"
BASELINE_VERSION = "kfm.workflow-security-baseline.v1"
DEFAULT_BASELINE = Path(__file__).with_name("workflow_security_baseline.json")
MAX_WORKFLOW_BYTES = 512 * 1024
MAX_BASELINE_BYTES = 512 * 1024
MAX_FINDINGS = 10_000
SHA256_RE = re.compile(r"^[0-9a-f]{40}$")
SAFE_ID_RE = re.compile(r"^[A-Za-z0-9_.-]{1,128}$")
TOP_KEY_RE = re.compile(r"^(?:\"([^\"]+)\"|'([^']+)'|([A-Za-z_][A-Za-z0-9_-]*)):\s*(.*)$")
WRITE_SCOPE_ALLOWLIST = frozenset({"pull-requests", "security-events"})
TRUSTED_PULL_REQUEST_WRITE_TRIGGERS = frozenset(
    {"repository_dispatch", "workflow_dispatch", "push"}
)
GITHUB_HOSTED_RUNNERS = frozenset({"ubuntu-latest", "ubuntu-24.04"})
UNTRUSTED_SHELL_EXPRESSION_RE = re.compile(
    r"\$\{\{\s*(?:"
    r"github\.(?:head_ref|event\.client_payload(?:\.|\b)|"
    r"event\.(?:comment|issue_comment)\.body\b|"
    r"event\.issue\.(?:title|body)\b|"
    r"event\.pull_request\.(?:title|body|head\.(?:ref|label))\b)"
    r"|inputs\.[A-Za-z0-9_-]+)"
)
PULL_REQUEST_HEAD_RE = re.compile(
    r"\$\{\{\s*(?:github\.head_ref|github\.event\.pull_request\.head(?:\.|\b)|"
    r"github\.event\.pull_request\.merge_commit_sha\b)"
)
BRACKET_PROPERTY_RE = re.compile(r"\[\s*['\"]([A-Za-z0-9_-]+)['\"]\s*\]")


@dataclass(frozen=True)
class Rule:
    rule_id: str
    title: str
    baseline_allowed: bool


RULES: tuple[Rule, ...] = (
    Rule("KFM-WF-001", "Workflow input must be safe, bounded UTF-8", False),
    Rule("KFM-WF-002", "Workflow name is required", False),
    Rule("KFM-WF-003", "Workflow names are unique under Unicode case-folding", False),
    Rule("KFM-WF-004", "External actions use immutable full commit pins", False),
    Rule("KFM-WF-005", "Container images use immutable SHA-256 digest pins", False),
    Rule("KFM-WF-006", "Checkout never persists credentials", True),
    Rule("KFM-WF-007", "Workflow-level permissions are explicit", False),
    Rule("KFM-WF-008", "Write permissions are not granted at workflow scope", True),
    Rule("KFM-WF-009", "Write permission scopes use the bounded allowlist", False),
    Rule("KFM-WF-010", "Pull-request mutation jobs use trusted triggers only", False),
    Rule("KFM-WF-011", "pull_request_target workflows remain read-only", False),
    Rule("KFM-WF-012", "pull_request_target checkout is pinned to trusted base", False),
    Rule("KFM-WF-013", "pull_request_target never selects pull-request head", False),
    Rule("KFM-WF-014", "Self-hosted runners are denied", False),
    Rule("KFM-WF-015", "Reusable workflows cannot inherit all secrets", False),
    Rule("KFM-WF-016", "Secrets are not placed in workflow-global environment", False),
    Rule("KFM-WF-017", "Untrusted event expressions are not interpolated in shell", False),
    Rule("KFM-WF-018", "Downloaded content is not piped to a shell", False),
    Rule("KFM-WF-019", "Deprecated workflow command channels are denied", False),
    Rule("KFM-WF-020", "Every job has a bounded timeout", True),
)
RULE_BY_ID = {rule.rule_id: rule for rule in RULES}
if len(RULES) != 20 or len(RULE_BY_ID) != 20:
    raise RuntimeError("workflow security profile must contain exactly 20 unique rules")


class BaselineError(ValueError):
    """Raised when an implementation baseline is malformed or unsafe."""


@dataclass(frozen=True, order=True)
class Finding:
    rule_id: str
    path: str
    subject: str
    evidence_sha256: str
    fingerprint: str
    line: int

    def as_dict(self, disposition: str) -> dict[str, object]:
        return {
            "disposition": disposition,
            "evidence_sha256": self.evidence_sha256,
            "fingerprint": self.fingerprint,
            "line": self.line,
            "path": self.path,
            "rule_id": self.rule_id,
            "subject": self.subject,
        }


@dataclass(frozen=True)
class Step:
    job_id: str
    ordinal: int
    subject: str
    start: int
    end: int
    lines: tuple[str, ...]


@dataclass(frozen=True)
class Job:
    job_id: str
    start: int
    end: int
    lines: tuple[str, ...]
    permissions: Mapping[str, str]
    steps: tuple[Step, ...]


@dataclass(frozen=True)
class Workflow:
    path: str
    absolute_path: Path
    text: str
    lines: tuple[str, ...]
    name: str | None
    triggers: frozenset[str]
    top_permissions: Mapping[str, str] | None
    jobs: tuple[Job, ...]
    run_line_indexes: frozenset[int]


def _digest(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def _label(value: str, fallback: str) -> str:
    value = value.strip().strip("\"'")
    return value if SAFE_ID_RE.fullmatch(value) else fallback


def _finding(
    rule_id: str,
    path: str,
    subject: str,
    evidence: str,
    line: int,
) -> Finding:
    evidence_sha256 = _digest(evidence)
    fingerprint = _digest("\0".join((rule_id, path, subject, evidence_sha256)))
    return Finding(rule_id, path, subject, evidence_sha256, fingerprint, line)


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_content(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and not stripped.startswith("#")


def _strip_inline_comment(value: str) -> str:
    quote: str | None = None
    escaped = False
    for index, character in enumerate(value):
        if escaped:
            escaped = False
            continue
        if character == "\\" and quote == '"':
            escaped = True
            continue
        if quote:
            if character == quote:
                quote = None
            continue
        if character in {"'", '"'}:
            quote = character
        elif character == "#" and (index == 0 or value[index - 1].isspace()):
            return value[:index].rstrip()
    return value.rstrip()


def _unquoted_projection(value: str) -> str:
    projected: list[str] = []
    quote: str | None = None
    escaped = False
    for character in _strip_inline_comment(value):
        if escaped:
            escaped = False
            projected.append(" ")
            continue
        if character == "\\" and quote == '"':
            escaped = True
            projected.append(" ")
            continue
        if quote:
            if character == quote:
                quote = None
            projected.append(" ")
            continue
        if character in {"'", '"'}:
            quote = character
            projected.append(" ")
        else:
            projected.append(character)
    return "".join(projected)


def _normalize_expression_properties(value: str) -> str:
    return BRACKET_PROPERTY_RE.sub(lambda match: "." + match.group(1), value)


def _key(line: str, indent: int | None = None) -> tuple[str, str] | None:
    if not _is_content(line) or (indent is not None and _indent(line) != indent):
        return None
    match = TOP_KEY_RE.match(_strip_inline_comment(line.lstrip(" ")))
    if not match:
        return None
    return next(value for value in match.groups()[:3] if value is not None), match.group(4)


def _top_key_index(lines: Sequence[str], wanted: str) -> int | None:
    for index, line in enumerate(lines):
        parsed = _key(line, 0)
        if parsed and parsed[0] == wanted:
            return index
    return None


def _section_end(lines: Sequence[str], start: int, indent: int) -> int:
    for index in range(start + 1, len(lines)):
        if _is_content(lines[index]) and _indent(lines[index]) <= indent:
            return index
    return len(lines)


def _inline_mapping(value: str) -> dict[str, str] | None:
    stripped = value.strip()
    if stripped == "{}":
        return {}
    if not (stripped.startswith("{") and stripped.endswith("}")):
        return None
    result: dict[str, str] = {}
    body = stripped[1:-1].strip()
    if not body:
        return result
    for item in body.split(","):
        if ":" not in item:
            return None
        key, raw = item.split(":", 1)
        normalized_key = key.strip().strip("\"'")
        normalized_value = raw.strip().strip("\"'")
        if not normalized_key or normalized_key in result:
            return None
        result[normalized_key] = normalized_value
    return result


def _mapping_at(lines: Sequence[str], index: int, indent: int) -> dict[str, str]:
    parsed = _key(lines[index], indent)
    if not parsed:
        return {}
    value = parsed[1].strip()
    inline = _inline_mapping(value)
    if inline is not None:
        return inline
    if value:
        return {"*": value.strip("\"'")}
    end = _section_end(lines, index, indent)
    result: dict[str, str] = {}
    child_indent: int | None = None
    for child_index in range(index + 1, end):
        line = lines[child_index]
        if not _is_content(line):
            continue
        observed = _indent(line)
        if observed <= indent:
            break
        if child_indent is None:
            child_indent = observed
        if observed != child_indent:
            continue
        child = _key(line, child_indent)
        if child:
            result[child[0]] = child[1].strip().strip("\"'")
    return result


def _triggers(lines: Sequence[str]) -> frozenset[str]:
    index = _top_key_index(lines, "on")
    if index is None:
        return frozenset()
    value = (_key(lines[index], 0) or ("", ""))[1].strip()
    known = {
        "branch_protection_rule",
        "check_run",
        "create",
        "delete",
        "deployment",
        "deployment_status",
        "discussion",
        "discussion_comment",
        "fork",
        "gollum",
        "issue_comment",
        "issues",
        "label",
        "merge_group",
        "milestone",
        "page_build",
        "project",
        "project_card",
        "project_column",
        "public",
        "pull_request",
        "pull_request_review",
        "pull_request_review_comment",
        "pull_request_target",
        "push",
        "registry_package",
        "release",
        "repository_dispatch",
        "schedule",
        "status",
        "watch",
        "workflow_call",
        "workflow_dispatch",
        "workflow_run",
    }
    found: set[str] = set()
    if value:
        found.update(token for token in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", value) if token in known)
        return frozenset(found)
    end = _section_end(lines, index, 0)
    for line in lines[index + 1 : end]:
        parsed = _key(line, 2)
        if parsed and parsed[0] in known:
            found.add(parsed[0])
    return frozenset(found)


def _workflow_name(lines: Sequence[str]) -> str | None:
    index = _top_key_index(lines, "name")
    if index is None:
        return None
    value = (_key(lines[index], 0) or ("", ""))[1].strip().strip("\"'")
    return value or None


def _permissions(lines: Sequence[str], indent: int, start: int, end: int) -> Mapping[str, str] | None:
    for index in range(start, end):
        parsed = _key(lines[index], indent)
        if parsed and parsed[0] == "permissions":
            return _mapping_at(lines, index, indent)
    return None


def _steps(lines: Sequence[str], job_id: str, start: int, end: int) -> tuple[Step, ...]:
    steps_index: int | None = None
    for index in range(start + 1, end):
        parsed = _key(lines[index], 4)
        if parsed and parsed[0] == "steps":
            steps_index = index
            break
    if steps_index is None:
        return ()
    starts = [
        index
        for index in range(steps_index + 1, end)
        if _is_content(lines[index])
        and _indent(lines[index]) == 6
        and lines[index].lstrip().startswith("-")
    ]
    result: list[Step] = []
    for ordinal, step_start in enumerate(starts, 1):
        step_end = starts[ordinal] if ordinal < len(starts) else end
        block = tuple(lines[step_start:step_end])
        name: str | None = None
        first = block[0].lstrip()[1:].strip()
        if first.startswith("name:"):
            name = first.split(":", 1)[1].strip().strip("\"'")
        if name is None:
            for line in block[1:]:
                parsed = _key(line, 8)
                if parsed and parsed[0] == "name":
                    name = parsed[1].strip().strip("\"'")
                    break
        subject_name = _label(name or "", f"step-{ordinal}")
        result.append(
            Step(
                job_id=job_id,
                ordinal=ordinal,
                subject=f"job={job_id};step={subject_name}",
                start=step_start,
                end=step_end,
                lines=block,
            )
        )
    return tuple(result)


def _jobs(lines: Sequence[str]) -> tuple[Job, ...]:
    jobs_index = _top_key_index(lines, "jobs")
    if jobs_index is None:
        return ()
    jobs_end = _section_end(lines, jobs_index, 0)
    starts: list[tuple[int, str]] = []
    for index in range(jobs_index + 1, jobs_end):
        parsed = _key(lines[index], 2)
        if parsed:
            starts.append((index, _label(parsed[0], f"job-{len(starts) + 1}")))
    result: list[Job] = []
    for ordinal, (job_start, job_id) in enumerate(starts):
        job_end = starts[ordinal + 1][0] if ordinal + 1 < len(starts) else jobs_end
        result.append(
            Job(
                job_id=job_id,
                start=job_start,
                end=job_end,
                lines=tuple(lines[job_start:job_end]),
                permissions=_permissions(lines, 4, job_start + 1, job_end) or {},
                steps=_steps(lines, job_id, job_start, job_end),
            )
        )
    return tuple(result)


def _run_chunks(lines: Sequence[str], jobs: Sequence[Job]) -> tuple[list[tuple[str, str, int]], frozenset[int]]:
    chunks: list[tuple[str, str, int]] = []
    indexes: set[int] = set()
    for job in jobs:
        for step in job.steps:
            for index in range(step.start, step.end):
                stripped = lines[index].lstrip(" ")
                parsed = _key(lines[index], 8)
                if stripped.startswith("- run:"):
                    raw_value = stripped[len("- run:") :].lstrip()
                elif parsed and parsed[0] == "run":
                    raw_value = parsed[1]
                else:
                    continue
                content: list[str] = []
                if raw_value.strip() not in {"|", "|-", "|+", ">", ">-", ">+"}:
                    content.append(raw_value)
                run_indent = _indent(lines[index])
                for child in range(index + 1, step.end):
                    if _is_content(lines[child]) and _indent(lines[child]) <= run_indent:
                        break
                    indexes.add(child)
                    content.append(lines[child].lstrip(" "))
                chunks.append((step.subject, "\n".join(content), index + 1))
    return chunks, frozenset(indexes)


def _structural_findings(workflow: Workflow) -> list[Finding]:
    """Reject YAML features outside the scanner's canonical, reviewed subset.

    This is a deliberate fail-closed boundary. GitHub accepts a broader YAML
    language, including anchors and flow-style step mappings. The local static
    scanner must never partially interpret those constructs and report PASS.
    """

    findings: list[Finding] = []
    top_keys: dict[str, int] = {}
    jobs_index = _top_key_index(workflow.lines, "jobs")
    jobs_end = (
        _section_end(workflow.lines, jobs_index, 0)
        if jobs_index is not None
        else len(workflow.lines)
    )
    for index, line in enumerate(workflow.lines):
        if index in workflow.run_line_indexes or not _is_content(line):
            continue
        leading = line[: len(line) - len(line.lstrip(" \t"))]
        if "\t" in leading:
            findings.append(
                _finding("KFM-WF-001", workflow.path, f"yaml-line={index + 1}", "TAB_INDENTATION_DENIED", index + 1)
            )
            continue
        stripped = _strip_inline_comment(line.lstrip(" "))
        indent = _indent(line)
        key_prefix = stripped.split(":", 1)[0] if ":" in stripped else ""
        if key_prefix.startswith(("'", '"')):
            allowed_quoted_on = (
                indent == 0
                and key_prefix in {"'on'", '"on"'}
                and "\\" not in key_prefix
            )
            if not allowed_quoted_on:
                findings.append(
                    _finding(
                        "KFM-WF-001",
                        workflow.path,
                        f"yaml-line={index + 1}",
                        "QUOTED_OR_ESCAPED_MAPPING_KEY_DENIED",
                        index + 1,
                    )
                )
        if re.match(r"^-\s*['\"][^'\"]+['\"]\s*:", stripped):
            findings.append(
                _finding(
                    "KFM-WF-001",
                    workflow.path,
                    f"yaml-line={index + 1}",
                    "QUOTED_STEP_KEY_DENIED",
                    index + 1,
                )
            )
        parsed = _key(line, 0)
        if parsed:
            key = parsed[0]
            if key in top_keys:
                findings.append(
                    _finding(
                        "KFM-WF-001",
                        workflow.path,
                        f"yaml-line={index + 1}",
                        f"DUPLICATE_TOP_LEVEL_KEY:{key}",
                        index + 1,
                    )
                )
            top_keys[key] = index + 1
        if stripped in {"---", "..."} or stripped.startswith("%YAML"):
            findings.append(
                _finding("KFM-WF-001", workflow.path, f"yaml-line={index + 1}", "YAML_DOCUMENT_DIRECTIVE_DENIED", index + 1)
            )
        projection = _unquoted_projection(line)
        if re.match(r"^\s*!<?[A-Za-z0-9_./:-]+", projection) or re.search(
            r":\s*!<?[A-Za-z0-9_./:-]+", projection
        ):
            findings.append(
                _finding("KFM-WF-001", workflow.path, f"yaml-line={index + 1}", "YAML_TAG_DENIED", index + 1)
            )
        if re.search(r"(?:^|[\s,:\[{])(?:&|\*)[A-Za-z0-9_-]+(?:\b|$)", projection):
            findings.append(
                _finding("KFM-WF-001", workflow.path, f"yaml-line={index + 1}", "YAML_ANCHOR_OR_ALIAS_DENIED", index + 1)
            )
        if re.match(r"^\s*<<\s*:", projection):
            findings.append(
                _finding("KFM-WF-001", workflow.path, f"yaml-line={index + 1}", "YAML_MERGE_KEY_DENIED", index + 1)
            )
        if re.match(r"^\s*-\s*\{", projection):
            findings.append(
                _finding("KFM-WF-001", workflow.path, f"yaml-line={index + 1}", "FLOW_STYLE_STEP_DENIED", index + 1)
            )
        parsed_any = _key(line, indent)
        if parsed_any and parsed_any[1].strip() in {"|", "|-", "|+", ">", ">-", ">+"}:
            if parsed_any[0] not in {"path", "run", "cache-dependency-path"}:
                findings.append(
                    _finding(
                        "KFM-WF-001",
                        workflow.path,
                        f"yaml-line={index + 1}",
                        "NON_RUN_BLOCK_SCALAR_DENIED",
                        index + 1,
                    )
                )
        if "\\" in _strip_inline_comment(line) and not (
            index in workflow.run_line_indexes or (parsed_any and parsed_any[0] == "run")
        ):
            findings.append(
                _finding(
                    "KFM-WF-001",
                    workflow.path,
                    f"yaml-line={index + 1}",
                    "ESCAPED_SECURITY_SCALAR_DENIED",
                    index + 1,
                )
            )
        if jobs_index is not None and jobs_index < index < jobs_end:
            if re.match(r"^(?:permissions|runs-on|steps|timeout-minutes)\s*:", stripped) and indent != 4:
                findings.append(
                    _finding(
                        "KFM-WF-001",
                        workflow.path,
                        f"yaml-line={index + 1}",
                        "CANONICAL_JOB_KEY_INDENTATION_REQUIRED",
                        index + 1,
                    )
                )
            if re.match(
                r"^-\s*(?:env|id|if|name|run|shell|uses|with|working-directory)\s*:",
                stripped,
            ) and indent != 6:
                findings.append(
                    _finding(
                        "KFM-WF-001",
                        workflow.path,
                        f"yaml-line={index + 1}",
                        "CANONICAL_STEP_INDENTATION_REQUIRED",
                        index + 1,
                    )
                )

    if jobs_index is None:
        findings.append(_finding("KFM-WF-001", workflow.path, "jobs", "JOBS_MAPPING_REQUIRED", 1))
    else:
        jobs_value = (_key(workflow.lines[jobs_index], 0) or ("", ""))[1].strip()
        if jobs_value:
            findings.append(
                _finding("KFM-WF-001", workflow.path, "jobs", "BLOCK_STYLE_JOBS_MAPPING_REQUIRED", jobs_index + 1)
            )
        has_job_content = any(
            _is_content(line)
            for line in workflow.lines[jobs_index + 1 : jobs_end]
        )
        if has_job_content and not workflow.jobs:
            findings.append(
                _finding(
                    "KFM-WF-001",
                    workflow.path,
                    "jobs",
                    "CANONICAL_JOB_INDENTATION_REQUIRED",
                    jobs_index + 1,
                )
            )
        for job in workflow.jobs:
            parsed = _key(workflow.lines[job.start], 2)
            if not parsed or parsed[1].strip():
                findings.append(
                    _finding(
                        "KFM-WF-001",
                        workflow.path,
                        f"job={job.job_id}",
                        "BLOCK_STYLE_JOB_MAPPING_REQUIRED",
                        job.start + 1,
                    )
                )
    return findings


def _relative_workflow_path(path: Path, root: Path) -> str:
    resolved_root = root.resolve()
    resolved = path.resolve(strict=False)
    try:
        relative = resolved.relative_to(resolved_root).as_posix()
    except ValueError as exc:
        raise ValueError("workflow path escapes repository root") from exc
    parsed = PurePosixPath(relative)
    if parsed.parts[:2] != (".github", "workflows") or parsed.suffix not in {".yml", ".yaml"}:
        raise ValueError("workflow path is outside .github/workflows or has an unsupported suffix")
    return relative


def _load_workflow(path: Path, root: Path) -> tuple[Workflow | None, list[Finding]]:
    try:
        relative = _relative_workflow_path(path, root)
    except ValueError:
        relative = path.name
        return None, [_finding("KFM-WF-001", relative, "workflow-input", "PATH_OUTSIDE_BOUNDARY", 0)]
    try:
        if path.is_symlink():
            raise BaselineError("SYMLINK_DENIED")
        if not path.is_file():
            raise BaselineError("NOT_REGULAR_FILE")
        if path.stat().st_size > MAX_WORKFLOW_BYTES:
            raise BaselineError("FILE_TOO_LARGE")
        text = path.read_text(encoding="utf-8")
        if "\x00" in text:
            raise BaselineError("NUL_DENIED")
    except UnicodeDecodeError:
        return None, [_finding("KFM-WF-001", relative, "workflow-input", "UTF8_REQUIRED", 0)]
    except OSError:
        return None, [_finding("KFM-WF-001", relative, "workflow-input", "READ_ERROR", 0)]
    except BaselineError as exc:
        return None, [_finding("KFM-WF-001", relative, "workflow-input", str(exc), 0)]
    lines = tuple(text.splitlines())
    jobs = _jobs(lines)
    _, run_indexes = _run_chunks(lines, jobs)
    permissions_index = _top_key_index(lines, "permissions")
    top_permissions = (
        _mapping_at(lines, permissions_index, 0) if permissions_index is not None else None
    )
    return (
        Workflow(
            path=relative,
            absolute_path=path,
            text=text,
            lines=lines,
            name=_workflow_name(lines),
            triggers=_triggers(lines),
            top_permissions=top_permissions,
            jobs=jobs,
            run_line_indexes=run_indexes,
        ),
        [],
    )


def _uses_entries(workflow: Workflow) -> list[tuple[int, str, str]]:
    result: list[tuple[int, str, str]] = []
    ordinal = 0
    for index, line in enumerate(workflow.lines):
        if index in workflow.run_line_indexes or not _is_content(line):
            continue
        match = re.match(r"^\s*(?:-\s*)?uses:\s*([^\s#]+)", line)
        if not match:
            continue
        ordinal += 1
        result.append((index + 1, match.group(1).strip("\"'"), f"uses={ordinal}"))
    return result


def _checkout_steps(workflow: Workflow) -> list[Step]:
    result: list[Step] = []
    for job in workflow.jobs:
        for step in job.steps:
            if re.search(
                r"(?:^|\n)\s*(?:-\s*)?uses:\s*actions/checkout@",
                "\n".join(step.lines),
                re.IGNORECASE,
            ):
                result.append(step)
    return result


def _checkout_disables_persisted_credentials(step: Step) -> bool:
    for line in step.lines:
        if not _is_content(line):
            continue
        if re.match(
            r"^\s*persist-credentials:\s*(?:false|\"false\"|'false')\s*(?:#.*)?$",
            line,
        ):
            return True
        if re.search(
            r"\bwith:\s*\{[^}]*\bpersist-credentials\s*:\s*(?:false|\"false\"|'false')(?:\s*,|\s*})",
            line,
        ):
            return True
    return False


def _all_write_permissions(workflow: Workflow) -> list[tuple[str, str, int]]:
    result: list[tuple[str, str, int]] = []
    top = workflow.top_permissions or {}
    for scope, value in top.items():
        if value in {"write", "write-all"} or scope == "*" and value == "write-all":
            result.append(("workflow", scope, (_top_key_index(workflow.lines, "permissions") or 0) + 1))
    for job in workflow.jobs:
        for scope, value in job.permissions.items():
            if value in {"write", "write-all"} or scope == "*" and value == "write-all":
                result.append((f"job={job.job_id}", scope, job.start + 1))
    return result


def _scan_workflow(workflow: Workflow) -> list[Finding]:
    findings: list[Finding] = _structural_findings(workflow)
    path = workflow.path
    if workflow.name is None:
        findings.append(_finding("KFM-WF-002", path, "workflow-name", "NAME_MISSING", 1))

    for line, reference, subject in _uses_entries(workflow):
        if reference.startswith("./"):
            continue
        if reference.startswith("docker://"):
            image = reference[len("docker://") :]
            if not re.search(r"@sha256:[0-9a-f]{64}$", image):
                findings.append(_finding("KFM-WF-005", path, subject, image, line))
            continue
        if "@" not in reference or not SHA256_RE.fullmatch(reference.rsplit("@", 1)[1]):
            findings.append(_finding("KFM-WF-004", path, subject, reference, line))

    for job in workflow.jobs:
        container_indexes: list[int] = []
        service_indexes: list[int] = []
        for index in range(job.start + 1, job.end):
            parsed = _key(workflow.lines[index], 4)
            if not parsed:
                continue
            if parsed[0] == "container":
                container_indexes.append(index)
                image = parsed[1].strip().strip("\"'")
                if image and not re.search(r"@sha256:[0-9a-f]{64}$", image):
                    findings.append(
                        _finding("KFM-WF-005", path, f"job={job.job_id};container", image, index + 1)
                    )
            elif parsed[0] == "services":
                service_indexes.append(index)
        for container_index in container_indexes:
            if (_key(workflow.lines[container_index], 4) or ("", ""))[1].strip():
                continue
            end = _section_end(workflow.lines, container_index, 4)
            for index in range(container_index + 1, end):
                parsed = _key(workflow.lines[index], 6)
                if parsed and parsed[0] == "image":
                    image = parsed[1].strip().strip("\"'")
                    if not re.search(r"@sha256:[0-9a-f]{64}$", image):
                        findings.append(
                            _finding("KFM-WF-005", path, f"job={job.job_id};container", image, index + 1)
                        )
        for services_index in service_indexes:
            services_end = _section_end(workflow.lines, services_index, 4)
            for index in range(services_index + 1, services_end):
                parsed = _key(workflow.lines[index], 8)
                if parsed and parsed[0] == "image":
                    image = parsed[1].strip().strip("\"'")
                    if not re.search(r"@sha256:[0-9a-f]{64}$", image):
                        findings.append(
                            _finding(
                                "KFM-WF-005",
                                path,
                                f"job={job.job_id};service-line={index + 1}",
                                image,
                                index + 1,
                            )
                        )

    for step in _checkout_steps(workflow):
        if not _checkout_disables_persisted_credentials(step):
            findings.append(
                _finding("KFM-WF-006", path, step.subject, "PERSIST_CREDENTIALS_NOT_FALSE", step.start + 1)
            )

    if workflow.top_permissions is None:
        findings.append(
            _finding("KFM-WF-007", path, "workflow-permissions", "PERMISSIONS_MISSING", 1)
        )

    writes = _all_write_permissions(workflow)
    for owner, scope, line in writes:
        if owner == "workflow":
            findings.append(
                _finding("KFM-WF-008", path, f"scope={scope}", "WORKFLOW_SCOPE_WRITE", line)
            )
        if scope not in WRITE_SCOPE_ALLOWLIST:
            findings.append(
                _finding("KFM-WF-009", path, f"{owner};scope={scope}", scope, line)
            )

    for owner, scope, line in writes:
        if scope != "pull-requests":
            continue
        if not workflow.triggers or not workflow.triggers.issubset(TRUSTED_PULL_REQUEST_WRITE_TRIGGERS):
            findings.append(
                _finding(
                    "KFM-WF-010",
                    path,
                    owner,
                    ",".join(sorted(workflow.triggers)) or "TRIGGER_UNKNOWN",
                    line,
                )
            )

    if "pull_request_target" in workflow.triggers:
        for owner, scope, line in writes:
            findings.append(
                _finding("KFM-WF-011", path, f"{owner};scope={scope}", scope, line)
            )
        for step in _checkout_steps(workflow):
            block = "\n".join(step.lines)
            if not re.search(
                r"(?:^|\n)\s*ref:\s*[\"']?\$\{\{\s*github\.event\.pull_request\.base\.sha\s*\}\}[\"']?\s*(?:#.*)?$",
                block,
                re.MULTILINE,
            ):
                findings.append(
                    _finding("KFM-WF-012", path, step.subject, "TRUSTED_BASE_REF_REQUIRED", step.start + 1)
                )
        occurrence = 0
        for index, line in enumerate(workflow.lines):
            if line.lstrip().startswith("#"):
                continue
            if PULL_REQUEST_HEAD_RE.search(_normalize_expression_properties(line)):
                occurrence += 1
                findings.append(
                    _finding(
                        "KFM-WF-013",
                        path,
                        f"head-reference={occurrence}",
                        line.strip(),
                        index + 1,
                    )
                )

    for job in workflow.jobs:
        caller_job = any(
            (parsed := _key(workflow.lines[index], 4)) is not None
            and parsed[0] == "uses"
            for index in range(job.start + 1, job.end)
        )
        if caller_job:
            continue
        runs_on_parts: list[str] = []
        runs_on_value: str | None = None
        for offset, line in enumerate(job.lines):
            parsed = _key(line, 4)
            if parsed and parsed[0] == "runs-on":
                runs_on_value = parsed[1].strip()
                runs_on_parts.append(parsed[1])
                absolute = job.start + offset
                for child in range(absolute + 1, job.end):
                    if _is_content(workflow.lines[child]) and _indent(workflow.lines[child]) <= 4:
                        break
                    runs_on_parts.append(workflow.lines[child])
                break
        runner_text = "\n".join(runs_on_parts)
        normalized_runner = runner_text.replace('"', " ").replace("'", " ")
        scalar_runner = (runs_on_value or "").strip().strip("\"'")
        if (
            not runs_on_value
            or runs_on_value.startswith(('{', '['))
            or scalar_runner not in GITHUB_HOSTED_RUNNERS
        ):
            findings.append(
                _finding("KFM-WF-014", path, f"job={job.job_id}", "NON_GITHUB_HOSTED_RUNNER_DENIED", job.start + 1)
            )
        if runs_on_value == "" and any(
            _key(workflow.lines[index], 6) is not None
            for index in range(job.start + 1, job.end)
        ):
            findings.append(
                _finding("KFM-WF-014", path, f"job={job.job_id}", "RUNNER_GROUP_MAPPING_DENIED", job.start + 1)
            )
        if "${{" in runner_text:
            findings.append(
                _finding("KFM-WF-014", path, f"job={job.job_id}", "DYNAMIC_RUNNER_DENIED", job.start + 1)
            )
        if re.search(r"(?i)(?:^|[\s,\[])self-hosted(?:[\s,\]]|$)", normalized_runner):
            findings.append(
                _finding("KFM-WF-014", path, f"job={job.job_id}", runner_text, job.start + 1)
            )

    for index, line in enumerate(workflow.lines):
        if index in workflow.run_line_indexes or line.lstrip().startswith("#"):
            continue
        if re.search(r"\bsecrets:\s*(?:inherit\b|\"inherit\"|'inherit')", line):
            findings.append(
                _finding("KFM-WF-015", path, f"secrets-inherit={index + 1}", "SECRETS_INHERIT", index + 1)
            )

    env_index = _top_key_index(workflow.lines, "env")
    if env_index is not None:
        env_end = _section_end(workflow.lines, env_index, 0)
        for index in range(env_index, env_end):
            normalized_expression = _normalize_expression_properties(workflow.lines[index])
            if re.search(r"\$\{\{[^}]*\bsecrets\s*\.", normalized_expression):
                findings.append(
                    _finding("KFM-WF-016", path, f"global-env={index + 1}", "GLOBAL_SECRET", index + 1)
                )

    run_chunks, _ = _run_chunks(workflow.lines, workflow.jobs)
    for subject, content, line in run_chunks:
        normalized_content = _normalize_expression_properties(content)
        tainted = tuple(UNTRUSTED_SHELL_EXPRESSION_RE.finditer(normalized_content))
        for ordinal, match in enumerate(tainted, 1):
            findings.append(
                _finding(
                    "KFM-WF-017",
                    path,
                    f"{subject};expression={ordinal}",
                    match.group(0),
                    line,
                )
            )
        if re.search(r"(?im)\b(?:curl|wget)\b[^\n|]*\|\s*(?:ba|z|k)?sh\b", content):
            findings.append(
                _finding("KFM-WF-018", path, subject, "DOWNLOAD_PIPE_TO_SHELL", line)
            )
        deprecated = sorted(set(re.findall(r"::(?:set-output|add-path|save-state)\b", content)))
        for command in deprecated:
            findings.append(_finding("KFM-WF-019", path, f"{subject};command={command[2:]}", command, line))

    for job in workflow.jobs:
        caller_job = any(
            (parsed := _key(workflow.lines[index], 4)) is not None
            and parsed[0] == "uses"
            for index in range(job.start + 1, job.end)
        )
        if caller_job:
            continue
        timeout_values: list[tuple[str, int]] = []
        for offset, line in enumerate(job.lines):
            parsed = _key(line, 4)
            if parsed and parsed[0] == "timeout-minutes":
                timeout_values.append((parsed[1].strip().strip("\"'"), job.start + offset + 1))
        if len(timeout_values) != 1:
            evidence = "TIMEOUT_MISSING" if not timeout_values else "TIMEOUT_DUPLICATE"
            findings.append(_finding("KFM-WF-020", path, f"job={job.job_id}", evidence, job.start + 1))
        else:
            value, line = timeout_values[0]
            try:
                bounded = int(value)
            except ValueError:
                bounded = 0
            if not 1 <= bounded <= 60:
                findings.append(_finding("KFM-WF-020", path, f"job={job.job_id}", value, line))

    return findings


def discover_workflows(repo_root: Path) -> tuple[Path, ...]:
    workflow_root = repo_root / ".github/workflows"
    if not workflow_root.is_dir():
        return ()
    return tuple(sorted((*workflow_root.glob("*.yml"), *workflow_root.glob("*.yaml"))))


def scan(repo_root: Path, workflow_paths: Sequence[Path] | None = None) -> tuple[tuple[Finding, ...], int]:
    root = repo_root.resolve()
    paths = tuple(workflow_paths) if workflow_paths is not None else discover_workflows(root)
    workflows: list[Workflow] = []
    findings: list[Finding] = []
    for path in paths:
        candidate = path if path.is_absolute() else root / path
        workflow, input_findings = _load_workflow(candidate, root)
        findings.extend(input_findings)
        if workflow is not None:
            workflows.append(workflow)
            findings.extend(_scan_workflow(workflow))

    selected_relative = {workflow.path for workflow in workflows}
    name_workflows = list(workflows)
    if workflow_paths is not None:
        for path in discover_workflows(root):
            try:
                relative = _relative_workflow_path(path, root)
            except ValueError:
                continue
            if relative in selected_relative:
                continue
            workflow, _input_findings = _load_workflow(path, root)
            if workflow is not None:
                name_workflows.append(workflow)

    by_name: dict[str, list[Workflow]] = {}
    for workflow in name_workflows:
        if workflow.name:
            by_name.setdefault(workflow.name.casefold(), []).append(workflow)
    for normalized, members in sorted(by_name.items()):
        if len(members) < 2:
            continue
        paths_in_group = ",".join(sorted(item.path for item in members))
        for workflow in members:
            if workflow_paths is not None and workflow.path not in selected_relative:
                continue
            findings.append(
                _finding("KFM-WF-003", workflow.path, "workflow-name", normalized + "\0" + paths_in_group, 1)
            )
    unique = sorted(set(findings))
    if len(unique) > MAX_FINDINGS:
        raise BaselineError("finding budget exceeded")
    return tuple(unique), len(workflows)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise BaselineError(f"duplicate baseline key: {key}")
        result[key] = value
    return result


def _finite_constant(value: str) -> object:
    raise BaselineError(f"non-finite baseline number: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise BaselineError(f"non-finite baseline number: {value}")
    return parsed


def load_baseline(path: Path) -> dict[str, dict[str, object]]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BASELINE_BYTES:
        raise BaselineError("baseline is missing, unsafe, or too large")
    try:
        data = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_finite_constant,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, BaselineError) as exc:
        raise BaselineError(f"baseline JSON is invalid: {type(exc).__name__}") from exc
    exact_keys = {
        "authority",
        "closure_ref",
        "entries",
        "generated_from_ref",
        "non_effects",
        "owner",
        "schema_version",
    }
    if not isinstance(data, dict) or set(data) != exact_keys:
        raise BaselineError("baseline root does not match the v1 contract")
    if data["schema_version"] != BASELINE_VERSION or data["authority"] != "implementation_waivers_only":
        raise BaselineError("baseline identity or authority is invalid")
    if not isinstance(data["owner"], str) or not data["owner"]:
        raise BaselineError("baseline owner is missing")
    if not isinstance(data["closure_ref"], str) or not data["closure_ref"]:
        raise BaselineError("baseline closure_ref is missing")
    expected_non_effects = [
        "does_not_define_or_amend_rules",
        "does_not_waive_invariant_findings",
        "does_not_authorize_workflow_or_repository_writes",
    ]
    if data["non_effects"] != expected_non_effects:
        raise BaselineError("baseline non_effects are invalid")
    entries = data["entries"]
    if not isinstance(entries, list) or len(entries) > MAX_FINDINGS:
        raise BaselineError("baseline entries must be a bounded array")
    exact_entry_keys = {
        "evidence_sha256",
        "expires_on",
        "fingerprint",
        "path",
        "rule_id",
        "subject",
    }
    result: dict[str, dict[str, object]] = {}
    ordered: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict) or set(entry) != exact_entry_keys:
            raise BaselineError(f"baseline entry {index} does not match the v1 contract")
        rule_id = entry.get("rule_id")
        if not isinstance(rule_id, str) or rule_id not in RULE_BY_ID:
            raise BaselineError(f"baseline entry {index} has an unknown rule")
        if not RULE_BY_ID[rule_id].baseline_allowed:
            raise BaselineError(f"baseline entry {index} attempts to waive an invariant")
        fingerprint = entry.get("fingerprint")
        if not isinstance(fingerprint, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", fingerprint):
            raise BaselineError(f"baseline entry {index} has an invalid fingerprint")
        if fingerprint in result:
            raise BaselineError(f"duplicate baseline fingerprint: {fingerprint}")
        for field in ("evidence_sha256", "expires_on", "path", "subject"):
            if not isinstance(entry.get(field), str) or not entry[field]:
                raise BaselineError(f"baseline entry {index} has an invalid {field}")
        try:
            date.fromisoformat(str(entry["expires_on"]))
        except ValueError as exc:
            raise BaselineError(f"baseline entry {index} has an invalid expires_on") from exc
        ordered.append(fingerprint)
        result[fingerprint] = entry
    if ordered != sorted(ordered):
        raise BaselineError("baseline entries are not sorted by fingerprint")
    return result


def candidate_baseline(
    findings: Sequence[Finding],
    *,
    owner: str,
    closure_ref: str,
    generated_from_ref: str,
    expires_on: str,
) -> dict[str, object]:
    date.fromisoformat(expires_on)
    entries = [
        {
            "evidence_sha256": finding.evidence_sha256,
            "expires_on": expires_on,
            "fingerprint": finding.fingerprint,
            "path": finding.path,
            "rule_id": finding.rule_id,
            "subject": finding.subject,
        }
        for finding in findings
        if RULE_BY_ID[finding.rule_id].baseline_allowed
    ]
    entries.sort(key=lambda item: str(item["fingerprint"]))
    return {
        "authority": "implementation_waivers_only",
        "closure_ref": closure_ref,
        "entries": entries,
        "generated_from_ref": generated_from_ref,
        "non_effects": [
            "does_not_define_or_amend_rules",
            "does_not_waive_invariant_findings",
            "does_not_authorize_workflow_or_repository_writes",
        ],
        "owner": owner,
        "schema_version": BASELINE_VERSION,
    }


def evaluate(
    findings: Sequence[Finding],
    workflow_count: int,
    baseline: Mapping[str, Mapping[str, object]],
    *,
    as_of: date | None = None,
    selected_paths: frozenset[str] | None = None,
) -> tuple[int, dict[str, object]]:
    today = as_of or date.today()
    observed = {finding.fingerprint: finding for finding in findings}
    applicable_baseline = {
        fingerprint: entry
        for fingerprint, entry in baseline.items()
        if selected_paths is None or entry.get("path") in selected_paths
    }
    stale = sorted(set(applicable_baseline) - set(observed))
    baselined: set[str] = set()
    expired: set[str] = set()
    metadata_mismatch: set[str] = set()
    invariant: set[str] = set()
    new_drift: set[str] = set()
    for finding in findings:
        rule = RULE_BY_ID[finding.rule_id]
        entry = applicable_baseline.get(finding.fingerprint)
        if not rule.baseline_allowed:
            invariant.add(finding.fingerprint)
        elif entry is None:
            new_drift.add(finding.fingerprint)
        elif any(
            entry.get(field) != getattr(finding, field)
            for field in ("rule_id", "path", "subject", "evidence_sha256", "fingerprint")
        ):
            metadata_mismatch.add(finding.fingerprint)
        elif date.fromisoformat(str(entry["expires_on"])) < today:
            expired.add(finding.fingerprint)
        else:
            baselined.add(finding.fingerprint)

    if metadata_mismatch:
        outcome, exit_code = "ERROR_VALIDATOR", 2
    elif invariant or stale:
        outcome, exit_code = "FAIL_INVARIANT", 1
    elif expired:
        outcome, exit_code = "HOLD_UNRESOLVED", 1
    elif new_drift:
        outcome, exit_code = "FAIL_NEW_DRIFT", 1
    else:
        outcome, exit_code = "PASS", 0

    rendered: list[dict[str, object]] = []
    for finding in findings:
        fingerprint = finding.fingerprint
        if fingerprint in invariant:
            disposition = "FAIL_INVARIANT"
        elif fingerprint in new_drift:
            disposition = "FAIL_NEW_DRIFT"
        elif fingerprint in expired:
            disposition = "HOLD_EXPIRED_BASELINE"
        elif fingerprint in metadata_mismatch:
            disposition = "ERROR_BASELINE_MISMATCH"
        else:
            disposition = "BASELINED_WARNING"
        rendered.append(finding.as_dict(disposition))
    report = {
        "authority": {
            "approves_review": False,
            "authorizes_repository_write": False,
            "authorizes_release": False,
            "deploys": False,
            "publishes": False,
        },
        "baseline": {
            "applicable_count": len(applicable_baseline),
            "expired_count": len(expired),
            "metadata_mismatch_count": len(metadata_mismatch),
            "stale_fingerprints": stale,
        },
        "counts": {
            "baselined_warning": len(baselined),
            "fail_invariant": len(invariant),
            "fail_new_drift": len(new_drift),
            "finding": len(findings),
        },
        "findings": rendered,
        "outcome": outcome,
        "rule_count": len(RULES),
        "schema_version": REPORT_VERSION,
        "workflow_count": workflow_count,
    }
    return exit_code, report


def _text_report(report: Mapping[str, object]) -> str:
    counts = report["counts"]
    baseline = report["baseline"]
    assert isinstance(counts, Mapping) and isinstance(baseline, Mapping)
    return (
        f"{report['outcome']}: {report['workflow_count']} workflows; "
        f"{counts['fail_invariant']} invariant; {counts['fail_new_drift']} new drift; "
        f"{counts['baselined_warning']} baselined warnings; "
        f"{len(baseline['stale_fingerprints'])} stale baseline entries"
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--no-baseline", action="store_true")
    parser.add_argument("--workflow", action="append", type=Path, default=[])
    parser.add_argument("--format", choices=("json", "text"), default="json")
    parser.add_argument("--emit-baseline", action="store_true")
    parser.add_argument("--baseline-owner", default="@bartytime4life")
    parser.add_argument("--closure-ref", default="current-change:workflow-security-hardening")
    parser.add_argument("--generated-from-ref", default="worktree")
    parser.add_argument("--expires-on", default="2026-11-10")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        findings, workflow_count = scan(
            args.repo_root,
            tuple(args.workflow) if args.workflow else None,
        )
        if args.emit_baseline:
            if any(not RULE_BY_ID[finding.rule_id].baseline_allowed for finding in findings):
                raise BaselineError("cannot emit a baseline while invariant findings exist")
            payload = candidate_baseline(
                findings,
                owner=args.baseline_owner,
                closure_ref=args.closure_ref,
                generated_from_ref=args.generated_from_ref,
                expires_on=args.expires_on,
            )
            print(json.dumps(payload, indent=2, sort_keys=True) + "\n", end="")
            return 0
        baseline = {} if args.no_baseline else load_baseline(args.baseline)
        selected_paths = None
        if args.workflow:
            selected_paths = frozenset(
                _relative_workflow_path(
                    path if path.is_absolute() else args.repo_root / path,
                    args.repo_root,
                )
                for path in args.workflow
            )
        exit_code, report = evaluate(
            findings,
            workflow_count,
            baseline,
            selected_paths=selected_paths,
        )
    except (BaselineError, OSError, UnicodeError, ValueError) as exc:
        report = {
            "authority": {"authorizes_repository_write": False},
            "error": type(exc).__name__,
            "outcome": "ERROR_VALIDATOR",
            "rule_count": len(RULES),
            "schema_version": REPORT_VERSION,
        }
        exit_code = 2
    if args.format == "text":
        print(_text_report(report) if "counts" in report else f"ERROR_VALIDATOR: {report['error']}")
    else:
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
