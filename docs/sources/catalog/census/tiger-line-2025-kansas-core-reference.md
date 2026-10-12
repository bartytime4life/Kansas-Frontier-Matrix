<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-census-tiger-line-2025-kansas-core-reference
title: TIGER/Line 2025 Kansas Core Source Reference
type: implementation-note
version: v0.1
status: proposed
owners: OWNER_TBD — Census source steward · Connector steward · Spatial Foundation steward · Validation steward
created: 2026-09-12
updated: 2026-09-12
policy_label: public; source-reference; census-geography; non-activating; externally-held
owning_root: docs/
responsibility: human-facing review note for one exact externally held TIGER/Line acquisition; no source admission, registry, evidence, release, publication, or runtime authority
truth_posture: "CONFIRMED exact Drive-handoff inventory, byte counts, digests, retrieval window, ZIP checks, and repository validator results / PROPOSED package selection and downstream roles / HOLD activation, admission, rights, sensitivity, release, publication, and runtime binding"
related:
  - docs/sources/catalog/census/tiger-line.md
  - docs/sources/catalog/census/README.md
  - connectors/census/README.md
  - connectors/census/tiger-line-2025-kansas-core.source-reference.json
  - tools/validators/source/tiger_line_kansas_core_reference.py
  - tests/source/test_tiger_line_kansas_core_reference.py
  - data/registry/sources/
tags: [kfm, census, tiger-line, kansas, source-reference, checksum, vintage, non-activating]
notes:
  - "A read-back-verified operator Drive handoff supplied the package facts; private Drive locators and raw payloads are intentionally absent from Git."
  - "This note and its connector-local manifest are review inputs, not SourceDescriptor, admission, evidence, release, publication, or runtime authority."
[/KFM_META_BLOCK_V2] -->

# TIGER/Line 2025 Kansas Core Source Reference

> Exact, checksum-bound inventory of one 2025 U.S. Census Bureau TIGER/Line
> acquisition assembled for Kansas review. Status: **PROPOSED / INACTIVE**.

## Outcome

The read-back-verified operator Drive handoff contains 326 original Census ZIP
packages totaling 991,516,458 bytes. Git records the official Census URLs,
filenames, sizes, checksums, source timestamps, retrieval timestamps, and
integrity results in
[`connectors/census/tiger-line-2025-kansas-core.source-reference.json`](../../../../connectors/census/tiger-line-2025-kansas-core.source-reference.json).
The ZIP payloads remain external to the repository.

| Inventory fact | Exact value |
|---|---:|
| Census ZIP packages | 326 |
| Census ZIP bytes | 991,516,458 |
| Product directories | 14 |
| County-scoped packages | 315 |
| Statewide or national packages | 11 |
| Kansas counties represented per county-scoped product | 105 |
| ZIP integrity checks | 326 passed |

## Candidate product selection

| Product | Packages | Candidate role | Boundary |
|---|---:|---|---|
| `STATE`, `COUNTY`, `COUSUB`, `PLACE` | 4 | Administrative/reference geometry | Not legal-boundary or cadastral authority. |
| `TRACT`, `BG`, `TABBLOCK20`, `ZCTA520` | 4 | Statistical/reference geometry | Not demographic data; joins remain vintage-bound. |
| `PRISECROADS`, `PRIMARYROADS`, `ROADS` | 107 | Transportation context/input | Not canonical road, access, or routing authority. |
| `RAILS` | 1 | Rail context/input | Not operating-status or ownership authority. |
| `AREAWATER`, `LINEARWATER` | 210 | Hydrographic context/input | Not canonical hydrology or streamflow authority. |

`ROADS`, `AREAWATER`, and `LINEARWATER` each contain one package for every
Kansas county GEOID from `20001` through `20209` in the exact 105-county set.
The other 11 products are represented by one Kansas-statewide or national
package as appropriate.

This is a candidate acquisition set, not an approved feature-class allow-list.
Product roles, CRS, topology, rights, sensitivity, admission, and downstream
fitness still require steward review.

## Integrity identity

| Check | Value |
|---|---|
| Package-index SHA-256 | `711f30103c647c76241f6450e3c9ad71abc5d4efbdeed591b975c1bb9cda7fbe` |
| Operator source-manifest SHA-256 | `bfb69f7630e6df94495d82507cf9a47c5eb5bd320667fff78f7acc0ef8af577d` |
| Operator delivery-index SHA-256 | `04624ea690e65280833ca6e44c01b8da66b8d60a4ff3405215dd3c5f03de410a` |
| Retrieval window | `2026-09-12T22:19:44Z` – `2026-09-12T22:24:30Z` |

The national `ZCTA520` source ZIP is 529,118,424 bytes with SHA-256
`e87129634eefe8719ef06ce4cfdf6588520be2e359360e590aaae90e4afb1911`.
It exceeded the transfer connector's single-file limit and entered operator
custody as six ordered pieces. The repository preserves the original ZIP's
source identity; transfer segmentation does not define another Census artifact.

No private Drive locator, Drive file ID, ZIP payload, extracted shapefile, or
derived geometry is committed. The public Census HTTPS URLs are acquisition
references only; they are not map or application runtime bindings.

## Offline verification

The validator checks the exact Census host and path, 2025 vintage, Kansas county
set, singleton package selection, ordering, counts, byte totals, timestamps,
SHA-256 values, package-index identity, private-locator exclusion, and all false
governance flags. It performs no network I/O.

```bash
python tools/validators/source/tiger_line_kansas_core_reference.py
```

An operator can verify an external handoff laid out as `PRODUCT/source.zip`.
The optional CRC pass decompresses each ZIP in memory without extracting it:

```bash
python tools/validators/source/tiger_line_kansas_core_reference.py \
  --payload-root /path/to/tiger2025-kansas-core \
  --check-zip-crc
```

Focused regression coverage is in
[`tests/source/test_tiger_line_kansas_core_reference.py`](../../../../tests/source/test_tiger_line_kansas_core_reference.py).

## Non-effects and next gates

This slice does not:

- register or activate a `SourceDescriptor`;
- approve a TIGER/Line feature-class allow-list;
- admit any bytes to RAW or QUARANTINE;
- complete CRS, topology, rights, or sensitivity review;
- emit a receipt, EvidenceBundle, proof pack, or release record;
- authorize publication or public use;
- bind a source to the governed API, site, or map runtime; or
- change a deployed environment.

Before any later activation, stewards must resolve the canonical feature-class
selection, source role per product, current Census rights/attribution posture,
sensitivity posture, CRS/topology inspection, target lifecycle location,
offline/unavailable behavior, and rollback-safe release boundary.

## Public upstream references

- [TIGER/Line Shapefiles landing page](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)
- [Official TIGER2025 archive root](https://www2.census.gov/geo/tiger/TIGER2025/)
- [KFM TIGER/Line product doctrine](./tiger-line.md)
