-- Fresh public-copy storage only. No private archive/review bytes are migrated.
CREATE TABLE IF NOT EXISTS public_delivery_active (
  family TEXT PRIMARY KEY CHECK(family IN ('subsurface','groundwater','archive')),
  package_id TEXT NOT NULL,
  manifest_sha256 TEXT NOT NULL,
  previous_package_id TEXT,
  state TEXT NOT NULL CHECK(state IN ('ACTIVE','WITHDRAWN')),
  revision INTEGER NOT NULL CHECK(revision > 0)
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS public_delivery_events (
  event_id TEXT PRIMARY KEY,
  family TEXT NOT NULL,
  package_id TEXT NOT NULL,
  previous_package_id TEXT,
  manifest_sha256 TEXT NOT NULL,
  occurred_at TEXT NOT NULL,
  actor TEXT NOT NULL,
  action TEXT NOT NULL CHECK(action IN ('ACTIVATE','ROLLBACK','WITHDRAW'))
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS public_delivery_staging_events (
  family TEXT NOT NULL,
  package_id TEXT NOT NULL,
  artifact_name TEXT NOT NULL,
  artifact_sha256 TEXT NOT NULL,
  bytes INTEGER NOT NULL,
  staged_at TEXT NOT NULL,
  actor TEXT NOT NULL,
  PRIMARY KEY(family,package_id,artifact_name)
);
