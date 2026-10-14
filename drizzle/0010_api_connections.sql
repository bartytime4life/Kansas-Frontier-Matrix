-- Additive intake receipt index. Shares daily archive budget and lease; no data release.
CREATE TABLE api_connection_receipts (id TEXT PRIMARY KEY NOT NULL REFERENCES daily_archive_captures(id), source_id TEXT NOT NULL, slot INTEGER NOT NULL, receipt TEXT NOT NULL);
--> statement-breakpoint
CREATE INDEX api_connection_source_slot ON api_connection_receipts(source_id,slot DESC,id);
