#!/usr/bin/env python3
"""Offline fake of the exact cosign invocation used by fixture tests."""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path


def arg_value(name: str) -> str:
    try:
        return sys.argv[sys.argv.index(name) + 1]
    except (ValueError, IndexError):
        raise SystemExit(2)

if len(sys.argv) < 3 or sys.argv[1] != "verify-blob-attestation":
    raise SystemExit(2)
bundle_path = Path(arg_value("--bundle"))
predicate_type = arg_value("--type")
identity = arg_value("--certificate-identity")
issuer = arg_value("--certificate-oidc-issuer")
if "--offline" not in sys.argv:
    raise SystemExit(3)
subject_path = Path(sys.argv[-1])
bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
subject_digest = "sha256:" + hashlib.sha256(subject_path.read_bytes()).hexdigest()
checks = [
    bundle.get("verified") is True,
    bundle.get("subject_sha256") == subject_digest,
    bundle.get("predicate_type") == predicate_type,
    bundle.get("certificate_identity") == identity,
    bundle.get("certificate_oidc_issuer") == issuer,
    bundle.get("rekor_inclusion_verified") is True,
    bundle.get("signed_entry_timestamp_verified") is True,
]
print(json.dumps({"checks": len(checks), "verified": all(checks)}, sort_keys=True, separators=(",", ":")))
raise SystemExit(0 if all(checks) else 1)
