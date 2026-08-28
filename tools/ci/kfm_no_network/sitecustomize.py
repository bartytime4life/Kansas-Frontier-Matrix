"""Opt-in fail-closed network guard loaded by Python at interpreter startup.

Put this directory on ``PYTHONPATH`` and set ``KFM_NO_NETWORK=1``. The module
then denies common IPv4 and IPv6 egress paths before application imports run.
It deliberately leaves Unix-domain sockets alone so local test harnesses can
still use process-local IPC.

This is a Python-process control. It is not a host firewall, network
namespace, container policy, or runner-wide isolation proof.
"""

from __future__ import annotations

import os
import socket
import urllib.request
from typing import Any


DENIAL_MESSAGE = "KFM no-network guard denied Python network egress"
_NETWORK_FAMILIES = frozenset({socket.AF_INET, socket.AF_INET6})


class NetworkAccessDenied(RuntimeError):
    """Raised before a guarded Python network operation can leave the process."""


_original_connect = socket.socket.connect
_original_connect_ex = socket.socket.connect_ex
_original_sendto = socket.socket.sendto
_original_create_connection = socket.create_connection
_original_getaddrinfo = socket.getaddrinfo
_original_urlopen = urllib.request.urlopen


def _deny(operation: str) -> None:
    raise NetworkAccessDenied(f"{DENIAL_MESSAGE}: {operation}")


def _guarded_connect(self: socket.socket, address: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.connect")
    return _original_connect(self, address)


def _guarded_connect_ex(self: socket.socket, address: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.connect_ex")
    return _original_connect_ex(self, address)


def _guarded_sendto(self: socket.socket, *args: Any, **kwargs: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.sendto")
    return _original_sendto(self, *args, **kwargs)


def _guarded_create_connection(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.create_connection")


def _guarded_getaddrinfo(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.getaddrinfo")


def _guarded_urlopen(*_args: Any, **_kwargs: Any) -> Any:
    _deny("urllib.request.urlopen")


def activate() -> bool:
    """Install the guard only for the explicit no-network posture."""

    if os.environ.get("KFM_NO_NETWORK") != "1":
        return False

    socket.socket.connect = _guarded_connect
    socket.socket.connect_ex = _guarded_connect_ex
    socket.socket.sendto = _guarded_sendto
    socket.create_connection = _guarded_create_connection
    socket.getaddrinfo = _guarded_getaddrinfo
    urllib.request.urlopen = _guarded_urlopen
    return True


GUARD_ACTIVE = activate()
