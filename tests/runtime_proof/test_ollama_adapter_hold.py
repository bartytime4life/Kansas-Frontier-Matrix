"""Proof that the held OllamaAdapter seam fails closed without any I/O.

The live Ollama binding is deferred by the proposed ADR-0008 and ADR-0019 and
the governed-AI integration architecture. This suite proves only the hold:
importing the module touches nothing, constructing the adapter raises a named
reason code, and the module imports no network, process, or environment
surface. It does not prove a provider binding, policy enforcement, or receipts.
"""
from __future__ import annotations

import ast
import importlib
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
ADAPTER_PATH = REPOSITORY_ROOT / "runtime/model_adapters/OllamaAdapter.py"
MODULE_NAME = "runtime.model_adapters.OllamaAdapter"


def _forbidden(*args: object, **kwargs: object) -> None:
    raise AssertionError("held adapter attempted a side effect")


class OllamaAdapterHoldTest(unittest.TestCase):
    def _fresh_import(self):
        sys.modules.pop(MODULE_NAME, None)
        with mock.patch.object(socket, "socket", _forbidden), \
                mock.patch.object(socket, "create_connection", _forbidden), \
                mock.patch.object(subprocess, "Popen", _forbidden):
            return importlib.import_module(MODULE_NAME)

    def test_import_is_inert(self) -> None:
        module = self._fresh_import()
        self.assertEqual(module.HOLD_REASON_CODE, "OLLAMA_ADAPTER_NOT_ADMITTED")

    def test_construction_raises_named_hold_for_any_arguments(self) -> None:
        module = self._fresh_import()
        calls = ((), ("http://127.0.0.1:11434",), ("model", {"temperature": 0}))
        for args in calls:
            with self.subTest(args=args), \
                    mock.patch.object(socket, "socket", _forbidden), \
                    mock.patch.object(socket, "create_connection", _forbidden), \
                    mock.patch.object(subprocess, "Popen", _forbidden):
                with self.assertRaises(module.OllamaAdapterHold) as caught:
                    module.OllamaAdapter(*args, host="http://127.0.0.1:11434")
                self.assertEqual(caught.exception.reason_code, module.HOLD_REASON_CODE)
                self.assertTrue(str(caught.exception).startswith(module.HOLD_REASON_CODE + ":"))
                self.assertNotIn("11434", str(caught.exception))

    def test_hold_is_not_a_finite_outcome_substitute(self) -> None:
        module = self._fresh_import()
        public = {name for name in vars(module) if not name.startswith("_")}
        self.assertEqual(
            public - {"annotations"},
            {"HOLD_REASON_CODE", "OllamaAdapter", "OllamaAdapterHold"},
        )
        self.assertFalse(hasattr(module.OllamaAdapter, "respond"))

    def test_module_imports_no_io_surface(self) -> None:
        tree = ast.parse(ADAPTER_PATH.read_text(encoding="utf-8"))
        imported: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module.split(".")[0])
        self.assertEqual(imported, {"__future__"})


if __name__ == "__main__":
    unittest.main()
