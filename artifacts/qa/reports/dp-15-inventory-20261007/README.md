<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/qa/dp-15-inventory-20261007
title: DP-15 current-tree inventory review aid
type: qa-report
version: v1.0.0
status: generated-review-aid; non-authoritative; human-review-pending
owners: ["@bartytime4life — review routing only"]
created: 2026-10-07
updated: 2026-10-07
policy_label: repository-facing
owning_root: artifacts/
responsibility: Replaceable lexical inventory and exact-source review aid; no policy, proof, release, or DP adoption authority.
truth_posture: CONFIRMED tracked-blob visitation and classified lexical inventory at the pinned revision; UNKNOWN external/deployed state; no operational approval.
generated_from: main@c90836cdb7a34791669907053522de0458f21ae9
generator_identity: scan.py + classify.py v1.0.0 for machine inventory; AI-authored source-review narrative
content_digests: data/receipts/generated/genrec-dp15-current-tree-inventory-20261007.json
edit_policy: Regenerate machine outputs; review narrative classifications against pinned bytes.
[/KFM_META_BLOCK_V2] -->

# DP-15 current-tree inventory — 2026-10-07 UTC

The inventory confirms the prior conclusion: **no accepted DP-specific semantic contract, schema, policy rule, admitted dependency, mechanism/accountant, budget ledger, DP fixture/test family, validator/CI check, emitted DP receipt/release object, or DP runtime/API/map/AI consumer was found in this current-main tree.** DP-15's repository-coverage uncertainty can close at this revision. DP-01–DP-14 and graduation gates G0–G12 retain their existing states; operational use remains `HOLD`.

This is a replaceable QA review aid under `artifacts/qa/reports/`, not an EvidenceBundle, proof, accounting record, policy decision, acceptance record, release object, or new canonical writer. Its claims are derived from pinned source bytes. The generated-work receipt is separate under `data/receipts/generated/`.

## Exact snapshot and coverage

| Item | Observation |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Main commit | `c90836cdb7a34791669907053522de0458f21ae9` |
| Tree | `219cd776542fc79030897633acc77d4cb3e3b0e3` |
| Target prior blob | `ae05701e304ff7e7f339035cc19116cd2e5f4d05` |
| Recursive tree manifest SHA-256 | `12592fa8e5e55f4659adf2922a982cf66ed86ca58108d1980b344bd542f66296` |
| Tracked blobs visited | **14,164**, **215,327,106 bytes**; every Git blob SHA recomputed |
| Modes | 14,073 regular non-executable files; 91 executable files; no symlink or gitlink entries |
| Decoded representations | 14,903; ordinary UTF-8, all 258 gzip payloads, vendored tar member text, two PDF text extractions, GLB JSON when present, binary printable metadata |
| Read/decode failures | **0** |
| Classified hit rows / paths | **67,125 / 5,653**; **0 unclassified rows** |
| Dependency/config manifests | 73 exact paths in `summary.json`; includes all tracked Python/Node locks, project manifests, requirements and Dockerfiles |

No ignore rule, hidden-path exclusion, GitHub search index, result limit, extension-only filter, or default ripgrep binary exclusion controls the primary inventory. It reads commit objects directly with `git ls-tree -r -z --full-tree` and `git cat-file --batch`, asserts every blob hash, and records all matches. Path matching includes file names. Archive member and decompressed locations use `::` suffixes; their `blob` binds the tracked container, not a separate Git object. Line `0` is a pathname hit. Binary strings line numbers refer to the extracted printable representation.

Coverage is exhaustive for **tracked-object visitation at this commit**, with the full disclosed lexical families and reviewed DP declarations. It is not a mathematical proof that arbitrarily obfuscated code is impossible, a scan of Git history/other branches, a check of installed dependencies or running/deployed services, or an inventory of remote GitHub release assets/Actions artifacts, untracked data, secrets, external storage or host configuration. Those limits do not leave any tracked path unvisited. No DP mechanism was run and no sensitive data or budget was processed.

## Surface coverage

| Root / surface | Tracked blobs visited |
|---|---:|
| `.github` | 505 |
| `apps` | 765 |
| `artifacts` | 47 |
| `catalog` | 43 |
| `configs` | 31 |
| `connectors` | 367 |
| `contracts` | 819 |
| `control_plane` | 36 |
| `data` | 2081 |
| `docs` | 1841 |
| `examples` | 15 |
| `fixtures` | 3244 |
| `infra` | 23 |
| `migrations` | 11 |
| `packages` | 265 |
| `pipeline_specs` | 149 |
| `pipelines` | 153 |
| `policy` | 358 |
| `release` | 93 |
| `runtime` | 22 |
| `schemas` | 1049 |
| `scripts` | 22 |
| `tests` | 1270 |
| `tools` | 938 |

All remaining tracked root files are enumerated in `summary.json`. `data/`, `release/`, and legacy `artifacts/` were scanned recursively; source-ledger and generic receipt/release names were not assumed to be DP ledgers or DP-bearing objects.

## Search families and evidence files

The exact regular expressions and query counts are in [summary.json](summary.json). They cover differential privacy/differentially private, DPBudget/DPReceipt and `dp_*` budget/aggregate/noise/receipt/accounting terms; DP/RDP/zCDP/CDP/LDP/GDP, Rényi, pure/approximate/local DP, DP-SGD, DAS/TopDown/disclosure avoidance, DP05 data-profile identifiers and privacy-preserving aliases; OpenDP, Google DP, PyDP, diffprivlib, Opacus, TensorFlow Privacy, dp-accounting, PipelineDP, SmartNoise, Tumult, privacy-on-beam and related library names; epsilon/eps/Greek epsilon-delta, Laplace/Gaussian, accountants, filters/odometers, privacy-spent/noise-scale/add-noise terms, randomized response, geometric/exponential mechanisms, neighboring datasets and contribution bounds; and broad privacy/sensitivity/noise/clipping/budget/ledger/delta/composition/anonymity terms.

- [inventory.json.gz](inventory.json.gz): every matching exact path, source Git blob, directly declared source status, authority level, disposition and per-query line list. Declared status is preserved as evidence, not treated as adoption proof.
- [hits.csv.gz](hits.csv.gz): every one of the 67,125 matching line/path rows, matched terms, query family, authority level, disposition and reason. No hit is dropped because it is unrelated to DP.
- [dp-declarations.json](dp-declarations.json): complete source lines for DP guidance, upstream claims and generated provenance, with classifications; 65 distinct exact paths.
- [scan.py](scan.py) and [classify.py](classify.py): read-only reproduction scripts. These are QA tools, not a DP validator, enforcement rule or accepted dependency.

Classification separates the file's responsibility from the DP claim. Executable code can exist for a non-DP profile; an accepted placement rule cannot accept a DP mechanism; a document's `CONFIRMED` label can describe corpus wording without proving implementation.

## Authority and implementation readback

| Surface | Exact source readback | DP disposition |
|---|---|---|
| Semantic / machine shape | `contracts/data/typed_receipt_aggregation.md`; `schemas/contracts/v1/data/typed_receipt_aggregation.schema.json` | Proposed inactive / fixture-only / authority `NONE`; aggregates receipt declarations, not numeric private data or privacy loss. Its validator, fixtures and tests are real bounded machinery for this separate profile, not DP. |
| Agriculture aggregation | `contracts/domains/agriculture/aggregation-receipt.md`; `schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json`; `policy/sensitivity/agriculture/aggregation_thresholds.yaml`; `tests/domains/agriculture/test_nass_aggregate_only.py` | Draft/scaffold with permissive empty schema, proposed threshold placeholder and docstring-only test; no DP guarantee or accountant. |
| Receipt lane | `data/receipts/aggregation/README.md` | Placement-held, README-only lane; no emitted DP receipt in the recursive scan. |
| Redaction implementation | `packages/redaction/src/redaction/core.py` | Greenfield comment-only placeholder, not a mechanism. Other redaction receipt validation is not DP implementation. |
| Runtime serving gate | `packages/policy-runtime/src/policy_runtime/core.py`; `apps/governed-api/src/governed_api/main.py`; `apps/governed-api/src/governed_api/routes/registry.py` | Water release reference/time/rights/sensitivity checks and finite routes; no DP accounting, mechanism constructor or DP consumer. Source inspection only, not live runtime acceptance. |
| API/map/AI | All `apps/site/source/app/`, including `app/api/qwen/route.ts` and API routes; full `apps/`, `runtime/`, `packages/` | No DP import, constructor, ledger transaction or release binding found. Hosted Qwen route returns disabled responses; that is not a DP protection. No inference operation performed. |
| Dependencies | 73 manifest/lock/config paths; expanded `apps/site/source/vendor/vinext-0.0.50-kfm.1.tgz` | No DP library pinned/imported/admitted in these sources. Vendored `private` keywords and internal budgets are non-DP framework source. |
| Policy, CI, validators, fixtures/tests | Full `policy/`, `.github/`, `tools/`, `fixtures/`, `tests/` and nested app/connector tests | No DP-specific enforcement or fixture family. Generic privacy boundaries, resource budgets, receipt fields and synthetic redaction declarations do not close DP gates. |
| Receipts, release objects and ledgers | Full `data/`, `release/`, `catalog/`, `control_plane/`, `artifacts/` | The prior DP modernization generated receipt records document authorship only; no DP expenditure/accounting/output receipt or release object found. |

### Proposed names traced to current bytes

`docs/doctrine/sensitivity.md` names `DPBudgetRecord`, `dp_aggregate_v1`, `schemas/contracts/v1/dp_budget_record.schema.json`, `dp-budget-presence`, and `dp-aggregate-only`. The first two are candidate prose; the schema path has **no tracked entry**, and the two job names have **no workflow definition** in the complete workflow inventory. No alternate DP schema/job home was found by the full content/path scan.

`docs/atlases/sensitivity-tier-reference.md` names `contracts/data/aggregation_receipt.md` and `fixtures/sensitivity/invalid/dp_applied_to_per_record_display.json`; neither has a tracked entry. `docs/domains/people-dna-land/DNA_HANDLING.md` names `dp_applied_to_raw_points.json`; no tracked file with that basename exists. FEMA and FTDNA pages' `DPReceipt`, `dp_budget_ref`, `kfm:dp_applied` and `kfm:dp_epsilon` are prose/examples, not schemas, instances or consumers. Proposed fixture names are not counted as actual fixtures.

### Non-DP aliases and plausible mechanisms

- `docs/standards/Darwin_Core.md`: **DwC-DP** means Darwin Core Data Package.
- Census place documentation/contracts: **CDP** means Census-designated place; `apps/site/source/scripts/verify-explorer-geometry.mjs`: **CDP** means Chrome DevTools Protocol.
- EconomicObservation contract/schema/fixtures/validator/tests: **GDP** is the economic measure, not Gaussian differential privacy.
- Hydrology/geology diagrams: **DP** is the node label for `data/processed/`.
- `connectors/census/src/census/acs_api.py`, its test, `apps/site/source/tests/rendered-html.test.mjs` and `fixtures/ui/acs_population_context/acs-2024-dp05-bounded.json`: **DP05** is a Census data-profile identifier, not a privacy mechanism.
- `apps/site/source/app/api/hydrology/streamflow/route.ts`: `Number.EPSILON` protects longitude/latitude normalization. `tools/validators/common/validate_station_spatial_assignment_assessment.py` and `tools/validators/map/validate_georeference_spatial_distribution.py`: `eps`/`EPS` are geometry tolerances. `tools/validators/map/validate_georeference_transform_quality.py` uses deterministic Gaussian elimination, not Gaussian noise. Their exact hit lines and blobs are in the indexes.
- `apps/site/source/app/wind-arrow-canvas.ts` uses visual `noise` for particle placement. Geometry clipping, weather/measurement noise, resource budgets, change deltas, source ledgers and generic privacy controls are non-DP support matches.
- The eight residual binary assets are three PNGs, three HDF5 lightning fixtures and two synthetic 3D fixture byte payloads. Their exact paths, sizes/types and lexical coincidences are in `summary.json` and the indexes. They are data/assets, not executable privacy machinery. Gzip and vendored tar payloads were expanded, not excluded as binary.

Upstream Census DP/DAS assertions in source documentation are **classified repository claims**, not freshly verified upstream facts or KFM implementation. This inventory does not endorse the ACS assertion, select an upstream privacy profile, admit a source, or rewrite unrelated source documentation. NIST/OpenDP external snapshots in the standard retain their historical dates.

## Complete DP declaration path classification

Full lines and exact line numbers are in `dp-declarations.json`; all other lexical hits, including aliases, are in `inventory.json.gz` and `hits.csv.gz`. Every row below has **no accepted/executable KFM DP authority**.

| Exact path | Responsibility / authority level | Declared source status | DP classification |
|---|---|---|---|
| `connectors/ftDNA/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `connectors/ftDNA/src/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `connectors/ftDNA/src/ftDNA/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `connectors/gbif/src/gbif/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `data/catalog/domain/people/dna/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | repository-grounded draft; PROPOSED; CONFLICTED-SEGMENT; compatibility-sublane; catalog-stage; restricted; deny-by-default; release-gated; no-active-dna-catalog-established | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `data/receipts/generated/genrec-dp-budgets-standard-modernization-20260818.json` | GENERATED_PROVENANCE | not declared in a directly readable status field | DOCUMENTATION_PROVENANCE |
| `data/registry/sensitivity/archaeology/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/adr/ADR-0016-telemetry-redaction-posture.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | proposed | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/architecture/sensitivity.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; repository-grounded; non-authoritative; convergence-hold | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/atlases/sensitivity-tier-reference.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/doctrine/sensitivity.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/domains/archaeology/SENSITIVITY.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/domains/archaeology/SOURCE_REGISTRY.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/atmosphere/SENSITIVITY.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/fauna/DATA_LIFECYCLE.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/fauna/POLICY.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/flora/SOURCE_REGISTRY.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/DNA_HANDLING.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/domains/people-dna-land/EXPANSION_BACKLOG.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/EXPANSION_PLAN.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/MISSING_OR_PLANNED_FILES.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; repository-grounded landing boundary; mixed implementation maturity; sensitive-domain holds preserved; non-release; non-publication | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/SENSITIVITY_PROFILE.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/SOURCE_FAMILIES.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/SOURCE_LEDGER.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/SOURCE_REGISTRY.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/domains/people-dna-land/sublanes/dna.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/focus-mode/CONSENT_PATTERN.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; repository-grounded; documentation-only; mixed-maturity; no-consent-authority; no-runtime-enforcement; non-release; non-publication | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/intake/exploratory/new-ideas-5-19-26-source-map.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; triaged; noncanonical | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/runbooks/SENSITIVITY_ESCALATION.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/security/DATA_CLASSIFICATION.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/security/KEY_ROTATION.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/census/acs-estimates.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, NON_DP_ALIAS, UPSTREAM_CENSUS_CLAIM_OR_GUIDANCE |
| `docs/sources/catalog/census/decennial-counts.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, NON_DP_ALIAS, UPSTREAM_CENSUS_CLAIM_OR_GUIDANCE |
| `docs/sources/catalog/census/decennial-microdata.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/census/nhgis-compilations.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | ADJACENT_PRIVACY_OR_NON_DP_ALIAS, BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/ebird/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/ebird/ebird-api.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/sources/catalog/ebird/ebird-basic-dataset.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/ebird/sampling-event-data.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/eddmaps/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/familysearch/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/familysearch/family-tree.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/fema/nfip-claim-policy-aggregates.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/fema/openfema-auxiliary-tables.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/ftdna/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/ftdna/autosomal-raw-data.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/ftdna/dna-matches.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/sources/catalog/ftdna/dna-segments.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/sources/catalog/ftdna/haplogroup-data.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/sources/catalog/inaturalist/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/sources/catalog/natureserve/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/standards/DP_BUDGETS.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; guidance-only; operational-use-hold | ADJACENT_PRIVACY_OR_NON_DP_ALIAS, BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/standards/DUO_PROFILE.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | "draft; repository-grounded; upstream-currentness-refreshed; no-adoption; no-policy-activation; no-conformance-proof; no-release; no-publication" | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/standards/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | "active; repository-grounded; mixed-maturity" | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/standards/REDACTION_DETERMINISM.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/standards/REDACTION_PROFILES.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | "draft; repository-grounded; catalog-home-conflicted; proposed-inactive; fixture-only-receipt-proof; no-active-profile; no-transform-runtime; no-release; no-publication" | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/standards/SENSITIVITY_RUBRIC.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/standards/STAC-DwC.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `docs/standards/stac-dwc-hybrid.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION, NON_DP_NUMERIC_OR_GUIDANCE |
| `docs/wiki/Security-and-Sensitivity.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | PROPOSED wiki source; review required | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `packages/domains/archaeology/generalization/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; repository-grounded; bounded-readme-surface; generalizer-not-implemented; profiles-not-accepted; sensitive-domain; non-authoritative | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `packages/redaction/src/redaction/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `policy/domains/archaeology/promotion/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; repository-grounded; README-only-direct-lane; shared-shape-validation-confirmed; archaeology-enforcement-unestablished; fail-closed; non-authoritative-for-release | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |
| `policy/domains/archaeology/sensitivity/README.md` | GUIDANCE_OR_BOUNDARY_DOCUMENT | draft; repository-grounded; README-only-direct-lane; parent-rego-scaffolds-confirmed; transform-and-receipt-shapes-permissive; archaeology-sensitivity-enforcement-unestablished; fail-closed; non-authoritative-for-release | BROAD_NON_DP_SUPPORT, DP_GUIDANCE_PROPOSAL_OR_EXCLUSION |

## Reproduce and check

Requires Python 3, Git, `file` and `pdftotext`; executes no target-repository code, mechanism, API, CI job, service or model. Run from a checkout containing the pinned commit. Outputs go to a temporary directory; the target commit is read from Git objects even when the working tree has this documentation patch.

```bash
python artifacts/qa/reports/dp-15-inventory-20261007/scan.py . c90836cdb7a34791669907053522de0458f21ae9 /tmp/kfm-dp15-raw
python artifacts/qa/reports/dp-15-inventory-20261007/classify.py . /tmp/kfm-dp15-raw /tmp/kfm-dp15-classified
cmp artifacts/qa/reports/dp-15-inventory-20261007/hits.csv.gz /tmp/kfm-dp15-classified/hits.csv.gz
cmp artifacts/qa/reports/dp-15-inventory-20261007/inventory.json.gz /tmp/kfm-dp15-classified/inventory.json.gz
cmp artifacts/qa/reports/dp-15-inventory-20261007/dp-declarations.json /tmp/kfm-dp15-classified/dp-declarations.json
```

The scan also emits the complete raw tree and decoded-representation manifests into the temporary output, allowing all 14,164 paths and every content digest to be audited. The checked-in tree digest binds the full enumerated source set. Binary type descriptions are observations from `file`; machine output may vary if extractor/tool versions change.

## Closure and rollback

Only DP-15 is marked `CLOSED — CURRENT_TREE_INVENTORY_ONLY` in the proposed standard patch. Closure means the previously unperformed recursive current-main inventory is complete with no hidden **identified** DP implementation; it does not grant semantic acceptance, dependency admission, a numeric budget, an operative mechanism, a ledger writer, runtime conformance, review/owner acceptance, release, deployment or publication. Fresh DP-bearing source or authority requires a successor inventory; this result is not a perpetual absence claim.

Revert the documentation/QA/receipt commit through ordinary review. No privacy budget exists or is refunded by this documentation change. Human review remains pending.
