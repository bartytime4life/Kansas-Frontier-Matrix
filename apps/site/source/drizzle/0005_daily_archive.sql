-- Additive archive only. No existing dataset, receipt, or admission is changed.
CREATE TABLE daily_archive_captures (
  id TEXT PRIMARY KEY NOT NULL,
  day TEXT NOT NULL,
  feed TEXT NOT NULL,
  attempt INTEGER NOT NULL,
  status TEXT NOT NULL,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  bytes INTEGER NOT NULL DEFAULT 0,
  sha256 TEXT,
  object_key TEXT,
  feature_count INTEGER,
  source_time TEXT,
  source_day TEXT,
  message TEXT NOT NULL DEFAULT '',
  UNIQUE(day, feed, attempt)
);
--> statement-breakpoint
CREATE INDEX daily_archive_day_feed ON daily_archive_captures(day DESC, feed, attempt DESC);
--> statement-breakpoint
CREATE TABLE daily_archive_lock (id INTEGER PRIMARY KEY CHECK(id = 1), token TEXT NOT NULL, expires_at TEXT NOT NULL);
--> statement-breakpoint
CREATE TABLE daily_archive_settings (id INTEGER PRIMARY KEY CHECK(id = 1), budget INTEGER NOT NULL CHECK(budget >= 16777216), paused INTEGER NOT NULL DEFAULT 0 CHECK(paused IN (0,1)));
--> statement-breakpoint
CREATE TABLE daily_archive_reviews (id TEXT PRIMARY KEY NOT NULL, capture_id TEXT NOT NULL REFERENCES daily_archive_captures(id), state TEXT NOT NULL CHECK(state IN ('reviewed','held','pending')), note TEXT NOT NULL, reviewed_at TEXT NOT NULL);
--> statement-breakpoint
CREATE INDEX daily_archive_review_capture ON daily_archive_reviews(capture_id, reviewed_at DESC, id DESC);
