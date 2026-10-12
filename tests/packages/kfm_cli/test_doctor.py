from __future__ import annotations

from typer.testing import CliRunner

from kfm_cli.cli import build_app


runner = CliRunner()


def test_doctor_passes_with_packaged_config() -> None:
    result = runner.invoke(build_app(), ["doctor"])

    assert result.exit_code == 0, result.output
    assert "app.name" in result.stdout
    assert "paths.data_dir" in result.stdout
    assert "ci.strict" in result.stdout
    assert "PASS" in result.stdout


def test_doctor_fails_when_required_key_is_missing(tmp_path) -> None:
    config_dir = tmp_path / "conf"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(
        "app:\n  name: test-app\npaths:\n  data_dir: data\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        build_app(),
        ["doctor", "--config-dir", str(config_dir)],
    )

    assert result.exit_code == 1
    assert "ci.strict" in result.stdout
    assert "FAIL" in result.stdout


def test_doctor_accepts_false_boolean_value(tmp_path) -> None:
    config_dir = tmp_path / "conf"
    config_dir.mkdir()
    (config_dir / "config.yaml").write_text(
        "app:\n  name: test-app\npaths:\n  data_dir: data\nci:\n  strict: false\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        build_app(),
        ["doctor", "--config-dir", str(config_dir)],
    )

    assert result.exit_code == 0, result.output
    assert "False" in result.stdout
