"""ADR-0044 owner self-release: admitted public sources only; everything else keeps two-person review."""
import json
import re
from pathlib import Path

import pytest
from connectors_core.captured_json import canonical_bytes, digest_bytes
from hashing import compute_spec_hash
from policy_runtime.core import SELF_RELEASE_LICENSES, serving_gate
from release.water_projection import project

from pipelines.domains.hydrology.admission import DESCRIPTOR, load_admission
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.package import prepare_water_package
from tests.domains.hydrology.test_usgs_water_normalizer import acquired
from tests.packages.release.test_water_snapshot import NOW, synthetic_decision

ROOT = Path(__file__).resolve().parents[3]
SITE_GATE = ROOT / "apps/site/source/app/governed-water.ts"


def admitted_snapshot():
    raw = acquired()
    return prepare_water_package(normalize_capture(raw.manifest, raw.objects), admission=load_admission())


def owner_decision(snapshot, *, reviewer="@bartytime4life", releaser="@bartytime4life"):
    return dict(synthetic_decision(snapshot), reviewer=reviewer, releaser=releaser)


def evidence_of(snapshot):
    return json.loads(snapshot["artifacts"]["evidence.json"])


def reseal(snapshot, evidence):
    snapshot["artifacts"]["evidence.json"] = canonical_bytes(evidence).decode()
    snapshot["manifest"]["artifacts"]["evidence.json"] = digest_bytes(snapshot["artifacts"]["evidence.json"].encode())
    snapshot["manifest"]["package_id"] = compute_spec_hash({k: v for k, v in snapshot["manifest"].items() if k != "package_id"})
    return snapshot


def test_admitted_license_is_the_only_self_release_license_in_both_gates():
    admission = load_admission()
    assert SELF_RELEASE_LICENSES == {admission["license"]}
    site_list = re.search(r"SELF_RELEASE_LICENSES: readonly string\[\] = (\[.*?\]);", SITE_GATE.read_text()).group(1)
    assert json.loads(site_list) == [admission["license"]]


def test_admission_requires_an_approved_active_public_descriptor(tmp_path):
    descriptor = json.loads(DESCRIPTOR.read_text())
    for field, value in [("review_state", "needs_review"), ("sensitivity_default", "restricted")]:
        changed = dict(descriptor, **{field: value})
        path = tmp_path / f"{field}.json"
        path.write_text(json.dumps(changed))
        with pytest.raises(ValueError, match="SOURCE_NOT_ADMITTED"):
            load_admission(path)


def test_unadmitted_preparation_still_carries_the_hold():
    raw = acquired()
    evidence = evidence_of(prepare_water_package(normalize_capture(raw.manifest, raw.objects)))
    assert {e["bundle"]["sensitivity"]["level"] for e in evidence["entries"]} == {"quarantine"}
    assert all("review required" in e["bundle"]["rights"]["license"] for e in evidence["entries"])


@pytest.mark.parametrize("reviewer", ["@bartytime4life", "@independent-reviewer"])
def test_admitted_public_package_answers_for_owner_or_independent_review(reviewer):
    snapshot = admitted_snapshot()
    response = project(canonical_bytes(snapshot), owner_decision(snapshot, reviewer=reviewer), view="layers", now=NOW)
    assert response["envelope"]["outcome"] == "ANSWER"
    assert response["data"]


def test_unadmitted_package_still_requires_independent_review():
    raw = acquired()
    snapshot = prepare_water_package(normalize_capture(raw.manifest, raw.objects))
    evidence = evidence_of(snapshot)
    assert serving_gate(snapshot["manifest"], evidence, owner_decision(snapshot), now=NOW) == "INDEPENDENT_REVIEW_REQUIRED"


@pytest.mark.parametrize("mutation", ["sensitivity", "license"])
def test_one_non_public_or_unlisted_bundle_blocks_self_release(mutation):
    snapshot = admitted_snapshot()
    evidence = evidence_of(snapshot)
    bundle = evidence["entries"][-1]["bundle"]
    if mutation == "sensitivity":
        bundle["sensitivity"]["level"] = "restricted"
    else:
        bundle["rights"]["license"] = "U.S. Public Domain"
    bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
    snapshot = reseal(snapshot, evidence)
    assert serving_gate(snapshot["manifest"], evidence, owner_decision(snapshot), now=NOW) == "INDEPENDENT_REVIEW_REQUIRED"
    independent = owner_decision(snapshot, reviewer="@independent-reviewer")
    expected = "RIGHTS_OR_SENSITIVITY_HOLD" if mutation == "sensitivity" else "ELIGIBLE"
    assert serving_gate(snapshot["manifest"], evidence, independent, now=NOW) == expected
