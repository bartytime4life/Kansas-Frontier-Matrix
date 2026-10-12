"""Shared constants and finite validation result types for path aliases."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTER_PATH = REPO_ROOT / "control_plane/path_alias_register.yaml"
ROOT_REGISTRY_PATH = REPO_ROOT / "control_plane/root_registry.yaml"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/path_alias_register.schema.json"
DOCTRINE_PATH = REPO_ROOT / "docs/doctrine/directory-rules.md"
ADR_PATH = REPO_ROOT / "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/path_alias_register"

ADOPTED_DOCTRINE_SHA256 = "44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e"
ADOPTED_DECISION = "ADR-0029"
EXPECTED_ROOT_REGISTRY_SHA256 = "9dba2956624827673e3fcb7d903c567cbdc042aaf104d20728dc7b2d762f3641"
EXPECTED_ROOT_REGISTRY_BASE = "29bf0c8c6b112df0a77c141d54a3a39fc5e9dfaf"
REQUIRED_RULE_IDS = frozenset(
    {
        "DIR-COMPAT-001",
        "DIR-COMPAT-002",
        "DIR-COMPAT-003",
        "DIR-CONTROL-001",
        "DIR-CONTROL-002",
        "DIR-ENFORCE-001",
    }
)
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "path-alias-register-projection-only"

EXPOSURE_RANK = {
    "restricted": 0,
    "internal": 1,
    "semi_public": 2,
    "public": 3,
    "mixed": 3,
}
MUTATION_RANK = {
    "immutable": 0,
    "read_only": 0,
    "generated": 1,
    "append_only": 2,
    "versioned": 3,
    "mixed": 4,
}


class DuplicateKeyError(ValueError):
    """Raised for duplicate JSON object members."""


class NonFiniteNumberError(ValueError):
    """Raised for JSON NaN or infinity."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def outcome(self) -> str:
        codes = {finding.code for finding in self.findings}
        if not codes:
            return "PASS"
        if any(
            code.startswith(("INPUT_", "JSON_", "SCHEMA_UNAVAILABLE", "ROOT_REGISTRY_UNAVAILABLE", "REPO_ROOT_"))
            for code in codes
        ):
            return "ERROR_VALIDATOR"
        if any(code in {"DECISION_EVIDENCE_MISSING", "CONSUMER_EVIDENCE_MISSING"} for code in codes):
            return "HOLD_UNRESOLVED"
        if any(
            code in {
                "ALIAS_EXPIRED",
                "ALIAS_PATH_MISSING",
                "CANONICAL_TARGET_MISSING",
                "REGISTERED_ROOT_MISSING",
            }
            for code in codes
        ):
            return "FAIL_NEW_DRIFT"
        return "FAIL_INVARIANT"
