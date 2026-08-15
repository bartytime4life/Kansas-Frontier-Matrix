<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://register/source-corpus-reconciliation-2026-08-15
title: KFM Source-Corpus Reconciliation Ledger — 2026-08-15
type: evidence-ledger
version: v1.0
status: draft; repository-grounded; non-authoritative; issue-2874-tranche
owner: "NEEDS VERIFICATION — review routes through current CODEOWNERS; no independent corpus steward was verified"
created: 2026-08-15
updated: 2026-08-15
policy_label: repository-facing
owning_root: docs/
responsibility: >-
  Record a dated, human-readable reconciliation between supplied KFM source
  proposals and exact current repository evidence without creating source,
  policy, lifecycle, release, or publication authority.
truth_posture: >-
  CONFIRMED current repository paths, baseline SHA, accepted Directory Rules,
  inspected pull requests, issue state, and exact-head workflow stage /
  PROPOSED rankings and next-slice recommendations / UNKNOWN uninspected
  runtime, deployments, settings, source rights, and steward decisions /
  NEEDS VERIFICATION hosted results for this draft branch and every deferred
  authority-bearing candidate.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 5971a181ed345e7de49cccf71611d51c0d54121a
  exact_head_validator_suite_run: 31908776480
  active_overlap_prs: [2923, 2924, 2927]
related:
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/registers/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - CONTRIBUTING.md
  - control_plane/verification_backlog.yaml
  - issues/2874
  - issues/2768
notes:
  - "This dated packet is subordinate to the canonical human verification backlog and issue #2874."
  - "It does not project accepted governance into control_plane/; that register remains separately governed."
  - "No source file, Google Drive artifact, source endpoint, repository setting, lifecycle store, release, deployment, or publication surface is modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Source-Corpus Reconciliation Ledger — 2026-08-15

> **Campaign outcome:** one bounded governance/documentation slice is selected:
> preserve the current source-to-repository reconciliation as a dated,
> inspectable packet. No trust-bearing feature slice is selected while active
> pull requests own overlapping EvidenceBundle work and the exact-main aggregate
> validator still fails in the repository-topology ratchet.

## 1. Goal, authority, and evidence boundary

This packet supports issue `#2874`. It turns the supplied PDFs, Markdown
manuals, Drive documents, accepted repository doctrine, current contracts,
schemas, policies, tests, workflows, recent merges, open pull requests, and
exact-head workflow evidence into a ranked implementation ledger.

It is **not** a new source of truth. It is subordinate to:

1. accepted ADRs and the adopted Directory Rules;
2. current contracts, schemas, policy, registries, validators, tests, workflows,
   and executable behavior;
3. current authoritative repository documentation;
4. accepted or current Drive material;
5. planning reports, atlases, manuals, seed cards, draft standards, and
   greenfield plans as proposal sources only.

### Exact repository baseline

| Field | CONFIRMED result |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Baseline | `main@5971a181ed345e7de49cccf71611d51c0d54121a` |
| Baseline commit | Merge of PR `#2925`, People/DNA/Land EvidenceBundle projection |
| Accepted placement authority | `ADR-0029` plus `docs/doctrine/directory-rules.md` |
| Current human ledger | `docs/registers/VERIFICATION_BACKLOG.md` |
| Current machine projection | `control_plane/verification_backlog.yaml`, still `entries: []` |
| Exact-main inherited failure | `validator-suite` run `31908776480`, failing at `Enforce repository workflow and topology ratchets`; the fail-closed canary passed |
| Open overlap | Draft PRs `#2923` (roads/rail/trade), `#2924` (settlements/infrastructure), and `#2927` (hazards) |
| Runtime/deployment/source activation | `UNKNOWN`; not exercised |
| Drive mutation | None |

### Directory Rules basis

`docs/registers/` owns human-readable governance registers and dated
verification views. This file records a current reconciliation packet; it does
not redefine the canonical verification backlog, create a machine authority, or
admit a new object family. `control_plane/` remains the home for machine
projections of accepted governance, not for a self-authorizing copy of this
draft.

## 2. Source coverage and authority treatment

| Source family | Representative source and locator | Treatment in this run |
|---|---|---|
| Directory governance | *KFM Directory Governance Standard v2.0.0-draft.1*, cover and §§1–7 | The source's adoption proposal is **SUPERSEDED** by accepted ADR-0029; post-adoption topology convergence remains partial. |
| Pipeline and trust spine | *Pipeline Living Implementation Manual v0.3*, pp. 3–7 and §§8, 16–17 | Proposal/lineage source. Existing query, evidence-resolution, change-proposal, and recompile families control implementation claims. |
| Briefing integration | *Briefing-to-System Integration Architecture*, pp. 2–7 and §§3–11, 19, 27 | Proposal source. The repository already has a broad deterministic/read-only foundation; do not create a second family. |
| Evidence and public claims | *Connected-Dots Architecture Brief* §§2–6; *Unified Doctrine Synthesis* §§3–13 | Doctrine synthesis. Shared EvidenceBundle and EvidenceRef repository surfaces control exact implementation. |
| MapLibre/UI | *MapLibre Operating Architecture*, pp. 3–7 and §§5–8, 12–14 | Doctrine/proposal. Explorer Web remains a bounded downstream shell; no direct store or direct model path is admitted. |
| Soil | *Soil Architecture Extended Pro*, pp. 4–8 and §§8–20 | Proposal/lineage. Current Soil contracts, profiles, fixtures, validators, tests, and workflows control exact support vocabulary. |
| Geology/resources | *Geology & Natural Resources Architecture*, pp. 3–7 and §§7–18 | Proposal/lineage. Current shared projection and exact-location controls bound implementation. |
| Map artifacts | *Master MapLibre Components-Functions-Features*, pp. 3–5 and tile/provenance chapters | Proposal backlog. Structural PMTiles/COG proof does not establish signer trust, policy approval, release, or publication. |
| Whole-system/greenfield | *Definitive Greenfield Building Plan v1.1*, §§2, 7.29–7.33 | The empty-repository premise is **CONTRADICTED/SUPERSEDED** by current repository evidence; object-family ideas remain individually reconcilable. |
| Atlases and seed cards | Pass 18, Pass 20, consolidated Domains Atlas, Encyclopedia, Full Atlas seed cards | High-recall proposal indexes. They do not prove current implementation or authorize paths. |
| General references | *Domain-Driven Design Reference*; *AI Concepts Using Python* | Reference only. They support modeling/testing language but do not independently justify a KFM PR. |
| Drive refinements | Newer KFM planning/build documents found by Drive search, including briefing and idea-integration material | Read-only corroboration. No Drive document was found that outranks accepted ADR-0029 or current repository behavior. |

## 3. Ranked candidate ledger

Statuses apply only to the bounded outcome described in each row.

| Rank / ID | Candidate and source location | Current repository evidence and status | Governing authority, owning root, dependencies | Rights, sensitivity, security, publication | Acceptance, disposition, and proposed PR boundary |
|---:|---|---|---|---|---|
| 1 / `RC-001` | **Current source-corpus reconciliation packet.** User campaign contract; issue `#2874`; prior tranche in `docs/registers/VERIFICATION_BACKLOG.md`. | Prior ledger predates current domain projection merges, PR `#2926`, and current open overlap. **PARTIAL** before this packet. | ADR-0029; `docs/registers/` owns the human view. Depends on exact baseline, source locators, PR/issue overlap, and failure classification. | Repository-facing only; no sensitive payloads or live sources. No release/publication effect. | **SELECTED.** Add this dated packet plus one generated authoring receipt. Accept when final bytes are hash-bound, changed paths are exactly two, links/metadata are valid, and hosted results are read back. Rollback: revert the two-file packet. |
| 2 / `RC-002` | **Repository-topology ratchet repair.** Directory Standard §§5–7; Research Agenda W02–W03. | Exact-main aggregate validator fails at the topology ratchet; focused domain workflows can still pass. **NEEDS VERIFICATION** at exact offending paths. | Accepted Directory Rules; likely `control_plane/`, `tools/validators/`, tests, and affected roots. Requires root-by-root ownership, consumer graph, migration/rollback, and no broad cleanup. | Potential authority and compatibility impact; no destructive move without ADR/migration proof. | **DEFER.** First capture exact validator output and isolate one monotonic violation reduction. One PR per independently reversible path family. |
| 3 / `RC-003` | **Complete shared EvidenceBundle projection convergence.** Connected-Dots §§2–6; Pass 20 shared-kernel idea; domain atlas evidence sections. | Soil, Geology, Flora, Fauna, Habitat, Agriculture, Atmosphere, Archaeology, and People/DNA/Land bounded projections are on current main. Roads/Rail/Trade, Settlements/Infrastructure, and Hazards are owned by open draft PRs `#2923`, `#2924`, `#2927`. Broader resolver/authentication remains **PARTIAL**. | Shared contract/schema under evidence roots; domain schemas are projections; focused validators/tests/workflows. | Domain-specific sensitivity remains upstream. A schema-valid bundle is not authenticated evidence or release permission. | **DEFER/OVERLAP.** Do not duplicate active PRs. After their disposition, verify registry/consumer closure rather than creating another projection family. |
| 4 / `RC-004` | **Source authority-resolution and snapshot-read profile.** Greenfield §7.29; Research Agenda W05; Pipeline source-registry sections. | SourceDescriptor/activation shapes exist. PR `#2926` adds a no-network Kansas transportation assessment profile but does not admit sources. **PARTIAL / BLOCKED**. | `contracts/source/`, `schemas/.../source/`, fixtures, validators, tests; source authority and policy decisions remain separate. | Rights, redistribution, sensitivity, precision, identity, and steward authority remain unresolved; live activation denied. | **DEFER.** Next slice may authenticate one read-only metadata snapshot with no lifecycle write, credential, or source activation. |
| 5 / `RC-005` | **Briefing official-source snapshot verification.** Briefing architecture §§3–11, 19, 27. | BriefingSignal, TemporalAuthorityEnvelope, issue/read, source-snapshot candidate, evidence-chain, and obligation propagation already exist. **PARTIAL**. | Existing briefing contracts/schemas/fixtures/validators/tests/workflows. Depends on source admission and evidence resolution. | Generated briefing prose remains non-authoritative; no direct path to evidence, mutation, release, or public truth. | **PROPOSED HOLD.** One authenticated read-only source snapshot only after source authority and credential handling are closed. |
| 6 / `RC-006` | **Governed Explorer client-to-Evidence Drawer interaction.** MapLibre manual §§5–8; Whole-System Build Reference UI plane. | Explorer Web has a fail-closed static entrypoint, bounded feature slices, payload schemas, and boundary tests, but no proven end-to-end public interaction. **PARTIAL**. | `apps/explorer-web/`, governed API contract, shared/domain EvidenceBundle projections, policy/citation finite outcomes, accessibility tests. | Must not expose internal stores, raw feature properties, denial reasons, or sensitive geometry. | **DEFER.** Select one already modeled public-safe domain only after EvidenceRef resolution and policy/citation behavior are executable. |
| 7 / `RC-007` | **PromotionReceipt producer and ordered A–G readiness binding.** Greenfield §§2, 7.31; Research Agenda C-08. | Contract/schema/fixtures/validator/tests/workflow exist; policy/review are inactive or fixture-only. **PARTIAL / BLOCKED**. | Promotion and receipt families; legitimate producer; generated-receipt integrity; policy/review authority. | A passing fixture is not approval, transition, release, or publication. | **DEFER.** Repair only a verified producer binding or vocabulary conflict; do not create another gate family. |
| 8 / `RC-008` | **CatalogMatrix aggregate registration.** Greenfield catalog closure; Master MapLibre catalog chapters. | Four bounded profiles exist; broad schema/generic entrypoint and aggregate registration remain incomplete. **PARTIAL / BLOCKED**. | Catalog contracts/schemas/validators, aggregate registry, STAC/DCAT/PROV parity, receipt integrity. | Catalog description is not proof, policy, review, release, or publication. | **DEFER.** First clear the exact topology/receipt blocker; then register existing profiles with focused aggregate-selection regression coverage. |
| 9 / `RC-009` | **Governed query-save-recompile executor.** Pipeline v0.3 §§16–17. | QueryRunRecord, EvidenceResolutionRecord, AIChangeProposal, and inactive RecompileManifest exist; no authorized writer or reviewer. **PARTIAL / BLOCKED**. | Existing control-loop families; policy, review, destination authorization, correction, rollback, and write executor. | No private chain-of-thought; no autonomous canonical mutation or publication. | **REJECT FOR THIS CAMPAIGN.** Requires a separate authority decision and complete write/review/rollback contract. |
| 10 / `RC-010` | **PMTiles/COG cryptographic trust and signer admission.** Greenfield §§7.30–7.32; Master MapLibre pp. 3–5. | Structural manifests, byte-range and shape-only carrier checks exist; admitted trust roots and cryptographic verification do not. **PARTIAL / BLOCKED**. | Release, proof, signing, policy, verifier authority, signer registry, correction, rollback. | Key/trust-root admission and release authorization are security-significant. | **DEFER TO DECISION PACKET.** No new structural fixture until signer/verifier authority is decided. |
| 11 / `RC-011` | **Soil support-type and shared-evidence convergence.** Soil report §§8–20. | Shared EvidenceBundle projection and persisted one-positive-fixture-per-eight-support-types coverage are on current main. Bounded fixture claim **IMPLEMENTED**; live lane **PARTIAL**. | Current Soil contract/profile/schema/fixtures/validator/tests/workflow. | No live NRCS/Mesonet/NOAA/NASA activation; rights and publication remain held. | **NO NEW PR.** Next work requires a specific validator gap or admitted source, not more speculative fixtures. |
| 12 / `RC-012` | **Geology anti-collapse and public-safe geometry.** Geology report §§7–18. | Shared EvidenceBundle projection and focused public-safe/role surfaces exist. Bounded shape claim **IMPLEMENTED**; end-to-end lane **PARTIAL / NEEDS VERIFICATION**. | Current geology schemas, policy, validators, tests, and docs. | Boreholes, wells, samples, resources, and sensitive exact locations remain fail-closed. | **DEFER.** Refresh one verified path/shape conflict only; no live source or public-location exposure. |
| 13 / `RC-013` | **MapLibre-only browser renderer.** `maplibre3d.md` §§0–2. | MapLibre code and capability profiles exist; Cesium compatibility surfaces remain; the proposed renderer ADR is not accepted. **PARTIAL / NEEDS VERIFICATION**. | Accepted ADR required for dependency retirement; import/consumer/capability comparison and rollback. | Plugin supply chain, license, performance, and sensitive 3D geometry require review. | **HOLD.** Produce a current zero-consumer/capability decision packet before removing a renderer dependency. |
| 14 / `RC-014` | **Live governed-AI provider.** MapLibre manual §§12–14; AI Build Contract §§20–23. | MockAdapter and finite response envelopes exist; live provider, effective policy/citation execution, and public route do not. **PARTIAL / BLOCKED**. | Evidence resolution, policy, citation, AIReceipt, adapter, telemetry, governed route. | Model output is never evidence or release authority; prompt/data exposure and source terms require review. | **REJECT FOR THIS CAMPAIGN.** Close evidence/policy/citation boundaries first; retain no-network MockAdapter. |
| 15 / `RC-015` | **Greenfield root tree and broad scaffold expansion.** Greenfield Plan §§3–7. | Current repository is a large established monorepo with adopted Directory Rules and many existing families. Empty-start assumption **SUPERSEDED / CONTRADICTED**. | Current repository and accepted ADRs outrank the plan. | Broad scaffolding can create parallel authority and dead paths. | **REJECT.** Reconcile individual object-family gaps only; never copy the proposed tree wholesale. |
| 16 / `RC-016` | **Generic DDD/AI-library modernization.** DDD Reference; *AI Concepts Using Python*. | No KFM-specific acceptance gap was established from these references alone. **UNKNOWN / REFERENCE ONLY**. | Must attach to a verified KFM contract, test, performance, or architecture need. | Generic model/ML work can create uncited derived claims or new dependencies. | **REJECT AS STANDALONE WORK.** Use only as supporting craft evidence inside a repository-grounded slice. |

## 4. Ideas already implemented, superseded, or contradicted

### Implemented within bounded scopes

- Shared EvidenceBundle projection patterns are present for nine domain lanes on
  the baseline; three more lanes are owned by current draft PRs.
- Soil's eight declared support types each have a persisted positive synthetic
  fixture under the existing inactive profile.
- Briefing intake has deterministic, read-only, non-authoritative foundations.
- Query/evidence/change/recompile object families exist in a no-write,
  no-network posture.
- Promotion, CatalogMatrix, PMTiles/COG, MapLibre, MockAdapter, and Explorer
  surfaces have meaningful bounded fixtures or code, but not end-to-end
  authority closure.

### Superseded or contradicted

- The Directory Standard PDF's `PROPOSED FOR ADOPTION` label is superseded by
  accepted ADR-0029.
- Greenfield documents' empty-repository assumption is contradicted by current
  repository evidence.
- Earlier repo snapshots and route/path claims are lineage only when they differ
  from current main.
- Proposals that create a second CandidateDelta, EvidenceBundle, gate family,
  source registry, schema home, policy home, catalog home, or public-client
  trust path are rejected unless an accepted migration decision explicitly
  requires them.

## 5. Selection decision

Only `RC-001` is implemented in this campaign.

The stop conditions for additional PRs are active:

- open PRs already own the remaining obvious domain projection gaps;
- exact-main aggregate validation has an inherited topology failure whose exact
  path set must be isolated before repair;
- source activation, signer trust, live AI, writer authority, renderer
  retirement, and public-client claim delivery require decisions or dependency
  closure not established in this run;
- creating a second ledger, object family, or authority home would weaken
  governance.

## 6. Validation and acceptance plan

### Performed in this connector session

- refreshed `main` immediately before branch creation;
- inspected accepted ADR-0029 and the adopted Directory Rules;
- inspected the register lane contract, current verification backlog, machine
  backlog projection, contribution rules, and generated-receipt schema;
- searched open PRs, recent merged PRs, active issues, and issue `#2874`
  checkpoints;
- inspected exact-main workflow and job stages for the inherited validator
  failure;
- searched Drive for newer KFM material and treated it read-only;
- checked that no open PR owns this new dated ledger path.

### Repository-native checks required on the branch

```bash
python tools/validators/validate_docs_links.py \
  docs/registers/SOURCE_CORPUS_RECONCILIATION_2026-08-15.md
python tools/validators/check_doc_metadata.py \
  docs/registers/SOURCE_CORPUS_RECONCILIATION_2026-08-15.md
python tools/validators/check_docs_stale.py
python tools/validators/validate_docs_graph.py
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-source-corpus-reconciliation-20260815.json \
  --repo-root .
git diff --check
```

No local command result is claimed because no mounted checkout was available.
Hosted exact-head results must be read back and classified separately.

### Acceptance criteria

1. Branch starts from the exact baseline in §1.
2. Changed paths are exactly this packet and its generated receipt.
3. The receipt hash matches the final Markdown bytes.
4. No source, contract, schema, policy, workflow, lifecycle, release, runtime,
   deployment, publication, or repository setting changes.
5. The pull request remains draft.
6. Introduced failures are zero or explicitly repaired; inherited topology
   failures remain separately identified.
7. Issue `#2874` remains open.

## 7. Security, rights, sensitivity, and publication impact

This packet contains repository metadata, proposal classifications, and public
source-document locators only. It contains no credentials, private endpoint,
restricted source payload, living-person record, DNA/genomic record, precise
archaeological or rare-species location, infrastructure vulnerability, or
private-land join.

No source is admitted or activated. No lifecycle object is promoted. No release,
deployment, publication, access widening, or public-client behavior is created.

## 8. Rollback and non-effects

Before merge, close the draft pull request and delete its task branch. After any
separately authorized merge, revert the two-file packet. No data migration,
source shutdown, cache invalidation, release withdrawal, deployment rollback,
public correction, or Drive cleanup is required.

This packet does not close issue `#2874`, accept a proposed ADR, alter the
canonical verification backlog, populate the machine backlog, authenticate
evidence, approve policy, authorize a reviewer, or make any source-derived idea
public truth.
