"""Deterministic synthetic tests; no Census access, disclosure review, or admission claim."""
from dataclasses import FrozenInstanceError
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

PATH = Path(__file__).resolve().parents[1] / "src/census/acs_api.py"
SPEC = importlib.util.spec_from_file_location("kfm_census_acs_api_tested", PATH)
acs = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = acs
SPEC.loader.exec_module(acs)
NOW = "2026-09-26T12:00:00Z"
VARS = ("NAME", "B01001_001E")
URL = acs.acs_url(2023, "acs/acs5", VARS, "county")
HEADER = ["NAME", "B01001_001E", "B01001_001M", "state", "county"]


def body(rows, header=HEADER):
    return json.dumps([header, *rows]).encode()


def parse(rows, url=URL, header=HEADER, status=200):
    return acs.parse_response(body(rows, header), status=status, source_url=url,
                              retrieved_at=NOW)


class PlanTests(unittest.TestCase):
    def test_url_pairs_moe_and_scopes_kansas(self):
        params = parse_qs(urlsplit(URL).query)
        self.assertEqual(params["get"], ["NAME,B01001_001E,B01001_001M"])
        self.assertEqual(params["for"], ["county:*"])
        self.assertEqual(params["in"], ["state:20"])
        self.assertNotIn("key", params)
        state = parse_qs(urlsplit(acs.acs_url(2023, "acs/acs5", ["B01001_001E"], "state")).query)
        self.assertEqual((state["for"], "in" in state), (["state:20"], False))
        bg = parse_qs(urlsplit(acs.acs_url(2023, "acs/acs5", ["B01001_001E"],
                                           "block group")).query)
        self.assertEqual(bg["in"], ["state:20 county:*"])
        pe = acs.acs_url(2023, "acs/acs5/profile", ["DP05_0001PE"], "county")
        self.assertIn("DP05_0001PM", parse_qs(urlsplit(pe).query)["get"][0])
        subject = acs.acs_url(2023, "acs/acs5/subject", ["S0101_C01_001E"], "county")
        self.assertIn("S0101_C01_001M", parse_qs(urlsplit(subject).query)["get"][0])

    def test_plan_rejections(self):
        for args in ((2004, "acs/acs5", VARS, "county"), (2023, "dec/pl", VARS, "county"),
                     (2023, "acs/acs5", ("B01001_001X",), "county"),
                     (2023, "acs/acs5", (), "county"), (2023, "acs/acs5", VARS, "zcta"),
                     (2023, "acs/acs5", [f"B01001_{i:03d}E" for i in range(30)], "county")):
            with self.subTest(args=args[:2] + (args[3],)), \
                    self.assertRaises(acs.AcsInputError):
                acs.acs_url(*args)

    def test_source_url_rejections(self):
        with self.assertRaises(acs.AcsInputError) as caught:
            parse([], url=URL + "&key=SECRETKEY")
        self.assertEqual(str(caught.exception), "API_KEY_IN_URL")
        self.assertNotIn("SECRETKEY", str(caught.exception))
        for bad in (URL.replace("https", "http"), URL.replace("state%3A20", "state%3A40"),
                    URL.replace("api.census.gov", "example.org"), URL + "&extra=1",
                    URL.replace("acs/acs5", "acs/acs3")):
            with self.subTest(bad=bad), self.assertRaises(acs.AcsInputError):
                parse([], url=bad)


class ParseTests(unittest.TestCase):
    def test_numbers_are_exact_decimals(self):
        table = parse([["Synthetic County, Kansas", "1234", "56", "20", "001"],
                       ["Other County, Kansas", "0", "13", "20", "003"]])
        first, second = table.rows
        self.assertEqual(first.geoid, "20001")
        self.assertEqual(first.name, "Synthetic County, Kansas")
        self.assertEqual([v.value for v in first.values[1:]], [Decimal("1234"), Decimal("56")])
        self.assertEqual(second.values[1].value, Decimal("0"))
        self.assertEqual(first.route, "RAW_CANDIDATE")
        self.assertEqual((table.coverage, table.admission), ("NOT_ESTABLISHED", "NOT_ADMITTED"))
        with self.assertRaises(FrozenInstanceError):
            first.route = "PUBLISHED"

    def test_annotations_never_become_numbers_or_zero(self):
        for raw, annotation in acs.ANNOTATIONS.items():
            with self.subTest(raw=raw):
                (row,) = parse([["X", raw, "-555555555", "20", "001"]]).rows
                estimate, moe = row.values[1], row.values[2]
                self.assertIsNone(estimate.value)
                self.assertEqual((estimate.raw, estimate.annotation), (raw, annotation))
                self.assertEqual(moe.annotation, "MOE_CONTROLLED_NO_SAMPLING_ERROR")
                self.assertEqual(row.route, "RAW_CANDIDATE")
        (row,) = parse([["X", None, "1", "20", "001"]]).rows
        self.assertEqual((row.values[1].value, row.values[1].annotation),
                         (None, "NULL_FROM_SOURCE"))

    def test_unrecognized_negative_quarantines(self):
        (row,) = parse([["X", "-5", "1", "20", "001"]]).rows
        self.assertEqual((row.route, row.reasons), ("QUARANTINE_CANDIDATE",
                                                     ("UNRECOGNIZED_NEGATIVE",)))
        self.assertIsNone(row.values[1].value)

    def test_estimate_without_moe_flagged(self):
        url = acs.acs_url(2023, "acs/acs5", VARS, "county", pair_moe=False)
        table = parse([["X", "1", "20", "001"]], url=url,
                      header=["NAME", "B01001_001E", "state", "county"])
        self.assertEqual(table.table_reasons, ("ESTIMATE_WITHOUT_MOE",))

    def test_empty_results_are_not_absence(self):
        empty = acs.parse_response(b"", status=204, source_url=URL, retrieved_at=NOW)
        self.assertTrue(empty.empty_result)
        self.assertEqual(empty.table_reasons, ("EMPTY_RESULT_NOT_ABSENCE",))
        self.assertTrue(parse([]).empty_result)

    def test_malformed_tables_rejected_whole(self):
        cases = {
            "header": ([["X", "1", "2", "20", "001"]], ["NAME", "B", "C", "state", "county"]),
            "width": ([["X", "1", "20", "001"]], HEADER),
            "other state": ([["X", "1", "2", "40", "001"]], HEADER),
            "bad county": ([["X", "1", "2", "20", "1"]], HEADER),
            "duplicate": ([["X", "1", "2", "20", "001"], ["Y", "1", "2", "20", "001"]], HEADER),
            "text number": ([["X", "1,234", "2", "20", "001"]], HEADER),
            "non-string": ([["X", 1234, "2", "20", "001"]], HEADER),
        }
        for name, (rows, header) in cases.items():
            with self.subTest(name=name), self.assertRaises(acs.AcsInputError):
                parse(rows, header=header)
        for raw in (b'{"error": "x"}', b"[[NaN]]", b"not json", b"[]"):
            with self.subTest(raw=raw), self.assertRaises(acs.AcsInputError):
                acs.parse_response(raw, status=200, source_url=URL, retrieved_at=NOW)
        for status, code in ((429, "RATE_LIMITED"), (400, "HTTP_STATUS")):
            with self.assertRaises(acs.AcsInputError) as caught:
                acs.parse_response(b"error", status=status, source_url=URL, retrieved_at=NOW)
            self.assertEqual(str(caught.exception), code)

    def test_state_level_request(self):
        url = acs.acs_url(2023, "acs/acs5", ["B01001_001E"], "state")
        table = parse([["5", "2", "20"]], url=url,
                      header=["B01001_001E", "B01001_001M", "state"])
        self.assertEqual((table.request.geography, table.rows[0].geoid), ("state", "20"))

    def test_tract_geoid(self):
        url = acs.acs_url(2023, "acs/acs5", ["B01001_001E"], "tract")
        (row,) = parse([["5", "2", "20", "001", "000100"]], url=url,
                       header=["B01001_001E", "B01001_001M", "state", "county", "tract"]).rows
        self.assertEqual(row.geoid, "20001000100")


class NestingBoundTests(unittest.TestCase):
    def call(self, depth):
        raw = ("[" * depth + "]" * depth).encode()
        with self.assertRaises(acs.AcsInputError) as ctx:
            acs.parse_response(raw, status=200, source_url=URL, retrieved_at=NOW)
        return str(ctx.exception)

    def test_bound_is_exact_and_interpreter_independent(self):
        self.assertEqual(acs.MAX_NESTING, 32)
        self.assertNotEqual(self.call(acs.MAX_NESTING), "NESTING_DEPTH")
        # Past the bound, and past 3.11's decoder limit, the code is the same everywhere.
        for depth in (acs.MAX_NESTING + 1, 5000, 100_000):
            with self.subTest(depth=depth):
                self.assertEqual(self.call(depth), "NESTING_DEPTH")


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            parse([["X", "1", "2", "20", "001"]])


if __name__ == "__main__":
    unittest.main()
