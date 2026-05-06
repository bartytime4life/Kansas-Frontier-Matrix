"""Compatibility shim for tests importing apps.governed_api.server."""

from apps.api.server import app

__all__ = ["app"]
