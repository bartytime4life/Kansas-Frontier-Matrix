"""Negative proof for the Hydrology Python-process no-egress guard.

The tests start fresh Python interpreters with the CI ``sitecustomize`` path so
they verify startup-time enforcement rather than relying on a test-local mock.
They do not establish a host firewall, network namespace, container policy,
non-Python isolation, or runner-wide egress denial.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[3]
GUARD_ROOT = REPO_ROOT / "tools/ci/kfm_no_network"
DENIAL_MESSAGE = "KFM no-network guard denied Python network egress"


def _guarded_python(source: str, *, enabled: bool = True) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["KFM_NO_NETWORK"] = "1" if enabled else "0"
    python_path = [str(GUARD_ROOT), str(REPO_ROOT)]
    if env.get("PYTHONPATH"):
        python_path.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(python_path)
    return subprocess.run(
        [sys.executable, "-c", source],
        cwd=REPO_ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )


def test_guard_requires_explicit_no_network_posture() -> None:
    result = _guarded_python(
        "import sitecustomize; assert not sitecustomize.GUARD_ACTIVE",
        enabled=False,
    )
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    ("operation", "source"),
    (
        (
            "socket.connect",
            "import socket; socket.socket().connect(('192.0.2.1', 443))",
        ),
        (
            "socket.connect",
            "import socket; "
            "socket.socket(socket.AF_INET6).connect(('2001:db8::1', 443, 0, 0))",
        ),
        (
            "socket.connect_ex",
            "import socket; socket.socket().connect_ex(('192.0.2.1', 443))",
        ),
        (
            "socket.create_connection",
            "import socket; socket.create_connection(('example.invalid', 443))",
        ),
        (
            "socket.getaddrinfo",
            "import socket; socket.getaddrinfo('example.invalid', 443)",
        ),
        (
            "socket.sendto",
            "import socket; "
            "socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto("
            "b'x', ('192.0.2.1', 53))",
        ),
        (
            "urllib.request.urlopen",
            "import urllib.request; urllib.request.urlopen('https://example.invalid')",
        ),
    ),
)
def test_guard_denies_common_python_egress_paths(operation: str, source: str) -> None:
    result = _guarded_python(source)
    assert result.returncode != 0
    assert DENIAL_MESSAGE in result.stderr
    assert operation in result.stderr


def test_guard_preserves_unix_domain_socket_routing() -> None:
    result = _guarded_python(
        "import socket; import sitecustomize; "
        "local_socket = type('LocalSocket', (), {'family': socket.AF_UNIX})(); "
        "sitecustomize._original_connect = lambda _socket, address: address; "
        "assert sitecustomize._guarded_connect(local_socket, 'local.sock') == 'local.sock'"
    )
    assert result.returncode == 0, result.stderr
