"""No-network byte-integrity regressions for both local artifact-reader helpers.

Run: python -m unittest discover -s tests/validators \
    -p 'test_artifact_reader_short_reads.py' -v

Short reads are simulated by limiting real os.read calls on temporary regular
files. No schema or validator finding is mocked. These tests prove the helper
boundary, not source admission, immutable snapshots, or public release.
"""

from __future__ import annotations

import hashlib
import json
import os
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators import _source_artifact
from tools.validators.evidence import _kfm_geo_manifest


class _ReaderChecks:
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / "input.bin"
        self.real_read = os.read
        self.real_close = os.close

    def short_reads(self, size: int = 2):
        return mock.patch.object(
            self.helper.os,
            "read",
            side_effect=lambda fd, count: self.real_read(fd, min(size, count)),
        )

    def assert_finding(self, result, code: str) -> None:
        value, findings = result
        self.assertIsNone(value)
        self.assertEqual([finding.code for finding in findings], [code])
        self.assertEqual([finding.field for finding in findings], ["/"])

    def test_complete_payload_and_digest_survive_short_reads(self) -> None:
        payload = bytes(range(256)) * 3
        self.path.write_bytes(payload)
        with self.short_reads(7):
            value, findings = self.helper.read_regular_bytes(self.path, len(payload))
        self.assertEqual(findings, [])
        self.assertIsInstance(value, bytes)
        self.assertEqual(value, payload)
        self.assertEqual(hashlib.sha256(value).digest(), hashlib.sha256(payload).digest())

    def test_valid_json_with_split_utf8_is_not_truncated(self) -> None:
        expected = {"label": "Kansas \u2014 synthetic", "items": [1, 2, 3]}
        self.path.write_text(json.dumps(expected, ensure_ascii=False), encoding="utf-8")
        with self.short_reads(1):
            value, findings = self.helper.read_json_object(self.path)
        self.assertEqual((value, findings), (expected, []))

    def test_valid_prefix_cannot_hide_invalid_json_suffix(self) -> None:
        self.path.write_bytes(b"{} invalid trailing bytes")
        with self.short_reads():
            result = self.helper.read_json_object(self.path)
        self.assert_finding(result, "INVALID_JSON")

    def test_valid_prefix_cannot_hide_invalid_utf8_suffix(self) -> None:
        self.path.write_bytes(b"{}\xff")
        with self.short_reads():
            result = self.helper.read_json_object(self.path)
        self.assert_finding(result, "READ_ERROR")

    def test_duplicate_members_still_fail_after_short_reads(self) -> None:
        self.path.write_bytes(b'{"value":1,"value":2}')
        with self.short_reads():
            result = self.helper.read_json_object(self.path)
        self.assert_finding(result, "DUPLICATE_KEY")

    def test_nonfinite_numbers_still_fail_after_short_reads(self) -> None:
        self.path.write_bytes(b'{"value":NaN}')
        with self.short_reads():
            result = self.helper.read_json_object(self.path)
        self.assert_finding(result, "NONFINITE_NUMBER")

    def test_depth_budget_still_applies_after_short_reads(self) -> None:
        self.path.write_text('{"nested":' + "[" * 65 + "0" + "]" * 65 + "}")
        with self.short_reads():
            result = self.helper.read_json_object(self.path)
        self.assert_finding(result, "JSON_COMPLEXITY_LIMIT")

    def test_partial_read_error_discards_prefix_and_closes_descriptor(self) -> None:
        self.path.write_bytes(b"{} trailing bytes")
        descriptors = []

        def fail_after_prefix(fd, count):
            descriptors.append(fd)
            if len(descriptors) == 1:
                return self.real_read(fd, min(count, 2))
            raise OSError("synthetic-private-diagnostic")

        with (
            mock.patch.object(self.helper.os, "read", side_effect=fail_after_prefix),
            mock.patch.object(self.helper.os, "close", wraps=self.real_close) as close,
        ):
            result = self.helper.read_json_object(self.path)
        self.assert_finding(result, "READ_ERROR")
        self.assertNotIn("synthetic-private-diagnostic", repr(result))
        close.assert_called_once_with(descriptors[0])
        with self.assertRaises(OSError):
            os.fstat(descriptors[0])

    def test_growth_after_stat_exhausts_only_remaining_budget(self) -> None:
        self.path.write_bytes(b"{}")
        requests, returned = [], []

        def grow_then_read(fd, count):
            requests.append(count)
            if len(requests) == 1:
                with self.path.open("ab") as writer:
                    writer.write(b"more bytes")
            chunk = self.real_read(fd, min(count, 2))
            returned.append(len(chunk))
            return chunk

        with (
            mock.patch.object(self.helper.os, "read", side_effect=grow_then_read),
            mock.patch.object(self.helper.os, "close", wraps=self.real_close) as close,
        ):
            result = self.helper.read_regular_bytes(self.path, 4)
        self.assert_finding(result, "FILE_TOO_LARGE")
        self.assertEqual(requests, [5, 3, 1])
        self.assertEqual(sum(returned), 5)
        close.assert_called_once()

    def test_exact_limit_requires_eof_and_remains_valid(self) -> None:
        self.path.write_bytes(b"1234")
        with self.short_reads() as read:
            value, findings = self.helper.read_regular_bytes(self.path, 4)
        self.assertEqual((value, findings), (b"1234", []))
        self.assertEqual([call.args[1] for call in read.call_args_list], [5, 3, 1])

    def test_empty_file_and_zero_budget_remain_valid(self) -> None:
        self.path.write_bytes(b"")
        with self.short_reads() as read:
            result = self.helper.read_regular_bytes(self.path, 0)
        self.assertEqual(result, (b"", []))
        self.assertEqual(read.call_args.args[1], 1)

    def test_nonempty_file_exceeds_zero_budget_without_open(self) -> None:
        self.path.write_bytes(b"x")
        with mock.patch.object(self.helper.os, "open") as opened:
            result = self.helper.read_regular_bytes(self.path, 0)
        self.assert_finding(result, "FILE_TOO_LARGE")
        opened.assert_not_called()

    def test_declared_oversize_fails_before_open(self) -> None:
        self.path.write_bytes(b"12345")
        with mock.patch.object(self.helper.os, "open") as opened:
            result = self.helper.read_regular_bytes(self.path, 4)
        self.assert_finding(result, "FILE_TOO_LARGE")
        opened.assert_not_called()

    def test_missing_file_preserves_safe_read_error(self) -> None:
        self.assert_finding(self.helper.read_regular_bytes(self.path, 16), "READ_ERROR")

    def test_directory_is_rejected_before_open(self) -> None:
        self.path.mkdir()
        with mock.patch.object(self.helper.os, "open") as opened:
            result = self.helper.read_regular_bytes(self.path, 16)
        self.assert_finding(result, "UNSAFE_FILE")
        opened.assert_not_called()

    def test_symlink_is_rejected_before_open(self) -> None:
        target = self.path.with_suffix(".target")
        target.write_bytes(b"{}")
        self.path.symlink_to(target)
        with mock.patch.object(self.helper.os, "open") as opened:
            result = self.helper.read_regular_bytes(self.path, 16)
        self.assert_finding(result, "UNSAFE_FILE")
        opened.assert_not_called()

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO support unavailable")
    def test_fifo_is_rejected_before_open(self) -> None:
        os.mkfifo(self.path)
        with mock.patch.object(self.helper.os, "open") as opened:
            result = self.helper.read_regular_bytes(self.path, 16)
        self.assert_finding(result, "UNSAFE_FILE")
        opened.assert_not_called()

    def test_large_read_requests_are_chunk_bounded(self) -> None:
        payload = b"x" * (128 * 1024 + 1)
        self.path.write_bytes(payload)
        with mock.patch.object(self.helper.os, "read", wraps=self.real_read) as read:
            result = self.helper.read_regular_bytes(self.path, len(payload))
        self.assertEqual(result, (payload, []))
        self.assertTrue(all(0 < call.args[1] <= 64 * 1024 for call in read.call_args_list))

    def test_success_closes_descriptor_and_preserves_open_flags(self) -> None:
        self.path.write_bytes(b"synthetic bytes")
        with (
            mock.patch.object(self.helper.os, "open", wraps=os.open) as opened,
            mock.patch.object(self.helper.os, "close", wraps=self.real_close) as close,
            self.short_reads(),
        ):
            result = self.helper.read_regular_bytes(self.path, 32)
        self.assertEqual(result, (b"synthetic bytes", []))
        flags = opened.call_args.args[1]
        for flag in ("O_NOFOLLOW", "O_NONBLOCK"):
            expected = getattr(os, flag, 0)
            self.assertEqual(flags & expected, expected)
        close.assert_called_once()
        with self.assertRaises(OSError):
            os.fstat(close.call_args.args[0])

    def test_reader_does_not_use_network(self) -> None:
        self.path.write_bytes(b"{}")
        with (
            mock.patch.object(socket.socket, "connect", side_effect=AssertionError("network")),
            mock.patch.object(socket, "create_connection", side_effect=AssertionError("network")),
            self.short_reads(),
        ):
            result = self.helper.read_json_object(self.path)
        self.assertEqual(result, ({}, []))


class SourceArtifactReaderTests(_ReaderChecks, unittest.TestCase):
    helper = _source_artifact


class GeoManifestReaderTests(_ReaderChecks, unittest.TestCase):
    helper = _kfm_geo_manifest


if __name__ == "__main__":
    unittest.main()
