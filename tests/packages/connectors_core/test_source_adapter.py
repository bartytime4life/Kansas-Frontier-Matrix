"""Deterministic no-network tests for the SourceAdapter protocol boundary."""
from __future__ import annotations

from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta, timezone
import hashlib
import importlib
from pathlib import Path
import socket
import sys
from unittest.mock import patch

import pytest

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "packages/connectors-core/src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from connectors_core import source_adapter as adapter_module  # noqa: E402
from connectors_core.source_adapter import (  # noqa: E402
    AdapterBoundaryError,
    DiscoveryCursor,
    ParseFinding,
    ParseOutcome,
    ParseResult,
    SourceHealth,
    SourceHealthStatus,
    SourceLocator,
    assert_source_adapter_boundary,
)

DIGEST = "sha256:" + hashlib.sha256(b"fixture").hexdigest()
ARTIFACT_REF = f"source-artifact:{DIGEST}"
NOW = datetime(2026, 8, 9, 1, 20, tzinfo=timezone.utc)


def locator() -> SourceLocator:
    return SourceLocator(
        source_descriptor_ref="kfm://source/fixture",
        profile_id="fixture-v1",
        native_id="native-001",
        safe_locator="https://source.example.test/records",
        locator_kind="api_record",
        parameter_names=("format", "id"),
        expected_media_types=("application/geo+json", "application/json"),
    )


def parsed_result() -> ParseResult:
    return ParseResult(
        source_artifact_ref=ARTIFACT_REF,
        parser_id="kfm://parser/fixture",
        parser_version="1.0.0",
        parser_spec_digest=DIGEST,
        outcome=ParseOutcome.PARSED,
        records=({"id": "a", "values": [1, 2]},),
        findings=(),
        unsupported_flags=(),
    )


def test_cursor_and_locator_are_explicit_canonical_and_deterministic():
    cursor = DiscoveryCursor(
        profile_id="fixture-v1",
        observed_at=NOW,
        cursor="page-0002",
        limit=50,
    )
    first = locator()
    second = locator()

    assert cursor.observed_at == NOW
    assert cursor.limit == 50
    assert first.parameter_names == ("format", "id")
    assert first.expected_media_types == (
        "application/geo+json",
        "application/json",
    )
    assert first.locator_digest == second.locator_digest
    assert first.locator_digest.startswith("sha256:")


def test_cursor_and_locator_reject_secret_or_noncanonical_inputs():
    with pytest.raises(AdapterBoundaryError, match="secret-like"):
        DiscoveryCursor("fixture-v1", NOW, cursor="access_token=secret")
    with pytest.raises(AdapterBoundaryError, match="canonical"):
        SourceLocator(
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            native_id="native-001",
            safe_locator="https://source.example.test/records?id=001",
            locator_kind="api_record",
            parameter_names=("format", "id"),
            expected_media_types=("application/json",),
        )
    with pytest.raises(AdapterBoundaryError, match="sorted and unique"):
        SourceLocator(
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            native_id="native-001",
            safe_locator="https://source.example.test/records",
            locator_kind="api_record",
            parameter_names=("id", "format"),
            expected_media_types=("application/json",),
        )
    with pytest.raises(AdapterBoundaryError, match="expected_media_types"):
        SourceLocator(
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            native_id="native-001",
            safe_locator="https://source.example.test/records",
            locator_kind="https_url",
        )


def test_parse_result_is_deeply_immutable_and_authority_free():
    result = parsed_result()

    assert result.record_count == 1
    assert result.records_copy() == [{"id": "a", "values": [1, 2]}]
    with pytest.raises(TypeError):
        result.records[0]["id"] = "changed"  # type: ignore[index]
    with pytest.raises(TypeError):
        result.records[0]["values"][0] = 99  # type: ignore[index]
    with pytest.raises(FrozenInstanceError):
        result.public_use_allowed = True  # type: ignore[misc]
    assert not result.authority_created
    assert not result.evidence_created
    assert not result.lifecycle_write_allowed
    assert not result.receipt_created
    assert not result.release_authorized
    assert not result.publication_authorized
    assert not result.public_use_allowed
    assert not result.repository_mutation_allowed


def test_parse_outcome_invariants_fail_closed():
    base = dict(
        source_artifact_ref=ARTIFACT_REF,
        parser_id="kfm://parser/fixture",
        parser_version="1.0.0",
        parser_spec_digest=DIGEST,
    )
    with pytest.raises(AdapterBoundaryError, match="PARSED requires"):
        ParseResult(**base, outcome=ParseOutcome.PARSED)
    with pytest.raises(AdapterBoundaryError, match="requires at least one finding"):
        ParseResult(**base, outcome=ParseOutcome.MALFORMED)
    with pytest.raises(AdapterBoundaryError, match="unsupported_flags"):
        ParseResult(**base, outcome=ParseOutcome.UNSUPPORTED)
    with pytest.raises(AdapterBoundaryError, match="at least two records"):
        ParseResult(
            **base,
            outcome=ParseOutcome.CONFLICT,
            records=({"id": "a"},),
            findings=(ParseFinding("SOURCE_CONFLICT", "/records"),),
            source_conflict_ref="kfm://source-conflict/fixture",
        )
    conflict = ParseResult(
        **base,
        outcome=ParseOutcome.CONFLICT,
        records=({"id": "a"}, {"id": "b"}),
        findings=(ParseFinding("SOURCE_CONFLICT", "/records"),),
        source_conflict_ref="kfm://source-conflict/fixture",
    )
    assert conflict.record_count == 2
    with pytest.raises(AdapterBoundaryError, match="cannot create authority"):
        ParseResult(
            **base,
            outcome=ParseOutcome.PARSED,
            records=({"id": "a"},),
            public_use_allowed=True,
        )
    with pytest.raises(TypeError, match="keys must be strings"):
        ParseResult(
            **base,
            outcome=ParseOutcome.PARSED,
            records=({1: "not-json"},),
        )
    with pytest.raises(TypeError, match="finite"):
        ParseResult(
            **base,
            outcome=ParseOutcome.PARSED,
            records=({"value": float("nan")},),
        )


def test_source_health_preserves_false_clear_boundary_and_time_order():
    health = SourceHealth(
        adapter_id="fixture-adapter",
        source_descriptor_ref="kfm://source/fixture",
        profile_id="fixture-v1",
        observed_at=NOW,
        status=SourceHealthStatus.UNREACHABLE,
        reason_codes=("STATUS_CHECK_FAILED",),
        status_check_completed=False,
        last_success_at=NOW - timedelta(hours=1),
        last_artifact_ref=ARTIFACT_REF,
    )
    assert health.clear_signal_allowed is False
    assert health.status is SourceHealthStatus.UNREACHABLE

    with pytest.raises(AdapterBoundaryError, match="never authorize clearing"):
        SourceHealth(
            adapter_id="fixture-adapter",
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            observed_at=NOW,
            status=SourceHealthStatus.UNKNOWN,
            reason_codes=("STATUS_UNCONFIRMED",),
            status_check_completed=False,
            clear_signal_allowed=True,
        )
    with pytest.raises(AdapterBoundaryError, match="after observed_at"):
        SourceHealth(
            adapter_id="fixture-adapter",
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            observed_at=NOW,
            status=SourceHealthStatus.DEGRADED,
            reason_codes=("SOURCE_STALE",),
            status_check_completed=True,
            last_success_at=NOW + timedelta(seconds=1),
        )
    with pytest.raises(AdapterBoundaryError, match="HEALTHY requires"):
        SourceHealth(
            adapter_id="fixture-adapter",
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            observed_at=NOW,
            status=SourceHealthStatus.HEALTHY,
            reason_codes=("SOURCE_HEALTHY",),
            status_check_completed=False,
        )


class GoodAdapter:
    adapter_id = "fixture-adapter"

    def discover(self, cursor):
        return (locator(),)

    def fetch(self, source_locator):
        return object()

    def parse(self, artifact):
        return parsed_result()

    def source_health(self):
        return SourceHealth(
            adapter_id=self.adapter_id,
            source_descriptor_ref="kfm://source/fixture",
            profile_id="fixture-v1",
            observed_at=NOW,
            status=SourceHealthStatus.HEALTHY,
            reason_codes=("SOURCE_HEALTHY",),
            status_check_completed=True,
            last_success_at=NOW,
            last_artifact_ref=ARTIFACT_REF,
        )


class OverreachingAdapter(GoodAdapter):
    def publish(self):
        raise AssertionError("must never be called")


def test_protocol_check_is_structural_noninvoking_and_rejects_forbidden_capability():
    good = GoodAdapter()
    assert assert_source_adapter_boundary(good) is good
    with pytest.raises(AdapterBoundaryError, match="publish"):
        assert_source_adapter_boundary(OverreachingAdapter())
    with pytest.raises(AdapterBoundaryError, match="does not satisfy"):
        assert_source_adapter_boundary(object())


def test_import_is_side_effect_free_and_module_has_no_effect_clients(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    before = list(tmp_path.iterdir())
    boom = AssertionError("ambient network")
    with (
        patch.object(socket.socket, "connect", side_effect=boom),
        patch.object(socket.socket, "connect_ex", side_effect=boom),
        patch.object(socket, "create_connection", side_effect=boom),
        patch.object(socket, "getaddrinfo", side_effect=boom),
    ):
        assert importlib.reload(adapter_module) is adapter_module
    assert list(tmp_path.iterdir()) == before

    source = Path(adapter_module.__file__).read_text(encoding="utf-8")
    forbidden = (
        "import requests",
        "import httpx",
        "import aiohttp",
        "import urllib.request",
        "import socket",
        "import subprocess",
        "import os",
        "from pathlib import Path",
        "open(",
        "data/raw",
        "data/work",
        "data/quarantine",
        "data/processed",
        "data/catalog",
        "data/published",
    )
    assert all(token not in source for token in forbidden)
