#!/usr/bin/env python3
"""Offline fake of conftest for deterministic fixture tests."""
from __future__ import annotations
import json
import sys
from pathlib import Path

if len(sys.argv) < 3 or sys.argv[1] != "test":
    raise SystemExit(2)
packet = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
allowed = (
    packet.get("policy_context", {}).get("evaluation") == "PASS"
    and packet.get("policy_context", {}).get("profile") == "public-safe"
)
print(json.dumps([] if allowed else [{"msg": "policy denied"}], sort_keys=True, separators=(",", ":")))
raise SystemExit(0 if allowed else 1)
