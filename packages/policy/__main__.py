from __future__ import annotations

import argparse
import json
from pathlib import Path

from .decision_engine import StaticDecisionEngine
from .inputs import build_policy_input


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m packages.policy",
        description="Evaluate a policy-support decision using the packages/policy adapter.",
    )
    parser.add_argument("--input", required=True, help="Path to runtime policy input JSON.")
    parser.add_argument("--decision", required=True, help="Proposed decision (ANSWER/ABSTAIN/DENY/ERROR).")
    parser.add_argument("--out", default=None, help="Optional output path for normalized result JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    input_doc = json.loads(Path(args.input).read_text(encoding="utf-8"))

    policy_input = build_policy_input(
        request_id=str(input_doc.get("request_id", "<unknown>")),
        actor_id=input_doc.get("actor_id"),
        release_state=input_doc.get("release_state"),
        evidence_renderable=bool(input_doc.get("evidence_renderable", True)),
        payload=input_doc,
    )

    engine = StaticDecisionEngine(decision=args.decision)
    result = engine.evaluate(policy_input)
    output = {
        "decision": result.decision,
        "reasons": list(result.reasons),
        "obligations": list(result.obligations),
    }

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
