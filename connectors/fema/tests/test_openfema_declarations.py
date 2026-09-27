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


def body(rows, *, skip=0, top=2, count=None, odata_filter=FILTER, **meta):
    metadata = {"skip": skip, "top": top, "filter": odata_filter, "count":
                len(rows) if count is None else count, "entityname": of.ENTITY,
                "rundate": "2026-09-27T00:00:00.000Z", **meta}
    return json.dumps({"metadata": metadata, of.ENTITY: rows}).encode()


def parse(rows=None, *, skip=0, top=2, count=None, **meta):
    url = of.page_url(FILTER, skip=skip, top=top)
    return of.parse_page(body([record()] if rows is None else rows, skip=skip, top=top,
                              count=count, **meta), status=200, source_url=url,
                         retrieved_at=NOW)


class PlanTests(unittest.TestCase):
    def test_url_is_deterministic_and_counted(self):
        params = parse_qs(urlsplit(of.page_url(FILTER, skip=20, top=10)).query)
        self.assertEqual(params["$filter"], ["state eq 'KS'"])
        self.assertEqual((params["$orderby"], params["$count"]), (["id"], ["true"]))
        self.assertEqual((params["$skip"], params["$top"]), (["20"], ["10"]))

    def test_filter_window_and_rejections(self):
        self.assertEqual(of.declaration_filter(declared_from="2000-01-01", declared_to="2010-01-01"),
                         "state eq 'KS' and declarationDate ge '2000-01-01T00:00:00.000Z' "
                         "and declarationDate lt '2010-01-01T00:00:00.000Z'")
        for kwargs in ({"declared_from": "2000-1-1"},
                       {"declared_from": "2010-01-01", "declared_to": "2000-01-01"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(of.OpenFemaInputError):
                of.declaration_filter(**kwargs)
        for args in (("state eq 'OK'",), (FILTER,)):
            with self.assertRaises(of.OpenFemaInputError):
                of.page_url(*args, top=10_001) if args == (FILTER,) else of.page_url(*args)

    def test_source_url_allowlist(self):
        good = of.page_url(FILTER)
        for bad in (good.replace("https", "http"), good.replace("www.fema.gov", "evil.gov"),
                    good.replace("orderby=id", "orderby=declarationDate"),
                    good.replace("count=true", "count=false"), good + "&$select=id",
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


class ReconcileTests(unittest.TestCase):
    def walk(self, total=5, top=2, count=None):
        pages, skip = [], 0
        while True:
            rows = [record(n) for n in range(skip + 1, min(skip + top, total) + 1)]
            page = parse(rows, skip=skip, top=top, count=total if count is None else count)
            pages.append(page)
            nxt = of.next_page_url(page)
            if nxt is None:
                return pages
            skip += top

    def test_complete_capture(self):
        capture = of.reconcile(list(reversed(self.walk())))
        self.assertEqual(capture.outcome, "CAPTURE_CANDIDATE")
        self.assertEqual(len(capture.records), 5)
        self.assertEqual(capture.coverage, "NOT_ESTABLISHED")

    def test_incomplete_captures(self):
        pages = self.walk()
        self.assertIn("PAGE_GAP_OR_OVERLAP", of.reconcile([pages[0], pages[2]]).reasons)
        self.assertIn("END_NOT_REACHED", of.reconcile(pages[:2]).reasons)
        drifted = parse([record(3), record(4)], skip=2, count=9)
        self.assertIn("COUNT_DRIFT", of.reconcile([pages[0], drifted, pages[2]]).reasons)
        self.assertIn("COUNT_MISMATCH", of.reconcile(self.walk(count=7)).reasons)
        repeated = parse([record(2), record(3)], skip=2, count=5)
        self.assertIn("DUPLICATE_ACROSS_PAGES",
                      of.reconcile([pages[0], repeated, pages[2]]).reasons)
        with self.assertRaises(of.OpenFemaInputError):
            of.reconcile([])


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            of.reconcile([parse()])


if __name__ == "__main__":
    unittest.main()
