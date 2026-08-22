#!/usr/bin/env python3
"""Validate the MRTS-04 governance-parity projection without granting authority.

The profile composes existing validator owners and the adopted topology engine.
It does not redefine their rules, mutate their baselines, or convert inherited
repository drift into conformance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.directory_governance import validate_repository_topology as topology


INSTANCE_PATH = REPO_ROOT / "control_plane/repository_governance_parity.yaml"
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/repository_governance_parity.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT / "fixtures/contracts/v1/governance/repository_governance_parity"
)
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_PINNED_BLOB_BYTES = 64 * 1024 * 1024
GIT_TIMEOUT_SECONDS = 15
LANE_TIMEOUT_SECONDS = 120
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")


class ParityError(ValueError):
    """Raised for unsafe or malformed profile inputs."""


class UniqueLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: UniqueLoader, node: yaml.MappingNode, deep: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise ParityError("YAML mapping keys must be unique strings")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code, "field": self.field}


LANE_SPECS: dict[str, tuple[str, str, tuple[str, ...] | None]] = {
    "control-plane-registry-packet": (
        "tools/validators/control_plane/validate_control_plane_registry_packet.py",
        "PASS",
        (sys.executable, "tools/validators/control_plane/validate_control_plane_registry_packet.py"),
    ),
    "object-family-register": (
        "tools/validators/control_plane/validate_object_family_register.py",
        "PASS",
        (sys.executable, "tools/validators/control_plane/validate_object_family_register.py"),
    ),
    "path-alias-register": (
        "tools/validators/directory_governance/validate_path_alias_register.py",
        "PASS",
        (sys.executable, "tools/validators/directory_governance/validate_path_alias_register.py"),
    ),
    "public-boundary-guards": (
        "apps/governed-api/tests/test_boundary_guards.py",
        "PASS",
        (
            sys.executable,
            "-m",
            "pytest",
            "-q",
            "--strict-config",
            "--strict-markers",
            "tests/policy/test_control_plane_register_meta_contract.py",
            "tests/policy/test_explorer_web_adapter_boundary.py",
            "tests/policy/test_pipeline_connector_non_publisher.py",
            "apps/governed-api/tests/test_boundary_guards.py",
        ),
    ),
    "repository-topology": (
        "tools/validators/directory_governance/validate_repository_topology.py",
        "HOLD_INHERITED",
        None,
    ),
    "root-registry": (
        "tools/validators/directory_governance/validate_root_registry.py",
        "PASS",
        (sys.executable, "tools/validators/directory_governance/validate_root_registry.py"),
    ),
}

EXPECTED_GOVERNING_PATHS = (
    "control_plane/path_alias_register.yaml",
    "control_plane/root_registry.yaml",
    "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md",
    "docs/doctrine/directory-rules.md",
    "tools/validators/directory_governance/repository_topology_baseline.json",
    "tools/validators/directory_governance/validate_repository_topology.py",
)

EXPECTED_COVERAGE: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "baseline_shrink_only": (("repository-topology",), ()),
    "check_not_run_never_passes": (tuple(sorted(LANE_SPECS)), ()),
    "duplicate_schema_and_authority_ids": (
        ("control-plane-registry-packet", "object-family-register", "repository-topology"),
        ("KFM-TOPO-015", "KFM-TOPO-016"),
    ),
    "generated_mirror_provenance": (("repository-topology",), ("KFM-TOPO-017",)),
    "path_grammar_root_and_alias_governance": (
        ("path-alias-register", "repository-topology", "root-registry"),
        tuple(f"KFM-TOPO-{index:03d}" for index in range(1, 12)) + ("KFM-TOPO-020",),
    ),
    "policy_source_placement": (
        ("repository-topology",),
        ("KFM-TOPO-012", "KFM-TOPO-018"),
    ),
    "public_runtime_and_lifecycle_boundary": (
        ("public-boundary-guards", "repository-topology"),
        ("KFM-TOPO-014",),
    ),
    "registry_reference_and_digest_integrity": (
        (
            "control-plane-registry-packet",
            "object-family-register",
            "path-alias-register",
            "root-registry",
        ),
        ("KFM-TOPO-019",),
    ),
    "trust_object_placement": (
        ("object-family-register", "repository-topology"),
        ("KFM-TOPO-013",),
    ),
}

REQUIRED_NON_EFFECTS = (
    "does_not_accept_or_amend_adr",
    "does_not_activate_source",
    "does_not_approve_policy_or_review",
    "does_not_authorize_migration_or_deletion",
    "does_not_expand_topology_baseline",
    "does_not_mutate_registry_or_lifecycle",
    "does_not_release_deploy_promote_or_publish",
    "does_not_turn_inherited_hold_into_pass",
)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ParityError("duplicate JSON key")
        result[key] = value
    return result


def _nonfinite(value: str) -> Any:
    raise ParityError(f"non-finite number: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ParityError("non-finite number")
    return parsed


def _load_yaml(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file() or not 0 < path.stat().st_size <= MAX_FILE_BYTES:
        raise ParityError("input file is missing, unsafe, empty, or oversized")
    try:
        value = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueLoader)
    except (OSError, UnicodeError, yaml.YAMLError, ParityError) as exc:
        raise ParityError("input YAML is invalid") from exc
    if not isinstance(value, dict):
        raise ParityError("input YAML root must be an object")
    return value


def _load_schema(path: Path = SCHEMA_PATH) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file() or not 0 < path.stat().st_size <= MAX_FILE_BYTES:
        raise ParityError("schema is missing, unsafe, empty, or oversized")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ParityError) as exc:
        raise ParityError("schema JSON is invalid") from exc
    if not isinstance(value, dict):
        raise ParityError("schema root must be an object")
    Draft202012Validator.check_schema(value)
    return value


def _git(repo_root: Path, *args: str, env: Mapping[str, str] | None = None) -> bytes:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo_root,
            env=dict(env) if env is not None else None,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            check=False,
            timeout=GIT_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ParityError("Git evidence read failed") from exc
    if result.returncode != 0:
        raise ParityError("Git evidence read failed")
    return result.stdout


def _resolve_commit(repo_root: Path, ref: str) -> str:
    if not FULL_SHA.fullmatch(ref):
        raise ParityError("base_ref is not a full commit SHA")
    try:
        resolved = _git(repo_root, "rev-parse", "--verify", f"{ref}^{{commit}}").decode("ascii").strip()
    except UnicodeError as exc:
        raise ParityError("base_ref did not resolve safely") from exc
    if resolved != ref:
        raise ParityError("base_ref did not resolve exactly")
    return resolved


def _read_pinned_blob(repo_root: Path, ref: str, path: str) -> bytes:
    parsed = PurePosixPath(path)
    if parsed.is_absolute() or parsed.as_posix() != path or ".." in parsed.parts:
        raise ParityError("governing path is unsafe")
    raw = _git(repo_root, "ls-tree", "-z", ref, "--", path)
    records = [item for item in raw.split(b"\0") if item]
    if len(records) != 1:
        raise ParityError("governing path is absent or ambiguous")
    try:
        header, name = records[0].split(b"\t", 1)
        mode, object_type, object_id = header.decode("ascii").split(" ")
        decoded_name = name.decode("utf-8")
    except (ValueError, UnicodeError) as exc:
        raise ParityError("governing tree entry is malformed") from exc
    if decoded_name != path or mode not in {"100644", "100755"} or object_type != "blob":
        raise ParityError("governing target is not a regular tracked file")
    try:
        size = int(_git(repo_root, "cat-file", "-s", object_id).decode("ascii").strip())
    except (ValueError, UnicodeError) as exc:
        raise ParityError("governing blob size is invalid") from exc
    if not 0 < size <= MAX_PINNED_BLOB_BYTES:
        raise ParityError("governing blob size is outside the budget")
    blob = _git(repo_root, "cat-file", "blob", object_id)
    if len(blob) != size:
        raise ParityError("governing blob read is incomplete")
    return blob


def _run_lane(command: tuple[str, ...], repo_root: Path) -> str:
    env = os.environ.copy()
    env.update(
        {
            "KFM_NO_NETWORK": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "PYTHONUNBUFFERED": "1",
            "TZ": "UTC",
        }
    )
    try:
        result = subprocess.run(
            command,
            cwd=repo_root,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
            timeout=LANE_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "ERROR"
    return "PASS" if result.returncode == 0 else "FAIL"


def _scan_ref(repo_root: Path, ref: str) -> tuple[tuple[topology.Finding, ...], int]:
    descriptor, index_name = tempfile.mkstemp(prefix="kfm-mrts04-index-")
    os.close(descriptor)
    os.unlink(index_name)
    env = os.environ.copy()
    env["GIT_INDEX_FILE"] = index_name
    prior = os.environ.get("GIT_INDEX_FILE")
    try:
        _git(repo_root, "read-tree", ref, env=env)
        os.environ["GIT_INDEX_FILE"] = index_name
        return topology.scan(repo_root)
    finally:
        if prior is None:
            os.environ.pop("GIT_INDEX_FILE", None)
        else:
            os.environ["GIT_INDEX_FILE"] = prior
        try:
            Path(index_name).unlink(missing_ok=True)
        except OSError:
            pass


def _validate_shape(instance: Mapping[str, Any], schema: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for error in sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda item: list(item.path)):
        field = "/" + "/".join(str(item) for item in error.path)
        findings.append(Finding("SCHEMA_INVALID", field))
    if findings:
        return findings

    refs = instance["governing_refs"]
    ref_paths = [item["path"] for item in refs]
    if ref_paths != sorted(set(ref_paths)) or tuple(ref_paths) != EXPECTED_GOVERNING_PATHS:
        findings.append(Finding("GOVERNING_REFS_NOT_CANONICAL", "/governing_refs"))

    lanes = instance["lanes"]
    lane_ids = [item["lane_id"] for item in lanes]
    if lane_ids != sorted(set(lane_ids)) or set(lane_ids) != set(LANE_SPECS):
        findings.append(Finding("LANE_SET_INVALID", "/lanes"))
    else:
        for index, lane in enumerate(lanes):
            expected = LANE_SPECS[lane["lane_id"]]
            if (lane["owner_path"], lane["expected_outcome"]) != expected[:2]:
                findings.append(Finding("LANE_BINDING_INVALID", f"/lanes/{index}"))

    coverage = instance["coverage"]
    criterion_ids = [item["criterion_id"] for item in coverage]
    if criterion_ids != sorted(set(criterion_ids)) or set(criterion_ids) != set(EXPECTED_COVERAGE):
        findings.append(Finding("COVERAGE_SET_INVALID", "/coverage"))
    else:
        for index, item in enumerate(coverage):
            expected = EXPECTED_COVERAGE[item["criterion_id"]]
            actual = (tuple(item["lane_ids"]), tuple(item["topology_rule_ids"]))
            if actual != expected:
                findings.append(Finding("COVERAGE_BINDING_INVALID", f"/coverage/{index}"))

    if tuple(instance["required_non_effects"]) != REQUIRED_NON_EFFECTS:
        findings.append(Finding("NON_EFFECTS_INVALID", "/required_non_effects"))
    return findings


def validate_current(
    *, repo_root: Path = REPO_ROOT, instance_path: Path = INSTANCE_PATH
) -> tuple[list[Finding], dict[str, Any]]:
    instance = _load_yaml(instance_path)
    schema = _load_schema(repo_root / SCHEMA_PATH.relative_to(REPO_ROOT))
    findings = _validate_shape(instance, schema)
    lane_results: dict[str, str] = {}
    topology_summary: dict[str, Any] = {
        "introduced_finding_count": None,
        "resolved_finding_count": None,
    }
    if findings:
        return sorted(set(findings)), _report(findings, lane_results, topology_summary)

    base_ref = _resolve_commit(repo_root, str(instance["base_ref"]))
    for index, item in enumerate(instance["governing_refs"]):
        try:
            blob = _read_pinned_blob(repo_root, base_ref, str(item["path"]))
        except ParityError:
            findings.append(Finding("GOVERNING_REF_UNRESOLVED", f"/governing_refs/{index}/path"))
            continue
        digest = "sha256:" + hashlib.sha256(blob).hexdigest()
        if digest != item["sha256"]:
            findings.append(Finding("GOVERNING_DIGEST_MISMATCH", f"/governing_refs/{index}/sha256"))

    for lane_id, (_owner, expected, command) in sorted(LANE_SPECS.items()):
        if lane_id == "repository-topology":
            continue
        if not (repo_root / _owner).is_file() or (repo_root / _owner).is_symlink():
            actual = "NOT_RUN"
        else:
            actual = _run_lane(command or (), repo_root)
        lane_results[lane_id] = actual
        if actual == "NOT_RUN":
            findings.append(Finding("LANE_NOT_RUN", f"/lanes/{lane_id}"))
        elif actual != expected:
            findings.append(Finding("LANE_OUTCOME_MISMATCH", f"/lanes/{lane_id}"))

    try:
        current_findings, tracked_count = topology.scan(repo_root)
        base_findings, base_tracked_count = _scan_ref(repo_root, base_ref)
        baseline_path = repo_root / topology.BASELINE_REPOSITORY_PATH
        baseline_data, baseline_entries = topology._load_baseline_bytes(
            baseline_path.read_bytes(), label="current"
        )
        topology.enforce_trusted_baseline(
            repo_root, baseline_data, baseline_entries, base_ref
        )
        _topology_code, topology_report = topology.evaluate(
            current_findings,
            tracked_count,
            baseline_entries,
            expires_on=str(baseline_data["expires_on"]),
        )
        current_fingerprints = {item.fingerprint for item in current_findings}
        base_fingerprints = {item.fingerprint for item in base_findings}
        introduced = sorted(current_fingerprints - base_fingerprints)
        resolved = sorted(base_fingerprints - current_fingerprints)
        counts = topology_report["counts"]
        stale_count = len(topology_report["baseline"]["stale_fingerprints"])
        topology_summary = {
            "base_tracked_path_count": base_tracked_count,
            "tracked_path_count": tracked_count,
            "introduced_finding_count": len(introduced),
            "resolved_finding_count": len(resolved),
            "fail_invariant": counts["fail_invariant"],
            "fail_new_drift": counts["fail_new_drift"],
            "baselined_warning": counts["baselined_warning"],
            "stale_fingerprints": stale_count,
            "rule_count": topology_report["rule_count"],
        }
        expected_topology = dict(instance["expected_topology"])
        actual_expected = {
            key: topology_summary[key]
            for key in (
                "rule_count",
                "fail_invariant",
                "fail_new_drift",
                "baselined_warning",
                "stale_fingerprints",
            )
        }
        if actual_expected != expected_topology:
            findings.append(Finding("TOPOLOGY_EXPECTATION_MISMATCH", "/expected_topology"))
        if introduced:
            findings.append(Finding("TOPOLOGY_INTRODUCED_DRIFT", "/topology"))
        if topology_report["outcome"] == "PASS":
            lane_results["repository-topology"] = "PASS"
        else:
            lane_results["repository-topology"] = "HOLD_INHERITED"
        if lane_results["repository-topology"] != LANE_SPECS["repository-topology"][1]:
            findings.append(Finding("TOPOLOGY_HOLD_MISCLASSIFIED", "/lanes/repository-topology"))
    except (OSError, ValueError, topology.TopologyError, ParityError):
        lane_results["repository-topology"] = "ERROR"
        findings.append(Finding("TOPOLOGY_NOT_EVALUATED", "/topology"))

    return sorted(set(findings)), _report(findings, lane_results, topology_summary)


def _report(
    findings: Sequence[Finding], lane_results: Mapping[str, str], topology_summary: Mapping[str, Any]
) -> dict[str, Any]:
    profile_outcome = "FAIL" if findings else "PASS"
    if findings:
        conformance = "FAIL"
    elif lane_results.get("repository-topology") == "HOLD_INHERITED":
        conformance = "HOLD_INHERITED"
    elif lane_results and all(value == "PASS" for value in lane_results.values()):
        conformance = "PASS"
    else:
        conformance = "NOT_RUN"
    return {
        "authority": {
            "authorizes_baseline_expansion": False,
            "authorizes_migration_or_deletion": False,
            "authorizes_release": False,
            "publishes": False,
        },
        "conformance_outcome": conformance,
        "findings": [item.as_dict() for item in sorted(set(findings))],
        "lane_results": dict(sorted(lane_results.items())),
        "profile_integrity_outcome": profile_outcome,
        "scope": "validator-parity-inherited-versus-introduced-classification-only",
        "topology": dict(topology_summary),
    }


def classify_fixture(case: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    states = case.get("lane_states")
    if not isinstance(states, dict) or set(states) != set(LANE_SPECS):
        return [Finding("COVERAGE_SET_INVALID", "/lane_states")]
    for lane_id, value in states.items():
        if value == "NOT_RUN":
            findings.append(Finding("LANE_NOT_RUN", f"/lane_states/{lane_id}"))
        elif value == "FAIL":
            findings.append(Finding("LANE_OUTCOME_MISMATCH", f"/lane_states/{lane_id}"))
    if case.get("coverage_complete") is not True:
        findings.append(Finding("COVERAGE_SET_INVALID", "/coverage_complete"))
    if case.get("baseline_growth") is True:
        findings.append(Finding("BASELINE_GROWTH", "/baseline_growth"))
    introduced = case.get("introduced_topology_findings")
    if not isinstance(introduced, int) or isinstance(introduced, bool) or introduced < 0:
        findings.append(Finding("SCHEMA_INVALID", "/introduced_topology_findings"))
    elif introduced:
        findings.append(Finding("TOPOLOGY_INTRODUCED_DRIFT", "/introduced_topology_findings"))
    failures = case.get("topology_current_failures")
    if not isinstance(failures, int) or isinstance(failures, bool) or failures < 0:
        findings.append(Finding("SCHEMA_INVALID", "/topology_current_failures"))
    elif failures and states.get("repository-topology") == "PASS":
        findings.append(Finding("TOPOLOGY_HOLD_MISCLASSIFIED", "/lane_states/repository-topology"))
    return sorted(set(findings))


def validate_fixtures(root: Path = FIXTURE_ROOT) -> tuple[bool, list[dict[str, Any]]]:
    manifest_path = root / "expected_findings_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    results: list[dict[str, Any]] = []
    ok = True
    for relative, expected_codes in sorted(manifest.items()):
        case = _load_yaml(root / relative)
        findings = classify_fixture(case)
        actual_codes = sorted({item.code for item in findings})
        expected = sorted(expected_codes)
        if actual_codes != expected:
            ok = False
        results.append(
            {
                "file": relative,
                "finding_codes": actual_codes,
                "outcome": "PASS" if not findings else "FAIL",
            }
        )
    return ok, results


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--instance", type=Path, default=INSTANCE_PATH)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.fixtures:
            ok, results = validate_fixtures()
            for result in results:
                print(json.dumps(result, sort_keys=True, separators=(",", ":")))
            return 0 if ok else 1
        findings, report = validate_current(
            repo_root=args.repo_root.resolve(), instance_path=args.instance.resolve()
        )
    except (OSError, UnicodeError, ValueError, ParityError) as exc:
        report = {
            "error": type(exc).__name__,
            "profile_integrity_outcome": "ERROR",
            "scope": "validator-parity-inherited-versus-introduced-classification-only",
        }
        findings = [Finding("VALIDATOR_ERROR", "/")]
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
