"""Compare the reusable schema-registry package with the current local resolver.

This validator is deliberately read-only and no-network.  It proves identifier
and decoded-document parity over the current canonical schema tree.  It does not
approve schemas, contracts, policy, evidence, promotion, release, or
publication, and it does not migrate any consumer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages" / "schema-registry" / "src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from schema_registry import SchemaRegistryError, build_registry_snapshot
from tools.validators._common.local_resolver import build_registry as build_legacy_registry


class ParityOutcome(StrEnum):
    PASS = "PASS"
    ERROR = "ERROR"


@dataclass(frozen=True, order=True, slots=True)
class Finding:
    code: str
    schema_id: str | None
    detail: str

    def as_dict(self) -> dict[str, str]:
        result = {"code": self.code, "detail": self.detail}
        if self.schema_id is not None:
            result["schema_id"] = self.schema_id
        return result


@dataclass(frozen=True, slots=True)
class ParityReport:
    outcome: ParityOutcome
    legacy_id_count: int
    package_id_count: int
    skipped_missing_id_count: int
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome is ParityOutcome.PASS

    def as_dict(self) -> dict[str, object]:
        return {
            "outcome": self.outcome.value,
            "legacy_id_count": self.legacy_id_count,
            "package_id_count": self.package_id_count,
            "skipped_missing_id_count": self.skipped_missing_id_count,
            "findings": [finding.as_dict() for finding in self.findings],
            "authority": "validation_only",
        }


def _document_digest(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(encoded).hexdigest()}"


def validate_parity(repo_root: Path) -> ParityReport:
    root = Path(repo_root)
    schema_root = root / "schemas" / "contracts" / "v1"

    try:
        package_snapshot = build_registry_snapshot(schema_root)
        package_registry = package_snapshot.to_referencing_registry()
    except SchemaRegistryError as exc:
        return ParityReport(
            ParityOutcome.ERROR,
            0,
            0,
            0,
            (
                Finding(
                    f"PACKAGE_{exc.code.value}",
                    None,
                    "the package registry rejected the current schema tree",
                ),
            ),
        )
    except Exception:
        return ParityReport(
            ParityOutcome.ERROR,
            0,
            0,
            0,
            (
                Finding(
                    "PACKAGE_REGISTRY_ERROR",
                    None,
                    "the package registry could not be built",
                ),
            ),
        )

    try:
        legacy_registry = build_legacy_registry(root)
    except Exception:
        return ParityReport(
            ParityOutcome.ERROR,
            0,
            len(package_snapshot.records),
            len(package_snapshot.skipped),
            (
                Finding(
                    "LEGACY_REGISTRY_ERROR",
                    None,
                    "the existing validator-local registry could not be built",
                ),
            ),
        )

    legacy_ids = tuple(sorted(str(value) for value in legacy_registry.keys()))
    package_ids = package_snapshot.schema_ids
    findings: list[Finding] = []

    legacy_only = sorted(set(legacy_ids) - set(package_ids))
    package_only = sorted(set(package_ids) - set(legacy_ids))
    for schema_id in legacy_only:
        findings.append(
            Finding(
                "ID_ONLY_IN_LEGACY_REGISTRY",
                schema_id,
                "schema id is absent from the package snapshot",
            )
        )
    for schema_id in package_only:
        findings.append(
            Finding(
                "ID_ONLY_IN_PACKAGE_REGISTRY",
                schema_id,
                "schema id is absent from the existing validator-local registry",
            )
        )

    for schema_id in sorted(set(legacy_ids) & set(package_ids)):
        try:
            legacy_digest = _document_digest(legacy_registry.contents(schema_id))
            package_digest = _document_digest(package_registry.contents(schema_id))
        except Exception:
            findings.append(
                Finding(
                    "REGISTRY_CONTENT_UNREADABLE",
                    schema_id,
                    "one registry could not return decoded schema content",
                )
            )
            continue
        if legacy_digest != package_digest:
            findings.append(
                Finding(
                    "REGISTRY_CONTENT_MISMATCH",
                    schema_id,
                    "decoded schema content differs between registry implementations",
                )
            )

    ordered = tuple(sorted(findings))
    return ParityReport(
        ParityOutcome.PASS if not ordered else ParityOutcome.ERROR,
        len(legacy_ids),
        len(package_ids),
        len(package_snapshot.skipped),
        ordered,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate package parity with the current KFM local schema resolver."
    )
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--pretty", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    report = validate_parity(args.repo_root)
    if args.pretty:
        output = json.dumps(report.as_dict(), indent=2, sort_keys=True)
    else:
        output = json.dumps(report.as_dict(), sort_keys=True, separators=(",", ":"))
    print(output)
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
