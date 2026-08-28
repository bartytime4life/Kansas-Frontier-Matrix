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
            "socket.send",
            "import socket; socket.socket(socket.AF_INET, socket.SOCK_DGRAM).send(b'x')",
        ),
        (
            "socket.sendall",
            "import socket; socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendall(b'x')",
        ),
        (
            "socket.sendmsg",
            "import socket; "
            "assert hasattr(socket.socket, 'sendmsg'); "
            "socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendmsg("
            "[b'x'], [], 0, ('192.0.2.1', 53))",
        ),
        (
            "socket.sendfile",
            "import io, socket; "
            "assert hasattr(socket.socket, 'sendfile'); "
            "socket.socket(socket.AF_INET).sendfile(io.BytesIO(b'x'))",
        ),
        (
            "socket.gethostbyname",
            "import socket; socket.gethostbyname('example.invalid')",
        ),
        (
            "socket.gethostbyname_ex",
            "import socket; socket.gethostbyname_ex('example.invalid')",
        ),
        (
            "socket.gethostbyaddr",
            "import socket; socket.gethostbyaddr('192.0.2.1')",
        ),
        (
            "socket.getnameinfo",
            "import socket; socket.getnameinfo(('192.0.2.1', 53), 0)",
        ),
        (
            "socket.getfqdn",
            "import socket; socket.getfqdn('192.0.2.1')",
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
        "sitecustomize._original_send = lambda _socket, data: data; "
        "sitecustomize._original_sendall = lambda _socket, data: data; "
        "sitecustomize._original_sendto = lambda _socket, data, address: (data, address); "
        "sitecustomize._original_sendmsg = lambda _socket, buffers: buffers; "
        "sitecustomize._original_sendfile = lambda _socket, file: file; "
        "assert sitecustomize._guarded_connect(local_socket, 'local.sock') == 'local.sock'; "
        "assert sitecustomize._guarded_send(local_socket, b'x') == b'x'; "
        "assert sitecustomize._guarded_sendall(local_socket, b'x') == b'x'; "
        "assert sitecustomize._guarded_sendto(local_socket, b'x', 'local.sock') == "
        "(b'x', 'local.sock'); "
        "assert sitecustomize._guarded_sendmsg(local_socket, [b'x']) == [b'x']; "
        "marker = object(); "
        "assert sitecustomize._guarded_sendfile(local_socket, marker) is marker"
    )
    assert result.returncode == 0, result.stderr
