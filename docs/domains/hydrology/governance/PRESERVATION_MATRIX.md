# Hydrology Preservation Matrix

| Data class | Preserve | Transform allowed | Delete allowed |
| --- | --- | --- | --- |
| RAW fixtures | Yes (pinned snapshots) | No (copy-only) | No |
| WORK artifacts | Optional (run scoped) | Yes | Yes, by retention policy |
| QUARANTINE artifacts | Yes (until reviewed) | Annotation only | Restricted |
| PROCESSED artifacts | Yes | Rebuild with new `spec_hash` | No |
| PUBLISHED artifacts | Yes (immutable) | No | No |
| Release aliases | Yes (history) | Move pointer only | No hard delete |

## Policy intent
Preserve auditability and reproducibility over storage convenience.
