-- Additive indexes matching the submission list order (created_at DESC, id DESC).
-- They let the reviewer queue and per-owner pages read rows in keyset order
-- instead of scanning and sorting the whole table. No row is changed.
CREATE INDEX IF NOT EXISTS idx_submissions_created_id ON data_submissions (created_at, id);
--> statement-breakpoint
CREATE INDEX IF NOT EXISTS idx_submissions_owner_created_id ON data_submissions (owner_key, created_at, id);
