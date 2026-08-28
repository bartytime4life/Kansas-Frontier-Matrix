#!/usr/bin/env python3
"""Deterministic, no-network TemporalSlice SQL storage experiment.

The experiment uses the Python standard-library SQLite engine as a portable
executor for a conservative SQL subset that is also accepted by DuckDB. It
proves index shape, half-open temporal lookup, explicit supersession, stable
change ordering, and fail-closed ambiguity handling for synthetic records only.

It does not create a production database, resolve references, evaluate policy,
authorize promotion or release, or publish any artifact.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from enum import StrEnum
from typing import Iterable, Sequence

SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
SLICE_ID = re.compile(r"^kfm:temporal-slice:sha256:[0-9a-f]{64}$")
CHANGE_STATES = frozenset({"BASELINE", "UNCHANGED", "CHANGED", "UNKNOWN", "ERROR"})

DDL = """
CREATE TABLE IF NOT EXISTS temporal_slice_index (
    slice_id TEXT PRIMARY KEY,
    dataset_version_ref TEXT NOT NULL,
    grid_key TEXT NOT NULL,
    temporal_start TEXT NOT NULL,
    temporal_end TEXT NOT NULL,
    change_state TEXT NOT NULL,
    delta_magnitude REAL,
    previous_slice_ref TEXT,
    superseded_by_ref TEXT,
    evidence_bundle_ref TEXT NOT NULL,
    run_receipt_ref TEXT NOT NULL,
    artifact_digest TEXT NOT NULL,
    CHECK (temporal_start < temporal_end),
    CHECK (delta_magnitude IS NULL OR delta_magnitude >= 0),
    CHECK (previous_slice_ref IS NULL OR previous_slice_ref <> slice_id),
    CHECK (superseded_by_ref IS NULL OR superseded_by_ref <> slice_id)
);
CREATE INDEX IF NOT EXISTS idx_temporal_slice_lookup
ON temporal_slice_index (
    dataset_version_ref,
    grid_key,
    temporal_start,
    temporal_end,
    slice_id
);
CREATE INDEX IF NOT EXISTS idx_temporal_slice_change
ON temporal_slice_index (
    dataset_version_ref,
    grid_key,
    temporal_start,
    delta_magnitude,
    slice_id
);
"""


class SelectionOutcome(StrEnum):
    FOUND = "FOUND"
    NOT_FOUND = "NOT_FOUND"
    AMBIGUOUS = "AMBIGUOUS"


@dataclass(frozen=True)
class StoredTemporalSlice:
    slice_id: str
    dataset_version_ref: str
    grid_key: str
    temporal_start: str
    temporal_end: str
    change_state: str
    delta_magnitude: float | None
    previous_slice_ref: str | None
    superseded_by_ref: str | None
    evidence_bundle_ref: str
    run_receipt_ref: str
    artifact_digest: str


@dataclass(frozen=True)
class SelectionResult:
    outcome: SelectionOutcome
    record: StoredTemporalSlice | None
    candidates: tuple[str, ...]


def _canonical_utc(value: str) -> str:
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a UTC offset")
    normalized = parsed.astimezone(timezone.utc)
    return normalized.isoformat(timespec="seconds").replace("+00:00", "Z")


def _validate_ref(value: str, field: str) -> None:
    if not isinstance(value, str) or not value or value != value.strip() or any(ch.isspace() for ch in value):
        raise ValueError(f"{field} must be a canonical nonblank reference")


def _validate_record(record: StoredTemporalSlice) -> StoredTemporalSlice:
    if not SLICE_ID.fullmatch(record.slice_id):
        raise ValueError("slice_id must use the TemporalSlice SHA-256 identity form")
    for field in (
        "dataset_version_ref",
        "grid_key",
        "evidence_bundle_ref",
        "run_receipt_ref",
    ):
        _validate_ref(getattr(record, field), field)
    if record.change_state not in CHANGE_STATES:
        raise ValueError("change_state is not governed")
    if record.delta_magnitude is not None and record.delta_magnitude < 0:
        raise ValueError("delta_magnitude cannot be negative")
    if not SHA256.fullmatch(record.artifact_digest) or set(record.artifact_digest[7:]) == {"0"}:
        raise ValueError("artifact_digest must be a non-placeholder SHA-256")
    start = _canonical_utc(record.temporal_start)
    end = _canonical_utc(record.temporal_end)
    if start >= end:
        raise ValueError("temporal window must be non-empty")
    if record.previous_slice_ref == record.slice_id or record.superseded_by_ref == record.slice_id:
        raise ValueError("slice lineage cannot self-reference")
    return StoredTemporalSlice(
        **{
            **asdict(record),
            "temporal_start": start,
            "temporal_end": end,
        }
    )


class TemporalSliceStore:
    """Small deterministic index experiment; not a production repository."""

    def __init__(self, connection: sqlite3.Connection | None = None) -> None:
        self.connection = connection or sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.connection.executescript(DDL)

    def close(self) -> None:
        self.connection.close()

    def insert(self, record: StoredTemporalSlice) -> None:
        normalized = _validate_record(record)
        values = asdict(normalized)
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO temporal_slice_index (
                    slice_id, dataset_version_ref, grid_key,
                    temporal_start, temporal_end, change_state,
                    delta_magnitude, previous_slice_ref, superseded_by_ref,
                    evidence_bundle_ref, run_receipt_ref, artifact_digest
                ) VALUES (
                    :slice_id, :dataset_version_ref, :grid_key,
                    :temporal_start, :temporal_end, :change_state,
                    :delta_magnitude, :previous_slice_ref, :superseded_by_ref,
                    :evidence_bundle_ref, :run_receipt_ref, :artifact_digest
                )
                """,
                values,
            )

    def supersede(self, predecessor_id: str, successor_id: str) -> None:
        if predecessor_id == successor_id:
            raise ValueError("a slice cannot supersede itself")
        rows = self.connection.execute(
            "SELECT * FROM temporal_slice_index WHERE slice_id IN (?, ?)",
            (predecessor_id, successor_id),
        ).fetchall()
        by_id = {row["slice_id"]: row for row in rows}
        if set(by_id) != {predecessor_id, successor_id}:
            raise KeyError("both predecessor and successor must exist")
        predecessor = by_id[predecessor_id]
        successor = by_id[successor_id]
        if (
            predecessor["dataset_version_ref"] != successor["dataset_version_ref"]
            or predecessor["grid_key"] != successor["grid_key"]
        ):
            raise ValueError("supersession must stay within one dataset/grid partition")
        if successor["temporal_start"] < predecessor["temporal_start"]:
            raise ValueError("successor cannot begin before predecessor")
        if successor["previous_slice_ref"] not in (None, predecessor_id):
            raise ValueError("successor previous_slice_ref conflicts with predecessor")
        if predecessor["superseded_by_ref"] not in (None, successor_id):
            raise ValueError("predecessor is already superseded by another slice")
        with self.connection:
            self.connection.execute(
                "UPDATE temporal_slice_index SET superseded_by_ref = ? WHERE slice_id = ?",
                (successor_id, predecessor_id),
            )
            self.connection.execute(
                "UPDATE temporal_slice_index SET previous_slice_ref = ? WHERE slice_id = ?",
                (predecessor_id, successor_id),
            )

    def select_at(self, dataset_version_ref: str, grid_key: str, at_time: str) -> SelectionResult:
        at = _canonical_utc(at_time)
        rows = self.connection.execute(
            """
            SELECT * FROM temporal_slice_index
            WHERE dataset_version_ref = ?
              AND grid_key = ?
              AND superseded_by_ref IS NULL
              AND temporal_start <= ?
              AND ? < temporal_end
            ORDER BY temporal_start DESC, temporal_end DESC, slice_id ASC
            """,
            (dataset_version_ref, grid_key, at, at),
        ).fetchall()
        if not rows:
            return SelectionResult(SelectionOutcome.NOT_FOUND, None, ())
        if len(rows) > 1:
            return SelectionResult(
                SelectionOutcome.AMBIGUOUS,
                None,
                tuple(row["slice_id"] for row in rows),
            )
        return SelectionResult(
            SelectionOutcome.FOUND,
            StoredTemporalSlice(**dict(rows[0])),
            (rows[0]["slice_id"],),
        )

    def changed_since(
        self,
        dataset_version_ref: str,
        grid_key: str,
        since: str,
    ) -> tuple[StoredTemporalSlice, ...]:
        instant = _canonical_utc(since)
        rows = self.connection.execute(
            """
            SELECT * FROM temporal_slice_index
            WHERE dataset_version_ref = ?
              AND grid_key = ?
              AND temporal_start >= ?
              AND change_state = 'CHANGED'
              AND superseded_by_ref IS NULL
            ORDER BY delta_magnitude DESC, temporal_start ASC, slice_id ASC
            """,
            (dataset_version_ref, grid_key, instant),
        ).fetchall()
        return tuple(StoredTemporalSlice(**dict(row)) for row in rows)

    def index_names(self) -> tuple[str, ...]:
        rows = self.connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'index' AND name NOT LIKE 'sqlite_autoindex_%' ORDER BY name"
        ).fetchall()
        return tuple(row["name"] for row in rows)


def _fixture_record(
    suffix: str,
    start: str,
    end: str,
    *,
    state: str = "BASELINE",
    delta: float | None = None,
    previous: str | None = None,
) -> StoredTemporalSlice:
    digest = suffix.rjust(64, "0")[-64:]
    return StoredTemporalSlice(
        slice_id=f"kfm:temporal-slice:sha256:{digest}",
        dataset_version_ref="kfm:dataset-version:synthetic:2026-08-06",
        grid_key="h3:8726e26d6ffffff",
        temporal_start=start,
        temporal_end=end,
        change_state=state,
        delta_magnitude=delta,
        previous_slice_ref=previous,
        superseded_by_ref=None,
        evidence_bundle_ref=f"kfm:evidence-bundle:synthetic:{suffix}",
        run_receipt_ref=f"kfm:run-receipt:synthetic:{suffix}",
        artifact_digest=f"sha256:{('a' + suffix).ljust(64, 'b')[:64]}",
    )


def self_test() -> dict[str, object]:
    store = TemporalSliceStore()
    try:
        baseline = _fixture_record("1", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z")
        changed = _fixture_record(
            "2",
            "2026-08-06T12:00:00Z",
            "2026-08-07T00:00:00Z",
            state="CHANGED",
            delta=0.12,
            previous=baseline.slice_id,
        )
        store.insert(baseline)
        store.insert(changed)
        ambiguous = store.select_at(
            baseline.dataset_version_ref,
            baseline.grid_key,
            "2026-08-06T18:00:00Z",
        )
        store.supersede(baseline.slice_id, changed.slice_id)
        selected = store.select_at(
            baseline.dataset_version_ref,
            baseline.grid_key,
            "2026-08-06T18:00:00Z",
        )
        return {
            "ambiguous_before_supersession": ambiguous.outcome,
            "index_names": store.index_names(),
            "selected_after_supersession": selected.record.slice_id if selected.record else None,
            "status": "PASS",
        }
    finally:
        store.close()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if not args.self_test:
        parser.error("use --self-test; this experiment does not open production databases")
    print(json.dumps(self_test(), sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
