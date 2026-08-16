#!/usr/bin/env python3
"""Validate the synthetic-only FrontierClassification fixture packet.

The validator composes already-governed fixture contracts. It never performs
network access, reads lifecycle stores, changes threshold policy, classifies a
real county, or creates review, release, publication, API, or map authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages" / "hashing" / "src"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)
from tools.validators.data.validate_county_year_panel import (  # noqa: E402
    canonical_identity as county_year_panel_identity,
    validate_payload as validate_county_year_panel,
)
from tools.validators.evidence.validate_access_observation import (  # noqa: E402
    canonical_identity as access_observation_identity,
    validate_payload as validate_access_observation,
)
from tools.validators.evidence.validate_frontier_definition import (  # noqa: E402
    canonical_identity as frontier_definition_identity,
    validate_payload as validate_frontier_definition,
)
from tools.validators.evidence.validate_population_observation import (  # noqa: E402
    canonical_identity as population_observation_identity,
    validate_payload as validate_population_observation,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/frontier_classification.schema.json"
CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/frontier_classification/cases.json"
IDENTITY_PREFIX = "kfm:frontier-classification:"
METHOD_REF = (
    "kfm://method/frontier-classification/synthetic-v1@sha256:"
    "1212121212121212121212121212121212121212121212121212121212121212"
)
SCOPE = "frontier-classification-fixture-only-v1"
MAX_FINDINGS = 100


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def coherent(self) -> bool:
        return self.outcome == "PASS" and not self.findings


@dataclass
class FixtureContext:
    candidate: dict[str, Any]
    registry: dict[str, Any]
    definition: dict[str, Any]
    panel: dict[str, Any]
    observations: dict[str, dict[str, Any]]
    expected_traces: list[dict[str, Any]]
    expected_classification: dict[str, Any]
    expected_posture: dict[str, Any]
    prior_assessment: dict[str, Any] | None = None
    force_registry_error: bool = False


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _list(value: object) -> list[Any]:
    return list(value) if isinstance(value, list) else []


def _pointer(parts: Sequence[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _day(value: object) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _identity_projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    metadata = subject.get("metadata")
    if isinstance(metadata, dict):
        metadata.pop("generated_at", None)
    return subject


def seal(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest = compute_spec_hash(_identity_projection(value))
    value["spec_hash"] = digest
    value["assessment_id"] = IDENTITY_PREFIX + digest.removeprefix("sha256:")
    return value


def _digest_ref(path: str, digest: str) -> str:
    return f"kfm://{path}@{digest}"


def _seal_frontier_definition(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest, identifier = frontier_definition_identity(value)
    value["spec_hash"] = digest
    value["definition_id"] = identifier
    return value


def _seal_county_year_panel(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest, identifier = county_year_panel_identity(value)
    value["spec_hash"] = digest
    value["panel_id"] = identifier
    return value


def _seal_access_observation(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest, identifier = access_observation_identity(value)
    value["spec_hash"] = digest
    value["observation_id"] = identifier
    return value


def _seal_population_observation(candidate: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(dict(candidate))
    digest, identifier = population_observation_identity(value)
    value["spec_hash"] = digest
    value["observation_id"] = identifier
    return value


def _set_pointer(candidate: Any, pointer: str, value: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
    ]
    if not parts or parts == [""]:
        raise ValueError("root replacement is not supported")
    parent = candidate
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    last = parts[-1]
    if isinstance(parent, list):
        index = int(last)
        if index == len(parent):
            parent.append(copy.deepcopy(value))
        else:
            parent[index] = copy.deepcopy(value)
    else:
        parent[last] = copy.deepcopy(value)
