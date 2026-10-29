"""Synthetic negative cases for the offline checker; these are not historical evidence."""
import datetime as dt
import importlib.util
import io
from pathlib import Path
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


if __name__ == "__main__":
    unittest.main()
