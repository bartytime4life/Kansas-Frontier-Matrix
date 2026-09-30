#!/usr/bin/env python3
"""Project every pinned scaffold finding into the existing verification backlog.

One entry per artifact reconciles duplicate detector markers. A populated queue
is an inventory, not proof of working behavior. Uninspected gaps retain HOLD.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = "6994a65843c4999313fda01183b63333213134f3"
BACKLOG = ROOT / "control_plane/verification_backlog.yaml"
DELIVERED_WATER_PATHS = {'pipelines/domains/hydrology/validate.py', 'packages/release/src/release/core.py', 'tests/domains/hydrology/test_usgs_water_normalizer.py', 'apps/governed-api/pyproject.toml', 'packages/policy-runtime/pyproject.toml', 'packages/catalog/src/catalog/core.py', 'apps/workers/src/catalog_worker/main.py', 'apps/workers/src/validate_worker/main.py', 'packages/release/pyproject.toml', 'schemas/contracts/v1/domains/hydrology/flow_observation.schema.json', 'packages/evidence-resolver/pyproject.toml', 'packages/policy-runtime/src/policy_runtime/core.py', 'apps/workers/src/ingest_worker/main.py', 'pipelines/domains/hydrology/normalize.py', 'packages/catalog/pyproject.toml'}
GOVERNING = ["docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md", "docs/doctrine/directory-rules.md", "tools/qa/scaffold_baseline.json"]


def blob(path):
    return subprocess.run(["git", "show", BASE + ":" + path], cwd=ROOT, check=True, capture_output=True).stdout


def digest(raw):
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def queue():
    baseline = json.loads(blob("tools/qa/scaffold_baseline.json"))
    grouped = defaultdict(list)
    for item in baseline["findings"]:
        grouped[item["path"]].append(item["kind"])
    shared = [digest(blob(path)) for path in GOVERNING]
    result = yaml.safe_load(BACKLOG.read_text())
    result.update(base_ref=BASE, completeness="partial", implementation_status="PARTIAL", owner_role="maintainer", entries=[])
    result["meta"].update(owner="maintainer", last_reviewed="2026-09-30", description="Pinned 949-marker inventory, reconciled to 747 artifact entries. Open entries are holds, not implemented capabilities.")
    for path, kinds in sorted(grouped.items()):
        root = path.split("/")[0]
        pilot = any(word in path for word in ("hydrology", "governed-api", "catalog", "release/", "policy-runtime", "evidence-resolver", "workers"))
        priority = "P1" if pilot else "P2" if root in {"connectors", "packages", "policy", "schemas"} else "P3"
        evidence = digest(blob(path))
        notes = {"priority": priority, "disposition": "retain_explicit_hold", "markers": sorted(kinds),
                 "current_behavior": "Pinned detector findings only; runtime behavior is not established by this inventory.",
                 "user_consequence": "Do not advertise this artifact as an operational capability until its consumer and behavior pass review.",
                 "dependencies": ["source-integrity", "evidence-review-release-boundary"] if pilot else ["water-pilot-acceptance", "owning-root-consumer-review"],
                 "next_change": "Inspect the owning consumer and choose a bounded implementation, consolidation or retirement with changed-area tests.",
                 "acceptance_command": "python tools/qa/completion_queue.py --check",
                 "expected_result": "All pinned markers accounted for; implementation acceptance additionally requires behavior tests, docs and rollback linked in the delivery review.",
                 "rollback": "Revert the isolated delivery patch; preserve historical receipts and source bytes."}
        if path in DELIVERED_WATER_PATHS:
            notes.update(disposition="implement", current_behavior="Bounded water-pilot implementation and declared consumer now exist; pinned marker evidence remains historical.",
                         next_change="Complete independent review, real-source governance and rendered acceptance; broader domain behavior remains held.",
                         acceptance_command="python -m pytest -q tests/packages/release tests/domains/hydrology/test_usgs_water_normalizer.py tests/connectors/usgs/water_data apps/governed-api/tests tests/tools/test_water_job.py",
                         expected_result="Changed-area water tests pass; no real source/release authority is conferred.",
                         delivery_docs="docs/runbooks/water-pilot.md")
        result["entries"].append({"entry_id": "gap-" + hashlib.sha256(path.encode()).hexdigest()[:24], "subject_id": "kfm://artifact/" + path,
            "kind": "scaffold_gap", "path": path, "path_sha256": evidence, "authority_status": "CONFIRMED", "implementation_status": "PARTIAL" if path in DELIVERED_WATER_PATHS else "NOT_INSPECTED",
            "owner_role": root.replace(".", "") + "_steward", "governing_refs": GOVERNING,
            "source_digests": sorted(set([evidence, *shared])), "reason_codes": sorted(kind.lower() for kind in kinds), "notes": json.dumps(notes, separators=(",", ":"))})
    result["entries"].sort(key=lambda e: e["entry_id"])
    return result, baseline


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true"); group.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    expected, baseline = queue()
    if args.write:
        BACKLOG.write_text(yaml.safe_dump(expected, sort_keys=False, allow_unicode=True, width=120))
    elif yaml.safe_load(BACKLOG.read_text()) != expected:
        print('{"outcome":"FAIL","reason_code":"QUEUE_DRIFT"}')
        return 1
    print(json.dumps({"outcome": "PASS", "pinned_markers": baseline["summary"]["total"], "artifact_entries": len(expected["entries"]), "authority": "projection_only"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
