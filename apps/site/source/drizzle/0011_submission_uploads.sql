-- Additive, shared reservations for data and land intake. Pending uploads do not
-- expire automatically: storage cleanup must finish before capacity is released.
CREATE TABLE IF NOT EXISTS data_submission_uploads (
  id TEXT PRIMARY KEY NOT NULL,
  owner_key TEXT NOT NULL,
  created_at TEXT NOT NULL
);
--> statement-breakpoint
CREATE INDEX IF NOT EXISTS idx_submission_uploads_owner ON data_submission_uploads (owner_key);
