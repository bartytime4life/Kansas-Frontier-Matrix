"""Fresh-process proof for the Geology Python no-network startup guard.

The shared guard covers its named public Python APIs and the direct private
``_socket.socket`` constructor alias. These tests do not claim a host firewall,
dependency-install isolation, non-Python egress denial, or coverage of every
other private extension factory or API.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
GUARD_ROOT = REPO_ROOT / "tools/ci/kfm_no_network"
DENIAL_MESSAGE = "KFM no-network guard denied Python network egress"


def _guarded_python(
    source: str, *, enabled: bool = True
) -> subprocess.CompletedProcess[str]:
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
        "import socket, sitecustomize; "
        "assert not sitecustomize.GUARD_ACTIVE; "
        "assert socket.SocketType is sitecustomize._original_socket_type",
        enabled=False,
    )
    assert result.returncode == 0, result.stderr


def test_guard_starts_and_denies_public_socket_type_alias() -> None:
    result = _guarded_python(
        "import socket, sitecustomize; "
        "assert sitecustomize.GUARD_ACTIVE; "
        "assert socket.SocketType is socket.socket; "
        "socket.SocketType(socket.AF_INET, socket.SOCK_DGRAM).sendmsg("
        "[b'x'], [], 0, ('192.0.2.1', 53))"
    )
    assert result.returncode != 0
    assert DENIAL_MESSAGE in result.stderr
    assert "socket.sendmsg" in result.stderr


def test_guard_denies_private_extension_socket_constructor() -> None:
    result = _guarded_python(
        "import _socket, socket, sitecustomize; "
        "assert _socket.socket is socket.socket; "
        "assert socket.socket is not sitecustomize._original_socket_type; "
        "_socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendmsg("
        "[b'x'], [], 0, ('192.0.2.1', 53))"
    )
    assert result.returncode != 0
    assert DENIAL_MESSAGE in result.stderr
    assert "socket.sendmsg" in result.stderr


def test_guard_preserves_unix_routing() -> None:
    result = _guarded_python(
        "import socket, sitecustomize; "
        "local_socket = type('LocalSocket', (), {'family': socket.AF_UNIX})(); "
        "sitecustomize._original_connect = lambda _socket, address: address; "
        "assert sitecustomize._guarded_connect(local_socket, 'local.sock') "
        "== 'local.sock'"
    )
    assert result.returncode == 0, result.stderr
