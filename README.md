# Kansas Frontier Matrix

KFM is a Kansas-first, **map-first, time-aware, evidence-first, trust-visible**
spatial knowledge and publication system. Every consequential claim resolves
from `EvidenceRef` to `EvidenceBundle`; maps, tiles, graphs, dashboards, and
AI answers are *carriers* of evidence — never sovereign truth.

## Core invariant
`RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`
Promotion is a governed state transition, not a file move.

## Top-level map
| Root | Authority |
|------|-----------|
| `docs/` | Human-facing control plane: doctrine, architecture, ADR, domain docs, runbooks, sources, security, governance, registers, intake, archive, reports. |
| `control_plane/` | Machine-readable governance registers: documents, sources, object families, domain lanes, policy gates, release states, contradictions, deprecations. |
| `contracts/` | Semantic meaning of each object family. Pairs 1:1 with `schemas/`. |
| `schemas/` | Machine-checkable JSON Schema (and tests/valid + tests/invalid). |
| `policy/` | Policy-as-code (OPA/rego), bundles, fixtures, runtime/promotion/sensitivity/rights/release/UI policies. |
| `tests/` | Proves the doctrine: contracts, schemas, policy, validators, pipelines, api, ui, e2e, runtime_proof, domain tests. |
| `fixtures/` | No-network, deterministic test data: valid, invalid, golden, synthetic, per-domain. |
| `tools/` | Repo-wide validators, generators, catalog builders, proof-pack assembly, release tooling, QA, diff. |
| `scripts/` | Small operational scripts (dev, maintenance, one_off). |
| `apps/` | Deployable applications: `governed-api`, `explorer-web`, `review-console`, `cli`, `workers`, `admin`. |
| `packages/` | Shared libraries: evidence resolver, policy runtime, registries, hashing, geo, temporal, catalog, release, ui, maplibre, cesium, per-domain. |
| `connectors/` | Source-specific fetch + admission code. Outputs to `data/raw/` or `data/quarantine/`. |
| `pipelines/` | Executable pipeline logic: ingest, normalize, validate, catalog, triplets, publish, rollback, per-domain. |
| `pipeline_specs/` | Declarative pipeline configuration (the *what*; `pipelines/` is the *how*). |
| `data/` | Lifecycle data: raw, work, quarantine, processed, catalog, triplets, receipts, proofs, published, registry, prov, manifests, reports. |
| `release/` | Release decisions, manifests, promotion decisions, rollback cards, correction & withdrawal notices, signatures, changelog. |
| `runtime/` | Local runtime wiring + model adapters (Ollama, Mock); subordinate to evidence/policy/release. |
| `infra/` | Deployment, host, network, exposure posture; deny-by-default. |
| `configs/` | Safe non-secret configuration defaults and templates. |
| `migrations/` | Database / schema / data / graph migrations + rollback scripts. |
| `examples/` | Example source intakes, story decks, walkthroughs. |
| `artifacts/` | Optional / compatibility: build, docs, qa, temporary. *Not* a home for trust-bearing receipts/proofs/manifests. |

See `docs/architecture/SYSTEM_MAP.md` and `docs/doctrine/` for the full
architecture narrative.

## Status
Greenfield scaffold. Every file is a placeholder unless explicitly
promoted via ADR + governed change.
