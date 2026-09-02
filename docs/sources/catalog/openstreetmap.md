# OpenStreetMap (OSM)

> Umbrella entry for the `openstreetmap` source family.

Status: **stub** (placeholder generated from `SKELETON_MAP.md`).

## What this page is

This file is the top-level catalog umbrella for the `openstreetmap` source family.
It links to the source descriptor(s), connector, and per-product catalog entries.

## Where the canonical material lives

- Source descriptors: `data/registry/sources/openstreetmap.yaml` (per-product descriptors under each domain register)
- Connector: `connectors/openstreetmap/`
- Per-product catalog entries: [`openstreetmap/`](./openstreetmap/)
- Standards: `docs/standards/STAC.md`, `docs/standards/DCAT.md`, `docs/standards/PROV.md`
- Rights & sensitivity: `docs/sources/RIGHTS_GUIDANCE.md`, `docs/sources/catalog/RIGHTS-AND-SENSITIVITY-MAP.md`

## Authority

This umbrella is documentation-only and does **not** carry promotion authority.
Admission of a source for ingest is governed by:

1. A signed `data/registry/sources/<source>.yaml` descriptor.
2. `policy/source/descriptor_required_before_ingest.rego`.
3. The promotion gate in `release/promotion_decisions/`.

See `docs/sources/ADMISSION_PROCESS.md` and `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`.

## Next steps

Replace this stub with a full source-family page using the template at
`docs/sources/catalog/_template/SOURCE_FAMILY_TEMPLATE.md`.
