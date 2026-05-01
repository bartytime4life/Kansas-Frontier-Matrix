# eBird Consumer Change Management (Layer 29)

Layer 29 adds local-only consumer impact and upgrade workflows.

- `kfm-ebird-consumer-impact`: scans certified consumers, computes deterministic `impact_id`, writes compatibility and renewal artifacts.
- `kfm-ebird-consumer-upgrade`: builds local-only upgrade/notification packs and deterministic `upgrade_pack_id`.

Safety: no network calls, no credential usage, no external notification delivery, no real eBird data, and no public exact coordinates.
