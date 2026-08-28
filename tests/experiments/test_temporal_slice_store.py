from __future__ import annotations

import sqlite3
import unittest

from tools.experiments.temporal_slice_store import (
    SelectionOutcome,
    StoredTemporalSlice,
    TemporalSliceStore,
)


def record(
    digit: str,
    start: str,
    end: str,
    *,
    dataset: str = "kfm:dataset-version:test",
    grid: str = "h3:test",
    state: str = "BASELINE",
    delta: float | None = None,
    previous: str | None = None,
) -> StoredTemporalSlice:
    return StoredTemporalSlice(
        slice_id="kfm:temporal-slice:sha256:" + digit * 64,
        dataset_version_ref=dataset,
        grid_key=grid,
        temporal_start=start,
        temporal_end=end,
        change_state=state,
        delta_magnitude=delta,
        previous_slice_ref=previous,
        superseded_by_ref=None,
        evidence_bundle_ref=f"kfm:evidence-bundle:{digit}",
        run_receipt_ref=f"kfm:run-receipt:{digit}",
        artifact_digest="sha256:" + ("a" if digit != "a" else "b") * 64,
    )


class TemporalSliceStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = TemporalSliceStore()
        self.addCleanup(self.store.close)

    def test_expected_indexes_exist(self) -> None:
        self.assertEqual(
            self.store.index_names(),
            ("idx_temporal_slice_change", "idx_temporal_slice_lookup"),
        )

    def test_half_open_temporal_selection(self) -> None:
        item = record("1", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z")
        self.store.insert(item)
        inside = self.store.select_at(item.dataset_version_ref, item.grid_key, "2026-08-06T12:00:00Z")
        at_end = self.store.select_at(item.dataset_version_ref, item.grid_key, "2026-08-07T00:00:00Z")
        self.assertEqual(inside.outcome, SelectionOutcome.FOUND)
        self.assertEqual(inside.record, item)
        self.assertEqual(at_end.outcome, SelectionOutcome.NOT_FOUND)

    def test_overlapping_unsuperseded_slices_fail_closed(self) -> None:
        first = record("1", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z")
        second = record("2", "2026-08-06T12:00:00Z", "2026-08-07T00:00:00Z", state="CHANGED", delta=0.2, previous=first.slice_id)
        self.store.insert(first)
        self.store.insert(second)
        result = self.store.select_at(first.dataset_version_ref, first.grid_key, "2026-08-06T18:00:00Z")
        self.assertEqual(result.outcome, SelectionOutcome.AMBIGUOUS)
        self.assertEqual(result.candidates, (second.slice_id, first.slice_id))

    def test_explicit_supersession_resolves_overlap(self) -> None:
        first = record("1", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z")
        second = record("2", "2026-08-06T12:00:00Z", "2026-08-07T00:00:00Z", state="CHANGED", delta=0.2, previous=first.slice_id)
        self.store.insert(first)
        self.store.insert(second)
        self.store.supersede(first.slice_id, second.slice_id)
        result = self.store.select_at(first.dataset_version_ref, first.grid_key, "2026-08-06T18:00:00Z")
        self.assertEqual(result.outcome, SelectionOutcome.FOUND)
        self.assertEqual(result.record.slice_id if result.record else None, second.slice_id)

    def test_change_order_is_deterministic(self) -> None:
        low = record("1", "2026-08-06T01:00:00Z", "2026-08-06T02:00:00Z", state="CHANGED", delta=0.1)
        high_late = record("2", "2026-08-06T03:00:00Z", "2026-08-06T04:00:00Z", state="CHANGED", delta=0.5)
        high_early = record("3", "2026-08-06T02:00:00Z", "2026-08-06T03:00:00Z", state="CHANGED", delta=0.5)
        for item in (low, high_late, high_early):
            self.store.insert(item)
        result = self.store.changed_since(low.dataset_version_ref, low.grid_key, "2026-08-06T00:00:00Z")
        self.assertEqual(tuple(item.slice_id for item in result), (high_early.slice_id, high_late.slice_id, low.slice_id))

    def test_dataset_and_grid_partitions_do_not_leak(self) -> None:
        a = record("1", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z")
        b = record("2", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z", dataset="kfm:dataset-version:other")
        c = record("3", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z", grid="h3:other")
        for item in (a, b, c):
            self.store.insert(item)
        result = self.store.select_at(a.dataset_version_ref, a.grid_key, "2026-08-06T12:00:00Z")
        self.assertEqual(result.outcome, SelectionOutcome.FOUND)
        self.assertEqual(result.record.slice_id if result.record else None, a.slice_id)

    def test_invalid_records_fail_before_storage(self) -> None:
        with self.assertRaises(ValueError):
            self.store.insert(record("1", "2026-08-07T00:00:00Z", "2026-08-06T00:00:00Z"))
        with self.assertRaises(ValueError):
            self.store.insert(record("2", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z", state="CHANGED", delta=-1))
        count = self.store.connection.execute("SELECT COUNT(*) FROM temporal_slice_index").fetchone()[0]
        self.assertEqual(count, 0)

    def test_duplicate_slice_identity_is_rejected(self) -> None:
        item = record("1", "2026-08-06T00:00:00Z", "2026-08-07T00:00:00Z")
        self.store.insert(item)
        with self.assertRaises(sqlite3.IntegrityError):
            self.store.insert(item)


if __name__ == "__main__":
    unittest.main()
