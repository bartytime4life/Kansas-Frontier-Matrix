from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PolicyInput:
    request_id: str
    actor_id: str | None
    release_state: str | None
    evidence_renderable: bool
    payload: dict[str, Any]


def build_policy_input(
    *,
    request_id: str,
    payload: dict[str, Any],
    actor_id: str | None = None,
    release_state: str | None = None,
    evidence_renderable: bool = True,
) -> PolicyInput:
    """Build a stable, explicit policy input envelope for runtime adapters."""
    return PolicyInput(
        request_id=request_id,
        actor_id=actor_id,
        release_state=release_state,
        evidence_renderable=evidence_renderable,
        payload=payload,
    )
