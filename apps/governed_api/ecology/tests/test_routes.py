from apps.governed_api.ecology import routes


def test_default_schema_path_points_to_existing_schema() -> None:
    assert routes.DEFAULT_SCHEMA_PATH.exists()


def test_abstain_when_proof_pack_missing() -> None:
    result = routes.get_ecology_evidence_bundle(candidate_id="missing_candidate")
    assert result["status"] == "ok"
    assert result["data"]["decision"] == "abstain"
    assert result["data"]["error_code"] == "ECO_EB_PROOF_PACK_MISSING"
