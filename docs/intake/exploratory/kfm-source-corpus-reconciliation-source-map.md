<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/kfm-source-corpus-reconciliation-source-map
title: KFM Source Corpus - Current Repository Reconciliation Ledger
type: exploratory-intake-source-map
version: v0.2.0
status: triaged; repository-grounded; non-authoritative; campaign-in-progress
owners: ["@bartytime4life"]
created: 2026-08-15
updated: 2026-08-15
policy_label: public; intake; exploratory; evidence-reconciliation
truth_posture: cite-or-abstain; current-repository claims pinned to an exact main snapshot
owning_root: docs/
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 13f1a8e9bfbad807ab9131bd7c2972ed61a95918
repository_tree: 62f5206b538a7efa25373a34cb1635417407b1b3
issue: 2874
parent_tracker: 2768
related:
  - ./README.md
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ./comprehensive-research-verification-report-source-map.md
  - ../../registers/VERIFICATION_BACKLOG.md
tags: [kfm, intake, source-corpus, reconciliation, evidence-ledger, issue-2874]
notes:
  - "The supplied files remain read-only external source artifacts; this record stores identities and bounded dispositions, not their bodies."
  - "Merged PR #2877 remains the concise active-candidate register; this file is its source-identity and detailed-reconciliation companion."
  - "No source activation, promotion, release, deployment, publication, merge, or repository-setting change is authorized."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM source corpus - current repository reconciliation ledger

> **Outcome:** Pin the 28 supplied source artifacts, reconcile 18 major candidate clusters against `main@13f1a8e9bfbad807ab9131bd7c2972ed61a95918`, record three newer connected-Drive refinements, and remove duplicate, represented, superseded, blocked, or reference-only work from the active queue. Merged PR `#2877` remains the concise candidate register.

> [!IMPORTANT]
> This exploratory ledger is not doctrine, an ADR, source admission, EvidenceBundle, receipt, proof, release decision, or publication authority. Accepted ADRs, adopted Directory Rules, current contracts/schemas/policies/tests/workflows, and executable evidence outrank planning prose.

**Quick links:** [Checkpoint](#checkpoint) · [Placement](#placement) · [Sources](#sources) · [Drive](#drive) · [Ledger](#ledger) · [Selection](#selection) · [Validation](#validation) · [Rollback](#rollback)

<a id="checkpoint"></a>

## Campaign checkpoint

| Field | Evidence |
|---|---|
| Repository / main | `bartytime4life/Kansas-Frontier-Matrix@13f1a8e9bfbad807ab9131bd7c2972ed61a95918` |
| Main tree / tip | `62f5206b538a7efa25373a34cb1635417407b1b3`; merge PR `#2879`, `docs(wiki): polish Home landing page` |
| Placement authority | Accepted `ADR-0029`; adopted `docs/doctrine/directory-rules.md` |
| Parent / issue | `#2768` / `#2874` |
| Prior tranche | PR `#2877` merged `SC-001`-`SC-014` into `docs/registers/VERIFICATION_BACKLOG.md` |
| Concurrent work | Open PR `#2880` changes only `docs/wiki/Architecture.md` and its generated receipt; target paths are disjoint |
| Inherited exact-main failure | `validator-suite` run `31864536281`: `run-validators` failed at **Enforce repository workflow and topology ratchets**; fail-closed canary passed |
| Inherited exact-main failure | `schema-validation` run `31864536229`: fixture validation failed at **Validate configured aggregate fixture families**; inventory passed and later schema/contract tests were skipped |
| Selected change | One additive companion source map under `docs/intake/exploratory/`; no candidate-register rewrite |
| Release/publication effect | None |

The two exact-main failures predate this branch and are recorded without inferring a root cause. This documentation-only slice does not modify the failing workflows, validators, fixture families, schemas, topology baselines, or aggregate configuration.

<a id="placement"></a>

## Directory Rules and placement basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted by [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), make path selection an authority decision. The [intake README](../README.md) and [exploratory README](./README.md) establish `docs/intake/exploratory/` as the non-canonical waiting room for source maps and unresolved proposals. This file explains source identities and current dispositions; it creates no parallel contract, schema, policy, source, registry, receipt, proof, release, or publication home.

<a id="sources"></a>

## Supplied source census

`SHA-256` binds the exact bytes used in this reconciliation. Page counts apply to PDFs.

| ID | Supplied file | Bytes | Pages | SHA-256 | Disposition |
|---|---|---:|---:|---|---|
| S01 | `KFM_Directory_Governance_Standard_v2.0.0-draft.1.pdf` | 222,418 | 33 | `2b8db8901f893d9aabb94bb32db5cbc2e0bb0c881bf74068551e9b3b76602893` | `DIRECT` |
| S02 | `Kansas Frontier Matrix — AI Build Operating Contract.md` | 99,610 | — | `20cdee04ece6b1c84aea2f327675999f60d66cb5415d7f9ec5c99e310ebb0c59` | `DIRECT` |
| S03 | `# KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent.md` | 142,614 | — | `028998b9caed5df18eed4d8531b007ff545432a0b0689097487e6310dae13bd8` | `LINEAGE` |
| S04 | `GPT Markdown Prompt 4.0.pdf` | 366,446 | 39 | `0f9d8ba8a17619dadf6db6088df85d9841f3d8a5d88436ee26a888f911949a60` | `DIRECT` |
| S05 | `Kansas Frontier Matrix — Connected-Dots Architecture Brief.md` | 51,699 | — | `b1d79a368e219a500e7b861f42ecb2f100b00e5bbb48a6a13f9451871cd57da0` | `CORROBORATIVE` |
| S06 | `Unified Doctrine Synthesis.md` | 134,062 | — | `eaa80edf61177241379938e0f8d739812b541a96ae33b14e34cd45d882a3ba57` | `CORROBORATIVE` |
| S07 | `KFM Unified Doctrine Synthesis.md` | 126,116 | — | `1eb07fe8cceed546a1d26bdca8b542f8d96a197d799e66a3b47c75102f40d76b` | `DUPLICATE_VARIANT` |
| S08 | `Unified Implementation Architecture Build Manual.md` | 84,595 | — | `e92500f9b40007e8b69d183ecaa6247c542ffec25857875ecd2dbd00709785b1` | `LINEAGE` |
| S09 | `Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf` | 63,565 | 28 | `b28b0cba512b95c8c106a143acb65c89d384843ff313420b2429daa51f8fcf78` | `LINEAGE` |
| S10 | `# Kansas Frontier Matrix Implementation Reference.pdf` | 252,138 | 20 | `d948332b6c5bfcdd956cf6264f7bcb88d6881ac00ca8afc2534a02d288d4b3c2` | `LINEAGE` |
| S11 | `Repository Structure Guiding Document.md` | 119,619 | — | `afe08af316d1f89779bab0d39888cdc65ee989907806a4126c331c50e4a0aa3a` | `LINEAGE` |
| S12 | `Kansas Frontier Matrix Repository Structure Guiding Document.md` | 120,088 | — | `22f54412f85cf2f17f6c26b9aff67912a91a566b64cc83c440474c12150d930c` | `DUPLICATE_VARIANT` |
| S13 | `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` | 79,287 | 30 | `43d0c6fea4cc64edb87238a13ac49b639934a82dcef0fab2ef49217add0ba8cf` | `DIRECT` |
| S14 | `KFM_Briefing_to_System_Integration_Architecture.docx` | 407,195 | — | `68872f9226c4e4a288e888b51fb9d80c4a621a4d660ee36dd6fef7edb3c34c4e` | `DIRECT` |
| S15 | `KFM_Comprehensive_Research_and_Verification_Agenda.docx` | 77,198 | — | `c8749ba82be0107c8734aa4aa297c639bf6083582005c97b48d936f19ff9f0d7` | `DIRECT` |
| S16 | `KFM_Living_Compass_Working_Edition_1.0(1).docx` | 266,265 | — | `fa38a004587bbe145dc5b9a3945c7a1f471372ca2499538af81ec2066caa2d03` | `CORROBORATIVE` |
| S17 | `KFM_MapLibre_Operating_Architecture_Governed_UI_AI_Interaction_Manual_REVISED.pdf` | 582,496 | 22 | `77f56ec1ab632b76c7728cfb250330271b7dc8948db95c8c0594c92ad9ca6b36` | `DIRECT` |
| S18 | `maplibre3d.md` | 62,501 | — | `5148c85acaef7f299864df5b1804eb07498cb81ab4c4bcc39a9625287ee2817b` | `DIRECT` |
| S19 | `Master MapLibre Components-Functions-Features.pdf` | 1,592,794 | 554 | `309cf67311059c549e144ae9961b2f49eddf1caab8739a51b47ae88c2f5c1c90` | `CORROBORATIVE` |
| S20 | `kfm_soil_architecture_extended_pro_pdf_only_report.pdf` | 104,154 | 25 | `7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea` | `DIRECT` |
| S21 | `KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf` | 142,522 | 42 | `d334f43df8fd74f17115cc0f51861cf8238c9cb99d37adaf95f5e4e1655fdf51` | `DIRECT` |
| S22 | `kfm_encyclopedia.pdf` | 239,723 | 82 | `cc899a7a57cbadb5870709be07d9b0dbfd01712cd794d63dc4d640485970419a` | `CORROBORATIVE` |
| S23 | `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` | 1,939,390 | 509 | `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9` | `BACKLOG` |
| S24 | `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | 554,630 | — | `57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780` | `BACKLOG` |
| S25 | `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` | 3,301,956 | 1279 | `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639` | `BACKLOG` |
| S26 | `KFM_Full_Atlas_seed_cards.md` | 871,381 | — | `9a95ab510bd984c257a8c578f8646993c7fe55d76f7d3c5f60d8bb9ad04ec3a2` | `BACKLOG` |
| S27 | `Domain-Driven Design Reference.pdf` | 327,895 | 59 | `4406daa99ff0e3d58757d62d40358c9fd745f95137e99f14602659d0c3f54e55` | `REFERENCE_ONLY` |
| S28 | `AI_Concepts_Using_Python.pdf` | 3,368,044 | 435 | `cb6275b4bf2c44e5fc56b166b1161ceb859a1de0562462814ad5b8ad6fd111b6` | `REFERENCE_ONLY` |

Disposition rules: `DIRECT` may supply candidate pressure but not authority; `CORROBORATIVE` reinforces an existing boundary; `LINEAGE` preserves historical intent; `DUPLICATE_VARIANT` is byte-distinct but not a second implementation demand; `BACKLOG` is idea inventory; `REFERENCE_ONLY` supplies craft language only.

<a id="drive"></a>

## Newer connected-Drive refinements

Private links and provider identifiers are intentionally omitted.

| Drive title | Reconciliation | Disposition |
|---|---|---|
| `GPT Markdown Prompt 6.0` | Confirms v6 is the implementation-forward successor already represented by the current repository prompt family. | `SUPERSEDED` for v5 operational posture; no second prompt file |
| `KFM Curated Feature & Component Forge Agent` | Reinforces source-mining, collision checks, dependency closure, draft-PR delivery, and non-publication boundaries already used by `#2874`. | `CORROBORATIVE`; method only |
| `KFM_Comprehensive_Research_and_Verification_Report.docx` | Narrows the supplied research agenda; the existing repository source map already owns dated report reconciliation. | `PARTIAL`; do not re-import dated maturity claims |

<a id="ledger"></a>

## Detailed evidence ledger

Each row preserves every field required by issue `#2874`. Status vocabulary is `IMPLEMENTED`, `PARTIAL`, `ABSENT`, `SUPERSEDED`, `CONTRADICTED`, `BLOCKED`, or `NEEDS VERIFICATION`.

| ID | Candidate idea | Source | Intended outcome | Current repository evidence | Status | Authority conflicts | Safety / governance impact | Smallest useful next slice | Validation | Rollback |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Adopt and enforce Directory Rules v2 without creating parallel authority | S01 pp. 5-21; S11/S12 §§1-4; S15 C-01, C-03, C-06, C-10-C-14 | One writable placement authority, deterministic responsibility-root routing, machine projections, and… | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` is accepted and pins `docs/doctrine/directory-rules.md`;… | PARTIAL | S01 labels the standard proposed, but accepted ADR-0029 later adopted its exact bytes. S11/S12 are old-… | Prevents duplicate schema, policy, source, proof, release, and lifecycle homes;… | HOLD broad moves. Permit only file-specific convergence after consumer/reference inventory, path-decision evidence,… | Reverify adopted digest/blob; root and lane registers; path-alias and topology validators; Markdown… | Revert only the bounded migration or projection change. Do not roll back or rewrite the… |
| C02 | Make the inspectable claim, lifecycle law, and governed public… | S05 §§1-6; S06/S07 §§1-13; S08 §§0-4; S09 pp. 1-7; S13 pp. 3-7; S22 pp. 3-6 | Every consequential public claim resolves through evidence, policy, review, release, correction, and… | Repository-native doctrine and architecture include `docs/doctrine/lifecycle-law.md`, `docs/doctrine/encyclopedia.md`, `docs/architecture/trust-… | PARTIAL | Greenfield and docs-only sources cannot prove current implementation. Presence of doctrine, contracts,… | Keeps canonical/internal stores, generated prose, and rendered artifacts from becoming… | Do not add another broad doctrine document. Select a follow-up only when one exact released candidate can be traced… | Carrier assessment fixtures; governed-API boundary tests; EvidenceRef-to-EvidenceBundle resolution;… | Revert the bounded candidate proof or adapter change; preserve canonical evidence and… |
| C03 | Govern source admission separately from descriptor shape, activation,… | S02 §§20-21; S09 source-intake sections; S15 W04-W06; S20 §§3, 13-16; S21 §§4,… | No connector or watcher gains admitted lifecycle effect without a reviewed SourceDescriptor and… | `docs/adr/ADR-0017-source-descriptor-admission-process.md` remains proposed, while SourceDescriptor path convergence, SourceActivationDecision… | PARTIAL | Executable shape and fixture success do not authenticate source authority. Planning documents propose… | Prevents publicly accessible or technically valid feeds from silently becoming… | HOLD live activation. The next decision-bearing slice is source-admission authority and one fully reviewed source… | Descriptor schema/alias parity; activation negative fixtures; authority-register state; policy… | Deactivate or retire only the bounded source decision and connector route; preserve… |
| C04 | Use query-save-recompile as a governed improvement loop rather than… | S13 §§5-8, 16, 21-27; S05 §10; S06 §22; S16 Trails 16-22 | Questions, evidence resolutions, candidate deltas, validation, compilation, review, promotion, and… | Current main contains `contracts/governance/query_run_record.md`, `contracts/governance/recompile_manifest.md`, schemas/fixtures,… | PARTIAL | The source describes a broad loop; current evidence proves bounded records and deterministic generation,… | Prevents saved model output or repeated generated text from becoming canonical truth… | No broad loop implementation. Require a reproducible missing transition or consumer before adding another object; any… | Schema and fixture polarity; deterministic recompile manifest; digest/replay checks; denial of… | Revert the bounded contract/generator change and restore the prior manifest; no… |
| C05 | Treat recurring briefings as non-authoritative discovery signals | S14 §§1-11, 17-20, 25-28; S16 Trails 02-18 | Briefing prose becomes a typed, deduplicated internal signal that routes evidence-backed work without… | Current main contains `contracts/governance/briefing_signal.md`, `contracts/evidence/temporal_authority_envelope.md`, machine schemas, fixture… | PARTIAL | The first no-network object slices are represented. Live official-source verification, broad lane… | Reduces duplicate issue noise and prevents generated narratives from bypassing source,… | Do not recreate BriefingSignal or TemporalAuthorityEnvelope. A follow-up requires a concrete missing lane or current… | Signal determinism and duplicate tests; temporal-envelope tests; no-network workflow; issue-… | Revert the affected fixture/validator/contract slice; preserve source snapshots, issue… |
| C06 | Keep governed AI finite, evidence-bounded, and receipt-bearing | S02 §1 and §§20-24; S05 §§8-9; S06 §§18-21; S17 §§12-14; S28 as background only | AI adapters return bounded ANSWER/ABSTAIN/DENY/ERROR envelopes, resolve evidence and policy first, and… | Current main contains governed-AI architecture and boundaries, `policy/ai_builder/`, adapter contracts, a deterministic MockAdapter path,… | PARTIAL | The AI Build Operating Contract and source manuals include proposed operational realizations. Current… | Prevents fluent generation, hidden model reasoning, or direct model endpoints from… | HOLD live provider/model integration until evidence resolution, policy execution, citation validation, prompt… | MockAdapter finite outcomes; RuntimeResponseEnvelope schema/consumer compatibility; AIReceipt… | Disable or revert the adapter slice while preserving input evidence, receipts, denial… |
| C07 | Keep MapLibre, Evidence Drawer, and Focus Mode downstream of released… | S17 §§3-18; S19 pp. 3-15; S05 §§8-9 | A map interaction follows released layer -> candidate ID -> governed API -> EvidenceBundle -> Evidence… | Current main contains the Explorer shell boundary, MapLibre architecture and package scaffold, Evidence Drawer and Focus contracts,… | PARTIAL | The source's renderer architecture is represented, but ADR-0007 remains proposed and the MapLibre… | Prevents feature properties, pixels, popups, client filters, or model prose from… | Do not add a second UI trust model. Advance only through a current failing consumer or a same-candidate released-layer… | Explorer adapter-boundary tests; Evidence Drawer payload fixtures; Focus finite outcomes; MapLibre… | Revert the bounded adapter/UI slice and restore the prior released layer manifest; no… |
| C08 | Resolve the MapLibre-only browser renderer and governed 3D proposal | S18 §§0-11 and Appendix B; S17 §§10-16; S19 renderer/3D categories | One governed browser renderer family with explicit plugin/custom-layer admission, 2D evidence parity,… | `docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md` exists but remains `proposed`; current main has a placeholder… | BLOCKED | S18 says the ADR was not yet filed and assumes current external capability evidence; current repo now… | A premature 3D/plugin rollout would widen supply-chain, sensitive-location,… | Decision packet first: accept, reject, or narrow ADR-0007; select one physical package; pin the dependency; define… | ADR/index coherence; recursive dependency/acquisition scan; exact package pin and lock; six browser… | Remove the admitted plugin/runtime change and restore the prior package/lock/adapter… |
| C09 | Separate PMTiles/COG/GeoParquet structural integrity from cryptographic… | S09 §§7, 16-21; S17 delivery sections; S19 pp. 3-15; S23 REL/MAP; S24 PMTiles and… | Static geospatial carriers are deterministic, range-verifiable, manifest-bound, attestable, public-safe,… | Current main contains PMTiles attestation contracts/tests/workflow, partial-read/Merkle fixture profiles, a generated HOLD marker, GeoParquet… | PARTIAL | Source atlases sometimes collapse signatures, receipts, Merkle/range proof, catalog records, and… | Avoids treating a structurally valid archive or generated receipt as authentic,… | Prepare the PMTiles trust-closure decision packet: key/trust-root admission, verifier authority, failure semantics,… | Structural fixture tests; byte-range/Merkle verification; signature-negative tests; trust-root… | Revert only the trust integration or release candidate; keep historical… |
| C10 | Preserve soil support-type separation across survey, derivative,… | S20 pp. 4-25, especially §§8-16 and 20-24; S23 source/model/validation chapters | SSURGO/SDA, gridded derivatives, station moisture, satellite grids, pedons, and interpretations cannot… | Current main contains soil domain architecture, contracts including `support_type_profile.md`, `soil_moisture_observation.md`, and… | PARTIAL | S20 was a no-repo PDF plan and proposed a combined SSURGO/SDA + Mesonet + PMTiles first slice. Current… | Prevents false equivalence among static survey, modeled grids, in-situ sensors, and… | Do not recreate the planned thin slice wholesale. Reconcile any remaining SSURGO/SDA or Mesonet gap against existing… | Support-type profile workflow; soil-moisture and MUKEY fixtures; source-role negative cases; time-… | Revert the bounded soil profile/pipeline change, restore prior receipts/manifests, and… |
| C11 | Keep mineral occurrence, deposit, estimate, permit, production, and… | S21 pp. 7, 16, 19, 22; §§7-22 | Geology/resource records preserve source role, classification method, confidence, public-safe geometry,… | `docs/intake/exploratory/geology-natural-resources-architecture-source-map.md` already reconciles the report against current main. The bounded… | PARTIAL | The report's full path/schema/source plan is not authority. Current schemas remain permissive in places,… | Avoids overstating mineral/resource potential, exposing sensitive locations, or… | HOLD live sources and schema hardening until vocabulary, classification authority, rights, and stewardship are… | Resource-class positive/negative fixtures; exact-location denial; schema compatibility; source-role… | Revert the bounded fixture profile and receipt; no source, resource claim, or public… |
| C12 | Graduate fauna-habitat relations only through public-safe, evidence-… | S22 domain chapters; S23 POL/FIE/UIX; S24 cross-domain ideas; S25 domain and… | Fauna occurrence and habitat relations remain synthetic/candidate until evidence, geoprivacy, policy,… | Current main contains `contracts/cross_domain/fauna_habitat/public_safe_assignment_profile.md`, deterministic fixtures, validator, tests,… | PARTIAL | An `ALLOW` in the profile means `CANDIDATE_RELATION`, not canonical relation authority or public… | Protects rare-species precision and prevents an analytical join from becoming… | HOLD seam graduation until canonical relation authority, live geoprivacy transform, EvidenceBundle closure, review,… | Pair-specific fixture matrix; policy/generalization negatives; evidence reference resolution;… | Remove or supersede only the candidate relation profile/release; retain original… |
| C13 | Treat greenfield and historical repository-structure plans as lineage,… | S08-S12; S15 C-01-C-14 and W02-W04 | Use old plans to identify design intent while current accepted ADRs, current files, tests, and workflows… | Current main is a broad monorepo with established responsibility roots and substantial tracked implementation surfaces. ADR-0029 is the accepted… | SUPERSEDED | S09 assumes an empty repository; S10-S12 describe older snapshots and former ambiguities. Those current-… | Prevents destructive greenfield rewrites, duplicate roots, and reintroduction of… | No greenfield scaffold or broad structural migration. Use old plans only as proposal pressure and open file-specific… | Current recursive tree; accepted ADR/index; root registries; topology validator; open… | Close/revert the bounded structural PR and restore prior paths/aliases. Never rewrite… |
| C14 | Convert atlas and seed-card abundance into deduplicated, dependency-… | S22-S26; S16 Trails 02-22 | Stable ideas retain source lineage and IDs while only verified, owned, fixture-ready, reversible slices… | Current repo contains `docs/kfm_full_atlas_seed_cards.md`, intake indexes/registers, many per-idea source maps, contracts, validators, receipts,… | PARTIAL | S23-S26 were generated without current repo implementation proof and include overlapping category… | Reduces duplicate object families, oversized campaigns, and persuasive but unsupported… | Process by candidate cluster, not by document order. Require source location, current repo evidence, collision search,… | Stable-ID uniqueness; source-map links; duplicate/collision searches; exact path ownership;… | Close the candidate PR or mark the card/source map superseded; preserve source lineage… |
| C15 | Use the Comprehensive Research Agenda as a residue register, not… | S15 C-01-C-16; W01-W22; domain dossiers and appendices | Separate questions resolvable by external authority, repository/runtime inspection, governance decision,… | This session resolved many REPO-mode questions at `main@13f1a8e9...`: accepted Directory Rules, current object families, source-map conventions,… | PARTIAL | The agenda's document-only UNKNOWN posture is historically accurate but cannot be carried forward as… | Prevents web research from filling implementation gaps and prevents code presence from… | Split remaining items by mode and owner. Prioritize PMTiles trust closure, source rights/currentness for any proposed… | Each research item must retain primary source locator, version/access date, repo revision if… | Supersede only the resolved research item or decision packet; preserve the dated agenda… |
| C16 | Use the Living Compass to enforce narrow proof closure | S16 Trails 02-22 | Broad discovery remains separate from narrow experiments; proof maturity, hold conditions, source… | Issue #2874 requires candidate/source/repo/status/governance/next-slice/validation/rollback fields, and the existing intake/source-map pattern… | IMPLEMENTED | The Compass is guidance subordinate to accepted doctrine and repository controls; it does not create… | Prevents activity volume, document count, and idea novelty from being reported as proof… | Use it as review criteria for #2874; do not copy it into a second doctrine or control-plane surface. | Every selected slice has explicit non-goals, proof boundary, stop/hold conditions, validation, and… | Remove only this source-ledger interpretation if rejected; no operational state depends… |
| C17 | Converge AI/Markdown implementation prompts without treating prompts as… | S02-S04; S15 C-16 | AI agents may implement scoped repository work while remaining bounded by current user authority,… | Current main contains `docs/prompts/kfm-repository-build-markdown-modernization-agent.md`, `docs/prompts/ai-builder-system-prompts.md`,… | PARTIAL | S03 v5 is superseded operationally by S04 v6, while repository doctrine/prompt files retain mixed… | Prevents embedded prompts, issue text, or generated receipts from expanding… | Treat v5 as lineage; reconcile v6 against the current repo prompt and policy only through a separate prompt-authority… | Prompt version/identity; policy tests; terminal-state ceiling; no-force/no-merge/no-release checks;… | Restore the prior prompt/policy bytes and abandon the task branch; no release or… |
| C18 | Retain DDD and general AI texts as craft references only | S27 pp. 1-38; S28 pp. 77-84, 100-115, 146-170 | Use bounded contexts, ubiquitous language, layered isolation, data lifecycle, evaluation, and… | Current repo already has KFM-specific domain lanes, shared-kernel/responsibility-layer architecture, contracts, schemas, policies, validators,… | SUPERSEDED | These references do not define KFM paths, authority, source rights, sensitivity, lifecycle transitions,… | Prevents generic software/ML advice from weakening evidence, policy, sensitivity, or… | No direct PR. Cite these only as background when a KFM-specific design choice needs explanatory language and remains… | Trace any derived recommendation to a KFM contract/ADR/test; do not cite the reference as… | Remove the explanatory reference; no repository behavior or authority should depend on… |

<a id="selection"></a>

## Selection and dependency order

**Selected now:** one reconciliation-only draft PR adding this source map. It preserves merged PR `#2877` as the concise candidate register and selects no runtime, connector, policy, release, or publication object.

**Removed from the active queue:** second broad doctrine/connected-dots/encyclopedia/greenfield/MapLibre/soil/geology documents; wholesale atlas or seed-card translation; duplicate SourceDescriptor, query-save-recompile, briefing, Evidence Drawer, Focus Mode, PMTiles, soil, geology, fauna-habitat, RuntimeResponseEnvelope, or AIReceipt families; direct implementation from DDD/general-AI references; live source activation; 3D plugin admission; cryptographic trust; release, deployment, or publication.

**Dependency-ordered residue after review:**

1. classify the exact-main workflow/topology-ratchet and aggregate-fixture failures;
2. prepare a PMTiles trust-root/key/verifier/revocation decision packet without weakening the HOLD;
3. resolve source-admission authority and review one source's rights/currentness before activation;
4. resolve the MapLibre renderer decision, package home, dependency pin, plugin governance, and browser probes before 3D work; and
5. graduate fauna-habitat, governed AI, soil, geology, or briefing seams only when their recorded evidence, policy, release, correction, and rollback prerequisites close.

<a id="validation"></a>

## Validation and review boundary

Before review or merge, verify:

- the target was absent on the pinned base and the branch starts from exact `main@13f1a8e9bfbad807ab9131bd7c2972ed61a95918`;
- all 28 filenames, byte counts, PDF page counts, and SHA-256 values match the supplied artifacts;
- all 18 candidate rows contain every issue-required field and an allowed status;
- accepted ADR-0029 and adopted Directory Rules control placement;
- relative links and internal anchors resolve;
- open PR `#2880` remains disjoint or is re-reconciled if its scope changes;
- exact-main failures remain inherited unless later evidence proves otherwise;
- base-to-head comparison contains exactly this one additive Markdown file; and
- hosted checks are reported separately from local source validation.

Local authored-source checks for this file validate source hashes, candidate-field completeness, allowed statuses, anchor resolution, Markdown parsing, current checkpoint identifiers, and absence of stale checkpoint markers.

<a id="rollback"></a>

## Rollback and correction

Before merge, close the draft PR and abandon the branch. After an authorized merge, revert the single additive commit or delete this file through normal reviewed history. No canonical evidence, lifecycle object, contract, schema, policy, registry, receipt, proof, release, runtime, deployment, or public surface depends on it.

When evidence changes, preserve this dated revision as lineage, update only affected rows with a new repository SHA, rerun current-main/open-PR/exact-path/workflow/source-hash checks, and route any behavior change through its owning governed surfaces.

[Back to top](#top)
