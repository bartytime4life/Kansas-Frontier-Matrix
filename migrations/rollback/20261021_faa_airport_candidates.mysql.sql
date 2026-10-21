-- MANUAL disposable-environment rollback only. Never delete irreplaceable captures.
-- First preserve a verified backup plus immutable RAW/receipts and stop candidate imports.
-- These dedicated candidate tables have no public readers or release bindings.
DROP TABLE IF EXISTS kfm_faa_airport_revisions;
DROP TABLE IF EXISTS kfm_faa_captures;
