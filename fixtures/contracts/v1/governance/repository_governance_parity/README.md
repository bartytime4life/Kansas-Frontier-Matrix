# Repository governance parity fixtures

Synthetic fixtures exercise only the MRTS-04 classification boundary. They do
not scan repository content, create authority, waive topology drift, or approve
migration, deletion, release, deployment, promotion, or publication.

- `valid/inherited_hold.yaml` proves that an exact inherited hold remains a
  hold while the parity profile itself validates.
- `invalid/` covers check-not-run, lane failure, introduced drift, baseline
  growth, missing coverage, and an inherited failure mislabeled as pass.

The expected manifest binds each fixture to stable finding codes. All payloads
are synthetic and no-network.
