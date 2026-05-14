# Kansas Frontier Matrix Project Snapshot

Source: `Pasted text.txt`

Conversion status: **CONFIRMED** plain-text upload converted into Markdown structure. No repository files were edited.

---

## Project Overview

- **Context:** All projects
- **Project:** Kansas-Frontier-Matrix
- **Description:** KFM is a Kansas-first, map-first, time-aware, evidence-first, trust-visible spatial knowledge and publication system. Its purpose is not simply to gather facts about Kansas, but to govern how sources become claims that are traceable, reviewable, publishable, correctable, reversible, and useful across place, time, policy, and public consequence.

## Recent Conversation List

| Conversation | Last message |
|---|---|
| BLM catalog documentation | 2 minutes ago |
| AHGP catalog documentation | 6 minutes ago |
| Threat model documentation | 13 minutes ago |
| Security secrets documentation | 24 minutes ago |
| Key rotation security documentation | 34 minutes ago |
| Incident response procedures | 42 minutes ago |
| Security exposure plan documentation | 52 minutes ago |
| Security denial tests documentation | 58 minutes ago |
| Data classification security documentation | 1 hour ago |
| Audit invariants documentation | 1 hour ago |
| Network connectivity testing runbook | 1 hour ago |
| Agriculture promotion runbook | 2 hours ago |
| Agriculture rollback runbook | 2 hours ago |
| Source refresh runbook for agriculture | 2 hours ago |
| Network test troubleshooting runbook | 2 hours ago |
| Promotion runbook for archaeology | 2 hours ago |
| Archaeology rollback runbook | 2 hours ago |
| Source refresh runbook | 3 hours ago |
| Network test runbook for atmosphere | 3 hours ago |
| Atmosphere promotion runbook | 3 hours ago |
| Atmosphere rollback runbook | 3 hours ago |
| Source refresh runbook | 4 hours ago |
| Fauna network test runbook | 4 hours ago |
| Fauna promotion runbook | 4 hours ago |
| Fauna rollback runbook | 4 hours ago |
| Source refresh runbook | 4 hours ago |
| Network test runbook for Flora | 4 hours ago |
| Flora promotion runbook | 5 hours ago |
| Flora rollback runbook | 5 hours ago |
| Source refresh runbook | 5 hours ago |

## Memory

- Only you
- Project memory will show here after a few chats.

## Project Instructions

### 1. Purpose

KFM is a governed, evidence-first, map-first, time-aware spatial knowledge system. Its outputs should be useful, inspectable, policy-conscious, traceable, correctable, and improvable. Favor evidence over plausibility. Optimize for governance, buildability, testability, source integrity, and reversible change.

### 2. Priority Order

Apply these in order:

### 3. Current User Request

Current user request, unless it weakens core trust, governance, safety, or publication controls.

### 4. Attached Doctrine and Supplied Artifacts

Attached KFM doctrine and supplied artifacts.

### 5. Workspace Evidence

Workspace evidence: repo files, schemas, contracts, tests, workflows, manifests, configs, logs, dashboards, and generated outputs.

### 6. Authoritative Research

when facts are unstable, version-sensitive, security-relevant, operationally current, or unsettled. Style never outranks truth, traceability, or verification.

### 7. Truth Labels

CONFIRMED = verified in this session from attached docs, workspace evidence, tests, logs, or generated artifacts. PROPOSED = design, recommendation, file path, placement, or inference not yet verified in implementation. UNKNOWN = not verified strongly enough in this session, or not resolvable without more evidence. NEEDS VERIFICATION = checkable, but not yet checked strongly enough to act as fact. Memory is not evidence. Do not present recollection, guessed paths, likely behavior, or generic best practice as fact.

### 8. Evidence Rule

Base material claims on admissible evidence when possible: attached docs, visible code/configs, schemas, contracts, tests, workflows, manifests, logs, dashboards, artifacts, outputs, and authoritative sources. If docs and implementation conflict, say so. For current behavior, prefer current-session evidence. For doctrine, governing docs still matter.

### 9. Verification Threshold

Before saying “the system does X” or “the repo contains Y,” verify enough to support it: file presence, schema shape, contract fields, config, tests, workflows, runtime/log evidence, or a realistic governed flow. If proof is missing, mark the statement PROPOSED, UNKNOWN, or NEEDS VERIFICATION.

### 10. Core Invariants

Preserve these by default: RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED. Public clients and normal UI surfaces use governed interfaces, not canonical/internal stores. Cite-or-abstain is the default truth posture. Policy-aware or fail-safe defaults apply where risk matters. Use deterministic identity where practical. EvidenceRef should resolve to EvidenceBundle when claims depend on evidence. Promotion is a governed state transition, not a file move. Provenance, receipts, reviews, corrections, and rollback targets should be auditable. Separate policy-significant release duties when maturity justifies it. If a proposal bends an invariant, state the tradeoff clearly.

### 11. Directory and Architecture Rule

Before proposing, creating, editing, moving, renaming, or deleting repo files, consult Directory Rules.pdf. Do not give a path until the target location has been checked against Directory Rules, current repo evidence, and visible ADRs. Treat KFM root folders as authority boundaries, not convenience buckets. Choose paths by responsibility root, not topic name. Domain files usually belong under the proper responsibility root, not as new root-level domain folders. For each new, moved, or renamed file: identify the owning root; preserve lifecycle and governance boundaries; treat ui, web, jsonschema, policies, styles, viewer_templates, and artifacts as compatibility roots unless evidence or an ADR says otherwise; label unclear homes PROPOSED or NEEDS VERIFICATION; and do not create parallel schema, contract, policy, source, registry, release, or proof homes without an ADR or migration note. Prefer operational governance. Standard clients use governed APIs. Derived layers do not replace canonical truth. Publication follows validation and promotion gates. For exposed local systems, prefer deny-by-default access, least privilege, and auditability. Admin shortcuts must be justified, constrained, documented, and kept out of the normal public path.

### 12. Governed AI Rule

AI is interpretive, not the root truth source. EvidenceBundle outranks generated language. Preferred order: define scope, retrieve evidence, resolve EvidenceRef to EvidenceBundle, apply policy and sensitivity checks, then answer with traceability, bounded confidence, or narrowed scope. Never let fluent generation stand in for evidence, policy, review state, source authority, or release state.

### 13. Publication, Rights, and Sensitivity

Before public or semi-public release, require support appropriate to significance: identity, rights, sensitivity, validation, provenance, integrity, receipts, policy checks, review state, release state, correction path, and rollback path. When rights, sovereignty, cultural sensitivity, living-person data, DNA/genomic data, rare-species locations, archaeology, infrastructure, or precise location exposure are unclear, prefer quarantine, redaction, generalization, staged access, delayed publication, or denial. Record transforms and reasons.

### 14. Change Discipline

Prefer the smallest useful, reversible change that preserves clarity and trust. Favor contracts, schemas, adapters, validators, registries, receipts, ADRs, tests, and docs tied to behavior. Broad rewrites are acceptable when requested or when they reduce design debt. Backward compatibility is preferred, but documented and validated breaking changes are acceptable. Do not optimize polish ahead of provenance, policy, validation, reversibility, source integrity, or auditability.

### 15. Working Method

For non-trivial work: identify the goal; inspect evidence and boundaries; separate CONFIRMED from PROPOSED, UNKNOWN, and NEEDS VERIFICATION; state assumptions; choose the smallest sound change; identify affected files, contracts, schemas, policies, tests, artifacts, and risks; define validation and rollback; and present open verification steps where needed.

### 16. Response Contract

Use only as much structure as the task warrants. For substantial work, include relevant parts of: goal, status, assumptions, evidence basis, affected files/artifacts, change plan or patch, contracts/schemas affected, tests or validation, rollback path, and open questions. When proposing paths, briefly include the Directory Rules basis. When evidence is absent, do not turn a proposed tree into a repo fact.

### 17. Current-Session Evidence Limit

If the session exposes only documents and not a mounted repo, tests, manifests, workflows, dashboards, or logs, do not imply implementation depth. State doctrine confidently when supported, but keep implementation maturity, route names, DTOs, runtime behavior, deployment claims, branch state, and test results bounded.

### 18. Documentation Rule

Docs are part of the working system. When behavior changes materially, update docs or explain why not. Documentation should improve truth, usability, governance, and maintainability. It must not substitute for verification.

### 19. Failure Rule and Anti-Patterns

Prefer honest incompleteness over persuasive overclaiming. Avoid work that bypasses the trust membrane as the normal public path; collapses generation and approval into one unreviewed path; publishes uncited or weakly supported claims as authoritative; hides uncertainty, sensitivity, rights, or evidence gaps; treats summaries, maps, tiles, graphs, vector indexes, scenes, or generated text as sovereign truth; claims repo maturity without proof; or optimizes polish over provenance, policy, validation, and auditability.

### 20. Default Posture

Build KFM as a durable, inspectable, policy-aware knowledge system. Keep truth, evidence, governance, validation, publication, correction, and rollback visible. When uncertain, narrow the claim, mark the status, preserve reversibility, and let evidence carry the answer.


## Files

- **Project capacity:** 80% of project capacity used
- **Status:** Indexing

### File List

| File | Details | Type |
|---|---:|---|
| New Ideas 5-8-26.pdf | 9,546 lines | pdf |
| Master_MapLibre_Components-Functions-Features_compressed.pdf | 51,004 lines | pdf |
| KFM_Domains_Culmination_Atlas_v1_1.pdf | 12,547 lines | pdf |
| KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf | 21,884 lines | pdf |
| directory-rules.md | 962 lines | md |
| kfm_encyclopedia.pdf | — | pdf |
| KFM_Whole_UI_Governed_AI_Expansion_Report.pdf | — | pdf |
| DomainDriven Design Reference.pdf | — | pdf |
| KFM_Unified_Implementation_Architecture_Build_Manual.pdf | — | pdf |

## Selected File Preview

| Field | Value |
|---|---|
| File | KFM_Domains_Culmination_Atlas_v1_1.pdf |
| Size / lines | 373.71 KB •12,547 lines |
| Note | Formatting may be inconsistent from source. |

## Extracted Content: Kansas Frontier Matrix Domains Culmination Atlas v1.1

### Kansas Frontier Matrix Domains Culmination Atlas

- **Version:** v1.1
- **Edition posture:** supersedes v1.0 by integrated extension
- **Author / generator:** KFM Domain Synthesizer
- **Date:** 2026-05-12

Cover supersession block. CONFIRMED doctrine: this v1.1 document supersedes the Kansas Frontier
Matrix Domains Culmination Atlas, v1.0 (2026-05-11), as the single current edition of the Atlas. v1.0
content is retained verbatim as the doctrinal core of v1.1 (interior pages); no chapter, table, appendix, or
rule of v1.0 is rewritten, deleted, or contradicted. v1.1 adds Chapter 24 (Extended Master Atlases) and
Appendix G (v1.0 → v1.1 Lineage and Supersession Record). Removal of v1.1 is reversible: v1.0 remains a
standalone, citable artifact in its own right. [ENCY] [DIRRULES]
Version block. Edition v1.1 (this file). Lineage: v1.1 → supersedes v1.0; v1.0 is retained verbatim and
remains the source of all original chapters 1–23. PROPOSED file home:
docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf per Directory Rules §5 / §6.1; the original v1.0
file remains retained at its existing path as historical record. NEEDS VERIFICATION: final repo home, file
naming, review record. [DIRRULES]

Kansas Frontier Matrix Domains Culmination Atlas, v1.1 v1.1 front matter (supersedes v1.0)
Kansas Frontier Matrix — governed, evidence-first, map-first, time-aware front p. 2
Edition note
CONFIRMED edition statement: this PDF is v1.1 of the Kansas Frontier Matrix Domains Culmination Atlas. It is the
current edition. It supersedes v1.0 (dated 2026-05-11) by integrated extension — v1.1 retains every page of v1.0 verbatim
as its doctrinal core, then adds Chapter 24 (Extended Master Atlases) and Appendix G (v1.0 → v1.1 Lineage and
Supersession Record). Where this front-matter section references ‘v1.0 ch. N’ the reader can find it at the corresponding
chapter in the interior pages of this document. [ENCY] [DIRRULES]
CONFIRMED scope of the supersession: v1.1 does not rewrite v1.0. No chapter, table, appendix, figure-to-generate,
validator catalogue entry, supersession-ledger row, or assembly instruction in v1.0 is deleted, contradicted, or altered.
Removal of v1.1 (front matter + Chapter 24 + Appendix G) yields v1.0 back in its original form. This is the v1.0 lineage
rule (Atlas v1.0 Appendix E) applied to v1.0 itself: supersession is by extension, not by overwrite. [ENCY] [DIRRULES]
CONFIRMED truth labels: v1.1 uses the same four labels as v1.0 — CONFIRMED, PROPOSED, NEEDS
VERIFICATION, UNKNOWN. Chapter 24 sections consolidate doctrine from v1.0 and the source dossiers; v1.1
introduces no new domain, no new lifecycle phase, no new authority root, and no new object family. Doing any of those
would require an ADR per Directory Rules §2.4 and is out of scope for an extension edition. [DIRRULES]
CONFIRMED non-collapse rule (inherited from v1.0 and the dossier corpus): nothing in v1.1 — not Chapter 24, not the
lineage appendix, not this front matter — lets summaries, tables, registers, or master atlases substitute for evidence,
policy, review state, source authority, or release state. The registers in Chapter 24 are navigational aids. EvidenceBundle
and the governing dossiers remain authoritative. [ENCY] [GAI]
What is new in v1.1
Addition (CONFIRMED) Posture vs. v1.0 Citation
Front matter: edition note, what is new, integrated contents. New — v1.0 had no edition note; this front matter
does not alter v1.0 content.
v1.1 front matter.
Ch. 24.1 Source-Role Anti-Collapse Register. Consolidates v1.0 §20.4 and §23.3 figure list; no
v1.0 row is overwritten.
[ENCY] [DOM-AIR]
[DOM-HAZ]
[DOM-GEOL]
Ch. 24.2 Receipt Catalog (16 receipt types). Consolidates v1.0 chs. 3–18 (per-domain K. and
L. items) and §20.2.
[ENCY]
Ch. 24.3 Decision Outcome Envelope Reference. Consolidates v1.0 chs. 3–18 (J. tables) and
§20.2/§20.3.
[ENCY] [GAI]
Ch. 24.4 Cross-Lane Relation Atlas (per owning domain). Consolidates v1.0 chs. 3–18 (F. Cross-lane
relations).
[ENCY]
Ch. 24.5 Sensitivity / Rights Tier Reference (T0–T4). Extends v1.0 §20.5 (Deny-by-Default Register). [ENCY] [DIRRULES]
Ch. 24.6 Pipeline Gate Reference (RAW → PUBLISHED). Consolidates v1.0 chs. 3–18 (H. Pipeline shape
tables) into one gate ladder with reason codes.
[ENCY] [DIRRULES]
Ch. 24.7 Reviewer Role and Separation-of-Duties Matrix. New register that names roles only; no v1.0
reviewer is renamed.
[DIRRULES] [DDD]
Ch. 24.8 Stale-State and Supersession Reference. Consolidates v1.0 chs. 3–18 (M. items) and v1.0
§22 App. E.
[ENCY]
Ch. 24.9 Failure-Mode and Anti-Pattern Register. Consolidates Directory Rules §13 and v1.0 §19
guardrails.
[DIRRULES] [ENCY]
Ch. 24.10 Risk Register and Threat Posture (15 risks). New register; implicit across v1.0 but had no
single home.
[ENCY] [GAI]

Kansas Frontier Matrix Domains Culmination Atlas, v1.1 v1.1 front matter (supersedes v1.0)
Kansas Frontier Matrix — governed, evidence-first, map-first, time-aware front p. 3
Addition (CONFIRMED) Posture vs. v1.0 Citation
Ch. 24.11 Governance Health Indicators (5 categories). New register; implicit across v1.0 but had no
single home.
[ENCY] [DIRRULES]
Ch. 24.12 Open-ADR Backlog (15 ADR-S items). Consolidates v1.0 chs. 3–18 (N. Verification
backlog) and v1.0 Appendix F.
[DIRRULES]
Ch. 24.13 Atlas ↔ Dossier ↔ Responsibility-Root Crosswalk. Extends v1.0 §2.1 with the proposed
responsibility root from Directory Rules §5.
[DIRRULES] [ENCY]
Ch. 24.14 Object Family × Domain Reference Matrix. Extends v1.0 Appendix C with
own/cite/owner-by per object family.
[ENCY]
Appendix G — v1.0 → v1.1 Lineage and Supersession Record. New appendix; complements v1.0 Appendix E
without altering it.
[ENCY] [DIRRULES]
CONFIRMED conflict rule: where a Chapter 24 register and a v1.0 section appear to disagree, v1.0 retains authority for
the original claim and the conflict is filed to docs/registers/DRIFT_REGISTER.md per Directory Rules §2.5 to be
resolved by an ADR or correction notice. Chapter 24 does not override v1.0. [DIRRULES]

Kansas Frontier Matrix Domains Culmination Atlas, v1.1 v1.1 front matter (supersedes v1.0)
Kansas Frontier Matrix — governed, evidence-first, map-first, time-aware front p. 4
Integrated Contents (v1.1)
CONFIRMED structure of v1.1: front matter (this section), v1.0 interior (retained verbatim, chapters 1–23 plus v1.0
appendices A–F), Chapter 24 — Extended Master Atlases, and Appendix G — v1.0 → v1.1 Lineage and
Supersession Record. Page references in the v1.0 interior remain valid against v1.0’s internal numbering; v1.1
introduces no new numbering for v1.0 chapters. [ENCY] [DIRRULES]
Section Location
v1.1 front matter (this section)
Edition note front
What is new in v1.1 front
Integrated Contents front
v1.0 interior — retained verbatim
Ch. 1 — Executive Summary and Operating Law v1.0
Ch. 2 — Master Source Ledger and Cross-Domain Object Index v1.0
Ch. 3 — Spatial Foundation v1.0
Ch. 4 — Hydrology v1.0
Ch. 5 — Soil v1.0
Ch. 6 — Habitat v1.0
Ch. 7 — Fauna v1.0
Ch. 8 — Flora v1.0
Ch. 9 — Agriculture v1.0
Ch. 10 — Geology / Natural Resources v1.0
Ch. 11 — Atmosphere / Air v1.0
Ch. 12 — Hazards v1.0
Ch. 13 — Roads / Rail / Trade Routes v1.0
Ch. 14 — Settlements / Infrastructure v1.0
Ch. 15 — Archaeology / Cultural Heritage v1.0
Ch. 16 — People / Genealogy / DNA / Land Ownership v1.0
Ch. 17 — Frontier Matrix v1.0
Ch. 18 — Planetary / 3D / Digital Twin / Synthetic v1.0
Ch. 19 — Cross-Domain Systems v1.0
Ch. 20 — Master Atlases (viewing, capability, API, validator, deny) v1.0
Ch. 21 — Roadmap and Dependency Graph v1.0
Ch. 22 — Appendices A–F (glossary, source family, object family, directory rules, supersession,
self-check)
v1.0
Ch. 23 — Assembly Instructions v1.0
v1.1 additions

Kansas Frontier Matrix Domains Culmination Atlas, v1.1 v1.1 front matter (supersedes v1.0)
Kansas Frontier Matrix — governed, evidence-first, map-first, time-aware front p. 5
Section Location
Ch. 24 — Extended Master Atlases v1.1
24.1 Source-Role Anti-Collapse Register v1.1
24.2 Receipt Catalog v1.1
24.3 Decision Outcome Envelope Reference v1.1
24.4 Cross-Lane Relation Atlas (per owning domain) v1.1
24.5 Sensitivity / Rights Tier Reference (T0–T4) v1.1
24.6 Pipeline Gate Reference (RAW → PUBLISHED) v1.1
24.7 Reviewer Role and Separation-of-Duties Matrix v1.1
24.8 Stale-State and Supersession Reference v1.1
24.9 Failure-Mode and Anti-Pattern Register v1.1
24.10 Risk Register and Threat Posture v1.1
24.11 Governance Health Indicators v1.1
24.12 Open-ADR Backlog v1.1
24.13 Atlas ↔ Dossier ↔ Responsibility-Root Crosswalk v1.1
24.14 Object Family × Domain Reference Matrix v1.1
Appendix G — v1.0 → v1.1 Lineage and Supersession Record v1.1
Location key: ‘front’ = this front-matter section; ‘v1.0’ = the v1.0 interior pages that follow this section (retained verbatim); ‘v1.1’ =
the new Chapter 24 and Appendix G pages that follow the v1.0 interior.

Kansas Frontier Matrix Domains Culmination Atlas, v1.0
KFM Domain Synthesizer
2026-05-11
Contents
Cover and governance note 6
1. Executive Summary and Operating Law 8
1.1 Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2. Master Source Ledger and Cross-Domain Object Index 9
2.1 Domain-to-dossier map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2 Cross-domain object family spine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3. Spatial Foundation, Cartography, Reference Systems 13
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4. Hydrology 20
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
1

N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5. Soil 27
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
6. Habitat 34
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
7. Fauna 41
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
8. Flora 48
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
2

B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
9. Agriculture 55
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
10. Geology and Natural Resources 62
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
11. Atmosphere and Air 69
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
3

F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
12. Hazards 76
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
13. Roads, Rail, and Trade Routes 83
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
14. Settlements and Infrastructure 90
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
4

J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
15. Archaeology and Cultural Heritage 97
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
16. People, Genealogy, DNA, and Land Ownership 104
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
17. Frontier Demography / Economy / Settlement / Land / Time Matrix 111
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
5

N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
18. Planetary, 3D, Digital Twin, and Synthetic Spatial Systems 118
A. Domain identity and one-line purpose. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
B. Scope, boundary, and explicit non-ownership. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
C. Ubiquitous language. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
D. Key source families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
E. Main object families. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
F. Cross-lane relations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
G. Map and viewing products. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
H. Pipeline shape (RAW -> PUBLISHED). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
I. Sensitivity, rights, and publication posture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
J. API, contract, and schema surfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
K. Validators, tests, fixtures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
L. Governed AI behavior for this domain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
M. Publication, correction, and rollback. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
N. Verification backlog and open questions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
19. Cross-Domain Systems 125
20. Master Atlases 127
20.1 Master Viewing Mode Atlas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
20.2 Master Capability / Action Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
20.3 Master API Surface Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
20.4 Master Validator / Test Catalogue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
20.5 Deny-by-Default Register and Sensitivity Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . 128
21. Programming Possibilities Backlog, Dependencies, and Roadmap 130
21.1 Dependency graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
22. Appendices 132
Appendix A. Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Appendix B. Source family index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
Appendix C. Object family index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
Appendix D. Directory Rules summary and proposed file-home conventions . . . . . . . . . . . . . . 136
Appendix E. Supersession and lineage notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
Appendix F. Final self-check . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
23. Assembly Instructions 138
23.1 Recommended Pandoc command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
23.2 LaTeX and Typst alternatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
23.3 Figures and diagrams to generate separately . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
23.4 Cover-page governance note . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
Cover and governance note
CONFIRMED doctrine / PROPOSED assembled artifact: This Atlas is a governed, evidence-first, map-first,
time-aware, inspectable synthesis of the attached KFM doctrine and domain dossiers, prepared as a single
reference for stewards, implementers, reviewers, and auditors. [ENCY] [DIRRULES]
Governance note for cover page. CONFIRMED doctrine: The Kansas Frontier Matrix treats the inspectable
claim as the durable unit of public value; maps, tiles, graphs, dashboards, indexes, scenes, exports, and AI
6

answers are downstream carriers that must remain subordinate to EvidenceBundle, policy, review, release state,
correction, and rollback. [ENCY] [MAP-MASTER] [GAI]
Version block. PROPOSED: Title KFM_Domains_Culmination_Atlas_v1.0; phase-assembled Markdown and
PDF artifacts produced from the attached dossier corpus and the phase outputs in this conversation. NEEDS
VERIFICATION: final repo implementation, exact file homes, route names, schema homes, runtime behavior,
CI workflows, dashboards, and live source activation remain unverified until a mounted KFM repository is
inspected. [DIRRULES]
7

1. Executive Summary and Operating Law
CONFIRMED doctrine: KFM is Kansas-first, map-first, time-aware, evidence-first, governed, auditable, correctable, and reversible; public claims should cite evidence or abstain. [ENCY]
CONFIRMED doctrine: RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET ->
PUBLISHED is the governing lifecycle, and promotion is a governed state transition rather than a file move.
[DIRRULES]
CONFIRMED doctrine: EvidenceBundle outranks generated language, renderer state, graph projections, search
indexes, tiles, PMTiles, COGs, dashboards, and synthetic scenes. [ENCY] [GAI] [MAP-MASTER]
CONFIRMED doctrine: Sensitive domains fail closed; archaeology, rare species, rare plants, critical infrastructure, living-person data, DNA, culturally sensitive places, private landowner-sensitive joins, and unclear rights
are denied, restricted, generalized, staged, or reviewed before publication. [ENCY]
CONFIRMED doctrine: Directory Rules govern placement by responsibility root, not topic convenience, and
schema-home authority defaults to schemas/contracts/v1/<...> unless an accepted ADR says otherwise.
[DIRRULES]
PROPOSED implementation posture: The Atlas should be used as an implementation map, acceptance checklist, and audit reference; it is not proof that the target repository already contains the described schemas,
routes, workflows, validators, or release artifacts. [ENCY] [DIRRULES]
1.1 Definitions
Term Definition Citation
Domain CONFIRMED doctrine bounded
responsibility lane with owned
object semantics and governed
cross-lane relations.
[DDD] [ENCY]
Bounded context CONFIRMED reference model
boundary where a term has
defined meaning and ownership.
[DDD]
EvidenceBundle CONFIRMED resolved evidence
package for a claim.
[ENCY]
EvidenceRef CONFIRMED reference that must
resolve to EvidenceBundle before
public claim authority.
[ENCY]
Governed API CONFIRMED doctrine / PROPOSED
implementation interface
enforcing evidence, policy, release,
finite outcomes, and audit.
[GAI] [ENCY]
Promotion CONFIRMED governed release
transition, not file movement.
[DIRRULES]
Redaction Receipt CONFIRMED object family /
PROPOSED implementation record
of public-safe field or geometry
transformation.
[ENCY]
Runtime Response Envelope CONFIRMED doctrine / PROPOSED
implementation finite answer
envelope for AI and runtime
surfaces.
[GAI]
8

2. Master Source Ledger and Cross-Domain Object Index
CONFIRMED: This source ledger lists the short-name citations used in the Atlas and states what each source
supports; source dossiers are evidence of doctrine, planning, and lineage, not proof of current repository
implementation. [ENCY] [DIRRULES]
Short-name Filename or source Role in Atlas
[DIRRULES] Directory Rules Canonical placement and lifecycle
doctrine
[MAP-MASTER] MapLibre Master MapLibre, renderer, tiles,
Evidence Drawer, Focus Mode
doctrine
[INDEX-18] Pass 18 Idea Index Representation, APIs, temporal
modeling, validation,
release-discipline expansion
[ENCY] Encyclopedia Master
domain/object/source/capability
spine
[DOM-AG] Agriculture dossier Agriculture domain dossier
[DOM-FLORA] Flora dossier Flora domain dossier
[DOM-SETTLE] Settlements/Infrastructure dossier Settlements and infrastructure
dossier
[DOM-HF] Habitat+Fauna thin slice Habitat + Fauna thin-slice dossier
[DOM-HAZ] Hazards dossier Hazards domain dossier
[DOM-ARCH] Archaeology dossier Archaeology domain dossier
[DOM-ROADS] Roads/Rail dossier Roads, rail, and trade routes
dossier
[DOM-AIR] Atmosphere/Air dossier Atmosphere and air dossier
[DOM-GEOL] Geology dossier Geology and natural resources
dossier
[DOM-SOIL] Soil dossier Soil domain dossier
[DOM-HAB] Habitat dossier Habitat domain dossier
[DOM-FAUNA] Fauna dossier Fauna domain dossier
[DOM-HYD] Hydrology dossier Hydrology domain dossier
[DOM-PEOPLE] People/DNA/Land dossier People, genealogy, DNA, and land
ownership dossier
[GAI] Governed AI dossier Governed AI and AIReceipt
doctrine
[UIAI] Whole UI + AI report Whole UI and governed AI
expansion plan
[DDD] DDD Reference Bounded context and ubiquitous
language reference
[UNIFIED] Unified / pipeline lineage Unified build and pipeline
roadmap lineage
2.1 Domain-to-dossier map
Domain Primary citations Status
Spatial Foundation [ENCY] [MAP-MASTER]
[INDEX-18]
CONFIRMED doctrine /
PROPOSED implementation
9

Domain Primary citations Status
Hydrology [DOM-HYD] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Soil [DOM-SOIL] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Habitat [DOM-HAB] [DOM-HF] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Fauna [DOM-FAUNA] [DOM-HF]
[ENCY]
CONFIRMED doctrine /
PROPOSED implementation
Flora [DOM-FLORA] [ENCY] CONFIRMED dossier /
PROPOSED implementation
Agriculture [DOM-AG] [ENCY] CONFIRMED dossier /
PROPOSED implementation
Geology [DOM-GEOL] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Atmosphere/Air [DOM-AIR] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Hazards [DOM-HAZ] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Roads/Rail [DOM-ROADS] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Settlements/Infrastructure [DOM-SETTLE] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Archaeology [DOM-ARCH] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
People/DNA/Land [DOM-PEOPLE] [ENCY] CONFIRMED doctrine /
PROPOSED implementation
Frontier Matrix [ENCY] [UNIFIED] CONFIRMED doctrine /
PROPOSED implementation
Planetary/3D [ENCY] [MAP-MASTER] [UIAI] CONFIRMED doctrine /
PROPOSED implementation
2.2 Cross-domain object family spine
Domain Object families Status / citation
Spatial Foundation Coordinate Reference Profile,
GeographyVersion, Projection
Transform Receipt, Geometry
Fingerprint, Base Layer
Descriptor, MapStyleRule, Scale
Support Profile,
UncertaintySurface…
CONFIRMED object-family spine
/ PROPOSED implementation
[ENCY] [MAP-MASTER]
[INDEX-18]
Hydrology Watershed, HUCUnit,
HydroFeature, ReachIdentity,
GaugeSite, FlowObservation,
WaterLevelObservation, Water
Quality Observation…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-HYD] [ENCY]
10

Domain Object families Status / citation
Soil SoilMapUnit, SoilComponent,
Horizon, SoilProperty, Hydrologic
Soil Group, Soil Moisture
Observation, Pedon, ErosionRisk…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-SOIL] [ENCY]
Habitat HabitatPatch,
LandCoverObservation,
EcologicalSystem, Habitat Quality
Score, SuitabilityModel,
ConnectivityEdge, Corridor,
Restoration Opportunity…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-HAB] [DOM-HF] [ENCY]
Fauna Taxon, Taxon Crosswalk,
Conservation Status, Occurrence
Evidence, Occurrence Restricted,
Occurrence Public, RangePolygon,
SeasonalRange…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-FAUNA] [DOM-HF]
[ENCY]
Flora Plant Taxon, FloraTaxon
Crosswalk, Flora Occurrence,
SpecimenRecord, Rare Plant
Record, Vegetation Community,
InvasivePlantRecord, Phenology
Observation…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-FLORA] [ENCY]
Agriculture Crop Observation, Field
Candidate, Crop Rotation, Yield
Observation, Irrigation Link,
Conservation Practice, Soil Crop
Suitability, Agricultural Economy
Observation…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-AG] [ENCY]
Geology Geologic Unit, SurficialUnit,
Lithology, Stratigraphic Interval,
StructureFeature,
GeologyBoundaryVersion,
BoreholeReference, Well
LogReference…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-GEOL] [ENCY]
Atmosphere/Air AirStation, AirObservation,
PM2.5 Observation, Ozone
Observation, SmokeContext,
AODRaster, Weather Station,
Weather Observation…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-AIR] [ENCY]
Hazards Hazard Event, Hazard
Observation, Warning Context,
Advisory Context, Disaster
Declaration, Flood Context,
Wildfire Detection,
SmokeContext…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-HAZ] [ENCY]
Roads/Rail Road Segment, Rail Segment,
CorridorRoute, RouteMembership,
Network Node, Crossing, Bridge,
Ferry…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-ROADS] [ENCY]
11

Domain Object families Status / citation
Settlements/Infrastructure Settlement, Municipality,
CensusPlace, Townsite,
GhostTown, Fort, Mission,
ReservationCommunity…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-SETTLE] [ENCY]
Archaeology Archaeological Site,
SiteComponent,
CulturalTemporalPeriod,
SurveyProject, SurveyTransect,
ShovelTest, TestUnit,
ExcavationUnit…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-ARCH] [ENCY]
People/DNA/Land Person Assertion,
PersonCanonical, NameAssertion,
LifeEvent, Residence Event,
Migration Event, Genealogy
Relationship, FamilyGroup…
CONFIRMED object-family spine
/ PROPOSED implementation
[DOM-PEOPLE] [ENCY]
Frontier Matrix Frontier Definition,
GeographyVersion, County-Year
Panel, Population Observation,
Economic Observation,
Agriculture Observation, Access
Observation, Settlement Status…
CONFIRMED object-family spine
/ PROPOSED implementation
[ENCY] [UNIFIED]
Planetary/3D Scene Manifest, Terrain Model, 3D
Tile Set, glTF Asset, Point Cloud,
Digital Twin View, Synthetic
Surface, ViewState…
CONFIRMED object-family spine
/ PROPOSED implementation
[ENCY] [MAP-MASTER] [UIAI]
12

3. Spatial Foundation, Cartography, Reference Systems
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Provide the shared spatial grammar for coordinate reference systems, geometry validity, scale, spatial support, generalization, uncertainty, basemap context, and
cartographic representation. [ENCY] [MAP-MASTER] [INDEX-18]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Coordinate reference profiles; Geography versions; Projection
transform receipts; Geometry fingerprints; Base-layer descriptors; Map style rules; Scale-support profiles; Uncertainty surfaces; Generalization transforms. [ENCY] [MAP-MASTER] [INDEX-18]
CONFIRMED / PROPOSED: This domain explicitly does not own: Hydrology, soil, geology, hazards, transport,
settlements, archaeology, people, habitat, fauna, flora, agriculture, and atmosphere truth stay with their
domain lanes. [ENCY] [MAP-MASTER] [INDEX-18]
C. Ubiquitous language.
Term Definition Citation
Coordinate Reference Profile CONFIRMED term / PROPOSED
field realization: Coordinate
Reference Profile is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
GeographyVersion CONFIRMED term / PROPOSED
field realization:
GeographyVersion is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
Projection Transform Receipt CONFIRMED term / PROPOSED
field realization: Projection
Transform Receipt is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
Geometry Fingerprint CONFIRMED term / PROPOSED
field realization: Geometry
Fingerprint is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
Base Layer Descriptor CONFIRMED term / PROPOSED
field realization: Base Layer
Descriptor is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
13

Term Definition Citation
MapStyleRule CONFIRMED term / PROPOSED
field realization:
MapStyleRule is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
Scale Support Profile CONFIRMED term / PROPOSED
field realization: Scale
Support Profile is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
UncertaintySurface CONFIRMED term / PROPOSED
field realization:
UncertaintySurface is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
Generalization Transform CONFIRMED term / PROPOSED
field realization:
Generalization Transform is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
LayerManifest CONFIRMED term / PROPOSED
field realization:
LayerManifest is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER]
[INDEX-18]
D. Key source families.
Source family Role Rights / sensitivity Freshness Status
USGS 3DEP /
terrain
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
TIGER
administrative
geometry
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
GNIS names authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
14

Source family Role Rights / sensitivity Freshness Status
state and local GIS authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
authoritative
basemaps
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
imagery / DEM /
COG
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
historical maps authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[INDEX-18]
E. Main object families.
Object Purpose Identity rule Temporal handling
Coordinate Reference
Profile
Represents Coordinate
Reference Profile
evidence or released
derivative within Spatial
Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
GeographyVersion Represents
GeographyVersion
evidence or released
derivative within Spatial
Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Projection Transform
Receipt
Represents Projection
Transform Receipt
evidence or released
derivative within Spatial
Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Geometry Fingerprint Represents Geometry
Fingerprint evidence or
released derivative within
Spatial Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Base Layer Descriptor Represents Base Layer
Descriptor evidence or
released derivative within
Spatial Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
15

Object Purpose Identity rule Temporal handling
MapStyleRule Represents MapStyleRule
evidence or released
derivative within Spatial
Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Scale Support Profile Represents Scale Support
Profile evidence or
released derivative within
Spatial Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
UncertaintySurface Represents
UncertaintySurface
evidence or released
derivative within Spatial
Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Generalization Transform Represents
Generalization
Transform evidence or
released derivative within
Spatial Foundation.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Spatial Foundation All domains CRS, scale, geometry,
layer, and representation
grammar.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Spatial Foundation Hydrology/soil/geology/hazardsterrain and raster
support.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Spatial Foundation Archaeology/fauna/flora/infrastructure/people public-safe geometry and
sensitivity transforms.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Spatial Foundation MapLibre/Governed AI renderer and Focus
surfaces stay downstream
of released evidence.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include CRS/scale inspection; source comparison; uncertainty view; staledata view; sensitivity-redacted map; Evidence Drawer; time slider; diagnostics. [ENCY] [MAP-MASTER]
16

[INDEX-18]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Spatial Foundation follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [ENCY] [MAP-MASTER] [INDEX-18]
Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Sensitive geometry, unclear rights, and false precision fail closed; public maps consume
released artifacts only. [ENCY] [MAP-MASTER] [INDEX-18]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Spatial Foundation
feature/detail resolver;
route TBD
SpatialFoundationDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Spatial Foundation layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
17

Endpoint or artifact DTO / schema Outcomes Status
Spatial Foundation
Evidence Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Spatial Foundation Focus
Mode answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: CRS/datum transform validation. [ENCY] [MAP-MASTER] [INDEX-18]
• PROPOSED: geometry validity and fingerprint regression. [ENCY] [MAP-MASTER] [INDEX-18]
• PROPOSED: scale/support validation. [ENCY] [MAP-MASTER] [INDEX-18]
• PROPOSED: LayerManifest and GeoManifest closure. [ENCY] [MAP-MASTER] [INDEX-18]
• PROPOSED: sensitive public-geometry denial. [ENCY] [MAP-MASTER] [INDEX-18]
• PROPOSED: renderer-boundary tests. [ENCY] [MAP-MASTER] [INDEX-18]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Spatial Foundation EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when
evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI]
[ENCY] [MAP-MASTER] [INDEX-18]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Spatial Foundation publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule,
and rollback target. [ENCY Appendix E] [ENCY] [MAP-MASTER] [INDEX-18]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify actual schema home and
path conventions in mounted repo.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify LayerManifest/GeoManifest
implementation and tests.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Define geometry fingerprint
canonicalization rule.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
18

Item to verify Evidence that would settle it Status
Prove no UI access to
RAW/WORK/QUARANTINE or
canonical stores.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
19

4. Hydrology
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern watersheds, HUC units, hydro features, reaches,
gauges, flow and level observations, water quality, groundwater context, regulatory flood context, observed
flood evidence, drought and irrigation links. [DOM-HYD] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Watersheds and HUC units; HydroFeature and ReachIdentity;
GaugeSite; FlowObservation; WaterLevelObservation; Water Quality Observation; Groundwater Well; NFHLZone / Flood Context; Observed Flood Event; Hydrograph and UpstreamTrace. [DOM-HYD] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Emergency alerts and life-safety warnings
are hazards/official-source concerns.; NFHL regulatory context is not observed inundation.; Soil, agriculture,
geology, and infrastructure keep their own canonical claims. [DOM-HYD] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Watershed CONFIRMED term / PROPOSED
field realization: Watershed
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-HYD] [ENCY]
HUCUnit CONFIRMED term / PROPOSED
field realization: HUCUnit is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-HYD] [ENCY]
HydroFeature CONFIRMED term / PROPOSED
field realization:
HydroFeature is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HYD] [ENCY]
ReachIdentity CONFIRMED term / PROPOSED
field realization:
ReachIdentity is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HYD] [ENCY]
GaugeSite CONFIRMED term / PROPOSED
field realization: GaugeSite is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-HYD] [ENCY]
20

Term Definition Citation
FlowObservation CONFIRMED term / PROPOSED
field realization:
FlowObservation is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HYD] [ENCY]
WaterLevelObservation CONFIRMED term / PROPOSED
field realization:
WaterLevelObservation is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HYD] [ENCY]
Water Quality Observation CONFIRMED term / PROPOSED
field realization: Water
Quality Observation is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HYD] [ENCY]
Groundwater Well CONFIRMED term / PROPOSED
field realization:
Groundwater Well is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HYD] [ENCY]
NFHLZone CONFIRMED term / PROPOSED
field realization: NFHLZone
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-HYD] [ENCY]
Observed Flood Event CONFIRMED term / PROPOSED
field realization: Observed
Flood Event is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HYD] [ENCY]
Flood Context CONFIRMED term / PROPOSED
field realization: Flood
Context is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-HYD] [ENCY]
D. Key source families.
21

Source family Role Rights / sensitivity Freshness Status
USGS WBD /
HUC12
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
NHDPlus HR /
3DHP-oriented
hydrography
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
USGS Water Data
/ NWIS
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
FEMA NFHL /
MSC
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
3DEP terrain authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
water quality and
groundwater
sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
historical observed
flood evidence
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HYD]
[ENCY]
E. Main object families.
Object Purpose Identity rule Temporal handling
Watershed Represents Watershed
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
HUCUnit Represents HUCUnit
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
22

Object Purpose Identity rule Temporal handling
HydroFeature Represents HydroFeature
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ReachIdentity Represents ReachIdentity
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
GaugeSite Represents GaugeSite
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
FlowObservation Represents
FlowObservation
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
WaterLevelObservation Represents
WaterLevelObservation
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Water Quality
Observation
Represents Water
Quality Observation
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Groundwater Well Represents Groundwater
Well evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
NFHLZone Represents NFHLZone
evidence or released
derivative within
Hydrology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
23

This domain Related lane Relation type Constraint
Hydrology Hazards flood, drought, warning,
declaration, resilience
context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Hydrology Soil soil moisture, hydrologic
group, infiltration,
runoff.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Hydrology Agriculture irrigation, drought stress,
crop-water context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Hydrology Settlements/Infrastructure floodplain, bridges, dams,
utilities, exposure
context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include HUC12 watershed view; gauge/site time-series view; hydrograph
view; regulatory flood-context layer; observed flood-event layer; terrain-derived hydrology layer; Evidence
Drawer. [DOM-HYD] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Hydrology follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [DOM-HYD] [ENCY]
Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
24

Stage Handling Gate Status
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Hydrology denies unclear rights and flood-role misuse; NFHL-as-observed-flood
claims are denied. Infrastructure and private-property implications require review. [DOM-HYD] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Hydrology feature/detail
resolver; route TBD
HydrologyDecisionEnvelopeANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Hydrology layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Hydrology Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Hydrology Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: HUC12 fingerprint validation. [DOM-HYD] [ENCY]
• PROPOSED: NHDPlus HR identity ambiguity tests. [DOM-HYD] [ENCY]
• PROPOSED: USGS parameter/unit/qualifier/no-data tests. [DOM-HYD] [ENCY]
• PROPOSED: NFHL role-separation tests. [DOM-HYD] [ENCY]
• PROPOSED: EvidenceBundle closure tests. [DOM-HYD] [ENCY]
• PROPOSED: no-network hydrology proof fixture. [DOM-HYD] [ENCY]
25

L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Hydrology EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence
is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-HYD]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Hydrology publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-HYD] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify HUC12 fixture and
fingerprint rule.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify NHDPlus HR crosswalk and
ambiguity ABSTAIN behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify USGS Water normalizer
and NFHL source-role separation.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify hydrology API and
MapLibre layer adapter.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
26

5. Soil
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern static soil survey evidence, gridded derivatives,
components, horizons, pedons, soil moisture observations, interpretations, suitability, erosion context, and
public-safe soil map/API products. [DOM-SOIL] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: SoilMapUnit; SoilComponent; Horizon; SoilProperty; Hydrologic
Soil Group; Soil Moisture Observation; ErosionRisk; SuitabilityRating; Pedon / SoilProfileView; Component
Horizon Join; SoilTimeCaveat. [DOM-SOIL] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Crop and yield claims belong to Agriculture.;
Streamflow, groundwater, and flood context belong to Hydrology/Hazards.; Lithology, boreholes, and stratigraphy belong to Geology. [DOM-SOIL] [ENCY]
C. Ubiquitous language.
Term Definition Citation
SoilMapUnit CONFIRMED term / PROPOSED
field realization: SoilMapUnit
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SOIL] [ENCY]
SoilComponent CONFIRMED term / PROPOSED
field realization:
SoilComponent is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-SOIL] [ENCY]
Horizon CONFIRMED term / PROPOSED
field realization: Horizon is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SOIL] [ENCY]
SoilProperty CONFIRMED term / PROPOSED
field realization: SoilProperty
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SOIL] [ENCY]
Hydrologic Soil Group CONFIRMED term / PROPOSED
field realization: Hydrologic
Soil Group is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-SOIL] [ENCY]
27

Term Definition Citation
Soil Moisture Observation CONFIRMED term / PROPOSED
field realization: Soil
Moisture Observation is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SOIL] [ENCY]
Pedon CONFIRMED term / PROPOSED
field realization: Pedon is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SOIL] [ENCY]
SuitabilityRating CONFIRMED term / PROPOSED
field realization:
SuitabilityRating is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SOIL] [ENCY]
SoilTimeCaveat CONFIRMED term / PROPOSED
field realization:
SoilTimeCaveat is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-SOIL] [ENCY]
authoritative_static_soil CONFIRMED term / PROPOSED
field realization:
authoritative_static_soil is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SOIL] [ENCY]
gridded_derivative_soil CONFIRMED term / PROPOSED
field realization:
gridded_derivative_soil is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SOIL] [ENCY]
station_soil_moisture CONFIRMED term / PROPOSED
field realization:
station_soil_moisture is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SOIL] [ENCY]
D. Key source families.
28

Source family Role Rights / sensitivity Freshness Status
NRCS SSURGO authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
USDA NRCS Soil
Data Access
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
NRCS gSSURGO authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
NRCS gNATSGO authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
Kansas Mesonet
soil moisture
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
NRCS SCAN authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
NOAA USCRN authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
NASA SMAP authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SOIL]
[ENCY]
E. Main object families.
29

Object Purpose Identity rule Temporal handling
SoilMapUnit Represents SoilMapUnit
evidence or released
derivative within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SoilComponent Represents
SoilComponent evidence
or released derivative
within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Horizon Represents Horizon
evidence or released
derivative within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SoilProperty Represents SoilProperty
evidence or released
derivative within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Hydrologic Soil Group Represents Hydrologic
Soil Group evidence or
released derivative within
Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Soil Moisture
Observation
Represents Soil Moisture
Observation evidence or
released derivative within
Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Pedon Represents Pedon
evidence or released
derivative within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ErosionRisk Represents ErosionRisk
evidence or released
derivative within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SuitabilityRating Represents
SuitabilityRating
evidence or released
derivative within Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
30

Component Horizon Join Represents Component
Horizon Join evidence or
released derivative within
Soil.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Soil Agriculture soil-crop suitability,
irrigation, drought stress.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Soil Hydrology infiltration, runoff,
hydrologic group, soil
moisture.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Soil Habitat/Fauna/Flora substrate and moisture
context without
rare-location exposure.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Soil Geology parent material relation
without replacing
lithology truth.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include static soil mapunit view; component/horizon drill-down; hydrologic soil group view; soil-moisture station series; gridded derivative view; suitability/interpretation view;
support-type badges. [DOM-SOIL] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Soil follows RAW -> WORK / QUARANTINE ->
PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state transition.
[DIRRULES] [DOM-SOIL] [ENCY]
31

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Support-type separation is mandatory; static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface. [DOM-SOIL] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Soil feature/detail
resolver; route TBD
SoilDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Soil layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Soil Evidence Drawer
payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Soil Focus Mode answer Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: MUKEY/COKEY/CHKEY lineage tests. [DOM-SOIL] [ENCY]
32

• PROPOSED: horizon depth sanity. [DOM-SOIL] [ENCY]
• PROPOSED: soil-moisture unit/depth/QC tests. [DOM-SOIL] [ENCY]
• PROPOSED: support-type separation denial. [DOM-SOIL] [ENCY]
• PROPOSED: dual-hash stability tests. [DOM-SOIL] [ENCY]
• PROPOSED: catalog closure and Evidence Drawer tests. [DOM-SOIL] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Soil EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-SOIL]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Soil publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and rollback target.
[ENCY Appendix E] [DOM-SOIL] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify SSURGO/SDA query
fixtures and query_hash rule.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Mesonet normalizer and
source rights.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify gSSURGO/gNATSGO
support metadata.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Soil EvidenceBundle,
CatalogMatrix, and layer registry.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
33

6. Habitat
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern habitat patches, land-cover observations, ecological systems, habitat quality, suitability models, connectivity, corridors, restoration opportunities, stewardship
zones, receipts, uncertainty, and public-safe habitat products. [DOM-HAB] [DOM-HF] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: HabitatPatch; LandCoverObservation; EcologicalSystem; Habitat Quality Score; SuitabilityModel; ConnectivityEdge; Corridor; Restoration Opportunity; StewardshipZone;
Model Run Receipt; UncertaintySurface. [DOM-HAB] [DOM-HF] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Fauna owns taxa and animal occurrence.; Flora
owns plant taxa, specimens, occurrences, and rare plant records.; Soil, hydrology, agriculture, hazards, and
archaeology retain their own truth. [DOM-HAB] [DOM-HF] [ENCY]
C. Ubiquitous language.
Term Definition Citation
HabitatPatch CONFIRMED term / PROPOSED
field realization:
HabitatPatch is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HAB] [DOM-HF] [ENCY]
LandCoverObservation CONFIRMED term / PROPOSED
field realization:
LandCoverObservation is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAB] [DOM-HF] [ENCY]
EcologicalSystem CONFIRMED term / PROPOSED
field realization:
EcologicalSystem is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAB] [DOM-HF] [ENCY]
Habitat Quality Score CONFIRMED term / PROPOSED
field realization: Habitat
Quality Score is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HAB] [DOM-HF] [ENCY]
SuitabilityModel CONFIRMED term / PROPOSED
field realization:
SuitabilityModel is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAB] [DOM-HF] [ENCY]
34

Term Definition Citation
ConnectivityEdge CONFIRMED term / PROPOSED
field realization:
ConnectivityEdge is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAB] [DOM-HF] [ENCY]
Corridor CONFIRMED term / PROPOSED
field realization: Corridor is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-HAB] [DOM-HF] [ENCY]
Restoration Opportunity CONFIRMED term / PROPOSED
field realization: Restoration
Opportunity is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HAB] [DOM-HF] [ENCY]
StewardshipZone CONFIRMED term / PROPOSED
field realization:
StewardshipZone is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAB] [DOM-HF] [ENCY]
Regulatory critical habitat CONFIRMED term / PROPOSED
field realization: Regulatory
critical habitat is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HAB] [DOM-HF] [ENCY]
Modeled habitat CONFIRMED term / PROPOSED
field realization: Modeled
habitat is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-HAB] [DOM-HF] [ENCY]
Geoprivacy transform CONFIRMED term / PROPOSED
field realization: Geoprivacy
transform is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-HAB] [DOM-HF] [ENCY]
D. Key source families.
35

Source family Role Rights / sensitivity Freshness Status
USFWS ECOS /
critical habitat
services
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
KDWP state
review context
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
NLCD land cover authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
NWI wetlands authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
GAP / LANDFIRE authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
NatureServe and
controlled
biodiversity sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
GBIF/iNaturalist/iDigBio
occurrence inputs
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
PAD-US
stewardship context
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAB]
[DOM-HF] [ENCY]
E. Main object families.
36

Object Purpose Identity rule Temporal handling
HabitatPatch Represents HabitatPatch
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
LandCoverObservation Represents
LandCoverObservation
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
EcologicalSystem Represents
EcologicalSystem
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Habitat Quality Score Represents Habitat
Quality Score evidence or
released derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SuitabilityModel Represents
SuitabilityModel
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ConnectivityEdge Represents
ConnectivityEdge
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Corridor Represents Corridor
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Restoration Opportunity Represents Restoration
Opportunity evidence or
released derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
StewardshipZone Represents
StewardshipZone
evidence or released
derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
37

Model Run Receipt Represents Model Run
Receipt evidence or
released derivative within
Habitat.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Habitat Fauna habitat assignment and
occurrence context, with
geoprivacy.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Habitat Flora vegetation community
and rare plant context
under Flora controls.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Habitat Soil/Hydrology substrate, moisture,
wetlands, riparian
support.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Habitat Hazards fire, drought, flood,
smoke and resilience
stress context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include habitat overlay registry; source-role badges; critical habitat view;
modeled habitat view; occurrence summary view; connectivity/corridor view; Evidence Drawer Habitat panel.
[DOM-HAB] [DOM-HF] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Habitat follows RAW -> WORK / QUARANTINE
-> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state transition.
[DIRRULES] [DOM-HAB] [DOM-HF] [ENCY]
38

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Regulatory critical habitat, modeled habitat, species range, occurrence points, and
landscape context must not be flattened. Sensitive occurrence details deny by default. [DOM-HAB] [DOM-HF]
[ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Habitat feature/detail
resolver; route TBD
HabitatDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Habitat layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Habitat Evidence Drawer
payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Habitat Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
39

K. Validators, tests, fixtures.
• PROPOSED: Source descriptor tests. [DOM-HAB] [DOM-HF] [ENCY]
• PROPOSED: critical habitat source-role tests. [DOM-HAB] [DOM-HF] [ENCY]
• PROPOSED: modeled-as-critical denial tests. [DOM-HAB] [DOM-HF] [ENCY]
• PROPOSED: occurrence geoprivacy tests. [DOM-HAB] [DOM-HF] [ENCY]
• PROPOSED: catalog closure tests. [DOM-HAB] [DOM-HF] [ENCY]
• PROPOSED: Habitat+Fauna thin-slice fixtures. [DOM-HAB] [DOM-HF] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Habitat EvidenceBundles,
compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-HAB]
[DOM-HF] [ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Habitat publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and rollback
target. [ENCY Appendix E] [DOM-HAB] [DOM-HF] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify official critical habitat
source descriptors.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify sensitive occurrence policy
and geoprivacy transforms.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify model-card requirements for
suitability products.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Habitat MapLibre overlay
registry and Focus behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
40

7. Fauna
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern animal taxonomic identity, conservation/legal
status, occurrence evidence, monitoring, range, seasonal support, sensitive sites, mortality, disease, invasive
species, geoprivacy, public-safe products, and bounded APIs. [DOM-FAUNA] [DOM-HF] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Taxon; Taxon Crosswalk; Conservation Status; Occurrence
Evidence; Occurrence Restricted; Occurrence Public; RangePolygon; SeasonalRange; MigrationRoute; SensitiveSite; MortalityObservation; DiseaseObservation; Invasive Species Record; Redaction Receipt. [DOMFAUNA] [DOM-HF] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Habitat owns habitat patches and suitability.;
Flora owns plant records.; Hydrology/soil/agriculture/roads/people provide context only through governed
joins. [DOM-FAUNA] [DOM-HF] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Taxon CONFIRMED term / PROPOSED
field realization: Taxon is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Taxon Crosswalk CONFIRMED term / PROPOSED
field realization: Taxon
Crosswalk is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Conservation Status CONFIRMED term / PROPOSED
field realization:
Conservation Status is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Occurrence Evidence CONFIRMED term / PROPOSED
field realization: Occurrence
Evidence is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Occurrence Restricted CONFIRMED term / PROPOSED
field realization: Occurrence
Restricted is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
41

Term Definition Citation
Occurrence Public CONFIRMED term / PROPOSED
field realization: Occurrence
Public is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
SensitiveSite CONFIRMED term / PROPOSED
field realization: SensitiveSite
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
SeasonalRange CONFIRMED term / PROPOSED
field realization:
SeasonalRange is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
MonitoringEvent CONFIRMED term / PROPOSED
field realization:
MonitoringEvent is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Redaction Receipt CONFIRMED term / PROPOSED
field realization: Redaction
Receipt is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Geoprivacy transform CONFIRMED term / PROPOSED
field realization: Geoprivacy
transform is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
Public-safe derivative CONFIRMED term / PROPOSED
field realization: Public-safe
derivative is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FAUNA] [DOM-HF]
[ENCY]
D. Key source families.
42

Source family Role Rights / sensitivity Freshness Status
KDWP-like
steward sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
USFWS ECOS-like
federal sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
NatureServe /
heritage-style
sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
GBIF/eBird/iNaturalist/iDigBio/BISONlike aggregatorsauthority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
EDDMapS and
invasive feeds
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
agency monitoring/surveys/eDNA/acoustic/telemetryauthority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
NLCD/NWI/PADUS/SSURGO
context layers
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FAUNA]
[DOM-HF] [ENCY]
E. Main object families.
Object Purpose Identity rule Temporal handling
Taxon Represents Taxon
evidence or released
derivative within Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Taxon Crosswalk Represents Taxon
Crosswalk evidence or
released derivative within
Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
43

Object Purpose Identity rule Temporal handling
Conservation Status Represents Conservation
Status evidence or
released derivative within
Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Occurrence Evidence Represents Occurrence
Evidence evidence or
released derivative within
Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Occurrence Restricted Represents Occurrence
Restricted evidence or
released derivative within
Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Occurrence Public Represents Occurrence
Public evidence or
released derivative within
Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
RangePolygon Represents
RangePolygon evidence
or released derivative
within Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SeasonalRange Represents
SeasonalRange evidence
or released derivative
within Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
MigrationRoute Represents
MigrationRoute evidence
or released derivative
within Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SensitiveSite Represents SensitiveSite
evidence or released
derivative within Fauna.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
44

This domain Related lane Relation type Constraint
Fauna Habitat derived habitat
assignment and seasonal
support.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Fauna Flora ecological community,
pollinator, invasive,
food-web context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Fauna Hydrology aquatic/riparian/wetland/spawning
context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Fauna Hazards disease, mortality,
wildfire, flood, drought
exposure.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include public species status view; public range polygons; occurrence
density grid; species richness grid; invasive monitoring public layer; seasonal support layer; public-safe popup;
taxon search. [DOM-FAUNA] [DOM-HF] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Fauna follows RAW -> WORK / QUARANTINE ->
PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state transition.
[DIRRULES] [DOM-FAUNA] [DOM-HF] [ENCY]
Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
45

Stage Handling Gate Status
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Exact sensitive occurrence, nest, den, roost, hibernacula, spawning, and stewardcontrolled records fail closed. Public exact occurrence tiles for sensitive taxa are denied. [DOM-FAUNA]
[DOM-HF] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Fauna feature/detail
resolver; route TBD
FaunaDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Fauna layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Fauna Evidence Drawer
payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Fauna Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: Source-role authority tests. [DOM-FAUNA] [DOM-HF] [ENCY]
• PROPOSED: taxonomy resolution and ambiguity tests. [DOM-FAUNA] [DOM-HF] [ENCY]
• PROPOSED: occurrence restricted/public split tests. [DOM-FAUNA] [DOM-HF] [ENCY]
• PROPOSED: redaction receipt validation. [DOM-FAUNA] [DOM-HF] [ENCY]
• PROPOSED: tile field allowlist tests. [DOM-FAUNA] [DOM-HF] [ENCY]
• PROPOSED: Runtime Response Envelope negative cases. [DOM-FAUNA] [DOM-HF] [ENCY]
46

L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Fauna EvidenceBundles,
compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-FAUNA]
[DOM-HF] [ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Fauna publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and rollback
target. [ENCY Appendix E] [DOM-FAUNA] [DOM-HF] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify fauna source rights and
steward roles.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify taxonomy resolution
implementation.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify restricted/public occurrence
split.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify public layer safety and AI
no-leak behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
47

8. Flora
A. Domain identity and one-line purpose.
CONFIRMED dossier / PROPOSED implementation: Govern plant taxonomic identity, flora occurrences, specimens, surveys, vegetation communities, rare/protected/culturally sensitive flora controls, public-safe surfaces,
evidence-backed maps, correction, and rollback. [DOM-FLORA] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Plant Taxon; SpecimenRecord; Flora Occurrence; Rare Plant
Record; Vegetation Community; InvasivePlantRecord; Phenology Observation; RangePolygon; Habitat Association; Botanical Survey; Restoration Planting; Redaction Receipt. [DOM-FLORA] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Habitat owns habitat patches and suitability.;
Fauna owns animal taxa and occurrences.; Soil, hydrology, agriculture, hazards, roads, settlements, archaeology,
and people keep their truth. [DOM-FLORA] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Plant Taxon CONFIRMED term / PROPOSED
field realization: Plant Taxon
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-FLORA] [ENCY]
FloraTaxon Crosswalk CONFIRMED term / PROPOSED
field realization: FloraTaxon
Crosswalk is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
Flora Occurrence CONFIRMED term / PROPOSED
field realization: Flora
Occurrence is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
SpecimenRecord CONFIRMED term / PROPOSED
field realization:
SpecimenRecord is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
Rare Plant Record CONFIRMED term / PROPOSED
field realization: Rare Plant
Record is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
48

Term Definition Citation
Vegetation Community CONFIRMED term / PROPOSED
field realization: Vegetation
Community is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
InvasivePlantRecord CONFIRMED term / PROPOSED
field realization:
InvasivePlantRecord is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-FLORA] [ENCY]
Phenology Observation CONFIRMED term / PROPOSED
field realization: Phenology
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
DistributionSurface CONFIRMED term / PROPOSED
field realization:
DistributionSurface is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-FLORA] [ENCY]
Habitat Association CONFIRMED term / PROPOSED
field realization: Habitat
Association is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
SourceRole CONFIRMED term / PROPOSED
field realization: SourceRole
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-FLORA] [ENCY]
Redaction Receipt CONFIRMED term / PROPOSED
field realization: Redaction
Receipt is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-FLORA] [ENCY]
D. Key source families.
49

Source family Role Rights / sensitivity Freshness Status
KDWP flora/listed
species context
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
KDWP Ecological
Review Tool or
stewardship
outputs
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
Kansas Biological
Survey / KU
herbarium surfaces
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
USFWS ECOS
plant context
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
NatureServe
Explorer / Explorer
Pro
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
GBIF vascular
plant downloads
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
iDigBio specimen
records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
iNaturalist-derived
observations
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-FLORA]
[ENCY]
E. Main object families.
50

Object Purpose Identity rule Temporal handling
Plant Taxon Represents Plant Taxon
evidence or released
derivative within Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
FloraTaxon Crosswalk Represents FloraTaxon
Crosswalk evidence or
released derivative within
Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Flora Occurrence Represents Flora
Occurrence evidence or
released derivative within
Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SpecimenRecord Represents
SpecimenRecord
evidence or released
derivative within Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Rare Plant Record Represents Rare Plant
Record evidence or
released derivative within
Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Vegetation Community Represents Vegetation
Community evidence or
released derivative within
Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
InvasivePlantRecord Represents
InvasivePlantRecord
evidence or released
derivative within Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Phenology Observation Represents Phenology
Observation evidence or
released derivative within
Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
RangePolygon Represents
RangePolygon evidence
or released derivative
within Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
51

Habitat Association Represents Habitat
Association evidence or
released derivative within
Flora.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Flora Habitat habitat association and
vegetation community
context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Flora Fauna pollinator, food-web,
invasive, biodiversity
context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Flora Soil/Hydrology substrate, wetland,
riparian, drought
context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Flora Hazards fire, drought, flood,
smoke, vegetation stress.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include public generalized occurrence layer; public range/distribution
layer; vegetation community layer; invasive plant layer; phenology/condition layer; habitat association summary; review candidate view. [DOM-FLORA] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Flora follows RAW -> WORK / QUARANTINE ->
PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state transition.
[DIRRULES] [DOM-FLORA] [ENCY]
52

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Rare, protected, culturally sensitive, and steward-reviewed flora default to generalized,
withheld, staged, or denied public geometry. [DOM-FLORA] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Flora feature/detail
resolver; route TBD
FloraDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Flora layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Flora Evidence Drawer
payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Flora Focus Mode answer Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: Taxonomy reconciliation tests. [DOM-FLORA] [ENCY]
53

• PROPOSED: rights/sensitivity validators. [DOM-FLORA] [ENCY]
• PROPOSED: exact sensitive public geometry denial. [DOM-FLORA] [ENCY]
• PROPOSED: catalog closure tests. [DOM-FLORA] [ENCY]
• PROPOSED: API finite-outcome fixtures. [DOM-FLORA] [ENCY]
• PROPOSED: no-live-network fixture pipeline. [DOM-FLORA] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Flora EvidenceBundles,
compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-FLORA]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Flora publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and rollback
target. [ENCY Appendix E] [DOM-FLORA] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify source endpoints and rights. mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify rare-plant steward policy. mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify exact/public geometry
thresholds.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Focus Mode and Evidence
Drawer behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
54

9. Agriculture
A. Domain identity and one-line purpose.
CONFIRMED dossier / PROPOSED implementation: Govern agricultural aggregate observations, soil/moisture/vegetatio
context, crop progress, suitability, stress indicators, irrigation links, conservation practice context, agricultural
economy observations, and public-safe products. [DOM-AG] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Crop Observation; Field Candidate; Crop Rotation; Yield Observation; Irrigation Link; Conservation Practice; Soil Crop Suitability; Agricultural Economy Observation;
SupplyChainNode; Drought Stress Indicator; Pest Stress Indicator; Aggregation Receipt. [DOM-AG] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Soil owns canonical soil map-unit and horizon
semantics.; Hydrology owns water observations and flood context.; People/Land owns ownership, title, parcels,
and living-person privacy. [DOM-AG] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Crop Observation CONFIRMED term / PROPOSED
field realization: Crop
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
Field Candidate CONFIRMED term / PROPOSED
field realization: Field
Candidate is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
Yield Observation CONFIRMED term / PROPOSED
field realization: Yield
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
Soil Crop Suitability CONFIRMED term / PROPOSED
field realization: Soil Crop
Suitability is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
Drought Stress Indicator CONFIRMED term / PROPOSED
field realization: Drought
Stress Indicator is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
55

Term Definition Citation
Pest Stress Indicator CONFIRMED term / PROPOSED
field realization: Pest Stress
Indicator is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
Aggregation Receipt CONFIRMED term / PROPOSED
field realization: Aggregation
Receipt is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
MUKEY CONFIRMED term / PROPOSED
field realization: MUKEY is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AG] [ENCY]
Component percentage CONFIRMED term / PROPOSED
field realization: Component
percentage is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
Hydrologic group CONFIRMED term / PROPOSED
field realization: Hydrologic
group is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-AG] [ENCY]
VWC CONFIRMED term / PROPOSED
field realization: VWC is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AG] [ENCY]
Spec hash CONFIRMED term / PROPOSED
field realization: Spec hash is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AG] [ENCY]
D. Key source families.
56

Source family Role Rights / sensitivity Freshness Status
SSURGO / Soil
Data Access
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
gSSURGO authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
Kansas Mesonet authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
NRCS SCAN authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
NOAA USCRN authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
NASA SMAP authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
NASA HLS /
HLS-VI
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
USDA NASS
QuickStats / Crop
Progress
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AG] [ENCY]
E. Main object families.
57

Object Purpose Identity rule Temporal handling
Crop Observation Represents Crop
Observation evidence or
released derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Field Candidate Represents Field
Candidate evidence or
released derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Crop Rotation Represents Crop
Rotation evidence or
released derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Yield Observation Represents Yield
Observation evidence or
released derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Irrigation Link Represents Irrigation
Link evidence or released
derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Conservation Practice Represents Conservation
Practice evidence or
released derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Soil Crop Suitability Represents Soil Crop
Suitability evidence or
released derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Agricultural Economy
Observation
Represents Agricultural
Economy Observation
evidence or released
derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SupplyChainNode Represents
SupplyChainNode
evidence or released
derivative within
Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
58

Drought Stress Indicator Represents Drought
Stress Indicator evidence
or released derivative
within Agriculture.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Agriculture Soil MUKEY joins and
suitability support.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Agriculture Hydrology irrigation, drought,
water-use context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Agriculture Atmosphere/Air weather, heat, smoke,
vegetation stress.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Agriculture People/Land farm/operator and
parcel-sensitive contexts
remain restricted.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include public-safe crop progress maps; aggregate crop-condition view;
soil-crop suitability map; station soil-moisture series; satellite/grid moisture context; vegetation-index context;
drought/pest stress indicators. [DOM-AG] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Agriculture follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [DOM-AG] [ENCY]
59

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Aggregate statistics and satellite products must not become field/operator truth;
farm/operator private data, proprietary yield, pesticide records, and private-sensitive joins fail closed. [DOMAG] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Agriculture
feature/detail resolver;
route TBD
AgricultureDecisionEnvelopeANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Agriculture layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Agriculture Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Agriculture Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
60

K. Validators, tests, fixtures.
• PROPOSED: SSURGO/SDA lineage tests. [DOM-AG] [ENCY]
• PROPOSED: soil-moisture unit/depth/QC tests. [DOM-AG] [ENCY]
• PROPOSED: crop progress aggregate-only tests. [DOM-AG] [ENCY]
• PROPOSED: vegetation index mask/time tests. [DOM-AG] [ENCY]
• PROPOSED: policy denial for field-level NASS claims. [DOM-AG] [ENCY]
• PROPOSED: catalog closure tests. [DOM-AG] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Agriculture EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence
is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-AG]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Agriculture publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-AG] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify NASS/QuickStats and Crop
Progress activation.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Mesonet and HLS/SMAP
product terms.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify public release sensitivity
rules for farm/operator joins.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Agriculture API and layer
registry.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
61

10. Geology and Natural Resources
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern bedrock/surficial geology, stratigraphy,
lithology, structures, boreholes, logs, cores, geophysics, geochemistry, mineral/resource distinctions, extraction/reclamation context, public-safe layers, and bounded AI. [DOM-GEOL] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Geologic Unit; Lithology; Stratigraphic Interval; Geologic Age;
Fault Structure; Borehole; Well Log; Core Sample; Geophysical Observation; Geochemistry Sample; Mineral
Occurrence; Resource Deposit; Extraction Site; Reclamation Record; CrossSection; Hydrostratigraphic Unit.
[DOM-GEOL] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Hydrology measurements, soils, hazards risk,
ownership/lease/permit/title claims, and UI/AI statements remain outside canonical geology truth. [DOMGEOL] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Geologic Unit CONFIRMED term / PROPOSED
field realization: Geologic
Unit is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-GEOL] [ENCY]
Lithology CONFIRMED term / PROPOSED
field realization: Lithology is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-GEOL] [ENCY]
Stratigraphic Interval CONFIRMED term / PROPOSED
field realization:
Stratigraphic Interval is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-GEOL] [ENCY]
StratigraphicCorrelation CONFIRMED term / PROPOSED
field realization:
StratigraphicCorrelation is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-GEOL] [ENCY]
SurficialUnit CONFIRMED term / PROPOSED
field realization: SurficialUnit
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-GEOL] [ENCY]
62

Term Definition Citation
StructureFeature CONFIRMED term / PROPOSED
field realization:
StructureFeature is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-GEOL] [ENCY]
GeologyBoundaryVersion CONFIRMED term / PROPOSED
field realization:
GeologyBoundaryVersion is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-GEOL] [ENCY]
BoreholeReference CONFIRMED term / PROPOSED
field realization:
BoreholeReference is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-GEOL] [ENCY]
Well LogReference CONFIRMED term / PROPOSED
field realization: Well
LogReference is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-GEOL] [ENCY]
Mineral Occurrence CONFIRMED term / PROPOSED
field realization: Mineral
Occurrence is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-GEOL] [ENCY]
ResourceEstimate CONFIRMED term / PROPOSED
field realization:
ResourceEstimate is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-GEOL] [ENCY]
Extraction Site CONFIRMED term / PROPOSED
field realization: Extraction
Site is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-GEOL] [ENCY]
D. Key source families.
63

Source family Role Rights / sensitivity Freshness Status
Kansas Geological
Survey data and
maps
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
KGS surficial
geology and
geologic maps
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
USGS NGMDB
and GeMS
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
KGS oil and gas
wells and
production
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
KCC oil and gas
regulatory data
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
KGS/KDHE
WWC5 and
water-well program
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
KGS LAS digital
well logs and well
tops
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
USGS MRDS authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-GEOL]
[ENCY]
E. Main object families.
64

Object Purpose Identity rule Temporal handling
Geologic Unit Represents Geologic Unit
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SurficialUnit Represents SurficialUnit
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Lithology Represents Lithology
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Stratigraphic Interval Represents Stratigraphic
Interval evidence or
released derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
StructureFeature Represents
StructureFeature
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
GeologyBoundaryVersion Represents
GeologyBoundaryVersion
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
BoreholeReference Represents
BoreholeReference
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Well LogReference Represents Well
LogReference evidence or
released derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Geochemistry
SampleReference
Represents Geochemistry
SampleReference
evidence or released
derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
65

Mineral Occurrence Represents Mineral
Occurrence evidence or
released derivative within
Geology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Geology Soil parent material and
surficial context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Geology Hydrology hydrostratigraphy and
aquifer context without
replacing measurements.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Geology Hazards fault/landslide/subsidence
risk context without
owning risk.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Geology People/Land lease, parcel, operator
relation cannot prove
deposits.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include bedrock unit map; surficial unit map; structure/fault view;
stratigraphy/correlation view; borehole public-generalized view; mineral occurrence/deposit summary; extraction/reclamation context. [DOM-GEOL] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Geology follows RAW -> WORK / QUARANTINE
-> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state transition.
[DIRRULES] [DOM-GEOL] [ENCY]
66

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Exact borehole, sample, sensitive resource, well-log, and private well locations default
to restricted or generalized public geometry. Occurrence, deposit, estimate, permit, production, and reserve
claims must remain distinct. [DOM-GEOL] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Geology feature/detail
resolver; route TBD
GeologyDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Geology layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Geology Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Geology Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
67

K. Validators, tests, fixtures.
• PROPOSED: Source-role validators. [DOM-GEOL] [ENCY]
• PROPOSED: resource-class anti-collapse tests. [DOM-GEOL] [ENCY]
• PROPOSED: public-safe geometry tests. [DOM-GEOL] [ENCY]
• PROPOSED: borehole/well-log rights tests. [DOM-GEOL] [ENCY]
• PROPOSED: catalog closure tests. [DOM-GEOL] [ENCY]
• PROPOSED: AI evidence-before-model tests. [DOM-GEOL] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Geology EvidenceBundles,
compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-GEOL]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Geology publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-GEOL] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify KGS and KCC source
descriptors.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify borehole/well-log public
policy.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Define resource classification
scheme and tests.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify geology API, MapLibre,
and Evidence Drawer integration.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
68

11. Atmosphere and Air
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern air observations, AQI reports, regulatory
archives, low-cost sensors, model fields, remote-sensing masks, climate/anomaly context, fusion products,
meteorological support, advisories, and public-safe products. [DOM-AIR] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: AirStation; AirObservation; PM2.5 Observation; Ozone Observation; SmokeContext; AODRaster; Weather Station; Weather Observation; WindField; Precipitation Observation; Temperature Observation; Climate Normal; Climate Anomaly; Forecast Context; Advisory Context.
[DOM-AIR] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Hazards owns emergency/hazard event truth
and life-safety context. Agriculture, hydrology, habitat, settlements, and other domains own their canonical
claims. [DOM-AIR] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Knowledge character CONFIRMED term / PROPOSED
field realization: Knowledge
character is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-AIR] [ENCY]
OBSERVED_SENSOR CONFIRMED term / PROPOSED
field realization:
OBSERVED_SENSOR is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-AIR] [ENCY]
PUBLIC_AQI_REPORT CONFIRMED term / PROPOSED
field realization:
PUBLIC_AQI_REPORT is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-AIR] [ENCY]
REGULATORY_ARCHIVE CONFIRMED term / PROPOSED
field realization:
REGULATORY_ARCHIVE is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AIR] [ENCY]
LOW_COST_SENSOR CONFIRMED term / PROPOSED
field realization:
LOW_COST_SENSOR is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-AIR] [ENCY]
69

Term Definition Citation
ATMOSPHERIC_MODEL_FIELD CONFIRMED term / PROPOSED
field realization: ATMOSPHERIC_MODEL_FIELD is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AIR] [ENCY]
REMOTE_SENSING_MASK CONFIRMED term / PROPOSED
field realization:
REMOTE_SENSING_MASK is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AIR] [ENCY]
CLIMATE_ANOMALY_CONTEXTCONFIRMED term / PROPOSED
field realization: CLIMATE_ANOMALY_CONTEXT
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AIR] [ENCY]
DERIVED_FUSION CONFIRMED term / PROPOSED
field realization:
DERIVED_FUSION is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-AIR] [ENCY]
METEOROLOGICAL_CONTEXT CONFIRMED term / PROPOSED
field realization: METEOROLOGICAL_CONTEXT is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-AIR] [ENCY]
ALERT_AND_ADVISORY_CONTEXT CONFIRMED term / PROPOSED
field realization:
ALERT_AND_ADVISORY_CONTEXT
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AIR] [ENCY]
NETWORK_AND_SITE_CONTEXTCONFIRMED term / PROPOSED
field realization: NETWORK_AND_SITE_CONTEXT
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-AIR] [ENCY]
D. Key source families.
70

Source family Role Rights / sensitivity Freshness Status
OpenAQ-like
aggregators
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
EPA AQS-like
archive
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
AirNow / agency
reporting
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
CAMS /
ECMWF-family
model fields
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
HRRR-Smoke /
NOAA smoke
forecast
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
HMS smoke authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
GOES/ABI AOD authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
VIIRS fire/hotspot authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-AIR]
[ENCY]
E. Main object families.
71

Object Purpose Identity rule Temporal handling
AirStation Represents AirStation
evidence or released
derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
AirObservation Represents
AirObservation evidence
or released derivative
within Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
PM2.5 Observation Represents PM2.5
Observation evidence or
released derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Ozone Observation Represents Ozone
Observation evidence or
released derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SmokeContext Represents
SmokeContext evidence
or released derivative
within Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
AODRaster Represents AODRaster
evidence or released
derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Weather Station Represents Weather
Station evidence or
released derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Weather Observation Represents Weather
Observation evidence or
released derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
WindField Represents WindField
evidence or released
derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
72

Precipitation
Observation
Represents Precipitation
Observation evidence or
released derivative within
Atmosphere/Air.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Atmosphere/Air Hazards smoke, heat/cold,
advisory, visibility,
fire/emissions context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Atmosphere/Air Agriculture heat, smoke,
precipitation, vegetation
stress.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Atmosphere/Air Hydrology precipitation, drought,
flood-weather forcing.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Atmosphere/Air Biodiversity domains phenology, smoke, fire,
drought stress without
exposing sensitive
locations.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include observed sensor layers; public AQI report layers; regulatory archive
layers; low-cost sensor caveat layers; model-field layers; remote-sensing mask layers; climate/anomaly context;
derived fusion layers; advisory layers. [DOM-AIR] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Atmosphere/Air follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [DOM-AIR] [ENCY]
73

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: AQI is not concentration; AOD is not PM2.5; model fields are not observations;
low-cost sensor public release requires correction, caveats, confidence, and limitations. [DOM-AIR] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Atmosphere/Air
feature/detail resolver;
route TBD
AtmosphereAirDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Atmosphere/Air layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Atmosphere/Air
Evidence Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Atmosphere/Air Focus
Mode answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: Knowledge-character registry tests. [DOM-AIR] [ENCY]
74

• PROPOSED: unit normalization tests. [DOM-AIR] [ENCY]
• PROPOSED: AQI-as-concentration denial. [DOM-AIR] [ENCY]
• PROPOSED: AOD-as-PM2.5 denial. [DOM-AIR] [ENCY]
• PROPOSED: model-as-observed denial. [DOM-AIR] [ENCY]
• PROPOSED: low-cost sensor caveat tests. [DOM-AIR] [ENCY]
• PROPOSED: dryrun no-live-fetch tests. [DOM-AIR] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Atmosphere/Air EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI]
[DOM-AIR] [ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Atmosphere/Air publication requires ReleaseManifest,
EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-AIR] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify source rights and endpoint
behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Implement knowledge-character
registry.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify catalog/proof/release
closure.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify MapLibre/Evidence
Drawer/Focus Mode integration.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
75

12. Hazards
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern historical hazard events, warnings/advisories/watches
as context, disaster declarations, regulatory hazard areas, scientific observations, remote sensing, models,
exposure and resilience summaries, and bounded public runtime answers. [DOM-HAZ] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Hazard Event; Hazard Observation; Warning Context; Advisory Context; Disaster Declaration; Flood Context; Wildfire Detection; SmokeContext; Drought Indicator;
Earthquake Event; Heat Cold Event; Exposure Summary; Resilience Summary; Hazard Timeline; ImpactArea.
[DOM-HAZ] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: KFM Hazards is not an emergency alert system
and must not provide life-safety instructions. Hydrology, Atmosphere/Air, Settlements, Roads, and other lanes
own their canonical sources. [DOM-HAZ] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Hazard Event CONFIRMED term / PROPOSED
field realization: Hazard
Event is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-HAZ] [ENCY]
historical_event_record CONFIRMED term / PROPOSED
field realization:
historical_event_record is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
operational_warning CONFIRMED term / PROPOSED
field realization:
operational_warning is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
operational_advisory CONFIRMED term / PROPOSED
field realization:
operational_advisory is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
operational_watch CONFIRMED term / PROPOSED
field realization:
operational_watch is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
76

Term Definition Citation
administrative_declaration CONFIRMED term / PROPOSED
field realization:
administrative_declaration is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
regulatory_context CONFIRMED term / PROPOSED
field realization:
regulatory_context is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
scientific_observation CONFIRMED term / PROPOSED
field realization:
scientific_observation is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
remote_sensing_detection CONFIRMED term / PROPOSED
field realization:
remote_sensing_detection is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
modeled_derivative CONFIRMED term / PROPOSED
field realization:
modeled_derivative is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
resilience_analysis CONFIRMED term / PROPOSED
field realization:
resilience_analysis is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
unknown_unclassified CONFIRMED term / PROPOSED
field realization:
unknown_unclassified is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-HAZ] [ENCY]
D. Key source families.
77

Source family Role Rights / sensitivity Freshness Status
NOAA Storm
Events /
NCEI-style records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
NWS
alerts/warnings/advisories/watches
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
FEMA Disaster
Declarations /
OpenFEMA
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
FEMA NFHL /
MSC flood hazard
context
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
USGS Earthquake
Catalog
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
NOAA HMS Fire
and Smoke
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
NASA FIRMS
active fire
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
Kansas/local
emergency context
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-HAZ]
[ENCY]
E. Main object families.
78

Object Purpose Identity rule Temporal handling
Hazard Event Represents Hazard Event
evidence or released
derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Hazard Observation Represents Hazard
Observation evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Warning Context Represents Warning
Context evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Advisory Context Represents Advisory
Context evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Disaster Declaration Represents Disaster
Declaration evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Flood Context Represents Flood
Context evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Wildfire Detection Represents Wildfire
Detection evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SmokeContext Represents
SmokeContext evidence
or released derivative
within Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Drought Indicator Represents Drought
Indicator evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
79

Earthquake Event Represents Earthquake
Event evidence or
released derivative within
Hazards.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Hazards Hydrology flood/drought/water
event context with role
separation.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Hazards Atmosphere/Air smoke, heat/cold,
AQI/advisory, wind,
fire-weather context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Hazards Settlements/Infrastructure exposure, lifelines,
dependencies.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Hazards Roads/Rail closures, detours,
bridge/crossing exposure,
resilience.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include historical event layers; operational warning context layers; advisory/watch context; disaster declaration layers; regulatory hazard areas; scientific observation layers; remotesensing detections; exposure/resilience summaries; role-aware hazard timelines. [DOM-HAZ] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Hazards follows RAW -> WORK / QUARANTINE
-> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state transition.
[DIRRULES] [DOM-HAZ] [ENCY]
80

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Operational warning products are contextual only and not for life safety; unknown
source roles are quarantined; expired operational context cannot appear as current warning state. [DOM-HAZ]
[ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Hazards feature/detail
resolver; route TBD
HazardsDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Hazards layer manifest
resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Hazards Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Hazards Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
81

K. Validators, tests, fixtures.
• PROPOSED: Source-role anti-collapse tests. [DOM-HAZ] [ENCY]
• PROPOSED: temporal-role validators. [DOM-HAZ] [ENCY]
• PROPOSED: emergency-alert denial. [DOM-HAZ] [ENCY]
• PROPOSED: operational expiry/freshness tests. [DOM-HAZ] [ENCY]
• PROPOSED: catalog closure tests. [DOM-HAZ] [ENCY]
• PROPOSED: Evidence Drawer disclaimer tests. [DOM-HAZ] [ENCY]
• PROPOSED: UI no-direct-source tests. [DOM-HAZ] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Hazards EvidenceBundles,
compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-HAZ]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Hazards publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-HAZ] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify official source endpoints
and rights.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Implement role taxonomy and
freshness states.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify emergency-alert boundary
enforcement.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify release/correction/rollback
drill.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
82

13. Roads, Rail, and Trade Routes
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern Kansas roads, rail, historic routes, trade and mobility corridors, restrictions, facilities, graph projections, catalog/proof/release objects, governed APIs, MapLibre UI, Evidence Drawer, Focus Mode, correction, and rollback. [DOM-ROADS] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Road Segment; Historic Route; Rail Segment; Depot; Siding;
Yard; Crossing; Bridge; Ferry; River Crossing; Freight Corridor; Route Event; Operator Status; Access Restriction; Network Edge; Movement Story Node. [DOM-ROADS] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Settlements owns settlement and infrastructure
canonical claims. Hydrology owns water evidence. Archaeology/People/Land/Hazards retain their truth and
sensitivity policies. [DOM-ROADS] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Road Segment CONFIRMED term / PROPOSED
field realization: Road
Segment is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-ROADS] [ENCY]
Rail Segment CONFIRMED term / PROPOSED
field realization: Rail
Segment is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-ROADS] [ENCY]
CorridorRoute CONFIRMED term / PROPOSED
field realization:
CorridorRoute is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ROADS] [ENCY]
RouteMembership CONFIRMED term / PROPOSED
field realization:
RouteMembership is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ROADS] [ENCY]
Network Node CONFIRMED term / PROPOSED
field realization: Network
Node is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-ROADS] [ENCY]
83

Term Definition Citation
Crossing CONFIRMED term / PROPOSED
field realization: Crossing is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-ROADS] [ENCY]
TransportFacility CONFIRMED term / PROPOSED
field realization:
TransportFacility is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ROADS] [ENCY]
RestrictionEvent CONFIRMED term / PROPOSED
field realization:
RestrictionEvent is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ROADS] [ENCY]
StatusEvent CONFIRMED term / PROPOSED
field realization: StatusEvent
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-ROADS] [ENCY]
OperatorAssignment CONFIRMED term / PROPOSED
field realization:
OperatorAssignment is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ROADS] [ENCY]
Historic RouteClaim CONFIRMED term / PROPOSED
field realization: Historic
RouteClaim is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ROADS] [ENCY]
TradeRouteCorridor CONFIRMED term / PROPOSED
field realization:
TradeRouteCorridor is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ROADS] [ENCY]
D. Key source families.
84

Source family Role Rights / sensitivity Freshness Status
Census
TIGER/Line roads
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
FHWA HPMS authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
FHWA National
Highway Freight
Network
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
WZDx feeds authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
KDOT / KanPlan /
KanDrive / Kansas
GIS
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
county/state bridge
and restriction data
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
GNIS names authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
OpenStreetMap authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ROADS]
[ENCY]
E. Main object families.
85

Object Purpose Identity rule Temporal handling
Road Segment Represents Road
Segment evidence or
released derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Rail Segment Represents Rail Segment
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
CorridorRoute Represents
CorridorRoute evidence
or released derivative
within Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
RouteMembership Represents
RouteMembership
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Network Node Represents Network
Node evidence or
released derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Crossing Represents Crossing
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Bridge Represents Bridge
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Ferry Represents Ferry
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
TransportFacility Represents
TransportFacility
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
86

RestrictionEvent Represents
RestrictionEvent
evidence or released
derivative within
Roads/Rail.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Roads/Rail Settlements/Infrastructure depots, crossings,
facilities, dependencies.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Roads/Rail Hydrology bridge/ferry/ford/river
crossing.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Roads/Rail Hazards closure, detour,
flood/fire/smoke
exposure.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Roads/Rail Archaeology/Cultural
Heritage
historic routes,
Indigenous corridors,
forts, missions.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include modern roads layer; rail alignment layer; facility/crossing view;
restriction/status timeline; freight-corridor context; historic route claim view; generalized trade-route corridor;
derived graph/connectivity view. [DOM-ROADS] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Roads/Rail follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [DOM-ROADS] [ENCY]
87

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Indigenous trade and mobility corridors, oral history, treaty, cultural, and interpretive
evidence default to steward review and generalized public geometry. Critical transport facilities require review.
[DOM-ROADS] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Roads/Rail
feature/detail resolver;
route TBD
RoadsRailDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Roads/Rail layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Roads/Rail Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Roads/Rail Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
88

K. Validators, tests, fixtures.
• PROPOSED: Route membership and designation separation tests. [DOM-ROADS] [ENCY]
• PROPOSED: operator/status temporal tests. [DOM-ROADS] [ENCY]
• PROPOSED: OSM/GNIS legal-status denial. [DOM-ROADS] [ENCY]
• PROPOSED: historic overprecision denial. [DOM-ROADS] [ENCY]
• PROPOSED: public generalization receipt tests. [DOM-ROADS] [ENCY]
• PROPOSED: transport graph projection rollback tests. [DOM-ROADS] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Roads/Rail EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-ROADS]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Roads/Rail publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-ROADS] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify
KDOT/FHWA/FRA/WZDx/source
terms.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify Indigenous/cultural
corridor policy.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Implement
RouteUncertaintyProfile.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify transport graph and
MapLibre integration.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
89

14. Settlements and Infrastructure
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern settlements, municipalities, census places, historic townsites, ghost towns, forts, missions, reservation communities, infrastructure assets, networks, facilities, service areas, operators, condition observations, dependencies, and public-safe representations. [DOMSETTLE] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Settlement; Municipality; CensusPlace; Townsite; GhostTown;
Fort; Mission; ReservationCommunity; Infrastructure Asset; Network Node; Network Segment; Facility; Service
Area; Operator; Condition Observation; Dependency. [DOM-SETTLE] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Roads/Rail owns transport routes. Hydrology
owns water evidence. Hazards owns hazard events and warnings. People/Land owns ownership and livingperson privacy. [DOM-SETTLE] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Settlement CONFIRMED term / PROPOSED
field realization: Settlement
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
Municipality CONFIRMED term / PROPOSED
field realization: Municipality
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
CensusPlace CONFIRMED term / PROPOSED
field realization: CensusPlace
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
Townsite CONFIRMED term / PROPOSED
field realization: Townsite is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
GhostTown CONFIRMED term / PROPOSED
field realization: GhostTown
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
90

Term Definition Citation
Fort CONFIRMED term / PROPOSED
field realization: Fort is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SETTLE] [ENCY]
Mission CONFIRMED term / PROPOSED
field realization: Mission is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
ReservationCommunity CONFIRMED term / PROPOSED
field realization:
ReservationCommunity is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SETTLE] [ENCY]
Infrastructure Asset CONFIRMED term / PROPOSED
field realization:
Infrastructure Asset is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-SETTLE] [ENCY]
Network Node CONFIRMED term / PROPOSED
field realization: Network
Node is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-SETTLE] [ENCY]
Network Segment CONFIRMED term / PROPOSED
field realization: Network
Segment is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[DOM-SETTLE] [ENCY]
Facility CONFIRMED term / PROPOSED
field realization: Facility is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-SETTLE] [ENCY]
D. Key source families.
91

Source family Role Rights / sensitivity Freshness Status
Census TIGER /
census place
geography
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
GNIS and
gazetteers
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
state/local GIS /
Kansas
Geoportal-style
sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
municipal and local
legal records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
historical gazetteers
and maps
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
infrastructure
operators and
providers
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
KDOT / bridge /
facility sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
FEMA / hazards /
resilience sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-SETTLE]
[ENCY]
E. Main object families.
92

Object Purpose Identity rule Temporal handling
Settlement Represents Settlement
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Municipality Represents Municipality
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
CensusPlace Represents CensusPlace
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Townsite Represents Townsite
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
GhostTown Represents GhostTown
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Fort Represents Fort evidence
or released derivative
within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Mission Represents Mission
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ReservationCommunity Represents
ReservationCommunity
evidence or released
derivative within Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Infrastructure Asset Represents Infrastructure
Asset evidence or
released derivative within
Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
93

Network Node Represents Network
Node evidence or
released derivative within
Settlements/Infrastructure.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Settlements/Infrastructure Roads/Rail depot, bridge, crossing,
transport facility
relation.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Settlements/Infrastructure Hazards exposure, resilience,
warnings, declarations.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Settlements/Infrastructure Hydrology water, wastewater,
stormwater, floodplain,
drainage.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Settlements/Infrastructure People/Land residence, ownership,
parcel, migration context
with restrictions.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include current settlement view; historic townsite view; legal-status-event
view; census-place comparison; public-safe asset view; service-area aggregate view; dependency-summary view;
restricted internal review view. [DOM-SETTLE] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Settlements/Infrastructure follows RAW -> WORK /
QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed
state transition. [DIRRULES] [DOM-SETTLE] [ENCY]
94

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Critical infrastructure, utilities, condition observations, dependencies, operatorsensitive details, and exact facility geometry default to restricted or review. [DOM-SETTLE] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Settlements/Infrastructure
feature/detail resolver;
route TBD
SettlementsInfrastructureDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Settlements/Infrastructure
layer manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Settlements/Infrastructure
Evidence Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Settlements/Infrastructure
Focus Mode answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas / contracts / v1
/
finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: Legal municipality evidence tests. [DOM-SETTLE] [ENCY]
95

• PROPOSED: census-vs-municipality distinction. [DOM-SETTLE] [ENCY]
• PROPOSED: infrastructure topology tests. [DOM-SETTLE] [ENCY]
• PROPOSED: condition observed_at tests. [DOM-SETTLE] [ENCY]
• PROPOSED: restricted geometry no-leak tests. [DOM-SETTLE] [ENCY]
• PROPOSED: catalog/proof/release closure tests. [DOM-SETTLE] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Settlements/Infrastructure
EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN
when evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request.
[GAI] [DOM-SETTLE] [ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Settlements/Infrastructure publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state
rule, and rollback target. [ENCY Appendix E] [DOM-SETTLE] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify source rights and municipal
legal-source roles.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify critical infrastructure
policy.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify public-safe layer registry. mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify API and Focus Mode
auth/policy behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
96

15. Archaeology and Cultural Heritage
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern archaeological sites, surveys, artifacts, contexts,
excavation units, remote-sensing and LiDAR candidates, geophysics, 3D documentation, cultural/steward
review, chronology, sensitivity transforms, and public-safe summaries. [DOM-ARCH] [ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Archaeological Site; Survey; Artifact; Feature; Context; ExcavationUnit; Remote Sensing Anomaly; LiDAR Candidate; Geophysics Observation; 3D Documentation; Cultural
Review; Steward Review; Collection Accession; Chronology Assertion; Sensitivity Transform. [DOM-ARCH]
[ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Roads/Rail, People/Land, Geology, Hazards,
and Spatial Foundation supply context but cannot confirm sites or bypass archaeological sensitivity. [DOMARCH] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Archaeological Site CONFIRMED term / PROPOSED
field realization:
Archaeological Site is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ARCH] [ENCY]
SiteComponent CONFIRMED term / PROPOSED
field realization:
SiteComponent is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ARCH] [ENCY]
CulturalTemporalPeriod CONFIRMED term / PROPOSED
field realization:
CulturalTemporalPeriod is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ARCH] [ENCY]
SurveyProject CONFIRMED term / PROPOSED
field realization:
SurveyProject is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ARCH] [ENCY]
SurveyTransect CONFIRMED term / PROPOSED
field realization:
SurveyTransect is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ARCH] [ENCY]
97

Term Definition Citation
ExcavationUnit CONFIRMED term / PROPOSED
field realization:
ExcavationUnit is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ARCH] [ENCY]
ProvenienceContext CONFIRMED term / PROPOSED
field realization:
ProvenienceContext is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ARCH] [ENCY]
StratigraphicUnit CONFIRMED term / PROPOSED
field realization:
StratigraphicUnit is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ARCH] [ENCY]
ArtifactRecord CONFIRMED term / PROPOSED
field realization:
ArtifactRecord is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-ARCH] [ENCY]
CollectionRepositoryRecord CONFIRMED term / PROPOSED
field realization:
CollectionRepositoryRecord is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-ARCH] [ENCY]
CandidateFeature CONFIRMED term / PROPOSED
field realization:
CandidateFeature is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-ARCH] [ENCY]
PublicationTransformReceipt CONFIRMED term / PROPOSED
field realization:
PublicationTransformReceipt is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-ARCH] [ENCY]
D. Key source families.
98

Source family Role Rights / sensitivity Freshness Status
State site inventory
/ SHPO or
equivalent
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
public NRHP-like
listings
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
field survey forms authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
excavation records
and provenience
packets
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
artifact/collection/repository
records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
lab reports authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
historic
maps/plats/land
records/newspapers
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
oral history and
cultural knowledge
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-ARCH]
[ENCY]
E. Main object families.
99

Object Purpose Identity rule Temporal handling
Archaeological Site Represents
Archaeological Site
evidence or released
derivative within
Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SiteComponent Represents
SiteComponent evidence
or released derivative
within Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
CulturalTemporalPeriod Represents
CulturalTemporalPeriod
evidence or released
derivative within
Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SurveyProject Represents
SurveyProject evidence
or released derivative
within Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
SurveyTransect Represents
SurveyTransect evidence
or released derivative
within Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ShovelTest Represents ShovelTest
evidence or released
derivative within
Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
TestUnit Represents TestUnit
evidence or released
derivative within
Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ExcavationUnit Represents
ExcavationUnit evidence
or released derivative
within Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ProvenienceContext Represents
ProvenienceContext
evidence or released
derivative within
Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
100

StratigraphicUnit Represents
StratigraphicUnit
evidence or released
derivative within
Archaeology.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Archaeology Spatial Foundation exact/public geometry
split and transform
receipts.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Archaeology Roads/Rail historic routes and
cultural paths.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Archaeology Settlements forts, missions, townsites,
reservation communities.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Archaeology Hazards threat, erosion, fire,
flood, exposure context
with exact-site denial.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include public generalized site summaries; public survey-coverage summaries; candidate-feature surfaces; remote-sensing anomaly surfaces; steward-only review maps; restricted
exact-geometry review; chronology/context views; threat/risk review views. [DOM-ARCH] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Archaeology follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [DOM-ARCH] [ENCY]
101

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Exact archaeological locations, burial, human remains, sacred sites, unresolved cultural sensitivity, collection security, private landowner details, and looting-risk exposure fail closed. [DOMARCH] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Archaeology
feature/detail resolver;
route TBD
ArchaeologyDecisionEnvelopeANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Archaeology layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Archaeology Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Archaeology Focus Mode
answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
102

K. Validators, tests, fixtures.
• PROPOSED: EvidenceBundle-required tests. [DOM-ARCH] [ENCY]
• PROPOSED: candidate-not-site tests. [DOM-ARCH] [ENCY]
• PROPOSED: public no-leak tests. [DOM-ARCH] [ENCY]
• PROPOSED: rights and cultural-review tests. [DOM-ARCH] [ENCY]
• PROPOSED: exact sensitive geometry denial. [DOM-ARCH] [ENCY]
• PROPOSED: catalog closure tests. [DOM-ARCH] [ENCY]
• PROPOSED: AI exact-location denial. [DOM-ARCH] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Archaeology EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is
insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [DOM-ARCH]
[ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Archaeology publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [DOM-ARCH] [ENCY]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify steward authority and
confidentiality.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Define public geometry thresholds
and transform profiles.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify oral history/cultural
knowledge protocol.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify emergency public-layer
disablement and rollback drill.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
103

16. People, Genealogy, DNA, and Land Ownership
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern assertion-first person evidence, genealogy relationships, restricted DNA evidence, land instruments, ownership intervals, chain-of-title reasoning, consent,
policy decisions, review, correction, graph projection, EvidenceBundle views, and rollback. [DOM-PEOPLE]
[ENCY]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Person Assertion; Person Identity Candidate; Genealogy Relationship; FamilyGroup; LifeEvent; Residence Event; Migration Event; Land Ownership Assertion; Deed
Instrument; Title Instrument; Assessor Record; TaxRecord; Parcel Version; Ownership Interval; DNA Match
Evidence; Relationship Hypothesis. [DOM-PEOPLE] [ENCY]
CONFIRMED / PROPOSED: This domain explicitly does not own: Settlements, roads, archaeology, hydrology,
agriculture, hazards, and spatial foundation provide context but do not weaken living-person, DNA, title, or
parcel-boundary controls. [DOM-PEOPLE] [ENCY]
C. Ubiquitous language.
Term Definition Citation
Person Assertion CONFIRMED term / PROPOSED
field realization: Person
Assertion is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-PEOPLE] [ENCY]
PersonCanonical CONFIRMED term / PROPOSED
field realization:
PersonCanonical is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-PEOPLE] [ENCY]
NameAssertion CONFIRMED term / PROPOSED
field realization:
NameAssertion is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-PEOPLE] [ENCY]
LifeEvent CONFIRMED term / PROPOSED
field realization: LifeEvent is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-PEOPLE] [ENCY]
RelationshipAssertion CONFIRMED term / PROPOSED
field realization:
RelationshipAssertion is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-PEOPLE] [ENCY]
104

Term Definition Citation
DNA Match Evidence CONFIRMED term / PROPOSED
field realization: DNA Match
Evidence is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-PEOPLE] [ENCY]
DNAKitToken CONFIRMED term / PROPOSED
field realization:
DNAKitToken is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-PEOPLE] [ENCY]
ConsentGrant CONFIRMED term / PROPOSED
field realization:
ConsentGrant is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-PEOPLE] [ENCY]
RevocationReceipt CONFIRMED term / PROPOSED
field realization:
RevocationReceipt is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-PEOPLE] [ENCY]
LandParcel CONFIRMED term / PROPOSED
field realization: LandParcel
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[DOM-PEOPLE] [ENCY]
LegalDescription CONFIRMED term / PROPOSED
field realization:
LegalDescription is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[DOM-PEOPLE] [ENCY]
LandInstrument CONFIRMED term / PROPOSED
field realization:
LandInstrument is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[DOM-PEOPLE] [ENCY]
D. Key source families.
105

Source family Role Rights / sensitivity Freshness Status
vital/cemetery/burial/obituary/church/school/military/census/directory/court/probate
records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-PEOPLE]
[ENCY]
GEDCOM/GEDZip/tree
overlays
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-PEOPLE]
[ENCY]
DNA vendor match
CSV/segment/triangulation
data
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-PEOPLE]
[ENCY]
patent/deed/mortgage/lien/easement/lease/mineral/water/access/probate
instruments
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-PEOPLE]
[ENCY]
assessor and tax
roll records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-PEOPLE]
[ENCY]
plat/survey/metes/bounds/PLSS/subdivision/derived
geometry
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[DOM-PEOPLE]
[ENCY]
E. Main object families.
Object Purpose Identity rule Temporal handling
Person Assertion Represents Person
Assertion evidence or
released derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
PersonCanonical Represents
PersonCanonical
evidence or released
derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
NameAssertion Represents
NameAssertion evidence
or released derivative
within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
106

Object Purpose Identity rule Temporal handling
LifeEvent Represents LifeEvent
evidence or released
derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Residence Event Represents Residence
Event evidence or
released derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Migration Event Represents Migration
Event evidence or
released derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Genealogy Relationship Represents Genealogy
Relationship evidence or
released derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
FamilyGroup Represents FamilyGroup
evidence or released
derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
DNA Match Evidence Represents DNA Match
Evidence evidence or
released derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
DNASegment Represents DNASegment
evidence or released
derivative within
People/DNA/Land.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
People/DNA/Land Settlements residence, cemetery,
school, court, county,
township, place relation.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
People/DNA/Land Roads/Rail migration, access,
movement.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
107

This domain Related lane Relation type Constraint
People/DNA/Land Archaeology historic person, land,
documentary,
cultural-place context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
People/DNA/Land Agriculture farm, land use,
producer-adjacent
context with privacy.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include historical person profile maps; residence/event timelines; migration paths with uncertainty; land parcel context with warnings; chain-of-title summaries; instrument timeline
views; restricted DNA/consent review; living-person review. [DOM-PEOPLE] [ENCY]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: People/DNA/Land follows RAW -> WORK /
QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a
governed state transition. [DIRRULES] [DOM-PEOPLE] [ENCY]
Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
108

I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Living-person output and DNA-derived outputs are denied or restricted by default;
raw kit/vendor IDs and DNA segments are not public; assessor/tax records and parcel geometry are not title
truth. [DOM-PEOPLE] [ENCY]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
People/DNA/Land
feature/detail resolver;
route TBD
PeopleDNALandDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
People/DNA/Land layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
People/DNA/Land
Evidence Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
People/DNA/Land
Focus Mode answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas/contracts/v1/ finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
K. Validators, tests, fixtures.
• PROPOSED: Person assertion evidence tests. [DOM-PEOPLE] [ENCY]
• PROPOSED: GEDCOM import rights/living-flag tests. [DOM-PEOPLE] [ENCY]
• PROPOSED: DNA consent and raw-ID no-log tests. [DOM-PEOPLE] [ENCY]
• PROPOSED: revocation cleanup tests. [DOM-PEOPLE] [ENCY]
• PROPOSED: legal-description and chain-of-title gap tests. [DOM-PEOPLE] [ENCY]
• PROPOSED: assessor-as-title denial. [DOM-PEOPLE] [ENCY]
• PROPOSED: graph projection safety tests. [DOM-PEOPLE] [ENCY]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released People/DNA/Land EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when
evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI]
[DOM-PEOPLE] [ENCY]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: People/DNA/Land publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule,
and rollback target. [ENCY Appendix E] [DOM-PEOPLE] [ENCY]
109

N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify living-person policy. mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify DNA consent/revocation
enforcement.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify land instrument chain logic. mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify geometry-role boundary
logic.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify UI/API restricted field
no-leak behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
110

17. Frontier Demography / Economy / Settlement / Land / Time Matrix
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern county-year panels, geography versions, frontier
definitions, population/economic/agriculture/access observations, settlement status, public land and land-office
data, boundary changes, crosswalks, uncertainty, threshold models, and matrix releases. [ENCY] [UNIFIED]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Frontier Definition; GeographyVersion; County-Year Panel; Population Observation; Economic Observation; Agriculture Observation; Access Observation; Settlement Status;
Land Office Record; Public Land Record; Admin Boundary Change; Crosswalk; Uncertainty Class; Frontier
Threshold Model; Matrix Release. [ENCY] [UNIFIED]
CONFIRMED / PROPOSED: This domain explicitly does not own: People/DNA/Land owns living-person, DNA,
title, parcel, and ownership decisions. Roads/Rail owns route/corridor semantics. Settlements owns legal and
infrastructure status. [ENCY] [UNIFIED]
C. Ubiquitous language.
Term Definition Citation
Frontier Definition CONFIRMED term / PROPOSED
field realization: Frontier
Definition is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
County-Year Panel CONFIRMED term / PROPOSED
field realization: County-Year
Panel is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
GeographyVersion CONFIRMED term / PROPOSED
field realization:
GeographyVersion is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [UNIFIED]
Population Observation CONFIRMED term / PROPOSED
field realization: Population
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
Economic Observation CONFIRMED term / PROPOSED
field realization: Economic
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
111

Term Definition Citation
Agriculture Observation CONFIRMED term / PROPOSED
field realization: Agriculture
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
Access Observation CONFIRMED term / PROPOSED
field realization: Access
Observation is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
Settlement Status CONFIRMED term / PROPOSED
field realization: Settlement
Status is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
Land Office Record CONFIRMED term / PROPOSED
field realization: Land Office
Record is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
Public Land Record CONFIRMED term / PROPOSED
field realization: Public Land
Record is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [UNIFIED]
Admin Boundary Change CONFIRMED term / PROPOSED
field realization: Admin
Boundary Change is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [UNIFIED]
Crosswalk CONFIRMED term / PROPOSED
field realization: Crosswalk is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[ENCY] [UNIFIED]
D. Key source families.
112

Source family Role Rights / sensitivity Freshness Status
Census decennial,
ACS, historical
datasets
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
Census/TIGER
geography
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
GNIS and
gazetteers
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
NASS and
agricultural
historical statistics
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
land office and
public land records
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
rail/road/market
access sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
historical gazetteers
and maps
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
economic statistics
and county
histories
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY] [UNIFIED]
E. Main object families.
113

Object Purpose Identity rule Temporal handling
Frontier Definition Represents Frontier
Definition evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
GeographyVersion Represents
GeographyVersion
evidence or released
derivative within Frontier
Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
County-Year Panel Represents County-Year
Panel evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Population Observation Represents Population
Observation evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Economic Observation Represents Economic
Observation evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Agriculture Observation Represents Agriculture
Observation evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Access Observation Represents Access
Observation evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Settlement Status Represents Settlement
Status evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Land Office Record Represents Land Office
Record evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
114

Public Land Record Represents Public Land
Record evidence or
released derivative within
Frontier Matrix.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Frontier Matrix People/Land public land and
land-office context
without living/DNA/title
leakage.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Frontier Matrix Settlements settlement status and
municipality/censusplace relation.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Frontier Matrix Roads/Rail access observations and
transport context.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Frontier Matrix Agriculture aggregate agricultural
statistics.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include frontier county-year dashboard; time slider; county panel map;
threshold model comparison; settlement/access overlay; land office/public land layer; uncertainty view; matrix
cell inspector. [ENCY] [UNIFIED]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Frontier Matrix follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [ENCY] [UNIFIED]
115

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: Aggregate county-year outputs are the safest first public posture; sensitive joins to
living persons, DNA, exact archaeology, rare species/plants, and critical infrastructure are denied or generalized.
[ENCY] [UNIFIED]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Frontier Matrix
feature/detail resolver;
route TBD
FrontierMatrixDecisionEnvelope ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Frontier Matrix layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Frontier Matrix Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Frontier Matrix Focus
Mode answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas / contracts / v1
/
finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
116

K. Validators, tests, fixtures.
• PROPOSED: GeographyVersion and Crosswalk tests. [ENCY] [UNIFIED]
• PROPOSED: temporal role separation. [ENCY] [UNIFIED]
• PROPOSED: measure/unit tests. [ENCY] [UNIFIED]
• PROPOSED: evidence closure for matrix cells. [ENCY] [UNIFIED]
• PROPOSED: policy denial for sensitive joins. [ENCY] [UNIFIED]
• PROPOSED: Matrix Release rollback tests. [ENCY] [UNIFIED]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Frontier Matrix EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI]
[ENCY] [UNIFIED]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Frontier Matrix publication requires ReleaseManifest,
EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [ENCY] [UNIFIED]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify exact UNIFIED source
binding and mounted repo status.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Implement Frontier Definition
registry.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Build one county-year panel
fixture.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify source rights and crosswalk
logic.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify matrix cell inspector and
Focus behavior.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
117

18. Planetary, 3D, Digital Twin, and Synthetic Spatial Systems
A. Domain identity and one-line purpose.
CONFIRMED doctrine / PROPOSED implementation: Govern terrain models, 3D tile sets, glTF assets, point
clouds, digital-twin views, synthetic surfaces, scene manifests, representation receipts, reality-boundary notes,
3D admission decisions, and public-safe scenes. [ENCY] [MAP-MASTER] [UIAI]
B. Scope, boundary, and explicit non-ownership.
CONFIRMED / PROPOSED: This domain owns: Scene Manifest; Terrain Model; 3D Tile Set; glTF Asset; Point
Cloud; Digital Twin View; Synthetic Surface; ViewState; Representation Receipt; Reality Boundary Note; 3D
Admission Decision. [ENCY] [MAP-MASTER] [UIAI]
CONFIRMED / PROPOSED: This domain explicitly does not own: This lane renders, relates, or represents released
governed evidence; it does not own geology, hydrology, archaeology, settlements, infrastructure, hazards, habitat, fauna, flora, people, land, roads, agriculture, soil, or atmosphere truth. [ENCY] [MAP-MASTER] [UIAI]
C. Ubiquitous language.
Term Definition Citation
Scene Manifest CONFIRMED term / PROPOSED
field realization: Scene
Manifest is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER] [UIAI]
Terrain Model CONFIRMED term / PROPOSED
field realization: Terrain
Model is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER] [UIAI]
3D Tile Set CONFIRMED term / PROPOSED
field realization: 3D Tile Set
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[ENCY] [MAP-MASTER] [UIAI]
glTF Asset CONFIRMED term / PROPOSED
field realization: glTF Asset
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[ENCY] [MAP-MASTER] [UIAI]
Point Cloud CONFIRMED term / PROPOSED
field realization: Point Cloud
is used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[ENCY] [MAP-MASTER] [UIAI]
118

Term Definition Citation
Digital Twin View CONFIRMED term / PROPOSED
field realization: Digital Twin
View is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER] [UIAI]
Synthetic Surface CONFIRMED term / PROPOSED
field realization: Synthetic
Surface is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER] [UIAI]
ViewState CONFIRMED term / PROPOSED
field realization: ViewState is
used inside this domain with
meaning constrained by source
role, evidence, time, and release
state.
[ENCY] [MAP-MASTER] [UIAI]
Representation Receipt CONFIRMED term / PROPOSED
field realization:
Representation Receipt is used
inside this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER] [UIAI]
Reality Boundary Note CONFIRMED term / PROPOSED
field realization: Reality
Boundary Note is used inside this
domain with meaning constrained
by source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER] [UIAI]
3D Admission Decision CONFIRMED term / PROPOSED
field realization: 3D
Admission Decision is used inside
this domain with meaning
constrained by source role,
evidence, time, and release state.
[ENCY] [MAP-MASTER] [UIAI]
3D as carrier CONFIRMED term / PROPOSED
field realization: 3D as
carrier is used inside this domain
with meaning constrained by
source role, evidence, time, and
release state.
[ENCY] [MAP-MASTER] [UIAI]
D. Key source families.
119

Source family Role Rights / sensitivity Freshness Status
USGS 3DEP and
terrain sources
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
LiDAR and
point-cloud
collections
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
3D Tiles and glTF
assets
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
terrain services and
imagery
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
3D archaeology
documentation
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
synthetic and
model surfaces
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
planetary datasets authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
MapLibre/tile/renderer
artifacts
authority /
observation /
context / model as
source role requires
rights and current
terms NEEDS
VERIFICATION;
sensitive joins fail
closed
source-vintage or
cadence specific
[ENCY]
[MAP-MASTER]
[UIAI]
E. Main object families.
120

Object Purpose Identity rule Temporal handling
Scene Manifest Represents Scene
Manifest evidence or
released derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Terrain Model Represents Terrain
Model evidence or
released derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
3D Tile Set Represents 3D Tile Set
evidence or released
derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
glTF Asset Represents glTF Asset
evidence or released
derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Point Cloud Represents Point Cloud
evidence or released
derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Digital Twin View Represents Digital Twin
View evidence or released
derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Synthetic Surface Represents Synthetic
Surface evidence or
released derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
ViewState Represents ViewState
evidence or released
derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
Representation Receipt Represents
Representation Receipt
evidence or released
derivative within
Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
121

Reality Boundary Note Represents Reality
Boundary Note evidence
or released derivative
within Planetary/3D.
PROPOSED deterministic
basis: source id + object
role + temporal scope +
normalized digest.
CONFIRMED source,
observed, valid, retrieval,
release, and correction
times stay distinct where
material.
F. Cross-lane relations.
This domain Related lane Relation type Constraint
Planetary/3D Spatial Foundation CRS, vertical datum,
terrain, geometry
support.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Planetary/3D Archaeology 3D documentation and
cultural review.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Planetary/3D Infrastructure critical
facility/dependency
scene exposure controls.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
Planetary/3D Hazards scenario/exposure
context without
emergency instruction.
CONFIRMED / PROPOSED
relation must preserve
ownership, source role,
sensitivity, and
EvidenceBundle support.
G. Map and viewing products.
PROPOSED: Domain viewing products include terrain evidence view; point-cloud review view; 3D tile scene view;
glTF asset inspection; digital-twin composite view; synthetic-surface comparison; reality-boundary overlay; 3D
admission review view; planetary reference view. [ENCY] [MAP-MASTER] [UIAI]
CONFIRMED doctrine: Cross-cutting viewing products include Evidence Drawer, time-aware state, trust
badges, sensitivity-redacted view, correction/stale-state view, and governed Focus Mode. [MAP-MASTER]
[GAI]
H. Pipeline shape (RAW -> PUBLISHED).
CONFIRMED doctrine / PROPOSED lane application: Planetary/3D follows RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED, with promotion as a governed state
transition. [DIRRULES] [ENCY] [MAP-MASTER] [UIAI]
122

Stage Handling Gate Status
RAW Capture immutable
source payload or
reference with source
role, rights, sensitivity,
citation, time, and hash.
SourceDescriptor exists. PROPOSED
WORK /
QUARANTINE
Normalize schema,
geometry, time, identity,
evidence, rights, and
policy; hold failures.
Validation and policy
gate pass, or quarantine
reason is recorded.
PROPOSED
PROCESSED Emit validated
normalized objects,
receipts, and public-safe
candidates.
EvidenceRef,
ValidationReport, and
digest closure exist.
PROPOSED
CATALOG / TRIPLET Emit catalog records,
EvidenceBundles,
graph/triplet projections,
and release candidates.
Catalog/proof closure
passes.
PROPOSED
PUBLISHED Serve released public-safe
artifacts through
governed APIs and
manifests.
ReleaseManifest,
correction path, rollback
target, and review/policy
state exist.
PROPOSED
I. Sensitivity, rights, and publication posture.
CONFIRMED / PROPOSED: 3D scenes are higher-exposure carriers; public 3D should use generalized/lowerresolution/clipped/withheld content where sensitive. Synthetic surfaces require Reality Boundary Note.
[ENCY] [MAP-MASTER] [UIAI]
CONFIRMED doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent
release state blocks public promotion. [ENCY] [DIRRULES]
J. API, contract, and schema surfaces.
Endpoint or artifact DTO / schema Outcomes Status
Planetary/3D
feature/detail resolver;
route TBD
Planetary3DDecisionEnvelopeANSWER / ABSTAIN /
DENY / ERROR
PROPOSED governed API
surface; exact route
UNKNOWN.
Planetary/3D layer
manifest resolver
LayerManifest / domain
layer descriptor
ANSWER / DENY / ERROR PROPOSED; public-safe
release only.
Planetary/3D Evidence
Drawer payload
EvidenceDrawerPayload
+ EvidenceBundle
projection
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; evidence and
policy filtered.
Planetary/3D Focus
Mode answer
Runtime Response
Envelope + AIReceipt
ANSWER / ABSTAIN /
DENY / ERROR
PROPOSED; AI never root
truth.
Schema responsibility
root
schemas / contracts / v1
/
finite validator outcomes PROPOSED; verify with
Directory Rules and
ADR. [DIRRULES]
123

K. Validators, tests, fixtures.
• PROPOSED: 3D admission validators. [ENCY] [MAP-MASTER] [UIAI]
• PROPOSED: Scene Manifest closure tests. [ENCY] [MAP-MASTER] [UIAI]
• PROPOSED: terrain CRS/vertical datum tests. [ENCY] [MAP-MASTER] [UIAI]
• PROPOSED: point-cloud sensitivity tests. [ENCY] [MAP-MASTER] [UIAI]
• PROPOSED: synthetic-as-observed denial. [ENCY] [MAP-MASTER] [UIAI]
• PROPOSED: no-leak tests for sensitive domains. [ENCY] [MAP-MASTER] [UIAI]
• PROPOSED: renderer-boundary tests. [ENCY] [MAP-MASTER] [UIAI]
L. Governed AI behavior for this domain.
CONFIRMED doctrine / PROPOSED implementation: AI may summarize released Planetary/3D EvidenceBundles, compare evidence, explain limitations, and draft steward-review notes; AI must ABSTAIN when evidence
is insufficient and DENY where policy, rights, sensitivity, or release state blocks the request. [GAI] [ENCY]
[MAP-MASTER] [UIAI]
M. Publication, correction, and rollback.
CONFIRMED doctrine / PROPOSED implementation: Planetary/3D publication requires ReleaseManifest, EvidenceBundle, validation/policy support, review state where required, correction path, stale-state rule, and
rollback target. [ENCY Appendix E] [ENCY] [MAP-MASTER] [UIAI]
N. Verification backlog and open questions.
Item to verify Evidence that would settle it Status
Verify actual scene
implementation and schema home.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Define 3D admission policy. mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify point-cloud and
synthetic/reality-boundary rules.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
Verify 3D archaeology,
infrastructure, and rare-species
no-leak gates.
mounted repo files, schemas,
registry entries, tests, logs,
emitted artifacts, review records,
or release manifests
NEEDS VERIFICATION
124

19. Cross-Domain Systems
System Scope Guardrail Citation
MapLibre UI + Evidence
Drawer + Focus Mode
CONFIRMED doctrine /
PROPOSED
implementation:
MapLibre renders
released layers and
interaction state;
Evidence Drawer
explains
evidence/policy/release;
Focus Mode answers only
through finite envelopes.
Renderer is not truth,
source registry, policy
engine, citation authority,
review authority, release
authority, or AI
authority.
[MAP-MASTER] [UIAI]
[GAI]
Governed AI runtime
and AIReceipt
CONFIRMED doctrine /
PROPOSED
implementation:
Provider-neutral model
adapter, policy pre/post
check, citation validation,
structured output
validation, AIReceipt,
Runtime Response
Envelope.
No direct public model
traffic, no
RAW/WORK/QUARANTINE
prompt content, no
uncited authoritative
claims.
[GAI]
Catalog / Proof /
EvidenceBundle /
ReleaseManifest spine
CONFIRMED doctrine /
PROPOSED
implementation:
SourceDescriptor,
EvidenceBundle,
CatalogMatrix,
ValidationReport,
PolicyDecision,
ReleaseManifest,
CorrectionNotice,
RollbackCard.
Catalog search and graph
projection are not proof
by themselves.
[ENCY Appendix E]
Correction and rollback
path
CONFIRMED doctrine /
PROPOSED
implementation:
CorrectionNotice,
rollback target, alias
repointing, derivative
invalidation,
stale/superseded/withdrawn
badging.
Rollback does not
silently delete history.
[ENCY Appendix E]
125

System Scope Guardrail Citation
Review queues CONFIRMED doctrine /
PROPOSED
implementation:
ReviewRecord,
PolicyDecision,
quarantine disposition,
rights/steward/sensitivity/release
review.
AI suggestions are not
approvals; sensitive lanes
fail closed.
[ENCY] [GAI]
PROPOSED: Cross-system tests should prove no public client can reach RAW, WORK, QUARANTINE, canonical/internal stores, graph internals, vector indexes, source APIs, or direct model runtimes. [MAP-MASTER]
[GAI]
126

20. Master Atlases
20.1 Master Viewing Mode Atlas
Viewing mode Domains Shows Guardrail Citation
Evidence Drawer All domains EvidenceBundle,
source role, policy,
freshness,
correction, release,
rollback
ABSTAIN or DENY if
unresolved/restricted
[MAP-MASTER]
Focus Mode All domains bounded
AI/runtime answer
finite
ANSWER/ABSTAIN/DENY/ERROR
only
[GAI]
Time slider Hydrology, Soil,
Air, Hazards,
Roads,
People/Land,
Frontier Matrix
time roles and
temporal scopes
time roles do not
collapse
[DOM-HAZ]
[DOM-PEOPLE]
Sensitivity-redacted
view
Archaeology, Fauna,
Flora,
Infrastructure,
People/DNA, 3D
generalized or
withheld geometry
exact restricted
public geometry
denied
[DOM-ARCH]
[DOM-FAUNA]
Matrix cell
inspector
Frontier Matrix geography version,
definition,
observations,
uncertainty,
evidence
matrix cell is
analytical release,
not spreadsheet
truth
[ENCY]
3D / terrain /
synthetic scene
Planetary/3D terrain, point cloud,
scene, synthetic
surface
admit only when
trust controls
survive
[MAP-MASTER]
20.2 Master Capability / Action Matrix
Capability Applies to Required support Outcomes Citation
Source admission All domains SourceDescriptor,
rights, role,
cadence, sensitivity
PASS/HOLD/DENY/ERROR [ENCY]
RAW capture All domains immutable
payload/ref, hash,
source time
public access
DENY
[DIRRULES]
Evidence resolution All claim surfaces EvidenceRef ->
EvidenceBundle
ANSWER/ABSTAIN/DENY/ERROR [ENCY]
Catalog closure All published
domains
CatalogMatrix,
digests,
EvidenceRefs,
release refs
PASS/HOLD/DENY/ERROR [ENCY]
Public-safe
transformation
Sensitive domains redaction/generalization/publication
receipt
PASS/DENY/ERROR[DOM-ARCH]
[DOM-FAUNA]
[DOM-FLORA]
127

Capability Applies to Required support Outcomes Citation
Correction/Rollback All published
domains
CorrectionNotice,
RollbackCard,
derivative
invalidation
ACCEPTED/HOLD/DENY/ERROR [ENCY]
20.3 Master API Surface Table
API family Domains DTO/schema Outcomes / status
Source summary resolver All domains SourceDescriptor
projection
ANSWER/ABSTAIN/DENY/ERR
PROPOSED
implementation
Domain feature/detail
lookup
All domain lanes DomainFeatureEnvelope
+ DecisionEnvelope
ANSWER/ABSTAIN/DENY/ERR
PROPOSED
implementation
Layer manifest resolver All map domains LayerManifest /
GeoManifest
ANSWER/DENY/ERROR;
PROPOSED
implementation
Evidence resolver All domains EvidenceBundle ANSWER/ABSTAIN/DENY/ERR
PROPOSED
implementation
Focus Mode runtime All domains Runtime Response
Envelope + AIReceipt
ANSWER/ABSTAIN/DENY/ERR
PROPOSED
implementation
Review queue surface Sensitive/releasesignificant domainsReviewRecord +
PolicyDecision
ALLOW/RESTRICT/DENY/ERR
PROPOSED
implementation
20.4 Master Validator / Test Catalogue
Test family Domains Required negative case Expected outcome
Lifecycle boundary All public surface references
RAW/WORK/QUARANTINE/internal
store
DENY/ERROR
Source-role anti-collapse Hydrology, Air, Hazards,
Geology, Agriculture,
People/Land
regulatory/model/aggregate/admin
source used as different
truth class
DENY
Sensitivity redaction Archaeology, Fauna,
Flora, Infrastructure,
People/DNA, 3D
restricted exact public
geometry
DENY
AI citation and policy All Focus Mode domains uncited answer or
restricted prompt/output
ABSTAIN/DENY/ERROR
Catalog/release closure All digest mismatch or
missing rollback target
HOLD/DENY/ERROR
Emergency-alert
boundary
Hazards, Hydrology, Air KFM used as life-safety
instruction
DENY
20.5 Deny-by-Default Register and Sensitivity Matrix
128

Domain/surface Denied by default Allowed only when Citation
Archaeology exact sites, burial,
human remains, sacred
sites, looting-risk detail
steward/cultural review
+ transform receipt +
EvidenceBundle
[DOM-ARCH]
Fauna exact sensitive
occurrences,
nests/dens/roosts/hibernacula/spawning
geoprivacy + Redaction
Receipt + public-safe
derivative
[DOM-FAUNA]
Flora exact
rare/protected/culturally
sensitive plant locations
review +
generalized/withheld
geometry + Redaction
Receipt
[DOM-FLORA]
Infrastructure critical assets,
dependencies, condition
detail
steward review +
public-safe generalization
[DOM-SETTLE]
People/DNA/Land living-person private
output, raw DNA ids,
DNA segments, private
person-parcel joins
consent + policy +
restricted authorized
surface
[DOM-PEOPLE]
Hazards emergency instructions
or KFM as alert
authority
not allowed as KFM
authority
[DOM-HAZ]
Governed AI RAW/WORK access,
uncited claims, direct
model-public traffic
released EvidenceBundle
+ policy-safe context +
AIReceipt
[GAI]
129

21. Programming Possibilities Backlog, Dependencies, and Roadmap
CONFIRMED doctrine / PROPOSED roadmap: Build the governance spine before public features: source ledger,
schemas, fixtures, validators, policy gates, EvidenceBundle closure, finite envelopes, release manifests, correction path, and rollback targets. [ENCY] [UNIFIED]
Phase Scope Exit criteria
Rollback / failure
posture
0 Repo inspection and
evidence inventory
branch/files/schema
home/tests/workflows/manifests/logs
inventoried or
UNKNOWN
no implementation claim
without proof
1 Documentation control
plane
source ledger, ADR
index, registers,
verification backlog
revert doc PR and
preserve correction note
2 Shared schemas and
no-network fixtures
core governance schemas
and valid/invalid fixtures
remove schema wave if
ADR fails
3 Validators and policy
gates
reason-coded
DENY/ABSTAIN/ERROR/HOLD
outcomes
disable only if stronger
gate replaces
4 No-network
query-save-recompile dry
run
loop records and
validation reports with
no publication
no direct PUBLISHED
target
5 Hydrology proof-bearing
thin slice
HUC/gauge/NFHL
fixture, EvidenceBundle,
drawer, rollback
never label NFHL
observed flood
6 Soil plus habitat/fauna
controls
support-type separation
and sensitive occurrence
denial
disable sensitive layer if
leak
7 Governed API and
evidence resolver
finite envelope contracts
deny raw/work bypass
disable route or revert
alias
8 MapLibre shell and
Evidence Drawer
released layer click opens
evidence drawer
revert layer registry
9 Governed AI / Focus
Mode
AIReceipt and citation
validation over released
evidence
disable AI adapter if
failing
10 Public-safe aggregate
expansions
agriculture/geology/air/hazards
fixtures pass gates
per-domain rollback
11 Transport and
settlements expansion
road/rail and settlement
identity public-safe layers
disable facility layer if
leak
12 Sensitive-lane staged
builds
flora/fauna/archaeology/people/infrastructure
public-safe or restricted
surfaces
default DENY
13 Graph and analytics derived graph/triplets
from evidence; not root
truth
rebuild graph or disable
view
14 Frontier Matrix first
release
one county-year panel
with Matrix Release and
rollback
badge changed cells
15 Public atlas/dashboards/stories/exportsstory/export receipts and
citations
withdraw story/export if
unsafe
130

Phase Scope Exit criteria
Rollback / failure
posture
16 3D/digital
twin/synthetic scenes
Scene Manifest, Reality
Boundary Note, 3D
admission closure
remove unsafe scene
17 Live source activation
maturity
one source at a time with
terms, tests, monitoring,
rollback
disable source descriptor
21.1 Dependency graph
Upstream Downstream Dependency type Citation
Directory Rules All implementation
phases
placement and lifecycle
authority
[DIRRULES]
SourceDescriptor All domains source admission [ENCY]
EvidenceBundle All public claims evidence closure [ENCY]
ValidationReport +
PolicyDecision
Promotion / public APIs gate enforcement [ENCY]
Hydrology proof lane MapLibre / Evidence
Drawer / Focus Mode
first proof-bearing
map/AI slice
[DOM-HYD]
Geoprivacy controls Habitat/Fauna/Flora/3D/Mapssenitive-location policy [DOM-FAUNA]
[DOM-FLORA]
ReleaseManifest +
RollbackCard
Map/UI/exports/AI publication and recovery [ENCY]
131

22. Appendices
Appendix A. Glossary
Term Definition Citation
Domain CONFIRMED doctrine bounded
responsibility lane with owned
object semantics and governed
cross-lane relations.
[DDD] [ENCY]
Bounded context CONFIRMED reference model
boundary where a term has
defined meaning and ownership.
[DDD]
EvidenceBundle CONFIRMED resolved evidence
package for a claim.
[ENCY]
EvidenceRef CONFIRMED reference that must
resolve to EvidenceBundle before
public claim authority.
[ENCY]
Governed API CONFIRMED doctrine / PROPOSED
implementation interface
enforcing evidence, policy, release,
finite outcomes, and audit.
[GAI] [ENCY]
Promotion CONFIRMED governed release
transition, not file movement.
[DIRRULES]
Redaction Receipt CONFIRMED object family /
PROPOSED implementation record
of public-safe field or geometry
transformation.
[ENCY]
Runtime Response Envelope CONFIRMED doctrine / PROPOSED
implementation finite answer
envelope for AI and runtime
surfaces.
[GAI]
RollbackCard CONFIRMED rollback target and
drill object that preserves history
while repointing current release
state.
[ENCY Appendix E]
Trust membrane CONFIRMED doctrine boundary
that prevents raw, unreviewed,
restricted, or generated state from
becoming public truth.
[DIRRULES] [GAI]
Appendix B. Source family index
Short-name Source Role
[DIRRULES] Directory Rules Canonical placement and lifecycle
doctrine
[MAP-MASTER] MapLibre Master MapLibre, renderer, tiles,
Evidence Drawer, Focus Mode
doctrine
132

Short-name Source Role
[INDEX-18] Pass 18 Idea Index Representation, APIs, temporal
modeling, validation,
release-discipline expansion
[ENCY] Encyclopedia Master
domain/object/source/capability
spine
[DOM-AG] Agriculture dossier Agriculture domain dossier
[DOM-FLORA] Flora dossier Flora domain dossier
[DOM-SETTLE] Settlements/Infrastructure dossier Settlements and infrastructure
dossier
[DOM-HF] Habitat+Fauna thin slice Habitat + Fauna thin-slice dossier
[DOM-HAZ] Hazards dossier Hazards domain dossier
[DOM-ARCH] Archaeology dossier Archaeology domain dossier
[DOM-ROADS] Roads/Rail dossier Roads, rail, and trade routes
dossier
[DOM-AIR] Atmosphere/Air dossier Atmosphere and air dossier
[DOM-GEOL] Geology dossier Geology and natural resources
dossier
[DOM-SOIL] Soil dossier Soil domain dossier
[DOM-HAB] Habitat dossier Habitat domain dossier
[DOM-FAUNA] Fauna dossier Fauna domain dossier
[DOM-HYD] Hydrology dossier Hydrology domain dossier
[DOM-PEOPLE] People/DNA/Land dossier People, genealogy, DNA, and land
ownership dossier
[GAI] Governed AI dossier Governed AI and AIReceipt
doctrine
[UIAI] Whole UI + AI report Whole UI and governed AI
expansion plan
[DDD] DDD Reference Bounded context and ubiquitous
language reference
[UNIFIED] Unified / pipeline lineage Unified build and pipeline
roadmap lineage
Appendix C. Object family index
Domain Core object families Citation
Spatial Foundation Coordinate Reference Profile,
GeographyVersion, Projection
Transform Receipt, Geometry
Fingerprint, Base Layer
Descriptor, MapStyleRule, Scale
Support Profile,
UncertaintySurface,
Generalization Transform
[ENCY] [MAP-MASTER]
[INDEX-18]
133

Domain Core object families Citation
Hydrology Watershed, HUCUnit,
HydroFeature, ReachIdentity,
GaugeSite, FlowObservation,
WaterLevelObservation, Water
Quality Observation, Groundwater
Well, NFHLZone, Observed Flood
Event, Hydrograph
[DOM-HYD] [ENCY]
Soil SoilMapUnit, SoilComponent,
Horizon, SoilProperty, Hydrologic
Soil Group, Soil Moisture
Observation, Pedon, ErosionRisk,
SuitabilityRating, Component
Horizon Join, SoilTimeCaveat
[DOM-SOIL] [ENCY]
Habitat HabitatPatch,
LandCoverObservation,
EcologicalSystem, Habitat Quality
Score, SuitabilityModel,
ConnectivityEdge, Corridor,
Restoration Opportunity,
StewardshipZone, Model Run
Receipt, UncertaintySurface
[DOM-HAB] [DOM-HF] [ENCY]
Fauna Taxon, Taxon Crosswalk,
Conservation Status, Occurrence
Evidence, Occurrence Restricted,
Occurrence Public, RangePolygon,
SeasonalRange, MigrationRoute,
SensitiveSite,
MortalityObservation,
DiseaseObservation
[DOM-FAUNA] [DOM-HF]
[ENCY]
Flora Plant Taxon, FloraTaxon
Crosswalk, Flora Occurrence,
SpecimenRecord, Rare Plant
Record, Vegetation Community,
InvasivePlantRecord, Phenology
Observation, RangePolygon,
Habitat Association, Botanical
Survey, Restoration Planting
[DOM-FLORA] [ENCY]
Agriculture Crop Observation, Field
Candidate, Crop Rotation, Yield
Observation, Irrigation Link,
Conservation Practice, Soil Crop
Suitability, Agricultural Economy
Observation, SupplyChainNode,
Drought Stress Indicator, Pest
Stress Indicator, Aggregation
Receipt
[DOM-AG] [ENCY]
134

Domain Core object families Citation
Geology Geologic Unit, SurficialUnit,
Lithology, Stratigraphic Interval,
StructureFeature,
GeologyBoundaryVersion,
BoreholeReference, Well
LogReference, Geochemistry
SampleReference, Mineral
Occurrence, Resource Deposit,
ResourceEstimate
[DOM-GEOL] [ENCY]
Atmosphere/Air AirStation, AirObservation,
PM2.5 Observation, Ozone
Observation, SmokeContext,
AODRaster, Weather Station,
Weather Observation, WindField,
Precipitation Observation,
Temperature Observation, Climate
Normal
[DOM-AIR] [ENCY]
Hazards Hazard Event, Hazard
Observation, Warning Context,
Advisory Context, Disaster
Declaration, Flood Context,
Wildfire Detection, SmokeContext,
Drought Indicator, Earthquake
Event, Heat Cold Event, Exposure
Summary
[DOM-HAZ] [ENCY]
Roads/Rail Road Segment, Rail Segment,
CorridorRoute, RouteMembership,
Network Node, Crossing, Bridge,
Ferry, TransportFacility,
RestrictionEvent, StatusEvent,
OperatorAssignment
[DOM-ROADS] [ENCY]
Settlements/Infrastructure Settlement, Municipality,
CensusPlace, Townsite,
GhostTown, Fort, Mission,
ReservationCommunity,
Infrastructure Asset, Network
Node, Network Segment, Facility
[DOM-SETTLE] [ENCY]
Archaeology Archaeological Site,
SiteComponent,
CulturalTemporalPeriod,
SurveyProject, SurveyTransect,
ShovelTest, TestUnit,
ExcavationUnit,
ProvenienceContext,
StratigraphicUnit, ArtifactRecord,
Sample
[DOM-ARCH] [ENCY]
135

Domain Core object families Citation
People/DNA/Land Person Assertion,
PersonCanonical, NameAssertion,
LifeEvent, Residence Event,
Migration Event, Genealogy
Relationship, FamilyGroup, DNA
Match Evidence, DNASegment,
Relationship Hypothesis,
LandParcel
[DOM-PEOPLE] [ENCY]
Frontier Matrix Frontier Definition,
GeographyVersion, County-Year
Panel, Population Observation,
Economic Observation,
Agriculture Observation, Access
Observation, Settlement Status,
Land Office Record, Public Land
Record, Admin Boundary Change,
Crosswalk
[ENCY] [UNIFIED]
Planetary/3D Scene Manifest, Terrain Model, 3D
Tile Set, glTF Asset, Point Cloud,
Digital Twin View, Synthetic
Surface, ViewState,
Representation Receipt, Reality
Boundary Note, 3D Admission
Decision, SceneEvidenceBundle
[ENCY] [MAP-MASTER] [UIAI]
Appendix D. Directory Rules summary and proposed file-home conventions
Responsibility root Primary responsibility Status [DIRRULES]
docs/ human-facing doctrine, ADRs,
runbooks, registers
CONFIRMED rule / PROPOSED
presence
control_plane/ machine-readable governance
maps and indexes
CONFIRMED rule / PROPOSED
presence
contracts/ object meaning and semantic
contracts
CONFIRMED rule / PROPOSED
presence
schemas/ machine-checkable shape, default
schemas/contracts/v1/<...>
CONFIRMED rule / PROPOSED
presence
policy/ allow/deny/restrict/abstain/review
decisions
CONFIRMED rule / PROPOSED
presence
tests/ and fixtures/ deterministic proof and
valid/invalid examples
CONFIRMED rule / PROPOSED
presence
data/ RAW, WORK, QUARANTINE,
PROCESSED, CATALOG,
TRIPLET, PUBLISHED lifecycle
artifacts
CONFIRMED rule / PROPOSED
presence
release/ release decisions, correction
notices, rollback cards
CONFIRMED rule / PROPOSED
presence
Appendix E. Supersession and lineage notes
136

Item Lineage posture Status
Directory Rules placement authority for the Atlas CONFIRMED [DIRRULES]
Domain dossier PDFs planning evidence and
source-ledger inputs; not
implementation proof
CONFIRMED planning evidence /
PROPOSED implementation
KFM Encyclopedia object/source/capability spine; not
superseded by this Atlas
CONFIRMED [ENCY]
MapLibre and Governed AI
reports
UI/AI doctrine and lineage;
implementation remains unverified
CONFIRMED doctrine / NEEDS
VERIFICATION implementation
This Atlas new synthesis manuscript; does
not alter source authority
PROPOSED final artifact
pending QA
Appendix F. Final self-check
Question Result Status / citation
All domains covered Phases 3-18 are represented with
A-N template sections.
CONFIRMED in assembled draft
/ NEEDS PDF QA
Cross-domain systems covered MapLibre, Evidence Drawer,
Focus Mode, Governed AI,
catalog/proof/release,
correction/rollback, review queues
covered.
CONFIRMED in assembled draft
Sensitive domains fail closed Archaeology, rare fauna/flora,
infrastructure, living-person and
DNA controls are deny-by-default.
CONFIRMED doctrine / PROPOSED
implementation
AI and maps subordinate to
evidence
MapLibre, scenes, AI, tiles,
graphs, and dashboards are
downstream carriers.
CONFIRMED doctrine
Unsupported implementation
claims labeled
Routes, schema homes, validators,
CI, runtime, dashboards and
source activation are PROPOSED/UNKNOWN/NEEDS
VERIFICATION.
CONFIRMED draft rule / NEEDS
final scan
Publication/correction/rollback
visible
Every chapter and master system
includes release, correction,
rollback, stale/supersession
controls.
CONFIRMED in assembled draft
137

23. Assembly Instructions
CONFIRMED artifact: This Markdown file is the phase-assembled Atlas manuscript with explicit \pagebreak
markers before major chapters and appendices. [DIRRULES]
23.1 Recommended Pandoc command
pandoc KFM_Domains_Culmination_Atlas_v1.0.md \
--from markdown+pipe_tables+raw_tex \
--toc --toc-depth=2 \
--pdf-engine=xelatex \
-V geometry:margin=0.62in \
-V fontsize=11pt \
-V colorlinks=true \
-o KFM_Domains_Culmination_Atlas_v1.0.pdf
23.2 LaTeX and Typst alternatives
PROPOSED LaTeX alternative: convert Markdown to LaTeX with Pandoc, inspect table wrapping, then compile
with latexmk -xelatex.
pandoc KFM_Domains_Culmination_Atlas_v1.0.md --from markdown+pipe_tables+raw_tex --toc --toc-depth=
latexmk -xelatex KFM_Domains_Culmination_Atlas_v1.0.tex
PROPOSED Typst alternative: convert high-level sections into Typst headings and tables, then compile with
typst compile; verify table wrapping and page breaks because this manuscript uses Markdown \pagebreak
markers.
pandoc KFM_Domains_Culmination_Atlas_v1.0.md -t typst -o KFM_Domains_Culmination_Atlas_v1.0.typ
typst compile KFM_Domains_Culmination_Atlas_v1.0.typ KFM_Domains_Culmination_Atlas_v1.0.pdf
23.3 Figures and diagrams to generate separately
Figure Description Citation
KFM lifecycle spine A horizontal flow diagram showing
RAW -> WORK/QUARANTINE
-> PROCESSED ->
CATALOG/TRIPLET ->
PUBLISHED, with promotion,
correction, and rollback gates.
[DIRRULES]
Evidence-to-public-surface
membrane
A layered diagram showing
SourceDescriptor, EvidenceBundle,
PolicyDecision, ReleaseManifest,
governed API, MapLibre/Evidence
Drawer/Focus Mode.
[ENCY] [MAP-MASTER] [GAI]
Sensitive-domain fail-closed map A matrix-style figure marking
archaeology, fauna, flora,
infrastructure, living-person/DNA,
and 3D exposure with
DENY/generalize/review paths.
[ENCY]
138

Figure Description Citation
Cross-domain dependency graph A directed graph from Directory
Rules and governance spine to
hydrology proof lane, MapLibre
shell, AI, public-safe domains,
sensitive lanes, Frontier Matrix,
and 3D.
[UNIFIED]
Hydrology proof-lane exemplar A flow from WBD/HUC fixture
through validation,
EvidenceBundle, LayerManifest,
Evidence Drawer, Focus Mode,
and rollback.
[DOM-HYD]
Source-role anti-collapse diagram A diagram showing observed,
regulatory, modeled, aggregate,
administrative, candidate, and
synthetic records as separate
source-role channels.
[DOM-AIR] [DOM-HAZ]
[DOM-GEOL]
3D admission gate A decision tree for 2D default, 3D
allowed/restricted/denied, Reality
Boundary Note, and no-leak tests.
[MAP-MASTER] [ENCY]
23.4 Cover-page governance note
CONFIRMED doctrine: KFM is a governed spatial evidence and publication system: evidence first, map first,
time aware, policy conscious, auditable, reversible, and correction ready. The public unit of value is an
inspectable claim whose evidence, source role, spatial scope, temporal scope, rights/sensitivity posture, review
state, release state, correction lineage, and rollback target can be examined; no map, tile, graph, dashboard,
scene, index, export, or AI answer is sovereign truth by display alone. [ENCY] [DIRRULES] [MAP-MASTER]
[GAI]
139

Chapter 24 — Extended Master Atlases
CONFIRMED chapter scope: Chapter 24 is the v1.1 extension to the Master Atlases of Atlas v1.0 (ch. 20). v1.0 ch. 20
covers five master atlases — Viewing Mode, Capability/Action, API Surface, Validator/Test, and Deny-by-Default +
Sensitivity. Chapter 24 adds fourteen further registers that consolidate doctrine already present in v1.0 and the source
dossiers but scattered across per-domain sections, the Validator Catalogue, and the figure-to-generate list. No section in
Chapter 24 introduces a new domain, lifecycle phase, authority root, or object family. [ENCY] [DIRRULES]
CONFIRMED reading guidance: each section in Chapter 24 begins with a CONFIRMED purpose statement and is
composed of one or more master tables. Where a Chapter 24 section extends an existing v1.0 section (notably v1.0 §20.5,
§2.1, and Appendix C, E, F), the relationship is named in the section preamble. Where a section is new, that is also stated.
[ENCY] [DIRRULES]
CONFIRMED authority rule: the master tables in Chapter 24 are navigational, not authoritative. EvidenceBundle, the
source dossiers, and the schemas/contracts under schemas/contracts/v1/… (per Directory Rules §7.4 / ADR-0001) remain
the canonical sources for any claim. A Chapter 24 table that disagrees with v1.0 is treated as a drift entry, not as a
correction. [ENCY] [DIRRULES] [GAI]
24.1 Master Source-Role Anti-Collapse Register
CONFIRMED doctrine: KFM treats source role as a first-class identity attribute. An observed reading is not
interchangeable with a modeled estimate; a regulatory determination is not interchangeable with an administrative
compilation; an aggregate publication is not interchangeable with candidate evidence; synthetic content is never the same
thing as observed reality. The lifecycle and the governed API both fail closed when these roles are conflated. Atlas v1.0
references this as the ‘source-role anti-collapse’ rule in §20.4 and as a figure-to-generate in §23.3, but does not
consolidate the roles. This section does. [ENCY] [DOM-AIR] [DOM-HAZ] [DOM-GEOL] [DOM-AG]
[DOM-PEOPLE]
24.1.1 Canonical source-role classes
Role Definition (CONFIRMED doctrine) Typical example Allowed downstream role Citation
Observed A direct reading, measurement, or
first-hand evidentiary record tied to a
place and time.
Stream-gauge stage reading; soil
pedon description; air quality
monitor sample; ground
archaeological observation.
May feed modeled or aggregate
products; never relabeled as
‘regulatory’ or ‘administrative’.
[DOM-HYD]
[DOM-SOIL]
[DOM-AIR]
[DOM-ARCH]
Regulatory An authoritative determination by a
regulatory or governing body with
legal or administrative force.
NFHL flood-zone designation;
air-quality non-attainment
ruling; designated critical habitat
unit; protected-species listing.
Cite as regulatory context; never
labeled an ‘observed’ event or a
‘modeled’ estimate.
[DOM-HYD]
[DOM-AIR]
[DOM-FAUNA]
[DOM-FLORA]
Modeled A derived product from inputs,
assumptions, or fitted parameters;
uncertainty and provenance of inputs
must be preserved.
Hydrograph reconstruction;
smoke trajectory model;
suitability raster; population
estimation surface; AODRaster.
Cite with model identity, run receipt,
and bounds; never labeled an
observation.
[DOM-HYD]
[DOM-AIR]
[DOM-HAB]
[DOM-AG]
Aggregate A published summary, total, or
average over a unit (county, year,
watershed); irreversible loss of
individual record fidelity.
USDA crop county totals;
Census tract aggregates; decadal
climate normal; resource
estimate summary.
Cite with aggregation receipt; never
treated as a per-place record.
[DOM-AG]
[DOM-AG]
[DOM-PEOPLE]
[DOM-GEOL]
[DOM-AIR]
Administrati
ve
A compiled record produced by an
agency for administration, registration,
or accounting purposes — not
necessarily an observation or a
regulation.
Land office tract book; deed
index compilation; county
incorporation record; transport
facility roster.
Cite as administrative context; never
collapsed with observation or
regulation.
[DOM-PEOPLE]
[DOM-SETTLE]
[DOM-ROADS]

Role Definition (CONFIRMED doctrine) Typical example Allowed downstream role Citation
Candidate A proposed record awaiting validation,
evidence resolution, deduplication, or
steward review; not yet authoritative.
Quarantined connector output;
unresolved person assertion;
duplicate site candidate;
unmerged crop observation.
May be cited as candidate evidence in
WORK / QUARANTINE; must not
appear in PUBLISHED without
promotion.
[ENCY]
[DOM-PEOPLE]
[DOM-ARCH]
Synthetic Content generated by simulation,
reconstruction, AI, or interpolation
that has no underlying first-hand
observation. Includes synthetic
surfaces, generated text, AI-drafted
notes.
Synthetic terrain surface;
reconstructed historical scene;
AI-drafted summary of an
EvidenceBundle.
Carries Reality Boundary Note and
Representation Receipt; must never be
presented or queried as observed
reality.
[ENCY] [MAPMASTER]
[UIAI] [GAI]
Reading note: the role of a source is set at admission (SourceDescriptor) and is preserved through every promotion. Promotion does
not upgrade an observation to a regulation, or a model to an aggregate, or a candidate to a verified record — those are separate
governed transitions with their own evidence and review requirements. [ENCY] [DIRRULES]
24.1.2 Anti-collapse failure modes (DENY conditions)
Collapse pattern Domains most at
risk
Denied outcome Required guardrail Citation
Modeled product labeled or queried
as observed.
Air; Hydrology;
Habitat; Agriculture;
3D
DENY at publication;
ABSTAIN at AI surface.
Run receipt + uncertainty surface +
role-preserving DTO field.
[DOM-AIR]
[DOM-HYD]
[DOM-HAB]
[DOM-AG]
[MAP-MASTER]
Regulatory zone labeled as an
observed flood / event.
Hydrology; Hazards;
Air
DENY publication of
regulatory layer as event
evidence.
Separate regulatory-layer and
observed-event lanes; banner in UI.
[DOM-HYD]
[DOM-HAZ]
[DOM-AIR]
Aggregate cited as a per-place truth. Agriculture; People;
Geology; Air
DENY join from
aggregate cell to single
record; ABSTAIN at AI.
Aggregation receipt;
geometry-scope guard; matrix-cell
semantics.
[DOM-AG]
[DOM-PEOPLE]
[DOM-GEOL]
Administrative compilation cited as
observation.
People/Land;
Settlements; Roads
DENY publication of
compilation as observed
event timeline.
Source-role tag preserved; named
LifeEvent / AdminEvent types.
[DOM-PEOPLE]
[DOM-SETTLE]
[DOM-ROADS]
Candidate record exposed on a
public surface.
All DENY at trust
membrane; route to
QUARANTINE.
Promotion gate; no PUBLISHED
edge to WORK / QUARANTINE.
[ENCY]
[DIRRULES]
Synthetic content presented as
observed reality.
Planetary/3D; AI;
Archaeology; Habitat
DENY publication;
HOLD for steward
review; ABSTAIN at AI.
Reality Boundary Note;
Representation Receipt; UI badge.
[ENCY]
[MAP-MASTER]
[UIAI]
[DOM-ARCH]
[DOM-HAB]
AI text treated as evidence. All Focus Mode
surfaces
DENY publication;
ABSTAIN at Focus
Mode; AIReceipt
mandatory.
Cite-or-abstain rule; AIReceipt;
release state required.
[GAI] [ENCY]
[UIAI]
24.1.3 Roles to source-descriptor fields (PROPOSED)
PROPOSED schema-home note: source-role is a SourceDescriptor field; the canonical schema home defaults to
schemas/contracts/v1/source/source-descriptor.json per Directory Rules §7.4 and ADR-0001, unless an accepted ADR
relocates it. NEEDS VERIFICATION: actual file presence and field names are not asserted here. [DIRRULES]
PROPOSED descriptor surface (illustrative, not authoritative):

Field Type / vocabulary Required? Notes
source_role enum: observed | regulatory | modeled |
aggregate | administrative | candidate |
synthetic
MUST Set at admission. Never edited
in-place; corrections must produce a
new descriptor and a
CorrectionNotice.
role_authority string (issuing body / model identity /
steward)
MUST when role in
{regulatory, modeled,
aggregate}
Disambiguates the authoring authority
for downstream cite text.
role_aggregation_unit geometry-scope token (county, HUC, tract,
year, decade, etc.)
MUST when
source_role =
aggregate
Prevents geometry-scope drift on join.
role_model_run_ref EvidenceRef → ModelRunReceipt MUST when
source_role = modeled
Pins the inputs, parameters, and
version that produced the value.
role_synthetic_basis structured: { method, inputs,
reality_boundary_note_ref }
MUST when
source_role = synthetic
Records what is and is not real in the
carrier.
role_candidate_disposition enum: pending | merged | rejected |
quarantined
MUST when
source_role = candidate
Tracks promotion state; PUBLISHED
edge forbidden until merged.
NEEDS VERIFICATION: implementation of these fields in the mounted SourceDescriptor schema. Names above are PROPOSED
shape; an ADR or schema PR would be the authoritative resolution. [DIRRULES] [ENCY]

24.2 Master Receipt Catalog
CONFIRMED doctrine: KFM uses receipts to make consequential transformations inspectable. A receipt is a structured,
persisted record of a specific governed operation, with enough context for audit and rollback. The receipt is never
optional when the operation is consequential; if no receipt exists, the operation did not happen in the governed sense.
[ENCY] [GAI]
Atlas v1.0 mentions receipts in many places (AIReceipt, RedactionReceipt, AggregationReceipt, RepresentationReceipt,
ModelRunReceipt, RollbackCard, CorrectionNotice, ReviewRecord, TransformReceipt) but does not collect them. This
section is the consolidated reference. PROPOSED schema home: each receipt class should be under
schemas/contracts/v1/receipts/ unless an ADR relocates it. NEEDS VERIFICATION: actual file presence. [DIRRULES]
[ENCY]
24.2.1 Receipt family catalog
Receipt Purpose (CONFIRMED doctrine) Triggered by Required content (PROPOSED
shape)
Citation
SourceDescriptor Records source identity, rights, role,
sensitivity, cadence at admission. Not
strictly a ‘receipt’ but listed here
because it anchors every downstream
receipt.
Source admission. source_id, source_role, authority,
rights, sensitivity, cadence, ingest
hash, time, citation.
[ENCY]
[DIRRULES]
TransformReceipt
(Projection /
Generalization)
Records a spatial or attribute transform
applied to a feature (reprojection,
generalization, snap, simplification).
Geometry
normalization,
projection,
generalization.
input_geom_hash,
output_geom_hash, transform,
parameters, tolerance, timestamp,
actor.
[MAP-MASTER]
[ENCY]
RedactionReceipt Records a public-safe transformation
that removed, masked, fuzzed, or
withheld content for sensitivity, rights,
or policy.
Sensitive-domain
publication;
living-person fields;
rare-species
occurrences;
archaeological coords;
infrastructure detail.
policy_ref, redaction_method,
kept_fields, removed_fields,
geometry_transform, reviewer.
[DOM-ARCH]
[DOM-FAUNA]
[DOM-FLORA]
[DOM-PEOPLE]
[DOM-SETTLE]
AggregationReceipt Records an aggregation step
(county-year roll-up, decadal mean,
watershed total) and pins the geometry
scope.
Aggregate publication;
matrix cell
computation.
geometry_scope, time_scope,
aggregation_method,
input_source_refs, suppression_rule,
output_unit.
[DOM-AG]
[DOM-PEOPLE]
[DOM-AIR]
[DOM-GEOL]
ModelRunReceipt Records a modeled output: model
identity, version, inputs, parameters,
uncertainty, validation.
Modeled product
publication; suitability
surface; smoke
trajectory; restoration
model.
model_id, model_version, inputs[],
parameters, run_time,
uncertainty_surface_ref,
validation_ref.
[DOM-HAB]
[DOM-AIR]
[DOM-AG]
[MAP-MASTER]
RepresentationReceip
t
Records a representation step where
surface fidelity differs from evidence
fidelity — e.g., 3D scene from 2D
evidence, synthetic terrain, tile
downsampling.
3D scene publication;
tile/PMTiles export;
visual-only
generalization.
evidence_ref,
representation_method, parameters,
reality_boundary_note_ref.
[MAP-MASTER]
[UIAI] [ENCY]
AIReceipt Records a governed AI answer:
prompt scope, evidence used, policy
decision, outcome class,
abstention/denial reason.
Any Focus Mode
answer; any AI-drafted
note or summary.
prompt_scope, evidence_refs[],
policy_ref, outcome (ANSWER /
ABSTAIN / DENY / ERROR),
reason_code, model_id, time.
[GAI] [UIAI]
[ENCY]

Receipt Purpose (CONFIRMED doctrine) Triggered by Required content (PROPOSED
shape)
Citation
ReviewRecord Records a steward, rights-holder, or
policy review of a candidate transition:
source admission, redaction approval,
promotion, release.
Promotion gate;
sensitive-lane
publication; correction
acceptance.
reviewer, role, decision (ALLOW /
RESTRICT / DENY / HOLD),
evidence_refs[], policy_ref, time.
[ENCY]
[DIRRULES]
PolicyDecision Records a policy evaluation: which
rule, against which object, with which
outcome.
Every governed gate;
rights / sensitivity /
release checks.
policy_id, target_object, decision,
reason_code, time, evidence_refs[].
[ENCY]
[DIRRULES]
ValidationReport Records the outcome of a validator
run.
WORK promotion;
PROCESSED →
CATALOG; release
closure.
validator_id, target, passes[],
failures[], time, deterministic_inputs.
[ENCY]
[DIRRULES]
ReleaseManifest Records the contents, version,
signatures, and rollback target for a
release.
PUBLISHED
transition.
release_id, contents[], digests,
evidence_refs[], rollback_target,
time.
[ENCY]
[DIRRULES]
CorrectionNotice Records that a published claim was
corrected: what changed, why, and
what derivatives were invalidated.
Post-publication
correction.
claim_ref, prior_release_ref,
change_summary, invalidates[],
review_ref, time.
[ENCY]
[DIRRULES]
RollbackCard Records a rollback decision and the
targeted prior release.
Failed release;
correction.
release_id, rollback_to, reason,
invalidates[], review_ref, time.
[ENCY]
[DIRRULES]
RealityBoundaryNote Public-facing or steward-facing
statement that a carrier is synthetic or
reconstructed and not direct evidence.
Synthetic surfaces;
reconstructed scenes;
AI-drafted text.
scope, method_summary,
evidence_refs[], visibility.
[ENCY]
[MAP-MASTER]
[UIAI]
MatrixCellReceipt Records the inputs, definitions,
geography version, and uncertainty of
a single Frontier Matrix cell.
Matrix-cell publication. cell_id, definition_ref,
geography_version, inputs[],
uncertainty, review_ref.
[ENCY]
[UNIFIED]
(Frontier Matrix)
StorySnapshot /
ExportReceipt
Records the evidence, redactions, and
release state at the moment of a story /
export / atlas snapshot.
Story or export
publication.
snapshot_id, evidence_refs[],
redactions[], release_refs[],
rollback_target, time.
[ENCY] [UIAI]
24.2.2 Receipt ↔ lifecycle phase mapping
Receipt RAW WORK /
QUARANTINE
PROCESSED CATALOG /
TRIPLET
PUBLISHED
SourceDescriptor • • • • •
TransformReceipt • • •
RedactionReceipt • • • •
AggregationReceipt • • • •
ModelRunReceipt • • • •
RepresentationReceipt • • •
AIReceipt • • • (Focus Mode only)
ReviewRecord • • • •
PolicyDecision • • • • •
ValidationReport • • •
ReleaseManifest • •
CorrectionNotice • •

Receipt RAW WORK /
QUARANTINE
PROCESSED CATALOG /
TRIPLET
PUBLISHED
RollbackCard • •
RealityBoundaryNote • • •
MatrixCellReceipt • • •
StorySnapshot • •
Reading note: a dot means the receipt is normally emitted, amended, or referenced at that phase. Receipts created earlier remain
referenced (not duplicated) at later phases via EvidenceRef.

24.3 Master Decision Outcome Envelope Reference
CONFIRMED doctrine: every governed API surface, validator, policy gate, and Focus Mode answer in KFM returns a
finite outcome from a small, well-known set. v1.0 introduces these outcomes incrementally across the J. and K. tables for
each domain and consolidates them at §20.2 and §20.3, but does not put them in one place with their semantics. This
section does. [GAI] [ENCY]
24.3.1 Outcome classes
Outcome When (CONFIRMED doctrine) Required artifacts Public-surface effect Citation
ANSWER Evidence is sufficient, policy permits,
release state allows, review state (if
required) is recorded.
EvidenceBundle resolved;
PolicyDecision = allow;
ReleaseManifest applies.
Substantive answer with evidence
drawer and citation.
[GAI] [ENCY]
ABSTAIN Evidence is insufficient or incomplete;
or the AI surface cannot cite; or
evidence is stale and no released
alternative is found.
AIReceipt with reason; no
claim emitted.
Returns a non-substantive note with a
reason; never invents.
[GAI] [ENCY]
DENY Policy, rights, sensitivity, or release
state forbids the answer. Sensitive lanes
default here.
PolicyDecision = deny +
reason_code; AIReceipt
records denial.
Returns denial reason; offers
alternative non-restricted surface
where possible.
[GAI] [ENCY]
[DOM-ARCH]
[DOM-FAUNA]
[DOM-PEOPLE]
ERROR The governed API cannot evaluate —
missing schema, malformed query,
contract violation, infrastructure failure.
Error envelope with diagnostic
code, no claim leakage.
Returns a finite, actionable error;
never silently falls through to a
different lane.
[GAI] [ENCY]
HOLD Promotion / release / correction is
paused pending a steward, rights-holder,
or policy review.
ReviewRecord pending;
PolicyDecision = hold; no
public claim emitted while
held.
Surface remains in prior state; no
silent rollback or replacement.
[ENCY]
[DIRRULES]
PASS (Validator-class outcome.) A validator
or admission check completed and the
input is acceptable.
ValidationReport pass. Internal only; does not directly emit a
public answer.
[ENCY]
[DIRRULES]
FAIL (Validator-class outcome.) A validator
or admission check completed and the
input is unacceptable.
ValidationReport with failure
list.
Promotion blocked; quarantine where
appropriate.
[ENCY]
[DIRRULES]
24.3.2 Outcome × surface mapping
Surface Outcomes returned Forbidden outcome / behavior Citation
Source summary resolver ANSWER / ABSTAIN / DENY /
ERROR
Returning raw source bytes; returning quarantined
source as ANSWER.
[ENCY]
[DIRRULES]
Domain feature/detail lookup ANSWER / ABSTAIN / DENY /
ERROR
Returning an unreleased candidate as ANSWER;
exposing internal store identifiers.
[ENCY] [GAI]
Layer manifest resolver ANSWER / DENY / ERROR Returning a layer that lacks a ReleaseManifest; serving
WORK or CATALOG layers to public clients.
[ENCY]
[MAP-MASTER]
Evidence Drawer payload ANSWER / ABSTAIN / DENY /
ERROR
Returning a payload that includes restricted geometry
or uncited claim text.
[ENCY]
[MAP-MASTER]
Focus Mode (AI runtime) ANSWER / ABSTAIN / DENY /
ERROR
Generating uncited language as ANSWER; substituting
model output for EvidenceBundle.
[GAI] [ENCY]
Review queue / steward
console
ALLOW / RESTRICT / DENY /
HOLD / ERROR
Mixing review and publication duties on the same actor
when separation is required; bypassing logging.
[ENCY]
[DIRRULES]

Surface Outcomes returned Forbidden outcome / behavior Citation
Validator harness PASS / FAIL / ERROR Returning PASS without ValidationReport; emitting
PASS for non-deterministic inputs.
[ENCY]
[DIRRULES]
Release queue ALLOW / HOLD / DENY /
ERROR
Publishing without ReleaseManifest, rollback target, or
correction path.
[ENCY]
[DIRRULES]
Correction / rollback ACCEPTED / HOLD / DENY /
ERROR
Accepting a correction without invalidating
downstream derivatives; silent rollback without
RollbackCard.
[ENCY]
[DIRRULES]

24.4 Master Cross-Lane Relation Atlas
CONFIRMED doctrine: every domain in Atlas v1.0 owns its objects and publishes interfaces that other domains may
cite, but never modify. v1.0 documents these edges per-domain in the F. Cross-lane relations sections (chapters 3–18).
This supplement consolidates the strongest edges into a single matrix so that cross-domain queries and reviews can be
reasoned about as a whole. [ENCY]
How to read this matrix: a cell at (row = owner domain, column = consumer domain) names the relation the consumer
may rely on, citing the owner’s public-safe surface. The owning domain is responsible for the object’s meaning, lifecycle,
and release; the consumer cites it as evidence context. No row consumes from another row except via this lattice.
24.4.1 Edges owned by Spatial Foundation
Owner: Spatial
Foundation
Consumes from owner Relation (CONFIRMED doctrine) Citation
Spatial Foundation All domains Coordinate Reference Profile, GeographyVersion, Projection
Transform Receipt, scale-support, and base-layer descriptors are
sourced here.
[MAP-MASTER]
[ENCY]
Hazards / Hydrology / Air Time-aware overlay primitives are constrained by Spatial
Foundation rules (clipping, projection, generalization tolerances).
[DOM-HYD]
[DOM-HAZ]
[DOM-AIR]
Planetary/3D Vertical datum, terrain reference, and reality-boundary rendering
constraints originate here.
[MAP-MASTER]
[UIAI]
24.4.2 Edges owned by Hydrology
Owner: Hydrology Consumes from owner Relation (CONFIRMED doctrine) Citation
Hydrology Soil HUC / watershed identity bounds soil hydrologic group context. [DOM-HYD]
[DOM-SOIL]
Habitat / Fauna / Flora Wetland and reach identity feeds habitat-quality and
occurrence-context joins.
[DOM-HYD]
[DOM-HAB]
[DOM-FAUNA]
[DOM-FLORA]
Agriculture Reach identity and water-availability context bound irrigation links;
observed flow is not a yield input without modeling.
[DOM-HYD]
[DOM-AG]
Hazards Observed flow and water-level observations are cited as context for
flood events; NFHL is regulatory context only.
[DOM-HYD]
[DOM-HAZ]
Settlements / Infrastructure Reach proximity and HUC context drive settlement and crossing
analyses, but do not override settlement identity.
[DOM-HYD]
[DOM-SETTLE]
Frontier Matrix HUC / reach as cross-temporal anchors for water-availability cells. [DOM-HYD]
[UNIFIED]
24.4.3 Edges owned by Soil
Owner: Soil Consumes from owner Relation (CONFIRMED doctrine) Citation
Soil Habitat SoilMapUnit / SoilComponent context feeds ecological system
inference.
[DOM-SOIL]
[DOM-HAB]
Agriculture Soil suitability rating and hydrologic group bound crop suitability;
soil time caveat must be carried.
[DOM-SOIL]
[DOM-AG]
Hazards Erosion risk context informs flood and dust hazard analyses. [DOM-SOIL]
[DOM-HAZ]

Owner: Soil Consumes from owner Relation (CONFIRMED doctrine) Citation
Settlements Townsite footing / drainage context (advisory; not regulatory). [DOM-SOIL]
[DOM-SETTLE]
24.4.4 Edges owned by Habitat
Owner: Habitat Consumes from owner Relation (CONFIRMED doctrine) Citation
Habitat Fauna / Flora Habitat patch, ecological system, and stewardship zone provide the
context for occurrence interpretation.
[DOM-HAB]
[DOM-FAUNA]
[DOM-FLORA]
Agriculture Conservation-practice candidates are framed by habitat-quality
scores; never used to instruct land management.
[DOM-HAB]
[DOM-AG]
Planetary/3D Habitat patches are admitted to 3D scenes only via generalized
geometry; sensitive habitat denied.
[DOM-HAB]
[MAP-MASTER]
24.4.5 Edges owned by Fauna
Owner: Fauna Consumes from owner Relation (CONFIRMED doctrine) Citation
Fauna Habitat Occurrence records (public-safe only) feed habitat-quality model
evaluation; restricted occurrences never cross.
[DOM-FAUNA]
[DOM-HAB]
Hazards Mortality / disease observations as hazard context (e.g., wildlife
disease, fish kills) with rights and stewardship checks.
[DOM-FAUNA]
[DOM-HAZ]
Agriculture Pest stress indicators are agriculture-owned; fauna is the source of
taxonomic identity only.
[DOM-FAUNA]
[DOM-AG]
24.4.6 Edges owned by Flora
Owner: Flora Consumes from owner Relation (CONFIRMED doctrine) Citation
Flora Habitat Vegetation community feeds ecological system mapping; rare-plant
exact location denied to public consumers.
[DOM-FLORA]
[DOM-HAB]
Agriculture Invasive-plant context informs management framing; never an
instruction.
[DOM-FLORA]
[DOM-AG]
Archaeology Ethnobotanical context (steward-reviewed) may bound site
interpretation; never overrides cultural-heritage authority.
[DOM-FLORA]
[DOM-ARCH]
24.4.7 Edges owned by Agriculture
Owner: Agriculture Consumes from owner Relation (CONFIRMED doctrine) Citation
Agriculture Frontier Matrix Aggregate county-year crop and yield observations are matrix-cell
inputs (with aggregation receipt).
[DOM-AG]
[UNIFIED]
Hazards Drought and pest stress indicators provide context for hazard
analysis; not regulatory.
[DOM-AG]
[DOM-HAZ]
People/Land Field candidates may be joined to LandParcel context; private
person-parcel joins fail closed by default.
[DOM-AG]
[DOM-PEOPLE]
24.4.8 Edges owned by Geology / Natural Resources
Owner: Geology /
Natural Resources
Consumes from owner Relation (CONFIRMED doctrine) Citation
Geology / Natural
Resources
Hydrology Surficial unit and lithology provide groundwater context (advisory). [DOM-GEOL]
[DOM-HYD]

Owner: Geology /
Natural Resources
Consumes from owner Relation (CONFIRMED doctrine) Citation
Hazards Faults, earthquake events, and subsidence context are hazard inputs. [DOM-GEOL]
[DOM-HAZ]
Agriculture Resource and soil-parent material context (advisory; not regulatory
or aggregate).
[DOM-GEOL]
[DOM-AG]
Planetary/3D Subsurface units may be cited as 3D scene context with admission
and reality-boundary controls.
[DOM-GEOL]
[MAP-MASTER]
24.4.9 Edges owned by Atmosphere / Air
Owner: Atmosphere /
Air
Consumes from owner Relation (CONFIRMED doctrine) Citation
Atmosphere / Air Hazards Smoke context, AOD raster, and weather observations are cited as
hazard inputs.
[DOM-AIR]
[DOM-HAZ]
Hydrology Precipitation observations and climate normals provide hydrologic
context.
[DOM-AIR]
[DOM-HYD]
Agriculture Climate normals and precipitation context bound drought indicators. [DOM-AIR]
[DOM-AG]
Frontier Matrix Decadal normals are aggregate inputs to time-aware cells. [DOM-AIR]
[UNIFIED]
24.4.10 Edges owned by Hazards
Owner: Hazards Consumes from owner Relation (CONFIRMED doctrine) Citation
Hazards All domains Hazard event context is cited; KFM is never an alert authority. The
supplement explicitly retains v1.0’s emergency-alert boundary.
[DOM-HAZ]
[ENCY]
Planetary/3D Scenario and exposure context may anchor a 3D scene with
admission and reality-boundary controls; never as instruction.
[DOM-HAZ]
[MAP-MASTER]
24.4.11 Edges owned by Roads / Rail / Trade Routes
Owner: Roads / Rail /
Trade Routes
Consumes from owner Relation (CONFIRMED doctrine) Citation
Roads / Rail / Trade
Routes
Settlements Network nodes and crossings anchor settlement connectivity;
facility identity is settlement-owned.
[DOM-ROADS]
[DOM-SETTLE]
Frontier Matrix Access observations bound the access cells in the matrix. [DOM-ROADS]
[UNIFIED]
Archaeology Historical corridor reconstructions cited as context only; exact
archaeological coordinates denied.
[DOM-ROADS]
[DOM-ARCH]
24.4.12 Edges owned by Settlements / Infrastructure
Owner: Settlements /
Infrastructure
Consumes from owner Relation (CONFIRMED doctrine) Citation
Settlements /
Infrastructure
People/Land Settlement identity (Township, GhostTown, Townsite, Reservation
Community) bounds residence and ownership context.
[DOM-SETTLE]
[DOM-PEOPLE]
Frontier Matrix Settlement status feeds settlement cells in the matrix. [DOM-SETTLE]
[UNIFIED]
Hazards Critical-infrastructure exposure context with default deny on public
detail.
[DOM-SETTLE]
[DOM-HAZ]

24.4.13 Edges owned by Archaeology / Cultural Heritage
Owner: Archaeology /
Cultural Heritage
Consumes from owner Relation (CONFIRMED doctrine) Citation
Archaeology / Cultural
Heritage
Settlements Cultural temporal period and survey context bound historical
settlement interpretation; site coords denied.
[DOM-ARCH]
[DOM-SETTLE]
Planetary/3D Sites are admitted only via steward-reviewed, generalized 3D
representation with reality-boundary note.
[DOM-ARCH]
[MAP-MASTER]
People/Land Cultural affiliations cited with rights, sovereignty, and steward
review.
[DOM-ARCH]
[DOM-PEOPLE]
24.4.14 Edges owned by People, Genealogy, DNA, Land Ownership
Owner: People,
Genealogy, DNA, Land
Ownership
Consumes from owner Relation (CONFIRMED doctrine) Citation
People, Genealogy,
DNA, Land Ownership
Settlements Residence events anchor settlement membership; living-person
fields fail closed.
[DOM-PEOPLE]
[DOM-SETTLE]
Frontier Matrix Aggregated population observations feed matrix cells. [DOM-PEOPLE]
[UNIFIED]
Archaeology Indigenous community context: steward-reviewed and
rights-bounded.
[DOM-PEOPLE]
[DOM-ARCH]
Agriculture LandParcel context may bound field-candidate joins; private
person-parcel joins denied by default.
[DOM-PEOPLE]
[DOM-AG]
24.4.15 Edges owned by Frontier Matrix
Owner: Frontier
Matrix
Consumes from owner Relation (CONFIRMED doctrine) Citation
Frontier Matrix All domain analytics
surfaces
Matrix cells are analytical releases with their own evidence and
rollback. Other domains do not edit cells.
[ENCY] [UNIFIED]
UI / story / atlas exports Frontier-matrix snapshots feed story exports with snapshot receipts. [UIAI] [ENCY]
24.4.16 Edges owned by Planetary, 3D, Digital Twin, Synthetic
Owner: Planetary, 3D,
Digital Twin, Synthetic
Spatial
Consumes from owner Relation (CONFIRMED doctrine) Citation
Planetary, 3D, Digital
Twin, Synthetic Spatial
All domains 3D scenes may cite domain releases under admission rules; never an
instruction or alert surface.
[ENCY]
[MAP-MASTER]
[UIAI]
UI / Evidence Drawer Scene Manifests, viewstates, and reality-boundary notes are
rendered with the same Evidence Drawer discipline as 2D layers.
[MAP-MASTER]
[UIAI]
Note on completeness: the per-row tables above capture the strongest cross-lane edges. Atlas v1.0’s per-domain F. sections remain
the authoritative source for the full edge list, including conditional and rarely-used relations. Where a relation in v1.0 conflicts with
one here, v1.0 governs and the conflict should be filed against the supplement. [DIRRULES] [ENCY]

7. Master Sensitivity / Rights Tier Reference (extends v1.0 §20.5)
CONFIRMED doctrine: KFM publishes only the safest representation that still answers the steward’s and the public’s
reasonable needs. v1.0 §20.5 introduces a Deny-by-Default Register that names per-domain restrictions. This section
extends it with a tier scheme, a uniform set of allowed transforms, and a uniform set of gates — so that ‘publish at tier N’
becomes a reviewable, repeatable action across domains. [ENCY] [DOM-ARCH] [DOM-FAUNA] [DOM-FLORA]
[DOM-PEOPLE] [DOM-SETTLE]
24.5.1 Tier scheme (PROPOSED)
Tier Name Definition (PROPOSED) Default audience Citation
T0 Open Public-safe with no transformations required; no rights,
sensitivity, or steward gating beyond standard release.
Any public client via
governed API.
[ENCY]
[MAP-MASTER]
T1 Generalized Public-safe only after generalization, fuzzing, aggregation, or
redaction; transform is reviewed and recorded.
Any public client via
governed API.
[ENCY]
[DOM-FAUNA]
[DOM-FLORA]
T2 Reviewer Released only to authenticated reviewers or domain stewards;
policy-bounded; correction path active.
Stewards, reviewers, named
research collaborators.
[ENCY]
[DIRRULES]
T3 Restricted Released only under named agreement (rights, sovereignty, or
consent) and recorded.
Named authorized parties
only.
[ENCY]
[DOM-PEOPLE]
[DOM-ARCH]
T4 Denied Not released to any audience; the existence of a record may be
released only as steward review permits.
— [ENCY]
[DOM-ARCH]
[DOM-PEOPLE]
24.5.2 Per-domain tier matrix (extends v1.0 §20.5)
Domain / object class Default tier Allowed transforms (PROPOSED) Required gates Citation
Archaeology — site location T4 Steward review + cultural review +
generalized geometry (coarse cell) +
RedactionReceipt → T2 or T1.
RedactionReceipt +
ReviewRecord +
PolicyDecision.
[DOM-ARCH]
Archaeology — human remains /
sacred sites
T4 No transform releases this to T0; T3 only
under explicit named authorization.
Sovereignty review +
ReviewRecord +
PolicyDecision.
[DOM-ARCH]
Fauna — sensitive occurrence T4 Geoprivacy generalization +
RedactionReceipt → T1.
RedactionReceipt +
ReviewRecord +
PolicyDecision.
[DOM-FAUNA]
Fauna — range polygon T1 Aggregate / generalized public-safe layer. AggregationReceipt or
RedactionReceipt.
[DOM-FAUNA]
Flora — rare or culturally
sensitive plant location
T4 Generalized geometry + steward review →
T2 or T1.
RedactionReceipt +
ReviewRecord.
[DOM-FLORA]
People/DNA — living-person
fields
T4 Aggregation by tract or county +
AggregationReceipt → T1.
Consent or aggregation gate +
ReviewRecord.
[DOM-PEOPLE]
People/DNA — raw DNA
segment data
T4 No transform releases this to a public tier;
T3 only under explicit research agreement.
Named consent +
ReviewRecord +
PolicyDecision.
[DOM-PEOPLE]
People/Land — private
person-parcel join
T4 Generalized parcel + de-identified person
→ T2 only.
RedactionReceipt +
ReviewRecord.
[DOM-PEOPLE]
Infrastructure — critical asset
detail
T4 Generalized facility footprint + suppressed
dependency → T1.
Steward review +
RedactionReceipt.
[DOM-SETTLE]

Domain / object class Default tier Allowed transforms (PROPOSED) Required gates Citation
Infrastructure — condition /
vulnerability
T4 T3 to named authorities only; never T0 /
T1.
Steward review + named-party
agreement.
[DOM-SETTLE]
Hazards — KFM as alert
authority
T4 forever No transform permits KFM to act as an
emergency-alert authority. The boundary
holds.
Policy boundary; deny at
runtime.
[DOM-HAZ]
Governed AI — RAW / WORK
access via AI surface
T4 AI never reads RAW or WORK content;
only released EvidenceBundle.
PolicyDecision + AIReceipt. [GAI]
Planetary/3D — sensitive 3D
scene content
T4 Generalization / clipping / withholding;
Reality Boundary Note + Representation
Receipt → T1 or T2 where steward review
supports.
Steward review +
RedactionReceipt +
RepresentationReceipt.
[MAP-MASTER]
[UIAI]
24.5.3 Tier transitions (allowed motion)
From → To Required artifact Required reviewer Reversibility (CONFIRMED doctrine)
T4 → T3 PolicyDecision + ReviewRecord +
agreement
Steward + rights-holder
where applicable
Reversible: agreement revocation returns object
to T4 with CorrectionNotice.
T4 → T2 PolicyDecision + ReviewRecord Steward Reversible: review revocation returns object to
T4.
T4 → T1 RedactionReceipt + ReviewRecord Steward Reversible: redaction can be re-evaluated;
correction may demote a published T1 to T4.
T3 → T2 PolicyDecision + ReviewRecord Steward Reversible.
T2 → T1 RedactionReceipt + ReviewRecord Steward Reversible.
T1 → T0 ReleaseManifest + ReviewRecord Steward + release authority Reversible: rollback supported via RollbackCard.
Any tier → T4
(downgrade)
CorrectionNotice + ReviewRecord Steward + rights-holder
where applicable
Always permitted; precedes derivative
invalidation.
Reading note: a tier upgrade (toward more public) always needs both a transform receipt and a review record; a tier downgrade
(toward less public) never needs both — correction alone is sufficient to remove or restrict.

8. Master Pipeline Gate Reference (RAW → PUBLISHED)
CONFIRMED doctrine: every domain follows the lifecycle invariant RAW → WORK / QUARANTINE →
PROCESSED → CATALOG / TRIPLET → PUBLISHED. v1.0 chapters 3–18 carry per-domain H. Pipeline shape
tables. This section consolidates the universal gates and the artifacts each gate requires — the things without which the
transition fails closed. [DIRRULES] [ENCY]
24.6.1 Lifecycle gates
Gate (transition) Pre-condition Required artifacts (PROPOSED
minimum)
Failure-closed outcome Citation
Admission (— → RAW) Source identity and rights are
minimally established at
discovery; source-role intent is
set.
SourceDescriptor (role, authority,
rights, sensitivity, cadence); hash of
payload or reference.
Source not admitted; logged
as candidate awaiting
steward.
[ENCY]
[DIRRULES]
Normalization (RAW →
WORK /
QUARANTINE)
Schema, geometry, time,
identity, evidence, rights, and
policy rules are runnable.
TransformReceipt; ValidationReport
(working set); PolicyDecision;
QUARANTINE for failures.
Quarantine with reason;
never silently promotes.
[ENCY]
[DIRRULES]
Validation (WORK →
PROCESSED)
Validators are deterministic
and tied to fixtures; required
receipts present.
ValidationReport pass;
RedactionReceipt if sensitivity
applies; AggregationReceipt if
applies.
Stay in WORK; structured
FAIL outcome.
[ENCY]
[DIRRULES]
Catalog closure
(PROCESSED →
CATALOG / TRIPLET)
EvidenceRefs resolve; catalog
matrix and digests close.
CatalogMatrix entry;
EvidenceBundle; graph/triplet
projections if applicable.
HOLD at PROCESSED;
structured FAIL outcome;
no public edge.
[ENCY]
[DIRRULES]
Release (CATALOG /
TRIPLET →
PUBLISHED)
Review state where required;
release authority distinct from
the original author when
materiality applies.
ReleaseManifest; rollback target;
correction path; ReviewRecord (if
required).
HOLD at CATALOG; no
public surface change.
[ENCY]
[DIRRULES]
Correction
(PUBLISHED →
PUBLISHED’)
Detected error or new
evidence; downstream
derivatives identified.
CorrectionNotice; ReviewRecord;
invalidation list; ReleaseManifest
update or supersession.
Stale-state announcement;
no silent edit.
[ENCY]
[DIRRULES]
Rollback (PUBLISHED
→ prior release)
Failed release or
post-publication failure;
targeted prior release
identified.
RollbackCard; CorrectionNotice;
ReleaseManifest reverts to prior
release; downstream derivative
invalidation.
Held at current state until
rollback validated.
[ENCY]
[DIRRULES]
24.6.2 Universal closure rules
CONFIRMED doctrine: a transition is closed only when (i) the required artifacts above exist, (ii) every required artifact
resolves — not just references — the artifacts it depends on (EvidenceRef → EvidenceBundle, source_id →
SourceDescriptor, model_id → ModelRunReceipt), and (iii) the policy gate evaluated and recorded its decision. Missing
any of these means the transition fails closed and the prior state is preserved. [ENCY] [DIRRULES]
CONFIRMED doctrine: the trust membrane forbids any public client, any normal UI surface, and any released AI surface
from reaching RAW, WORK, QUARANTINE, canonical/internal stores, graph internals, vector indexes, source APIs, or
direct model runtimes. The gates above are the only routes by which content reaches PUBLISHED, and PUBLISHED is
the only state from which the governed API may emit ANSWER. [GAI] [MAP-MASTER] [ENCY]
24.6.3 Gate failures — reason codes (PROPOSED catalog)

Failure family Reason code (PROPOSED) Gate(s) where it fires Recovery path
Missing required artifact MISSING_RECEIPT,
MISSING_EVIDENCE,
MISSING_REVIEW
Normalization / Validation /
Catalog / Release
Re-emit missing receipt; re-run
review; re-validate.
Schema / contract mismatch SCHEMA_MISMATCH,
CONTRACT_DRIFT
Normalization / Validation Schema fix and/or ADR; re-run
validator.
Rights / sensitivity
unresolved
RIGHTS_UNKNOWN,
SENSITIVITY_UNRESOLVED
Admission / Validation / Catalog
/ Release
Steward review; rights resolution;
tier reassignment.
Source-role collapse risk ROLE_COLLAPSE, ROLE_DOW
NCAST_FORBIDDEN
Validation / Catalog / Release Restore source role; refuse upcast.
Review state inadequate REVIEW_NEEDED,
REVIEW_INSUFFICIENT,
REVIEW_REJECTED
Catalog / Release Run required review; supply
ReviewRecord.
Release infrastructure error RELEASE_MANIFEST_INVALID
,
ROLLBACK_TARGET_MISSING
Release Manifest fix; supply rollback
target.
Correction lineage broken CORRECTION_DERIVATIVES_U
NRESOLVED, CORRECTION_PR
IOR_RELEASE_MISSING
Correction Resolve derivatives; supersession
entry.

9. Master Reviewer Role and Separation-of-Duties Matrix
CONFIRMED doctrine (operating-law invariant 9): KFM separates policy-significant release duties when maturity
justifies it. This section names the roles, the duties, and the cases where separation is required. Atlas v1.0 references
stewards and reviewers across per-domain M. sections but does not consolidate; this is a PROPOSED reference for ADR
discussion. [ENCY] [DIRRULES]
24.7.1 Role definitions (PROPOSED)
Role Definition Scope (PROPOSED) Citation
Source steward Owns admission, rights confirmation, and
sensitivity tag for a named source family.
SourceDescriptor lifecycle; admission
gate.
[ENCY]
[DIRRULES]
Domain steward Owns the meaning, contracts, and validators of a
domain’s object families.
Domain contracts and schemas;
validator authorship; review of
domain-internal promotions.
[ENCY] [DDD]
Sensitivity reviewer Reviews redaction, generalization, withholding,
and tier decisions for sensitive content.
RedactionReceipt; tier transitions for
sensitive lanes.
[ENCY]
[DOM-ARCH]
[DOM-FAUNA]
[DOM-FLORA]
[DOM-PEOPLE]
Rights-holder representative Confirms sovereignty, cultural-heritage, or
consent-based release decisions.
Archaeology, sovereign data,
living-person data, DNA data.
[DOM-ARCH]
[DOM-PEOPLE]
Release authority Issues ReleaseManifests and authorizes
PUBLISHED transitions; distinct from authorship
when materiality applies.
PUBLISHED transitions; rollback
authorization.
[ENCY]
[DIRRULES]
Correction reviewer Reviews CorrectionNotice / RollbackCard before
they amend a PUBLISHED claim.
Post-publication corrections;
rollbacks.
[ENCY]
[DIRRULES]
AI surface steward Reviews Focus Mode templates, AIReceipts, and
policy bindings; audits AI behavior against
doctrine.
Focus Mode; AIReceipt sampling;
cite-or-abstain audits.
[GAI] [UIAI]
Docs steward Owns governance documentation, ADR index,
drift register, and Atlas / supplement integrity.
docs/ tree; ADR index; drift register. [DIRRULES]
24.7.2 Separation-of-duties matrix
Action May the author also
approve?
Required separation (PROPOSED) Citation
Source admission (— → RAW) Yes for routine; No when
source has unresolved
rights / sovereignty.
Source steward + rights-holder rep where applicable. [ENCY]
[DIRRULES]
Normalization receipts Yes for routine; No when
transforms are
sensitivity-relevant.
Domain steward; sensitivity reviewer if
sensitivity-relevant.
[ENCY]
Validator authorship and run Yes (validators are
deterministic).
Domain steward; periodic audit by docs steward. [ENCY]
[DIRRULES]
Promotion to PROCESSED /
CATALOG
Yes for non-sensitive
routine; No for sensitive
lanes.
Domain steward + sensitivity reviewer (sensitive
lanes).
[ENCY]
[DOM-ARCH]
[DOM-FAUNA]
[DOM-PEOPLE]

Action May the author also
approve?
Required separation (PROPOSED) Citation
Release to PUBLISHED No when materiality
applies.
Author ≠ release authority; rights-holder rep where
applicable.
[ENCY]
[DIRRULES]
Sensitive-lane release No. Author + sensitivity reviewer + release authority +
rights-holder rep.
[ENCY]
[DOM-ARCH]
[DOM-FAUNA]
[DOM-PEOPLE]
Correction / rollback No when correction is
steward-significant.
Author / detector + correction reviewer + release
authority.
[ENCY]
[DIRRULES]
AI surface change (template /
policy binding)
No. AI surface steward + docs steward (policy binding). [GAI] [UIAI]
Atlas / supplement publication No. Docs steward + at least one subsystem owner (per
Directory Rules).
[DIRRULES]
Maturity note: Directory Rules §2 and KFM operating law treat separation of duties as maturity-dependent. Early-stage doctrine
work may be authored and approved by the same actor when materiality is low. As maturity rises and the public trust surface expands,
separation must be enforced through tooling, not custom; the supplement does not pretend the enforcement exists yet. [DIRRULES]

24.8 Master Stale-State and Supersession Reference
CONFIRMED doctrine: a PUBLISHED claim may become stale long before it is corrected. KFM separates ‘stale’ from
‘wrong’: a stale claim is one whose evidence, source freshness, dependent data, or context has aged past its declared
tolerance; a wrong claim is one whose substance is incorrect. Both states have visible markers and traceable lifecycles.
[ENCY] [DIRRULES]
24.8.1 Stale-state markers
Marker Triggered by (CONFIRMED
doctrine)
UI signal Required action
Source freshness expired Cadence in SourceDescriptor passed
without a new admission.
Stale source badge in
Evidence Drawer.
Re-admit or supersede; otherwise
mark dependent claims stale.
Schema version drift Object schema upgraded past the
published claim’s schema version.
Schema-drift badge; show
migration ADR if any.
Migrate, re-validate, re-release; or
mark stale.
Geography version drift GeographyVersion replaced; published
claim still bound to prior version.
Geography-version banner
with prior-version cite.
Rebind to current
GeographyVersion; re-release; or
mark stale.
Time-scope outside support Claim’s temporal scope falls outside
current data support window.
Time-out-of-support
indicator.
Mark stale; do not refresh silently.
Model version superseded ModelRunReceipt references an older
model than current.
Model-version badge with
new model identity.
Re-run; supersede; or mark stale.
Review aged out ReviewRecord older than the
review-cycle tolerance for the sensitive
lane.
Review-aged badge. Trigger steward review; potentially
downgrade tier.
Rights status changed Rights change in SourceDescriptor or
rights-holder communication.
Rights-changed badge. Re-evaluate tier; potentially
downgrade; emit CorrectionNotice
if necessary.
Policy version changed Policy referenced by PolicyDecision was
superseded.
Policy-version badge. Re-run gate; potentially supersede
release.
24.8.2 Supersession lineage (extends Atlas v1.0 Appendix E)
Object class Supersession rule Required lineage artifact
SourceDescriptor Replaced by a newer descriptor; old descriptor retained with
superseded_by link.
Supersession entry in source register.
EvidenceBundle Replaced when corrected; old bundle retained for audit. EvidenceBundle + CorrectionNotice +
supersession link.
GeographyVersion Replaced by a newer version; both versions remain queryable
for time-bound claims.
Version register entry + crosswalk.
Schema (under
schemas/contracts/v1/...)
Replaced via ADR; old schema retained. ADR + supersession link in schema header.
Policy Replaced via accepted ADR; old policy retained. ADR + supersession link.
ReleaseManifest Replaced by next release; rollback target remains valid. Manifest history + rollback chain.
AIReceipt Never superseded retroactively. Old answer retained; new
answer is a new receipt.
Two distinct AIReceipts with
cross-reference.
Atlas / supplement Superseded by ADR-recorded new version; lineage retained. Atlas / supplement supersession appendix.

24.9 Master Failure-Mode and Anti-Pattern Register
CONFIRMED doctrine: KFM doctrine names its anti-patterns rather than hoping reviewers will recognize them.
Directory Rules §13 covers placement anti-patterns; Atlas v1.0 §19 covers the cross-domain trust-membrane
anti-patterns. This supplement merges them into one register and adds the failure-mode catalog. [DIRRULES] [ENCY]
24.9.1 Placement and authority anti-patterns
Anti-pattern What goes wrong Where it shows up Counter-rule Citation
Two parallel schema
homes
Schemas authored under both schemas/ and
contracts/ or jsonschema/ without ADR;
reviewers no longer know which version is
authoritative.
Repo root tree. Single schema home (default
schemas/contracts/v1/…);
ADR-0001 governs migration.
[DIRRULES]
Domain folder at repo
root
Topic-based root (e.g., hydrology/)
competes with responsibility roots and
fragments the lifecycle.
Repo root tree. Domain files live under
responsibility roots; root
folders are governance-bearing
only.
[DIRRULES]
Compatibility root used
as authority
Files that should be in schemas/ or policy/
end up in jsonschema/ or policies/ and
harden into authority.
jsonschema/,
policies/, ui/, web/.
Compatibility roots are
mirrors; per-root README
must declare class.
[DIRRULES]
Artifacts directory
holding receipts
artifacts/ used to store proofs, receipts, or
release manifests — collapsing build
output, process memory, and trust-bearing
records.
artifacts/. artifacts/ is build / docs / qa
scratch only; trust-bearing
receipts live under data/ or
release/.
[DIRRULES]
Schema authored
alongside data file
Schema and instance live in the same
directory; reviewers drift.
data/, dossier folders. Shape under schemas/;
meaning under contracts/;
instance under data/.
[DIRRULES]
24.9.2 Trust-membrane anti-patterns
Anti-pattern What goes wrong DENY surface Citation
Public client reads RAW / WORK /
QUARANTINE.
Trust membrane bypassed; promotion gates
skipped.
Governed API; layer manifest resolver. [ENCY] [GAI]
[DIRRULES]
Map shell consumes canonical /
internal store directly.
Renderer becomes the public surface and
inherits no governance.
MapLibre shell wiring; layer registry. [MAP-MASTER]
[GAI]
AI returns uncited language. Generated text substitutes for evidence;
cite-or-abstain rule broken.
Focus Mode; AI surface steward. [GAI] [ENCY]
AI answers from RAW / WORK
rather than EvidenceBundle.
AI becomes its own truth source. Governed AI runtime; AIReceipt evaluator. [GAI]
Sensitive content released without
redaction.
RedactionReceipt missing; rights /
sovereignty violation.
Release queue; sensitivity reviewer. [DOM-ARCH]
[DOM-FAUNA]
[DOM-PEOPLE]
[ENCY]
Aggregate cited as per-place
observation.
Source-role collapse; matrix-cell semantics
violated.
Validator; Focus Mode citation evaluator. [DOM-AG]
[DOM-PEOPLE]
Synthetic surface presented without
Reality Boundary Note.
Reconstruction read as observation. Scene admission gate; representation
receipt validator.
[MAP-MASTER]
[UIAI]
KFM used as alert / instruction
authority.
Out-of-scope use of governed evidence as
life-safety guidance.
Hazards / Air / Hydrology surfaces. [DOM-HAZ]
Release without ReleaseManifest or
rollback target.
Public surface cannot be rolled back;
release not auditable.
Release queue; release authority. [ENCY]
[DIRRULES]

Anti-pattern What goes wrong DENY surface Citation
AI generation routed through admin
shortcut.
Admin bypass becomes a normal-path
public route.
Trust-membrane audit; infra. [GAI]
[DIRRULES]
24.9.3 Governance-process anti-patterns
Anti-pattern Counter-rule
Documenting a change instead of validating it. Docs are part of the working system but never substitute for validators, fixtures, or
schema. [DIRRULES]
Approving one’s own release on a sensitive lane. Separation-of-duties matrix §9.2; release authority distinct from author. [ENCY]
Treating an Atlas summary or matrix as evidence. Atlas, supplements, and master matrices are reference views; EvidenceBundle
remains authoritative. [ENCY]
Silent migrations between schema or policy homes. ADR required (Directory Rules §2.4); migration plan; supersession entry.
[DIRRULES]
Promotion that ‘upgrades’ a source role (e.g., modeled
→ observed).
Source role is fixed at admission; never upgraded by promotion. [ENCY] §3 of this
supplement.
Re-publishing a corrected claim without invalidating
derivatives.
CorrectionNotice must list invalidated derivatives; rollback card if needed. [ENCY]
[DIRRULES]

24.10 Master Risk Register and Threat Posture
PROPOSED register: a consolidated risk register that names trust-relevant risks across KFM, the guardrails that already
exist in v1.0 doctrine, and the residual concerns. This is a planning view, not a vulnerability catalog. Severity is
qualitative. [ENCY] [DIRRULES] [GAI]
Risk family Specific risk Severi
ty
Existing guardrails
(CONFIRMED doctrine)
Residual concern
(PROPOSED)
Citation
Source integrity Source role mislabeling at
admission (e.g., model output
ingested as observation).
High SourceDescriptor with role;
validator rejecting role
inconsistency; Source-Role
Anti-Collapse Register (this
supplement §3).
Validator coverage may not
include every role-pair;
periodic audit needed.
[ENCY]
Source integrity Source rights or sovereignty
status changes without
re-evaluation.
High Stale-state markers (this
supplement §10.1); source
freshness cadence; review
aged-out tolerance.
Rights-change detection across
third-party sources is not
automated.
[ENCY]
[DOM-PEOPLE]
Evidence chain EvidenceRef fails to resolve at
runtime; public surface still
renders.
High Cite-or-abstain rule; governed
API; ABSTAIN as a finite
outcome.
Public-surface caching could
mask resolution failure; audit
needed.
[GAI] [ENCY]
Promotion Promotion skipped or
short-circuited (admin path
used as public path).
High Trust membrane forbids public
access to RAW/WORK; admin
shortcuts must be justified,
constrained, audited.
Local-runtime admin endpoints
can drift; deny-by-default infra
and audit.
[ENCY]
[DIRRULES]
Sensitivity Sensitive coordinates leaked
via tile / vector / 3D /
screenshot / export.
High Tiered scheme (§7);
RedactionReceipt; sensitive-lane
fail-closed; 3D admission gate.
Side-channel leaks via labels,
popups, or AI text;
cross-surface lint needed.
[DOM-ARCH]
[DOM-FAUNA]
[DOM-FLORA]
[DOM-PEOPLE]
Sensitivity Living-person data exposed via
inference (e.g., aggregate +
context join).
High Aggregation receipt;
minimum-cell suppression;
person-parcel join denial.
Inference risk grows with
cross-lane joins; periodic threat
modeling of joins.
[DOM-PEOPLE]
AI governance AI emits uncited or weakly
cited language.
High AIReceipt; ABSTAIN/DENY
outcomes; AI surface steward
audit; Focus Mode templates.
Template drift;
out-of-distribution prompts;
mandatory AIReceipt
sampling.
[GAI] [UIAI]
AI governance AI presents synthetic content
as observed reality.
High Reality Boundary Note;
Representation Receipt;
deny-by-default 3D admission.
Text-only AI surfaces have
weaker visual cues; UI lint and
AIReceipt language gates.
[GAI]
[MAP-MASTER]
[UIAI]
Renderer / map Map shell becomes a public
surface (caching layers,
circumventing governed API).
Mediu
m
Renderer-boundary tests; layer
manifest resolver;
release-state-tagged tiles.
Third-party tile caches; bypass
audits.
[MAP-MASTER]
Lifecycle Schema or policy migrated
without ADR; downstream
code drifts.
Mediu
m
Directory Rules §2.4 ADR
requirement; per-root README;
drift register.
Drift register may lag
detection; periodic Directory
Rules audit.
[DIRRULES]
Lifecycle Correction published without
invalidating derivatives
(graphs, exports, stories).
Mediu
m
CorrectionNotice + invalidation
list; StorySnapshot receipts.
Cross-system invalidation
coverage; periodic
downstream-derivative audit.
[ENCY] [UIAI]
Release Public release lacks rollback
target.
Mediu
m
ReleaseManifest required at
PUBLISHED gate; rollback target
mandatory.
Manual rollback rehearsals;
rehearsal logs.
[ENCY]
[DIRRULES]

Risk family Specific risk Severi
ty
Existing guardrails
(CONFIRMED doctrine)
Residual concern
(PROPOSED)
Citation
Operational Local exposed system
(developer host, demo)
reachable beyond the loopback
boundary.
Mediu
m
Deny-by-default access; least
privilege; audit logging;
operational governance.
Host hardening drift; periodic
infra review.
[DIRRULES]
Source-role
abuse
AI surface used to perform
‘source-role upgrade’ by
paraphrase (e.g., quoting an
aggregate as a per-place fact).
High Cite-or-abstain; AIReceipt;
outcome envelope.
Paraphrase detection; periodic
AIReceipt sampling; ban list of
upcasting phrases.
[GAI]
Documentation Atlas / supplement / dossiers
cited as implementation proof.
Mediu
m
Truth labels; v1.0 self-check; this
supplement §1, §17.
Reviewers may slip; periodic
audit.
[DIRRULES]

24.11 Master Governance Health Indicators
PROPOSED indicators: measurable signals of whether KFM is operating in keeping with its own doctrine. None of these
is a sufficient condition for trust; together they describe a healthy posture. Indicators are reported, not enforced;
enforcement is the validator’s job. [ENCY] [DIRRULES]
24.11.1 Evidence and source integrity
Indicator What it measures Healthy posture (PROPOSED)
EvidenceRef resolution rate % of public-surface EvidenceRefs that resolve to an
EvidenceBundle on demand.
> 99.9% over the trailing release window.
Cite-or-abstain compliance % of Focus Mode answers with non-empty, resolving
evidence citations.
100% (any miss is a defect to investigate).
Source-role distribution drift Distribution of admitted source roles over time per
domain.
No silent shift without a documented ADR or
steward note.
Stale source rate % of admitted sources past their freshness cadence. Stewards reviewed and dispositioned (refresh /
supersede / mark stale) within tolerance.
Quarantine throughput % of admitted records that quarantine and the rate of
clearance.
Visible, with cause distribution; sustained high
backlog is a defect.
24.11.2 Release, correction, rollback
Indicator What it measures Healthy posture (PROPOSED)
Release with rollback target % of PUBLISHED releases that name a valid rollback
target.
100%.
Correction lead time Median time from defect detection to CorrectionNotice. Visibly tracked; trend not regressing.
Derivative-invalidation coverage % of corrections that name and invalidate downstream
derivatives.
Approaches 100% as coverage matures.
Rollback rehearsal rate Number of rehearsed rollbacks per release window. Non-zero; periodic, scheduled.
Supersession lineage gap Number of supersessions without a forward link. Zero.
24.11.3 Sensitivity and rights
Indicator What it measures Healthy posture (PROPOSED)
Sensitive-lane fail-closed rate % of unauthorized sensitive-lane requests that DENY at
the first gate.
100% at the first gate.
RedactionReceipt coverage % of public-safe transformations that emit a
RedactionReceipt.
100% for sensitive lanes.
Review-aged-out incidence Number of sensitive-lane claims past their review
cadence.
Visibly tracked; trend not regressing.
Rights-change response time Median time from rights-change detection to tier
reassignment.
Within stated tolerance per source family.
Sensitive-content side-channel
audit
Frequency of automated checks for label / popup /
AI-text leaks.
Periodic; documented.
24.11.4 AI surface health
Indicator What it measures Healthy posture (PROPOSED)
AIReceipt presence rate % of Focus Mode answers with an AIReceipt. 100%.

Indicator What it measures Healthy posture (PROPOSED)
ABSTAIN rate by template How often each Focus Mode template abstains. Visibly tracked; very low ABSTAIN suggests
over-fitting; very high suggests evidence gaps.
DENY reason distribution Reason codes returned by Focus Mode denials. Stable; large new-reason spikes investigated.
Synthetic-claim incidence % of audited AI answers flagged for presenting
synthetic content as observed.
Approaches zero; never silently.
24.11.5 Documentation and drift
Indicator What it measures Healthy posture (PROPOSED)
ADR completeness % of structural moves with an accepted ADR. 100% for Directory Rules §2.4 cases.
Drift register size Open entries in docs/registers/DRIFT_REGISTER.md. Visibly tracked; aged entries investigated.
Per-root README presence % of canonical roots with a current README
declaring authority class.
100%.
Atlas / supplement lineage clarity Each Atlas/supplement carries a current supersession
entry.
100%.

24.12 Master Open-ADR Backlog
PROPOSED backlog: a consolidated list of architectural questions that, per Directory Rules §2.4 and the operating law,
would warrant an ADR before a path, schema, policy, or release surface is treated as canonical. This list is drawn from
the v1.0 N. (Verification backlog) and Appendix F. (Self-check) entries; it is intended for triage, not for execution.
[DIRRULES] [ENCY]
# Question / decision needed Why it’s ADR-class Suggested ADR title (PROPOSED)
ADR-S-01 Where is the canonical schema home?
Confirm schemas/contracts/v1/… by
ADR-0001 or amend.
Schema-home rule is explicitly
ADR-required per Directory Rules §2.4(3).
Schema home: schemas/contracts/v1/…
(confirm or amend ADR-0001).
ADR-S-02 Should domain dossiers live under
docs/dossiers/ or docs/atlases/?
Placement of doctrine artifacts within docs/
is Directory Rules-class; minor but worth
recording.
Doctrine artifact placement under docs/.
ADR-S-03 Receipt class home:
schemas/contracts/v1/receipts/ vs.
schemas/contracts/v1/<domain>/receipts/.
A new parallel home or split is ADR-class
per Directory Rules §2.4(5).
Receipt schema layout.
ADR-S-04 Source-role enum — canonical vocabulary,
evolution rule.
Source-role anti-collapse is
doctrine-significant; vocabulary stability
matters.
Source-role vocabulary v1.
ADR-S-05 Sensitivity tier scheme (T0–T4) — adopt as
canonical or revise.
Tier scheme directly governs public
release; adoption is doctrine-class.
Sensitivity tier scheme.
ADR-S-06 AI surface boundary: Focus Mode vs. open AI
access (always denied? bounded?
steward-only?).
AI access boundary is a trust-membrane
question.
AI surface scope and trust-membrane
stance.
ADR-S-07 3D admission policy: minimum required
receipts, deny lanes, reality-boundary
disclosure.
3D scenes are higher-exposure; admission
policy is release-significant.
3D admission policy.
ADR-S-08 Frontier Matrix cell semantics: what counts as
a matrix-cell release, when is it stale, how do
corrections cascade.
Matrix cell is its own analytical release;
rules govern publication and rollback.
Frontier Matrix release rules.
ADR-S-09 Reviewer role separation: when is separation
enforced by tooling vs. custom.
Separation-of-duties affects release
authority; needs explicit threshold and
tooling.
Reviewer separation-of-duties threshold.
ADR-S-10 Stale-state propagation: how does a stale
upstream propagate stale-state markers to
downstream claims?
Cross-lane staleness is a correction-path
question.
Stale-state propagation.
ADR-S-11 Story / export receipt scope and retention. Stories and exports are public carriers; their
receipts and retention govern
post-publication correction.
Story / export receipt policy.
ADR-S-12 Connector cadence and quarantine recovery
policy.
Connector behavior governs RAW
admission; cadence and quarantine
recovery are operational-doctrine.
Connector cadence and quarantine
recovery.
ADR-S-13 Drift register triage: how often, by whom, with
what outcome.
Drift register is the bridge between repo
state and doctrine; needs an explicit triage
rule.
Drift register triage.
ADR-S-14 Cross-lane join policy: which joins require
steward review, which are denied, which are
open.
Cross-lane joins are inference-risk
multipliers.
Cross-lane join policy.
ADR-S-15 Atlas / supplement lifecycle: cadence of
revisions; deprecation rule; supersession path.
Doctrine artifacts also have a lifecycle;
should not drift.
Doctrine artifact lifecycle.

24.13 Atlas Section ↔ Dossier ↔ Responsibility Root Crosswalk
CONFIRMED purpose: v1.0 §2.1 maps each domain to its source dossier. This crosswalk extends that mapping with the
proposed responsibility root from Directory Rules §5. The goal is that any domain’s authority surface, evidence, and repo
home are discoverable from a single row. [DIRRULES] [ENCY]
Atlas
v1.0
chapter
Domain Source dossier (short
name)
Primary responsibility root
(PROPOSED)
Notes (PROPOSED / NEEDS
VERIFICATION)
3 Spatial Foundation (spine: encyclopedia +
MapLibre master)
schemas/contracts/v1/spatial/;
contracts/spatial/; packages/maplibre/
Compatibility: styles/, viewer_templates/;
migration target packages/maplibre/.
4 Hydrology [DOM-HYD] schemas/contracts/v1/hydrology/;
contracts/hydrology/
Proof-bearing thin slice (roadmap phase
5).
5 Soil [DOM-SOIL] schemas/contracts/v1/soil/;
contracts/soil/
Support-type separation per dossier.
6 Habitat [DOM-HAB]
[DOM-HF]
schemas/contracts/v1/habitat/;
contracts/habitat/
Pairs with Fauna under thin-slice plan.
7 Fauna [DOM-FAUNA]
[DOM-HF]
schemas/contracts/v1/fauna/;
contracts/fauna/;
policy/sensitivity/fauna/
Sensitive-occurrence lane; T4 default for
sensitive species.
8 Flora [DOM-FLORA] schemas/contracts/v1/flora/;
contracts/flora/; policy/sensitivity/flora/
Rare-plant lane; ethnobotanical context
governance.
9 Agriculture [DOM-AG] schemas/contracts/v1/agriculture/;
contracts/agriculture/
Aggregation receipts central; private-join
denial defaults.
10 Geology / Natural
Resources
[DOM-GEOL] schemas/contracts/v1/geology/;
contracts/geology/
Subsurface and resource-estimate
contexts.
11 Atmosphere / Air [DOM-AIR] schemas/contracts/v1/air/;
contracts/air/
Source-role anti-collapse for
observed/regulatory/modeled/aggregate is
acute.
12 Hazards [DOM-HAZ] schemas/contracts/v1/hazards/;
contracts/hazards/;
policy/release/hazards/
KFM is never an alert authority.
13 Roads / Rail / Trade [DOM-ROADS] schemas/contracts/v1/transport/;
contracts/transport/
Network identity governance.
14 Settlements /
Infrastructure
[DOM-SETTLE] schemas/contracts/v1/settlement/;
contracts/settlement/;
policy/sensitivity/infrastructure/
Critical-asset deny lane.
15 Archaeology / Cultural
Heritage
[DOM-ARCH] schemas/contracts/v1/archaeology/;
contracts/archaeology/;
policy/sensitivity/archaeology/
Sovereignty review path; deny default for
site coords.
16 People / Genealogy /
DNA / Land
[DOM-PEOPLE] schemas/contracts/v1/people/;
contracts/people/;
policy/sensitivity/people/;
policy/consent/people/
Living-person, DNA, and person-parcel
lanes deny-default.
17 Frontier Matrix (spine: ENCY +
UNIFIED)
schemas/contracts/v1/matrix/;
contracts/matrix/
Matrix-cell release rules; cell receipt.
18 Planetary / 3D / Digital
Twin / Synthetic
[MAP-MASTER]
[UIAI]
schemas/contracts/v1/scene/;
contracts/scene/; policy/release/scene/
3D admission policy; reality-boundary
doctrine.

Atlas
v1.0
chapter
Domain Source dossier (short
name)
Primary responsibility root
(PROPOSED)
Notes (PROPOSED / NEEDS
VERIFICATION)
19 (Cro
ss-doma
in syste
ms)
— MapLibre + GAI + UIAI
+ ENCY + UNIFIED
apps/governed-api/;
apps/explorer-web/;
packages/maplibre/; packages/ui/
Trust-membrane systems.
20
(Master
Atlases)
— (meta) MapLibre + GAI
+ ENCY + DIRRULES
docs/atlases/; control_plane/ Doctrine and machine-readable indexes.
21 (Roa
dmap)
— (meta) UNIFIED +
DIRRULES + ENCY
docs/roadmap/ Per-phase rollback posture preserved.
22 (App
endices)
— (meta) DDD +
DIRRULES + ENCY
docs/ Glossary and indexes; not
implementation.
NEEDS VERIFICATION: every responsibility-root path above is PROPOSED. Confirmation requires inspection of a mounted repo.
[DIRRULES]

24.14 Master Object Family × Domain Reference Matrix
PROPOSED matrix: which domains own each cross-cutting object family and which other domains cite it. This
consolidates v1.0 Appendix C and the per-domain F. tables into one view, to help reviewers see at a glance where an
object change ripples. [ENCY]
Object family Owner (CONFIRMED
doctrine)
Citing domains (CONFIRMED doctrine) Sensitivity default
(PROPOSED, this
supplement)
Citation
GeographyVersion Spatial Foundation All domains (any spatial product carries a
version).
T0 [MAP-MASTE
R]
CoordinateReferenceProfile Spatial Foundation All map producers. T0 [MAP-MASTE
R]
SourceDescriptor (cross-cutting, owned by
source steward)
All domains. varies by source;
defaults per domain
rules.
[ENCY]
EvidenceBundle (cross-cutting, owned by
ENCY doctrine)
All public claim surfaces. varies; mirrors the
claim’s tier.
[ENCY]
HUC / Watershed / Reach Hydrology Soil; Habitat; Fauna; Flora; Agriculture;
Hazards; Settlements; Frontier Matrix.
T0 [DOM-HYD]
NFHL zone Hydrology (regulatory
channel)
Hazards; Settlements; UI. T0 (regulatory) [DOM-HYD]
GaugeSite / FlowObservation Hydrology Hazards; Agriculture; Frontier Matrix. T0 [DOM-HYD]
SoilMapUnit / SoilComponent Soil Habitat; Agriculture; Hazards; Settlements
(advisory).
T0 [DOM-SOIL]
HabitatPatch /
EcologicalSystem
Habitat Fauna; Flora; Agriculture; Planetary/3D. T0 mostly; T1 for
stewardship zones.
[DOM-HAB]
OccurrenceRecord (sensitive) Fauna Habitat (public-safe derivative only);
Hazards (disease).
T4 default; T1 via
generalization.
[DOM-FAUN
A]
RangePolygon Fauna / Flora Habitat; Conservation; UI. T1 [DOM-FAUN
A] [DOM-FLO
RA]
RarePlantRecord Flora Habitat (public-safe derivative only);
Archaeology (ethnobotanical context,
steward review).
T4 default; T1 via
generalization.
[DOM-FLORA
]
CropObservation /
YieldObservation
Agriculture Frontier Matrix; Hazards (drought). T0 (aggregate) / T1
(field candidate).
[DOM-AG]
GeologicUnit / Lithology Geology Hydrology; Hazards; Agriculture;
Planetary/3D.
T0 [DOM-GEOL]
MineralOccurrence /
ResourceEstimate
Geology Hazards; Settlements; Frontier Matrix. T0 for aggregate; T2 for
detail in sensitive
contexts.
[DOM-GEOL]
WeatherObservation /
ClimateNormal
Atmosphere/Air Hydrology; Agriculture; Hazards; Frontier
Matrix.
T0 [DOM-AIR]
HazardEvent /
HazardObservation
Hazards All domains as cited context; UI; Frontier
Matrix.
T0 [DOM-HAZ]
DisasterDeclaration Hazards Settlements; UI. T0 [DOM-HAZ]
RoadSegment / RailSegment /
CorridorRoute
Roads/Rail Settlements; Archaeology (historical
context); Frontier Matrix.
T0 [DOM-ROADS
]

Object family Owner (CONFIRMED
doctrine)
Citing domains (CONFIRMED doctrine) Sensitivity default
(PROPOSED, this
supplement)
Citation
TransportFacility Roads/Rail Settlements; Hazards. T0 mostly; T2 / T4 for
sensitive condition
detail.
[DOM-ROADS
]
Settlement / Municipality /
GhostTown
Settlements People/Land; Frontier Matrix;
Archaeology.
T0 [DOM-SETTL
E]
Infrastructure Asset (critical) Settlements/Infrastructur
e
Hazards (with restriction). T4 default for critical
detail; T1 for generalized
footprint.
[DOM-SETTL
E]
ArchaeologicalSite Archaeology Settlements (historical context,
generalized); Planetary/3D
(admission-gated).
T4 default; T1
generalized only after
steward review.
[DOM-ARCH]
CulturalTemporalPeriod Archaeology Settlements; Frontier Matrix. T0 [DOM-ARCH]
PersonAssertion /
NameAssertion
People/Genealogy Settlements; Frontier Matrix. T1 / T2 (living-person
fields denied); aggregate
T0.
[DOM-PEOPL
E]
DNAMatchEvidence /
DNASegment
People/Genealogy (internal; not cross-cited). T4. [DOM-PEOPL
E]
LandParcel People/Land Agriculture (with restrictions); Settlements. T0 aggregate; T2/T4
private join detail.
[DOM-PEOPL
E]
FrontierDefinition /
CountyYearPanel
Frontier Matrix All domain analytics surfaces. T0 [ENCY]
[UNIFIED]
SceneManifest / TerrainModel
/ 3DTileSet
Planetary/3D All domains via admission. T0 / T1 / T2 / T4 by
content sensitivity.
[MAP-MASTE
R] [UIAI]
SyntheticSurface Planetary/3D (internal carrier; not cross-cited). T1 / T2 with mandatory
Reality Boundary Note.
[MAP-MASTE
R] [UIAI]
LayerManifest MapLibre / governed
API
All map-bearing public surfaces. T0 (manifest); content
tiers vary.
[MAP-MASTE
R]
AIReceipt Governed AI All Focus Mode surfaces. T2 / T0 depending on
contents.
[GAI]
ReleaseManifest /
RollbackCard
Release authority All PUBLISHED surfaces. T0 (manifest) / contents
may be T2 audit-only.
[ENCY]
[DIRRULES]
CorrectionNotice Correction reviewer All PUBLISHED surfaces. T0. [ENCY]
[DIRRULES]

Appendix G — v1.0 → v1.1 Lineage and Supersession Record
CONFIRMED purpose: Appendix G is the formal lineage record for the supersession of the Kansas Frontier Matrix
Domains Culmination Atlas, v1.0 (2026-05-11) by v1.1 (this document, 2026-05-12). It complements and does not
replace v1.0’s own Appendix E. v1.0 Appendix E remains the lineage record for everything that v1.0 itself superseded;
Appendix G records only the v1.0 → v1.1 step. [ENCY] [DIRRULES]
G.1 Supersession header
Field Value (CONFIRMED in this edition)
Prior edition Kansas Frontier Matrix Domains Culmination Atlas, v1.0; PDF dated 2026-05-11; 139 pages.
Current edition Kansas Frontier Matrix Domains Culmination Atlas, v1.1 (this document).
Supersession mode Integrated extension. v1.0 is retained verbatim as the interior of v1.1; v1.1 adds front matter,
Chapter 24, and Appendix G.
Supersession scope Edition identity only. v1.1 is the current edition for citation and circulation; v1.0 remains a
standalone, citable, historically valid artifact.
Reversibility Full. Removing v1.1 front matter, Chapter 24, and Appendix G yields v1.0 unchanged.
Conflict posture v1.0 retains authority over its original content. Any apparent disagreement between Chapter
24 and a v1.0 section is filed to docs/registers/DRIFT_REGISTER.md per Directory Rules
§2.5.
Authoring posture Doctrine synthesis only. v1.1 makes no new implementation claim and introduces no new
schema, route, validator, dashboard, or authority root.
G.2 What v1.1 adds (delta from v1.0)
v1.1 addition Posture vs. v1.0 Lineage link
Front matter: edition note, What is new in v1.1, Integrated
Contents.
Net addition. No v1.0 content altered. (this document, front
matter)
Chapter 24 — Extended Master Atlases (14 master
registers).
Net addition; positioned after the v1.0 interior
in this PDF.
(this document, Ch.
24)
Appendix G — v1.0 → v1.1 Lineage and Supersession
Record.
Net addition; complements v1.0 Appendix E. (this document, App.
G)
Edition metadata: Title set to ‘Kansas Frontier Matrix
Domains Culmination Atlas, v1.1’.
PDF metadata only; interior pages of v1.0
unchanged.
(PDF metadata)
G.3 What v1.1 does not change
Item Status under v1.1
Any v1.0 chapter (chs. 1–23). CONFIRMED unchanged. Page numbering, internal references, and
figure-to-generate IDs remain valid against v1.0.
v1.0 Appendix A (Glossary). CONFIRMED unchanged. Chapter 24 introduces no new glossary terms.
v1.0 Appendix B (Source family index / citation tags). CONFIRMED unchanged. Chapter 24 reuses existing short names only
(ENCY, DIRRULES, MAP-MASTER, GAI, DDD, UNIFIED, UIAI,
INDEX-18, DOM-*).

Item Status under v1.1
v1.0 Appendix C (Object family index). CONFIRMED unchanged. Chapter 24.14 extends the matrix but does not edit
v1.0 Appendix C.
v1.0 Appendix D (Directory Rules summary). CONFIRMED unchanged.
v1.0 Appendix E (Supersession and lineage). CONFIRMED unchanged. Appendix G is the v1.0 → v1.1 record only.
v1.0 Appendix F (Self-check). CONFIRMED unchanged. v1.1 carries its own self-check at G.6.
v1.0 chapter 23 (Assembly instructions). CONFIRMED unchanged. v1.1 was assembled by the procedure recorded at
G.5.
v1.0 truth labels and citation conventions. CONFIRMED unchanged. v1.1 inherits and reuses them.
Source dossiers (encyclopedia, directory rules,
MapLibre master, governed AI, DDD, INDEX-18, all
DOM-* dossiers).
CONFIRMED unchanged. v1.1 cites them; does not edit them.
G.4 Edition identity and citation form
Field Value
Title (PDF metadata) Kansas Frontier Matrix Domains Culmination Atlas, v1.1
Author (PDF metadata) KFM Domain Synthesizer
Edition date 2026-05-12
Supersedes v1.0 (PDF dated 2026-05-11; 139 pages)
Recommended citation form
(PROPOSED)
KFM Domain Synthesizer (2026). Kansas Frontier Matrix Domains Culmination Atlas,
v1.1. Edition supersedes v1.0; v1.0 retained verbatim as interior.
PROPOSED repo placement docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf (Directory Rules §5 / §6.1);
v1.0 retained at its existing path.
NEEDS VERIFICATION Final repo placement, file naming, and the review record (ADR / ReviewRecord) for the
v1.0 → v1.1 step against a mounted repository.
G.5 Assembly procedure for v1.1 (CONFIRMED in this edition)
CONFIRMED steps: (1) v1.1 front-matter pages are produced by reportlab and saved as a standalone PDF; (2) v1.0 is
referenced as a read-only input PDF and is not modified; (3) v1.1 back-matter pages (Chapter 24 plus Appendix G) are
produced by reportlab and saved as a standalone PDF; (4) the three PDFs are concatenated in order — front, v1.0 interior,
back — into the final v1.1 PDF using pypdf; (5) the final PDF’s Title metadata is set to ‘Kansas Frontier Matrix Domains
Culmination Atlas, v1.1’. CONFIRMED property: the v1.0 interior bytes are passed through unchanged. [ENCY]
[DIRRULES]
G.6 v1.1 self-check
Question Result Status
Does v1.1 retain every page of v1.0 verbatim? Yes — v1.0 is concatenated into the interior of v1.1
without modification.
CONFIRMED in this edition
(G.5).
Does v1.1 rewrite or contradict any v1.0 chapter,
table, or appendix?
No — all v1.1 additions are net-new (front matter, Ch.
24, App. G).
CONFIRMED.

Question Result Status
Does v1.1 introduce a new domain, lifecycle phase,
authority root, or object family?
No — doing so would require an ADR per Directory
Rules §2.4.
CONFIRMED.
Does v1.1 introduce new citation short names? No — only the v1.0 short names (ENCY, DIRRULES,
MAP-MASTER, GAI, DDD, UNIFIED, UIAI,
INDEX-18, DOM-*) are reused.
CONFIRMED.
Are all sensitive-domain defaults still failing closed? Yes — archaeology coords, sensitive fauna/flora,
living-person fields, DNA, critical infrastructure,
KFM-as-alert-authority default to T4 in Ch. 24.5.
CONFIRMED in Ch. 24.5.
Are Ch. 24 master tables navigational, not
authoritative?
Yes — EvidenceBundle, source dossiers, and
schemas/contracts/v1/… remain canonical.
CONFIRMED.
Is v1.1 reversible to v1.0? Yes — removing v1.1 front matter, Ch. 24, and App. G
yields v1.0 unchanged.
CONFIRMED.
Are unsupported implementation claims absent? Yes — routes, validators, dashboards, file paths, and
ADR outcomes remain PROPOSED or NEEDS
VERIFICATION wherever they appear.
CONFIRMED in this edition
/ NEEDS final scan.
Is the v1.0 → v1.1 supersession discoverable from
one row?
Yes — Appendix G.1 carries the supersession header. CONFIRMED.
G.7 Forward verification backlog for v1.1
# Item to verify Evidence that would settle it Status
VB-11-0
1
Schema home schemas/contracts/v1/…
confirmed by ADR-0001 and present in
mounted repo.
Mounted repo + ADR-0001 text. NEEDS VERIFICATION
VB-11-0
2
docs/atlases/ presence for v1.0 and v1.1
files.
Mounted repo tree. NEEDS VERIFICATION
VB-11-0
3
Receipt schemas present under
schemas/contracts/v1/receipts/.
Mounted repo + schemas. NEEDS VERIFICATION
VB-11-0
4
Source-role vocabulary present and used by
validators.
Schemas + validator code +
ValidationReports.
NEEDS VERIFICATION
VB-11-0
5
Sensitivity tier T0–T4 adopted as canonical
(ADR-S-05).
ADR + policy text. NEEDS VERIFICATION /
PROPOSED
VB-11-0
6
Per-root README presence for canonical
roots.
Mounted repo tree. NEEDS VERIFICATION
VB-11-0
7
Drift register present at
docs/registers/DRIFT_REGISTER.md.
Mounted repo tree. NEEDS VERIFICATION
VB-11-0
8
Governance health indicators (Ch. 24.11)
instrumented or owned by a steward.
Dashboard or steward note. NEEDS VERIFICATION /
PROPOSED
VB-11-0
9
Cross-lane join policy ADR drafted
(ADR-S-14).
ADR text. NEEDS VERIFICATION /
PROPOSED
VB-11-1
0
ReviewRecord exists for the v1.0 → v1.1
step.
Repo state at PUBLISHED. NEEDS VERIFICATION
End of Appendix G. End of v1.1 back matter. The v1.0 interior of this document (chapters 1–23 and v1.0 appendices A–F) remains the
doctrinal core and is unchanged. [ENCY] [DIRRULES] [MAP-MASTER] [GAI]
