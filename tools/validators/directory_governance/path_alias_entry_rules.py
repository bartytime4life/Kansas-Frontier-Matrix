"""Entry-level invariants for compatibility path and identity aliases."""

from __future__ import annotations

from datetime import date
from typing import Any, Mapping

from .path_alias_io import array, parse_date, root_for_path
from .path_alias_model import EXPOSURE_RANK, MUTATION_RANK, Finding, REQUIRED_RULE_IDS


def entry_findings(
    raw: Mapping[str, Any],
    index: int,
    *,
    roots: Mapping[str, Mapping[str, Any]],
    old_paths: list[Any],
    updated_at: date | None,
    expected_doctrine_digest: str,
    expected_decision: str,
    seen_identity_aliases: set[str],
) -> list[Finding]:
    findings: list[Finding] = []
    base = f"/aliases/{index}"
    old_path = raw.get("old_path")
    target = raw.get("canonical_target")
    if old_path == target:
        findings.append(Finding("ALIAS_SELF_TARGET", f"{base}/canonical_target"))
    if isinstance(target, str) and target in old_paths:
        findings.append(Finding("ALIAS_CHAIN_FORBIDDEN", f"{base}/canonical_target"))

    rule_ids = array(raw.get("rule_ids"))
    if rule_ids != sorted(set(rule_ids)):
        findings.append(Finding("RULE_IDS_NOT_CANONICAL", f"{base}/rule_ids"))
    if not REQUIRED_RULE_IDS.issubset(set(rule_ids)):
        findings.append(Finding("REQUIRED_RULE_IDS_MISSING", f"{base}/rule_ids"))
    if raw.get("source_digest") != expected_doctrine_digest:
        findings.append(Finding("ENTRY_SOURCE_DIGEST_MISMATCH", f"{base}/source_digest"))
    if raw.get("decision_ref") != expected_decision:
        findings.append(Finding("DECISION_EVIDENCE_MISSING", f"{base}/decision_ref"))

    identity = raw.get("identity_mapping")
    if isinstance(identity, Mapping):
        canonical_id = identity.get("canonical_id")
        ids = array(identity.get("aliases"))
        if canonical_id in ids:
            findings.append(Finding("CANONICAL_ID_REPEATED_AS_ALIAS", f"{base}/identity_mapping/aliases"))
        for item in ids:
            if not isinstance(item, str):
                continue
            if item in seen_identity_aliases:
                findings.append(Finding("IDENTITY_ALIAS_DUPLICATE", f"{base}/identity_mapping/aliases"))
            seen_identity_aliases.add(item)

    alias_root = root_for_path(str(old_path), roots) if isinstance(old_path, str) else None
    target_root = root_for_path(str(target), roots) if isinstance(target, str) else None
    if alias_root is None:
        findings.append(Finding("REGISTERED_ROOT_MISSING", f"{base}/old_path"))
    elif raw.get("alias_root") != alias_root.get("root_id"):
        findings.append(Finding("ALIAS_ROOT_MISMATCH", f"{base}/alias_root"))
    if target_root is None:
        findings.append(Finding("REGISTERED_ROOT_MISSING", f"{base}/canonical_target"))
    else:
        if raw.get("target_root") != target_root.get("root_id"):
            findings.append(Finding("TARGET_ROOT_MISMATCH", f"{base}/target_root"))
        if target_root.get("class") not in {"canonical", "platform"} or target_root.get("status") != "ACTIVE":
            findings.append(Finding("CANONICAL_TARGET_ROOT_INVALID", f"{base}/canonical_target"))
        family = raw.get("object_family")
        allowed = set(array(target_root.get("allowed_artifact_kinds")))
        prohibited = set(array(target_root.get("prohibited_artifact_kinds")))
        if family not in allowed or family in prohibited:
            findings.append(Finding("TARGET_OBJECT_FAMILY_INVALID", f"{base}/object_family"))

    writers = raw.get("writers")
    if isinstance(writers, Mapping):
        if array(writers.get("alias")):
            findings.append(Finding("ALIAS_WRITER_FORBIDDEN", f"{base}/writers/alias"))
        if not array(writers.get("canonical")):
            findings.append(Finding("CANONICAL_WRITER_REQUIRED", f"{base}/writers/canonical"))
    if raw.get("write_rule") != "canonical_only":
        findings.append(Finding("SINGLE_WRITE_REQUIRED", f"{base}/write_rule"))
    if not array(raw.get("consumers")):
        findings.append(Finding("CONSUMER_EVIDENCE_MISSING", f"{base}/consumers"))

    exposure = raw.get("exposure")
    if isinstance(exposure, Mapping):
        if EXPOSURE_RANK.get(str(exposure.get("alias")), 99) > EXPOSURE_RANK.get(str(exposure.get("target")), -1):
            findings.append(Finding("ALIAS_EXPOSURE_TOO_PERMISSIVE", f"{base}/exposure"))
    mutation = raw.get("mutation")
    if isinstance(mutation, Mapping):
        if MUTATION_RANK.get(str(mutation.get("alias")), 99) > MUTATION_RANK.get(str(mutation.get("target")), -1):
            findings.append(Finding("ALIAS_MUTATION_TOO_PERMISSIVE", f"{base}/mutation"))

    expiry = raw.get("expiry")
    if isinstance(expiry, Mapping) and expiry.get("mode") == "date" and updated_at is not None:
        expiry_date = parse_date(expiry.get("value"))
        if expiry_date is not None and expiry_date < updated_at:
            findings.append(Finding("ALIAS_EXPIRED", f"{base}/expiry/value"))
    exit_criteria = array(raw.get("exit_criteria"))
    if exit_criteria != sorted(set(exit_criteria)):
        findings.append(Finding("EXIT_CRITERIA_NOT_CANONICAL", f"{base}/exit_criteria"))

    findings.extend(class_findings(raw, base))
    return findings


def class_findings(raw: Mapping[str, Any], base: str) -> list[Finding]:
    findings: list[Finding] = []
    cls = raw.get("class")
    body_mode = raw.get("body_mode")
    read_rule = raw.get("read_rule")
    sync = raw.get("synchronization")
    sync_method = sync.get("method") if isinstance(sync, Mapping) else None
    if body_mode == "tombstone" and sync_method != "none_frozen":
        findings.append(Finding("TOMBSTONE_SYNC_FORBIDDEN", f"{base}/synchronization/method"))
    elif cls == "legacy":
        if body_mode not in {"legacy_body_read_only", "tombstone"} or sync_method != "none_frozen" or read_rule not in {"dual_read", "canonical_only_with_redirect"}:
            findings.append(Finding("LEGACY_CLASS_SEMANTICS_INVALID", base))
    elif cls == "mirror":
        if body_mode != "generated_mirror" or sync_method != "generated_one_way" or read_rule != "generated_read":
            findings.append(Finding("MIRROR_CLASS_SEMANTICS_INVALID", base))
    elif cls == "external_export":
        if body_mode != "external_export" or sync_method not in {"manual_export", "generated_one_way"} or read_rule != "generated_read":
            findings.append(Finding("EXTERNAL_EXPORT_SEMANTICS_INVALID", base))
    elif cls == "transitional":
        if body_mode != "transitional_copy" or sync_method != "copy_then_cutover" or read_rule != "dual_read":
            findings.append(Finding("TRANSITIONAL_CLASS_SEMANTICS_INVALID", base))
    elif cls == "deprecated":
        if body_mode not in {"deprecated_redirect", "tombstone"} or sync_method != "none_frozen" or read_rule not in {"dual_read", "canonical_only_with_redirect"}:
            findings.append(Finding("DEPRECATED_CLASS_SEMANTICS_INVALID", base))
    return findings
