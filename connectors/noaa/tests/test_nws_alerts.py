"""Deterministic synthetic tests; no NWS access and no alerting or life-safety claim."""
from dataclasses import FrozenInstanceError
import importlib.util
import json
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "src/noaa/nws_alerts.py"
SPEC = importlib.util.spec_from_file_location("kfm_noaa_nws_alerts_tested", PATH)
nws = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = nws
SPEC.loader.exec_module(nws)
URL = nws.alerts_url("KS")
RETRIEVED = "2026-05-01T12:00:00Z"


def alert(n=1, **props):
    # Synthetic values only: not a real NWS message, event, or area.
    alert_id = f"urn:oid:2.49.0.1.840.0.synthetic.{n}"
    base = {"id": alert_id, "event": "Synthetic Weather Statement", "status": "Actual",
            "messageType": "Alert", "sender": "w-nws.webmaster@noaa.gov",
            "severity": "Minor", "certainty": "Likely", "urgency": "Expected",
            "sent": "2026-05-01T10:00:00Z", "effective": "2026-05-01T10:00:00Z",
            "onset": "2026-05-01T11:00:00Z", "expires": "2026-05-01T18:00:00Z",
            "ends": "2026-05-01T20:00:00Z", "references": [],
            "geocode": {"UGC": ["KSZ001"], "SAME": ["020001"]},
            "instruction": "SYNTHETIC-INSTRUCTION-TEXT", "unknown_field": {"kept": True}}
    base.update(props)
    base = {k: v for k, v in base.items() if v is not ...}
    return {"id": f"https://api.weather.gov/alerts/{alert_id}", "type": "Feature",
            "geometry": None, "properties": base}


def collection(features, **extra):
    return json.dumps({"type": "FeatureCollection", "features": features, **extra}).encode()


def parse(features=None, url=URL, **kwargs):
    return nws.parse_alerts(collection([alert()] if features is None else features),
                            status=200, source_url=url, retrieved_at=RETRIEVED, **kwargs)


class UrlTests(unittest.TestCase):
    def test_urls(self):
        self.assertEqual(URL, "https://api.weather.gov/alerts/active?area=KS")
        self.assertEqual(nws.alerts_url("KS", active=False),
                         "https://api.weather.gov/alerts?area=KS")
        for bad in ("ks", "KAN", ""):
            with self.subTest(bad=bad), self.assertRaises(nws.NwsInputError):
                nws.alerts_url(bad)
        for bad in (URL + "&cachebust=1", URL.replace("https", "http"),
                    "https://api.weather.gov/points/39,-98", URL.replace("KS", "ks")):
            with self.subTest(bad=bad), self.assertRaises(nws.NwsInputError):
                parse(url=bad)


class ParseTests(unittest.TestCase):
    def test_context_only_candidate(self):
        (item,) = parse().alerts
        self.assertEqual((item.authority, item.life_safety_authority, item.admission),
                         ("NWS_ISSUED_CONTEXT_ONLY", False, "NOT_ADMITTED"))
        self.assertEqual(item.freshness_state, "WITHIN_SOURCE_WINDOW_AT_AS_OF")
        self.assertEqual(item.freshness_as_of, RETRIEVED)
        self.assertTrue(item.has_instruction)
        self.assertEqual(item.route, "RAW_CANDIDATE")
        self.assertIn('"unknown_field":{"kept":true}', item.raw_feature_json)
        with self.assertRaises(FrozenInstanceError):
            item.life_safety_authority = True

    def test_instruction_text_is_never_a_field(self):
        (item,) = parse().alerts
        surfaced = [v for k, v in vars(item).items() if k != "raw_feature_json"]
        self.assertFalse(any("SYNTHETIC-INSTRUCTION-TEXT" in str(v) for v in surfaced))
        self.assertFalse(any("current" == str(v).lower() for v in surfaced))

    def test_freshness_is_computed_at_as_of(self):
        cases = [("2026-05-01T12:00:00Z", "WITHIN_SOURCE_WINDOW_AT_AS_OF"),
                 ("2026-05-01T19:00:00Z", "EXPIRED"),
                 ("2026-05-01T21:00:00Z", "ENDED")]
        for as_of, state in cases:
            with self.subTest(as_of=as_of):
                (item,) = parse(as_of=as_of).alerts
                self.assertEqual((item.freshness_state, item.freshness_as_of), (state, as_of))
        (future,) = parse([alert(effective="2026-05-02T00:00:00Z",
                                 expires="2026-05-02T06:00:00Z", ends=...)]).alerts
        self.assertEqual(future.freshness_state, "NOT_YET_EFFECTIVE")
        (open_ended,) = parse([alert(expires=..., ends=...)]).alerts
        self.assertEqual(open_ended.freshness_state, "UNKNOWN_NO_END_TIME")
        with self.assertRaises(nws.NwsInputError):
            parse(as_of="2026-05-01T11:00:00Z")

    def test_update_lineage_supersedes_prior_message(self):
        ref = {"@id": "x", "identifier": "urn:oid:2.49.0.1.840.0.synthetic.1",
               "sender": "s", "sent": "2026-05-01T10:00:00Z"}
        prior, update = parse([alert(1), alert(2, messageType="Update", references=[ref])]).alerts
        self.assertEqual(prior.freshness_state, "SUPERSEDED_IN_COLLECTION")
        self.assertEqual(update.freshness_state, "WITHIN_SOURCE_WINDOW_AT_AS_OF")
        self.assertEqual(update.references, ("urn:oid:2.49.0.1.840.0.synthetic.1",))
        (cancel,) = parse([alert(3, messageType="Cancel", references=[ref])]).alerts
        self.assertEqual(cancel.freshness_state, "CANCELLATION_MESSAGE")

    def test_quarantine_reasons(self):
        cases = {"STATUS_NOT_ACTUAL": alert(status="Test"),
                 "OUTSIDE_REQUESTED_AREA": alert(geocode={"UGC": ["OKZ001"]}),
                 "EXPIRES_BEFORE_SENT": alert(expires="2026-05-01T09:00:00Z"),
                 "LINEAGE_REFERENCE_MISSING": alert(messageType="Update")}
        for reason, feature in cases.items():
            with self.subTest(reason=reason):
                (item,) = parse([feature]).alerts
                self.assertEqual(item.route, "QUARANTINE_CANDIDATE")
                self.assertIn(reason, item.reasons)

    def test_collection_level_signals(self):
        paged = nws.parse_alerts(collection([alert()], pagination={"next": "https://x"}),
                                 status=200, source_url=nws.alerts_url(active=False),
                                 retrieved_at=RETRIEVED)
        self.assertEqual(paged.reasons, ("PARTIAL_COLLECTION_MORE_PAGES",
                                         "SEVEN_DAY_WINDOW_NOT_ARCHIVE"))
        not_modified = nws.parse_alerts(b"", status=304, source_url=URL, retrieved_at=RETRIEVED,
                                        headers={"ETag": '"abc"', "X-Secret": "no"})
        self.assertEqual((not_modified.outcome, not_modified.cache_headers),
                         ("NO_OP", (("ETag", '"abc"'),)))
        self.assertEqual(parse([]).alerts, ())

    def test_malformed_collections_rejected_whole(self):
        cases = {
            "ALERT_IDENTITY": [{**alert(), "id": "https://evil.example/x"}],
            "ALERT_ENUM": [alert(status="Maybe")],
            "ALERT_EVENT": [alert(event="")],
            "TIME_FORMAT": [alert(sent="yesterday")],
            "REFERENCES_SHAPE": [alert(references=[{"identifier": 5}])],
            "GEOMETRY_SHAPE": [{**alert(), "geometry": {"type": "Point"}}],
            "DUPLICATE_ALERT_ID": [alert(1), alert(1)],
        }
        for code, features in cases.items():
            with self.subTest(code=code), self.assertRaises(nws.NwsInputError) as caught:
                parse(features)
            self.assertEqual(str(caught.exception), code)
        for status, code in ((429, "RATE_LIMITED"), (503, "HTTP_STATUS")):
            with self.assertRaises(nws.NwsInputError) as caught:
                nws.parse_alerts(b"", status=status, source_url=URL, retrieved_at=RETRIEVED)
            self.assertEqual(str(caught.exception), code)
        with self.assertRaises(nws.NwsInputError):
            nws.parse_alerts(b'{"type":"Feature"}', status=200, source_url=URL,
                             retrieved_at=RETRIEVED)


class NoNetworkTests(unittest.TestCase):
    def test_module_never_opens_sockets(self):
        with patch.object(socket, "socket", side_effect=AssertionError("network")), \
                patch.object(socket, "create_connection", side_effect=AssertionError("network")):
            parse()


if __name__ == "__main__":
    unittest.main()
