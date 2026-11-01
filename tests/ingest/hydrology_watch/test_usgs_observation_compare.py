"""Offline comparison and refusal behavior; all records here are synthetic."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import urlencode

from tools.ingest.hydrology_watch import usgs_observation_compare as m


def page(collection="continuous", times=None):
    times = times or (["2026-10-30", "2026-10-31"] if collection == "daily" else
                      ["2026-10-30T12:00:00Z", "2026-10-30T13:00:00Z"])
    interval = "2026-10-30/2026-10-31" if collection == "daily" else "2026-10-30T12:00:00Z/2026-10-30T13:00:00Z"
    query = dict(f="json", monitoring_location_id=m.STATION, parameter_code="00060", limit="10000", datetime=interval)
    url = f"https://api.waterdata.usgs.gov/ogcapi/v1/collections/{collection}/items?{urlencode(query)}"
    rows = [dict(type="Feature", geometry=None, properties=dict(
        time_series_id="fixture-series", monitoring_location_id=m.STATION,
        parameter_code="00060", statistic_id="00003" if collection == "daily" else "00011",
        time=t, value="10", unit_of_measure="ft^3/s", approval_status="Provisional",
        qualifier=None, last_modified="2026-10-31T00:00:00Z")) for t in times]
    return dict(type="FeatureCollection", features=rows, numberReturned=len(rows),
                links=[dict(rel="self", href=url)], timeStamp="2026-10-31T12:00:00Z")


def encoded(value):
    return json.dumps(value, allow_nan=False).encode()


def retained(value, collection="continuous"):
    body = encoded(value)
    url = value["links"][0]["href"]
    receipt = dict(query=url, error=None, feature_count=len(value["features"]), pages=[dict(
        url=url, status=200, sha256=hashlib.sha256(body).hexdigest(), bytes=len(body),
        numberReturned=len(value["features"]))])
    return dict(station=m.STATION, parameter="00060", evidence_files={
        f"{collection}-0.raw": body.decode(), f"{collection}-receipt.json": json.dumps(receipt)})


class ComparisonTests(unittest.TestCase):
    def compare(self, prior=None, current=None, collection="continuous"):
        prior = prior or page(collection)
        current = copy.deepcopy(prior) if current is None else current
        return m.compare_bytes(encoded(prior), encoded(current), collection)

    def change(self, field, value):
        before = page()
        after = copy.deepcopy(before)
        after["features"][0]["properties"][field] = value
        return self.compare(before, after)

    def test_unchanged_is_captured_field_answer_without_authority(self):
        result = self.compare()
        self.assertEqual(result["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")
        self.assertEqual(result["outcome"], "ANSWER")
        self.assertFalse(any(result["authority"].values()))
        self.assertEqual(result, self.compare())

    def test_value_unit_approval_qualifier_and_method_changes_are_distinct(self):
        for field, value in [("value", "11"), ("unit_of_measure", "m^3/s"),
                             ("approval_status", "Approved"), ("qualifier", ["ESTIMATED"]),
                             ("method_category", "Reported")]:
            with self.subTest(field=field):
                result = self.change(field, value)
                self.assertEqual(result["decision"], "REVIEW")
                self.assertEqual(result["changed_field_counts"], {field: 1})

    def test_numeric_spelling_and_source_order_do_not_create_revision(self):
        before = page()
        after = copy.deepcopy(before)
        after["features"].reverse()
        after["features"][0]["properties"]["value"] = 10.0
        result = self.compare(before, after)
        self.assertEqual(result["changed_field_counts"], {})
        self.assertEqual(result["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")
        self.assertNotEqual(result["prior"]["sha256"], result["current"]["sha256"])

    def test_tiny_numeric_revision_is_not_rounded_away(self):
        result = self.change("value", "10.0000000000000000000000000000000000000001")
        self.assertEqual(result["changed_field_counts"], {"value": 1})

    def test_provider_refresh_only_is_reported_without_measurement_alert(self):
        result = self.change("last_modified", "2026-11-01T00:00:00Z")
        self.assertEqual(result["provider_metadata_changed_records"], 1)
        self.assertEqual(result["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")

    def test_null_is_not_zero_and_unknown_approval_is_not_approved(self):
        result = self.change("value", None)
        self.assertEqual(result["current"]["null_values"], 1)
        result = self.change("approval_status", None)
        self.assertEqual(result["current"]["approval_status_counts"], {"Provisional": 1, "UNKNOWN": 1})
        self.assertEqual(result["changed_field_counts"], {"approval_status": 1})

    def test_missing_required_quality_field_refuses_comparison(self):
        before = page()
        after = copy.deepcopy(before)
        del after["features"][0]["properties"]["qualifier"]
        self.assertEqual(self.compare(before, after)["reason_code"], "PROPERTY_MISSING")

    def test_added_property_is_a_schema_review_signal(self):
        result = self.change("new_quality_field", "unrecognized")
        self.assertTrue(result["property_keys_changed"])
        self.assertEqual(result["decision"], "REVIEW")

    def test_series_change_is_inventory_change_not_a_value_revision(self):
        result = self.change("time_series_id", "different-series")
        self.assertEqual(result["changed_field_counts"], {"record_added": 1, "record_removed": 1})

    def test_missing_record_differs_from_null(self):
        before = page()
        after = copy.deepcopy(before)
        after["features"].pop()
        after["numberReturned"] = 1
        result = self.compare(before, after)
        self.assertEqual(result["changed_field_counts"], {"record_removed": 1})
        self.assertEqual(result["current"]["null_values"], 0)

    def test_duplicate_identity_is_never_silently_deduplicated(self):
        before = page()
        before["features"].append(copy.deepcopy(before["features"][0]))
        before["numberReturned"] += 1
        self.assertEqual(self.compare(before)["reason_code"], "DUPLICATE_IDENTITY")

    def test_rolling_window_and_added_filter_are_incomparable(self):
        for replacement in ["2026-10-31T13", "2026-10-30T14"]:
            before = page()
            after = copy.deepcopy(before)
            after["links"][0]["href"] = after["links"][0]["href"].replace("2026-10-30T13", replacement)
            result = self.compare(before, after)
            self.assertEqual(result["outcome"], "ABSTAIN")
            self.assertEqual(result["reason_code"], "QUERY_SCOPE_MISMATCH")
        before = page()
        after = copy.deepcopy(before)
        after["links"][0]["href"] += "&statistic_id=00011"
        self.assertEqual(self.compare(before, after)["reason_code"], "QUERY_SCOPE_MISMATCH")

    def test_query_order_does_not_matter(self):
        before = page()
        after = copy.deepcopy(before)
        base, args = after["links"][0]["href"].split("?")
        after["links"][0]["href"] = base + "?" + "&".join(reversed(args.split("&")))
        self.assertEqual(self.compare(before, after)["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")

    def test_paging_or_matched_count_or_cap_abstains(self):
        for change, reason in [
            (lambda p: p["links"].append(dict(rel="next", href="https://example.invalid")), "PAGINATION_INCOMPLETE"),
            (lambda p: p.update(numberMatched=3), "MATCHED_COUNT_INCOMPLETE"),
            (lambda p: p["links"][0].update(href=p["links"][0]["href"].replace("limit=10000", "limit=2")), "PAGE_CAP_REACHED")]:
            before = page()
            change(before)
            result = self.compare(before)
            self.assertEqual((result["outcome"], result["reason_code"]), ("ABSTAIN", reason))

    def test_wrong_identity_outside_window_and_unsupported_statistic(self):
        for field, value, reason in [("monitoring_location_id", "USGS-06892518", "OBSERVATION_SCOPE_INVALID"),
                                     ("parameter_code", "00065", "OBSERVATION_SCOPE_INVALID"),
                                     ("time", "2026-10-29T12:00:00Z", "OBSERVATION_OUTSIDE_INTERVAL"),
                                     ("statistic_id", "00003", "STATISTIC_UNSUPPORTED"),
                                     ("approval_status", "Other", "APPROVAL_UNSUPPORTED")]:
            with self.subTest(field=field):
                self.assertEqual(self.change(field, value)["reason_code"], reason)

    def test_unsafe_host_secret_query_and_duplicate_query_are_rejected(self):
        for edit in [lambda u: u.replace("api.waterdata.usgs.gov", "example.invalid"),
                     lambda u: u + "&api_key=DO_NOT_ECHO", lambda u: u + "&parameter_code=00060",
                     lambda u: "https://[malformed"]:
            before = page()
            before["links"][0]["href"] = edit(before["links"][0]["href"])
            result = self.compare(before)
            self.assertEqual(result["outcome"], "ERROR")
            self.assertNotIn("DO_NOT_ECHO", json.dumps(result))

    def test_invalid_values_are_rejected(self):
        for value in [True, "", "NaN", "Infinity", "1e100000", {"v": 1}]:
            with self.subTest(value=value):
                self.assertEqual(self.change("value", value)["reason_code"], "VALUE_INVALID")

    def test_json_duplicate_keys_nonfinite_and_malformed_are_errors(self):
        for raw in [b'{"type":1,"type":2}', b'{"value":NaN}', b'<html>redirect</html>', b'\xff']:
            self.assertEqual(m.compare_bytes(raw, encoded(page()), "continuous")["outcome"], "ERROR")

    def test_empty_is_not_a_no_change_answer(self):
        before = page()
        before.update(features=[], numberReturned=0)
        result = self.compare(before)
        self.assertEqual((result["outcome"], result["reason_code"]), ("ABSTAIN", "NO_OBSERVATIONS"))

    def test_daily_coverage_includes_query_edges(self):
        before = page("daily")
        after = copy.deepcopy(before)
        after["features"].pop(0)
        after["numberReturned"] = 1
        result = self.compare(before, after, "daily")
        self.assertEqual(result["current"]["captured_coverage"]["count"], 1)
        self.assertEqual(result["current"]["captured_coverage"]["details"][0][-1], "2026-10-30")

    def test_continuous_six_hour_boundary_holes_are_explicit(self):
        before = page()
        before["links"][0]["href"] = before["links"][0]["href"].replace("2026-10-30T12", "2026-10-30T00").replace("2026-10-30T13", "2026-10-31T00")
        result = self.compare(before)
        self.assertEqual(result["prior"]["captured_coverage"]["count"], 2)
        self.assertEqual(result["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")

    def test_timezone_spelling_is_normalized_but_unknown_offset_refused(self):
        result = self.change("time", "2026-10-30T07:00:00-05:00")
        self.assertEqual(result["changed_field_counts"], {})
        self.assertEqual(self.change("time", "2026-10-30T12:00:00-00:00")["reason_code"], "TIME_OFFSET_UNKNOWN")

    def test_retained_page_checks_hash_http_query_and_counts(self):
        before = retained(page())
        result = self.compare(before, page())
        self.assertEqual(result["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")
        self.assertEqual(result["prior"]["capture_binding"], "retained_receipt_bound")
        for field, value, reason in [("sha256", "0"*64, "CAPTURE_DIGEST_MISMATCH"),
                                     ("status", 302, "CAPTURE_HTTP_STATUS"),
                                     ("numberReturned", 3, "CAPTURE_COUNT_MISMATCH")]:
            wrapper = copy.deepcopy(before)
            receipt = json.loads(wrapper["evidence_files"]["continuous-receipt.json"])
            receipt["pages"][0][field] = value
            wrapper["evidence_files"]["continuous-receipt.json"] = json.dumps(receipt)
            self.assertEqual(self.compare(wrapper)["reason_code"], reason)

    def test_retained_edited_summary_has_no_authority_over_payload(self):
        before = retained(page())
        before["summary"] = {"continuous": {"count": 99999}}
        self.assertEqual(self.compare(before, page())["prior"]["records"], 2)

    def test_oversized_input_and_series_budgets(self):
        self.assertEqual(m.compare_bytes(b' '*(m.MAX_BYTES+1), b'{}', "daily")["reason_code"], "INPUT_TOO_LARGE")
        before = page()
        before["features"] = [copy.deepcopy(before["features"][0]) for _ in range(5)]
        for i, feature in enumerate(before["features"]):
            feature["properties"]["time_series_id"] = f"series-{i}"
        before["numberReturned"] = 5
        self.assertEqual(self.compare(before)["reason_code"], "SERIES_BUDGET_EXCEEDED")

    def test_detail_budget_retains_full_change_counts(self):
        before = page("daily", [f"2026-10-{i:02}" for i in range(1, 32)])
        before["links"][0]["href"] = before["links"][0]["href"].replace("2026-10-30%2F", "2026-10-01%2F")
        after = copy.deepcopy(before)
        for row in after["features"]:
            row["properties"]["value"] = "11"
        with patch.object(m, "DETAIL_LIMIT", 3):
            result = self.compare(before, after, "daily")
        self.assertEqual(len(result["changes"]), 3)
        self.assertEqual(result["changed_field_counts"], {"value": 31})
        self.assertTrue(result["details_truncated"])

    def test_no_network_and_no_input_mutation(self):
        before = encoded(page())
        with patch("socket.socket", side_effect=AssertionError("network prohibited")):
            self.assertEqual(m.compare_bytes(before, before, "continuous")["outcome"], "ANSWER")
        self.assertEqual(before, encoded(page()))

    def test_report_mutation_cannot_change_later_authority_flags(self):
        result = self.compare()
        result["authority"]["release"] = True
        self.assertFalse(any(self.compare()["authority"].values()))

    def test_retained_receipt_query_mismatch_and_multiple_pages_abstain(self):
        wrapper = retained(page())
        receipt = json.loads(wrapper["evidence_files"]["continuous-receipt.json"])
        receipt["query"] += "&statistic_id=00011"
        wrapper["evidence_files"]["continuous-receipt.json"] = json.dumps(receipt)
        self.assertEqual(self.compare(wrapper)["reason_code"], "CAPTURE_QUERY_MISMATCH")
        receipt["pages"].append(copy.deepcopy(receipt["pages"][0]))
        wrapper["evidence_files"]["continuous-receipt.json"] = json.dumps(receipt)
        self.assertEqual(self.compare(wrapper)["reason_code"], "CAPTURE_MULTIPAGE_UNSUPPORTED")

    def test_provider_response_order_cannot_be_reversed_silently(self):
        before = page()
        after = copy.deepcopy(before)
        after["timeStamp"] = "2026-10-30T12:00:00Z"
        result = self.compare(before, after)
        self.assertEqual(result["reason_code"], "PROVIDER_RESPONSE_ORDER_REVERSED")
        self.assertEqual(result["outcome"], "ABSTAIN")

    def test_property_key_budget_bounds_report_size(self):
        before = page()
        before["features"][0]["properties"]["x"*129] = "ignored"
        self.assertEqual(self.compare(before)["reason_code"], "PROPERTY_KEYS_BUDGET")

    def test_cli_query_and_comparison_preserve_files(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"prior.json"
            path.write_bytes(encoded(retained(page())))
            original = path.read_bytes()
            command = [sys.executable, str(Path(m.__file__).resolve()), str(path), "--collection", "continuous"]
            query_result = subprocess.run([*command, "--print-query"], capture_output=True, text=True, check=True)
            self.assertEqual(query_result.stdout.strip(), page()["links"][0]["href"])
            result = subprocess.run([*command, str(path)], capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout)["decision"], "NO_DIFFERENCE_IN_CAPTURED_FIELDS")
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual([p.name for p in Path(folder).iterdir()], ["prior.json"])

    def test_nonregular_and_static_symlink_inputs_are_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            directory = Path(folder)
            with self.assertRaises(m.Problem):
                m.read_regular(directory)
            target = directory/"data.json"
            target.write_bytes(encoded(page()))
            link = directory/"link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable on this host")
            with self.assertRaisesRegex(m.Problem, "INPUT_SYMLINK"):
                m.read_regular(link)


if __name__ == "__main__":
    unittest.main()
