import pytest

fastapi = pytest.importorskip("fastapi")
testclient = pytest.importorskip("fastapi.testclient")

from apps.governed_api.ecology.fastapi_routes import router



def test_evidence_bundle_route_is_registered() -> None:
    app = fastapi.FastAPI()
    app.include_router(router)
    client = testclient.TestClient(app)

    response = client.get("/v1/ecology/evidence-bundles/not_found")
    assert response.status_code == 200
    payload = response.json()
    assert payload["data"]["decision"] == "abstain"
