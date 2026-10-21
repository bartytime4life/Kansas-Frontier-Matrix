-- PROPOSED additive MySQL 8.0+ migration. NOT applied to any shared database.
-- Preflight version, InnoDB, CHECK enforcement, TLS, backups, quota, grants and runner.
-- No approval/release table or publishing procedure is created.
CREATE TABLE IF NOT EXISTS kfm_faa_captures (
  candidate_id CHAR(71) CHARACTER SET ascii COLLATE ascii_bin PRIMARY KEY,
  archive_sha256 CHAR(64) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  edition DATE NOT NULL,
  retrieved_at VARCHAR(32) NOT NULL,
  source_publication_time VARCHAR(32) NULL,
  parser_version VARCHAR(32) NOT NULL,
  source_rows INT UNSIGNED NOT NULL,
  accepted_rows INT UNSIGNED NOT NULL,
  rejected_rows INT UNSIGNED NOT NULL,
  rights_state VARCHAR(32) NOT NULL DEFAULT 'REVIEW_REQUIRED',
  release_state VARCHAR(16) NOT NULL DEFAULT 'HELD',
  CHECK (release_state = 'HELD'),
  UNIQUE KEY faa_capture_digest (archive_sha256, candidate_id)
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS kfm_faa_airport_revisions (
  candidate_id CHAR(71) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  revision_id VARCHAR(80) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  entity_id VARCHAR(40) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  edition DATE NOT NULL,
  valid_to_exclusive DATE NOT NULL,
  state CHAR(2) NOT NULL,
  county_name VARCHAR(64) NOT NULL,
  county_state CHAR(2) NOT NULL,
  faa_id VARCHAR(4) NOT NULL,
  icao_id VARCHAR(4) NULL,
  name VARCHAR(100) NOT NULL,
  longitude DECIMAL(12,8) NOT NULL,
  latitude DECIMAL(11,8) NOT NULL,
  elevation_ft_msl DECIMAL(9,2) NULL,
  horizontal_datum VARCHAR(32) NOT NULL,
  public_candidate BOOLEAN NOT NULL DEFAULT FALSE,
  record_json JSON NOT NULL,
  PRIMARY KEY (candidate_id, revision_id),
  UNIQUE KEY faa_candidate_entity (candidate_id, entity_id),
  KEY faa_county_edition (candidate_id, state, county_state, county_name, revision_id),
  KEY faa_space (candidate_id, longitude, latitude),
  FOREIGN KEY (candidate_id) REFERENCES kfm_faa_captures(candidate_id),
  CHECK (longitude BETWEEN -180 AND 180),
  CHECK (latitude BETWEEN -90 AND 90),
  CHECK (valid_to_exclusive > edition)
) ENGINE=InnoDB;
