from pathlib import Path

from pipelines.habitat_layer_build.validate.validate_layer_candidate import validate_file


def test_good_fixture_validates() -> None:
    fixture = Path("pipelines/habitat_layer_build/fixtures/good/habitat_layer_candidate.valid.json")
    assert validate_file(fixture) == []


def test_bad_fixture_fails() -> None:
    fixture = Path("pipelines/habitat_layer_build/fixtures/bad/missing_source_role.invalid.json")
    errors = validate_file(fixture)
    assert any("source_role" in error for error in errors)
