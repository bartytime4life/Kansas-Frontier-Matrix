from __future__ import annotations

from pathlib import Path

ALLOWED_STATUSES = {"missing", "present"}


def parse_required_entries(registry_path: Path) -> list[dict[str, str]]:
    in_required_block = False
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for raw in registry_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("required_doctrine_artifacts:"):
            in_required_block = True
            continue
        if not in_required_block:
            continue
        if line and not line.startswith("-") and not line.startswith("doc_id:") and not line.startswith("status:"):
            # End of required block when another top-level key appears.
            if not raw.startswith(" "):
                break
        if line.startswith("- filename:"):
            if current:
                entries.append(current)
            current = {"filename": line.split(":", 1)[1].strip()}
        elif line.startswith("status:") and current is not None:
            current["status"] = line.split(":", 1)[1].strip()
        elif line.startswith("doc_id:") and current is not None:
            current["doc_id"] = line.split(":", 1)[1].strip()

    if current:
        entries.append(current)

    if not in_required_block:
        raise ValueError("missing required_doctrine_artifacts block")

    seen: set[str] = set()
    for entry in entries:
        name = entry["filename"]
        if name in seen:
            raise ValueError(f"duplicate filename in registry: {name}")
        seen.add(name)

        status = entry.get("status", "missing")
        if status not in ALLOWED_STATUSES:
            raise ValueError(f"invalid status for {name}: {status}")
        entry["status"] = status

        doc_id = entry.get("doc_id", "")
        if not doc_id:
            raise ValueError(f"missing doc_id for {name}")

    return entries
