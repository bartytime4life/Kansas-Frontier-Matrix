#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path

def replay(bundle: dict, policy_input: dict) -> str:
    for rule in bundle.get("rules", []):
        cond = rule.get("if")
        if cond:
            if "review_complete" in cond and policy_input.get("review_complete") != cond["review_complete"]:
                continue
            if "risk_score_max" in cond and policy_input.get("risk_score", 10**9) > cond["risk_score_max"]:
                continue
            return rule.get("then", "deny")
        if "else" in rule:
            return rule["else"]
    return "deny"

def main() -> int:
    if len(sys.argv) != 3:
        print("usage: replay_decision_log.py <policy_bundle.json> <policy_input.json>")
        return 2
    bundle = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    policy_input = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    print(json.dumps({"result": replay(bundle, policy_input)}, sort_keys=True, separators=(",", ":")))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
