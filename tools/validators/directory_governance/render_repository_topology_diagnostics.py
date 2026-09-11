#!/usr/bin/env python3
"""Render bounded failure identities for the repository-topology ratchet.

This is a diagnostic projection over validate_repository_topology.py. It does
not define topology rules, mutate the baseline, authorize migration, or expose
finding evidence members. Exit codes are preserved from the underlying ratchet.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
from pathlib import Path
from typing import Mapping, Sequence

import validate_repository_topology as topology

DEFAULT_MAX_ITEMS = 20
MAX_ITEMS_LIMIT = 50
PLAIN_LOG_TOKEN = re.compile(r"[A-Za-z0-9_./:-]+")
FAILURE_DISPOSITIONS = frozenset(
    {"ERROR_BASELINE_MISMATCH", "FAIL_INVARIANT", "FAIL_NEW_DRIFT"}
)

# Only stable, repository-authored messages are projected. Unknown exception
# text is never echoed because it can contain refs, paths, or other untrusted
# values. The stage fallback still makes hosted failures actionable without
# widening the validator's output surface.
ERROR_REASON_CODES = {
    "trusted baseline ref is invalid": "TRUSTED_REF_INVALID",
    "trusted baseline ref cannot be resolved": "TRUSTED_REF_UNRESOLVED",
    "trusted baseline ref did not resolve to a commit": "TRUSTED_REF_NOT_COMMIT",
    "trusted baseline is missing outside the governed bootstrap": "TRUSTED_BASELINE_MISSING",
    "baseline transition adds waiver fingerprints": "BASELINE_WAIVER_ADDED",
    "baseline transition does not strictly shrink evidence": "BASELINE_EVIDENCE_NOT_SHRUNK",
    "baseline transition mutates a waiver entry": "BASELINE_WAIVER_MUTATED",
    "baseline transition extends expiry": "BASELINE_EXPIRY_EXTENDED",
    "baseline transition mutates protected metadata": "BASELINE_METADATA_MUTATED",
    "baseline is missing or unsafe": "BASELINE_MISSING_OR_UNSAFE",
}
STAGE_REASON_CODES = {
    "scan": "SCAN_ERROR",
    "baseline": "BASELINE_LOAD_ERROR",
    "trusted-baseline": "TRUSTED_BASELINE_ERROR",
    "evaluate": "EVALUATE_ERROR",
}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--baseline", type=Path, default=topology.DEFAULT_BASELINE)
    parser.add_argument(
        "--trusted-baseline-ref",
        default=os.environ.get("KFM_TRUSTED_BASE_REF"),
        help="Trusted base commit/ref whose baseline may only shrink.",
    )
    parser.add_argument("--max-items", type=int, default=DEFAULT_MAX_ITEMS)
    return parser


def _bounded_max(value: int) -> int:
    if value < 1 or value > MAX_ITEMS_LIMIT:
        raise topology.TopologyError(
            f"max-items must be between 1 and {MAX_ITEMS_LIMIT}"
        )
    return value


def error_reason_code(exc: BaseException, *, stage: str) -> str:
    if isinstance(exc, topology.TopologyError):
        known = ERROR_REASON_CODES.get(str(exc))
        if known is not None:
            return known
    return STAGE_REASON_CODES.get(stage, "VALIDATOR_ERROR")


def _log_token(value: str) -> str:
    """Encode a display token, not its underlying identity or fingerprint.

    Preserve ordinary ASCII identifiers. Everything else is a reversible JSON
    string with ASCII escapes, so CR/LF, terminal controls, bidi characters and
    field delimiters cannot forge log structure. Escape command introducers
    even inside a line: JSON quoting alone does not neutralize runner commands.
    Sorting and deduplication must use the original values, before encoding.
    """
    if PLAIN_LOG_TOKEN.fullmatch(value) and "::" not in value:
        return value
    return json.dumps(value, ensure_ascii=True).replace(":", r"\u003a").replace("#", r"\u0023")


def render_diagnostics(
    report: Mapping[str, object],
    baseline: Mapping[str, Mapping[str, object]],
    *,
    max_items: int,
) -> tuple[str, ...]:
    limit = _bounded_max(max_items)
    rows: list[tuple[str, str, str, str]] = []

    raw_findings = report.get("findings", [])
    if not isinstance(raw_findings, list):
        raise topology.TopologyError("report findings are malformed")
    for raw in raw_findings:
        if not isinstance(raw, dict):
            raise topology.TopologyError("report finding is malformed")
        disposition = raw.get("disposition")
        if disposition not in FAILURE_DISPOSITIONS:
            continue
        rule_id = raw.get("rule_id")
        subject = raw.get("subject")
        fingerprint = raw.get("fingerprint")
        if not all(isinstance(value, str) and value for value in (rule_id, subject, fingerprint)):
            raise topology.TopologyError("report finding identity is malformed")
        rows.append((str(disposition), str(rule_id), str(subject), str(fingerprint)))

    raw_baseline = report.get("baseline", {})
    if not isinstance(raw_baseline, dict):
        raise topology.TopologyError("report baseline is malformed")
    stale = raw_baseline.get("stale_fingerprints", [])
    if not isinstance(stale, list) or not all(isinstance(value, str) for value in stale):
        raise topology.TopologyError("stale baseline identities are malformed")
    for fingerprint in stale:
        entry = baseline.get(fingerprint)
        if not isinstance(entry, Mapping):
            raise topology.TopologyError("stale baseline entry cannot be resolved")
        rule_id = entry.get("rule_id")
        subject = entry.get("subject")
        if not all(isinstance(value, str) and value for value in (rule_id, subject)):
            raise topology.TopologyError("stale baseline entry identity is malformed")
        rows.append(("STALE_BASELINE", str(rule_id), str(subject), fingerprint))

    ordered = sorted(set(rows))
    rendered = [
        f"{disposition} {_log_token(rule_id)} subject={_log_token(subject)} "
        f"fingerprint={_log_token(fingerprint)}"
        for disposition, rule_id, subject, fingerprint in ordered[:limit]
    ]
    if len(ordered) > limit:
        rendered.append(f"... {len(ordered) - limit} additional failure identities omitted")
    return tuple(rendered)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    stage = "scan"
    try:
        max_items = _bounded_max(args.max_items)
        findings, tracked_count = topology.scan(args.repo_root)

        stage = "baseline"
        if args.baseline.is_symlink() or not args.baseline.is_file():
            raise topology.TopologyError("baseline is missing or unsafe")
        baseline_data, baseline = topology._load_baseline_bytes(
            args.baseline.read_bytes(), label="current"
        )

        if args.trusted_baseline_ref:
            stage = "trusted-baseline"
            topology.enforce_trusted_baseline(
                args.repo_root.resolve(),
                baseline_data,
                baseline,
                str(args.trusted_baseline_ref),
            )

        stage = "evaluate"
        code, report = topology.evaluate(
            findings,
            tracked_count,
            baseline,
            expires_on=str(baseline_data["expires_on"]),
        )
        counts = report["counts"]
        print(
            f"{report['outcome']}: {report['tracked_path_count']} tracked paths; "
            f"{counts['fail_invariant']} invariant; {counts['fail_new_drift']} new drift; "
            f"{counts['baselined_warning']} baselined warnings; "
            f"{len(report['baseline']['stale_fingerprints'])} stale baseline entries"
        )
        for line in render_diagnostics(report, baseline, max_items=max_items):
            print(line)
        return code
    except (OSError, UnicodeError, ValueError, topology.TopologyError) as exc:
        reason = error_reason_code(exc, stage=stage)
        print(f"ERROR_VALIDATOR: {type(exc).__name__} reason={reason}")
        return 2


# These are diagnostic bindings, never receipts, proofs or authenticated claims.
# Use fixed field names and hash-only file identity; never echo paths, refs,
# source/baseline content, exception text or arbitrary environment values.
CONTEXT_MAX_BYTES = 4 * 1024 * 1024
CONTEXT_MAX_INDEX_BYTES = 32 * 1024 * 1024
CONTEXT_HEX = re.compile(r"[0-9a-f]{40}(?:[0-9a-f]{24})?")
CONTEXT_EVENTS = frozenset({"pull_request", "push", "workflow_dispatch", "merge_group"})
# Fixed labels only: do not emit source paths or decoded governance content.
CONTEXT_INDEX_INPUTS = {
    b"control_plane/root_registry.yaml": "root_registry",
    b"control_plane/path_alias_register.yaml": "path_alias_register",
    b"docs/doctrine/directory-rules.md": "directory_rules",
    b"docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md": "directory_adoption",
}


def _context_index_inputs(root: Path, index: bytes) -> dict[str, object]:
    """Bind selected *indexed* bytes, not potentially different working files.

    Recompute each Git blob identity before emitting its independent SHA-256.
    A replaced/mismatched object cannot become comparable capture evidence.
    The native scanner remains the owner of topology and authority decisions.
    """
    selected: dict[str, str] = {}
    for record in index.split(b"\0"):
        if not record:
            continue
        header, path = record.split(b"\t", 1)
        label = CONTEXT_INDEX_INPUTS.get(path)
        if label is None:
            continue
        mode, oid, stage = header.decode("ascii").split(" ")
        if (mode not in ("100644", "100755") or stage != "0"
                or CONTEXT_HEX.fullmatch(oid) is None or label in selected):
            raise ValueError("unsafe indexed context input")
        selected[label] = oid
    if set(selected) != set(CONTEXT_INDEX_INPUTS.values()):
        raise ValueError("missing indexed context input")

    result: dict[str, object] = {}
    for label, oid in sorted(selected.items()):
        size_raw = topology._git(root, "--no-lazy-fetch", "cat-file", "-s", oid).strip()
        if re.fullmatch(rb"[0-9]{1,10}", size_raw) is None:
            raise ValueError("invalid indexed context size")
        size = int(size_raw)
        if size > CONTEXT_MAX_BYTES:
            raise ValueError("indexed context input too large")
        data = topology._git(root, "--no-lazy-fetch", "cat-file", "blob", oid)
        if len(data) != size or len(data) > CONTEXT_MAX_BYTES:
            raise ValueError("unstable indexed context input")
        algorithm = "sha1" if len(oid) == 40 else "sha256"
        framed = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
        if hashlib.new(algorithm, framed).hexdigest() != oid:
            raise ValueError("indexed context object mismatch")
        result[label] = {"git_blob": oid, "sha256": hashlib.sha256(data).hexdigest(),
                         "size_bytes": size}
    return result


def _context_digest(path: Path, root: Path) -> str:
    """Bound a regular in-checkout file read; this is not an atomic FS snapshot."""
    absolute = Path(os.path.abspath(path))
    relative = absolute.relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("unsafe context input")
    flags = os.O_RDONLY | os.O_NONBLOCK | getattr(os, "O_NOFOLLOW", 0)
    with os.fdopen(os.open(absolute, flags), "rb") as stream:
        before = os.fstat(stream.fileno())
        if not stat.S_ISREG(before.st_mode) or before.st_size > CONTEXT_MAX_BYTES:
            raise ValueError("unsafe context input")
        data = stream.read(CONTEXT_MAX_BYTES + 1)
        after = os.fstat(stream.fileno())
    if (len(data) > CONTEXT_MAX_BYTES or len(data) != before.st_size
            or (before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns)
            != (after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns)):
        raise ValueError("unstable context input")
    return hashlib.sha256(data).hexdigest()


def execution_context(repo_root: Path, baseline: Path) -> dict[str, object]:
    """Collect local Git/file identities without executing any scanned payload."""
    root = repo_root.resolve(strict=True)
    identities = []
    for revision in ("HEAD^{commit}", "HEAD^{tree}"):
        value = topology._git(root, "rev-parse", "--verify", revision).decode("ascii").strip()
        if CONTEXT_HEX.fullmatch(value) is None:
            raise ValueError("invalid context identity")
        identities.append(value)
    index = topology._git(root, "ls-files", "-s", "-z")
    if len(index) > CONTEXT_MAX_INDEX_BYTES:
        raise ValueError("context index too large")
    context: dict[str, object] = {
        "version": "kfm.topology-execution-context.v2",
        "checkout_commit": identities[0],
        "checkout_tree": identities[1],
        "index_sha256": hashlib.sha256(index).hexdigest(),
        "indexed_governance": _context_index_inputs(root, index),
        "validator_file_sha256": _context_digest(Path(topology.__file__), root),
        "diagnostic_file_sha256": _context_digest(Path(__file__), root),
        "baseline_file_sha256": _context_digest(baseline, root),
    }
    for name in ("GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT"):
        value = os.environ.get(name)
        if value is not None and re.fullmatch(r"[1-9][0-9]{0,19}", value) is None:
            raise ValueError("invalid run context")
        context[name.lower()] = value
    event = os.environ.get("GITHUB_EVENT_NAME")
    if event is not None and event not in CONTEXT_EVENTS:
        raise ValueError("unsupported event context")
    context["github_event_name"] = event
    return context


def _context_record(repo_root: Path, baseline: Path) -> tuple[str, str] | None:
    try:
        payload = json.dumps(execution_context(repo_root, baseline), sort_keys=True,
                             separators=(",", ":"), ensure_ascii=True)
        return hashlib.sha256(payload.encode("ascii")).hexdigest(), payload
    except (OSError, UnicodeError, ValueError, topology.TopologyError):
        return None


def run_with_context(argv: Sequence[str] | None = None) -> int:
    """CLI framing only; main() remains the compatible ratchet entry point.

    Context failure or change makes attribution NON_COMPARABLE, never a pass.
    It does not suppress or replace the underlying validator's exit status.
    Before/after agreement is not a signature or an atomic filesystem snapshot.
    """
    args = _parser().parse_args(argv)
    before = _context_record(args.repo_root, args.baseline)
    if before is None:
        print("TOPOLOGY_CONTEXT_BEGIN status=UNAVAILABLE")
    else:
        print(f"TOPOLOGY_CONTEXT_BEGIN id={before[0]} payload={before[1]}")
    code = None
    try:
        code = main(argv)
        return code
    finally:
        after = _context_record(args.repo_root, args.baseline)
        exit_label = str(code) if type(code) is int and code in (0, 1, 2) else "UNKNOWN"
        if before is not None and after == before:
            print(f"TOPOLOGY_CONTEXT_END status=UNCHANGED id={before[0]} validator_exit={exit_label}")
        else:
            print(f"TOPOLOGY_CONTEXT_END status=NON_COMPARABLE validator_exit={exit_label}")


if __name__ == "__main__":
    raise SystemExit(run_with_context())
