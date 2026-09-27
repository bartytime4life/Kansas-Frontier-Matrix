"""Route one classified USGS earthquake retrieval to a candidate lane; never writes.

The gate is deliberately conservative. A response that was not captured is held;
captured bytes that the parser rejects are a quarantine candidate; parsed bytes are a
raw candidate. Whatever the provisional lane, the final route is HOLD while the
connector descriptor leaves ``role`` or ``rights`` unresolved: rights and source role
are steward decisions, not something this module may infer. Nothing here grants
admission, establishes coverage, or persists material.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import earthquake
from .fetch import Retrieval

DESCRIPTOR = Path(__file__).resolve().with_name("descriptor.yaml")
RAW = "RAW_CANDIDATE"
QUARANTINE = "QUARANTINE_CANDIDATE"
HOLD = "HOLD"
DESCRIPTOR_KEYS = frozenset({"name", "role", "rights", "sensitivity_floor"})
UNRESOLVED = frozenset({"", "TBD", "UNKNOWN", "NEEDS_VERIFICATION"})
MAX_DESCRIPTOR_BYTES = 16 * 1024


def load_descriptor(path: Path = DESCRIPTOR) -> dict[str, str]:
    """Read the flat connector descriptor; any structure beyond ``key: value`` is refused."""
    try:
        data = path.read_bytes()
    except OSError:
        return {}
    if len(data) > MAX_DESCRIPTOR_BYTES:
        return {}
    result: dict[str, str] = {}
    try:
        lines = data.decode("utf-8").splitlines()
    except UnicodeError:
        return {}
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        key, sep, value = text.partition(":")
        key, value = key.strip(), value.strip()
        if not sep or key not in DESCRIPTOR_KEYS or key in result or line[:1].isspace():
            return {}
        result[key] = value
    return result


def descriptor_blockers(descriptor: dict[str, str]) -> tuple[str, ...]:
    if descriptor.get("name") != "usgs":
        return ("DESCRIPTOR_INVALID",)
    return tuple(f"DESCRIPTOR_{key.upper()}_UNRESOLVED" for key in ("role", "rights")
                 if descriptor.get(key, "").upper() in UNRESOLVED)


@dataclass(frozen=True)
class AdmissionDecision:
    route: str
    provisional_route: str
    reasons: tuple[str, ...]
    episode_id: str
    source_url: str
    snapshot: earthquake.SnapshotCandidate | None
    # Routing is not admission, a coverage claim, or a write to data/raw or data/quarantine.
    admission: str = "NOT_ADMITTED"
    coverage: str = "NOT_ESTABLISHED"
    write_performed: bool = False


def admit(retrieval: Retrieval, *, descriptor: dict[str, str] | None = None) -> AdmissionDecision:
    """Decide a candidate lane for one classified retrieval."""
    if not isinstance(retrieval, Retrieval):
        raise TypeError("retrieval must be a fetch.Retrieval")
    episode = retrieval.episode
    snapshot = None
    if not retrieval.captured or retrieval.body is None:
        provisional, reasons = HOLD, tuple(episode["result"]["reason_codes"])
    else:
        try:
            snapshot = earthquake.parse_snapshot(
                retrieval.body, status=episode["transport"]["http_status"],
                source_url=retrieval.source_url, retrieved_at=episode["completed_at"])
        except earthquake.EarthquakeInputError as error:
            provisional, reasons = QUARANTINE, (f"PARSE_{error.args[0]}",)
        else:
            provisional = RAW
            reasons = ("QUERY_LIMIT_REACHED",) if snapshot.query_limit_reached else ()
    blockers = descriptor_blockers(load_descriptor() if descriptor is None else descriptor)
    route = HOLD if blockers else provisional
    return AdmissionDecision(route, provisional, reasons + blockers, episode["episode_id"],
                             retrieval.source_url, snapshot)
