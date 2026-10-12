"""Projection and registry-wide semantic checks for path aliases."""

from __future__ import annotations

from typing import Any, Mapping

from .path_alias_entry_rules import entry_findings
from .path_alias_io import array, parse_date, sha256
from .path_alias_model import (
    ADOPTED_DECISION,
    ADOPTED_DOCTRINE_SHA256,
    EXPECTED_ROOT_REGISTRY_BASE,
    EXPECTED_ROOT_REGISTRY_SHA256,
    ROOT_REGISTRY_PATH,
    Finding,
)


def semantic_findings(
    candidate: Mapping[str, Any],
    root_registry: Mapping[str, Any],
    *,
    enforce_projection_binding: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    expected_doctrine_digest = f"sha256:{ADOPTED_DOCTRINE_SHA256}"
    expected_root_digest = f"sha256:{EXPECTED_ROOT_REGISTRY_SHA256}"

    doctrine = candidate.get("doctrine")
    if isinstance(doctrine, Mapping):
        if doctrine.get("sha256") != expected_doctrine_digest:
            findings.append(Finding("DOCTRINE_DIGEST_MISMATCH", "/doctrine/sha256"))
        if doctrine.get("decision_ref") != ADOPTED_DECISION:
            findings.append(Finding("DECISION_EVIDENCE_MISSING", "/doctrine/decision_ref"))

    projection = candidate.get("root_registry")
    if isinstance(projection, Mapping):
        if projection.get("sha256") != expected_root_digest:
            findings.append(Finding("ROOT_REGISTRY_DIGEST_MISMATCH", "/root_registry/sha256"))
        if projection.get("base_ref") != EXPECTED_ROOT_REGISTRY_BASE or projection.get("base_ref") != root_registry.get("base_ref"):
            findings.append(Finding("ROOT_REGISTRY_BASE_MISMATCH", "/root_registry/base_ref"))
        if enforce_projection_binding:
            try:
                actual = sha256(ROOT_REGISTRY_PATH)
            except OSError:
                findings.append(Finding("ROOT_REGISTRY_UNAVAILABLE", "/root_registry/path"))
            else:
                if projection.get("sha256") != f"sha256:{actual}":
                    findings.append(Finding("ROOT_REGISTRY_DIGEST_MISMATCH", "/root_registry/sha256"))

    roots = {
        entry.get("path"): entry
        for entry in array(root_registry.get("roots"))
        if isinstance(entry, Mapping) and isinstance(entry.get("path"), str) and isinstance(entry.get("root_id"), str)
    }
    aliases = array(candidate.get("aliases"))
    old_paths = [entry.get("old_path") for entry in aliases if isinstance(entry, Mapping)]
    alias_ids = [entry.get("alias_id") for entry in aliases if isinstance(entry, Mapping)]
    if old_paths != sorted(old_paths):
        findings.append(Finding("ALIASES_NOT_CANONICAL", "/aliases"))
    if len(old_paths) != len(set(old_paths)):
        findings.append(Finding("OLD_PATH_DUPLICATE", "/aliases"))
    if len(alias_ids) != len(set(alias_ids)):
        findings.append(Finding("ALIAS_ID_DUPLICATE", "/aliases"))

    updated_at = parse_date(candidate.get("updated_at"))
    seen_identity_aliases: set[str] = set()
    for index, raw in enumerate(aliases):
        if isinstance(raw, Mapping):
            findings.extend(
                entry_findings(
                    raw,
                    index,
                    roots=roots,
                    old_paths=old_paths,
                    updated_at=updated_at,
                    expected_doctrine_digest=expected_doctrine_digest,
                    expected_decision=ADOPTED_DECISION,
                    seen_identity_aliases=seen_identity_aliases,
                )
            )
    return findings
