"""Small, fail-closed developer CLI for KFM repository checks."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


CLI_INSTALL_HINT = 'python -m pip install -e "./packages/kfm-cli"'
OPTIONAL_CLI_MODULES = {
    "annotated_doc",
    "hydra",
    "markdown_it",
    "omegaconf",
    "rich",
    "shellingham",
    "typer",
}
TELEMETRY_PROFILES = {
    "trace_receipt_link", "openlineage_run_event_projection",
    "remote_sensing_lineage_activity", "map_build_sustainability",
}
TELEMETRY_OUTCOMES = {"PASS", "ABSTAIN", "DENY", "ERROR"}
DIFF_STATUSES = {"same", "changed", "error"}


def build_app() -> Any:
    """Build the Typer application after CLI dependencies are available."""

    import typer
    from hydra import compose, initialize_config_dir
    from omegaconf import OmegaConf
    from rich.console import Console
    from rich.table import Table

    app = typer.Typer(
        help="KFM developer command-line utilities.",
        no_args_is_help=True,
    )

    @app.callback()
    def root() -> None:
        """KFM developer command-line utilities."""

    @app.command()
    def doctor(
        config_dir: Path | None = typer.Option(
            None,
            "--config-dir",
            exists=True,
            file_okay=False,
            dir_okay=True,
            resolve_path=True,
            help="Hydra config directory; defaults to KFM's packaged config.",
        ),
    ) -> None:
        """Check whether the KFM developer configuration is usable."""

        selected_dir = config_dir or Path(__file__).resolve().parent / "conf"
        with initialize_config_dir(
            version_base=None,
            config_dir=str(selected_dir.resolve()),
        ):
            cfg = compose(config_name="config")

        checks = (
            ("app.name", OmegaConf.select(cfg, "app.name")),
            ("paths.data_dir", OmegaConf.select(cfg, "paths.data_dir")),
            ("ci.strict", OmegaConf.select(cfg, "ci.strict")),
        )

        table = Table(title="KFM Configuration Doctor")
        table.add_column("Check")
        table.add_column("Status")
        table.add_column("Value")

        failed = False
        for key, value in checks:
            passed = value is not None
            failed = failed or not passed
            table.add_row(
                key,
                "PASS" if passed else "FAIL",
                str(value) if passed else "missing",
            )

        Console().print(table)
        if failed:
            raise typer.Exit(code=1)

    @app.command()
    def diff(
        left: Path = typer.Option(..., "--left", help="Local JSON object before the change."),
        right: Path = typer.Option(..., "--right", help="Local JSON object after the change."),
        fail_on_change: bool = typer.Option(False, "--fail-on-change"),
    ) -> None:
        """Compare two local JSON objects without assigning policy authority."""

        repo = Path(__file__).resolve().parents[4]
        comparator = repo / "tools/diff/stable_diff.py"
        if not comparator.is_file():
            print(json.dumps({"tool": "stable-diff", "status": "error", "blocking": True,
                              "error": {"code": "COMPARATOR_UNAVAILABLE"}}, sort_keys=True))
            raise typer.Exit(code=2)
        command = [sys.executable, str(comparator), "--left", str(left.absolute()),
                   "--right", str(right.absolute())]
        if fail_on_change:
            command.append("--fail-on-change")
        try:
            result = subprocess.run(command, cwd=repo, capture_output=True,
                                    text=True, check=False, timeout=60)
            report = json.loads(result.stdout)
            if (not isinstance(report, dict)
                or set(report) != ({"tool", "status", "blocking", "left", "right", "summary"}
                    | ({"error"} if report.get("status") == "error" else set()))
                or report.get("tool") != "stable-diff"
                or report.get("status") not in DIFF_STATUSES
                or not isinstance(report.get("blocking"), bool)
                or not isinstance(report.get("summary"), dict)
                or set(report["summary"]) != {"added", "removed", "changed"}
                or any(not isinstance(report["summary"][key], list)
                       or any(not isinstance(item, str) for item in report["summary"][key])
                       for key in ("added", "removed", "changed"))
                or (report["status"] == "same" and any(report["summary"].values()))
                or (report["status"] == "changed" and not any(report["summary"].values()))
                or (report["status"] == "error" and
                    (any(report["summary"].values()) or not isinstance(report.get("error"), dict)
                     or set(report["error"]) != {"code", "message"}
                     or not all(isinstance(value, str) for value in report["error"].values())))
                or report.get("left") != str(left.absolute())
                or report.get("right") != str(right.absolute())
                or result.returncode not in (0, 1, 2)
                or (report["status"] == "error") != (result.returncode == 2)
                or (result.returncode == 1) != (report["status"] == "changed" and fail_on_change)
                or report["blocking"] != (report["status"] == "error" or
                    (report["status"] == "changed" and fail_on_change))):
                raise ValueError("invalid comparator report")
        except (OSError, subprocess.TimeoutExpired, ValueError):
            report = {"tool": "stable-diff", "status": "error", "blocking": True,
                      "error": {"code": "COMPARATOR_ERROR"}}
            result_code = 2
        else:
            result_code = result.returncode
        # The upstream report includes local input paths by contract; unlike
        # telemetry this is an explicitly operator-local comparison surface.
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        raise typer.Exit(code=result_code)

    @app.command()
    def telemetry(
        fixtures: bool = typer.Option(False, "--fixtures", help="Replay bounded local fixtures."),
        candidate: Path | None = typer.Option(None, "--candidate", help="Local candidate JSON file."),
        profile: str | None = typer.Option(None, "--profile", help="Explicit reviewed telemetry profile."),
    ) -> None:
        """Run the repository's bounded telemetry validator without enabling telemetry."""

        if fixtures == (candidate is not None) or (candidate is not None and profile is None):
            raise typer.BadParameter("select --fixtures or --candidate with --profile")
        repo = Path(__file__).resolve().parents[4]
        validator = repo / "tools/validators/validate_telemetry_safety.py"
        if not validator.is_file():
            Console(stderr=True).print("Telemetry validator unavailable in this checkout.")
            raise typer.Exit(code=1)
        command = [sys.executable, str(validator)]
        if fixtures:
            command.append("--fixtures")
        else:
            assert candidate is not None
            command.extend(("--candidate", str(candidate.absolute())))
        if profile is not None:
            command.extend(("--profile", profile))
        try:
            result = subprocess.run(
                command, cwd=repo, capture_output=True, text=True,
                check=False, timeout=300,
            )
            report = json.loads(result.stdout)
            if (
                not isinstance(report, dict)
                or set(report) != {"authority", "execution_mode", "outcome", "profiles", "scope"}
                or not isinstance(report.get("outcome"), str)
                or report["outcome"] not in TELEMETRY_OUTCOMES
                or report.get("authority") != "NONE"
                or report.get("execution_mode") != "FIXTURE_ONLY_NO_NETWORK"
                or report.get("scope") != "bounded_telemetry_profile_validation_only"
                or not isinstance(report.get("profiles"), dict)
                or not report["profiles"]
                or set(report["profiles"]) != ({profile} if profile else TELEMETRY_PROFILES)
                or any(
                    not isinstance(value, str) or value not in TELEMETRY_OUTCOMES
                    for value in report["profiles"].values()
                )
                or report["outcome"] != next(
                    (value for value in ("ERROR", "DENY", "ABSTAIN")
                     if value in report["profiles"].values()), "PASS"
                )
                or result.returncode not in (0, 1)
                or (report["outcome"] in {"PASS", "ABSTAIN"}) != (result.returncode == 0)
            ):
                raise ValueError("invalid bounded validator report")
        except (OSError, subprocess.TimeoutExpired, ValueError):
            report = {"authority": "NONE", "outcome": "ERROR", "scope": "bounded_telemetry_profile_validation_only"}
            result_code = 1
        else:
            result_code = result.returncode
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        raise typer.Exit(code=result_code)

    return app


def main() -> None:
    """Run the CLI with a useful error when dependencies are absent."""

    try:
        app = build_app()
    except ModuleNotFoundError as exc:
        if exc.name in OPTIONAL_CLI_MODULES:
            print(
                "KFM CLI dependencies are not installed. "
                f"Install them with: {CLI_INSTALL_HINT}",
                file=sys.stderr,
            )
            raise SystemExit(2) from exc
        raise
    app()
