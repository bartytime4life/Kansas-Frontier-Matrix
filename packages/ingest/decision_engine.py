from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

ALLOWED_DECISIONS = {"INGEST", "SKIP", "QUARANTINE", "ABSTAIN", "ERROR"}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_canonical(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def _stable_for_hash(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _stable_for_hash(v) for k, v in value.items() if k not in {"created_at"}}
    if isinstance(value, list):
        return [_stable_for_hash(v) for v in value]
    return value


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass
class IngestDecisionEngine:
    """Deterministic, no-network ingest decision preflight gate."""

    def evaluate(self, payload: dict[str, Any], created_at: str | None = None) -> dict[str, Any]:
        created_at = created_at or _now_iso()
        source = payload.get("source_descriptor") or {}
        source_id = source.get("source_id")

        plan = self._build_conditional_request_plan(payload, source_id, created_at)
        probe = self._build_probe_receipt(payload, source_id, created_at, plan)
        materiality = self._build_materiality(payload, source_id, created_at)

        prev_hash = payload.get("last_known_spec_hash")
        current_hash = payload.get("spec_hash_current") or self._compute_spec_hash_current(payload)

        etag_prev = (payload.get("last_ingest_receipt") or {}).get("etag")
        etag_curr = payload.get("etag")
        lm_prev = (payload.get("last_ingest_receipt") or {}).get("last_modified")
        lm_curr = payload.get("last_modified")
        ver_prev = (payload.get("last_ingest_receipt") or {}).get("dataset_version")
        ver_curr = payload.get("dataset_version")

        change_detected = any(
            [
                bool(prev_hash and current_hash and prev_hash != current_hash),
                bool(etag_prev and etag_curr and etag_prev != etag_curr),
                bool(lm_prev and lm_curr and lm_prev != lm_curr),
                bool(ver_prev and ver_curr and ver_prev != ver_curr),
            ]
        )

        policy_decision, policy_reason = self._policy_check(payload)
        decision, reason = self._synthesize_decision(change_detected, materiality["materiality"], policy_decision)

        envelope = {
            "object_type": "IngestDecisionEnvelope",
            "schema_version": "v1",
            "source_id": source_id,
            "decision": decision,
            "change_detected": change_detected,
            "materiality": materiality["materiality"],
            "policy_decision": policy_decision,
            "spec_hash_previous": prev_hash,
            "spec_hash_current": current_hash,
            "etag_previous": etag_prev,
            "etag_current": etag_curr,
            "last_modified_previous": lm_prev,
            "last_modified_current": lm_curr,
            "decision_reason": policy_reason if policy_decision == "DENY" else reason,
            "created_at": created_at,
            "deterministic": True,
        }
        envelope["decision_id"] = sha256_canonical(_stable_for_hash(envelope))

        ingest_intent = self._build_ingest_intent(payload, envelope, created_at) if decision == "INGEST" else None
        skip_record = self._build_skip_record(envelope, created_at) if decision == "SKIP" else None

        validator_report = self._validate(envelope)
        if not validator_report["valid"]:
            envelope["decision"] = "ERROR"
            envelope["decision_reason"] = "validation_failed"

        audit_log = self._audit_log(payload, plan, probe, materiality, envelope, ingest_intent, skip_record, created_at)

        return {
            "IngestDecisionEnvelope.v1": envelope,
            "MaterialityAssessment.v1": materiality,
            "SourceProbeReceipt.v1": probe,
            "ConditionalRequestPlan.v1": plan,
            "IngestIntent.v1": ingest_intent,
            "SkipDecisionRecord.v1": skip_record,
            "DecisionAuditLog.v1": audit_log,
            "DecisionValidatorReport.v1": validator_report,
        }

    def _compute_spec_hash_current(self, payload: dict[str, Any]) -> str:
        probe_metadata = payload.get("probe_metadata") or {}
        return sha256_canonical(_stable_for_hash(probe_metadata))

    def _build_conditional_request_plan(self, payload: dict[str, Any], source_id: str, created_at: str) -> dict[str, Any]:
        etag = payload.get("etag")
        last_modified = payload.get("last_modified")
        if etag:
            strategy = "if_none_match"
            headers = {"If-None-Match": etag}
        elif last_modified:
            strategy = "if_modified_since"
            headers = {"If-Modified-Since": last_modified}
        else:
            strategy = "metadata_probe"
            headers = {}
        out = {
            "object_type": "ConditionalRequestPlan",
            "schema_version": "v1",
            "source_id": source_id,
            "strategy": strategy,
            "headers": headers,
            "created_at": created_at,
        }
        out["plan_id"] = sha256_canonical(_stable_for_hash(out))
        return out

    def _build_probe_receipt(self, payload: dict[str, Any], source_id: str, created_at: str, plan: dict[str, Any]) -> dict[str, Any]:
        out = {
            "object_type": "SourceProbeReceipt",
            "schema_version": "v1",
            "source_id": source_id,
            "etag": payload.get("etag"),
            "last_modified": payload.get("last_modified"),
            "content_length": payload.get("content_length"),
            "dataset_version": payload.get("dataset_version"),
            "probe_metadata": payload.get("probe_metadata") or {},
            "request_plan_ref": plan["plan_id"],
            "created_at": created_at,
        }
        out["probe_id"] = sha256_canonical(_stable_for_hash(out))
        return out

    def _build_materiality(self, payload: dict[str, Any], source_id: str, created_at: str) -> dict[str, Any]:
        ruleset = payload.get("materiality_ruleset") or {}
        stats = (payload.get("probe_metadata") or {}).get("summary_stats") or {}
        delta = float(stats.get("delta", 0))
        threshold = float(ruleset.get("threshold", 0))
        if not ruleset:
            mat = "UNKNOWN"
            reason = "missing_materiality_ruleset"
        elif ruleset.get("force_unknown"):
            mat = "UNKNOWN"
            reason = "ruleset_unknown"
        elif delta > threshold:
            mat = "MATERIAL"
            reason = "delta_above_threshold"
        else:
            mat = "IMMATERIAL"
            reason = "delta_below_or_equal_threshold"
        out = {
            "object_type": "MaterialityAssessment",
            "schema_version": "v1",
            "source_id": source_id,
            "materiality": mat,
            "reason": reason,
            "threshold": threshold,
            "observed_delta": delta,
            "created_at": created_at,
        }
        out["assessment_id"] = sha256_canonical(_stable_for_hash(out))
        return out

    def _policy_check(self, payload: dict[str, Any]) -> tuple[str, str]:
        profile = payload.get("domain_policy_profile")
        if not profile:
            return "DENY", "missing_policy_profile"
        if profile.get("rights_status") in {None, "unknown"}:
            return "DENY", "unknown_rights"
        if profile.get("restricted_geometry"):
            return "DENY", "restricted_geometry"
        if profile.get("decision") == "DENY":
            return "DENY", "policy_block"
        return "ALLOW", "policy_allow"

    def _synthesize_decision(self, changed: bool, materiality: str, policy_decision: str) -> tuple[str, str]:
        if policy_decision == "DENY":
            return "SKIP", "policy_block"
        if not changed:
            return "SKIP", "no_change"
        if materiality == "IMMATERIAL":
            return "SKIP", "immaterial_change"
        if materiality == "UNKNOWN":
            return "ABSTAIN", "unknown_materiality"
        if materiality == "MATERIAL":
            return "INGEST", "material_change"
        return "ERROR", "invalid_materiality"

    def _build_ingest_intent(self, payload: dict[str, Any], envelope: dict[str, Any], created_at: str) -> dict[str, Any]:
        out = {
            "object_type": "IngestIntent",
            "schema_version": "v1",
            "decision_ref": envelope["decision_id"],
            "source_id": envelope["source_id"],
            "ingest_mode": payload.get("ingest_mode", "snapshot"),
            "expected_format": payload.get("expected_format", "json"),
            "mapping_strategy": payload.get("mapping_strategy", "default"),
            "target_lane": "RAW",
            "requires_quarantine": bool(payload.get("domain_policy_profile", {}).get("requires_quarantine", False)),
            "created_at": created_at,
        }
        out["intent_id"] = sha256_canonical(_stable_for_hash(out))
        return out

    def _build_skip_record(self, envelope: dict[str, Any], created_at: str) -> dict[str, Any]:
        reason = envelope["decision_reason"]
        out = {
            "object_type": "SkipDecisionRecord",
            "schema_version": "v1",
            "decision_ref": envelope["decision_id"],
            "reason": reason if reason in {"no_change", "immaterial_change", "policy_block"} else "policy_block",
            "created_at": created_at,
        }
        out["skip_id"] = sha256_canonical(_stable_for_hash(out))
        return out

    def _validate(self, envelope: dict[str, Any]) -> dict[str, Any]:
        errors = []
        if not envelope.get("source_id"):
            errors.append("missing_source_id")
        if not envelope.get("policy_decision"):
            errors.append("missing_policy_decision")
        if envelope.get("decision") not in ALLOWED_DECISIONS:
            errors.append("decision_enum_invalid")
        if not envelope.get("spec_hash_current"):
            errors.append("missing_spec_hash_current")
        if envelope.get("change_detected") is False and envelope.get("materiality") == "MATERIAL":
            errors.append("conflicting_signals")
        return {
            "object_type": "DecisionValidatorReport",
            "schema_version": "v1",
            "valid": len(errors) == 0,
            "errors": errors,
        }

    def _audit_log(self, payload: dict[str, Any], plan: dict[str, Any], probe: dict[str, Any], materiality: dict[str, Any], envelope: dict[str, Any], ingest_intent: dict[str, Any] | None, skip_record: dict[str, Any] | None, created_at: str) -> dict[str, Any]:
        out = {
            "object_type": "DecisionAuditLog",
            "schema_version": "v1",
            "decision_ref": envelope["decision_id"],
            "source_id": envelope.get("source_id"),
            "inputs": {
                "source_descriptor": payload.get("source_descriptor"),
                "temporal_window": payload.get("temporal_window"),
            },
            "artifacts": {
                "conditional_request_plan_ref": plan["plan_id"],
                "source_probe_receipt_ref": probe["probe_id"],
                "materiality_assessment_ref": materiality["assessment_id"],
                "ingest_intent_ref": (ingest_intent or {}).get("intent_id"),
                "skip_record_ref": (skip_record or {}).get("skip_id"),
            },
            "created_at": created_at,
        }
        out["audit_id"] = sha256_canonical(_stable_for_hash(out))
        return out
