#!/usr/bin/env python3
"""Validate adopted KFM repository placement with an exact drift ratchet.

The validator reads the Git index and repository-owned governance projections.
It is deterministic and no-network. Its baseline records inherited findings by
exact fingerprint only: it does not define rules, create path authority, approve
migration, authorize deletion, or grant release or publication status.
"""

from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import unicodedata
import zlib
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

REPORT_VERSION = "kfm.repository-topology-report.v1"
BASELINE_VERSION = "kfm.repository-topology-baseline.v1"
DEFAULT_BASELINE = Path(__file__).with_name("repository_topology_baseline.json")
BASELINE_REPOSITORY_PATH = "tools/validators/directory_governance/repository_topology_baseline.json"
BOOTSTRAP_BASE_SHA = "bff35f5ddf00ef623eacf96be13a743e134f482f"
ADOPTED_SHA256 = "44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e"
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_SELECTED_BLOB_BYTES = 256 * 1024 * 1024
MAX_EVIDENCE_BYTES = 16 * 1024 * 1024
MAX_BASELINE_EVIDENCE_BYTES = 32 * 1024 * 1024
MAX_EVIDENCE_MEMBERS = 20_000
MAX_EVIDENCE_MEMBER_BYTES = 16 * 1024
MAX_FINDINGS = 2_000
GIT_TIMEOUT_SECONDS = 30


@dataclass(frozen=True)
class Rule:
    rule_id: str
    title: str
    baseline_allowed: bool


RULES: tuple[Rule, ...] = (
    Rule("KFM-TOPO-001", "Tracked paths use safe, portable grammar", True),
    Rule("KFM-TOPO-002", "Every tracked top-level directory is registered", False),
    Rule("KFM-TOPO-003", "Repository-root files use the bounded allowlist", True),
    Rule("KFM-TOPO-004", "Deprecated and held roots do not expand silently", True),
    Rule("KFM-TOPO-005", "Artifacts use only the four compatibility lanes", True),
    Rule("KFM-TOPO-006", "Known scope slugs do not create unregistered aliases", True),
    Rule("KFM-TOPO-007", "Tracked paths are unique under NFC case-folding", True),
    Rule("KFM-TOPO-008", "Known collection spellings do not create parallel homes", True),
    Rule("KFM-TOPO-009", "Leaf directories are materialized, not speculative", True),
    Rule("KFM-TOPO-010", "Data direct children follow the normalized planes", True),
    Rule("KFM-TOPO-011", "Release direct children are object-family first", True),
    Rule("KFM-TOPO-012", "Normative Rego source lives under policy", True),
    Rule("KFM-TOPO-013", "Artifacts contain no trust-shaped family", True),
    Rule("KFM-TOPO-014", "Deployable apps do not read internal lifecycle stores", True),
    Rule("KFM-TOPO-015", "Canonical schema identifiers are unique", False),
    Rule("KFM-TOPO-016", "Human authority identifiers are unique", True),
    Rule("KFM-TOPO-017", "Tracked generated payloads declare provenance", True),
    Rule("KFM-TOPO-018", "Populated policy boundaries have a README", True),
    Rule("KFM-TOPO-019", "Topology enforcement binds to adopted authority", False),
    Rule("KFM-TOPO-020", "Active aliases have explicit closure state", True),
)
RULE_BY_ID = {rule.rule_id: rule for rule in RULES}
if len(RULES) != 20 or len(RULE_BY_ID) != 20:
    raise RuntimeError("repository topology profile must contain exactly 20 unique rules")


ROOT_FILE_ALLOWLIST = frozenset(
    {
        ".editorconfig",
        ".env.example",
        ".gitignore",
        ".pre-commit-config.yaml",
        "AUTHORS.md",
        "CHANGELOG.md",
        "CITATION.cff",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "LICENSE",
        "Makefile",
        "README.md",
        "SECURITY.md",
        "package.json",
        "pnpm-lock.yaml",
        "pnpm-workspace.yaml",
        "pyproject.toml",
    }
)
DATA_CHILDREN = frozenset(
    {
        "pre_raw",
        "raw",
        "work",
        "quarantine",
        "processed",
        "catalog",
        "triplets",
        "receipts",
        "proofs",
        "registry",
        "published",
    }
)
RELEASE_CHILDREN = frozenset(
    {
        "candidates",
        "manifests",
        "promotion_decisions",
        "correction_notices",
        "withdrawal_notices",
        "rollback_cards",
        "signatures",
        "changelog",
    }
)
ARTIFACT_CHILDREN = frozenset({"build", "docs", "qa", "temporary"})
SCOPE_ALIASES = frozenset({"air", "settlement", "transport", "people", "hydro"})
SCOPE_ROOTS = frozenset(
    {
        "connectors",
        "contracts",
        "data",
        "docs",
        "fixtures",
        "packages",
        "pipeline_specs",
        "pipelines",
        "policy",
        "release",
        "runtime",
        "schemas",
        "tests",
        "tools",
    }
)
APP_TEXT_SUFFIXES = frozenset(
    {
        ".bash",
        ".cjs",
        ".conf",
        ".css",
        ".env",
        ".gql",
        ".go",
        ".graphql",
        ".html",
        ".ini",
        ".java",
        ".js",
        ".json",
        ".jsx",
        ".kt",
        ".kts",
        ".mjs",
        ".py",
        ".rs",
        ".scss",
        ".sh",
        ".svelte",
        ".toml",
        ".ts",
        ".tsx",
        ".vue",
        ".xml",
        ".yaml",
        ".yml",
        ".zsh",
    }
)
APP_TEXT_NAMES = frozenset({"Dockerfile", "Makefile"})
WINDOWS_RESERVED = re.compile(r"(?i)^(?:con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?$")
DOC_ID_RE = re.compile(r'^\s*doc_id:\s*["\']?([^"\'\s]+)', re.MULTILINE)
INTERNAL_STORE_RE = re.compile(r"(?:^|[^A-Za-z0-9_])data/(?:raw|work|quarantine|processed)(?:/|\b)")
INTERNAL_STORE_CONSTRUCTION_RE = re.compile(
    r"(?is)(?:"
    r"(?:Path\s*\(\s*)?[\"']data[\"']\s*\)?\s*/\s*[\"'](?:raw|work|quarantine|processed)[\"']"
    r"|(?:path\.)?(?:join|resolve)\s*\(\s*[\"']data[\"']\s*,\s*[\"'](?:raw|work|quarantine|processed)[\"']"
    r")"
)
TRUST_ARTIFACT_RE = re.compile(r"(?i)(?:^|[_/.-])(?:release|proof|receipt|manifest|published|catalog|triplet)s?(?:[_/.-]|$)")
PLACEHOLDER_NAMES = frozenset({"README.md", ".gitkeep"})


class TopologyError(ValueError):
    """Raised when repository input or the baseline is unsafe or malformed."""


@dataclass(frozen=True, order=True)
class Finding:
    rule_id: str
    subject: str
    evidence_sha256: str
    evidence_members: tuple[str, ...]
    fingerprint: str
    baseline_allowed: bool

    def as_dict(self, disposition: str) -> dict[str, str]:
        return {
            "disposition": disposition,
            "evidence_sha256": self.evidence_sha256,
            "fingerprint": self.fingerprint,
            "rule_id": self.rule_id,
            "subject": self.subject,
        }


def _digest(value: str | bytes) -> str:
    raw = value if isinstance(value, bytes) else value.encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _encode_evidence_members(members: Sequence[str]) -> str:
    raw = "\0".join(members).encode("utf-8")
    return base64.b64encode(zlib.compress(raw, level=9)).decode("ascii")


def _decode_evidence_members(encoded: object, expected_digest: object) -> tuple[str, ...]:
    if not isinstance(encoded, str) or not encoded or len(encoded) > MAX_FILE_BYTES:
        raise TopologyError("baseline compressed evidence is invalid")
    try:
        compressed = base64.b64decode(encoded, validate=True)
        decompressor = zlib.decompressobj()
        raw = decompressor.decompress(compressed, MAX_EVIDENCE_BYTES + 1)
    except (binascii.Error, zlib.error) as exc:
        raise TopologyError("baseline compressed evidence cannot be decoded") from exc
    if (
        len(raw) > MAX_EVIDENCE_BYTES
        or not decompressor.eof
        or decompressor.unused_data
        or decompressor.unconsumed_tail
        or _digest(raw) != expected_digest
    ):
        raise TopologyError("baseline compressed evidence does not match its digest")
    try:
        members = tuple(raw.decode("utf-8").split("\0"))
    except UnicodeError as exc:
        raise TopologyError("baseline compressed evidence is not UTF-8") from exc
    if (
        not members
        or len(members) > MAX_EVIDENCE_MEMBERS
        or any(not member or len(member.encode("utf-8")) > MAX_EVIDENCE_MEMBER_BYTES for member in members)
        or list(members) != sorted(set(members))
    ):
        raise TopologyError("baseline compressed evidence members are invalid")
    return members


def _serialized_baseline_entry(finding: Finding) -> dict[str, str]:
    return {
        "evidence_sha256": finding.evidence_sha256,
        "evidence_zlib_base64": _encode_evidence_members(finding.evidence_members),
        "fingerprint": finding.fingerprint,
        "rule_id": finding.rule_id,
        "subject": finding.subject,
    }


def _finding(
    rule_id: str,
    subject: str,
    evidence: Iterable[str] | str,
    *,
    baseline_allowed: bool | None = None,
) -> Finding:
    members = (evidence,) if isinstance(evidence, str) else tuple(sorted(set(evidence)))
    rendered = "\0".join(members)
    evidence_sha256 = _digest(rendered)
    fingerprint = _digest("\0".join((rule_id, subject, evidence_sha256)))
    allowed = RULE_BY_ID[rule_id].baseline_allowed if baseline_allowed is None else baseline_allowed
    return Finding(rule_id, subject, evidence_sha256, members, fingerprint, allowed)


def _is_app_text_path(path: str) -> bool:
    parsed = PurePosixPath(path)
    return (
        path.startswith("apps/")
        and (parsed.suffix.casefold() in APP_TEXT_SUFFIXES or parsed.name in APP_TEXT_NAMES)
    )


def _git(repo_root: Path, *args: str) -> bytes:
    env = os.environ.copy()
    env.update(
        {
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_TERMINAL_PROMPT": "0",
            "LC_ALL": "C",
        }
    )
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise TopologyError("Git command timed out") from exc
    if result.returncode != 0:
        raise TopologyError("Git index unavailable")
    return result.stdout


def tracked_index(
    repo_root: Path,
) -> tuple[tuple[str, ...], Mapping[str, str], Mapping[str, str]]:
    raw = _git(repo_root, "ls-files", "-s", "-z")
    paths: list[str] = []
    modes: dict[str, str] = {}
    object_ids: dict[str, str] = {}
    for record in raw.split(b"\0"):
        if not record:
            continue
        try:
            header, path_raw = record.split(b"\t", 1)
            mode_raw, object_id_raw, stage_raw = header.split(b" ", 2)
            mode = mode_raw.decode("ascii")
            object_id = object_id_raw.decode("ascii")
            stage = stage_raw.decode("ascii")
            path = path_raw.decode("utf-8")
        except (ValueError, UnicodeError) as exc:
            raise TopologyError("Git index contains an undecodable entry") from exc
        if "\x00" in path or PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
            raise TopologyError("Git index contains an unsafe path")
        if stage != "0":
            raise TopologyError("Git index contains an unmerged entry")
        if path in object_ids:
            raise TopologyError("Git index contains a duplicate path")
        paths.append(path)
        modes[path] = mode
        object_ids[path] = object_id
    if paths != sorted(paths):
        paths.sort()
    return tuple(paths), modes, object_ids


def _index_blobs(
    repo_root: Path,
    object_ids: Mapping[str, str],
    wanted_paths: Iterable[str],
) -> Mapping[str, bytes]:
    wanted = sorted(set(wanted_paths))
    unique_ids = sorted({object_ids[path] for path in wanted if path in object_ids})
    if not unique_ids:
        return {}
    env = os.environ.copy()
    env.update(
        {
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_TERMINAL_PROMPT": "0",
            "LC_ALL": "C",
        }
    )
    object_input = ("\n".join(unique_ids) + "\n").encode("ascii")
    try:
        size_result = subprocess.run(
            ["git", "cat-file", "--batch-check"],
            cwd=repo_root,
            env=env,
            input=object_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise TopologyError("Git object-size query timed out") from exc
    if size_result.returncode != 0:
        raise TopologyError("Git object database unavailable")
    total_bytes = 0
    for expected_id, raw_line in zip(unique_ids, size_result.stdout.splitlines(), strict=True):
        try:
            header = raw_line.decode("ascii", errors="strict").split()
            if len(header) != 3 or header[0] != expected_id or header[1] != "blob":
                raise ValueError
            size = int(header[2])
        except (UnicodeError, ValueError) as exc:
            raise TopologyError("Git object-size response is malformed") from exc
        if size < 0 or size > MAX_FILE_BYTES:
            raise TopologyError("selected Git blob exceeds the per-file limit")
        total_bytes += size
        if total_bytes > MAX_SELECTED_BLOB_BYTES:
            raise TopologyError("selected Git blobs exceed the aggregate limit")
    try:
        result = subprocess.run(
            ["git", "cat-file", "--batch"],
            cwd=repo_root,
            env=env,
            input=object_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise TopologyError("Git object query timed out") from exc
    if result.returncode != 0:
        raise TopologyError("Git object database unavailable")
    by_id: dict[str, bytes] = {}
    offset = 0
    raw = result.stdout
    for expected_id in unique_ids:
        newline = raw.find(b"\n", offset)
        if newline < 0:
            raise TopologyError("Git batch response is truncated")
        header = raw[offset:newline].decode("ascii", errors="strict").split()
        if len(header) != 3 or header[0] != expected_id or header[1] != "blob":
            raise TopologyError("Git batch response is malformed")
        size = int(header[2])
        start = newline + 1
        end = start + size
        if end >= len(raw) or raw[end : end + 1] != b"\n":
            raise TopologyError("Git blob response is truncated")
        by_id[expected_id] = raw[start:end]
        offset = end + 1
    return {path: by_id[object_ids[path]] for path in wanted if path in object_ids}


def _read_json(path: Path) -> Mapping[str, object]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_FILE_BYTES:
        raise TopologyError(f"unsafe or missing JSON input: {path.name}")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, TopologyError) as exc:
        raise TopologyError(f"invalid JSON input: {path.name}") from exc
    if not isinstance(value, dict):
        raise TopologyError(f"JSON object required: {path.name}")
    return value


def _blob_json(blobs: Mapping[str, bytes], path: str) -> Mapping[str, object]:
    try:
        value = json.loads(
            blobs[path].decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except (KeyError, UnicodeError, json.JSONDecodeError, TopologyError) as exc:
        raise TopologyError(f"invalid indexed JSON input: {path}") from exc
    if not isinstance(value, dict):
        raise TopologyError(f"indexed JSON object required: {path}")
    return value


def _registered_roots(
    blobs: Mapping[str, bytes],
) -> tuple[set[str], Mapping[str, Mapping[str, object]]]:
    data = _blob_json(blobs, "control_plane/root_registry.yaml")
    raw_roots = data.get("roots")
    if not isinstance(raw_roots, list):
        raise TopologyError("root registry has no roots array")
    by_path: dict[str, Mapping[str, object]] = {}
    for entry in raw_roots:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise TopologyError("root registry entry is malformed")
        path = str(entry["path"]).removesuffix("/")
        if not path or "/" in path or path in by_path:
            raise TopologyError("root registry contains a duplicate or invalid path")
        by_path[path] = entry
    return set(by_path), by_path


def _path_findings(
    paths: Sequence[str],
    modes: Mapping[str, str],
    object_ids: Mapping[str, str],
    blobs: Mapping[str, bytes],
) -> list[Finding]:
    findings: list[Finding] = []
    path_set = set(paths)
    registered, roots = _registered_roots(blobs)
    observed_roots = {path.split("/", 1)[0] for path in paths if "/" in path}
    grammar_groups: dict[str, list[str]] = {
        "nonportable-punctuation": [],
        "uppercase": [],
    }

    for path in paths:
        unsafe: list[str] = []
        if modes.get(path) == "120000":
            unsafe.append("symlink")
        if "\\" in path:
            unsafe.append("backslash")
        if unicodedata.normalize("NFC", path) != path:
            unsafe.append("not-nfc")
        for segment in PurePosixPath(path).parts:
            if segment.endswith((" ", ".")):
                unsafe.append("trailing-dot-or-space")
            if "(" in segment or ")" in segment:
                unsafe.append("parentheses")
            if " " in segment:
                unsafe.append("space")
            if any(ord(char) > 127 for char in segment):
                unsafe.append("non-ascii")
            if "," in segment:
                unsafe.append("comma")
            if any(character.isupper() for character in segment):
                grammar_groups["uppercase"].append(path)
            if not re.fullmatch(r"[A-Za-z0-9._()-]+", segment):
                grammar_groups["nonportable-punctuation"].append(path)
            if any(ord(char) < 32 or ord(char) == 127 for char in segment):
                unsafe.append("control-character")
            if WINDOWS_RESERVED.fullmatch(segment):
                unsafe.append("windows-reserved")
        if unsafe:
            hard_unsafe = {
                "control-character",
                "not-nfc",
                "symlink",
                "trailing-dot-or-space",
                "windows-reserved",
            }
            findings.append(
                _finding(
                    "KFM-TOPO-001",
                    f"invariant-path:{path}" if hard_unsafe.intersection(unsafe) else path,
                    [*unsafe, f"mode={modes.get(path, 'MISSING')}", f"object={object_ids.get(path, 'MISSING')}"],
                    baseline_allowed=not bool(hard_unsafe.intersection(unsafe)),
                )
            )
    for grammar, members in sorted(grammar_groups.items()):
        if members:
            findings.append(_finding("KFM-TOPO-001", f"path-grammar:{grammar}", members))

    for root in sorted(observed_roots - registered):
        findings.append(_finding("KFM-TOPO-002", root + "/", "UNREGISTERED_ROOT"))
    for root in sorted(registered - observed_roots):
        entry = roots[root]
        if entry.get("status") not in {"RETIRED"}:
            findings.append(_finding("KFM-TOPO-002", root + "/", "REGISTERED_ROOT_MISSING"))

    for path in paths:
        if "/" not in path and path not in ROOT_FILE_ALLOWLIST:
            findings.append(_finding("KFM-TOPO-003", path, "ROOT_FILE_NOT_ALLOWED"))

    for root in ("catalog", "src"):
        members = [path for path in paths if path.startswith(root + "/")]
        if members:
            evidence = [f"{path}@{object_ids.get(path, 'MISSING')}" for path in members]
            findings.append(_finding("KFM-TOPO-004", root + "/", evidence))

    artifact_children = {
        PurePosixPath(path).parts[1]
        for path in paths
        if path.startswith("artifacts/") and len(PurePosixPath(path).parts) >= 3
    }
    for child in sorted(artifact_children - ARTIFACT_CHILDREN):
        members = [path for path in paths if path.startswith(f"artifacts/{child}/")]
        evidence = [f"{path}@{object_ids.get(path, 'MISSING')}" for path in members]
        findings.append(_finding("KFM-TOPO-005", f"artifacts/{child}/", evidence))
    for path in paths:
        if path.startswith("artifacts/") and len(PurePosixPath(path).parts) == 2 and path != "artifacts/README.md":
            findings.append(_finding("KFM-TOPO-005", path, "ARTIFACT_ROOT_PAYLOAD_DENIED"))

    for alias in sorted(SCOPE_ALIASES):
        members = [
            path
            for path in paths
            if path.split("/", 1)[0] in SCOPE_ROOTS and alias in PurePosixPath(path).parts[1:]
        ]
        if members:
            findings.append(_finding("KFM-TOPO-006", f"scope-alias:{alias}", members))

    normalized: dict[str, list[str]] = {}
    for path in paths:
        normalized.setdefault(unicodedata.normalize("NFC", path).casefold(), []).append(path)
    for key, members in sorted(normalized.items()):
        if len(set(members)) > 1:
            findings.append(_finding("KFM-TOPO-007", f"casefold:{key}", members))

    collection_prefixes = {
        "data/triplet/": "data/triplets/",
        "data/triplet(s)/": "data/triplets/",
        "docs/atlas/": "docs/atlases/",
        "release/manifest/": "release/manifests/",
        "release/correction/": "release/correction_notices/",
        "release/corrections/": "release/correction_notices/",
        "release/rollback/": "release/rollback_cards/",
        "data/rollback/": "data/receipts/rollback/",
        "data/catalog/domain/": "data/catalog/domains/",
        "pipelines/specs/": "pipeline_specs/",
    }
    for legacy, canonical in collection_prefixes.items():
        members = [path for path in paths if path.startswith(legacy)]
        if members:
            findings.append(_finding("KFM-TOPO-008", f"{legacy}->{canonical}", members))

    all_directories: set[str] = set()
    for path in paths:
        parts = PurePosixPath(path).parts
        all_directories.update("/".join(parts[:index]) for index in range(1, len(parts)))
    separator_groups: dict[str, list[str]] = {}
    for directory in all_directories:
        parsed = PurePosixPath(directory)
        normalized_name = parsed.name.replace("-", "_").lstrip("_")
        key = (parsed.parent / normalized_name).as_posix()
        separator_groups.setdefault(key, []).append(directory)
    for key, members in sorted(separator_groups.items()):
        if len(set(members)) > 1:
            findings.append(_finding("KFM-TOPO-008", f"separator-alias:{key}", members))

    directories: dict[str, set[str]] = {}
    child_dirs: set[str] = set()
    for path in paths:
        parts = PurePosixPath(path).parts
        for index in range(1, len(parts)):
            directory = "/".join(parts[:index])
            if index + 1 == len(parts):
                directories.setdefault(directory, set()).add(parts[-1])
            else:
                child_dirs.add(directory)
    scaffold_leaves = sorted(
        directory
        for directory, names in directories.items()
        if directory not in child_dirs and names and names <= PLACEHOLDER_NAMES
    )
    if scaffold_leaves:
        findings.append(_finding("KFM-TOPO-009", "scaffold-only-leaf-directories", scaffold_leaves))

    data_children = {
        PurePosixPath(path).parts[1]
        for path in paths
        if path.startswith("data/") and len(PurePosixPath(path).parts) >= 3
    }
    for child in sorted(data_children - DATA_CHILDREN):
        members = [path for path in paths if path.startswith(f"data/{child}/")]
        findings.append(_finding("KFM-TOPO-010", f"data/{child}/", members))
    for path in paths:
        if path.startswith("data/") and len(PurePosixPath(path).parts) == 2 and path != "data/README.md":
            findings.append(_finding("KFM-TOPO-010", path, "DATA_ROOT_PAYLOAD_DENIED"))

    release_children = {
        PurePosixPath(path).parts[1]
        for path in paths
        if path.startswith("release/") and len(PurePosixPath(path).parts) >= 3
    }
    for child in sorted(release_children - RELEASE_CHILDREN):
        members = [path for path in paths if path.startswith(f"release/{child}/")]
        findings.append(_finding("KFM-TOPO-011", f"release/{child}/", members))
    for path in paths:
        parts = PurePosixPath(path).parts
        if path.startswith("release/") and len(parts) == 2 and path != "release/README.md":
            findings.append(_finding("KFM-TOPO-011", path, "RELEASE_ROOT_PAYLOAD_DENIED"))
        elif (
            path.startswith("release/")
            and len(parts) == 3
            and parts[1] in RELEASE_CHILDREN
            and parts[-1] not in PLACEHOLDER_NAMES
        ):
            findings.append(_finding("KFM-TOPO-011", path, "RELEASE_DOMAIN_LANE_REQUIRED"))

    for path in paths:
        if path.endswith(".rego") and not path.startswith(("policy/", "fixtures/", "tests/")):
            findings.append(_finding("KFM-TOPO-012", path, "POLICY_SOURCE_OUTSIDE_POLICY"))

    trust_members = [path for path in paths if path.startswith("artifacts/") and TRUST_ARTIFACT_RE.search(path)]
    if trust_members:
        evidence = [f"{path}@{object_ids.get(path, 'MISSING')}" for path in trust_members]
        findings.append(_finding("KFM-TOPO-013", "artifacts/trust-shaped", evidence))

    return findings


def _content_findings(paths: Sequence[str], blobs: Mapping[str, bytes]) -> list[Finding]:
    findings: list[Finding] = []
    path_set = set(paths)

    for path in paths:
        if not _is_app_text_path(path):
            continue
        try:
            raw = blobs[path]
            if len(raw) > MAX_FILE_BYTES:
                raise TopologyError(f"selected app source exceeds the per-file limit: {path}")
            text = raw.decode("utf-8")
        except KeyError as exc:
            raise TopologyError(f"selected app source is missing: {path}") from exc
        except UnicodeError as exc:
            raise TopologyError(f"selected app source is not UTF-8: {path}") from exc
        if INTERNAL_STORE_RE.search(text) or INTERNAL_STORE_CONSTRUCTION_RE.search(text):
            test_only = "/tests/" in path and re.search(r"(?:^|[._-])test(?:[._-]|$)", PurePosixPath(path).name)
            findings.append(
                _finding(
                    "KFM-TOPO-014",
                    ("test-reference:" if test_only else "deployable-reference:") + path,
                    "INTERNAL_STORE_REFERENCE",
                    baseline_allowed=bool(test_only),
                )
            )

    schema_ids: dict[str, list[str]] = {}
    for path in paths:
        if not path.endswith(".schema.json") or path.startswith(("fixtures/", "tests/")):
            continue
        try:
            value = json.loads(
                blobs[path].decode("utf-8"),
                object_pairs_hook=_unique_object,
                parse_constant=_nonfinite,
                parse_float=_finite_float,
            )
        except (KeyError, UnicodeError, json.JSONDecodeError, TopologyError) as exc:
            raise TopologyError(f"canonical schema cannot be inspected: {path}") from exc
        if not isinstance(value, dict):
            raise TopologyError(f"canonical schema must be a JSON object: {path}")
        if isinstance(value, dict) and isinstance(value.get("$id"), str):
            schema_ids.setdefault(value["$id"], []).append(path)
    for schema_id, members in sorted(schema_ids.items()):
        if len(members) > 1:
            findings.append(_finding("KFM-TOPO-015", f"schema-id:{schema_id}", members))

    doc_ids: dict[str, list[str]] = {}
    for path in paths:
        if not path.endswith(".md") or path.startswith(("fixtures/", "tests/")):
            continue
        try:
            raw = blobs[path]
            if len(raw) > MAX_FILE_BYTES:
                raise TopologyError(f"selected Markdown exceeds the per-file limit: {path}")
            head = "\n".join(raw.decode("utf-8").splitlines()[:80])
        except KeyError as exc:
            raise TopologyError(f"selected Markdown is missing: {path}") from exc
        except UnicodeError as exc:
            raise TopologyError(f"selected Markdown is not UTF-8: {path}") from exc
        match = DOC_ID_RE.search(head)
        if match and "<" not in match.group(1) and "TODO" not in match.group(1):
            doc_ids.setdefault(match.group(1), []).append(path)
    for doc_id, members in sorted(doc_ids.items()):
        if len(members) > 1:
            findings.append(_finding("KFM-TOPO-016", f"doc-id:{doc_id}", members))

    payloads = [
        path
        for path in paths
        if path.startswith("artifacts/")
        and PurePosixPath(path).name not in {"README.md", ".gitkeep", ".gitignore"}
    ]
    required_keys = ("generated_from", "generator", "generator_version", "sha256", "edit_policy")
    edit_policies = {"generated_only", "manual_review_required", "regenerate_only", "read_only"}
    for path in payloads:
        try:
            text = blobs[path].decode("utf-8")
        except (KeyError, UnicodeError):
            text = ""
        failures: list[str] = []
        metadata: Mapping[str, object] | None = None
        try:
            parsed = json.loads(
                text,
                object_pairs_hook=_unique_object,
                parse_constant=_nonfinite,
                parse_float=_finite_float,
            )
            if isinstance(parsed, dict):
                metadata = parsed
        except (json.JSONDecodeError, TopologyError):
            metadata = None
        if metadata is None:
            failures.extend(f"metadata_unverified:{key}" for key in required_keys)
        else:
            for key in ("generated_from", "generator", "generator_version"):
                if not isinstance(metadata.get(key), str) or not str(metadata[key]).strip():
                    failures.append(f"invalid:{key}")
            digest = metadata.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
                failures.append("invalid:sha256")
            if metadata.get("edit_policy") not in edit_policies:
                failures.append("invalid:edit_policy")
        if failures:
            findings.append(_finding("KFM-TOPO-017", path, failures))

    policy_children = sorted(
        {
            PurePosixPath(path).parts[1]
            for path in paths
            if path.startswith("policy/") and len(PurePosixPath(path).parts) >= 3
        }
    )
    for child in policy_children:
        prefix = f"policy/{child}/"
        members = [path for path in paths if path.startswith(prefix)]
        payload = [path for path in members if PurePosixPath(path).name not in PLACEHOLDER_NAMES]
        if payload and prefix + "README.md" not in path_set:
            findings.append(_finding("KFM-TOPO-018", prefix, payload))

    try:
        doctrine_digest = hashlib.sha256(blobs["docs/doctrine/directory-rules.md"]).hexdigest()
    except KeyError:
        doctrine_digest = "MISSING"
    authority_evidence: list[str] = []
    if doctrine_digest != ADOPTED_SHA256:
        authority_evidence.append("DOCTRINE_DIGEST_MISMATCH")
    try:
        adr_head = blobs["docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"].decode(
            "utf-8"
        )[:12_000]
        if not re.search(r"(?m)^status:\s*accepted\s*$", adr_head):
            authority_evidence.append("ADR_NOT_ACCEPTED")
    except (KeyError, UnicodeError):
        authority_evidence.append("ADR_MISSING")
    try:
        registry = _blob_json(blobs, "control_plane/root_registry.yaml")
        doctrine = registry.get("doctrine")
        if not isinstance(doctrine, dict) or doctrine.get("sha256") != f"sha256:{ADOPTED_SHA256}" or doctrine.get("decision_ref") != "ADR-0029":
            authority_evidence.append("ROOT_REGISTRY_BINDING_MISMATCH")
    except TopologyError:
        authority_evidence.append("ROOT_REGISTRY_UNAVAILABLE")
    if authority_evidence:
        findings.append(_finding("KFM-TOPO-019", "adopted-directory-authority", authority_evidence))

    aliases = _blob_json(blobs, "control_plane/path_alias_register.yaml").get("aliases")
    if not isinstance(aliases, list):
        raise TopologyError("path alias register has no aliases array")
    alias_ids: set[str] = set()
    for entry in aliases:
        if not isinstance(entry, dict) or not isinstance(entry.get("alias_id"), str):
            raise TopologyError("path alias register entry is malformed")
        alias_id = str(entry["alias_id"])
        if not alias_id or alias_id in alias_ids:
            raise TopologyError("path alias register contains a duplicate or invalid alias_id")
        alias_ids.add(alias_id)
        if entry.get("status") != "ACTIVE":
            continue
        unresolved: list[str] = []
        if entry.get("consumer_closure") != "CLOSED":
            unresolved.append(f"consumer_closure={entry.get('consumer_closure')}")
        if entry.get("verification_state") != "VERIFIED":
            unresolved.append(f"verification_state={entry.get('verification_state')}")
        if entry.get("write_rule") != "canonical_only":
            unresolved.append("write_rule_not_canonical_only")
        expiry = entry.get("expiry")
        if not isinstance(expiry, dict) or expiry.get("mode") not in {"condition", "date"} or not isinstance(expiry.get("value"), str) or not expiry.get("value"):
            unresolved.append("expiry_invalid")
        elif expiry.get("mode") == "date":
            try:
                if date.fromisoformat(str(expiry["value"])) < date.today():
                    unresolved.append("expiry_elapsed")
            except ValueError:
                unresolved.append("expiry_invalid")
        exit_criteria = entry.get("exit_criteria")
        if not isinstance(exit_criteria, list) or not exit_criteria or not all(
            isinstance(item, str) and item for item in exit_criteria
        ):
            unresolved.append("exit_criteria_invalid")
        if unresolved:
            findings.append(_finding("KFM-TOPO-020", alias_id, unresolved))

    return findings


def scan(repo_root: Path) -> tuple[tuple[Finding, ...], int]:
    root = repo_root.resolve()
    paths, modes, object_ids = tracked_index(root)
    fixed = {
        "control_plane/path_alias_register.yaml",
        "control_plane/root_registry.yaml",
        "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md",
        "docs/doctrine/directory-rules.md",
    }
    content_paths = {
        path
        for path in paths
        if path.endswith((".md", ".schema.json"))
        or _is_app_text_path(path)
        or path.startswith("artifacts/")
    } | fixed
    blobs = _index_blobs(root, object_ids, content_paths)
    findings = _path_findings(paths, modes, object_ids, blobs) + _content_findings(paths, blobs)
    unique = tuple(sorted(set(findings)))
    if len(unique) > MAX_FINDINGS:
        raise TopologyError("finding budget exceeded")
    return unique, len(paths)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise TopologyError(f"duplicate baseline key: {key}")
        result[key] = value
    return result


def _nonfinite(value: str) -> object:
    raise TopologyError(f"non-finite baseline number: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise TopologyError(f"non-finite baseline number: {value}")
    return parsed


def _load_baseline_bytes(
    raw: bytes, *, label: str
) -> tuple[Mapping[str, object], dict[str, Mapping[str, object]]]:
    if len(raw) > MAX_FILE_BYTES:
        raise TopologyError(f"{label} baseline is too large")
    try:
        data = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, TopologyError) as exc:
        raise TopologyError(f"{label} baseline JSON is invalid: {type(exc).__name__}") from exc
    expected = {"authority", "closure_ref", "entries", "expires_on", "generated_from_ref", "non_effects", "owner", "schema_version"}
    if not isinstance(data, dict) or set(data) != expected:
        raise TopologyError("baseline root does not match the v1 contract")
    if data["schema_version"] != BASELINE_VERSION or data["authority"] != "implementation_waivers_only":
        raise TopologyError("baseline identity or authority is invalid")
    if data["non_effects"] != [
        "does_not_define_or_amend_rules",
        "does_not_authorize_migration_or_deletion",
        "does_not_grant_evidence_policy_review_release_or_publication_status",
    ]:
        raise TopologyError("baseline non_effects are invalid")
    for field in ("owner", "closure_ref", "generated_from_ref", "expires_on"):
        if not isinstance(data[field], str) or not data[field]:
            raise TopologyError(f"baseline {field} is invalid")
    date.fromisoformat(str(data["expires_on"]))
    entries = data["entries"]
    if not isinstance(entries, list) or len(entries) > MAX_FINDINGS:
        raise TopologyError("baseline entries must be a bounded array")
    result: dict[str, Mapping[str, object]] = {}
    ordered: list[str] = []
    aggregate_evidence_bytes = 0
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict) or set(entry) != {
            "evidence_sha256",
            "evidence_zlib_base64",
            "fingerprint",
            "rule_id",
            "subject",
        }:
            raise TopologyError(f"baseline entry {index} is malformed")
        rule_id = entry.get("rule_id")
        if not isinstance(rule_id, str) or rule_id not in RULE_BY_ID:
            raise TopologyError(f"baseline entry {index} has an unknown rule")
        subject = entry.get("subject")
        entry_allowed = RULE_BY_ID[rule_id].baseline_allowed
        if rule_id == "KFM-TOPO-001" and isinstance(subject, str) and subject.startswith("invariant-path:"):
            entry_allowed = False
        if rule_id == "KFM-TOPO-014" and (
            not isinstance(subject, str) or not subject.startswith("test-reference:")
        ):
            entry_allowed = False
        if not entry_allowed:
            raise TopologyError(f"baseline entry {index} attempts to waive an invariant")
        fingerprint = entry.get("fingerprint")
        if not isinstance(fingerprint, str) or not re.fullmatch(r"sha256:[0-9a-f]{64}", fingerprint):
            raise TopologyError(f"baseline entry {index} has an invalid fingerprint")
        if fingerprint in result:
            raise TopologyError(f"duplicate baseline fingerprint: {fingerprint}")
        for field in ("evidence_sha256", "subject"):
            if not isinstance(entry.get(field), str) or not entry[field]:
                raise TopologyError(f"baseline entry {index} has an invalid {field}")
        expected_fingerprint = _digest(
            "\0".join((rule_id, str(entry["subject"]), str(entry["evidence_sha256"])))
        )
        if fingerprint != expected_fingerprint:
            raise TopologyError(f"baseline entry {index} fingerprint does not match its evidence")
        members = _decode_evidence_members(
            entry.get("evidence_zlib_base64"), entry.get("evidence_sha256")
        )
        aggregate_evidence_bytes += sum(len(member.encode("utf-8")) + 1 for member in members)
        if aggregate_evidence_bytes > MAX_BASELINE_EVIDENCE_BYTES:
            raise TopologyError("baseline decoded evidence exceeds the aggregate limit")
        entry["evidence_members"] = members
        ordered.append(fingerprint)
        result[fingerprint] = entry
    if ordered != sorted(ordered):
        raise TopologyError("baseline entries are not sorted by fingerprint")
    return data, result


def load_baseline(path: Path) -> dict[str, Mapping[str, object]]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_FILE_BYTES:
        raise TopologyError("baseline is missing, unsafe, or too large")
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise TopologyError("baseline cannot be read") from exc
    _data, entries = _load_baseline_bytes(raw, label="current")
    return entries


def validate_baseline_transition(
    current_data: Mapping[str, object],
    current_entries: Mapping[str, Mapping[str, object]],
    trusted_data: Mapping[str, object],
    trusted_entries: Mapping[str, Mapping[str, object]],
) -> None:
    additions = sorted(set(current_entries) - set(trusted_entries))
    removals = sorted(set(trusted_entries) - set(current_entries))
    trusted_by_identity = {
        (entry["rule_id"], entry["subject"]): (fingerprint, entry)
        for fingerprint, entry in trusted_entries.items()
    }
    consumed_removals: set[str] = set()
    for fingerprint in additions:
        entry = current_entries[fingerprint]
        identity = (entry["rule_id"], entry["subject"])
        prior = trusted_by_identity.get(identity)
        if prior is None or prior[0] not in removals:
            raise TopologyError("baseline transition adds waiver fingerprints")
        current_members = set(entry["evidence_members"])
        trusted_members = set(prior[1]["evidence_members"])
        if not current_members < trusted_members:
            raise TopologyError("baseline transition does not strictly shrink evidence")
        consumed_removals.add(prior[0])
    for fingerprint in set(current_entries).intersection(trusted_entries):
        if current_entries[fingerprint] != trusted_entries[fingerprint]:
            raise TopologyError("baseline transition mutates a waiver entry")
    if date.fromisoformat(str(current_data["expires_on"])) > date.fromisoformat(
        str(trusted_data["expires_on"])
    ):
        raise TopologyError("baseline transition extends expiry")
    immutable = (
        "authority",
        "closure_ref",
        "generated_from_ref",
        "non_effects",
        "owner",
        "schema_version",
    )
    if any(current_data[field] != trusted_data[field] for field in immutable):
        raise TopologyError("baseline transition mutates protected metadata")


def enforce_trusted_baseline(
    repo_root: Path,
    current_data: Mapping[str, object],
    current_entries: Mapping[str, Mapping[str, object]],
    trusted_ref: str,
) -> None:
    if not re.fullmatch(r"[A-Za-z0-9_./^~:-]{1,200}", trusted_ref) or trusted_ref.startswith("-"):
        raise TopologyError("trusted baseline ref is invalid")
    try:
        trusted_sha = _git(repo_root, "rev-parse", "--verify", f"{trusted_ref}^{{commit}}").decode("ascii").strip()
    except (TopologyError, UnicodeError) as exc:
        raise TopologyError("trusted baseline ref cannot be resolved") from exc
    if not re.fullmatch(r"[0-9a-f]{40}", trusted_sha):
        raise TopologyError("trusted baseline ref did not resolve to a commit")
    try:
        raw = _git(repo_root, "show", f"{trusted_sha}:{BASELINE_REPOSITORY_PATH}")
    except TopologyError:
        expected_generation = f"main@{BOOTSTRAP_BASE_SHA}"
        if trusted_sha != BOOTSTRAP_BASE_SHA or current_data.get("generated_from_ref") != expected_generation:
            raise TopologyError("trusted baseline is missing outside the governed bootstrap")
        return
    trusted_data, trusted_entries = _load_baseline_bytes(raw, label="trusted")
    validate_baseline_transition(current_data, current_entries, trusted_data, trusted_entries)


def candidate_baseline(findings: Sequence[Finding], *, expires_on: str) -> dict[str, object]:
    date.fromisoformat(expires_on)
    entries = [
        _serialized_baseline_entry(finding)
        for finding in findings
        if finding.baseline_allowed
    ]
    entries.sort(key=lambda item: str(item["fingerprint"]))
    return {
        "authority": "implementation_waivers_only",
        "closure_ref": "ADR-0029-post-adoption-convergence-ratchet",
        "entries": entries,
        "expires_on": expires_on,
        "generated_from_ref": f"main@{BOOTSTRAP_BASE_SHA}",
        "non_effects": [
            "does_not_define_or_amend_rules",
            "does_not_authorize_migration_or_deletion",
            "does_not_grant_evidence_policy_review_release_or_publication_status",
        ],
        "owner": "@bartytime4life",
        "schema_version": BASELINE_VERSION,
    }


def evaluate(
    findings: Sequence[Finding],
    tracked_count: int,
    baseline: Mapping[str, Mapping[str, object]],
    *,
    expires_on: str,
    as_of: date | None = None,
) -> tuple[int, dict[str, object]]:
    observed = {finding.fingerprint: finding for finding in findings}
    stale = sorted(set(baseline) - set(observed))
    invariant: set[str] = set()
    new_drift: set[str] = set()
    baselined: set[str] = set()
    mismatch: set[str] = set()
    for finding in findings:
        entry = baseline.get(finding.fingerprint)
        if not finding.baseline_allowed:
            invariant.add(finding.fingerprint)
        elif entry is None:
            new_drift.add(finding.fingerprint)
        elif any(
            entry.get(field) != getattr(finding, field)
            for field in ("rule_id", "subject", "evidence_sha256", "fingerprint")
        ) or tuple(entry.get("evidence_members", ())) != finding.evidence_members:
            mismatch.add(finding.fingerprint)
        else:
            baselined.add(finding.fingerprint)
    expired = date.fromisoformat(expires_on) < (as_of or date.today())
    if mismatch:
        outcome, code = "ERROR_VALIDATOR", 2
    elif invariant or stale:
        outcome, code = "FAIL_INVARIANT", 1
    elif expired and baselined:
        outcome, code = "HOLD_UNRESOLVED", 1
    elif new_drift:
        outcome, code = "FAIL_NEW_DRIFT", 1
    else:
        outcome, code = "PASS", 0
    rendered = []
    for finding in findings:
        if finding.fingerprint in invariant:
            disposition = "FAIL_INVARIANT"
        elif finding.fingerprint in new_drift:
            disposition = "FAIL_NEW_DRIFT"
        elif finding.fingerprint in mismatch:
            disposition = "ERROR_BASELINE_MISMATCH"
        else:
            disposition = "BASELINED_WARNING"
        rendered.append(finding.as_dict(disposition))
    report = {
        "authority": {
            "authorizes_migration": False,
            "authorizes_repository_write": False,
            "authorizes_release": False,
            "publishes": False,
        },
        "baseline": {
            "applicable_count": len(baseline),
            "expires_on": expires_on,
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
        "tracked_path_count": tracked_count,
    }
    return code, report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--format", choices=("json", "text"), default="json")
    parser.add_argument("--emit-baseline", action="store_true")
    parser.add_argument("--expires-on", default="2026-11-10")
    parser.add_argument(
        "--trusted-baseline-ref",
        default=os.environ.get("KFM_TRUSTED_BASE_REF"),
        help="Trusted base commit/ref whose baseline may only shrink.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        findings, tracked_count = scan(args.repo_root)
        if args.emit_baseline:
            if any(not finding.baseline_allowed for finding in findings):
                raise TopologyError("cannot emit a baseline while invariant findings exist")
            print(json.dumps(candidate_baseline(findings, expires_on=args.expires_on), indent=2, sort_keys=True))
            return 0
        if args.baseline.is_symlink() or not args.baseline.is_file():
            raise TopologyError("baseline is missing or unsafe")
        baseline_data, baseline = _load_baseline_bytes(
            args.baseline.read_bytes(), label="current"
        )
        trusted_state = "NOT_REQUESTED"
        if args.trusted_baseline_ref:
            enforce_trusted_baseline(
                args.repo_root.resolve(),
                baseline_data,
                baseline,
                str(args.trusted_baseline_ref),
            )
            trusted_state = "VERIFIED"
        code, report = evaluate(
            findings,
            tracked_count,
            baseline,
            expires_on=str(baseline_data["expires_on"]),
        )
        report["baseline"]["trusted_transition"] = trusted_state
    except (OSError, UnicodeError, ValueError, TopologyError) as exc:
        report = {
            "authority": {"authorizes_repository_write": False},
            "error": type(exc).__name__,
            "outcome": "ERROR_VALIDATOR",
            "rule_count": len(RULES),
            "schema_version": REPORT_VERSION,
        }
        code = 2
    safe_report = json.loads(json.dumps(report))
    if (
        isinstance(safe_report, dict)
        and isinstance(safe_report.get("baseline"), dict)
        and "trusted_transition" in safe_report["baseline"]
    ):
        safe_report["baseline"]["trusted_transition"] = "[REDACTED]"

    if args.format == "text" and "counts" in safe_report:
        counts = safe_report["counts"]
        print(
            f"{safe_report['outcome']}: {safe_report['tracked_path_count']} tracked paths; "
            f"{counts['fail_invariant']} invariant; {counts['fail_new_drift']} new drift; "
            f"{counts['baselined_warning']} baselined warnings; "
            f"{len(safe_report['baseline']['stale_fingerprints'])} stale baseline entries"
        )
    elif args.format == "text":
        print(f"ERROR_VALIDATOR: {safe_report['error']}")
    else:
        print(json.dumps(safe_report, sort_keys=True, separators=(",", ":")))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
