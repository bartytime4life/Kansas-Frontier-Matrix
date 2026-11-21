"""Atmosphere pipelines and their test corpus run without live network access.

Planned intent (docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md): Pipeline dryrun must not perform live HTTP.

Two checks. First, no module under pipelines/domains/atmosphere/ imports a
network library, so the GHCN-Daily and NOAA Normals stages can only read the
bytes they are handed. Second, every other test module in this directory, which
drives those stages over synthetic fixtures, runs in a child interpreter. A
sitecustomize guard on that child's path, which its own subprocesses inherit,
refuses DNS lookups and non-local socket connections and logs each attempt. The
suite must pass and the log must stay empty, so a test that quietly catches a
refused connection still fails this check.
"""
from __future__ import annotations

import ast
import os
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
PIPELINES = REPO_ROOT / "pipelines/domains/atmosphere"
NETWORK_MODULES = {"socket", "ssl", "http", "urllib", "requests", "httpx", "aiohttp", "urllib3", "ftplib", "smtplib"}
LOG_VARIABLE = "KFM_NETWORK_ATTEMPT_LOG"

GUARD = textwrap.dedent(
    '''
    import os, socket

    _LOG = os.environ["KFM_NETWORK_ATTEMPT_LOG"]
    _LOCAL = {"localhost", "127.0.0.1", "::1"}

    def _refuse(kind, target):
        with open(_LOG, "a", encoding="utf-8") as log:
            log.write(f"{os.getpid()} {kind} {target!r}\\n")
        raise OSError(f"network blocked in Atmosphere tests: {kind} {target!r}")

    def _is_local(address):
        return isinstance(address, tuple) and address and str(address[0]) in _LOCAL

    _connect = socket.socket.connect
    _connect_ex = socket.socket.connect_ex
    _getaddrinfo = socket.getaddrinfo

    def connect(self, address):
        if self.family in (socket.AF_INET, socket.AF_INET6) and not _is_local(address):
            _refuse("connect", address)
        return _connect(self, address)

    def connect_ex(self, address):
        if self.family in (socket.AF_INET, socket.AF_INET6) and not _is_local(address):
            _refuse("connect_ex", address)
        return _connect_ex(self, address)

    def getaddrinfo(host, *args, **kwargs):
        if host is not None and str(host) not in _LOCAL:
            _refuse("getaddrinfo", host)
        return _getaddrinfo(host, *args, **kwargs)

    socket.socket.connect = connect
    socket.socket.connect_ex = connect_ex
    socket.getaddrinfo = getaddrinfo
    '''
)


def network_imports(root: Path) -> list[str]:
    """Return "path: module" for every network-library import under root."""
    found = []
    for path in sorted(root.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names = [node.module]
            else:
                continue
            for name in names:
                if name.split(".")[0] in NETWORK_MODULES:
                    found.append(f"{path.relative_to(root).as_posix()}: {name}")
    return found


def corpus_modules() -> list[str]:
    """Return the dotted names of every Atmosphere test module except this one."""
    return [
        f"tests.domains.atmosphere.{path.stem}"
        for path in sorted(HERE.glob("test_*.py"))
        if path.name != Path(__file__).name
    ]


def run_guarded(arguments: list[str], scratch: Path) -> tuple[subprocess.CompletedProcess[str], str]:
    guard_dir = scratch / "guard"
    guard_dir.mkdir()
    (guard_dir / "sitecustomize.py").write_text(GUARD, encoding="utf-8")
    log = scratch / "network-attempts.log"
    log.touch()
    environment = dict(os.environ)
    environment[LOG_VARIABLE] = str(log)
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(None, [str(guard_dir), str(REPO_ROOT), environment.get("PYTHONPATH", "")])
    )
    completed = subprocess.run(
        [sys.executable, *arguments],
        cwd=REPO_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
        timeout=600,
    )
    return completed, log.read_text(encoding="utf-8")


class AtmosphereNoLiveNetworkTests(unittest.TestCase):
    def test_pipelines_import_no_network_library(self) -> None:
        self.assertTrue(list(PIPELINES.glob("*.py")), "no Atmosphere pipeline modules found")
        self.assertEqual(network_imports(PIPELINES), [],
                         "Atmosphere pipeline stages must not import network libraries")

    def test_import_scan_detects_a_network_import(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            module = Path(scratch) / "stage.py"
            module.write_text("from urllib.request import urlopen\nimport json\n", encoding="utf-8")
            self.assertEqual(network_imports(Path(scratch)), ["stage.py: urllib.request"])

    def test_corpus_covers_the_domain_tests(self) -> None:
        modules = corpus_modules()
        self.assertIn("tests.domains.atmosphere.test_atmosphere_smoke", modules)
        self.assertIn("tests.domains.atmosphere.test_ghcnd_daily_candidate", modules)
        self.assertNotIn(f"tests.domains.atmosphere.{Path(__file__).stem}", modules)

    def test_atmosphere_corpus_passes_without_network(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            completed, attempts = run_guarded(["-m", "unittest", *corpus_modules()], Path(scratch))
        self.assertEqual(completed.returncode, 0, completed.stderr[-4000:])
        self.assertEqual(attempts, "", f"Atmosphere tests attempted network access:\n{attempts}")

    def test_guard_refuses_and_logs_a_lookup(self) -> None:
        probe = "import socket\ntry:\n    socket.getaddrinfo('example.org', 443)\nexcept OSError:\n    pass\n"
        with tempfile.TemporaryDirectory() as scratch:
            completed, attempts = run_guarded(["-c", probe], Path(scratch))
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("getaddrinfo 'example.org'", attempts)


if __name__ == "__main__":
    unittest.main()
