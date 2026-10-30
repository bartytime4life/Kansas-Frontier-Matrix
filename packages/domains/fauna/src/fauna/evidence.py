"""Link occurrence references within an explicit, offline bundle inventory.

This checks declared metadata only. It does not authenticate sources, interpret
claim scope, verify artifact bytes, close evidence, or approve public release.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import islice
from types import MappingProxyType
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
from referencing import Registry, Resource
from referencing.exceptions import CannotDetermineSpecification, Unresolvable

from .validation import Finding, validate_candidate

MAX_BUNDLES = 128
MAX_BUNDLE_REFS = 256
MAX_SCHEMA_RESOURCES = 16


@dataclass(frozen=True)
class EvidenceBindingResult:
    outcome: str
    required_refs: int = 0
    linked_refs: int = 0
    findings: tuple[Finding, ...] = ()

    @property
    def public_ready(self) -> bool:
        return False

    @property
    def integrity_verified(self) -> bool:
        return False


@dataclass(frozen=True)
class _BundleSupport:
    bundle_id: str
    source_records: frozenset[str]
    checksum_refs: frozenset[str]


class EvidenceCatalog:
    """Immutable reference index; retains no source payloads or bundle text."""

    def __init__(self, index: Mapping[str, tuple[_BundleSupport, ...]]):
        self._index = MappingProxyType(dict(index))

    @classmethod
    def from_candidates(
        cls, candidates: object, *, schema: Mapping[str, Any],
        resources: Iterable[Mapping[str, Any]] = (),
    ) -> EvidenceCatalog:
        """Validate candidate bundles with only explicitly supplied schemas.

        Bundle IDs are literal local inventory keys. An optional bundle_ref in
        a constituent EvidenceRef must name its containing bundle_id exactly.
        No URI aliases, filesystem traversal, network lookup or precedence rules
        are inferred. The operational bounds do not change the shared schema.
        """
        if not isinstance(candidates, list) or len(candidates) > MAX_BUNDLES:
            raise ValueError("prov.evidence_inventory_invalid")
        try:
            supplied = list(islice(iter(resources), MAX_SCHEMA_RESOURCES + 1))
            if len(supplied) > MAX_SCHEMA_RESOURCES:
                raise ValueError("schema.evidence_bundle_unavailable")
            registry = Registry()
            resource_ids: set[str] = set()
            for document in [schema, *supplied]:
                Draft202012Validator.check_schema(document)
                identifier = document.get("$id")
                if (not isinstance(identifier, str) or not identifier
                        or identifier in resource_ids):
                    raise ValueError("schema.evidence_bundle_unavailable")
                resource_ids.add(identifier)
                registry = registry.with_resource(identifier, Resource.from_contents(dict(document)))
            validator = Draft202012Validator(
                schema, registry=registry, format_checker=FormatChecker(),
            )
            index: dict[str, list[_BundleSupport]] = {}
            bundle_ids: set[str] = set()
            for candidate in candidates:
                if next(validator.iter_errors(candidate), None) is not None:
                    raise ValueError("schema.evidence_bundle_invalid")
                bundle_id = candidate["bundle_id"]
                refs = candidate["evidence_refs"]
                if bundle_id in bundle_ids or len(refs) > MAX_BUNDLE_REFS:
                    raise ValueError("prov.evidence_inventory_invalid")
                bundle_ids.add(bundle_id)
                text_fields = [
                    candidate["claim_scope"], *candidate["source_records"],
                    *candidate["citations"],
                ]
                if any(not value.strip() for value in text_fields):
                    raise ValueError("prov.evidence_metadata_empty")
                support = _BundleSupport(
                    bundle_id, frozenset(candidate["source_records"]),
                    frozenset(candidate["checksums"]),
                )
                seen: set[str] = set()
                for entry in refs:
                    ref = entry["ref"]
                    if not ref.strip() or len(ref) > 1024 or ref in seen:
                        raise ValueError("prov.evidence_inventory_invalid")
                    if entry.get("bundle_ref", bundle_id) != bundle_id:
                        raise ValueError("prov.bundle_reference_mismatch")
                    seen.add(ref)
                    index.setdefault(ref, []).append(support)
        except (SchemaError, Unresolvable, CannotDetermineSpecification,
                TypeError, KeyError, AttributeError, RecursionError) as exc:
            raise ValueError("schema.evidence_bundle_unavailable") from exc
        return cls({ref: tuple(support) for ref, support in index.items()})

    def assess(
        self, occurrence: object, *, schema: Mapping[str, Any],
    ) -> EvidenceBindingResult:
        """Check exact reference and source/raw metadata links, without mutation.

        A linked result is still an internal, held metadata rehearsal. Declared
        checksums are not recomputed; scope, rights, sensitivity, review and
        admission are not independently authenticated by this helper.
        """
        if isinstance(occurrence, Mapping):
            validation = occurrence.get("validation")
            if (isinstance(validation, Mapping)
                    and validation.get("validator_result") in ("deny", "error")):
                return EvidenceBindingResult(
                    validation["validator_result"],
                    findings=(Finding("obs.upstream_disposition_preserved", "/validation/validator_result"),),
                )
        validation = validate_candidate(occurrence, schema=schema)
        if not validation.ok:
            return EvidenceBindingResult("error", findings=validation.findings)
        refs = occurrence["provenance"]["evidence_refs"]
        findings: list[Finding] = []
        supports: list[_BundleSupport] = []
        linked = 0
        for position, ref in enumerate(refs):
            matches = self._index.get(ref, ())
            if len(matches) != 1:
                code = "prov.evidence_ref_ambiguous" if matches else "prov.evidence_ref_unresolved"
                findings.append(Finding(code, f"/provenance/evidence_refs/{position}"))
            else:
                linked += 1
                supports.append(matches[0])
        if not findings:
            source_supports = [
                support for support in supports
                if occurrence["source_record_id"] in support.source_records
            ]
            if not source_supports:
                findings.append(Finding("prov.source_record_binding_missing", "/source_record_id"))
            raw = occurrence["provenance"]["raw_artifact_ref"]
            if (raw is not None and source_supports
                    and not any(raw in support.checksum_refs for support in source_supports)):
                findings.append(Finding("prov.raw_artifact_binding_missing", "/provenance/raw_artifact_ref"))
        return EvidenceBindingResult(
            "linked" if not findings else "abstain", len(refs), linked, tuple(findings),
        )
