"""Synthetic, offline checks for the candidate ReleaseManifest comparator."""

from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
import json
import tempfile
import unittest
from pathlib import Path

from tools.diff.release_diff import compare_paths, main


def _write(path: Path, artifacts: list[dict], **fields: object) -> Path:
    path.write_text(
        json.dumps(
            {"object_type": "ReleaseManifest", "artifacts": artifacts, **fields}
        ),
        encoding="utf-8",
    )
    return path


class ReleaseDiffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_artifact_membership_and_content_changes_are_sorted(self) -> None:
        left = _write(
            self.root / "left.json",
            [
                {"artifact_ref": "ref:zulu", "digest": "old"},
                {"artifact_ref": "ref:bravo", "digest": "old"},
                {"artifact_ref": "ref:shared", "digest": "old"},
            ],
            release_id="release:candidate",
        )
        right = _write(
            self.root / "right.json",
            [
                {"digest": "new", "artifact_ref": "ref:shared"},
                {"artifact_ref": "ref:alpha", "digest": "new"},
                {"artifact_ref": "ref:yankee", "digest": "new"},
            ],
            release_id="release:candidate",
        )
        report, status = compare_paths(left, right, fail_on_change=True)
        self.assertEqual(status, 1)
        self.assertEqual((report["status"], report["blocking"]), ("changed", True))
        self.assertEqual(
            report["summary"], {"added": [], "removed": [], "changed": ["artifacts"]}
        )
        self.assertEqual(report["artifacts"], {
            "added": ["ref:alpha", "ref:yankee"],
            "removed": ["ref:bravo", "ref:zulu"],
            "changed": ["ref:shared"],
        })
        self.assertNotIn('"old"', json.dumps(report))
        self.assertNotIn('"new"', json.dumps(report))

    def test_same_content_ignores_object_key_order(self) -> None:
        left = _write(
            self.root / "left.json", [{"artifact_ref": "ref:one", "digest": "one"}]
        )
        right = _write(
            self.root / "right.json", [{"digest": "one", "artifact_ref": "ref:one"}]
        )
        report, status = compare_paths(left, right, fail_on_change=True)
        self.assertEqual((status, report["status"]), (0, "same"))
        self.assertEqual(
            report["artifacts"], {"added": [], "removed": [], "changed": []}
        )

    def test_ambiguous_or_untyped_manifest_fails_closed(self) -> None:
        left = _write(
            self.root / "left.json",
            [{"artifact_ref": "ref:one"}, {"artifact_ref": "ref:one"}],
        )
        right = _write(self.root / "right.json", [{"artifact_ref": "ref:one"}])
        report, status = compare_paths(left, right)
        self.assertEqual(
            (status, report["error"]["code"]), (2, "LEFT_ARTIFACT_REF_DUPLICATE")
        )
        left.write_text('{"id":"legacy-placeholder"}', encoding="utf-8")
        report, status = compare_paths(left, right)
        self.assertEqual(
            (status, report["error"]["code"]), (2, "LEFT_NOT_RELEASE_MANIFEST")
        )

    def test_invalid_json_and_nonfinite_numbers_are_rejected(self) -> None:
        left = self.root / "left.json"
        right = _write(self.root / "right.json", [{"artifact_ref": "ref:one"}])
        left.write_text('{"object_type":"ReleaseManifest",', encoding="utf-8")
        report, status = compare_paths(left, right)
        self.assertEqual((status, report["error"]["code"]), (2, "LEFT_JSON_INVALID"))
        left.write_text(
            '{"object_type":"ReleaseManifest","artifacts":['
            '{"artifact_ref":"ref:one","digest":NaN}]}',
            encoding="utf-8",
        )
        report, status = compare_paths(left, right)
        self.assertEqual(
            (status, report["error"]["code"]), (2, "LEFT_JSON_NONFINITE_NUMBER")
        )

    def test_deep_input_fails_with_finite_error(self) -> None:
        left = self.root / "left.json"
        right = _write(self.root / "right.json", [{"artifact_ref": "ref:one"}])
        left.write_text(
            '{"object_type":"ReleaseManifest","artifacts":['
            '{"artifact_ref":"ref:one","payload":' + "[" * 10_000
            + "0" + "]" * 10_000 + "}]}",
            encoding="utf-8",
        )
        report, status = compare_paths(left, right)
        self.assertEqual((status, report["error"]["code"]), (2, "LEFT_NESTING_LIMIT"))

    def test_cli_report_is_deterministic_and_never_modifies_inputs(self) -> None:
        left = _write(
            self.root / "left.json", [{"artifact_ref": "ref:one", "digest": "old"}]
        )
        right = _write(
            self.root / "right.json", [{"artifact_ref": "ref:one", "digest": "new"}]
        )
        before = (left.read_bytes(), right.read_bytes())
        output = self.root / "report.json"
        args = [
            "--left", str(left), "--right", str(right),
            "--output", str(output), "--fail-on-change",
        ]
        self.assertEqual(main(args), 1)
        first = output.read_bytes()
        self.assertEqual(main(args), 1)
        self.assertEqual(output.read_bytes(), first)
        self.assertTrue(first.endswith(b"\n"))
        self.assertEqual((left.read_bytes(), right.read_bytes()), before)

    def test_output_cannot_overwrite_an_input_or_follow_a_symlink(self) -> None:
        left = _write(self.root / "left.json", [{"artifact_ref": "ref:one"}])
        right = _write(self.root / "right.json", [{"artifact_ref": "ref:one"}])
        original = left.read_bytes()
        with redirect_stdout(StringIO()):
            self.assertEqual(main([
                "--left", str(left), "--right", str(right), "--output", str(left)
            ]), 2)
        self.assertEqual(left.read_bytes(), original)
        link = self.root / "report.json"
        link.symlink_to(left)
        with redirect_stdout(StringIO()):
            self.assertEqual(main([
                "--left", str(left), "--right", str(right), "--output", str(link)
            ]), 2)
        self.assertEqual(left.read_bytes(), original)
