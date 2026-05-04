import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def main() -> int:
    errors = []
    evidence_ref = load("fixtures/evidence/evidence_ref.valid.json")
    evidence_bundle = load("fixtures/evidence/evidence_bundle.valid.json")
    source = load("fixtures/source/source_descriptor.valid.json")
    drawer = load("fixtures/ui/evidence_drawer_payload.valid.json")
    release = load("release/dry_runs/synthetic_hydrology_release_manifest.json")

    if evidence_ref.get("bundle_id") != evidence_bundle.get("id"):
        errors.append("EvidenceRef does not resolve to EvidenceBundle")
    if evidence_ref.get("id") not in evidence_bundle.get("evidence_refs", []):
        errors.append("EvidenceBundle missing EvidenceRef id")
    for k in ["source_role", "rights_status", "public_release_allowed", "activation_status", "no_network"]:
        if k not in source:
            errors.append(f"source descriptor missing {k}")
    if source.get("rights_status") == "UNKNOWN" and source.get("public_release_allowed") is True:
        errors.append("public release allowed with UNKNOWN rights")
    if source.get("activation_status") != "synthetic_only":
        errors.append("source activation_status must be synthetic_only")
    if source.get("no_network") is not True:
        errors.append("source descriptor must assert no_network")
    if drawer.get("evidence_ref") != evidence_ref.get("id"):
        errors.append("drawer evidence_ref mismatch")
    if drawer.get("evidence_bundle_id") != evidence_bundle.get("id"):
        errors.append("drawer evidence_bundle_id mismatch")
    if not release.get("included_evidence_bundle_ids"):
        errors.append("release missing included evidence bundles")
    if evidence_bundle.get("id") not in release.get("included_evidence_bundle_ids", []):
        errors.append("release missing valid evidence bundle")
    if release.get("result") not in {"READY_FOR_REVIEW", "DENY", "ABSTAIN", "ERROR"}:
        errors.append("release result is not finite")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS hydrology proof-slice hardening")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
