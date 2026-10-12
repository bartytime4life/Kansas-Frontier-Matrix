"""Deterministic synthetic tests; no FEMA access, rights review, or admission claim."""
from dataclasses import FrozenInstanceError
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

PATH = Path(__file__).resolve().parents[1] / "src/fema/openfema_declarations.py"
SPEC = importlib.util.spec_from_file_location("kfm_fema_openfema_declarations_tested", PATH)
of = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = of
SPEC.loader.exec_module(of)
NOW = "2026-09-27T12:00:00Z"
FILTER = of.declaration_filter()


def rid(n):
    return f"00000000-0000-4000-8000-{n:012d}"


def record(n=1, **overrides):
    # Synthetic values only: not a real FEMA declaration.
    base = {"femaDeclarationString": "DR-9001-KS", "disasterNumber": 9001, "state": "KS",
            "declarationType": "DR", "declarationDate": "2020-05-01T00:00:00.000Z",
            "fyDeclared": 2020, "incidentType": "Flood", "declarationTitle": "SYNTHETIC",
            "ihProgramDeclared": False, "iaProgramDeclared": True, "paProgramDeclared": True,
            "hmProgramDeclared": True, "incidentBeginDate": "2020-04-01T00:00:00.000Z",
            "incidentEndDate": "2020-04-10T00:00:00.000Z", "disasterCloseoutDate": None,
            "tribalRequest": False, "fipsStateCode": "20", "fipsCountyCode": f"{n:03d}",
            "placeCode": "99001", "designatedArea": "Synthetic (County)",
            "declarationRequestNumber": "20001", "lastRefresh": "2026-01-01T00:00:00.000Z",
            "hash": "abc123", "id": rid(n), "region": 7}
    base.update(overrides)
    return {k: v for k, v in base.items() if v is not ...}


def full_filter(after_id=None, base=FILTER):
    return base if after_id is None else f"{base} and id gt '{after_id}'"


def body(rows, *, after_id=None, top=2, count=None, odata_filter=None, skip=0, **meta):
    metadata = {"skip": skip, "top": top, "filter": odata_filter or full_filter(after_id), "count":
                len(rows) if count is None else count, "entityname": of.ENTITY,
                "rundate": "2026-09-27T00:00:00.000Z", **meta}
    return json.dumps({"metadata": metadata, of.ENTITY: rows}).encode()


def parse(rows=None, *, after_id=None, top=2, count=None, base=FILTER, **meta):
    url = of.page_url(base, after_id=after_id, top=top)
    return of.parse_page(body([record()] if rows is None else rows, after_id=after_id, top=top,
                              count=count, odata_filter=full_filter(after_id, base), **meta),
                         status=200, source_url=url, retrieved_at=NOW)


class PlanTests(unittest.TestCase):
    def test_url_is_keyset_ordered_and_counted(self):
        params = parse_qs(urlsplit(of.page_url(FILTER, after_id=rid(7), top=10)).query)
        self.assertEqual(params["$filter"], [f"state eq 'KS' and id gt '{rid(7)}'"])
        self.assertEqual((params["$orderby"], params["$count"]), (["id"], ["true"]))
        self.assertEqual(params["$top"], ["10"])
        self.assertNotIn("$skip", params)

    def test_filter_window_and_rejections(self):
        self.assertEqual(of.declaration_filter(declared_from="2000-01-01", declared_to="2010-01-01"),
                         "state eq 'KS' and declarationDate ge '2000-01-01T00:00:00.000Z' "
                         "and declarationDate lt '2010-01-01T00:00:00.000Z'")
        for kwargs in ({"declared_from": "2000-1-1"}, {"declared_from": "2026-02-31"},
                       {"declared_to": "2026-99-99"},
                       {"declared_from": "2010-01-01", "declared_to": "2000-01-01"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(of.OpenFemaInputError):
                of.declaration_filter(**kwargs)
        for bad in ("state eq 'OK'", "state eq 'KS' or 1 eq 1",
                    FILTER + f" and id gt '{rid(1)}'"):
            with self.subTest(bad=bad), self.assertRaises(of.OpenFemaInputError):
                of.page_url(bad)
        for kwargs in ({"top": 10_001}, {"after_id": "not-a-uuid"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(of.OpenFemaInputError):
                of.page_url(FILTER, **kwargs)

    def test_source_url_allowlist(self):
        good = of.page_url(FILTER)
        for bad in (good.replace("https", "http"), good.replace("www.fema.gov", "evil.gov"),
                    good.replace("orderby=id", "orderby=declarationDate"),
                    good.replace("count=true", "count=false"), good + "&$select=id",
                    good + "&$skip=5",
                    good.replace("/v2/", "/v1/")):
            # Body metadata matches the good request, so only the URL can be the reason.
            with self.subTest(bad=bad), self.assertRaises(of.OpenFemaInputError) as caught:
                of.parse_page(body([], top=1000), status=200, source_url=bad,
                              retrieved_at=NOW)
            self.assertEqual(str(caught.exception), "SOURCE_URL")
        of.parse_page(body([], top=1000), status=200, source_url=good, retrieved_at=NOW)


class ParseTests(unittest.TestCase):
    def test_administrative_candidate(self):
        (item,) = parse().records
        self.assertEqual((item.source_role, item.role_authority, item.admission),
                         ("administrative", "FEMA", "NOT_ADMITTED"))
        self.assertEqual(item.geography_semantics, "DESIGNATED_JURISDICTION_NOT_HAZARD_FOOTPRINT")
        self.assertEqual((item.declaration_date, item.incident_begin_date, item.incident_end_date),
                         ("2020-05-01T00:00:00Z", "2020-04-01T00:00:00Z", "2020-04-10T00:00:00Z"))
        self.assertEqual((item.designated_area_kind, item.route), ("county", "RAW_CANDIDATE"))
        self.assertIn(("paProgramDeclared", True), item.programs_declared)
        with self.assertRaises(FrozenInstanceError):
            item.source_role = "observation"

    def test_flags_and_quarantine(self):
        (statewide,) = parse([record(fipsCountyCode="000")]).records
        self.assertEqual(statewide.designated_area_kind, "statewide")
        (ongoing,) = parse([record(incidentEndDate=None)]).records
        self.assertEqual((ongoing.route, ongoing.reasons), ("RAW_CANDIDATE", ("INCIDENT_END_UNSET",)))
        (drift,) = parse([record(newField="x")]).records
        self.assertEqual(drift.reasons, ("SCHEMA_DRIFT_ADDITIONAL_FIELD",))
        self.assertIn('"newField":"x"', drift.raw_record_json)
        cases = {"INCIDENT_END_BEFORE_BEGIN": {"incidentEndDate": "2020-03-01T00:00:00.000Z"},
                 "DECLARATION_IDENTITY_INCONSISTENT": {"femaDeclarationString": "EM-9001-KS"},
                 "CLOSEOUT_BEFORE_DECLARATION": {"disasterCloseoutDate": "2019-01-01T00:00:00.000Z"}}
        for reason, overrides in cases.items():
            with self.subTest(reason=reason):
                (item,) = parse([record(**overrides)]).records
                self.assertEqual(item.route, "QUARANTINE_CANDIDATE")
                self.assertIn(reason, item.reasons)

    def test_malformed_pages_rejected_whole(self):
        cases = {
            "SCHEMA_FIELD_MISSING": [record(hash=...)],
            "STATE_SCOPE_MISMATCH": [record(state="OK", fipsStateCode="40")],
            "RECORD_ID": [record(id="not-a-uuid")],
            "DECLARATION_TYPE": [record(declarationType="XX")],
            "PROGRAM_FLAG": [record(iaProgramDeclared="yes")],
            "TIME_FORMAT": [record(declarationDate="May 2020")],
            "DUPLICATE_RECORD_ID": [record(1), record(1, fipsCountyCode="003")],
            "ORDER_NOT_DETERMINISTIC": [record(2), record(1)],
            "PAGE_LIMIT_EXCEEDED": [record(1), record(2), record(3)],
        }
        for code, rows in cases.items():
            with self.subTest(code=code), self.assertRaises(of.OpenFemaInputError) as caught:
                parse(rows)
            self.assertEqual(str(caught.exception), code)
        url = of.page_url(FILTER, top=2)
        for raw, code in ((body([], skip=5), "METADATA_REQUEST_MISMATCH"),
                          (body([], top=3), "METADATA_REQUEST_MISMATCH"),
                          (body([], odata_filter="state eq 'OK'"), "METADATA_REQUEST_MISMATCH"),
                          (b'{"DisasterDeclarationsSummaries": []}', "METADATA_ABSENT"),
                          (b'{"metadata": {"count": NaN}}', "NONSTANDARD_JSON_NUMBER"),
                          (b'{"metadata": {}, "metadata": {}}', "DUPLICATE_JSON_KEY")):
            with self.subTest(code=code), self.assertRaises(of.OpenFemaInputError) as caught:
                of.parse_page(raw, status=200, source_url=url, retrieved_at=NOW)
            self.assertEqual(str(caught.exception), code)
        for status, code in ((429, "RATE_LIMITED"), (500, "HTTP_STATUS")):
            with self.assertRaises(of.OpenFemaInputError) as caught:
                of.parse_page(b"", status=status, source_url=url, retrieved_at=NOW)
            self.assertEqual(str(caught.exception), code)


class WindowTests(unittest.TestCase):
    def test_rows_outside_requested_window_reject_page(self):
        base = of.declaration_filter(declared_from="2020-01-01", declared_to="2021-01-01")
        (inside,) = parse([record()], base=base).records
        self.assertEqual(inside.declaration_date, "2020-05-01T00:00:00Z")
        for when in ("2000-05-01T00:00:00.000Z", "2021-01-01T00:00:00.000Z"):
            with self.subTest(when=when), self.assertRaises(of.OpenFemaInputError) as caught:
                parse([record(declarationDate=when)], base=base)
            self.assertEqual(str(caught.exception), "ROW_OUTSIDE_REQUESTED_WINDOW")


class ReconcileTests(unittest.TestCase):
    def walk(self, ids=(1, 2, 3, 4, 5), top=2):
        """Simulate a keyset walk over a source holding ``ids``."""
        pages, cursor = [], None
        while True:
            remaining = [n for n in ids if cursor is None or rid(n) > cursor]
            page = parse([record(n) for n in remaining[:top]], after_id=cursor, top=top,
                         count=len(remaining))
            pages.append(page)
            nxt = of.next_page_url(page)
            if nxt is None:
                return pages
            cursor = page.records[-1].record_id

    def test_complete_capture(self):
        capture = of.reconcile(list(reversed(self.walk())))
        self.assertEqual(capture.outcome, "CAPTURE_CANDIDATE")
        self.assertEqual(len(capture.records), 5)
        self.assertEqual(capture.coverage, "NOT_ESTABLISHED")

    def test_incomplete_captures(self):
        pages = self.walk()
        self.assertIn("CURSOR_GAP_OR_OVERLAP", of.reconcile([pages[0], pages[2]]).reasons)
        self.assertIn("END_NOT_REACHED", of.reconcile(pages[:2]).reasons)
        self.assertIn("CURSOR_NOT_FROM_START", of.reconcile(pages[1:]).reasons)
        drifted = parse([record(3), record(4)], after_id=rid(2), count=9)
        self.assertIn("COUNT_DRIFT", of.reconcile([pages[0], drifted, pages[2]]).reasons)
        with self.assertRaises(of.OpenFemaInputError):
            of.reconcile([])

    def test_source_change_between_pages_is_detected(self):
        # Page one reads [1, 2] from {1, 2, 4, 5}; then 2 is deleted and 6 inserted.
        first = parse([record(1), record(2)], count=4)
        later_source = (1, 4, 5, 6)
        remaining = [n for n in later_source if rid(n) > rid(2)]
        second = parse([record(n) for n in remaining[:2]], after_id=rid(2), count=len(remaining))
        third = parse([record(6)], after_id=rid(5), count=1)
        capture = of.reconcile([first, second, third])
        self.assertEqual(capture.outcome, "INCOMPLETE_CAPTURE")
        self.assertIn("COUNT_DRIFT", capture.reasons)
        # An unchanged source over the same ids reconciles cleanly.
        self.assertEqual(of.reconcile(self.walk(ids=(1, 2, 4, 5))).outcome, "CAPTURE_CANDIDATE")

    def test_cursor_must_advance(self):
        with self.assertRaises(of.OpenFemaInputError) as caught:
            parse([record(1)], after_id=rid(1))
        self.assertEqual(str(caught.exception), "ORDER_NOT_DETERMINISTIC")


class NestingBoundTests(unittest.TestCase):
    def call(self, depth):
        raw = ("[" * depth + "]" * depth).encode()
        with self.assertRaises(of.OpenFemaInputError) as ctx:
            of.parse_page(raw, status=200, source_url=of.page_url(FILTER, top=2),
                          retrieved_at=NOW)
        return str(ctx.exception)

    def test_bound_is_exact_and_interpreter_independent(self):
        self.assertEqual(of.MAX_NESTING, 32)
        self.assertNotEqual(self.call(of.MAX_NESTING), "NESTING_DEPTH")
        # Past the bound, and past 3.11's decoder limit, the code is the same everywhere.
        for depth in (of.MAX_NESTING + 1, 5000, 100_000):
            with self.subTest(depth=depth):
                self.assertEqual(self.call(depth), "NESTING_DEPTH")


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            of.reconcile([parse()])


if __name__ == "__main__":
    unittest.main()
