"""Checkout-local operator CLI for bounded, read-only commands."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from kfm_cli.commands import diff


def main(argv: Sequence[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "diff":
        return diff.main(argv[1:])
    parser = argparse.ArgumentParser(prog="kfm", description=__doc__)
    parser.add_argument("command", choices=("diff",), help="Read-only JSON comparison")
    parser.parse_args(argv)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
