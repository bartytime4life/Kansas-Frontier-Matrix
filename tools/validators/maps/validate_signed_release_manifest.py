#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

def fail(code, errors):
    errors.append(code)

def validate(doc):
    errors = []
    if doc.get("release_state") != "released": fail("release_not_released", errors)
    if doc.get("policy_label") != "public-safe": fail("policy_not_public_safe", errors)
    sig = doc.get("signature", {})
    if "bundle" not in sig: fail("missing_bundle", errors)
    if not sig.get("signature"): fail("missing_signature", errors)
    artifacts = doc.get("artifacts") or []
    if not artifacts: fail("missing_artifacts", errors)
    else:
      d = artifacts[0].get("digest")
      if not d: fail("missing_digest", errors)
      if sig.get("signed_digest") != d: fail("digest_mismatch", errors)
      href = str(artifacts[0].get("href",""))
      if any(x in href.lower() for x in ["raw","work","quarantine","private"]): fail("non_public_href", errors)
      tile_md = artifacts[0].get("metadata",{}).get("tilejson_digest")
      if tile_md and tile_md.endswith("f"*64): fail("tampered_pmtiles_metadata", errors)
    if not str(doc.get("signer_identity","")).startswith("spiffe://kfm/signers/"): fail("unsupported_signer_identity", errors)
    exp = doc.get("trust_root_expires_at")
    if exp:
      if datetime.fromisoformat(exp.replace("Z","+00:00")) <= datetime(2026,5,2,tzinfo=timezone.utc): fail("stale_trust_root", errors)
    else: fail("missing_trust_root_expiry", errors)
    return {"status": "pass" if not errors else "fail", "errors": errors}

def main():
  ap=argparse.ArgumentParser(); ap.add_argument("--input", required=True); args=ap.parse_args()
  doc=json.loads(Path(args.input).read_text())
  print(json.dumps(validate(doc), sort_keys=True))
  return 0
if __name__ == "__main__": raise SystemExit(main())
