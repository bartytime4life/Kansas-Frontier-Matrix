"""Synthetic negative cases for the offline checker; these are not historical evidence."""
import datetime as dt
import csv
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location("county_qualification", Path(__file__).resolve().parents[1] / "scripts/qualify-county-history.py")
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def version(start=18610129, end=18611231, identity="synthetic_county", number=1):
    return {"ID": identity, "VERSION": number, "START_N": start, "END_N": end, "FIPS": ""}


def event(**values):
    return dict.fromkeys(q.EVENT_FIELDS, "") | values


def snapshot_inputs():
    rows = [dict.fromkeys(q.FIELDS, "") | version() | {
        "NAME": "SYNTHETIC", "FULL_NAME": "Synthetic County", "CNTY_TYPE": "County",
        "CHANGE": "Synthetic mapped change", "CITATION": "Synthetic mapped citation"}]
    events = [event(**version(), CREATION_OR_CHANGE="Synthetic mapped change", CITATION="Synthetic mapped citation"),
              event(START_N="18610129", NAME="Synthetic event", CREATION_OR_CHANGE="Synthetic event without ID", CITATION="Synthetic event citation"),
              event(ID="synthetic_county", NAME="OLD NAME (see SYNTHETIC)")]
    receipts = [{"path": path, "bytes": 1, "sha256": str(index) * 64}
                for index, path in enumerate([q.SHAPE + "shp", q.SHAPE + "dbf", q.EVENTS], 1)]
    return rows, events, receipts


class CountyQualificationTests(unittest.TestCase):
    def test_inclusive_end_and_incoming_day(self):
        rows = [version(), version(18620101, 20001231, number=2)]
        self.assertEqual(q.select_rows(rows, dt.date(1861, 12, 31)), rows[:1])
        self.assertEqual(q.select_rows(rows, dt.date(1862, 1, 1)), rows[1:])
        self.assertEqual(q.interval(rows[-1])[1], dt.date(2001, 1, 1))

    def test_no_carry_forward_outside_source_coverage(self):
        for day in [dt.date(1804, 9, 30), dt.date(2001, 1, 1), dt.date(2026, 10, 29)]:
            with self.subTest(day=day), self.assertRaisesRegex(ValueError, "DATE_COVERAGE"):
                q.select_rows([version()], day)

    def test_calendar_dates_are_strict(self):
        self.assertEqual(q.source_date(20000229), dt.date(2000, 2, 29))
        for value in [19000229, 18610230, "1861-01-29", " 18610129", True, 18610129.0]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                q.source_date(value)
        with self.assertRaisesRegex(ValueError, "REVERSED_INTERVAL"):
            q.interval(version(18620101, 18610101))

    def test_missing_fips_does_not_erase_identity_or_gap(self):
        rows = [version(), version(18630101, 20001231, number=2)]
        self.assertEqual(q.select_rows(rows, dt.date(1862, 6, 1)), [])
        self.assertEqual(q.continuity(rows), [{"id": "synthetic_county", "fromInclusive": "1862-01-01", "toExclusive": "1863-01-01", "days": 365}])

    def test_duplicate_identity_and_overlap_fail(self):
        first = version()
        for rows, code in [([first, first], "DUPLICATE_VERSION"),
                           ([first, version(18611231, 18621231, number=2)], "SAME_INSTITUTION_OVERLAP"),
                           ([first, version(18620101, 18621231)], "REUSED_VERSION")]:
            with self.subTest(code=code), self.assertRaisesRegex(ValueError, code):
                q.continuity(rows)

    def test_event_without_end_is_not_open_ended_geometry(self):
        row = event(START_N="18610129", CREATION_OR_CHANGE="Synthetic dated event", CITATION="Synthetic citation")
        self.assertEqual(q.chronology_kind(row), "event_only")
        row["CITATION"] = ""
        with self.assertRaisesRegex(ValueError, "EVENT_EVIDENCE"):
            q.chronology_kind(row)

    def test_earlier_chronology_does_not_extend_geometry_coverage(self):
        row = event(START_N="18030430", CREATION_OR_CHANGE="Synthetic earlier event", CITATION="Synthetic citation")
        self.assertEqual(q.chronology_kind(row), "event_only")
        with self.assertRaisesRegex(ValueError, "DATE_COVERAGE"):
            q.interval(version(18030430, 18041001))

    def test_alias_without_dates_is_not_a_change_event(self):
        row = event(ID="synthetic_county", NAME="OLD NAME (see NEW NAME)")
        self.assertEqual(q.chronology_kind(row), "name_cross_reference")
        row["CREATION_OR_CHANGE"] = "A supposed event"
        with self.assertRaisesRegex(ValueError, "ALIAS_EVENT_CONFLICT"):
            q.chronology_kind(row)
        with self.assertRaisesRegex(ValueError, "UNDATED_RECORD"):
            q.chronology_kind(event(ID="synthetic_county", NAME="Ambiguous undated row"))

    def test_mapped_version_needs_citation_and_complete_dates(self):
        row = event(**version(), CREATION_OR_CHANGE="Synthetic version", CITATION="Synthetic citation")
        self.assertEqual(q.chronology_kind(row), "mapped_version")
        row["START_N"] = ""
        with self.assertRaises(ValueError):
            q.chronology_kind(row)

    def test_geometry_checks_without_claiming_topology(self):
        ring = [(-100., 37.), (-99., 37.), (-99., 38.), (-100., 37.)]
        q.check_geometry(ring, [0])
        cases = [(ring[:-1], [0]), (ring, [1]), (ring, [0, 0]),
                 ([(float("nan"), 37.)] + ring[1:], [0]),
                 ([(-181., 37.)] + ring[1:], [0]),
                 ([(-100., 37.)] * 4, [0]),
                 ([(-100., 37.), (-99., 37.), (-98., 37.), (-100., 37.)], [0])]
        for points, parts in cases:
            with self.subTest(points=points, parts=parts), self.assertRaises(ValueError):
                q.check_geometry(points, parts)

    def test_archive_pin_rejects_changed_bytes_before_parsing(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "different.zip"
            path.write_bytes(b"not the qualified archive")
            with self.assertRaisesRegex(ValueError, "ARCHIVE_DIGEST"):
                q.read_pinned_archive(path)
            link = Path(folder) / "alias.zip"
            link.symlink_to(path)
            with self.assertRaises(OSError):
                q.read_pinned_archive(link)
        with self.assertRaisesRegex(ValueError, "LOCAL_FILE_REQUIRED"):
            q.read_pinned_archive("https://example.org/archive.zip")

    def test_zip_members_cannot_escape_or_alias_paths(self):
        for name in ["../escape", "/absolute", q.ROOT + "../escape", q.ROOT + "bad\\path"]:
            with self.subTest(name=name):
                data = io.BytesIO()
                with zipfile.ZipFile(data, "w") as archive:
                    archive.writestr(name, b"synthetic")
                with zipfile.ZipFile(io.BytesIO(data.getvalue())) as archive:
                    with self.assertRaisesRegex(ValueError, "ZIP_PATH"):
                        q.checked_members(archive)

    def test_zip_requires_source_members_and_bounded_expansion(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w") as archive:
            archive.writestr(q.ROOT + "incomplete", b"synthetic")
        with zipfile.ZipFile(io.BytesIO(data.getvalue())) as archive:
            with self.assertRaisesRegex(ValueError, "ZIP_REQUIRED_MEMBERS"):
                q.checked_members(archive)
            archive.infolist()[0].file_size = q.MAX_ARCHIVE + 1
            with self.assertRaisesRegex(ValueError, "ZIP_ENTRY_SIZE"):
                q.checked_members(archive)

    def test_query_rejects_ambiguous_dates_before_opening_archive(self):
        self.assertEqual(q.query_date("1861-01-29"), dt.date(1861, 1, 29))
        for value in ["18610129", "1861-1-29", "1861-01-29T00:00:00Z", " 1861-01-29", "1900-02-29", "2001-01-01"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                q.query_date(value)
        result = subprocess.run([sys.executable, str(Path(q.__file__)), "does-not-exist.zip", "--date", "2001-01-01"],
                                text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout), {"status": "ERROR", "releaseEligible": False, "error": "DATE_COVERAGE"})

    def test_snapshot_keeps_events_aliases_and_missing_ids_distinct(self):
        rows, events, receipts = snapshot_inputs()
        snapshot = q.dated_snapshot(rows, events, receipts, dt.date(1861, 1, 29))
        self.assertEqual(len(snapshot["boundaryVersions"]), 1)
        self.assertIsNone(snapshot["boundaryVersions"][0]["fips"])
        self.assertEqual(snapshot["boundaryVersions"][0]["validToExclusive"], "1862-01-01")
        self.assertIsNone(snapshot["eventOnlyRecordsOnDay"][0]["institutionSourceId"])
        self.assertEqual(snapshot["undatedNameCrossReferences"][0]["temporalApplicability"], "unknown")
        self.assertFalse(snapshot["geometryIncluded"])
        self.assertFalse(snapshot["releaseEligible"])
        tomorrow = q.dated_snapshot(rows, events, receipts, dt.date(1861, 1, 30))
        self.assertEqual(tomorrow["eventOnlyRecordsOnDay"], [])
        self.assertEqual(tomorrow["boundaryVersions"][0]["id"], snapshot["boundaryVersions"][0]["id"])
        gap = q.dated_snapshot(rows, events, receipts, dt.date(1862, 1, 1))
        self.assertEqual(gap["boundaryVersions"], [])

    def test_snapshot_evidence_refs_resolve_and_source_record_numbers_survive_filtering(self):
        rows, events, receipts = snapshot_inputs()
        earlier = rows[0] | version(18600101, 18601231, identity="synthetic_earlier")
        rows.insert(0, earlier)
        events.insert(0, event(**version(18600101, 18601231, identity="synthetic_earlier"),
                               CREATION_OR_CHANGE="Earlier synthetic change", CITATION="Earlier synthetic citation"))
        snapshot = q.dated_snapshot(rows, events, receipts, dt.date(1861, 1, 29))
        version_record = snapshot["boundaryVersions"][0]
        self.assertEqual([ref["recordNumber"] for ref in version_record["evidenceRefs"]], [2, 2, 2])
        self.assertEqual(snapshot["eventOnlyRecordsOnDay"][0]["evidenceRefs"][0]["recordNumber"], 3)
        for item in snapshot["boundaryVersions"] + snapshot["eventOnlyRecordsOnDay"] + snapshot["undatedNameCrossReferences"]:
            for ref in item["evidenceRefs"]:
                self.assertIn(ref["artifactId"], snapshot["evidenceBundle"]["artifacts"])
        with self.assertRaisesRegex(ValueError, "SNAPSHOT_EVIDENCE"):
            q.dated_snapshot(rows, events, receipts[:-1], dt.date(1861, 1, 29))

    def test_source_revision_and_version_interval_are_part_of_identity(self):
        rows, events, receipts = snapshot_inputs()
        before = q.dated_snapshot(rows, events, receipts, dt.date(1861, 1, 29))
        rows[0]["END_N"] = events[0]["END_N"] = 18611230
        changed = q.dated_snapshot(rows, events, receipts, dt.date(1861, 1, 29))
        self.assertNotEqual(before["boundaryVersions"][0]["id"], changed["boundaryVersions"][0]["id"])
        original_digest = q.ARCHIVE_SHA256
        try:
            q.ARCHIVE_SHA256 = "f" * 64
            revision = q.dated_snapshot(rows, events, receipts, dt.date(1861, 1, 29))
        finally:
            q.ARCHIVE_SHA256 = original_digest
        self.assertNotEqual(changed["eventOnlyRecordsOnDay"][0]["id"], revision["eventOnlyRecordsOnDay"][0]["id"])

    def test_missing_chronology_join_fails_instead_of_exporting_uncited_record(self):
        rows, events, receipts = snapshot_inputs()
        with self.assertRaisesRegex(ValueError, "SNAPSHOT_VERSION_JOIN"):
            q.dated_snapshot(rows, events[1:], receipts, dt.date(1861, 1, 29))


@unittest.skipUnless(os.environ.get("KFM_COUNTY_ARCHIVE"), "Set KFM_COUNTY_ARCHIVE for opt-in real-source checks")
class RealCountyArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import shapefile
        cls.path = os.environ["KFM_COUNTY_ARCHIVE"]
        cls.report = q.qualify(cls.path)
        with zipfile.ZipFile(cls.path) as archive:
            cls.events = list(csv.DictReader(io.StringIO(archive.read(q.EVENTS).decode("cp1252")), delimiter="\t"))
            with shapefile.Reader(shp=io.BytesIO(archive.read(q.SHAPE + "shp")),
                                  shx=io.BytesIO(archive.read(q.SHAPE + "shx")),
                                  dbf=io.BytesIO(archive.read(q.SHAPE + "dbf")), encoding="cp1252") as reader:
                cls.rows = [row.as_dict() for row in reader.records()]

    def snapshot(self, day):
        return q.dated_snapshot(self.rows, self.events, self.report["members"], day)

    def test_all_transition_days_match_source_numeric_intervals_and_locators(self):
        days = {q.FIRST, q.LAST}
        for row in self.rows:
            for field in ["START_N", "END_N"]:
                value = str(row[field])
                boundary = dt.date(int(value[:4]), int(value[4:6]), int(value[6:]))
                days.update(boundary + dt.timedelta(days=offset) for offset in [-1, 0, 1]
                            if q.FIRST <= boundary + dt.timedelta(days=offset) <= q.LAST)
        for day in sorted(days):
            with self.subTest(day=day):
                numeric_day = int(day.strftime("%Y%m%d"))
                expected = {index for index, row in enumerate(self.rows, 1)
                            if row["START_N"] <= numeric_day <= row["END_N"]}
                snapshot = self.snapshot(day)
                actual = {item["evidenceRefs"][0]["recordNumber"] for item in snapshot["boundaryVersions"]}
                self.assertEqual(actual, expected)
                self.assertEqual(len(actual), len(snapshot["boundaryVersions"]))
                for item in snapshot["boundaryVersions"]:
                    record = self.events[item["evidenceRefs"][2]["recordNumber"] - 1]
                    self.assertEqual(record["ID"], item["institutionSourceId"])
                    self.assertEqual(int(record["VERSION"]), item["sourceVersion"])
                expected_events = {index for index, row in enumerate(self.events, 1)
                                   if not row["END_N"] and row["START_N"] == str(numeric_day)}
                actual_events = {item["evidenceRefs"][0]["recordNumber"] for item in snapshot["eventOnlyRecordsOnDay"]}
                self.assertEqual(actual_events, expected_events)

    def test_known_frames_and_clark_disappearance_and_return(self):
        expected = {"1804-10-01": 4, "1854-05-30": 2, "1855-08-25": 39, "1861-01-29": 50,
                    "1880-01-01": 105, "1900-01-01": 106, "2000-12-31": 105}
        for day, count in expected.items():
            self.assertEqual(len(self.snapshot(dt.date.fromisoformat(day))["boundaryVersions"]), count)
        for day, present in [("1883-02-21", True), ("1883-02-22", False), ("1885-03-12", False), ("1885-03-13", True)]:
            ids = {item["institutionSourceId"] for item in self.snapshot(dt.date.fromisoformat(day))["boundaryVersions"]}
            self.assertEqual("kss_clark" in ids, present)

    def test_repeated_full_qualification_is_deterministic_and_not_a_release(self):
        self.assertNotIn("snapshot", self.report)
        first = q.qualify(self.path, dt.date(1861, 1, 29))
        second = q.qualify(self.path, dt.date(1861, 1, 29))
        self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))
        self.assertEqual(first["status"], "HOLD")
        self.assertFalse(first["releaseEligible"])
        self.assertEqual(first["snapshot"]["selectedDay"], "1861-01-29")
        self.assertEqual(len(first["snapshot"]["boundaryVersions"]), 50)
        self.assertEqual(len(first["snapshot"]["undatedNameCrossReferences"]), 16)
        cli = subprocess.run([sys.executable, str(Path(q.__file__)), self.path, "--date", "1861-01-29"],
                             text=True, capture_output=True, check=False)
        self.assertEqual(cli.returncode, 0, cli.stderr)
        self.assertEqual(json.loads(cli.stdout), first)


if __name__ == "__main__":
    unittest.main()
