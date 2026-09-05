"""Only this test directory gets a no-network guard."""
import socket
import urllib.request
import pytest


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("NETWORK_FORBIDDEN_IN_ORDINARY_TESTS")
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(urllib.request.OpenerDirector, "open", denied)
