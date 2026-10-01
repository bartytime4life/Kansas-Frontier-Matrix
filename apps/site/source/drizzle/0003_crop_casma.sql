-- Reviewed 1 km soil tile package metadata. No package becomes active by migration.
CREATE TABLE IF NOT EXISTS crop_casma_packages (
  package_id TEXT PRIMARY KEY NOT NULL,
  day TEXT NOT NULL,
  manifest_key TEXT NOT NULL UNIQUE,
  source_sha256 TEXT NOT NULL,
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
  state TEXT NOT NULL CHECK(state IN ('STAGED','APPROVED','WITHDRAWN'))
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS crop_casma_active (
  singleton INTEGER PRIMARY KEY CHECK(singleton = 1),
  package_id TEXT NOT NULL,
  previous_package_id TEXT,
  revision INTEGER NOT NULL CHECK(revision > 0),
  FOREIGN KEY(package_id) REFERENCES crop_casma_packages(package_id)
);
