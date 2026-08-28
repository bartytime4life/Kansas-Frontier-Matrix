#!/usr/bin/env python3
"""Assemble one deterministic KFM release-support ProofPack candidate.

The assembler computes local SHA-256 digests and copies release/subject bindings
into each component. It never approves release, writes to canonical proof storage,
mutates lifecycle state, signs, deploys, or publishes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.proof_pack._common import load_json_object, resolve_regular_file, sha256_file
from tools.proof_pack.proof_pack_check import validate_payload

REQUIRED_TOP = frozenset(
    {"profile", "proof_pack_id", "release_id", "subject", "assembled_at", "components", "decision"}
)
REQUIRED_COMPONENT = frozenset({"kind", "artifact_id", "path", "recorded_at"})


def assemble_candidate(candidate_path: Path, *, repo_root: Path = REPO_ROOT) -> dict[str, object]:
    raw = load_json_object(candidate_path)
    if set(raw) != REQUIRED_TOP:
        raise ValueError("candidate top-level fields must exactly match the assembler contract")
    subject = raw.get("subject")
    components = raw.get("components")
    if not isinstance(subject, dict) or not isinstance(components, list):
        raise ValueError("candidate subject and components must have the expected types")
    subject_id = subject.get("subject_id")
    subject_spec_hash = subject.get("spec_hash")
    release_id = raw.get("release_id")
    if not all(isinstance(value, str) and value for value in (subject_id, subject_spec_hash, release_id)):
        raise ValueError("candidate release and subject bindings are required")

    assembled_components: list[dict[str, object]] = []
    for item in components:
        if not isinstance(item, dict) or set(item) != REQUIRED_COMPONENT:
            raise ValueError("candidate component fields must exactly match the assembler contract")
        path = resolve_regular_file(repo_root, item.get("path"))
        assembled_components.append(
            {
                "artifact_id": item["artifact_id"],
                "kind": item["kind"],
                "path": item["path"],
                "recorded_at": item["recorded_at"],
                "release_id": release_id,
                "sha256": sha256_file(path),
                "subject_id": subject_id,
                "subject_spec_hash": subject_spec_hash,
            }
        )
    assembled_components.sort(key=lambda item: (str(item["kind"]), str(item["artifact_id"]), str(item["path"])))

    result: dict[str, object] = {
        "assembled_at": raw["assembled_at"],
        "components": assembled_components,
        "decision": raw["decision"],
        "profile": raw["profile"],
        "proof_pack_id": raw["proof_pack_id"],
        "release_id": release_id,
        "subject": subject,
    }
    findings = validate_payload(result, repo_root=repo_root, verify_references=True)
    if findings:
        codes = ",".join(sorted({finding.code for finding in findings}))
        raise ValueError(f"assembled candidate failed ProofPack validation: {codes}")
    return result


def render_manifest(payload: Mapping[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.output.exists() and not args.force:
        raise SystemExit("output already exists; pass --force to replace it")
    try:
        payload = assemble_candidate(args.candidate, repo_root=args.repo_root)
    except (OSError, ValueError) as exc:
        print(f"PROOF_PACK_ASSEMBLY_FAIL reason={exc}", file=sys.stderr)
        return 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_manifest(payload), encoding="utf-8")
    print(f"PROOF_PACK_CANDIDATE_BUILT file={args.output.name} release_authority=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
