<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-heavy-readme
title: fixtures/heavy/README.md — Heavy Runtime Stress Fixture Boundary
type: readme; directory-readme; heavy-runtime-fixture-lane; non-authoritative
version: v0.2
status: draft; repository-grounded; contract-aligned; direct-inventory-bounded; consumer-wiring-unverified; dedicated-ci-unestablished; non-authoritative
owners:
  - "@bartytime4life — verified GitHub CODEOWNER for /fixtures/ review routing"
  - "OWNER_TBD — semantic fixture stewardship and heavy-corpus admission ownership"
created: NEEDS VERIFICATION — file predates this revision
updated: 2026-07-21
supersedes: pre-contract heavy runtime fixture README
policy_label: public-doc; fixtures; heavy; synthetic-only; deterministic; no-network-default; public-safe; performance-governance; storage-decision-required; sensitivity-aware; release-subordinate; correction-aware; rollback-aware; no-publication
current_path: fixtures/heavy/README.md
truth_posture:
  CONFIRMED:
    - fixtures/heavy/README.md exists at the checked base
    - fixtures/ is the repository responsibility root for reusable runtime and synthetic fixture corpora
    - fixtures/ and tests/fixtures/ have documented distinct scopes
    - fixtures/slim/ is the preferred sibling lane when a small corpus can exercise the behavior
    - .github/CODEOWNERS routes /fixtures/ review to @bartytime4life
    - the Makefile fixtures target is TODO-only and the default test target does not execute this lane
  PROPOSED:
    - this lane admits only synthetic, public-safe, reproducible stress inputs whose declared consumer cannot be exercised adequately by fixtures/slim/ or a narrower domain or test-local owner
    - every substantive heavy corpus carries a machine-readable or equivalently reviewable manifest covering identity, generator, seed, hashes, size, storage, consumer, sensitivity, expected envelope, and retirement
    - performance consumers separate immutable fixture identity from environment-specific measurement artifacts
  UNKNOWN:
    - exhaustive tracked and generated payload inventory, ignored files, external corpus stores, active consumers, current benchmark results, required-check significance, branch-protection enforcement, and release dependency
  NEEDS_VERIFICATION:
    - accepted semantic owners and review separation
    - exact admission and repository-size thresholds
    - substantive payloads, active consumers, two-way backlinks, deterministic regeneration, nonempty collection, no-network enforcement, and dedicated CI ownership
evidence_state_qualifiers:
  CONFLICTED:
    - the repository contains three Directory Rules documents with overlapping authority claims; CONTRIBUTING.md directs live contribution preflight to docs/architecture/directory-rules.md
  NARROWED:
    - direct inventory and consumer conclusions are bounded to connector reads and indexed repository search, not a byte-complete recursive tree walk
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: aa8a350980eeac2c8834f1cd89c714878a46a650
  target_prior_blob: d74300b6b69360af491f36e83693b6cacf8d70bb
  related_repository_blobs:
    contributing: 935f8bbefd8f966275887c9f58277746b9c67c28
    directory_rules_live_preflight: 18653c00ba193a4afaa3e07a0924452807fb98ef
    directory_rules_doctrine_copy: 2affb080e6f0043867c64c7f06c1ca52030fbd55
    fixtures_root_readme: b096b0ed49c8e7d95ddb0d4c813d06ef40f1528d
    fixtures_slim_readme: f175ac21e849f405c47efd7f40f1f29968992930
    fixtures_golden_readme: b746ffff48d0bc50f0d1b7341b9306803ed1f5fe
    tests_fixtures_readme: 2d0147e85eae86f687e85c5bea0d3e61f9c3a8f7
    codeowners: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
    makefile: 51537af34ee065c2de571134688415042b83b22a
    workflows_readme: c3dfbe1168d405e7244c6a7dacf0e0616faf120e
notes:
  - "This revision changes documentation only."
  - "Heavy fixtures are stress inputs, not benchmark truth, proof, release authority, or publication material."
  - "README presence, filenames, hashes, or a successful load test do not prove semantic correctness, evidence closure, policy admissibility, release readiness, production capacity, or current-world accuracy."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `fixtures/heavy/` — heavy runtime stress fixtures

> **One-line purpose.** `fixtures/heavy/` holds synthetic, public-safe, reproducible runtime stress inputs only when `fixtures/slim/`, a domain-owned fixture lane, or a test-local fixture cannot exercise the declared behavior adequately.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-blue">
  <img alt="Lane: heavy stress input" src="https://img.shields.io/badge/lane-heavy__stress__input-purple">
  <img alt="Inventory: bounded" src="https://img.shields.io/badge/inventory-bounded-orange">
  <img alt="Network: denied by default" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture__only-red">
</p>

> [!IMPORTANT]
> Start with [`fixtures/slim/`](../slim/README.md). A heavy case is admitted only when its named consumer needs scale, density, cardinality, topology, tile count, layer count, zoom span, or memory pressure that a small reviewable fixture cannot represent.

> [!CAUTION]
> A load, render, throughput, memory, or benchmark result is an environment-bound observation. It is not source truth, semantic truth, evidence closure, policy approval, production capacity, release readiness, or publication authority.

> [!WARNING]
> Never commit real source extracts, private identities, living-person information, DNA or genomic material, sensitive exact geometry, archaeology locations, rare-species localities, critical-infrastructure detail, credentials, live alerts, or reverse-engineerable protected information to make a stress corpus feel realistic.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs here](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related folders](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed)

---

## Purpose

This lane supports reviewable stress scenarios for the governed runtime and its checking surfaces. It helps maintainers:

- exercise renderer and map-runtime behavior beyond smoke-test scale;
- test bounded memory, throughput, latency, tile loading, layer density, feature density, and zoom-range behavior;
- reproduce performance regressions with immutable synthetic inputs;
- distinguish fixture identity from generated measurements and reports;
- keep storage, generation, rights, sensitivity, correction, and retirement decisions visible; and
- avoid using lifecycle data, production snapshots, or public-release material as convenient test input.

This lane is not a general large-file directory. Size alone does not make a fixture heavy, and a heavy corpus does not belong here if a domain, object family, runtime package, or test subtree is the accepted narrower owner.

[Back to top](#top)

## Authority level

**Implementation-supporting fixture lane; non-authoritative for truth, evidence, policy, review, release, capacity, and publication.**

The live contribution guide directs placement preflight to [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md). Its responsibility-root rule places reusable valid, invalid, golden, and synthetic checking inputs under `fixtures/`; executable assertions remain under `tests/`; contracts, schemas, policy, lifecycle data, proofs, receipts, releases, generated artifacts, and public clients keep separate authority homes.

> [!NOTE]
> The repository contains overlapping Directory Rules copies. That document-authority conflict remains **CONFLICTED / NEEDS VERIFICATION**. This README does not resolve it or create another authority surface. The target path already exists under `fixtures/`, so this documentation-only revision adds no root, migration, or parallel fixture home.

| Responsibility | Owning surface | This lane's boundary |
|---|---|---|
| Small reusable runtime fixture | `fixtures/slim/` | Preferred unless scale is essential to the case. |
| Heavy cross-cutting runtime stress input | `fixtures/heavy/` | Own only with a named consumer and documented scale need. |
| Domain-owned stress case | `fixtures/domains/<domain>/` | Preferred when domain meaning, policy, or sensitivity context is material. |
| Test-local fixture | `tests/fixtures/` or the owning test subtree | Use when the case exists only for one test area. |
| Executable test or benchmark harness | `tests/`, `tools/`, or an accepted package-owned test lane | Heavy files are inputs, not assertions or harness code. |
| Object meaning | `contracts/` | Fixtures imitate accepted meaning; they do not define it. |
| Machine shape | `schemas/` | Fixtures exercise schemas; they do not create schemas. |
| Policy and admissibility | `policy/` | Fixtures may exercise decisions; they do not decide policy. |
| Lifecycle data | `data/` | Heavy fixtures never replace or shortcut governed lifecycle lanes. |
| Measurements and generated reports | accepted temporary or `artifacts/` QA locations | Environment-bound results do not become fixture authority. |
| Release and rollback decisions | `release/` | Fixture or benchmark success never approves release. |
| Public runtime and maps | governed API, UI, and released map surfaces | Fixtures are not public APIs, maps, tiles, scenes, or products. |

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Heavy fixtures remain outside that lifecycle. Promotion is a governed state transition, never the consequence of a fixture load or benchmark pass.

[Back to top](#top)

## Status

| Evidence field | Current bounded result |
|---|---|
| Repository snapshot | `bartytime4life/Kansas-Frontier-Matrix` at `main@aa8a350980eeac2c8834f1cd89c714878a46a650` |
| Prior README blob | `d74300b6b69360af491f36e83693b6cacf8d70bb` |
| Path placement | **CONFIRMED** — existing child of the reusable `fixtures/` responsibility root. |
| Direct tracked inventory | **NARROWED / NEEDS VERIFICATION** — connector reads and indexed search did not provide a byte-complete recursive directory listing. |
| Direct consumer inventory | **NEEDS VERIFICATION** — indexed search did not establish an executable consumer of this lane. |
| Review route | **CONFIRMED** — `.github/CODEOWNERS` maps `/fixtures/` to `@bartytime4life`; required-review enforcement remains **UNKNOWN**. |
| Fixture regeneration | **CONFIRMED TODO-only** — the root `Makefile` fixture target prints a readiness marker. |
| Default test target | **CONFIRMED** — the root target runs schema and contract tests, not this lane. |
| Dedicated heavy-fixture CI | **NOT ESTABLISHED** — broad pull-request workflows exist, but no named heavy-corpus consumer or gate was confirmed. |
| Repository-size threshold | **NOT ESTABLISHED** — no accepted byte threshold was found in the bounded inspection. |
| Lane-specific accepted ADR | **NOT ESTABLISHED** — no accepted heavy-fixture ADR was found in the bounded ADR and repository search. |

### Safe conclusions

- **CONFIRMED:** the README, its parent fixture contract, and its slim and golden sibling guidance exist at the pinned commit.
- **CONFIRMED:** root `fixtures/` and `tests/fixtures/` document distinct reusable and test-local scopes.
- **CONFIRMED:** `/fixtures/` has a GitHub review-routing entry.
- **PROPOSED:** this lane is an exception path for scale-dependent, cross-cutting runtime stress inputs, not the default fixture home.
- **UNKNOWN:** exhaustive payload inventory, ignored or externally stored corpora, active consumers, current results, branch-protection rules, required checks, and release dependency.
- **NEEDS VERIFICATION:** exact size thresholds, accepted storage backends, semantic owners, consumer backlinks, deterministic regeneration, and dedicated validation.

### Maturity matrix

| Capability | Status | Evidence-bounded conclusion |
|---|---:|---|
| Directory README | `CONFIRMED` | A routing and boundary surface exists; this revision aligns it to the required folder-README order. |
| Direct heavy payloads | `NOT ESTABLISHED` | No byte-complete payload inventory was available. |
| Named executable consumers | `NOT ESTABLISHED` | No consumer was confirmed by bounded indexed search. |
| Deterministic generator | `NOT ESTABLISHED` | Required before substantive use. |
| Corpus manifest and hashes | `NOT ESTABLISHED` | Proposed admission contract below; no accepted schema was found. |
| No-network enforcement | `NOT ESTABLISHED` | Required posture; executable proof was not found. |
| Storage decision | `NOT ESTABLISHED` | Required before a large binary or external corpus is admitted. |
| Dedicated CI collection | `NOT ESTABLISHED` | Broad workflows do not prove this lane is exercised. |
| Benchmark authority | `DENIED` | Results remain environment-bound observations. |
| Release authority | `DENIED` | Fixtures never approve promotion or publication. |

[Back to top](#top)

## What belongs here

Material may be admitted only when it is synthetic or demonstrably public-safe, deterministic or reproducibly generated, reviewable, and tied to a declared scale-dependent consumer.

Examples include:

- synthetic PMTiles, MLT, vector-tile, GeoJSON, JSON, JSONL, SVG, YAML, or Markdown stress inputs;
- MapLibre runtime and in-adapter 3D-mode cases for feature density, layer density, tile count, zoom ranges, camera movement, style changes, attribution display, or bounded rendering pressure;
- generalized public-safe geometries created specifically for repeatable load testing;
- toy governed-API, Evidence Drawer, or Focus Mode envelopes repeated at stress scale without introducing real evidence or protected content;
- deterministic generators, pinned seeds, canonicalization profiles, checksums, and reviewable generation notes;
- corpus manifests recording purpose, owner, consumer, size, storage, rights, sensitivity, expected runtime envelope, and retirement posture;
- compact expected summaries or pointers to [`fixtures/golden/`](../golden/README.md) when a stable comparison is appropriate; and
- small sampling or inspection aids needed to review a larger external corpus without copying that corpus into Git.

### Admission gate

A proposed case must answer all of these questions before payload admission:

1. Why can `fixtures/slim/` not exercise the behavior?
2. Why is no domain, object-family, package, or test-local lane the narrower owner?
3. Which exact executable consumer loads the corpus?
4. Which scale dimension is essential: bytes, features, layers, tiles, topology, zoom span, concurrency, memory pressure, or another declared dimension?
5. How is the corpus generated or obtained, normalized, hashed, reviewed, corrected, and retired?
6. What prevents network access, ambient credentials, current time, local state, or live-source drift from changing the run?
7. What storage decision keeps ordinary repository review and clone behavior safe?
8. What finite result means collected, skipped, unsupported, failed, or passed without overstating production capacity?

If any answer is missing, keep the proposal out of this lane and mark it **NEEDS VERIFICATION**.

[Back to top](#top)

## What does NOT belong here

- A large file whose only justification is convenience, realism, or future use.
- Any fixture that remains practical in [`fixtures/slim/`](../slim/README.md).
- Domain-owned or test-local cases with a clearer accepted owner.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle data.
- Real source exports, production snapshots, live upstream responses, current-world caches, logs, or canonical/internal store copies.
- Sensitive exact geometry, protected cultural or sovereign material, living-person data, DNA or genomic material, rare-species locations, archaeology sites, critical-infrastructure detail, credentials, secrets, or private endpoints.
- Actual SourceDescriptors, EvidenceBundles, receipts, proofs, policy decisions, review records, release manifests, correction notices, or rollback cards.
- Contracts, schemas, policy rules, validators, benchmark harnesses, application code, renderer adapters, or executable tests.
- Generated metrics, traces, screenshots, flame graphs, rendered tiles, build products, or CI reports; these belong in declared temporary or generated-output locations.
- Public API payloads, public maps, public tiles, public scenes, release artifacts, or material presented as authoritative.
- A parallel browser-renderer fixture authority. Current Directory Rules identify MapLibre as the sole browser-side renderer; any incompatible architecture change requires its own accepted decision path.
- Opaque binary corpora that cannot be regenerated, sampled, hashed, licensed, sensitivity-reviewed, or removed safely.
- Duplicate copies of externally stored corpora or golden outputs created only for discoverability.

[Back to top](#top)

## Inputs

### Minimum corpus manifest

Before admitting a substantive corpus, record these fields in an accepted manifest format or equivalently explicit review note. The field set is **PROPOSED** until a schema and owner are accepted.

| Field | Required meaning |
|---|---|
| `scenario_id` | Stable toy identity; never a production or source-system identifier. |
| `purpose` | Behavior or risk the corpus exercises. |
| `heavy_justification` | Why a slim or narrower fixture cannot represent the case. |
| `consumer` | Exact test, validator, benchmark, runtime check, or documentation harness. |
| `scale_dimensions` | Bytes, records, features, layers, tiles, zooms, topology, concurrency, or other bounded dimensions. |
| `generator` | Pinned script, version, parameters, and deterministic seed, or a reviewed public-safe acquisition recipe. |
| `normalization` | Canonicalization applied before hashing and comparison. |
| `content_hashes` | Hashes for the manifest, generated corpus, and any immutable external object. |
| `format_versions` | Declared format, schema, contract, and compatibility versions where applicable. |
| `rights` | License or synthetic-generation posture and permitted repository/test use. |
| `sensitivity` | Review result, generalization, redaction, or denial rationale. |
| `storage` | Git, approved LFS, or approved immutable external storage decision; never an unpinned mutable URL. |
| `expected_envelope` | Bounded, environment-labeled expectations and finite outcomes. |
| `network_posture` | Denied by default; any exception needs explicit scope and review. |
| `owner_and_reviewers` | Fixture owner plus affected runtime, domain, security, rights, or sensitivity reviewers. |
| `correction_and_retirement` | How to replace, revoke, quarantine, or delete the corpus and update consumers. |

### Generation and identity rules

- Prefer a small deterministic generator and manifest over a large opaque checked-in payload.
- Pin generator version, dependency lock, seed, locale, timezone, coordinate reference system, ordering, float normalization, compression settings, and timestamps when they can affect bytes.
- Use toy IDs, toy refs, toy geometries, toy timestamps, toy hashes, and synthetic metadata.
- Regeneration must not depend on live KFM source systems, canonical stores, public APIs, ambient credentials, or the current clock.
- Hash the normalized content and fail closed on a mismatch. A filename or remote object key alone is not identity.
- If external storage is approved, pin an immutable object version and digest, document access and retention, and provide a small public-safe review sample where permitted.
- Do not invent a repository-size threshold in this README. Until an accepted threshold and storage owner exist, any corpus too large for ordinary review requires an explicit maintainer decision before commit.

[Back to top](#top)

## Outputs

This lane may support:

- reusable immutable stress inputs;
- deterministic corpus manifests, hashes, and generation notes;
- compact expected summaries or references to golden expectations;
- finite collection states such as `COLLECTED`, `SKIPPED`, `UNSUPPORTED`, `FAILED`, or `PASSED`; and
- reproducible inputs for renderer, runtime, governed-API, drawer, Focus Mode, or performance-governance checks.

Consumers may generate timing samples, throughput summaries, memory profiles, rendered images, tile traces, diff reports, or failure diagnostics. Those results are environment-bound outputs and must go to the accepted temporary or generated-output location, not back into this fixture lane by default.

Every result must identify at least:

- corpus and manifest hashes;
- consumer revision;
- runtime, operating system, architecture, dependency, and hardware context material to interpretation;
- warm-up, iteration, concurrency, cache, and network posture;
- success, skip, and failure counts; and
- whether the observation is local, CI, reference-hardware, or another explicitly named profile.

No output from this lane admits a source, resolves an EvidenceRef, approves policy, creates a receipt or proof, promotes lifecycle data, establishes production capacity, changes release state, or authorizes publication.

[Back to top](#top)

## Validation

### Current executable boundary

- The root `Makefile` target for fixtures is TODO-only; it does not regenerate or validate this lane.
- The root default test target executes schema and contract tests, not `fixtures/heavy/`.
- Broad pull-request workflows exist, but their presence does not prove that a heavy fixture is collected or consumed.
- The inspected documentation-build and link-check workflows are explicit readiness holds; a green held job does not prove README rendering or link validity.
- No dedicated heavy-corpus generator check, hash check, manifest validator, no-network check, consumer-backlink check, orphan detector, or benchmark gate was confirmed.

### Required pre-admission checks

1. **Placement:** confirm heavy scale is essential and no narrower owner applies.
2. **Inventory:** list every tracked payload, generator, manifest, external object, and consumer backlink.
3. **Reproducibility:** regenerate twice in clean, no-network environments and compare normalized hashes.
4. **Public safety:** inspect samples and metadata for real or sensitive material; fail closed when rights or sensitivity are unclear.
5. **Storage:** verify the accepted storage decision, clone/review impact, immutable identity, access path, retention, and removal path.
6. **Format:** run applicable schema, contract, container, tile, geometry, and corruption checks without treating them as semantic truth.
7. **Collection:** prove at least one intended consumer collects the case; zero collected, all skipped, or unsupported must not report success.
8. **Backlinks:** link manifest to consumer and consumer to manifest; reject orphans and duplicate scenario IDs.
9. **Measurement:** separate fixture validity from performance thresholds and label environment-bound results.
10. **Correction:** dry-run replacement or retirement so consumers fail visibly rather than silently selecting stale input.

### Performance-governance rules

| Concern | Required posture |
|---|---|
| Baseline | Pin corpus, consumer, environment profile, and comparison method. |
| Variability | Report distribution or repeated observations; do not promote a single timing to benchmark truth. |
| Threshold | Name owner, rationale, tolerance, and expiry or review trigger. |
| Cache | Declare cold, warm, mixed, or disabled state. |
| Network | Denied by default; local fixture loading must not silently fall back to live services. |
| Missing capability | Report `UNSUPPORTED` or `SKIPPED` with reason; do not convert it to pass. |
| Empty collection | Fail explicitly. Zero cases is not success. |
| Regression | Preserve the failing fixture and result long enough for review, but store generated evidence in the appropriate artifact location. |
| Improvement | Re-run on the same pinned profile before changing a threshold or expected envelope. |
| Release use | Treat as one review signal only; never as sole release authority. |

### README validation performed for this revision

- Confirmed the twelve required directory-README headings appear once and in the mandated order.
- Confirmed internal relative link targets used by this revision existed at the pinned base where connector reads were available.
- Confirmed this is a one-file documentation change after remote comparison.
- Did not claim fixture regeneration, payload validation, benchmark execution, or dedicated consumer coverage.

[Back to top](#top)

## Review burden

`.github/CODEOWNERS` routes `/fixtures/` changes to `@bartytime4life`. This is a verified GitHub review route, not proof of semantic ownership, completed review, independent approval, or branch-protection enforcement.

Review must include owners for every materially affected responsibility:

- fixture stewardship for admission, identity, pairing, and retirement;
- the named test, runtime, renderer, API, or performance consumer;
- domain stewardship when domain meaning or policy context is present;
- rights, privacy, sovereignty, cultural, ecological, archaeology, infrastructure, or living-person reviewers when applicable;
- security review for storage, network, decompression, path traversal, archive, parser, or generated-output risk;
- repository maintainers for large-file, LFS, or external-storage impact; and
- release or correction stewardship only when the check is referenced by a governed release process.

| Change class | Minimum review concern |
|---|---|
| README-only clarification | Fixture owner and affected documentation owner. |
| New generator or manifest | Fixture owner, consumer owner, security review, reproducibility evidence. |
| New checked-in heavy payload | Explicit repository-size/storage decision plus rights and sensitivity review. |
| New external corpus | Immutable identity, access, retention, license, availability, and rollback review. |
| Threshold or expected-envelope change | Consumer owner, comparison evidence, reason, and rollback target. |
| Domain or sensitive scenario | Domain and applicable policy/sensitivity reviewers; deny when required review is unavailable. |
| Release-gating use | Separate release authority and documented failure/rollback behavior. |

Do not approve bulk re-recording, threshold relaxation, corpus replacement, or a new storage dependency merely because a check failed. Review the behavioral reason and the old-to-new evidence.

[Back to top](#top)

## Related folders

| Path | Relationship |
|---|---|
| [`fixtures/README.md`](../README.md) | Parent fixture-root authority boundary and lane index. |
| [`fixtures/slim/README.md`](../slim/README.md) | Preferred home for small runtime and smoke-test fixtures. |
| [`fixtures/golden/README.md`](../golden/README.md) | Stable expected-output guidance; keep heavy expected outputs compact where practical. |
| [`fixtures/domains/README.md`](../domains/README.md) | Domain fixture parent; prefer a domain owner when meaning or sensitivity is domain-specific. |
| [`tests/fixtures/README.md`](../../tests/fixtures/README.md) | Unit-test-scoped fixture boundary; not the cross-cutting runtime corpus home. |
| [`contracts/README.md`](../../contracts/README.md) | Semantic meaning; heavy fixtures do not define contracts. |
| [`schemas/README.md`](../../schemas/README.md) | Machine shape; heavy fixtures do not define schemas. |
| [`policy/README.md`](../../policy/README.md) | Admissibility and sensitivity rules; fixture examples do not decide policy. |
| [`artifacts/README.md`](../../artifacts/README.md) | Generated-output boundary; measurements and reports are not fixture authority. |
| [`Makefile`](../../Makefile) | Current root command surface; the fixture target is TODO-only at the evidence snapshot. |
| [`.github/workflows/README.md`](../../.github/workflows/README.md) | Workflow inventory and trigger/permission posture; no dedicated heavy-lane consumer was established. |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) | Live contribution-preflight placement guidance, including the required README contract. |
| [`docs/registers/DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Repository drift register; it did not record the overlapping Directory Rules identity conflict at the inspected snapshot. |
| [`docs/adr/README.md`](../../docs/adr/README.md) | ADR lifecycle and index; accepted lane-specific authority remains unestablished. |

[Back to top](#top)

## ADRs

No accepted ADR specific to `fixtures/heavy/`, its storage threshold, or an external corpus authority was established by the bounded inspection. Absence from indexed search is not proof that no relevant ADR exists; treat the result as **NOT ESTABLISHED / NEEDS VERIFICATION**.

The current Directory Rules conflict is also unresolved: `CONTRIBUTING.md` directs live preflight to `docs/architecture/directory-rules.md`, while overlapping lowercase doctrine and uppercase architecture copies remain in the repository. This README follows the live preflight direction and does not try to settle document identity.

An ADR is required before a heavy-fixture change:

- adds, removes, renames, or changes the authority class of a repository root;
- creates a parallel fixture, benchmark, schema, policy, proof, receipt, data, release, or publication authority;
- establishes a new repository-wide LFS or external-corpus authority with governance consequences;
- changes the lifecycle, trust membrane, sole-browser-renderer, publication, or watcher-as-non-publisher invariant; or
- changes object meaning rather than merely supplying an example.

Routine README corrections, manifest additions, generator fixes, and properly scoped fixture updates normally require a focused reviewed pull request, not a new ADR, unless they cross one of those boundaries.

[`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) governs schema placement and reinforces the separation between machine shape and fixture examples. It does not authorize a heavy corpus, storage backend, benchmark threshold, or release gate.

[Back to top](#top)

## Last reviewed

| Field | Value |
|---|---|
| Review date | `2026-07-21` |
| Evidence base | `main@aa8a350980eeac2c8834f1cd89c714878a46a650` |
| Review scope | Target README, parent and sibling fixture guidance, test-fixture boundary, Directory Rules README contract, contribution guide, CODEOWNERS, Makefile, workflow inventory and selected PR workflows, drift register, ADR index, and bounded indexed searches. |
| Inventory limit | No byte-complete recursive tree, ignored-file inventory, external-store inventory, runtime trace, benchmark run, or branch-protection proof was available. |
| Next scheduled review | By `2027-01-21`, or earlier on any trigger below. |

Review this README immediately when:

- a payload, generator, manifest, consumer, expected summary, storage backend, or size threshold is added or changed;
- a fixture becomes domain-owned, test-local, slim enough for ordinary review, externally stored, deprecated, or unconsumed;
- a benchmark threshold becomes release-significant;
- a Directory Rules or ADR decision changes fixture placement, MapLibre runtime boundaries, LFS, or external-storage governance;
- a rights, sensitivity, provenance, security, or public-safety concern appears;
- CI begins collecting this lane, stops collecting it, reports zero cases, or changes required-check status; or
- six months pass without a documented review.

### Correction and rollback

For a documentation-only revision, rollback is a normal revert of the scoped commit. For a corpus change:

1. stop consumers from selecting the suspect corpus;
2. preserve the manifest, hashes, failure signal, and affected consumer revisions for review;
3. quarantine or remove prohibited material from ordinary access, recognizing that Git history and external caches may require a security-led purge procedure;
4. restore the last reviewed corpus or fail closed if none is safe;
5. update generator, manifest, hashes, consumers, expectations, and backlinks together;
6. record the correction reason, affected results, and retirement status; and
7. re-run deterministic, no-network, collection, and sensitivity checks before re-admission.

Do not rewrite public repository history or delete an external object casually. If secrets, protected data, or material legal/sovereignty risk enters history, stop normal fixture work and use the repository's incident and credential-revocation path.

### Open verification register

| Item | Status | Closure evidence |
|---|---|---|
| Complete tracked and generated child inventory | `NEEDS VERIFICATION` | Byte-complete recursive inventory plus ignored/generated/external-store review. |
| Active consumers and two-way backlinks | `NEEDS VERIFICATION` | Executable consumer references scenario ID and manifest; manifest names consumer. |
| Heavy admission and repository-size thresholds | `NEEDS VERIFICATION` | Accepted maintainer decision, policy, or ADR with owners and rollback. |
| Deterministic generator and hash enforcement | `NEEDS VERIFICATION` | Two clean no-network regenerations with identical normalized hashes. |
| Rights and sensitivity review | `NEEDS VERIFICATION` | Recorded public-safe review for every substantive corpus. |
| Storage, retention, access, and retirement | `NEEDS VERIFICATION` | Approved immutable storage decision and tested removal/recovery procedure. |
| Dedicated validation and nonempty collection | `NEEDS VERIFICATION` | Named CI job fails on corruption, hash drift, orphan, zero collected, and all skipped. |
| Semantic owners and required-review enforcement | `NEEDS VERIFICATION` | Accepted stewardship record and verified branch-protection behavior. |
| Current performance results | `UNKNOWN` | Environment-labeled run tied to pinned corpus and consumer hashes. |
| Release dependency | `UNKNOWN` | Accepted release contract names the check and preserves independent release authority. |

[Back to top](#top)
