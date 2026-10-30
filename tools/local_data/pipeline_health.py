"""Read a bounded private operator report. No capture, database access or publication."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from tools.local_data.file_io import read_regular

STATES = {"checked", "held", "degraded", "qualified", "unavailable", "unverified", "verified", "verified-copy", "overdue",
          "not-started", "complete", "running", "pending", "needs-independent-full-size-backup"}
CODES = re.compile(r"[A-Z][A-Z_]{1,63}\Z")


def _time(value):
    if not isinstance(value, str) or len(value) > 40 or not value.endswith("Z"):
        return None
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return value
    except ValueError:
        return None


def _record(value):
    if not isinstance(value, dict):
        return {"state": "unavailable"}
    result = {"state": value.get("state") if value.get("state") in STATES else "unavailable"}
    for key in ("finishedAt", "lastAttemptAt", "lastFinishedAt", "lastSuccessfulCaptureAt", "nextEligibleAt", "retryAt", "receiptTime", "receiptFileModifiedAt"):
        if key in value:
            result[key] = _time(value[key])
    for key in ("attempts", "files", "freeBytes", "totalBytes"):
        if isinstance(value.get(key), int) and not isinstance(value[key], bool) and 0 <= value[key] <= 2**53:
            result[key] = value[key]
    for key in ("exhausted", "matchesLatestBackup"):
        if isinstance(value.get(key), bool):
            result[key] = value[key]
    if value.get("candidateState") in {"valid", "invalid", "not-checked"}:
        result["candidateState"] = value["candidateState"]
    if isinstance(value.get("candidateReason"), str) and CODES.fullmatch(value["candidateReason"]):
        result["candidateReason"] = value["candidateReason"]
    if isinstance(value.get("reason"), str) and CODES.fullmatch(value["reason"]):
        result["reason"] = value["reason"]
    return result


def read_health(root: Path, *, now=None):
    try:
        value = json.loads(read_regular(root / "data/work/pipeline-health.json", 65536))
        if not isinstance(value, dict) or value.get("format") != "kfm-pipeline-operator-health-v1" or not _time(value.get("checkedAt")):
            raise ValueError("PIPELINE_REPORT_INVALID")
        checked = datetime.fromisoformat(value["checkedAt"].replace("Z", "+00:00"))
        age = ((now or datetime.now(timezone.utc)) - checked).total_seconds()
        jobs = value.get("jobs")
        return {"format": value["format"], "checkedAt": value["checkedAt"], "stale": age > 900 or age < -60,
                "state": value.get("state") if value.get("state") in STATES else "unavailable",
                "publication": value.get("publication") if value.get("publication") in {"disabled", "approved-profiles-required"} else "unknown",
                "jobs": [{**_record(job), "sourceId": job["sourceId"]} for job in jobs if isinstance(job, dict) and job.get("sourceId") in {"nws-alerts", "usgs-streamflow", "usgs-earthquakes"}][:3] if isinstance(jobs, list) else [],
                **{key: _record(value.get(key)) for key in ("storage", "lastTick", "backup", "restore", "preservedArchiveBackup")}}
    except (OSError, ValueError, TypeError):
        return {"format": "kfm-pipeline-operator-health-v1", "state": "unavailable", "stale": True, "jobs": []}
