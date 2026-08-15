<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-security-readme
title: docs/security/ — Security Guidance and Trust-Boundary Index
type: readme
subtype: sensitive-boundary-landing-page
version: v1.1
prior_version: v1
status: draft; repository-grounded; documentation-only; non-authoritative
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable security, policy, release, incident-response, and independent-review assignments"
created: 2026-05-08
updated: 2026-08-14
policy_label: repository-facing; mixed child sensitivity
current_path: docs/security/README.md
owning_root: docs/
responsibility: "Orient readers to KFM security guidance, disclose the current document inventory and maturity, preserve fail-closed trust boundaries, and route enforcement, operational response, evidence, and release work to their owning responsibility roots."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory security-documentation index
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, implementation, evidence, review, release, correction, and rollback authorities
canonical_relationship: same-path update; no sibling authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3abe21f9285ed7d2f9f652a2672d8f669aa7e884
  target_prior_blob: c4379f54f9f91b0d1d712cc3c569d2fe58a39f4a
  first_path_history_commit: 026b5baa7c1279ece55f9b1fa67c1770bfbddccd
  long_form_security_readme_commit: 1d31edda4e3f5b9143b37e5cb59920a24128f1c3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_status: accepted
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  inventory:
    direct_markdown_files_including_this_readme: 9
    direct_child_guidance_files: 8
    direct_child_directories: 0
    current_repo_grounded_child_docs: 1
    older_draft_child_docs_requiring_file_specific_reconciliation: 7
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - SECURITY.md
  - docs/runbooks/README.md
  - docs/runbooks/INCIDENT_RESPONSE.md
  - docs/security/THREAT_MODEL.md
  - docs/security/EXPOSURE_PLAN.md
  - docs/security/INCIDENT_RESPONSE.md
  - docs/security/DATA_CLASSIFICATION.md
  - docs/security/DENY_TESTS.md
  - docs/security/AUDIT_INVARIANTS.md
  - docs/security/SECRETS.md
  - docs/security/KEY_ROTATION.md
  - .github/CODEOWNERS
notes:
  - "v1.1 replaces an unmounted-repository proposal inventory with a current, exact nine-file lane index."
  - "The update records current file presence without upgrading any child document to adopted policy, validated control, rehearsed procedure, operational admission, release approval, or publication authority."
  - "The current lane contains naming, ownership, metadata, and doctrine-versus-runbook drift that requires file-specific follow-up; this change does not rename, delete, consolidate, or silently choose winners."
  - "The only verified GitHub review identity is @bartytime4life. CODEOWNERS routing is not proof of security stewardship, independent review, policy approval, or release authority."
  - "This one-file documentation update changes no secret, vulnerability channel, policy rule, infrastructure posture, route, runtime behavior, validator, test, workflow, receipt family, release decision, deployment, promotion, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/security/` — Security Guidance and Trust-Boundary Index

> **Human-readable security guidance for KFM's trust membrane, sensitive-data posture, exposure boundaries, negative tests, secrets, key lifecycle, audit invariants, and incident-response doctrine.** This lane explains what must be protected and how security concerns connect; it does not grant access, decide policy, prove enforcement, approve release, or publish anything.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-evidence-boundary)
[![Direct guidance files: 8](https://img.shields.io/badge/direct%20guidance%20files-8-0969da?style=flat-square)](#direct-child-map)
[![Posture: fail closed](https://img.shields.io/badge/posture-fail--closed-b42318?style=flat-square)](#security-operating-posture)
[![Disclosure: private first](https://img.shields.io/badge/disclosure-private%20first-b42318?style=flat-square)](../../SECURITY.md)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)
[![Evidence review: 2026-08-14](https://img.shields.io/badge/evidence%20review-2026--08--14-0969da?style=flat-square)](#last-evidence-review-and-rollback)

> [!IMPORTANT]
> **Security documentation is not a security decision.** A page, badge, checklist, threat table, test result, receipt, pull request, or merged commit cannot by itself create policy approval, source authority, evidence closure, access permission, operational admission, release state, or publication authority.

> [!CAUTION]
> **Do not disclose security-sensitive details publicly.** Use the private-first process in the repository-root [`SECURITY.md`](../../SECURITY.md). The exact operational private contact remains `NEEDS VERIFICATION`; never substitute a placeholder address, public issue, pull-request comment, screenshot, or log dump.

> [!WARNING]
> **KFM is not an emergency-alert or life-safety authority.** Security guidance protects the KFM system and its trust path. It must not be presented as public hazard response, emergency instruction, or authorization to act on real-world conditions.

**Quick navigation:** [Purpose](#purpose-and-inherited-authority) · [Authority](#authority-and-negative-authority) · [Status](#status-and-evidence-boundary) · [Map](#direct-child-map) · [Start here](#start-here) · [Inventory](#current-document-inventory) · [Posture](#security-operating-posture) · [Threats](#security-review-lenses) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Flow](#inputs-outputs-and-permitted-writers) · [Exposure](#exposure-sensitivity-and-public-safety) · [Storage](#mutability-retention-and-sensitive-working-material) · [Validation](#validation-and-negative-checks) · [Review](#ownership-review-and-escalation) · [Adjacent roots](#adjacent-responsibility-roots) · [Drift](#known-drift-and-conflicts) · [Backlog](#open-verification-backlog) · [Evidence](#evidence-basis-and-limitations) · [Rollback](#last-evidence-review-and-rollback)

---

## Purpose and inherited authority

`docs/security/` is the security-guidance lane inside KFM's human-readable [`docs/`](../README.md) responsibility root. It helps maintainers, reviewers, operators, researchers, and security reporters understand:

- which trust and exposure risks KFM is designed to refuse;
- how sensitive data, harmful precision, rights, consent, source role, and public delivery intersect;
- which documentation applies to threats, exposure, classification, deny tests, audit invariants, secrets, key rotation, and incident response;
- where enforceable rules, executable controls, evidence, receipts, proofs, release decisions, and operational procedures actually belong; and
- what remains draft, unverified, conflicted, or held.

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those rules list `docs/security/` as the direct `docs/` child for threat, incident, and exposure guidance. Under the adopted README profiles, this lane is a sensitive boundary and therefore uses the `BOUNDARY_COMPACT` contract.

This README inherits the `docs/` authority boundary. It does not create a security root, policy root, evidence store, incident system, release family, or operational secret store.

[Back to top](#top)

---

## Authority and negative authority

The lane is canonical **for human-readable security guidance and navigation only**. It is subordinate to the authority that owns each underlying decision or behavior.

| Concern | Owning authority | Role of `docs/security/` |
|---|---|---|
| Placement and documentation boundary | Accepted Directory Rules and the parent `docs/` contract | Explain the security-guidance lane and surface drift |
| Security object or interface meaning | `contracts/` | Cite semantics; do not redefine them |
| Machine-valid object shape | `schemas/` | Cite fields and versions; do not host schema authority |
| Allow, deny, hold, restrict, redact, or abstain | `policy/` plus governed review | Explain posture and expected outcomes |
| Runtime ingress, egress, authorization, and service behavior | Owning `apps/`, `runtime/`, `packages/`, and `infra/` surfaces | Name the boundary and required evidence; do not claim deployment |
| Tests, validators, scanners, and workflow gates | `tests/`, `tools/validators/`, and `.github/workflows/` | Explain expected proof and interpret bounded results |
| Evidence, receipts, proofs, and source identity | Governed `data/` accountability and registry families | Reference records; do not manufacture or approve them |
| Release, correction, withdrawal, and rollback | `release/` and linked accountability objects | Explain required handling; do not authorize it |
| Public vulnerability reporting | Repository-root [`SECURITY.md`](../../SECURITY.md) | Provide long-form context without inventing a contact |
| Operational incident procedure | [`docs/runbooks/`](../runbooks/README.md) | Provide security doctrine and hand off execution |
| This README | Human navigation and current-state disclosure | No access, policy, operational, release, or publication authority |

> [!IMPORTANT]
> **A missing security prerequisite is not permission.** Unresolved identity, rights, sensitivity, source role, evidence, policy, review, integrity, release state, correction path, rollback target, or private reporting channel remains `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or `NEEDS VERIFICATION` according to the owning contract.

[Back to top](#top)

---

## Status and evidence boundary

The observations below are pinned to `main@3abe21f9285ed7d2f9f652a2672d8f669aa7e884`. They describe tracked repository bytes, not deployed controls, operational readiness, incident rehearsal, secret custody, or security assurance.

| Surface | CONFIRMED observation | Bounded conclusion |
|---|---|---|
| This README | Prior blob `c4379f54f9f91b0d1d712cc3c569d2fe58a39f4a`; current text still describes an unmounted repository | Same-path v1.1 reconciliation is warranted |
| Direct lane inventory | Nine Markdown files: this README plus eight guidance documents; no direct child directories | The current navigation surface is exactly known at the pinned revision |
| Child maturity | Seven child documents still declare May 2026 draft/proposal-era metadata; `DENY_TESTS.md` has a later repository-grounded v1.1 update | File presence and useful guidance exist; lane-wide currency and operational admission do not |
| Threat and exposure guidance | `THREAT_MODEL.md` and `EXPOSURE_PLAN.md` exist | Their existence does not prove controls or public exposure posture are deployed |
| Incident guidance | Security doctrine and an operational runbook both exist in different lanes | Their boundary needs explicit reconciliation before consolidation or retirement |
| Disclosure entrypoint | Root `SECURITY.md` exists and requires private-first reporting | The actual private contact/channel remains `NEEDS VERIFICATION` |
| Review routing | CODEOWNERS defaults repository review to `@bartytime4life`; no separate `docs/security/` rule exists | One GitHub route is verified; qualified security stewardship and independent review are not |
| Deny-test implementation | `DENY_TESTS.md` reports five bounded structural/scaffold guards at its own pinned revision | Broader deny catalog and runtime/policy enforcement remain partial or proposed |
| Child identifiers and ownership | Several documents contain placeholder owners, IDs, paths, cadences, or no-mounted-repository language | Metadata cleanup requires file-specific evidence and should not be silently mass-edited |
| Runtime, infra, policy, signing, secret store, drills, incidents, releases, deployment, publication | Not established by this index | `UNKNOWN` unless proven by owning surfaces and exact-revision evidence |

### State separation

Do not collapse these independent states:

| Axis | Example |
|---|---|
| File presence | Markdown exists at a path |
| Documentation maturity | Draft, reconciled, stale, conflicted, superseded, or current at a pinned revision |
| Control implementation | Policy, runtime, infra, validator, workflow, or secret-store behavior exists |
| Negative-path proof | A named unsafe case is rejected with a stable reason |
| Operational rehearsal | An approved synthetic or restricted drill was executed and recorded |
| Review state | Authorized review is complete for a named scope |
| Operational admission | A control or procedure is approved for a named environment and actor class |
| Incident state | Detection, containment, correction, withdrawal, recovery, and closure are recorded |
| Release state | A specific immutable release is approved with correction and rollback support |
| Publication state | A public-safe carrier is actually exposed through governed delivery |

A green security-related check proves only its declared assertion and revision. It does not prove the whole security posture.

[Back to top](#top)

---

## Direct-child map

Directory Rules require this README to show only the directory it governs and its direct children.

```text
docs/security/
├── README.md                 # lane boundary, navigation, evidence limits, and backlog
├── AUDIT_INVARIANTS.md       # auditable trust and governance invariants
├── DATA_CLASSIFICATION.md    # sensitivity, audience tier, rights, and release crosswalk
├── DENY_TESTS.md             # negative-path doctrine, catalog, and bounded current guards
├── EXPOSURE_PLAN.md          # public, semi-public, internal, and restricted exposure posture
├── INCIDENT_RESPONSE.md      # security-incident doctrine and correction/rollback expectations
├── KEY_ROTATION.md           # cryptographic identity, custody, rotation, and revocation policy
├── SECRETS.md                # secret classes, storage boundaries, rotation, and leak handling
└── THREAT_MODEL.md           # threat families, guardrails, residual risks, and detection lenses
```

No direct child directory exists at the pinned revision. A future `assets/`, `drills/`, or other child is not current merely because an older proposal named it.

[Back to top](#top)

---

## Start here

| Need | Current entry point | Boundary |
|---|---|---|
| Report a vulnerability privately | Root [`SECURITY.md`](../../SECURITY.md) | Do not expose details publicly; exact contact remains unverified |
| Understand this lane | [`README.md`](./README.md) | Navigation and current-state disclosure only |
| Review threat families | [`THREAT_MODEL.md`](./THREAT_MODEL.md) | Threat guidance is not exploit evidence or risk acceptance |
| Review public exposure rules | [`EXPOSURE_PLAN.md`](./EXPOSURE_PLAN.md) | Exposure guidance is not deployed infra or policy proof |
| Classify sensitivity, audience, and rights | [`DATA_CLASSIFICATION.md`](./DATA_CLASSIFICATION.md) | Classification guidance does not make a release admissible |
| Review fail-closed test intent | [`DENY_TESTS.md`](./DENY_TESTS.md) | Five bounded guards do not prove complete deny coverage |
| Audit trust invariants | [`AUDIT_INVARIANTS.md`](./AUDIT_INVARIANTS.md) | Invariant catalog is not an audit result |
| Handle secrets | [`SECRETS.md`](./SECRETS.md) | Never commit secret values or invent a deployed secret store |
| Review key lifecycle | [`KEY_ROTATION.md`](./KEY_ROTATION.md) | Cadence, custody, and operational tooling require verification |
| Understand incident doctrine | [`INCIDENT_RESPONSE.md`](./INCIDENT_RESPONSE.md) | Doctrine and standard; not the operational command surface |
| Execute incident response | Runbook [`INCIDENT_RESPONSE.md`](../runbooks/INCIDENT_RESPONSE.md) | Restricted procedure; does not create life-safety authority |

[Back to top](#top)

---

## Current document inventory

The table records each current child document's declared state. It does not promote or approve any document.

| Document | Primary focus | Declared edition/state | Current evidence note |
|---|---|---|---|
| [`AUDIT_INVARIANTS.md`](./AUDIT_INVARIANTS.md) | Detectable trust, lifecycle, evidence, identity, AI, sensitivity, and release invariants | `v1`, `draft`, updated 2026-05-13 | Useful invariant catalog; owner and several implementation references remain placeholders |
| [`DATA_CLASSIFICATION.md`](./DATA_CLASSIFICATION.md) | Sensitivity 0–5, tiers T0–T4, rights, consent, transforms, release fields | `v0.1`, `draft`, updated 2026-05-13 | Consolidates vocabularies; ratification and current enforcement remain unproven |
| [`DENY_TESTS.md`](./DENY_TESTS.md) | Fail-closed doctrine, deny catalog, fixture vocabulary, and test-authoring guidance | `v1.1`, draft with five bounded guards confirmed, updated 2026-08-01 | Most repository-grounded child; explicitly says broader coverage remains proposed |
| [`EXPOSURE_PLAN.md`](./EXPOSURE_PLAN.md) | What may cross public, semi-public, internal, and restricted boundaries | `v1`, `draft`, updated 2026-05-13 | Current filename differs from the `EXPOSURE_POSTURE.md` name used by several siblings |
| [`INCIDENT_RESPONSE.md`](./INCIDENT_RESPONSE.md) | Security-incident doctrine, severity, containment, correction, withdrawal, rollback | `v0.1`, `draft`, updated 2026-05-13 | Must be distinguished from the operational runbook with the same basename |
| [`KEY_ROTATION.md`](./KEY_ROTATION.md) | Signing, KMS, pseudonymisation, secret, and identity rotation/revocation | `v1`, `draft`, updated 2026-05-13 | Metadata still has a replace-at-merge ID; cadences and ownership remain proposed |
| [`SECRETS.md`](./SECRETS.md) | Secret classes, allowed storage, OIDC-first posture, leak detection, rotation | `v0.1`, `draft`, updated 2026-05-13 | Doctrine is useful; actual store, owners, tools, and cadences remain unverified |
| [`THREAT_MODEL.md`](./THREAT_MODEL.md) | Threat families, security guardrails, forbidden public behaviors, residual risk | `v0.1`, `draft`, updated 2026-05-13 | Still describes current sibling paths and implementation as proposed |

### Reading rule

Treat a child document as:

- **guidance** when it explains doctrine or expected security behavior;
- **repository evidence** only for the exact tracked bytes and revision inspected;
- **implementation evidence** only when supported by owning code, configuration, tests, workflows, logs, or emitted artifacts;
- **operational evidence** only when tied to a named environment, actor, event, and immutable record; and
- **release evidence** only when the owning release and accountability objects support that conclusion.

[Back to top](#top)

---

## Security operating posture

This lane inherits KFM's broader trust posture and applies it under adversarial or failure conditions.

| Posture | Security meaning | Failure behavior |
|---|---|---|
| **Deny by default** | No public access, source activation, sensitive release, admin privilege, or trust transition exists without explicit admissibility | `DENY` or `HOLD` |
| **Least privilege** | People, apps, workers, connectors, workflows, and credentials receive only the capability required for a named task | Remove or narrow capability; escalate unexplained privilege |
| **Fail closed** | Missing evidence, policy, identity, integrity, rights, review, release, or rollback support cannot silently become allow | `ABSTAIN`, `DENY`, `ERROR`, or quarantine |
| **Private first** | Security-sensitive reports and reproduction details avoid public issues, comments, screenshots, and logs | Stop public disclosure; move to a verified private path |
| **Auditability** | Consequential security actions must leave bounded, reviewable process memory in the owning receipt, proof, incident, or release family | Treat missing records as an unresolved control gap |
| **Separation of duties** | Authoring, policy-significant review, release approval, incident command, and correction authority are not silently collapsed | Require the review appropriate to significance |
| **Reversibility** | Exposure, release, key, policy, and operational changes name correction, withdrawal, rollback, or forward-fix handling | Hold changes without a safe recovery path |
| **Cite or abstain** | Security claims about behavior or protection require current evidence | Mark `UNKNOWN` or `NEEDS VERIFICATION` rather than implying assurance |

These are operating constraints, not claims that every enforcement point is implemented.

[Back to top](#top)

---

## Security review lenses

Use the detailed child documents for analysis. This index supplies a bounded routing map.

| Review lens | Questions | Primary guidance |
|---|---|---|
| Trust-membrane bypass | Can a public or ordinary client reach RAW, WORK, QUARANTINE, canonical/internal stores, unpublished candidates, or direct model output? | [`THREAT_MODEL.md`](./THREAT_MODEL.md), [`EXPOSURE_PLAN.md`](./EXPOSURE_PLAN.md), [`DENY_TESTS.md`](./DENY_TESTS.md) |
| Sensitive data and harmful precision | Could exact location, identity linkage, inference, reconstruction, or metadata expose protected ecology, archaeology, infrastructure, living persons, DNA/genomics, land, or cultural material? | [`DATA_CLASSIFICATION.md`](./DATA_CLASSIFICATION.md), [`THREAT_MODEL.md`](./THREAT_MODEL.md) |
| Source and connector integrity | Can spoofing, mirror poisoning, schema drift, rights drift, stale status, or source-role collapse reach stronger lifecycle states? | [`THREAT_MODEL.md`](./THREAT_MODEL.md), [`AUDIT_INVARIANTS.md`](./AUDIT_INVARIANTS.md) |
| Policy and release bypass | Can an artifact be exposed without required policy, evidence, review, release, correction, or rollback support? | [`EXPOSURE_PLAN.md`](./EXPOSURE_PLAN.md), [`DENY_TESTS.md`](./DENY_TESTS.md), [`AUDIT_INVARIANTS.md`](./AUDIT_INVARIANTS.md) |
| Secrets and signing identities | Are secrets excluded from Git, clients, logs, fixtures, receipts, screenshots, and generated artifacts? Are custody and rotation bounded? | [`SECRETS.md`](./SECRETS.md), [`KEY_ROTATION.md`](./KEY_ROTATION.md) |
| CI and supply chain | Are dependencies, workflows, identities, artifacts, receipts, and signatures pinned and verifiable for the asserted scope? | [`THREAT_MODEL.md`](./THREAT_MODEL.md), [`KEY_ROTATION.md`](./KEY_ROTATION.md) |
| Governed AI | Can prompt injection, retrieval poisoning, direct model access, uncited generation, prompt leakage, or unsupported map action bypass evidence and policy? | [`THREAT_MODEL.md`](./THREAT_MODEL.md), architecture and policy owners |
| Telemetry and logs | Can prompts, raw evidence, restricted coordinates, secrets, or sensitive reasons leak through observability? | [`EXPOSURE_PLAN.md`](./EXPOSURE_PLAN.md), [`SECRETS.md`](./SECRETS.md) |
| Incident and correction | Can the system contain exposure, preserve evidence, correct or withdraw affected releases, invalidate caches, and restore a safe state? | [`INCIDENT_RESPONSE.md`](./INCIDENT_RESPONSE.md), runbook [`INCIDENT_RESPONSE.md`](../runbooks/INCIDENT_RESPONSE.md) |
| Admin and reviewer paths | Can a restricted convenience surface become the normal public path or silently combine author, approver, publisher, and incident roles? | [`THREAT_MODEL.md`](./THREAT_MODEL.md), [`AUDIT_INVARIANTS.md`](./AUDIT_INVARIANTS.md) |

[Back to top](#top)

---

## What belongs here

Content belongs in `docs/security/` when its primary responsibility is **human-readable security guidance** and it does not take over an enforcement, evidence, operational, or release authority.

Appropriate content includes:

- threat models and residual-risk registers that avoid live exploit details;
- public, semi-public, internal, and restricted exposure guidance;
- sensitivity, rights, consent, precision, and classification crosswalks;
- deny-test doctrine and interpretation of bounded negative-path evidence;
- auditable invariant catalogs;
- secret-handling and cryptographic-identity guidance;
- incident-response doctrine, severity semantics, correction expectations, and handoff boundaries;
- redacted, approved learning material after an incident when publication is safe; and
- navigation between root disclosure policy, runbooks, policy, implementation, evidence, and release surfaces.

A security document should identify its scope, evidence revision, owner or unresolved owner, sensitivity, non-effects, validation, correction path, and review trigger.

[Back to top](#top)

---

## What does not belong here

> [!WARNING]
> **Do not use a public documentation lane as a vulnerability workbench, secret store, policy engine, or incident command system.**

The following do not belong here as canonical writable authority:

| Artifact or responsibility | Owning family |
|---|---|
| Real secrets, private keys, tokens, credentials, signed URLs, secret-store handles that create access, or production configuration values | External secret store and owning runtime/infra process; never public docs |
| Unfixed exploit payloads, weaponized reproduction steps, exact internal topology, private logs, active triage transcripts, or unredacted incident evidence | Restricted incident and security handling selected by the authorized owner |
| Enforceable allow/deny/redaction/access/release rules | `policy/` |
| Machine schemas and semantic contracts | `schemas/` and `contracts/` |
| Firewalls, reverse proxies, VPNs, identity providers, host hardening, deployment manifests, or network policy | `infra/` and owning deployment surfaces |
| Runtime authorization, public routes, model adapters, or application logic | Owning `apps/`, `runtime/`, and `packages/` |
| Validators, scanners, test implementations, and workflow source | `tools/validators/`, `tests/`, and `.github/workflows/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, or PUBLISHED instances | Governed `data/` lanes |
| Receipts, proofs, source-registry instances, review records, or evidence bundles | Their governed `data/` accountability and identity families |
| Release manifests, promotion decisions, correction notices, withdrawal notices, rollback cards, or signing outputs | `release/` and linked accountability families |
| Operational incident command, live response coordination, or public emergency guidance | Authorized private incident process and `docs/runbooks/`; KFM is not a life-safety authority |
| Placeholder reporting addresses presented as operational | Nowhere; keep the channel `NEEDS VERIFICATION` until configured |

Public documentation may explain that a protected control or denial exists without revealing the payload, secret, exact coordinate, exploit path, or sensitive reason that would defeat the control.

[Back to top](#top)

---

## Inputs, outputs, and permitted writers

### Inputs

Security guidance may consume:

- accepted doctrine and ADRs;
- exact repository code, configuration, policy, tests, workflows, manifests, and generated artifacts;
- current threat, incident, drill, correction, withdrawal, and rollback evidence when access and sensitivity permit;
- official standards or maintainer guidance when a current external fact is required;
- redacted findings from reviews, incidents, and security testing; and
- open drift and verification records.

An input does not gain authority merely because a security document cites it.

### Outputs

This lane produces human guidance, indexes, threat and exposure models, classification references, negative-test catalogs, secret/key guidance, incident doctrine, review checklists, and redacted learning artifacts. It does not emit policy decisions, executable controls, evidence, receipts, proofs, releases, or public data.

### Permitted writers

Normal writers are reviewed repository changes made on feature branches by maintainers or authorized automation. Writers must:

1. keep sensitive working material out of public Git history;
2. preserve stable document identity and current truth labels;
3. cite exact repository evidence for implementation claims;
4. avoid copying secrets, private reports, or active incident details into generated prompts or receipts;
5. update affected guidance when a material security behavior changes; and
6. stop at reviewable repository state unless a separate authority governs a later operational or release transition.

AI-assisted security documentation remains interpretive and review-pending. Its generated receipt, prose, or pull request is not human approval.

[Back to top](#top)

---

## Exposure, sensitivity, and public safety

`docs/security/` is repository-facing and may be publicly readable. Treat every committed byte, filename, link target, example, image, table, diagram, commit message, pull-request body, and generated receipt as potentially public.

### Public-safe content

Appropriate public content can include:

- high-level threat families and defensive expectations;
- private-first disclosure instructions without unverified contact details;
- denial and redaction principles;
- synthetic examples that cannot reconstruct protected data;
- bounded test and validation descriptions;
- public-safe correction and rollback guidance; and
- clear evidence limitations.

### Content requiring restriction, redaction, or abstention

Prefer restricted handling, redaction, generalization, delayed publication, or denial for:

- active vulnerabilities and exploit chains;
- credentials, secrets, internal endpoints, or signer/private-key material;
- exact sensitive locations or reconstruction clues;
- living-person, DNA/genomic, genealogy, private-land, or consent-sensitive data;
- cultural, tribal, sacred, burial, archaeology, or sovereignty-sensitive material;
- critical infrastructure or operationally sensitive facility detail;
- source-restricted content and private reports;
- unredacted telemetry, logs, prompts, evidence payloads, or incident artifacts; and
- security reasons whose disclosure would reveal the protected fact.

When the correct classification is unclear, do not publish the detail merely to make documentation complete.

[Back to top](#top)

---

## Mutability, retention, and sensitive working material

| Property | Rule |
|---|---|
| Physical storage | Reviewed Git content for public-safe guidance; restricted operational evidence stays in its authorized system |
| Mutability | Versioned replacement with Git history; append-only chronology where an incident or decision record requires it |
| Stable identity | Preserve `doc_id`, path identity, anchors, and explicit supersession unless a reviewed migration says otherwise |
| Generated content | Edit the canonical source and regenerate; never hand-edit a verified mirror |
| Active vulnerability material | Keep out of public Git until remediated and approved for disclosure |
| Incident evidence | Preserve according to incident, privacy, legal, rights, and retention authority; public docs receive only approved redacted derivatives |
| Secret exposure | Revoke/rotate first, preserve minimal evidence safely, then correct public history through the authorized response |
| Deletion | Requires identity, inbound-reference, sensitivity, retention, correction, and rollback review |
| Documentation correction | Correct inaccurate guidance in place, retain decision lineage, and update the generated receipt for AI-authored changes |

A Git revert can reverse public documentation bytes. It cannot un-disclose a secret, exact location, or exploit detail already copied elsewhere. Sensitive-content prevention therefore outranks later cleanup.

[Back to top](#top)

---

## Validation and negative checks

Documentation validation proves only the asserted document properties. Security assurance requires evidence from the owning implementation and operational surfaces.

### Documentation checks for this lane

- one valid `KFM_META_BLOCK_V2` and one H1;
- exact direct-child map and working local links;
- stable top anchor and resolvable internal fragments;
- no stale unmounted-repository claims presented as current;
- no invented owner, private contact, secret store, incident record, deployment, policy approval, drill, or release;
- no secret-like values, private keys, raw credentials, exact protected coordinates, live exploit payloads, or unredacted incident details;
- explicit separation among guidance, policy, implementation, tests, evidence, runbooks, and release authority;
- public-safe language and final newline; and
- generated-receipt shape and artifact digest integrity for AI-authored changes.

### Security evidence checks by owning surface

| Assertion | Minimum evidence before claiming it |
|---|---|
| “Public clients cannot reach internal stores” | Route/import scans plus representative negative tests at an exact revision |
| “A policy denies this case” | Current policy source, matching input, decision output, and test |
| “Secrets are not committed” | Current scanner/configuration evidence and bounded repository scan; not prose alone |
| “A workflow is supply-chain hardened” | Exact workflow, pinned dependencies/actions, permissions, identity constraints, and hosted result |
| “A release is signed and verifiable” | Immutable artifact, digest, signature/attestation, verifier result, identity, and release record |
| “Incident response is operational” | Named owners/channels, approved procedure, rehearsal or incident record, and correction/rollback evidence |
| “Deny coverage is complete” | Enumerated threat/requirement matrix with positive and negative coverage; five bounded guards are not completion |
| “Data classification is enforced” | Contract/schema fields, policy decisions, lifecycle propagation, fixtures, tests, and public-render checks |

### Applicable repository-native checks

At the time this change is proposed, relevant hosted checks include documentation metadata, document graph, stale scan, links, docs build, security scanning, validator-suite, deny-test, policy-test, telemetry-policy, release dry-run, and changed-area controls. Their conclusions must be read at the exact head; an inherited failure stays visible and is not relabeled success.

```bash
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<receipt>.json \
  --repo-root .

git diff --check
```

The commands above are repository entry points to verify in a mounted checkout. Listing them here is not a claim that they ran in this authoring session.

[Back to top](#top)

---

## Ownership, review, and escalation

### Verified routing

Current CODEOWNERS evidence establishes one GitHub review route: `@bartytime4life`. It does not establish professional qualifications, independent review, incident command, security authority, policy authority, release authority, or separation of duties.

### Review burden

| Change | Minimum review posture |
|---|---|
| Typo, link, or bounded factual correction | Documentation review |
| Inventory, evidence snapshot, or maturity classification | Documentation review plus source verification |
| Threat family, sensitive category, disclosure posture, or security outcome vocabulary | Security and affected policy/domain review |
| Reporting channel or vulnerability handling | Verified security/repository owner; root `SECURITY.md` must remain synchronized |
| Secret/key custody or rotation guidance | Security, infra/runtime, and release/signing owners |
| Incident severity, containment, correction, withdrawal, or rollback doctrine | Security, operations/runbook, policy, and release owners |
| Normal public-path, access, policy, lifecycle, or release-boundary change | Accepted ADR or other governing decision plus implementation evidence |
| Policy-significant release or sensitive-data exception | Review appropriate to consequence; independent review when required |

### Escalation

Escalate rather than improvise when:

- a vulnerability report lacks a verified private channel;
- a document contains a real secret, exact protected location, or active exploit detail;
- docs and implementation disagree about an exposure boundary;
- policy, source rights, sensitivity, identity, or release state is unclear;
- a public path appears to bypass the governed API or released artifacts;
- an incident requires correction, withdrawal, cache invalidation, or rollback; or
- one person or automation path is implicitly acting as author, approver, publisher, and incident authority.

[Back to top](#top)

---

## Adjacent responsibility roots

| Surface | Relationship to this lane |
|---|---|
| [`docs/doctrine/`](../doctrine/) | Stable trust and lifecycle law that security guidance must not contradict |
| [`docs/adr/`](../adr/) | Accepted decisions that alter security architecture, exposure, or placement |
| [`docs/runbooks/`](../runbooks/README.md) | Human-executable operational procedures, including incident response |
| Root [`SECURITY.md`](../../SECURITY.md) | Public vulnerability-disclosure front door |
| [`.github/CODEOWNERS`](../../.github/CODEOWNERS) | GitHub review routing, not proof of review or authority |
| [`policy/`](../../policy/README.md) | Enforceable admissibility and finite security decisions |
| [`infra/`](../../infra/README.md) | Deployment, exposure, network, identity, and hardening implementation |
| [`apps/governed-api/`](../../apps/governed-api/) | Normal executable public trust path when current implementation supports it |
| `runtime/` and `packages/` | Provider/adaptor composition and reusable trust logic |
| `tests/`, `fixtures/`, and `tools/validators/` | Positive/negative enforcement evidence and reusable validation |
| [`data/`](../../data/README.md) | Lifecycle, registry, receipt, proof, and published instance families |
| [`release/`](../../release/README.md) | Release, correction, withdrawal, rollback, and signing decision plane |
| `artifacts/qa/` or hosted CI storage | Rebuildable scan/report output only; not security truth or release proof |

A reference from this README does not activate, adopt, or validate the adjacent surface.

[Back to top](#top)

---

## Known drift and conflicts

These findings are current documentation work, not permission for an unreviewed rename or deletion.

| Finding | Status | Smallest governed disposition |
|---|---|---|
| Current README proposes lowercase files and directories that do not match the actual uppercase nine-file lane | **CONFIRMED stale** | Replace the index with the exact direct-child map; do not create proposal paths |
| Actual file is `EXPOSURE_PLAN.md`, while several child metadata blocks and links name `EXPOSURE_POSTURE.md` | **CONFIRMED naming conflict** | Inventory all consumers, choose identity through file-specific review, then repair links or migrate with rollback |
| `docs/security/INCIDENT_RESPONSE.md` and `docs/runbooks/INCIDENT_RESPONSE.md` share a basename and overlapping language | **CONFIRMED scope overlap** | Define doctrine/standard versus procedure boundaries before consolidation, rename, or retirement |
| Most child docs still say their own current path or siblings are proposed/unverified | **CONFIRMED stale evidence language** | Reconcile each file against current repository evidence without upgrading behavior |
| Placeholder owner roles remain across the lane; CODEOWNERS only verifies `@bartytime4life` | **CONFIRMED ownership gap** | Record accountable assignments through the owning governance process; do not invent teams |
| `KEY_ROTATION.md` retains a replace-at-merge document ID and proposed cadences | **CONFIRMED metadata/decision gap** | Recover stable identity and ratify or narrow cadence claims before operational use |
| Root `SECURITY.md` requires private-first reporting but has no verified operational contact | **CONFIRMED P0 gap** | Configure and verify a private channel, then synchronize both surfaces |
| Child docs name policies, standards, runbooks, signatures, stores, and tools not proven current in this review | **NEEDS VERIFICATION** | Verify exact paths and implementation before converting prose to current fact |
| Broad security controls, negative tests, drills, incident automation, signing, and release integrity are not proven by this lane | **UNKNOWN** | Inspect owning code/config/tests/workflows/artifacts and record bounded results |

### Safe cleanup sequence

1. Freeze the current lane, inbound references, child identities, and exact digests.
2. Classify each conflict as stale prose, broken link, alias, overlap, missing authority, or implementation gap.
3. Decide identity and ownership before any move or rename.
4. Repair references and add negative guards before retiring an old name.
5. Validate documentation, policy, implementation, fixtures, tests, workflows, incident/release consumers, and rollback.
6. Prove zero writers and zero consumers before deletion.
7. Preserve correction and supersession history.

[Back to top](#top)

---

## Open verification backlog

### P0 — reporting, authority, and unsafe exposure

1. **NEEDS VERIFICATION — private vulnerability channel.** Configure and test at least one private reporting path, then update root `SECURITY.md` and relevant security guidance together.
2. **NEEDS VERIFICATION — accountable roles.** Identify security, policy, incident, infra/runtime, release, correction, and independent-review owners without treating CODEOWNERS routing as proof.
3. **NEEDS VERIFICATION — trust-membrane implementation.** Reconcile public routes, internal-store denial, direct-model denial, authn/authz, admin boundaries, and error behavior at a pinned revision.
4. **NEEDS VERIFICATION — sensitive-data enforcement.** Verify classification fields, deny-by-default policy, transforms, reason exposure, and public-render tests for every high-risk domain.
5. **NEEDS VERIFICATION — secrets and signing.** Inventory actual secret stores, credential paths, workflow identities, key custody, signatures, rotation/revocation, leak scanning, and recovery.

### P1 — documentation and operational closure

6. **CONFIRMED conflict — exposure identity.** Resolve `EXPOSURE_PLAN.md` versus `EXPOSURE_POSTURE.md` through a reference inventory and reversible identity decision.
7. **CONFIRMED overlap — incident surfaces.** Define the relationship among root disclosure policy, security incident doctrine, and operational incident runbook.
8. **NEEDS VERIFICATION — child metadata.** Reconcile placeholder IDs, owners, dates, paths, versions, review claims, and no-mounted-repository language in seven older child documents.
9. **NEEDS VERIFICATION — deny coverage.** Crosswalk threats and security requirements to implemented policy, validator, fixture, test, workflow, telemetry, and release checks; keep uncovered cases explicit.
10. **NEEDS VERIFICATION — drills and evidence.** Determine which incident, secret-leak, key-rotation, rollback, withdrawal, and correction drills have approved, exact-version records.

### P2 — maturity and maintainability

11. **PROPOSED — security documentation registry.** Consider a machine-readable current-document map only after consumers, schema, authority, generation, and correction ownership are defined.
12. **PROPOSED — metadata and link convergence.** Repair stale sibling names and cross-root references in dependency-closed batches rather than one broad search-and-replace.
13. **NEEDS VERIFICATION — retention and disclosure.** Define public, internal, restricted, and incident-evidence retention, redaction, legal/rights review, and approved postmortem publication.
14. **UNKNOWN — operational admission.** Determine which security controls and procedures, if any, are approved for real environments and actor classes rather than merely tracked.

[Back to top](#top)

---

## Evidence basis and limitations

| Evidence | Use in this edition | Limitation |
|---|---|---|
| `main@3abe21f9285ed7d2f9f652a2672d8f669aa7e884` | Pins target, lane inventory, child docs, disclosure entrypoint, Directory Rules, ADR, CODEOWNERS, and adjacent current paths | Commit bytes do not prove deployed controls or operational security |
| Exact `docs/security/` contents response | Confirms nine direct Markdown files and no direct child directory | Presence does not prove quality, enforcement, use, or approval |
| Complete prior README | Identifies stale proposal tree, placeholder owners, unmounted-repository claims, and intended lane scope | Prior prose is not current implementation evidence |
| Eight child documents | Supports bounded focus, version, status, date, and drift findings | Not a complete line-by-line audit of every child |
| Root `SECURITY.md` | Confirms private-first public disclosure posture and the unverified contact gap | Does not prove GitHub private reporting is enabled or monitored |
| Operational incident runbook | Confirms a separate runbook surface | Does not prove rehearsal, staffing, or current procedure validity |
| Accepted ADR-0029 and adopted Directory Rules | Establish placement, README profile, direct-child map, compatibility, migration, and rollback rules | Do not validate security behavior |
| Current CODEOWNERS | Establishes `@bartytime4life` as the sole verified GitHub review route | Does not establish review completion, qualification, independence, or security/release authority |
| Generated-receipt schema and validator | Establish current authoring-provenance shape and offline digest check | A valid receipt is process memory, not approval or security proof |

### Assumptions deliberately not made

This edition does not assume:

- the repository has a verified private vulnerability contact;
- GitHub private vulnerability reporting is enabled or monitored;
- a draft child document is adopted policy;
- a named security control is implemented because documentation describes it;
- five structural deny guards equal complete fail-closed coverage;
- an incident or key-rotation drill has occurred;
- a secret store, signer, KMS, OIDC trust, SBOM, SLSA, Sigstore, DSSE, or Rekor integration is operational;
- public routes, direct-model denial, or internal-store guards are complete;
- a green workflow proves security, policy, release, or publication;
- CODEOWNERS proves qualified or independent review;
- a generated receipt proves truth, security, human approval, or release readiness; or
- reverting Markdown reverses a real-world disclosure.

[Back to top](#top)

---

## Last evidence review and rollback

**2026-08-14** — v1.1 same-path repository-grounded reconciliation against `main@3abe21f9285ed7d2f9f652a2672d8f669aa7e884`.

Re-review this README when:

- a direct child is added, moved, renamed, superseded, or retired;
- the private vulnerability channel or root `SECURITY.md` changes;
- CODEOWNERS or accountable security/release/incident assignments change;
- accepted doctrine, an ADR, or policy changes security placement or outcomes;
- public routes, model access, admin access, secrets, signing, telemetry, or exposure posture changes;
- a security incident, correction, withdrawal, rollback, or disclosure reveals a guidance gap;
- deny-test or security-validation coverage changes materially; or
- an evidence-review maximum interval selected by the owning security governance arrives.

| Edition | Date | Change | Effect |
|---|---|---|---|
| **v1.1** | 2026-08-14 | Replaced proposal-only/unmounted-repository framing with the exact lane inventory, current entrypoint map, authority separation, maturity states, risk-based guidance, drift register, verification backlog, evidence limits, and rollback. | Documentation only; no security control or operational state change |
| **v1** | 2026-05-10 | Long-form security-lane proposal, future tree, posture guidance, and README contract. | Historical documentation state |
| **Initial path** | 2026-05-08 | Earliest path history returned for `docs/security/README.md`. | Origin details beyond path history remain bounded |

### Documentation rollback

Restore the prior file blob:

```text
path: docs/security/README.md
prior_blob: c4379f54f9f91b0d1d712cc3c569d2fe58a39f4a
```

or revert the focused content commit created by this change. That restores the v1 documentation snapshot. It does not revoke credentials, close a vulnerability, contain an incident, reverse a disclosure, alter policy, restore a deployment, invalidate a release, roll back data, or change repository settings.

[Back to top](#top)
