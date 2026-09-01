"""Small, fail-closed developer CLI for KFM repository checks."""

from __future__ import annotations

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
