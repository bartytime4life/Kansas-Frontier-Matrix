"""Build a private feed recovery report from service journal messages and read-only SQL checkpoints."""

from datetime import datetime, timedelta, timezone
import json
import re
import sqlite3


# These feeds appear in the installed daily schedule documented in the runbook.
DAILY_LAB_FEEDS = ("air-quality", "captures", "climdiv", "drought", "earthquakes",
                   "ghcnd", "iem-wind", "nass", "nwm", "prism", "usgs-daily", "water-quality")
MAX_JOURNAL_BYTES = 32 * 1024 * 1024
MAX_JOURNAL_LINE = 1024 * 1024
FEED_EVENTS = {"feed_started", "feed_done", "feed_failed"}
HOLD_REASONS = {
    "file blockers": "FILE_BLOCKERS",
    "missing matching provenance receipt": "PROVENANCE_RECEIPT_MISSING",
    "capture digest mismatch": "CAPTURE_DIGEST_MISMATCH",
    "invalid feature collection": "INVALID_CAPTURE_GEOJSON",
    "invalid feature": "INVALID_CAPTURE_GEOJSON",
}
REASON_CODE = re.compile(r"[A-Z][A-Z0-9_]{1,47}\Z")
UTC_TIME = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,6})?Z\Z")
RETRYABLE = {"FETCH_FAILED", "PIPELINE_LOCK_BUSY", "HTTP_408", "HTTP_429"}
ACTIONS = {
    "missing-evidence": "check-installed-timer-and-journal-window",
    "in-progress": "check-service-activity-and-wait",
    "missing-terminal-event": "check-service-result-before-retrying",
    "retryable-failure": "inspect-provider-or-lock-then-let-next-timer-retry",
    "review-required": "inspect-failure-and-preserve-checkpoint",
    "overdue": "check-installed-timer-and-service-result",
    "completed": "observe-next-scheduled-run",
}


def positive_hours(value):
    """Parse a bounded CLI threshold in whole hours."""
    hours = int(value)
    if not 1 <= hours <= 24 * 60:
        raise ValueError("hours must be from 1 to 1440")
    return hours


def timestamp(value):
    if not isinstance(value, str) or len(value) > 32 or not UTC_TIME.fullmatch(value):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def iso(moment):
    return moment.isoformat().replace("+00:00", "Z") if moment is not None else None


def _safe_reason(value):
    code = value.split(None, 1)[0] if isinstance(value, str) and value.strip() else ""
    return code if REASON_CODE.fullmatch(code) else "UNCLASSIFIED_FEED_ERROR"


def events(stream, feeds, now):
    """Read bounded journalctl -o cat output; parse only registered feed lifecycle events."""
    result = {feed: [] for feed in feeds}
    bytes_read = 0
    while line := stream.readline(MAX_JOURNAL_LINE + 1):
        bytes_read += len(line)
        if bytes_read > MAX_JOURNAL_BYTES or len(line) > MAX_JOURNAL_LINE:
            raise ValueError("JOURNAL_INPUT_LIMIT")
        if not line.lstrip().startswith(b"{"):
            continue
        try:
            value = json.loads(line)
        except (ValueError, RecursionError):
            continue
        if not isinstance(value, dict):
            continue
        feed, kind, at = value.get("feed"), value.get("event"), timestamp(value.get("at"))
        if not isinstance(feed, str) or feed not in result or not isinstance(kind, str) or kind not in FEED_EVENTS:
            continue
        if at is None or at > now + timedelta(minutes=5):
            continue
        started = timestamp(value.get("started_at"))
        # Old releases have terminal events only; their event time is the available evidence.
        if started is None or started.replace(microsecond=0) > at:
            started = at
        event = {"kind": kind, "at": at, "started_at": started}
        if kind == "feed_failed":
            event["reason_code"] = _safe_reason(value.get("reason"))
        if kind == "feed_done" and feed == "captures":
            count, reasons = value.get("held"), value.get("held_reasons")
            if type(count) is int and 0 <= count <= 2**53:
                event["held_count"] = count
                event["held_reasons"] = sorted({
                    HOLD_REASONS.get(reason, "CAPTURE_REVIEW_REQUIRED") for reason in reasons if isinstance(reason, str)
                }) if isinstance(reasons, list) else []
        result[feed].append(event)
    return result


def _checkpoints(path, selected):
    if path is None:
        return "not-configured", {}
    if not path.is_file():
        return "missing", {}
    try:
        conn = sqlite3.connect(path.absolute().as_uri() + "?mode=ro", uri=True, timeout=2)
        try:
            if not conn.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='kfm_feed_state'").fetchone():
                return "no-checkpoint-table", {}
            placeholders = ",".join("?" for _ in selected)
            rows = conn.execute(f"SELECT feed, updated_at FROM kfm_feed_state WHERE feed IN ({placeholders})", selected)
            return "readable", {name: stamp for name, value in rows if (stamp := timestamp(value)) is not None}
        finally:
            conn.close()
    except sqlite3.Error:
        return "unavailable", {}


def _held_state(entries, now, hold_age):
    first = last = None
    for event in sorted(entries, key=lambda entry: entry["at"]):
        if "held_count" not in event:
            continue
        if event["held_count"] == 0:
            first = last = None
        else:
            first = first or event["at"]
            last = event
    if last is None:
        return None
    if last["at"] - first >= hold_age:
        status = "stalled"
    elif now - last["at"] >= hold_age:
        status = "held-observation-stale"
    else:
        status = "held"
    return {"count": last["held_count"], "first_observed_at": iso(first), "observed_at": iso(last["at"]),
            "status": status, "reason_codes": last["held_reasons"],
            "next_action": "review-blockers-before-admission"}


def _feed_report(feed, entries, checkpoint, *, now, max_age_hours, run_timeout, hold_age):
    # Order by invocation start so an older overlapping attempt cannot replace a newer one.
    latest = max(entries, key=lambda e: (e["started_at"], e["at"], e["kind"] != "feed_started"), default=None)
    success = max((event["at"] for event in entries if event["kind"] == "feed_done"), default=None)
    row = {"feed": feed, "last_completed_at": iso(success), "last_sql_checkpoint_at": iso(checkpoint),
           "max_age_hours": max_age_hours}
    if latest is None:
        status = "missing-evidence"
    else:
        row["last_attempt_at"] = iso(latest["started_at"])
        if latest["kind"] == "feed_started":
            status = "missing-terminal-event" if now - latest["started_at"] >= run_timeout else "in-progress"
        elif latest["kind"] == "feed_failed":
            code = latest["reason_code"]
            row["failure_code"] = code
            status = "retryable-failure" if code in RETRYABLE or re.fullmatch(r"HTTP_5[0-9]{2}", code) else "review-required"
        else:
            status = "overdue" if now - success > timedelta(hours=max_age_hours) else "completed"
    held = _held_state(entries, now, hold_age)
    if held is not None:
        row["hold"] = held
    return {**row, "status": status, "next_action": ACTIONS[status]}


def report(stream, *, selected, observations, bulk, bulk_feeds, now=None,
           max_age_hours=None, run_timeout_hours=8, hold_age_hours=24):
    now = now or datetime.now(timezone.utc)
    selected = tuple(sorted(set(selected)))
    entries = events(stream, selected, now)
    groups = (("observations", observations, tuple(feed for feed in selected if feed not in bulk_feeds)),
              ("bulk", bulk, tuple(feed for feed in selected if feed in bulk_feeds)))
    databases, checkpoints = {}, {}
    for name, path, feeds in groups:
        if feeds:
            databases[name], values = _checkpoints(path, feeds)
            checkpoints.update(values)
    return {"format": "kfm-sql-feed-recovery-v1", "checked_at": iso(now), "databases": databases,
            "run_timeout_hours": run_timeout_hours, "hold_age_hours": hold_age_hours,
            "feeds": [_feed_report(feed, entries[feed], checkpoints.get(feed), now=now,
                                   max_age_hours=max_age_hours or (3 if feed == "captures" else 36),
                                   run_timeout=timedelta(hours=run_timeout_hours),
                                   hold_age=timedelta(hours=hold_age_hours)) for feed in selected]}
