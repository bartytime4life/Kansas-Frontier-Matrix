from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from collections.abc import Mapping
from pathlib import Path


SCHEMA_NAME = "evidence_drawer_payload.schema.json"
DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
BASELINE_RELATIVE_PATH = Path(
    "tools/validators/evidence_drawer_schema_family_baseline.json"
)
BASELINE_REPOSITORY_PATH = BASELINE_RELATIVE_PATH.as_posix()
ANCHORS = {
    "evidence": Path("schemas/contracts/v1/evidence") / SCHEMA_NAME,
    "runtime": Path("schemas/contracts/v1/runtime") / SCHEMA_NAME,
    "ui": Path("schemas/contracts/v1/ui") / SCHEMA_NAME,
}

REFERENCE_ONLY_KEYS = frozenset(
    {
        "$comment",
        "$id",
        "$ref",
        "$schema",
        "default",
        "deprecated",
        "description",
        "examples",
        "readOnly",
        "title",
        "writeOnly",
        "x-kfm",
    }
)
BASELINE_KEYS = frozenset(
    {
        "authority",
        "closure_ref",
        "entries",
        "generated_from_ref",
        "non_effects",
        "schema_version",
    }
)
BASELINE_NON_EFFECTS = [
    "does_not_select_canonical_authority",
    "does_not_accept_adr_0037",
    "does_not_waive_new_removed_or_changed_family_members",
    "does_not_authorize_migration_review_release_deployment_promotion_or_publication",
]
SHAPE_CLASSES = frozenset(
    {
        "closed-ui-profile-candidate",
        "domain-local-shape-scaffold",
        "local-shape-profile",
        "permissive-empty-scaffold",
        "reference-only-profile",
    }
)
FULL_SHA256 = re.compile(r"sha256:[0-9a-f]{64}")
MAIN_REF = re.compile(r"main@[0-9a-f]{40}")
TRUSTED_REF = re.compile(r"[A-Za-z0-9_./^~:-]{1,200}")
PUBLIC_AUDIT_FIELDS = (
    "outcome",
    "placement_state",
    "reason_codes",
    "schema_count",
    "shape_state",
    "baseline_state",
    "baseline_entry_count",
    "trusted_baseline_state",
    "boundary",
)


class ConvergenceError(ValueError):
    """A stable, non-sensitive failure at the schema-family trust boundary."""


def _load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"schema must be a JSON object: {path.as_posix()}")
    return data


def _shape_class(relative: Path, document: dict) -> str:
    has_ref = isinstance(document.get("$ref"), str) and bool(document.get("$ref"))
    has_local_shape = any(key not in REFERENCE_ONLY_KEYS for key in document)
    properties = document.get("properties")

    if has_ref and not has_local_shape:
        return "reference-only-profile"
    if (
        relative == ANCHORS["ui"]
        and isinstance(properties, dict)
        and bool(properties)
        and document.get("additionalProperties") is False
    ):
        return "closed-ui-profile-candidate"
    if (
        isinstance(properties, dict)
        and not properties
        and document.get("additionalProperties") is True
    ):
        return "permissive-empty-scaffold"
    if (
        relative.as_posix().startswith("schemas/contracts/v1/domains/")
        and isinstance(properties, dict)
        and bool(properties)
    ):
        return "domain-local-shape-scaffold"
    return "local-shape-profile"


def _document_fingerprint(document: dict) -> str:
    canonical = json.dumps(
        document,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _validate_family_baseline(data: dict) -> tuple[dict[str, dict], list[str]]:
    """Validate and index one already-decoded family baseline."""

    if set(data) != BASELINE_KEYS:
        return {}, ["baseline top-level shape is invalid"]
    if data.get("schema_version") != "kfm.evidence-drawer-schema-family-baseline.v1":
        return {}, ["baseline schema_version is not supported"]
    if data.get("authority") != "implementation_inventory_only":
        return {}, ["baseline authority is invalid"]
    if not isinstance(data.get("generated_from_ref"), str) or not MAIN_REF.fullmatch(
        data["generated_from_ref"]
    ):
        return {}, ["baseline generated_from_ref is invalid"]
    if data.get("closure_ref") != (
        "https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3368"
    ):
        return {}, ["baseline closure_ref is invalid"]
    if data.get("non_effects") != BASELINE_NON_EFFECTS:
        return {}, ["baseline non_effects are invalid"]
    entries = data.get("entries")
    if not isinstance(entries, list):
        return {}, ["baseline entries must be an array"]

    indexed: dict[str, dict] = {}
    errors: list[str] = []
    prior_subject = ""
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict) or set(entry) != {
            "document_fingerprint",
            "path",
            "shape_class",
        }:
            errors.append(f"entry {index} must be an object")
            continue
        subject = entry.get("path")
        shape_class = entry.get("shape_class")
        fingerprint = entry.get("document_fingerprint")
        parsed = Path(subject) if isinstance(subject, str) else None
        if (
            parsed is None
            or parsed.is_absolute()
            or parsed.as_posix() != subject
            or ".." in parsed.parts
            or parsed.name != SCHEMA_NAME
            or parsed.parts[:3] != ("schemas", "contracts", "v1")
        ):
            errors.append(f"entry {index} path is invalid")
            continue
        if subject <= prior_subject:
            errors.append(f"entry {index} path is duplicate or out of order")
            continue
        prior_subject = subject
        if shape_class not in SHAPE_CLASSES:
            errors.append(f"entry {index} shape_class is invalid")
            continue
        if not isinstance(fingerprint, str) or not FULL_SHA256.fullmatch(fingerprint):
            errors.append(f"entry {index} document_fingerprint is invalid")
            continue
        indexed[subject] = entry
    return indexed, sorted(errors)


def _load_family_baseline(
    path: Path,
) -> tuple[dict, dict[str, dict], list[str]]:
    try:
        data = _load_json(path)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return {}, {}, [
            "baseline file is missing, unreadable, malformed, or not an object"
        ]
    indexed, errors = _validate_family_baseline(data)
    return data, indexed, errors


def validate_baseline_transition(
    current_data: Mapping[str, object],
    current_entries: Mapping[str, Mapping[str, object]],
    trusted_data: Mapping[str, object],
    trusted_entries: Mapping[str, Mapping[str, object]],
) -> None:
    """Freeze the inventory until a separately accepted authority change exists."""

    added = sorted(set(current_entries) - set(trusted_entries))
    if added:
        raise ConvergenceError("family baseline transition adds schema members")
    removed = sorted(set(trusted_entries) - set(current_entries))
    if removed:
        raise ConvergenceError("family baseline transition removes schema members")
    changed = sorted(
        path
        for path in set(current_entries).intersection(trusted_entries)
        if current_entries[path] != trusted_entries[path]
    )
    if changed:
        raise ConvergenceError("family baseline transition changes schema members")
    protected = BASELINE_KEYS - {"entries"}
    if any(current_data.get(field) != trusted_data.get(field) for field in protected):
        raise ConvergenceError("family baseline transition changes protected metadata")


def _git(repo_root: Path, *args: str) -> bytes:
    try:
        process = subprocess.run(
            ["git", "-C", str(repo_root), *args],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ConvergenceError("trusted family baseline git check failed") from exc
    if process.returncode != 0:
        raise ConvergenceError("trusted family baseline git check failed")
    return process.stdout


def _trusted_family_inventory(repo_root: Path, trusted_sha: str) -> dict[str, dict]:
    try:
        raw_paths = _git(
            repo_root,
            "ls-tree",
            "-r",
            "-z",
            "--name-only",
            trusted_sha,
            "--",
            "schemas/contracts/v1",
        )
        paths = sorted(
            path.decode("utf-8")
            for path in raw_paths.split(b"\0")
            if path and Path(path.decode("utf-8")).name == SCHEMA_NAME
        )
    except (ConvergenceError, UnicodeError) as exc:
        raise ConvergenceError("trusted schema family inventory cannot be read") from exc

    inventory: dict[str, dict] = {}
    for path in paths:
        relative = Path(path)
        if (
            relative.is_absolute()
            or relative.as_posix() != path
            or ".." in relative.parts
            or relative.parts[:3] != ("schemas", "contracts", "v1")
        ):
            raise ConvergenceError("trusted schema family path is invalid")
        try:
            document = json.loads(_git(repo_root, "show", f"{trusted_sha}:{path}"))
        except (ConvergenceError, UnicodeError, json.JSONDecodeError) as exc:
            raise ConvergenceError("trusted schema family member is unreadable") from exc
        if not isinstance(document, dict):
            raise ConvergenceError("trusted schema family member is not an object")
        inventory[path] = {
            "path": path,
            "shape_class": _shape_class(relative, document),
            "document_fingerprint": _document_fingerprint(document),
        }
    return inventory


def enforce_trusted_baseline(
    repo_root: Path,
    current_data: Mapping[str, object],
    current_entries: Mapping[str, Mapping[str, object]],
    trusted_ref: str,
) -> None:
    if not TRUSTED_REF.fullmatch(trusted_ref) or trusted_ref.startswith("-"):
        raise ConvergenceError("trusted family baseline ref is invalid")
    try:
        trusted_sha = _git(
            repo_root, "rev-parse", "--verify", f"{trusted_ref}^{{commit}}"
        ).decode("ascii").strip()
    except (ConvergenceError, UnicodeError) as exc:
        raise ConvergenceError("trusted family baseline ref cannot be resolved") from exc
    if not re.fullmatch(r"[0-9a-f]{40}", trusted_sha):
        raise ConvergenceError("trusted family baseline ref did not resolve to a commit")

    try:
        raw = _git(repo_root, "show", f"{trusted_sha}:{BASELINE_REPOSITORY_PATH}")
    except ConvergenceError:
        if current_data.get("generated_from_ref") != f"main@{trusted_sha}":
            raise ConvergenceError(
                "trusted family baseline is missing outside the governed bootstrap"
            )
        if dict(current_entries) != _trusted_family_inventory(repo_root, trusted_sha):
            raise ConvergenceError(
                "bootstrap family baseline does not match trusted schema inventory"
            )
        return

    try:
        trusted_data = json.loads(raw.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ConvergenceError("trusted family baseline is malformed") from exc
    if not isinstance(trusted_data, dict):
        raise ConvergenceError("trusted family baseline is not an object")
    trusted_entries, trusted_errors = _validate_family_baseline(trusted_data)
    if trusted_errors:
        raise ConvergenceError("trusted family baseline is invalid")
    validate_baseline_transition(
        current_data,
        current_entries,
        trusted_data,
        trusted_entries,
    )


def audit(
    repo_root: Path,
    *,
    baseline_path: Path | None = None,
    trusted_baseline_ref: str | None = None,
) -> dict:
    schema_root = repo_root / "schemas/contracts/v1"
    paths = sorted(schema_root.rglob(SCHEMA_NAME))
    findings: list[dict] = []

    if not paths:
        return {
            "outcome": "ERROR",
            "placement_state": "NEEDS_REVIEW",
            "reason_codes": ["NO_EVIDENCE_DRAWER_SCHEMAS"],
            "schemas": [],
        }

    relative_paths = [path.relative_to(repo_root) for path in paths]
    missing_anchors = [
        role for role, relative in ANCHORS.items() if relative not in relative_paths
    ]

    documents: list[tuple[Path, dict]] = []
    parse_errors: list[str] = []
    for relative, path in zip(relative_paths, paths):
        try:
            documents.append((relative, _load_json(path)))
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            parse_errors.append(relative.as_posix())

    schema_ids = [
        document.get("$id")
        for _, document in documents
        if isinstance(document.get("$id"), str) and document.get("$id")
    ]
    duplicate_ids = sorted(
        schema_id for schema_id, count in Counter(schema_ids).items() if count > 1
    )

    invalid_drafts = sorted(
        relative.as_posix()
        for relative, document in documents
        if document.get("$schema") != DRAFT_2020_12
    )
    missing_ids = sorted(
        relative.as_posix()
        for relative, document in documents
        if not isinstance(document.get("$id"), str) or not document.get("$id")
    )

    for relative, document in documents:
        metadata = document.get("x-kfm")
        metadata = metadata if isinstance(metadata, dict) else {}
        properties = document.get("properties")
        property_count = len(properties) if isinstance(properties, dict) else None
        path_text = relative.as_posix()
        if relative == ANCHORS["evidence"]:
            role = "evidence-family-placement-candidate"
        elif relative == ANCHORS["runtime"]:
            role = "runtime-compatibility-or-placement-candidate"
        elif relative == ANCHORS["ui"]:
            role = "ui-public-safe-profile"
        elif path_text.startswith("schemas/contracts/v1/domains/"):
            role = "domain-profile-or-scaffold"
        else:
            role = "other-profile"

        shape_class = _shape_class(relative, document)
        findings.append(
            {
                "path": path_text,
                "role": role,
                "shape_class": shape_class,
                "document_fingerprint": _document_fingerprint(document),
                "reference_target": document.get("$ref"),
                "schema_id": document.get("$id"),
                "status": metadata.get("status"),
                "contract_doc": metadata.get("contract_doc"),
                "additional_properties": document.get("additionalProperties"),
                "property_count": property_count,
            }
        )

    classification_counts = dict(
        sorted(Counter(entry["shape_class"] for entry in findings).items())
    )
    local_shape_paths = sorted(
        entry["path"]
        for entry in findings
        if entry["shape_class"] != "reference-only-profile"
    )
    reference_only_paths = sorted(
        entry["path"]
        for entry in findings
        if entry["shape_class"] == "reference-only-profile"
    )
    if parse_errors:
        shape_state = "INCOMPLETE"
    elif len(local_shape_paths) > 1:
        shape_state = "MULTIPLE_LOCAL_SHAPE_WRITERS"
    elif len(local_shape_paths) == 1:
        shape_state = "SINGLE_LOCAL_SHAPE_WRITER_CANDIDATE"
    else:
        shape_state = "REFERENCE_ONLY"

    reason_codes: list[str] = []
    if missing_anchors:
        reason_codes.append("MISSING_PLACEMENT_ANCHOR")
    if parse_errors:
        reason_codes.append("SCHEMA_PARSE_ERROR")
    if missing_ids:
        reason_codes.append("MISSING_SCHEMA_ID")
    if duplicate_ids:
        reason_codes.append("DUPLICATE_SCHEMA_ID")
    if invalid_drafts:
        reason_codes.append("UNEXPECTED_JSON_SCHEMA_DRAFT")

    baseline_state = "NOT_EVALUATED"
    baseline_errors: list[str] = []
    unbaselined_schema_paths: list[str] = []
    stale_baseline_paths: list[str] = []
    changed_baseline_paths: list[str] = []
    baseline_entry_count = 0
    trusted_baseline_state = "NOT_EVALUATED"
    trusted_baseline_errors: list[str] = []
    if baseline_path is not None:
        baseline_data, baseline, baseline_errors = _load_family_baseline(baseline_path)
        baseline_entry_count = len(baseline)
        if baseline_errors:
            baseline_state = "ERROR"
            reason_codes.append("SCHEMA_FAMILY_BASELINE_ERROR")
        else:
            current = {entry["path"]: entry for entry in findings}
            unbaselined_schema_paths = sorted(set(current) - set(baseline))
            stale_baseline_paths = sorted(set(baseline) - set(current))
            changed_baseline_paths = sorted(
                path
                for path in set(current).intersection(baseline)
                if (
                    current[path]["shape_class"] != baseline[path]["shape_class"]
                    or current[path]["document_fingerprint"]
                    != baseline[path]["document_fingerprint"]
                )
            )
            if unbaselined_schema_paths:
                reason_codes.append("UNBASELINED_SCHEMA_FAMILY_MEMBER")
            if stale_baseline_paths:
                reason_codes.append("STALE_SCHEMA_FAMILY_BASELINE")
            if changed_baseline_paths:
                reason_codes.append("SCHEMA_FAMILY_FINGERPRINT_CHANGED")
            baseline_state = "PASS" if not (
                unbaselined_schema_paths
                or stale_baseline_paths
                or changed_baseline_paths
            ) else "ERROR"
            if trusted_baseline_ref is not None and baseline_state == "PASS":
                try:
                    enforce_trusted_baseline(
                        repo_root,
                        baseline_data,
                        baseline,
                        trusted_baseline_ref,
                    )
                except ConvergenceError as exc:
                    trusted_baseline_state = "ERROR"
                    trusted_baseline_errors = [str(exc)]
                    reason_codes.append("SCHEMA_FAMILY_TRUSTED_BASELINE_ERROR")
                else:
                    trusted_baseline_state = "PASS"
        if trusted_baseline_ref is not None and baseline_state != "PASS":
            trusted_baseline_state = "ERROR"
            trusted_baseline_errors = [
                "current family baseline must pass before trusted comparison"
            ]
            if "SCHEMA_FAMILY_TRUSTED_BASELINE_ERROR" not in reason_codes:
                reason_codes.append("SCHEMA_FAMILY_TRUSTED_BASELINE_ERROR")

    return {
        "outcome": "PASS" if not reason_codes else "ERROR",
        "placement_state": "NEEDS_REVIEW",
        "reason_codes": reason_codes,
        "anchor_paths": {role: path.as_posix() for role, path in ANCHORS.items()},
        "schema_count": len(paths),
        "shape_state": shape_state,
        "classification_counts": classification_counts,
        "local_shape_paths": local_shape_paths,
        "reference_only_paths": reference_only_paths,
        "parse_errors": parse_errors,
        "missing_anchors": missing_anchors,
        "missing_ids": missing_ids,
        "duplicate_ids": duplicate_ids,
        "invalid_drafts": invalid_drafts,
        "baseline_path": (
            baseline_path.relative_to(repo_root).as_posix()
            if baseline_path is not None and baseline_path.is_relative_to(repo_root)
            else baseline_path.as_posix() if baseline_path is not None else None
        ),
        "baseline_state": baseline_state,
        "baseline_entry_count": baseline_entry_count,
        "baseline_errors": baseline_errors,
        "trusted_baseline_state": trusted_baseline_state,
        "trusted_baseline_errors": trusted_baseline_errors,
        "unbaselined_schema_paths": unbaselined_schema_paths,
        "stale_baseline_paths": stale_baseline_paths,
        "changed_baseline_paths": changed_baseline_paths,
        "schemas": findings,
        "boundary": (
            "Inventory, shape classification, and trusted-base family freeze only; it does not "
            "select a canonical schema, accept an ADR, migrate consumers, change contract "
            "meaning, or grant review, release, deployment, promotion, or publication authority."
        ),
    }


def public_audit_projection(
    result: Mapping[str, object],
) -> dict[str, object]:
    """Return the bounded, public-safe CLI and workflow projection."""

    return {field: result.get(field) for field in PUBLIC_AUDIT_FIELDS}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Audit EvidenceDrawerPayload schema-family convergence."
    )
    parser.add_argument("repo_root", nargs="?", default=".")
    parser.add_argument("--trusted-baseline-ref")
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    result = audit(
        repo_root,
        baseline_path=repo_root / BASELINE_RELATIVE_PATH,
        trusted_baseline_ref=args.trusted_baseline_ref,
    )
    print(json.dumps(public_audit_projection(result), indent=2, sort_keys=True))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
