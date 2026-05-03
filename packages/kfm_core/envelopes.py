from dataclasses import dataclass, asdict
from typing import Any

FINITE_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


@dataclass(frozen=True)
class RuntimeEnvelope:
    outcome: str
    payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        if self.outcome not in FINITE_OUTCOMES:
            raise ValueError(f"Invalid outcome: {self.outcome}")
        return asdict(self)


def runtime_envelope(outcome: str, payload: dict[str, Any]) -> dict[str, Any]:
    return RuntimeEnvelope(outcome=outcome, payload=payload).to_dict()
