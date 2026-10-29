-- Additive MySQL 8+ projection. Existing capture and D1 tables are untouched.
CREATE TABLE IF NOT EXISTS kfm_pipeline_control (
 id TINYINT PRIMARY KEY, schema_version INT NOT NULL, paused BOOLEAN NOT NULL DEFAULT TRUE,
 worker_seen BIGINT NULL, worker_state VARCHAR(32) NULL
) ENGINE=InnoDB;
INSERT IGNORE INTO kfm_pipeline_control (id,schema_version) VALUES (1,1);
CREATE TABLE IF NOT EXISTS kfm_pipeline_nonces (
 nonce CHAR(64) PRIMARY KEY, expires BIGINT NOT NULL, INDEX kfm_pipeline_nonce_expiry (expires)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS kfm_pipeline_releases (
 release_id CHAR(64) PRIMARY KEY, source_id VARCHAR(32) NOT NULL,
 manifest_json MEDIUMTEXT NOT NULL, state VARCHAR(24) NOT NULL DEFAULT 'STAGED',
 projection_json MEDIUMTEXT NULL, created_at BIGINT NOT NULL,
 INDEX kfm_pipeline_history (source_id,created_at,release_id)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS kfm_pipeline_heads (
 source_id VARCHAR(32) PRIMARY KEY, release_id CHAR(64) NULL,
 previous_id CHAR(64) NULL, revision BIGINT NOT NULL DEFAULT 0
) ENGINE=InnoDB;
INSERT IGNORE INTO kfm_pipeline_heads (source_id) VALUES ('usgs-streamflow'),('nws-alerts'),('usgs-earthquakes'),('water'),('weather');
CREATE TABLE IF NOT EXISTS kfm_pipeline_events (
 event_id VARCHAR(64) PRIMARY KEY, source_id VARCHAR(32) NOT NULL,
 release_id CHAR(64) NOT NULL, previous_id CHAR(64) NULL,
 action VARCHAR(24) NOT NULL, occurred_at BIGINT NOT NULL
) ENGINE=InnoDB;
