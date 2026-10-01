-- Additive released projection. This migration stages no source or public record.
CREATE TABLE IF NOT EXISTS knowledge_releases (
  release_id TEXT PRIMARY KEY NOT NULL,
  package_key TEXT NOT NULL UNIQUE,
  package_sha256 TEXT NOT NULL,
  source_admission_ref TEXT NOT NULL,
  rights_ref TEXT NOT NULL,
  sensitivity_ref TEXT NOT NULL,
  policy_ref TEXT NOT NULL,
  review_ref TEXT NOT NULL,
  release_ref TEXT NOT NULL,
  reviewer_key TEXT NOT NULL,
  releaser_key TEXT NOT NULL,
  reviewed_at TEXT NOT NULL,
  released_at TEXT NOT NULL,
  state TEXT NOT NULL CHECK(state IN ('APPROVED','WITHDRAWN')),
  previous_release_id TEXT
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS knowledge_active (
  singleton INTEGER PRIMARY KEY CHECK(singleton = 1),
  release_id TEXT NOT NULL,
  revision INTEGER NOT NULL CHECK(revision > 0),
  FOREIGN KEY(release_id) REFERENCES knowledge_releases(release_id)
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS knowledge_public (
  record_id TEXT NOT NULL,
  release_id TEXT NOT NULL,
  kind TEXT NOT NULL CHECK(kind IN ('place','fact','person','event','story')),
  title TEXT NOT NULL,
  summary TEXT NOT NULL,
  location_label TEXT NOT NULL,
  geometry_role TEXT NOT NULL,
  time_start TEXT,
  time_end TEXT,
  source_ref TEXT NOT NULL,
  source_url TEXT NOT NULL,
  evidence_ref TEXT NOT NULL,
  rights_ref TEXT NOT NULL,
  sensitivity_ref TEXT NOT NULL,
  review_ref TEXT NOT NULL,
  correction_state TEXT NOT NULL CHECK(correction_state IN ('ACTIVE','WITHDRAWN')),
  public_state TEXT NOT NULL CHECK(public_state IN ('PUBLIC_SAFE','WITHHELD')),
  assertions_json TEXT NOT NULL,
  FOREIGN KEY(release_id) REFERENCES knowledge_releases(release_id),
  PRIMARY KEY (release_id, record_id)
);
--> statement-breakpoint
CREATE INDEX IF NOT EXISTS idx_knowledge_public_lookup ON knowledge_public (release_id, public_state, correction_state, title, record_id);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS knowledge_corrections (
  correction_id TEXT PRIMARY KEY NOT NULL,
  record_id TEXT NOT NULL,
  prior_release_id TEXT NOT NULL,
  next_release_id TEXT,
  state TEXT NOT NULL CHECK(state IN ('CORRECTED','WITHDRAWN')),
  reason_ref TEXT NOT NULL,
  recorded_at TEXT NOT NULL
);
