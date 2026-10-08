#!/usr/bin/env python3
"""Run the synthetic, no-network Hydrology proof slice.

The slice replays a closed, digest-pinned fixture set through a fixed sequence
of fail-closed gates and emits one deterministic proof record. Every case
produces a finite DecisionEnvelope (ANSWER, ABSTAIN, DENY, or ERROR) that is
validated against the Hydrology decision_envelope schema and compared with the
outcome the execution profile expects. The run is executed twice and the two
records must be byte-identical.

Posture: SYNTHETIC_FIXTURE_ONLY. The inputs are the Living Waters fixture
packet and synthetic request cases; no real source is read or admitted. The
gates are bounded in-harness rules, not a bound Rego evaluator, so the record
emits no PolicyDecision. The rollback rehearsal is a dry-run pointer swap. The
harness writes nothing to lifecycle storage and grants no release or
publication authority.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for _import_root in (REPO_ROOT, HASHING_SRC):
    if str(_import_root) not in sys.path:
        sys.path.insert(0, str(_import_root))

from hashing import JsonInputError, compute_spec_hash, load_json_file  # noqa: E402
from tools.validators._common.local_resolver import build_registry  # noqa: E402

DEFAULT_PROFILE = "control_plane/readiness/hydrology-proof-slice-profile.json"
SCHEMA_DIR = REPO_ROOT / "schemas/contracts/v1/domains/hydrology"
PACKET_VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/domains/hydrology/validate_living_waters_fixture_packet.py"
)
RECORD_SCHEMA_VERSION = "kfm.hydrology-proof-slice-record/v1"
ENVELOPE_VERSION = "hydrology-proof-slice-v1"
GENERALIZED_PRECISIONS = frozenset({"generalized_huc12"})
PERMITTED_PRESENTATIONS = frozenset(
    {
        ("synthetic_observation", "observed_gauge_series"),
        ("regulatory_context", "regulatory_context_overlay"),
    }
)
DENIED_LIFECYCLE_SEGMENTS = frozenset({"raw", "work", "quarantine", "processed"})
BASE_OBLIGATIONS = ("CITE_SYNTHETIC_FIXTURE", "LABEL_NOT_A_REAL_OBSERVATION")
EFFECTS = {
    "network_accessed": False,
    "source_admitted": False,
    "policy_decision_emitted": False,
    "lifecycle_written": False,
    "released": False,
    "published": False,
}


class ProofSliceError(ValueError):
    """The profile or a pinned input cannot be trusted; the run cannot proceed."""


@dataclass(frozen=True)
class Decision:
    outcome: str
    policy_family: str
    reason_code: str
    reasons: tuple[str, ...]
    obligations: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()


def _load_module(name: str, path: Path) -> Any:
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ProofSliceError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    # dataclasses resolve their defining module through sys.modules.
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        del sys.modules[name]
        raise
    return module


def _schema_validator(name: str, *, registry: Any) -> Draft202012Validator:
    schema = json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))
    return Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())


def _first_error(validator: Draft202012Validator, instance: Any) -> str | None:
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    if not errors:
        return None
    pointer = "/" + "/".join(str(part) for part in errors[0].absolute_path)
    return f"{pointer}: {errors[0].message}"


def _resolve(relative: str) -> Path:
    candidate = PurePosixPath(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ProofSliceError(f"input path must be repository-relative: {relative}")
    path = REPO_ROOT / candidate
    if path.is_symlink() or not path.is_file():
        raise ProofSliceError(f"input is not a regular file: {relative}")
    return path


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


class PinnedInputs:
    """Load only files the profile pins, and only when their bytes match."""

    def __init__(self) -> None:
        self._pins: dict[str, str] = {}
        self.loaded: dict[str, Any] = {}

    def pin(self, entry: Mapping[str, str]) -> None:
        path, digest = entry["path"], entry["sha256"]
        if self._pins.get(path, digest) != digest:
            raise ProofSliceError(f"conflicting pins for {path}")
        self._pins[path] = digest

    def is_pinned(self, relative: str) -> bool:
        return relative in self._pins

    def load(self, relative: str) -> Any:
        if relative in self.loaded:
            return self.loaded[relative]
        if relative not in self._pins:
            raise ProofSliceError(f"input is not pinned by the profile: {relative}")
        path = _resolve(relative)
        actual = _sha256(path)
        if actual != self._pins[relative]:
            raise ProofSliceError(
                f"pinned digest mismatch for {relative}: expected {self._pins[relative]}, got {actual}"
            )
        try:
            value = load_json_file(path)
        except JsonInputError as exc:
            raise ProofSliceError(f"unsafe JSON input {relative}: {exc}") from exc
        self.loaded[relative] = value
        return value

    def verify_all(self) -> None:
        """Load every pinned input, so a PASS covers the whole manifest."""

        for relative in sorted(self._pins):
            self.load(relative)

    def manifest(self) -> list[dict[str, str]]:
        return [{"path": path, "sha256": self._pins[path]} for path in sorted(self._pins)]


def _requested_path_is_public(requested: str, prefix: str) -> bool:
    candidate = PurePosixPath(requested)
    if candidate.is_absolute() or ".." in candidate.parts:
        return False
    if not requested.startswith(prefix):
        return False
    return not (DENIED_LIFECYCLE_SEGMENTS & set(candidate.parts[1:]))


def _evidence_closure(
    bundle: Any, *, packet_digest: str, bundle_validator: Draft202012Validator
) -> str | None:
    """Return a reason the bundle does not close over the packet, or None."""

    problem = _first_error(bundle_validator, bundle)
    if problem is not None:
        return f"EvidenceBundle is schema-invalid at {problem}"
    unhashed = {key: value for key, value in bundle.items() if key != "spec_hash"}
    if compute_spec_hash(unhashed) != bundle["spec_hash"]["value"]:
        return "EvidenceBundle spec_hash does not match its content"
    if bundle["checksums"].get("living_waters_packet") != packet_digest:
        return "EvidenceBundle does not bind the pinned Living Waters packet digest"
    return None


def decide(
    request: Mapping[str, Any],
    *,
    profile: Mapping[str, Any],
    inputs: PinnedInputs,
    packet: Mapping[str, Any],
    packet_digest: str,
    bundle_validator: Draft202012Validator,
) -> Decision:
    """Apply the fail-closed gates in order; the first gate that fails decides."""

    if request["surface"] != "governed_api":
        return Decision(
            "DENY", "capability", "UI_DIRECT_MODEL_CALL_DENIED",
            ("Only the governed API may answer; a direct browser-to-model call bypasses the trust membrane.",),
        )
    if not _requested_path_is_public(request["requested_artifact"], profile["public_artifact_prefix"]):
        return Decision(
            "DENY", "access", "PUBLIC_RAW_PATH_DENIED",
            ("A public surface may read only released artifacts, never RAW, WORK, QUARANTINE, or PROCESSED paths.",),
        )
    if request["policy_evaluator"] != "available":
        return Decision(
            "ERROR", "access", "POLICY_EVALUATOR_UNAVAILABLE",
            ("Policy could not be evaluated, so no answer is given.",),
        )

    bundle_path = request["evidence_bundle"]
    if bundle_path is None:
        return Decision(
            "ABSTAIN", "access", "MISSING_EVIDENCE_BUNDLE",
            ("No EvidenceBundle supports the claim; KFM cites or abstains.",),
        )
    if not inputs.is_pinned(bundle_path):
        return Decision(
            "ERROR", "access", "EVIDENCE_INPUT_NOT_PINNED",
            ("The requested EvidenceBundle is not part of the pinned profile.",),
        )
    bundle = inputs.load(bundle_path)
    closure_problem = _evidence_closure(
        bundle, packet_digest=packet_digest, bundle_validator=bundle_validator
    )
    if closure_problem is not None:
        return Decision("ABSTAIN", "access", "EVIDENCE_CLOSURE_FAILED", (closure_problem,))
    evidence_refs = tuple(
        [bundle["bundle_id"]] + sorted(item["ref"] for item in bundle["evidence_refs"])
    )

    if bundle["rights"]["license"] not in profile["license_allowlist"]:
        return Decision(
            "DENY", "access", "RIGHTS_UNKNOWN",
            ("The EvidenceBundle license is not on the profile allowlist.",),
            evidence_refs=evidence_refs,
        )
    if request["geometry_precision"] not in GENERALIZED_PRECISIONS:
        return Decision(
            "DENY", "sensitivity", "SENSITIVE_EXACT_GEOMETRY",
            ("Exact site geometry may not reach a public surface; only generalized HUC12 support is allowed.",),
            evidence_refs=evidence_refs,
        )
    if (request["feature_source_role"], request["presented_as"]) not in PERMITTED_PRESENTATIONS:
        return Decision(
            "DENY", "render", "SOURCE_ROLE_COLLAPSE",
            (
                f"A {request['feature_source_role']} feature may not be presented as {request['presented_as']}; "
                "regulatory flood-hazard context is never an observed flood event.",
            ),
            evidence_refs=evidence_refs,
        )

    scenarios = {item["id"]: item for item in packet["scenarios"]}
    scenario = scenarios.get(request["scenario_id"])
    if scenario is None:
        return Decision(
            "ERROR", "access", "SCENARIO_UNKNOWN",
            ("The requested scenario is not declared by the pinned packet.",),
            evidence_refs=evidence_refs,
        )
    packet_reason = scenario["reason_codes"][0]
    obligations = list(BASE_OBLIGATIONS)
    if scenario["state"] == "NO_RESULTS":
        return Decision("ABSTAIN", "access", packet_reason, (scenario["display_message"],), evidence_refs=evidence_refs)
    if scenario["state"] == "UNAVAILABLE":
        return Decision("ERROR", "access", packet_reason, (scenario["display_message"],), evidence_refs=evidence_refs)
    if scenario["state"] == "ABSTAIN" or scenario["join_outcome"] != "EXACT":
        return Decision("ABSTAIN", "access", packet_reason, (scenario["display_message"],), evidence_refs=evidence_refs)
    if scenario["state"] == "STALE":
        obligations.append("DISPLAY_STALE_BADGE")
    elif scenario["state"] != "AVAILABLE":
        return Decision(
            "ERROR", "access", "SCENARIO_STATE_UNSUPPORTED",
            ("The packet scenario state has no finite mapping.",),
            evidence_refs=evidence_refs,
        )

    if not request["rollback_target"]:
        return Decision(
            "DENY", "promotion", "RELEASE_ROLLBACK_MISSING",
            ("A release candidate without a rollback target cannot reach a public surface.",),
            evidence_refs=evidence_refs,
        )

    latest = packet["series"]["points"][-1]
    series = packet["series"]
    return Decision(
        "ANSWER", "access", packet_reason if scenario["state"] == "STALE" else "FIXTURE_EVIDENCE_RESOLVED",
        (
            f"{scenario['display_message']} Latest synthetic {series['parameter_name']} "
            f"{latest['value']} {series['unit_code']} at {latest['observed_at']} "
            f"({series['qualifier_name']}).",
        ),
        obligations=tuple(obligations),
        evidence_refs=evidence_refs,
    )


def _envelope(case_id: str, decision: Decision, evaluated_at: str) -> dict[str, Any]:
    return {
        "decision_id": f"hydrology:proof-slice:{case_id}",
        "outcome": decision.outcome,
        "policy_family": decision.policy_family,
        "reason_code": decision.reason_code,
        "reasons": list(decision.reasons),
        "obligations": list(decision.obligations),
        "evidence_refs": list(decision.evidence_refs),
        "evaluated_at": evaluated_at,
        "version": ENVELOPE_VERSION,
    }


def _rollback_rehearsal(base: Mapping[str, Any]) -> dict[str, Any]:
    """Publish and roll back one dry-run pointer; the pointer must return exactly."""

    candidate = base["release_candidate"]
    target = base["rollback_target"]
    pointer = target
    before = pointer
    pointer = candidate
    after_publish = pointer
    pointer = target
    return {
        "dry_run": True,
        "release_candidate": candidate,
        "rollback_target": target,
        "pointer_before": before,
        "pointer_after_publish": after_publish,
        "pointer_after_rollback": pointer,
        "outcome": "PASS" if pointer == before and after_publish == candidate != target else "FAIL",
    }


def build_record(profile_relative: str = DEFAULT_PROFILE) -> dict[str, Any]:
    """Run the slice once from the profile and return the proof record."""

    registry = build_registry(REPO_ROOT)
    profile_path = _resolve(profile_relative)
    try:
        profile = load_json_file(profile_path)
    except JsonInputError as exc:
        raise ProofSliceError(f"unsafe profile JSON: {exc}") from exc
    problem = _first_error(_schema_validator("proof_slice_profile.schema.json", registry=registry), profile)
    if problem is not None:
        raise ProofSliceError(f"profile is schema-invalid at {problem}")

    inputs = PinnedInputs()
    for entry in (profile["packet"], profile["base_request"], *profile["evidence_bundles"], *profile["cases"]):
        inputs.pin(entry)
    inputs.verify_all()

    packet_path = profile["packet"]["path"]
    packet = inputs.load(packet_path)
    packet_validator = _load_module("kfm_living_waters_packet_validator", PACKET_VALIDATOR_PATH)
    packet_findings = [
        f"{finding.code}:{finding.field}"
        for finding in packet_validator.validate_file(_resolve(packet_path))
    ]
    packet_validation = {"outcome": "FAIL" if packet_findings else "PASS", "findings": packet_findings}

    base = inputs.load(profile["base_request"]["path"])
    problem = _first_error(_schema_validator("proof_slice_request.schema.json", registry=registry), base)
    if problem is not None:
        raise ProofSliceError(f"base request is schema-invalid at {problem}")

    case_validator = _schema_validator("proof_slice_case.schema.json", registry=registry)
    envelope_validator = _schema_validator("decision_envelope.schema.json", registry=registry)
    bundle_validator = _schema_validator("evidence_bundle.schema.json", registry=registry)
    seen: set[str] = set()
    case_results: list[dict[str, Any]] = []
    for entry in profile["cases"]:
        case = inputs.load(entry["path"])
        problem = _first_error(case_validator, case)
        if problem is not None:
            raise ProofSliceError(f"{entry['path']} is schema-invalid at {problem}")
        if case["case_id"] in seen:
            raise ProofSliceError(f"duplicate case_id {case['case_id']}")
        seen.add(case["case_id"])

        request = copy.deepcopy(base)
        request.update(case["overrides"])
        if packet_findings:
            decision = Decision(
                "ERROR", "access", "PACKET_INVALID",
                ("The pinned Living Waters packet failed validation.",),
            )
        else:
            decision = decide(
                request,
                profile=profile,
                inputs=inputs,
                packet=packet,
                packet_digest=profile["packet"]["sha256"],
                bundle_validator=bundle_validator,
            )
        envelope = _envelope(case["case_id"], decision, profile["evaluated_at"])
        envelope_problem = _first_error(envelope_validator, envelope)
        if envelope_problem is not None:
            raise ProofSliceError(f"{case['case_id']}: emitted envelope is invalid at {envelope_problem}")
        case_results.append(
            {
                "case_id": case["case_id"],
                "thin_slice_assertion": case["thin_slice_assertion"],
                "expected_outcome": entry["expected_outcome"],
                "expected_reason_code": entry["expected_reason_code"],
                "matched": (decision.outcome, decision.reason_code)
                == (entry["expected_outcome"], entry["expected_reason_code"]),
                "envelope": envelope,
            }
        )

    rehearsal = _rollback_rehearsal(base)
    passed = (
        packet_validation["outcome"] == "PASS"
        and all(item["matched"] for item in case_results)
        and rehearsal["outcome"] == "PASS"
    )
    record: dict[str, Any] = {
        "schema_version": RECORD_SCHEMA_VERSION,
        "profile_id": profile["profile_id"],
        "profile_sha256": _sha256(profile_path),
        "posture": profile["posture"],
        "outcome": "PASS" if passed else "FAIL",
        "inputs": inputs.manifest(),
        "packet_validation": packet_validation,
        "cases": case_results,
        "rollback_rehearsal": rehearsal,
        "effects": dict(EFFECTS),
    }
    record["spec_hash"] = {"value": compute_spec_hash(record)}
    problem = _first_error(_schema_validator("proof_slice_record.schema.json", registry=registry), record)
    if problem is not None:
        raise ProofSliceError(f"emitted record is schema-invalid at {problem}")
    return record


def render(record: Mapping[str, Any]) -> str:
    return json.dumps(record, indent=2, sort_keys=True) + "\n"


SITE_CARRIER_PATH = "apps/site/source/app/living-waters-proof.json"
SITE_SCENARIO_CASES = {
    "current": "01-answer-current",
    "stale": "11-answer-stale",
    "no-results": "12-abstain-no-results",
    "unavailable": "13-error-artifact-unavailable",
    "ambiguous-reach": "09-abstain-ambiguous-reach",
}


def build_site_carrier() -> dict[str, Any]:
    """Project only the pinned synthetic packet and its five proved decisions.

    This is application fixture input, never a released artifact. The Site
    supplies schematic display geometry because the packet has no geometry;
    that drawing must not be presented as the named HUC12 or a gauge location.
    """
    record = build_record()
    if record["outcome"] != "PASS" or any(record["effects"].values()):
        raise ProofSliceError("Site carrier requires a passing, zero-effect synthetic proof")
    profile = load_json_file(_resolve(DEFAULT_PROFILE))
    inputs = PinnedInputs()
    for entry in (profile["packet"], profile["base_request"], *profile["evidence_bundles"], *profile["cases"]):
        inputs.pin(entry)
    if record["profile_sha256"] != _sha256(_resolve(DEFAULT_PROFILE)) or record["inputs"] != inputs.manifest():
        raise ProofSliceError("profile changed after proof evaluation; Site projection withheld")
    inputs.verify_all()
    packet = inputs.load(profile["packet"]["path"])
    base = inputs.load(profile["base_request"]["path"])
    bundle = inputs.load(base["evidence_bundle"])
    cases = {item["case_id"]: item for item in record["cases"]}
    return {
        "schema_version": "kfm.site-living-waters-synthetic/v1",
        "posture": record["posture"],
        "proof_record_hash": record["spec_hash"]["value"],
        "profile_sha256": record["profile_sha256"],
        "packet_sha256": profile["packet"]["sha256"],
        "packet": packet,
        "evidence_bundle": bundle,
        "feature_source_role": base["feature_source_role"],
        "presented_as": base["presented_as"],
        "scenarios": [
            {"id": scenario_id, "envelope": cases[case_id]["envelope"]}
            for scenario_id, case_id in SITE_SCENARIO_CASES.items()
        ],
        "rollback_rehearsal": record["rollback_rehearsal"],
        "effects": record["effects"],
    }


def run(profile_relative: str = DEFAULT_PROFILE) -> tuple[int, str]:
    """Run twice, require identical bytes, and return (exit code, output)."""

    try:
        first = render(build_record(profile_relative))
        second = render(build_record(profile_relative))
    except (ProofSliceError, OSError) as exc:
        return 2, json.dumps({"outcome": "ERROR", "reason": str(exc)}, sort_keys=True) + "\n"
    if first != second:
        return 1, json.dumps({"outcome": "FAIL", "reason": "REPLAY_NOT_DETERMINISTIC"}, sort_keys=True) + "\n"
    return (0 if json.loads(first)["outcome"] == "PASS" else 1), first


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0], allow_abbrev=False)
    parser.add_argument("--profile", default=DEFAULT_PROFILE, help="repository-relative profile path")
    site = parser.add_mutually_exclusive_group()
    site.add_argument("--site-carrier", action="store_true", help="print the pinned synthetic Site projection")
    site.add_argument("--check-site-carrier", action="store_true", help="check the committed Site projection without writing")
    parser.add_argument(
        "--output",
        type=Path,
        help="write the record here instead of stdout; must be outside the repository's data/ lifecycle root",
    )
    args = parser.parse_args(argv)
    if args.site_carrier or args.check_site_carrier:
        if args.profile != DEFAULT_PROFILE or args.output is not None:
            parser.error("Site projection uses the canonical profile and stdout only")
        try:
            output = render(build_site_carrier())
            if output != render(build_site_carrier()):
                raise ProofSliceError("Site projection is not deterministic")
            if args.check_site_carrier:
                if _resolve(SITE_CARRIER_PATH).read_text(encoding="utf-8") != output:
                    raise ProofSliceError("committed Site projection is stale; regenerate and review together")
                print(json.dumps({"outcome": "PASS", "posture": "SYNTHETIC_FIXTURE_ONLY"}))
            else:
                sys.stdout.write(output)
            return 0
        except (ProofSliceError, OSError) as exc:
            print(json.dumps({"outcome": "ERROR", "reason": str(exc)}), file=sys.stderr)
            return 2
    if args.output is not None:
        resolved = args.output.resolve()
        if resolved.is_relative_to((REPO_ROOT / "data").resolve()):
            print("refusing to write a proof record into lifecycle storage under data/", file=sys.stderr)
            return 2
    code, output = run(args.profile)
    if args.output is not None and code != 2:
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
