from __future__ import annotations

import base64
import hashlib
import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.pmtiles.validate_headless_render_review_packet import (
    EXPECTED_HOLDS,
    METRICS_PROFILE,
    SIDECAR_PROFILE,
    main,
    validate_directory,
)

PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


def _sha256(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


class HeadlessRenderReviewPacketTests(unittest.TestCase):
    def _write_packet(self, directory: Path) -> None:
        metrics = {
            "profile": METRICS_PROFILE,
            "status": "PROPOSED_INACTIVE",
            "execution_mode": "SYNTHETIC_FIXTURE_ONLY",
            "outcome": "PASS",
            "code": "HEADLESS_RENDER_REVIEW_PACKET_PASS",
            "source_kind": "SYNTHETIC_FIXTURE",
            "viewport": {
                "width": 390,
                "height": 844,
                "device_scale_factor": 3,
                "has_touch": True,
                "is_mobile": True,
            },
            "browser": {"engine": "chromium", "headless": True},
            "archive": {
                "name": "mobile-base.pmtiles",
                "archive_bytes": 347,
                "tile_bytes": 70,
            },
            "render": {
                "decoded": True,
                "rendered": True,
                "width": 1,
                "height": 1,
                "pixel_rgba": [17, 34, 51, 255],
            },
            "timing": {"verify_ms": 1.25, "decode_render_ms": 2.5},
            "external_request_count": 0,
            "maplibre_boot_state": "HOLD",
            "style_health": "NOT_EVALUATED",
            "publication_state": "NOT_EVALUATED",
            "authority": "NONE",
            "holds": list(EXPECTED_HOLDS),
        }
        metrics_bytes = (json.dumps(metrics, indent=2) + "\n").encode("utf-8")
        sidecar = {
            "profile": SIDECAR_PROFILE,
            "status": "PROPOSED_INACTIVE",
            "execution_mode": "SYNTHETIC_FIXTURE_ONLY",
            "source_kind": "SYNTHETIC_FIXTURE",
            "artifacts": [
                {
                    "name": "headless-render.png",
                    "role": "SCREENSHOT",
                    "media_type": "image/png",
                    "sha256": _sha256(PNG_1X1),
                },
                {
                    "name": "metrics.json",
                    "role": "METRICS",
                    "media_type": "application/json",
                    "sha256": _sha256(metrics_bytes),
                },
            ],
            "maplibre_boot_state": "HOLD",
            "style_health": "NOT_EVALUATED",
            "publication_state": "NOT_EVALUATED",
            "authority": "NONE",
            "holds": list(EXPECTED_HOLDS),
            "review_only": True,
        }
        (directory / "headless-render.png").write_bytes(PNG_1X1)
        (directory / "metrics.json").write_bytes(metrics_bytes)
        (directory / "sidecar.json").write_text(
            json.dumps(sidecar, indent=2) + "\n", encoding="utf-8"
        )

    def test_valid_packet_and_cli(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._write_packet(directory)
            self.assertEqual(validate_directory(directory), [])
            self.assertEqual(main([str(directory)]), 0)

    def test_digest_tampering_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._write_packet(directory)
            with (directory / "metrics.json").open("ab") as stream:
                stream.write(b" ")
            self.assertIn(
                "HEADLESS_RENDER_REVIEW_ARTIFACT_DIGEST_MISMATCH",
                [finding.code for finding in validate_directory(directory)],
            )

    def test_authority_overclaim_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._write_packet(directory)
            metrics_path = directory / "metrics.json"
            metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
            metrics["authority"] = "RELEASE"
            metrics_path.write_text(json.dumps(metrics), encoding="utf-8")
            self.assertIn(
                "HEADLESS_RENDER_REVIEW_AUTHORITY_OVERCLAIM",
                [finding.code for finding in validate_directory(directory)],
            )

    def test_duplicate_keys_and_symlinks_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._write_packet(directory)
            (directory / "metrics.json").write_text(
                '{"profile":"a","profile":"b"}', encoding="utf-8"
            )
            self.assertIn(
                "HEADLESS_RENDER_REVIEW_DUPLICATE_KEY",
                [finding.code for finding in validate_directory(directory)],
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._write_packet(directory)
            screenshot = directory / "headless-render.png"
            screenshot.unlink()
            screenshot.symlink_to(directory / "metrics.json")
            self.assertIn(
                "HEADLESS_RENDER_REVIEW_SYMLINK_DENIED",
                [finding.code for finding in validate_directory(directory)],
            )

    def test_validation_is_no_network(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            self._write_packet(directory)
            with (
                mock.patch.object(socket, "socket", side_effect=deny),
                mock.patch.object(socket, "create_connection", side_effect=deny),
                mock.patch.object(socket, "getaddrinfo", side_effect=deny),
            ):
                self.assertEqual(validate_directory(directory), [])


if __name__ == "__main__":
    unittest.main()
