#!/usr/bin/env python3
"""Validate a local MapLibre source-metadata projection without network access.

The checked ``source.meta`` values are client hints only.  A passing result does
not prove source authority, rights, evidence closure, policy, review, release,
publication, or remote-byte integrity, and references are never resolved here.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import stat
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

TOOL = "validate-maplibre-source-metadata"
TOOL_VERSION = "1.0.0"
PROFILE = "kfm-maplibre-source-metadata-projection/v1"
REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "tests/fixtures/maplibre/source-metadata"

MAX_BYTES = 1_000_000
MAX_DEPTH = 64
MAX_NODES = 100_000
MAX_SOURCES = 1_000
MAX_FINDINGS = 200

DIGEST_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
QUARTER_RE = re.compile(r"^[0-9]{4}Q[1-4]$")
SOURCE_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,255}$")
OPAQUE_EPOCH_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
LICENSE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.+-]{0,127}$")
KFM_REF_RE = re.compile(r"^kfm://[A-Za-z0-9][A-Za-z0-9._~:/-]{2,509}$")

OUTCOME_EXIT_CODES = {"ALLOW": 0, "ABSTAIN": 2, "DENY": 3, "ERROR": 4}
RANK = {"ABSTAIN": 1, "DENY": 2, "ERROR": 3}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    pointer: str
    detail: str

    def as_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "pointer": self.pointer,
            "detail": self.detail,
        }


@dataclass(frozen=True)
class ValidationOptions:
    source_name: str | None = None
    require_proof: bool = False
    require_manifest_ref: bool = False
    strict_epoch: bool = False


@dataclass(frozen=True)
class ValidationReport:
    outcome: str
    style_ref: str
    manifest_ref: str | None
    style_sha256: str | None
    manifest_sha256: str | None
    checked_sources: tuple[str, ...]
    options: ValidationOptions
    findings: tuple[Finding, ...]

    @property
    def reason_codes(self) -> tuple[str, ...]:
        return tuple(sorted({finding.code for finding in self.findings}))

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool": TOOL,
            "tool_version": TOOL_VERSION,
            "profile": PROFILE,
            "outcome": self.outcome,
            "style_ref": self.style_ref,
            "manifest_ref": self.manifest_ref,
            "style_sha256": self.style_sha256,
            "manifest_sha256": self.manifest_sha256,
            "checked_sources": list(self.checked_sources),
            "options": {
                "source_name": self.options.source_name,
                "require_proof": self.options.require_proof,
                "require_manifest_ref": self.options.require_manifest_ref,
                "strict_epoch": self.options.strict_epoch,
            },
            "reason_codes": list(self.reason_codes),
            "findings": [finding.as_dict() for finding in self.findings],
            "boundary": [
                "The checked source metadata is a renderer projection, not source, evidence, policy, review, release, or publication authority.",
                "Reference syntax and digest equality do not prove object existence, admissibility, or remote-byte binding.",
                "The validator performs no network access and emits no lifecycle, receipt, proof, release, or published object.",
            ],
        }


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> Any:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _digest(payload: bytes) -> str:
    return f"sha256:{hashlib.sha256(payload).hexdigest()}"


def _complexity(value: Any) -> Finding | None:
    stack = [(value, 1)]
    nodes = 0
    while stack:
        current, depth = stack.pop()
        nodes += 1
        if nodes > MAX_NODES:
            return Finding("ERROR", "JSON_NODE_LIMIT", "/", "JSON node limit exceeded")
        if depth > MAX_DEPTH:
            return Finding("ERROR", "JSON_DEPTH_LIMIT", "/", "JSON depth limit exceeded")
        if isinstance(current, Mapping):
            stack.extend((item, depth + 1) for item in current.values())
        elif isinstance(current, list):
            stack.extend((item, depth + 1) for item in current)
    return None


def _load(path: Path, pointer: str) -> tuple[dict[str, Any] | None, str | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, None, [Finding("ERROR", "INPUT_SYMLINK_DENIED", pointer, "symbolic-link input denied")]
        info = path.stat()
        if not stat.S_ISREG(info.st_mode):
            return None, None, [Finding("ERROR", "INPUT_NOT_REGULAR_FILE", pointer, "input is not a regular file")]
        if info.st_size > MAX_BYTES:
            return None, None, [Finding("ERROR", "INPUT_TOO_LARGE", pointer, "JSON input exceeds one megabyte")]
        raw = path.read_bytes()
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except FileNotFoundError:
        return None, None, [Finding("ERROR", "INPUT_MISSING", pointer, "input file is missing")]
    except (OSError, UnicodeError):
        return None, None, [Finding("ERROR", "INPUT_UNREADABLE", pointer, "input could not be read safely")]
    except json.JSONDecodeError:
        return None, None, [Finding("ERROR", "JSON_INVALID", pointer, "input is not valid JSON")]
    except DuplicateKeyError:
        return None, None, [Finding("ERROR", "JSON_DUPLICATE_KEY", pointer, "duplicate JSON member name")]
    except NonFiniteNumberError:
        return None, None, [Finding("ERROR", "JSON_NONFINITE_NUMBER", pointer, "JSON number is non-finite")]
    except (RecursionError, ValueError):
        return None, None, [Finding("ERROR", "JSON_COMPLEXITY_LIMIT", pointer, "JSON parser complexity limit exceeded")]

    sha = _digest(raw)
    if not isinstance(value, dict):
        return None, sha, [Finding("DENY", "JSON_ROOT_NOT_OBJECT", pointer, "JSON root must be an object")]
    limit = _complexity(value)
    return (None, sha, [limit]) if limit else (value, sha, [])


def _safe(value: Any, limit: int = 4_096) -> bool:
    return (
        isinstance(value, str)
        and 0 < len(value) <= limit
        and value == value.strip()
        and not any(ord(character) < 32 or ord(character) == 127 for character in value)
    )


def _valid_digest(value: Any) -> bool:
    return (
        isinstance(value, str)
        and DIGEST_RE.fullmatch(value) is not None
        and set(value.removeprefix("sha256:")) != {"0"}
    )


def _iso(value: str) -> date | datetime | None:
    try:
        if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
            return date.fromisoformat(value)
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None
    except ValueError:
        return None


def _epoch(value: Any, strict: bool) -> bool:
    if not _safe(value, 256):
        return False
    assert isinstance(value, str)
    if QUARTER_RE.fullmatch(value):
        return True
    if "/" in value:
        if value.count("/") != 1:
            return False
        start, end = (_iso(part) for part in value.split("/", 1))
        if start is None or end is None or type(start) is not type(end):
            return False
        return start <= end
    if _iso(value) is not None:
        return True
    return not strict and OPAQUE_EPOCH_RE.fullmatch(value) is not None


def _license(value: Any) -> bool:
    if not _safe(value, 512):
        return False
    assert isinstance(value, str)
    if LICENSE_RE.fullmatch(value):
        return True
    parsed = urlsplit(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and parsed.username is None and parsed.password is None and not parsed.fragment


def _ref(value: Any) -> bool:
    if not _safe(value, 512):
        return False
    assert isinstance(value, str)
    if KFM_REF_RE.fullmatch(value):
        return True
    parsed = urlsplit(value)
    return (
        parsed.scheme == "https"
        and bool(parsed.netloc)
        and parsed.username is None
        and parsed.password is None
        and not parsed.query
        and not parsed.fragment
    )


def _ptr(name: str, field: str = "") -> str:
    escaped = name.replace("~", "~0").replace("/", "~1")
    return f"/sources/{escaped}{field}"


def _style(style: Mapping[str, Any], options: ValidationOptions) -> tuple[tuple[str, ...], dict[str, str], list[Finding]]:
    findings: list[Finding] = []
    if style.get("version") != 8:
        findings.append(Finding("DENY", "STYLE_VERSION_INVALID", "/version", "MapLibre style version must be 8"))
    sources = style.get("sources")
    if not isinstance(sources, dict) or not sources:
        return (), {}, findings + [Finding("DENY", "STYLE_SOURCES_MISSING", "/sources", "style must contain sources")]
    if len(sources) > MAX_SOURCES:
        return (), {}, findings + [Finding("DENY", "STYLE_SOURCE_LIMIT", "/sources", "source-count limit exceeded")]

    if options.source_name is not None:
        if options.source_name not in sources:
            return (), {}, findings + [Finding("DENY", "SOURCE_NOT_FOUND", "/sources", "requested source is absent")]
        names = [options.source_name]
    else:
        names = sorted(sources)

    checked: list[str] = []
    digests: dict[str, str] = {}
    for name in names:
        if SOURCE_NAME_RE.fullmatch(name) is None:
            findings.append(Finding("DENY", "SOURCE_NAME_INVALID", "/sources", "source name is outside the identifier grammar"))
            continue
        checked.append(name)
        source = sources[name]
        if not isinstance(source, dict):
            findings.append(Finding("DENY", "SOURCE_NOT_OBJECT", _ptr(name), "source must be an object"))
            continue
        meta = source.get("meta")
        if not isinstance(meta, dict):
            findings.append(Finding("DENY", "SOURCE_META_MISSING", _ptr(name, "/meta"), "source metadata object is required"))
            continue

        epoch = meta.get("epoch")
        if epoch is None:
            findings.append(Finding("DENY", "SOURCE_EPOCH_MISSING", _ptr(name, "/meta/epoch"), "epoch is required"))
        elif not _epoch(epoch, options.strict_epoch):
            findings.append(Finding("DENY", "SOURCE_EPOCH_INVALID", _ptr(name, "/meta/epoch"), "epoch is outside the accepted grammar"))

        license_value = meta.get("license")
        if license_value is None:
            findings.append(Finding("DENY", "SOURCE_LICENSE_MISSING", _ptr(name, "/meta/license"), "license hint is required"))
        elif not _license(license_value):
            findings.append(Finding("DENY", "SOURCE_LICENSE_INVALID", _ptr(name, "/meta/license"), "license hint is outside the accepted grammar"))

        digest = meta.get("digest")
        if digest is None:
            findings.append(Finding("DENY", "SOURCE_DIGEST_MISSING", _ptr(name, "/meta/digest"), "source digest is required"))
        elif not _valid_digest(digest):
            findings.append(Finding("DENY", "SOURCE_DIGEST_INVALID", _ptr(name, "/meta/digest"), "digest must be a non-placeholder lowercase SHA-256"))
        else:
            digests[name] = digest

        proof_ref = meta.get("proof_ref")
        if options.require_proof and proof_ref is None:
            findings.append(Finding("DENY", "SOURCE_PROOF_REF_REQUIRED", _ptr(name, "/meta/proof_ref"), "proof reference is required by this profile"))
        elif proof_ref is not None and not _ref(proof_ref):
            findings.append(Finding("DENY", "SOURCE_PROOF_REF_INVALID", _ptr(name, "/meta/proof_ref"), "proof reference is outside the accepted grammar"))

        manifest_ref = meta.get("manifest_ref")
        if options.require_manifest_ref and manifest_ref is None:
            findings.append(Finding("DENY", "SOURCE_MANIFEST_REF_REQUIRED", _ptr(name, "/meta/manifest_ref"), "manifest reference is required by this profile"))
        elif manifest_ref is not None and not _ref(manifest_ref):
            findings.append(Finding("DENY", "SOURCE_MANIFEST_REF_INVALID", _ptr(name, "/meta/manifest_ref"), "manifest reference is outside the accepted grammar"))

        if meta.get("freshness") is not None and not _safe(meta["freshness"], 128):
            findings.append(Finding("DENY", "SOURCE_FRESHNESS_INVALID", _ptr(name, "/meta/freshness"), "freshness hint is invalid"))
    return tuple(checked), digests, findings


def _manifest(manifest: Mapping[str, Any]) -> tuple[dict[str, str], list[Finding]]:
    findings: list[Finding] = []
    values = manifest.get("source_digests")
    if not isinstance(values, dict) or not values:
        return {}, [Finding("DENY", "MANIFEST_SOURCE_DIGESTS_MISSING", "/source_digests", "source_digests is required")]
    if len(values) > MAX_SOURCES:
        return {}, [Finding("DENY", "MANIFEST_SOURCE_LIMIT", "/source_digests", "source-count limit exceeded")]
    valid: dict[str, str] = {}
    for name in sorted(values):
        if SOURCE_NAME_RE.fullmatch(name) is None:
            findings.append(Finding("DENY", "MANIFEST_SOURCE_NAME_INVALID", "/source_digests", "manifest source name is invalid"))
        elif not _valid_digest(values[name]):
            findings.append(Finding("DENY", "MANIFEST_DIGEST_INVALID", f"/source_digests/{name}", "manifest digest is invalid"))
        else:
            valid[name] = values[name]
    if manifest.get("manifest_id") is not None and not _safe(manifest["manifest_id"], 512):
        findings.append(Finding("DENY", "MANIFEST_ID_INVALID", "/manifest_id", "manifest identifier is invalid"))
    return valid, findings


def _outcome(findings: Sequence[Finding]) -> str:
    return "ALLOW" if not findings else max(findings, key=lambda item: RANK[item.severity]).severity


def validate_source_metadata(
    style_path: Path,
    *,
    manifest_path: Path | None = None,
    options: ValidationOptions | None = None,
) -> ValidationReport:
    options = options or ValidationOptions()
    style, style_sha, findings = _load(style_path, "/style")
    manifest: dict[str, Any] | None = None
    manifest_sha: str | None = None
    if manifest_path is not None:
        manifest, manifest_sha, manifest_findings = _load(manifest_path, "/manifest")
        findings.extend(manifest_findings)

    checked: tuple[str, ...] = ()
    style_digests: dict[str, str] = {}
    if style is not None:
        checked, style_digests, style_findings = _style(style, options)
        findings.extend(style_findings)

    manifest_digests: dict[str, str] = {}
    if manifest is not None:
        manifest_digests, manifest_findings = _manifest(manifest)
        findings.extend(manifest_findings)

    if style is not None and manifest is not None:
        for name in checked:
            digest = style_digests.get(name)
            if digest is None:
                continue
            if name not in manifest_digests:
                findings.append(Finding("ABSTAIN", "MANIFEST_SOURCE_UNMAPPED", _ptr(name, "/meta/digest"), "manifest does not map the selected source"))
            elif digest != manifest_digests[name]:
                findings.append(Finding("DENY", "SOURCE_DIGEST_MISMATCH", _ptr(name, "/meta/digest"), "style digest does not match the manifest projection"))

    ordered = sorted(findings, key=lambda item: (item.code, item.pointer, item.detail))
    if len(ordered) > MAX_FINDINGS:
        ordered = ordered[:MAX_FINDINGS] + [Finding("ERROR", "FINDING_LIMIT", "/", "finding limit exceeded")]
    final = tuple(ordered)
    return ValidationReport(
        outcome=_outcome(final),
        style_ref=style_path.as_posix(),
        manifest_ref=manifest_path.as_posix() if manifest_path else None,
        style_sha256=style_sha,
        manifest_sha256=manifest_sha,
        checked_sources=checked,
        options=options,
        findings=final,
    )


def _fixture_path(root: Path, value: Any) -> Path | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    relative = PurePosixPath(value)
    if str(relative) != value or any(part in {".", ".."} for part in relative.parts):
        return None
    candidate = root.joinpath(*relative.parts)
    try:
        candidate.resolve(strict=False).relative_to(root.resolve(strict=True))
    except (OSError, ValueError):
        return None
    return candidate


def run_fixtures(root: Path = FIXTURE_ROOT) -> int:
    cases_doc, _sha, findings = _load(root / "cases.json", "/cases")
    if cases_doc is None:
        print(json.dumps({"tool": TOOL, "mode": "fixtures", "outcome": "ERROR", "reason_codes": sorted({item.code for item in findings})}, sort_keys=True))
        return 1
    cases = cases_doc.get("cases")
    if not isinstance(cases, list) or not cases:
        print(json.dumps({"tool": TOOL, "mode": "fixtures", "outcome": "ERROR", "reason_codes": ["FIXTURE_CASES_MISSING"]}, sort_keys=True))
        return 1

    failures: list[dict[str, Any]] = []
    seen: set[str] = set()
    passed = 0
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str):
            failures.append({"id": "<invalid>", "reason": "CASE_INVALID"})
            continue
        case_id = case["id"]
        if SOURCE_NAME_RE.fullmatch(case_id) is None or case_id in seen:
            failures.append({"id": "<invalid>", "reason": "CASE_ID_INVALID"})
            continue
        seen.add(case_id)
        style = _fixture_path(root, case.get("style"))
        manifest_value = case.get("manifest")
        manifest = _fixture_path(root, manifest_value) if manifest_value is not None else None
        if style is None or (manifest_value is not None and manifest is None):
            failures.append({"id": case_id, "reason": "CASE_PATH_INVALID"})
            continue
        flags = case.get("flags", {})
        allowed_flags = {"source_name", "require_proof", "require_manifest_ref", "strict_epoch"}
        if not isinstance(flags, dict) or set(flags) - allowed_flags:
            failures.append({"id": case_id, "reason": "CASE_FLAGS_INVALID"})
            continue
        report = validate_source_metadata(
            style,
            manifest_path=manifest,
            options=ValidationOptions(
                source_name=flags.get("source_name"),
                require_proof=flags.get("require_proof") is True,
                require_manifest_ref=flags.get("require_manifest_ref") is True,
                strict_epoch=flags.get("strict_epoch") is True,
            ),
        )
        expected_codes = case.get("expected_reason_codes")
        if not isinstance(expected_codes, list) or any(not isinstance(code, str) for code in expected_codes):
            failures.append({"id": case_id, "reason": "CASE_EXPECTATION_INVALID"})
        elif report.outcome != case.get("expected_outcome") or list(report.reason_codes) != sorted(expected_codes):
            failures.append({
                "id": case_id,
                "reason": "CASE_RESULT_MISMATCH",
                "expected_outcome": case.get("expected_outcome"),
                "actual_outcome": report.outcome,
                "expected_reason_codes": sorted(expected_codes),
                "actual_reason_codes": list(report.reason_codes),
            })
        else:
            passed += 1

    summary = {
        "tool": TOOL,
        "tool_version": TOOL_VERSION,
        "profile": PROFILE,
        "mode": "fixtures",
        "outcome": "PASS" if not failures else "FAIL",
        "case_count": len(cases),
        "passed": passed,
        "failed": len(failures),
        "failures": failures,
        "boundary": "Fixture polarity proves only the local projection grammar and digest-comparison behavior.",
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if not failures else 1


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description="Validate local MapLibre source metadata without network access.")
    value.add_argument("style", nargs="?", type=Path)
    value.add_argument("--manifest", type=Path)
    value.add_argument("--source", dest="source_name")
    value.add_argument("--require-proof", action="store_true")
    value.add_argument("--require-manifest-ref", action="store_true")
    value.add_argument("--strict-epoch", action="store_true")
    value.add_argument("--fixtures", action="store_true")
    value.add_argument("--fixture-root", type=Path, default=FIXTURE_ROOT)
    return value


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.fixtures:
        return run_fixtures(args.fixture_root)
    options = ValidationOptions(args.source_name, args.require_proof, args.require_manifest_ref, args.strict_epoch)
    if args.style is None:
        report = ValidationReport(
            "ERROR", "<missing>", args.manifest.as_posix() if args.manifest else None,
            None, None, (), options,
            (Finding("ERROR", "STYLE_ARGUMENT_REQUIRED", "/style", "a local style JSON path is required"),),
        )
    else:
        try:
            report = validate_source_metadata(args.style, manifest_path=args.manifest, options=options)
        except Exception:  # pragma: no cover - outer fail-closed guard
            report = ValidationReport(
                "ERROR", args.style.as_posix(), args.manifest.as_posix() if args.manifest else None,
                None, None, (), options,
                (Finding("ERROR", "UNCAUGHT_EXCEPTION", "/", "unexpected internal validator failure"),),
            )
    print(json.dumps(report.to_dict(), indent=2, sort_keys=True))
    return OUTCOME_EXIT_CODES[report.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
