from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.evaluators.fixture_runner import EvaluatorError, run_fixture_evaluation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a deterministic evaluator fixture and emit a report."
    )
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--fixture", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--config-schema",
        type=Path,
        default=Path("tools/evaluators/config.schema.json"),
    )
    parser.add_argument(
        "--fixture-schema",
        type=Path,
        default=Path("tools/evaluators/fixtures/fixture.schema.json"),
    )
    parser.add_argument(
        "--report-schema",
        type=Path,
        default=Path("tools/evaluators/report.schema.json"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        evaluation = run_fixture_evaluation(
            config_path=args.config,
            fixture_path=args.fixture,
            report_schema_path=args.report_schema,
            config_schema_path=args.config_schema,
            fixture_schema_path=args.fixture_schema,
        )
    except EvaluatorError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(evaluation.report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote evaluator report: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
