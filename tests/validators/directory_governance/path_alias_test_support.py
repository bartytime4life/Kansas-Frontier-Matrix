"""Shared helpers for focused Path Alias Register tests."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tools.validators.directory_governance.validate_path_alias_register import validate_register
from tools.validators.directory_governance.path_alias_model import FIXTURE_ROOT


class PathAliasTestSupport:
    def valid_fixture(self) -> dict:
        return json.loads(
            (FIXTURE_ROOT / "valid" / "compatibility_classes.yaml").read_text(encoding="utf-8")
        )

    def validate_payload(self, payload: dict):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
            return validate_register(path, check_repository=False, enforce_projection_binding=False)
