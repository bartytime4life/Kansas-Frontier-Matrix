"""Deterministic storage, station selection and source-format boundary tests."""
import gzip
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from connectors.noaa.src.noaa import ghcnd as s
from tools.local_data import noaa_ghcnd as op
from tools.local_data.manage import init_store

SID = "USW00013984"
RUN = "20261007T180000Z"


def station(sid=SID, state="KS", lat=39.0):
    return f"{sid} {lat:8.4f} {-98.0:9.4f} {400:6.1f} {state} {'TEST STATION':30s} {'':3s} {'HCN':3s} {'':5s}\n".encode()


def csv_body(sid=SID):
    return gzip.compress((f"{sid},19000228,TMIN,-120,,X,0,0700\n"
                          f"{sid},20200229,PRCP,0,T,,N,\n").encode(), mtime=0)


def provider(key, limit):
    body = {
        "ghcnd-stations.txt": station()+station("USW00000001", "NE"),
        "by_station/": (f'<td><a href="{SID}.csv.gz">{SID}.csv.gz</a></td>\n'
                        f'<td align="right">2026-10-07 12:00</td>\n<td align="right">{len(csv_body())}</td>').encode(),
        "ghcnd-inventory.txt": f"{SID} {39.0:8.4f} {-98.0:9.4f} PRCP 1900 2020\n".encode(),
        "by_station/"+SID+".csv.gz": csv_body(),
    }.get(key, b"NOAA source documentation\n")
    return body, {"source_url": s.object_url(key), "retrieved_at": "2026-10-07T18:00:00Z",
                  "etag": None, "last_modified": None, "provider_checksum": None}


class SourceTests(unittest.TestCase):
    def test_kansas_state_selection_and_coordinates(self):
        self.assertEqual(list(s.kansas_stations(station()+station("USW00000001", "NE"))), [SID])
        with self.assertRaises(ValueError):
            s.kansas_stations(station(lat=15))

    def test_utf8_names_in_global_metadata(self):
        foreign = station("USW00000001", "NE").replace(b"TEST STATION", "CAFÉ STATION".encode())
        self.assertEqual(list(s.kansas_stations(station()+foreign)), [SID])

    def test_preserves_flags_and_whole_history(self):
        summary = s.inspect_station(csv_body(), SID)
        self.assertEqual(summary["first_date"], "19000228")
        self.assertEqual(summary["last_date"], "20200229")
        self.assertEqual(summary["quality_flags"], {"X": 1, "blank": 1})
        self.assertEqual(summary["measurement_flags"]["T"], 1)

    def test_crc_mixed_station_and_expansion_limits(self):
        for payload, limit in [(csv_body()[:-5], s.EXPANDED_BYTES),
                               (csv_body("USW00000001"), s.EXPANDED_BYTES), (csv_body(), 8)]:
            with self.assertRaises((ValueError, EOFError, OSError)):
                s.inspect_station(payload, SID, expanded_limit=limit)

    def test_date_validation(self):
        with self.assertRaises(ValueError):
            s.inspect_station(gzip.compress(f"{SID},19000229,PRCP,5,,,0,\n".encode()), SID)

    def test_fixed_provider_keys(self):
        for key in ("../../secret", "by_station/USW00013984.csv.gz?redirect=evil", "ghcnd_all.tar.gz"):
            with self.assertRaises(ValueError):
                s.object_url(key)

    def test_transport_rejects_oversize_short_and_redirected_responses(self):
        class Response(io.BytesIO):
            status = 200
            def geturl(self):
                return self.url
        for body, declared, url in [(b"x", "100", s.BASE+"readme.txt"),
                                    (b"x", "2", s.BASE+"readme.txt"),
                                    (b"x", "1", "https://other.invalid/readme.txt"),
                                    (b"long", None, s.BASE+"readme.txt")]:
            response = Response(body)
            response.headers = {} if declared is None else {"Content-Length": declared}
            response.url = url
            with patch.object(s, "build_opener") as opener:
                opener.return_value.open.return_value = response
                with self.assertRaises(ValueError):
                    s.fetch("readme.txt", 3)

    def test_global_archive_denied_without_network(self):
        with patch.object(s, "build_opener") as opener:
            with self.assertRaises(ValueError):
                s.fetch("ghcnd_all.tar.gz", 100)
            opener.assert_not_called()


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/"store"
        init_store(self.root)
        self.free = patch.object(op.shutil, "disk_usage", return_value=type("Disk", (), {"free": 2**42})())
        self.free.start()
        self.addCleanup(self.free.stop)

    def prepare(self):
        return op.prepare(self.root, RUN, fetcher=provider)

    def test_capture_verify_and_no_redownload_on_retry(self):
        self.prepare()
        report = op.capture(self.root, RUN, fetcher=provider)
        self.assertFalse(report["released"])
        self.assertEqual(report["captured_stations"], 1)
        verified = op.verify(self.root, RUN)
        self.assertEqual(verified["rows_checked"], 2)
        index = json.loads(Path(verified["index"]).read_text())
        self.assertEqual(index["features"][0]["properties"]["quality_flagged_rows"], 1)
        with patch.object(op.source, "utc_now", return_value="2026-10-07T18:30:00Z"):
            again = op.capture(self.root, RUN, fetcher=lambda *args: self.fail("must reuse"))
        self.assertEqual(again["compressed_station_bytes"], len(csv_body()))

    def test_tamper_is_rejected(self):
        self.prepare()
        op.capture(self.root, RUN, fetcher=provider)
        path = op.paths(self.root, RUN)[0]/"stations"/(SID+".csv.gz")
        path.write_bytes(b"bad")
        with self.assertRaises(ValueError):
            op.verify(self.root, RUN)

    def test_disk_reserve_and_cap_stop_before_fetch(self):
        with self.assertRaisesRegex(ValueError, "SOURCE_STORAGE_CAP"):
            op.prepare(self.root, RUN, cap=100, fetcher=lambda *args: self.fail("no network"))
        with patch.object(op.shutil, "disk_usage", return_value=type("Disk", (), {"free": 100})()):
            with self.assertRaisesRegex(ValueError, "FREE_SPACE_RESERVE"):
                self.prepare()

    def test_failed_station_remains_partial(self):
        self.prepare()
        def fail(*args):
            raise OSError("synthetic failure")
        report = op.capture(self.root, RUN, fetcher=fail)
        self.assertEqual(report["status"], "PARTIAL")
        self.assertEqual(report["failures"][0]["station_id"], SID)

    def test_symlink_and_traversal_denied(self):
        with self.assertRaises(ValueError):
            op.paths(self.root, "../escape")
        (self.root/"data/raw/noaa-ghcnd").symlink_to(self.root/"data/published", target_is_directory=True)
        with self.assertRaises(ValueError):
            self.prepare()

    def test_metadata_network_interruption_reuses_captured_objects(self):
        def fail(key, limit):
            if key == "ghcnd-inventory.txt":
                raise OSError("interrupted")
            return provider(key, limit)
        with self.assertRaises(OSError):
            op.prepare(self.root, RUN, fetcher=fail)
        calls = []
        def retry(key, limit):
            calls.append(key)
            return provider(key, limit)
        op.prepare(self.root, RUN, fetcher=retry)
        self.assertNotIn("ghcnd-stations.txt", calls)


if __name__ == "__main__":
    unittest.main()
