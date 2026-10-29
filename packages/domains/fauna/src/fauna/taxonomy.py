"""Deterministic matching within one caller-supplied taxonomy snapshot.

No fuzzy matching, live lookup, authority ranking, or source activation occurs.
A resolved name is a match in this snapshot, not independent taxonomic truth.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
import unicodedata
from typing import Any, Mapping

from .validation import Finding


def name_key(value: str) -> str:
    """Normalize typography only; retain authorship and rank qualifiers."""
    return " ".join(unicodedata.normalize("NFC", value).split()).casefold()


@dataclass(frozen=True)
class TaxonConcept:
    concept_id: str
    accepted_scientific_name: str
    taxon_rank: str
    synonyms: tuple[str, ...]
    evidence_refs: tuple[str, ...]


@dataclass(frozen=True)
class TaxonomyResolution:
    outcome: str
    queried_name: str
    authority: str
    snapshot_ref: str
    concept: TaxonConcept | None
    findings: tuple[Finding, ...] = ()


@dataclass(frozen=True)
class TaxonomyCatalog:
    authority: str
    snapshot_ref: str
    concepts: tuple[TaxonConcept, ...]
    _index: Mapping[str, tuple[TaxonConcept, ...]] = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        index: dict[str, list[TaxonConcept]] = {}
        for concept in self.concepts:
            for key in {name_key(concept.accepted_scientific_name),
                        *(name_key(synonym) for synonym in concept.synonyms)}:
                index.setdefault(key, []).append(concept)
        object.__setattr__(self, "_index", MappingProxyType({
            key: tuple(values) for key, values in index.items()
        }))

    @classmethod
    def from_candidate(
        cls, candidate: object, *, schema: Mapping[str, Any]
    ) -> TaxonomyCatalog:
        """Read a closed draft snapshot with the caller's canonical schema.

        Raises a bounded code, never the source payload or a schema error message.
        """
        from jsonschema import Draft202012Validator, FormatChecker
        from jsonschema.exceptions import SchemaError
        from referencing import Registry
        from referencing.exceptions import Unresolvable

        try:
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(
                schema, format_checker=FormatChecker(), registry=Registry()
            )
            valid = validator.is_valid(candidate)
        except (SchemaError, Unresolvable, ValueError, TypeError, RecursionError):
            raise ValueError("taxon.schema_unavailable") from None
        if not valid or not isinstance(candidate, Mapping):
            raise ValueError("taxon.snapshot_invalid")
        concepts = tuple(
            TaxonConcept(
                item["concept_id"], item["accepted_scientific_name"],
                item["taxon_rank"], tuple(item["synonyms"]),
                tuple(item["evidence_refs"]),
            )
            for item in candidate["concepts"]
        )
        if len({item.concept_id for item in concepts}) != len(concepts):
            raise ValueError("taxon.duplicate_concept")
        return cls(candidate["authority"], candidate["snapshot_ref"], concepts)

    def resolve(self, name: object) -> TaxonomyResolution:
        if not isinstance(name, str) or not name_key(name) or len(name) > 256:
            return TaxonomyResolution(
                "unresolved", "", self.authority, self.snapshot_ref, None,
                (Finding("taxon.name_invalid", "/taxon/scientific_name"),),
            )
        key = name_key(name)
        matches = self._index.get(key, ())
        if len(matches) == 1:
            return TaxonomyResolution(
                "resolved", name, self.authority, self.snapshot_ref, matches[0]
            )
        code = "taxon.name_ambiguous" if matches else "taxon.name_unresolved"
        return TaxonomyResolution(
            "ambiguous" if matches else "unresolved", name,
            self.authority, self.snapshot_ref, None,
            (Finding(code, "/taxon/scientific_name"),),
        )
