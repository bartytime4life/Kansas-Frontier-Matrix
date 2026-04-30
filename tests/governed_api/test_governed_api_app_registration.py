from __future__ import annotations

from apps.governed_api.server import app


def test_governed_api_routes_registered() -> None:
    routes = {route.path for route in app.routes}

    assert "/healthz" in routes
    assert "/ecology/timeslices/{id}" in routes
    assert "/ecology/evidence/{bundle_id:path}" in routes
    assert "/ecology/catalog/stac" in routes
