-- Additive storm events candidate/activation metadata (ADR-0047). Applying this migration activates nothing.
-- Storm events never share a table with water, weather or soil; their tables are untouched.
CREATE TABLE IF NOT EXISTS storm_events_packages (
  package_id TEXT PRIMARY KEY NOT NULL,
  object_key TEXT NOT NULL UNIQUE,
  staged_at TEXT NOT NULL,
  staged_by TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'STAGED' CHECK(state IN ('STAGED','WITHDRAWN'))
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS storm_events_active (
  singleton INTEGER PRIMARY KEY CHECK(singleton = 1),
  package_id TEXT NOT NULL,
  decision_json TEXT NOT NULL,
  previous_package_id TEXT,
  revision INTEGER NOT NULL CHECK(revision > 0),
  FOREIGN KEY(package_id) REFERENCES storm_events_packages(package_id)
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS storm_events_activation_events (
  event_id TEXT PRIMARY KEY NOT NULL,
  package_id TEXT NOT NULL,
  previous_package_id TEXT,
  decision_json TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  action TEXT NOT NULL CHECK(action IN ('ACTIVATE','ROLLBACK','WITHDRAW'))
);
