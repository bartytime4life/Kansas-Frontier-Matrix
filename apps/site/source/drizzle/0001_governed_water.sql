-- Additive candidate/activation metadata. Applying this migration activates nothing.
CREATE TABLE IF NOT EXISTS water_packages (
  package_id TEXT PRIMARY KEY NOT NULL,
  object_key TEXT NOT NULL UNIQUE,
  staged_at TEXT NOT NULL,
  staged_by TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'STAGED' CHECK(state IN ('STAGED','WITHDRAWN'))
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS water_active (
  singleton INTEGER PRIMARY KEY CHECK(singleton = 1),
  package_id TEXT NOT NULL,
  decision_json TEXT NOT NULL,
  previous_package_id TEXT,
  revision INTEGER NOT NULL CHECK(revision > 0),
  FOREIGN KEY(package_id) REFERENCES water_packages(package_id)
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS water_activation_events (
  event_id TEXT PRIMARY KEY NOT NULL,
  package_id TEXT NOT NULL,
  previous_package_id TEXT,
  decision_json TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  action TEXT NOT NULL CHECK(action IN ('ACTIVATE','ROLLBACK','WITHDRAW'))
);
