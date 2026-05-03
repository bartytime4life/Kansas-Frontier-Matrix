#!/usr/bin/env python3
"""KFM material-change detector and provenance signer.

Requires: Python 3 + requests + cosign installed in PATH.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

SOURCES_FILE = Path("sources.json")
LAST_META_DIR = Path(".last_meta")
EVIDENCE_FILE = Path("evidencebundle.json")
DECISION_FILE = Path("decision_log.json")
RUN_RECEIPT_FILE = Path("run_receipt.json")


class RunnerError(Exception):
    """Fail-closed runtime error."""


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_json(path: Path, obj: Any) -> None:
    path.write_text(canonical_json(obj) + "\n", encoding="utf-8")


def load_sources(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        raise RunnerError(f"Missing required input file: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RunnerError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, list):
        raise RunnerError("sources.json must contain a JSON array")
    required = {"id", "source_url", "access_method", "materiality_rule"}
    for i, src in enumerate(data):
        if not isinstance(src, dict):
            raise RunnerError(f"sources[{i}] must be an object")
        missing = sorted(required - set(src.keys()))
        if missing:
            raise RunnerError(f"sources[{i}] missing required keys: {', '.join(missing)}")
        if not all(isinstance(src[k], str) and src[k].strip() for k in required):
            raise RunnerError(f"sources[{i}] required keys must be non-empty strings")
    return data


def read_legacy_meta(source_id: str) -> Dict[str, Optional[str]]:
    return {
        "etag": (LAST_META_DIR / f"{source_id}.etag").read_text(encoding="utf-8").strip()
        if (LAST_META_DIR / f"{source_id}.etag").exists()
        else None,
        "last_modified": (LAST_META_DIR / f"{source_id}.last_modified").read_text(encoding="utf-8").strip()
        if (LAST_META_DIR / f"{source_id}.last_modified").exists()
        else None,
        "spec_hash": (LAST_META_DIR / f"{source_id}.spec_hash").read_text(encoding="utf-8").strip()
        if (LAST_META_DIR / f"{source_id}.spec_hash").exists()
        else None,
    }


def fetch_headers_with_retry(url: str, timeout_sec: int = 20, retries: int = 2) -> Tuple[Optional[str], Optional[str]]:
    sess = requests.Session()
    methods = ["HEAD", "GET"]
    last_error: Optional[Exception] = None
    for method in methods:
        for attempt in range(retries + 1):
            try:
                resp = sess.request(method, url, timeout=timeout_sec, allow_redirects=True, stream=(method == "GET"))
                if resp.status_code >= 500:
                    raise RunnerError(f"Upstream server error {resp.status_code} for {url}")
                if resp.status_code >= 400:
                    if method == "HEAD" and resp.status_code in (405, 501):
                        break
                    raise RunnerError(f"Upstream request failed {resp.status_code} for {url}")
                etag = resp.headers.get("ETag")
                last_mod = resp.headers.get("Last-Modified")
                return etag, last_mod
            except requests.RequestException as exc:
                last_error = exc
                if attempt == retries:
                    if method == "HEAD":
                        break
                    raise RunnerError(f"Network error for {url}: {exc}") from exc
    if last_error:
        raise RunnerError(f"Network error for {url}: {last_error}")
    raise RunnerError(f"Unable to query source headers for {url}")


def parse_cosign_identity(output: str) -> str:
    for line in output.splitlines():
        m = re.search(r"(?i)(certificate identity|subject|issuer):\s*(.+)", line)
        if m:
            return m.group(2).strip()
    return output.strip() or "unknown"


def run_cosign_sign(blob_path: str, bundle_path: str, ci_mode: bool) -> str:
    cmd = ["cosign", "sign-blob", blob_path, "--bundle", bundle_path]
    env = os.environ.copy()
    if ci_mode:
        # Best-effort non-interactive defaults for CI keyless flows.
        env.setdefault("COSIGN_YES", "true")
    try:
        proc = subprocess.run(cmd, check=False, text=True, capture_output=True, env=env)
    except FileNotFoundError as exc:
        raise RunnerError("cosign not found in PATH; install cosign before running.") from exc
    combined = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if proc.returncode != 0:
        hint = (
            "cosign sign-blob failed. Ensure CI has keyless OIDC enabled (recommended in GitHub Actions) "
            "or configure a local cosign key. Re-run with --ci-mode in CI environments."
        )
        raise RunnerError(f"{hint}\nCommand: {' '.join(cmd)}\nOutput:\n{combined.strip()}")
    return parse_cosign_identity(combined)


def main() -> int:
    parser = argparse.ArgumentParser(description="KFM material-change detector with provenance signing")
    parser.add_argument("--ci-mode", action="store_true", help="Attempt non-interactive cosign keyless flow for CI")
    args = parser.parse_args()

    sources = load_sources(SOURCES_FILE)
    run_id = str(uuid.uuid4())
    changed = False
    source_rows: List[Dict[str, Any]] = []
    pending_meta: Dict[str, Dict[str, Optional[str]]] = {}

    for src in sources:
        sid = src["id"]
        etag, last_mod = fetch_headers_with_retry(src["source_url"])
        prev = read_legacy_meta(sid)
        candidate_spec_hash = None
        if "expected_spec" in src:
            candidate_spec_hash = sha256_hex(canonical_json(src["expected_spec"]))
        src_changed = False
        if etag != prev["etag"] or last_mod != prev["last_modified"]:
            src_changed = True
        if candidate_spec_hash is not None and candidate_spec_hash != prev["spec_hash"]:
            src_changed = True
        changed = changed or src_changed

        source_rows.append(
            {
                "id": sid,
                "source_url": src["source_url"],
                "access_method": src["access_method"],
                "last_modified": last_mod if last_mod is not None else None,
                "etag": etag if etag is not None else None,
                "dataset_version": None,
                "candidate_spec_hash": candidate_spec_hash,
            }
        )
        pending_meta[sid] = {"etag": etag, "last_modified": last_mod, "spec_hash": candidate_spec_hash}

    if not changed:
        print("NO_MATERIAL_CHANGE")
        return 0

    bundle_id = str(uuid.uuid4())
    ts = now_utc_iso()
    evidence = {
        "schema_version": "kfm.v1",
        "bundle_id": bundle_id,
        "generated": ts,
        "kfm:spec_hash": "",
        "sources": source_rows,
        "payload_summary": {"rows": None, "geometry_bounds": None, "notes": None},
        "obligations": [],
        "provenance": {"runner": "kfm_material_change_runner.py", "run_id": run_id},
    }
    evidence["kfm:spec_hash"] = sha256_hex(canonical_json(evidence))
    kfm_spec_hash = evidence["kfm:spec_hash"]

    decision = {
        "decision_id": str(uuid.uuid4()),
        "timestamp": ts,
        "policy_query": "material_change_detector/v1",  # Wire policy endpoint integration here if externalized.
        "input_ref": {"bundle_id": bundle_id, "kfm:spec_hash": kfm_spec_hash},
        "result": {"allow": True, "reason": "material_change_detected"},
        "obligations": [],
        "explain_trace": "auto:etag_or_spec_hash_change",
    }

    run_receipt = {
        "run_id": run_id,
        "timestamp": ts,
        "evidence_bundle_id": bundle_id,
        "kfm:spec_hash": kfm_spec_hash,
        "artifacts": {"evidencebundle": "evidencebundle.json", "decision_log": "decision_log.json"},
        "signed_by": None,
        "signature_bundle": None,
    }

    for field in ("schema_version", "bundle_id", "generated", "kfm:spec_hash", "sources"):
        if evidence.get(field) in (None, ""):
            raise RunnerError(f"Missing required evidence field: {field}")

    write_json(EVIDENCE_FILE, evidence)
    write_json(DECISION_FILE, decision)
    write_json(RUN_RECEIPT_FILE, run_receipt)

    signer1 = run_cosign_sign("evidencebundle.json", "evidencebundle.bundle", args.ci_mode)
    signer2 = run_cosign_sign("decision_log.json", "decision_log.bundle", args.ci_mode)

    run_receipt["signed_by"] = signer1 if signer1 == signer2 else f"{signer1} | {signer2}"
    run_receipt["signature_bundle"] = {
        "evidencebundle": "evidencebundle.bundle",
        "decision_log": "decision_log.bundle",
    }
    run_receipt["fingerprint"] = sha256_hex(canonical_json(run_receipt))
    write_json(RUN_RECEIPT_FILE, run_receipt)

    LAST_META_DIR.mkdir(parents=True, exist_ok=True)
    for sid, meta in pending_meta.items():
        write_json(LAST_META_DIR / f"{sid}.json", meta)

    # Wire catalog upload of bundle/receipt here if your pipeline publishes artifacts upstream.
    print(f"MATERIAL_CHANGE_EMITTED bundle_id={bundle_id} kfm_spec_hash={kfm_spec_hash} run_receipt=run_receipt.json")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)

# --- Example sources.json ---
# [
#   {
#     "id": "county_boundaries",
#     "source_url": "https://example.org/data/county.geojson",
#     "access_method": "http",
#     "expected_spec": {"type": "FeatureCollection", "crs": "EPSG:4326"},
#     "materiality_rule": "etag_or_spec_hash"
#   }
# ]
#
# --- Example .github/workflows/material-change.yml ---
# name: material-change
# on: [push, workflow_dispatch]
# jobs:
#   detect:
#     runs-on: ubuntu-latest
#     permissions:
#       id-token: write
#       contents: read
#     steps:
#       - uses: actions/checkout@v4
#       - uses: actions/setup-python@v5
#         with:
#           python-version: "3.11"
#       - run: pip install requests
#       - run: curl -sSL https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64 -o /usr/local/bin/cosign && chmod +x /usr/local/bin/cosign
#       - run: python kfm_material_change_runner.py --ci-mode
#       - name: Upload artifacts
#         if: always()
#         uses: actions/upload-artifact@v4
#         with:
#           name: kfm-material-change
#           path: |
#             evidencebundle.json
#             decision_log.json
#             run_receipt.json
#             *.bundle
