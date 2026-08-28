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
_original_send = socket.socket.send
_original_sendall = socket.socket.sendall
_original_sendto = socket.socket.sendto
_original_sendmsg = getattr(socket.socket, "sendmsg", None)
_original_sendfile = getattr(socket.socket, "sendfile", None)
_original_create_connection = socket.create_connection
_original_getaddrinfo = socket.getaddrinfo
_original_gethostbyname = socket.gethostbyname
_original_gethostbyname_ex = socket.gethostbyname_ex
_original_gethostbyaddr = socket.gethostbyaddr
_original_getnameinfo = socket.getnameinfo
_original_getfqdn = socket.getfqdn
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


def _guarded_send(self: socket.socket, *args: Any, **kwargs: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.send")
    return _original_send(self, *args, **kwargs)


def _guarded_sendall(self: socket.socket, *args: Any, **kwargs: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.sendall")
    return _original_sendall(self, *args, **kwargs)


def _guarded_sendto(self: socket.socket, *args: Any, **kwargs: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.sendto")
    return _original_sendto(self, *args, **kwargs)


def _guarded_sendmsg(self: socket.socket, *args: Any, **kwargs: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.sendmsg")
    if _original_sendmsg is None:
        raise AttributeError("socket.sendmsg is unavailable on this platform")
    return _original_sendmsg(self, *args, **kwargs)


def _guarded_sendfile(self: socket.socket, *args: Any, **kwargs: Any) -> Any:
    if self.family in _NETWORK_FAMILIES:
        _deny("socket.sendfile")
    if _original_sendfile is None:
        raise AttributeError("socket.sendfile is unavailable on this platform")
    return _original_sendfile(self, *args, **kwargs)


def _guarded_create_connection(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.create_connection")


def _guarded_getaddrinfo(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.getaddrinfo")


def _guarded_gethostbyname(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.gethostbyname")


def _guarded_gethostbyname_ex(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.gethostbyname_ex")


def _guarded_gethostbyaddr(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.gethostbyaddr")


def _guarded_getnameinfo(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.getnameinfo")


def _guarded_getfqdn(*_args: Any, **_kwargs: Any) -> Any:
    _deny("socket.getfqdn")


def _guarded_urlopen(*_args: Any, **_kwargs: Any) -> Any:
    _deny("urllib.request.urlopen")


def activate() -> bool:
    """Install the guard only for the explicit no-network posture."""

    if os.environ.get("KFM_NO_NETWORK") != "1":
        return False

    socket.socket.connect = _guarded_connect
    socket.socket.connect_ex = _guarded_connect_ex
    socket.socket.send = _guarded_send
    socket.socket.sendall = _guarded_sendall
    socket.socket.sendto = _guarded_sendto
    if _original_sendmsg is not None:
        socket.socket.sendmsg = _guarded_sendmsg
    if _original_sendfile is not None:
        socket.socket.sendfile = _guarded_sendfile
    # ``socket.SocketType`` is the native ``_socket.socket`` class rather than
    # the patchable ``socket.socket`` subclass. Rebind the public constructor
    # alias after patching so it cannot bypass the guarded methods.
    socket.SocketType = socket.socket
    socket.create_connection = _guarded_create_connection
    socket.getaddrinfo = _guarded_getaddrinfo
    socket.gethostbyname = _guarded_gethostbyname
    socket.gethostbyname_ex = _guarded_gethostbyname_ex
    socket.gethostbyaddr = _guarded_gethostbyaddr
    socket.getnameinfo = _guarded_getnameinfo
    socket.getfqdn = _guarded_getfqdn
    urllib.request.urlopen = _guarded_urlopen
    return True


GUARD_ACTIVE = activate()
