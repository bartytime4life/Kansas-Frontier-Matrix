"""Regression coverage for the connectors_core supported import surface."""
from __future__ import annotations

import importlib


def test_supported_modules_import_without_runtime_setup() -> None:
    for module_name in (
        "connectors_core.core",
        "connectors_core.transport",
        "connectors_core.artifact_handoff",
        "connectors_core.retrieval_episode",
        "connectors_core.descriptor_gate",
    ):
        module = importlib.import_module(module_name)
        assert module.__name__ == module_name
