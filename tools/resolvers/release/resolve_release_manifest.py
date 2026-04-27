#!/usr/bin/env python3
"""
Resolve KFM ReleaseManifest closure.

This resolver checks whether a ReleaseManifest can actually close over the
artifact, EvidenceBundle, PROV sidecar, STAC item, DCAT dataset, receipts, and
attestation references it declares.

Finite outcomes:
- PUBLISHABLE
- ABSTAIN
- DENY
- ERROR

Default behavior is offline / repo-local:
- kfm:// refs are treated as logical refs and require explicit mapping later.
- http(s) refs using example.invalid are accepted as fixture-safe placeholders.
- file paths are resolved relative to repo root.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


REPO_ROOT = Path.cwd()

VALIDATORS = {
    "release": Path("tools/validators/release/validate_release_manifest.py"),
    "prov": Path("tools/validators/provenance/validate_prov_sidecar.py"),
    "stac": Path("tools/validators/catalog/validate_stac_item.py"),
    "dcat": Path("tools/validators/catalog/validate_dcat_dataset.py"),
}

FINITE_STATUS = ("PUBLISHABLE", "ABSTAIN", "DENY", "ERROR")


@dataclass
class ClosureResult:
    status: str = "PUBLISHABLE"
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    resolved: dict[str, Any] = field(default_factory=dict)

    def deny(self, message: str) -> None:
        self.failures.append(message)
        if self.status not in {"ERROR", "DENY"}:
            self.status = "DENY"

    def abstain(self, message: str) -> None:
        self.failures.append(message)
        if self.status == "PUBLISHABLE":
            self.status = "ABSTAIN"

    def error(self, message: str) -> None:
        self.failures.append(message)
        self.status = "ERROR"

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def emit(result: ClosureResult) -> None:
    print(
        json.dumps(
            {
                "status": result.status,
                "failures": result.failures,
                "warnings": result.warnings,
                "resolved": result.resolved,
            },
            indent=2,
            sort_keys=True,
        )
    )


def is_http_ref(ref: str) -> bool:
    return urlparse(ref).scheme in {"http", "https"}


def is_kfm_ref(ref: str) -> bool:
    return ref.startswith("kfm://")


def is_fixture_http_placeholder(ref: str) -> bool:
    parsed = urlparse(ref)
    return parsed.scheme in {"http", "https"} and parsed.hostname == "example.invalid"


def ref_to_path(ref: str) -> Path | None:
    parsed = urlparse(ref)

    if parsed.scheme in {"", "file"}:
        raw_path = parsed.path if parsed.scheme == "file" else ref
        path = Path(raw_path)
        return path if path.is_absolute() else REPO_ROOT / path

    return None


def validate_with(script: Path, target: Path, result: ClosureResult, label: str) -> None:
    if not script.exists():
        result.warn(f"{label}: validator not found: {script}")
        return

    completed = subprocess.run(
        [sys.executable, str(script), str(target)],
        text=True,
        capture_output=True,
        check=False,
    )

    if completed.returncode != 0:
        stderr = completed.stderr.strip()
        stdout = completed.stdout.strip()
        detail = stderr or stdout or f"validator exited {completed.returncode}"
        result.deny(f"{label}: validation failed: {detail}")


def resolve_ref(
    ref: str | None,
    *,
    label: str,
    result: ClosureResult,
    required: bool = True,
    allow_fixture_placeholders: bool = True,
) -> Path | None:
    if not ref:
        if required:
            result.deny(f"{label}: missing reference")
        return None

    if is_kfm_ref(ref):
        result.warn(f"{label}: logical KFM ref requires repository resolver mapping: {ref}")
        result.resolved[label] = {"ref": ref, "mode": "logical"}
        return None

    if is_fixture_http_placeholder(ref) and allow_fixture_placeholders:
        result.resolved[label] = {"ref": ref, "mode": "fixture-placeholder"}
        return None

    if is_http_ref(ref):
        result.warn(f"{label}: remote URL not fetched in offline resolver mode: {ref}")
        result.resolved[label] = {"ref": ref, "mode": "remote-unchecked"}
        return None

    path = ref_to_path(ref)
    if path is None:
        result.deny(f"{label}: unsupported reference format: {ref}")
        return None

    if not path.exists():
        result.deny(f"{label}: path does not exist: {path}")
        return path

    result.resolved[label] = {"ref": ref, "mode": "path", "path": str(path)}
    return path


def infer_kind_from_path(path: Path) -> str | None:
    name = path.name.lower()

    if name.endswith(".prov.jsonld"):
        return "prov"

    if name.endswith(".item.json"):
        return "stac"

    if name.endswith(".dataset.jsonld"):
        return "dcat"

    if name.endswith(".release-manifest.json"):
        return "release"

    return None


def validate_resolved_path(path: Path | None, result: ClosureResult, label: str) -> None:
    if path is None:
        return

    kind = infer_kind_from_path(path)
    if kind is None:
        return

    validate_with(VALIDATORS[kind], path, result, label)


def check_artifact_entry(
    artifact: dict[str, Any],
    *,
    index: int,
    manifest_spec_hash: str | None,
    result: ClosureResult,
) -> None:
    label = f"artifacts[{index}]"

    artifact_ref = artifact.get("artifact_ref")
    spec_hash = artifact.get("spec_hash")
    evidence_ref = artifact.get("evidence_ref")
    provenance_ref = artifact.get("provenance_ref")
    stac_ref = artifact.get("stac_ref")
    dcat_ref = artifact.get("dcat_ref")
    run_receipt_ref = artifact.get("run_receipt_ref")
    attestation_ref = artifact.get("attestation_ref")

    if manifest_spec_hash and spec_hash != manifest_spec_hash:
        result.deny(f"{label}: spec_hash does not match manifest spec_hash")

    artifact_path = resolve_ref(
        artifact_ref,
        label=f"{label}.artifact_ref",
        result=result,
        required=True,
    )

    evidence_path = resolve_ref(
        evidence_ref,
        label=f"{label}.evidence_ref",
        result=result,
        required=True,
    )

    provenance_path = resolve_ref(
        provenance_ref,
        label=f"{label}.provenance_ref",
        result=result,
        required=True,
    )

    stac_path = resolve_ref(
        stac_ref,
        label=f"{label}.stac_ref",
        result=result,
        required=True,
    )

    dcat_path = resolve_ref(
        dcat_ref,
        label=f"{label}.dcat_ref",
        result=result,
        required=True,
    )

    run_receipt_path = resolve_ref(
        run_receipt_ref,
        label=f"{label}.run_receipt_ref",
        result=result,
        required=False,
    )

    attestation_path = resolve_ref(
        attestation_ref,
        label=f"{label}.attestation_ref",
        result=result,
        required=False,
    )

    for resolved_path, resolved_label in (
        (artifact_path, f"{label}.artifact_ref"),
        (evidence_path, f"{label}.evidence_ref"),
        (provenance_path, f"{label}.provenance_ref"),
        (stac_path, f"{label}.stac_ref"),
        (dcat_path, f"{label}.dcat_ref"),
        (run_receipt_path, f"{label}.run_receipt_ref"),
        (attestation_path, f"{label}.attestation_ref"),
    ):
        validate_resolved_path(resolved_path, result, resolved_label)


def resolve_release_manifest(manifest_path: Path) -> ClosureResult:
    result = ClosureResult()

    if not manifest_path.exists():
        result.error(f"ReleaseManifest not found: {manifest_path}")
        return result

    validate_with(VALIDATORS["release"], manifest_path, result, "release_manifest")

    try:
        manifest = load_json(manifest_path)
    except json.JSONDecodeError as exc:
        result.error(f"ReleaseManifest is not valid JSON: {exc}")
        return result

    if result.status == "DENY":
        return result

    manifest_spec_hash = manifest.get("spec_hash")
    artifacts = manifest.get("artifacts", [])

    if not artifacts:
        result.deny("ReleaseManifest contains no artifacts")
        return result

    for idx, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            result.deny(f"artifacts[{idx}]: entry must be an object")
            continue

        check_artifact_entry(
            artifact,
            index=idx,
            manifest_spec_hash=manifest_spec_hash,
            result=result,
        )

    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve KFM ReleaseManifest closure.",
    )
    parser.add_argument(
        "manifest",
        help="Path to release manifest JSON file.",
    )
    parser.add_argument(
        "--strict-remote",
        action="store_true",
        help="Reserved for future online URL resolution. Currently remote refs are warnings.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_path = Path(args.manifest)

    result = resolve_release_manifest(manifest_path)
    emit(result)

    if result.status == "PUBLISHABLE":
        sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()
