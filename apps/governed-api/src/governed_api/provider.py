from dataclasses import dataclass
from enum import Enum
from typing import Protocol


LAYER_ID = "layer:synthetic-streamflow"
SOURCE_ID = "source:synthetic-streamflow"
FEATURE_ID = "feature:flow-001"
SELECTION_ID = "selection:flow-001"
EVIDENCE_REF = "kfm:evidence:synthetic:flow-001"
MAP_FEATURE_SELECTION_PROFILE = "kfm.explorer.map-feature-selection.v1"

RESTRICTED_LAYER_ID = "layer:synthetic-restricted"
RESTRICTED_FEATURE_ID = "feature:restricted"
RESTRICTED_EVIDENCE_REF = "kfm:evidence:synthetic:restricted"


@dataclass(frozen=True)
class PublicFeature:
    feature_id: str
    selection_id: str
    title: str
    coordinates: tuple[float, float]
    evidence_refs: tuple[str, ...]


@dataclass(frozen=True)
class PublicLayer:
    source_id: str
    layer_id: str
    kind: str
    title: str
    description: str
    features: tuple[PublicFeature, ...]


class EvidenceResolution(str, Enum):
    ANSWER = "ANSWER"
    ABSTAIN = "ABSTAIN"
    DENY = "DENY"
    ERROR = "ERROR"


class SliceProvider(Protocol):
    """App-local provider boundary for the deterministic public-safe slice."""

    def list_layers(self) -> tuple[PublicLayer, ...]:
        ...

    def resolve_evidence(
        self,
        *,
        layer_id: str,
        feature_id: str,
        evidence_ref: str,
    ) -> EvidenceResolution:
        ...


_PUBLIC_LAYERS = (
    PublicLayer(
        source_id=SOURCE_ID,
        layer_id=LAYER_ID,
        kind="circle",
        title="Synthetic streamflow demonstration",
        description=(
            "One generalized, fixture-only Kansas streamflow feature for the "
            "bounded governed map slice."
        ),
        features=(
            PublicFeature(
                feature_id=FEATURE_ID,
                selection_id=SELECTION_ID,
                title="Synthetic streamflow observation",
                coordinates=(-98.5, 38.5),
                evidence_refs=(EVIDENCE_REF,),
            ),
        ),
    ),
)


class DeterministicSliceProvider:
    """Return static in-process records without file, network, or model access."""

    def list_layers(self) -> tuple[PublicLayer, ...]:
        return _PUBLIC_LAYERS

    def resolve_evidence(
        self,
        *,
        layer_id: str,
        feature_id: str,
        evidence_ref: str,
    ) -> EvidenceResolution:
        requested = (layer_id, feature_id, evidence_ref)
        if requested == (LAYER_ID, FEATURE_ID, EVIDENCE_REF):
            return EvidenceResolution.ANSWER
        if requested == (
            RESTRICTED_LAYER_ID,
            RESTRICTED_FEATURE_ID,
            RESTRICTED_EVIDENCE_REF,
        ):
            return EvidenceResolution.DENY

        known_identifiers = {
            LAYER_ID,
            FEATURE_ID,
            EVIDENCE_REF,
            RESTRICTED_LAYER_ID,
            RESTRICTED_FEATURE_ID,
            RESTRICTED_EVIDENCE_REF,
        }
        requested_identifiers = {layer_id, feature_id, evidence_ref}
        if known_identifiers.intersection(requested_identifiers):
            if layer_id == LAYER_ID and feature_id == FEATURE_ID:
                return EvidenceResolution.ABSTAIN
            return EvidenceResolution.ERROR

        return EvidenceResolution.ABSTAIN


DEFAULT_PROVIDER: SliceProvider = DeterministicSliceProvider()
