-- Additive, Node composition-owned tables; run only after shared-DB review.
-- Never import D1/SQLite schemas, reset the database, or drop archived data.
CREATE TABLE IF NOT EXISTS kfm_ingest_control (
  id TINYINT NOT NULL PRIMARY KEY,
  schema_version INT NOT NULL,
  limit_bytes BIGINT UNSIGNED NOT NULL,
  used_bytes BIGINT UNSIGNED NOT NULL DEFAULT 0,
  reserved_bytes BIGINT UNSIGNED NOT NULL DEFAULT 0,
  paused BOOLEAN NOT NULL DEFAULT TRUE,
  lease_token VARCHAR(64) NULL,
  lease_until BIGINT UNSIGNED NOT NULL DEFAULT 0,
  last_tick BIGINT UNSIGNED NULL,
  last_actor VARCHAR(64) NULL
) ENGINE=InnoDB;
INSERT IGNORE INTO kfm_ingest_control (id,schema_version,limit_bytes) VALUES (1,1,80000000000);
CREATE TABLE IF NOT EXISTS kfm_ingest_jobs (
  source_id VARCHAR(64) NOT NULL PRIMARY KEY,
  capture_id CHAR(64) NULL,
  slot BIGINT UNSIGNED NULL,
  attempts INT UNSIGNED NOT NULL DEFAULT 0,
  retry_at BIGINT UNSIGNED NOT NULL DEFAULT 0,
  state VARCHAR(32) NOT NULL DEFAULT 'not-captured',
  last_error VARCHAR(64) NULL,
  checked_at BIGINT UNSIGNED NULL
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS kfm_ingest_captures (
  capture_id CHAR(64) NOT NULL PRIMARY KEY,
  source_id VARCHAR(64) NOT NULL,
  slot BIGINT UNSIGNED NOT NULL,
  sha256 CHAR(64) NOT NULL,
  byte_length BIGINT UNSIGNED NOT NULL,
  accounted_bytes BIGINT UNSIGNED NOT NULL,
  receipt MEDIUMTEXT NOT NULL,
  validation VARCHAR(32) NOT NULL,
  retrieved_at VARCHAR(32) NOT NULL,
  lifecycle VARCHAR(32) NOT NULL DEFAULT 'WORK/QUARANTINE',
  INDEX kfm_ingest_source_time (source_id,slot)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS kfm_ingest_chunks (
  capture_id CHAR(64) NOT NULL,
  chunk_index INT UNSIGNED NOT NULL,
  entity_bytes MEDIUMBLOB NOT NULL,
  PRIMARY KEY (capture_id,chunk_index),
  CONSTRAINT kfm_ingest_capture_fk FOREIGN KEY (capture_id) REFERENCES kfm_ingest_captures(capture_id)
) ENGINE=InnoDB;
-- Single-owner session; login replaces prior session, logout revokes it.
CREATE TABLE IF NOT EXISTS kfm_ingest_owner_session (
  owner_id VARCHAR(32) NOT NULL PRIMARY KEY,
  token_sha256 CHAR(64) NOT NULL,
  expires_at BIGINT UNSIGNED NOT NULL
) ENGINE=InnoDB;
