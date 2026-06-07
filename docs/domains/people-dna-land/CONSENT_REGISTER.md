<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/people-dna-land/consent-register
title: Consent Register — People / Genealogy / DNA / Land Domain
type: standard
version: v0.1
status: draft
owners: <people-dna-land domain steward — TODO via CODEOWNERS>, <privacy / consent steward — TODO>, <data steward — TODO>
created: 2026-06-06
updated: 2026-06-06
policy_label: restricted
related:
  # NEEDS VERIFICATION — repo paths PROPOSED until checked against a mounted repo
  - docs/domains/people-dna-land/CONSENT_MODEL.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/CANONICAL_PATHS.md
  - directory-rules.md
  - ai-build-operating-contract.md
tags: [kfm, domain, people-dna-land, consent, register, revocation, dna, living-person]
notes:
  # CONTRACT_VERSION = "3.0.0"
  # This is the operational REGISTER (the tracked list of consent grants + state). The doctrine/machinery is in CONSENT_MODEL.md.
  # HARD RULE: the register stores pointers, pseudonyms, status-list indices, DUO codes, and DSSE digests — NEVER raw PII, raw tokens (fingerprints only), or genotype data.
  # The register is NOT a publication permission: presence of a consent entry never publishes data (keystone rule, CONSENT_MODEL.md §2).
  # Register placement (data/registry/ vs control_plane/ vs policy/consent/) is an open ADR.
[/KFM_META_BLOCK_V2] -->

# Consent Register — People / Genealogy / DNA / Land Domain

> The **operational index** of consent grants KFM holds for living-person and DNA-derived material: each entry’s scope, status, retention, and revocation pointer. The register tracks **state**, not data — it stores pseudonyms, status-list pointers, DUO codes, and digests, **never** raw PII, raw tokens, or genotype. The *doctrine* of how consent works lives in [`CONSENT_MODEL.md`](./CONSENT_MODEL.md); this is the *ledger* that operationalizes it.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![doc type: register](https://img.shields.io/badge/doc%20type-operational%20register-blue)
![domain: people–dna–land](https://img.shields.io/badge/domain-people--dna--land-7a52a7)
![rule: pointers%20not%20PII](https://img.shields.io/badge/rule-pointers%20not%20PII-b30000)
![rule: presence%20%E2%89%A0%20permission](https://img.shields.io/badge/rule-presence%20%E2%89%A0%20permission-b30000)
![implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-9c6ade)
![CONTRACT_VERSION 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)

**Status:** `draft` · **Owners:** *privacy/consent steward; people-dna-land steward; data steward — TODO* · **Last updated:** *2026-06-06* · **`CONTRACT_VERSION = "3.0.0"`**

> [!IMPORTANT]
> **The register stores pointers, not payloads.** A consent-register entry holds a subject **pseudonym**, a consent **scope** (GA4GH DUO codes), a **status-list pointer** (URI + index), a **retention** bound, and the **digests** of the consent receipt / sidecar — and nothing else. It **never** stores a person’s name, a raw access token (only a token *fingerprint*), a DNA kit/vendor ID, or genotype data. The register is itself one of the most sensitive artifacts in the system; treat it `restricted`, deny-by-default.

> [!WARNING]
> **A register entry is not a publication permission.** Presence of a consent grant in this register never publishes anything (the keystone rule, `CONSENT_MODEL.md` §2). It records that a holder authorized a scoped use; publication still requires independent evidence closure, a `ReleaseManifest`, and promotion review. Implementation of the register and its schema is **PROPOSED** / `NEEDS VERIFICATION` against a mounted repo.

-----

## Contents

- [1. What this register is](#1-what-this-register-is)
- [2. Register vs model](#2-register-vs-model)
- [3. What an entry holds](#3-what-an-entry-holds)
- [4. The no-raw-data rule](#4-the-no-raw-data-rule)
- [5. Entry statuses](#5-entry-statuses)
- [6. Operating procedure](#6-operating-procedure)
- [7. Consent scope vocabulary (GA4GH DUO)](#7-consent-scope-vocabulary-ga4gh-duo)
- [8. Where the register lives](#8-where-the-register-lives)
- [9. Audit and the risk it guards](#9-audit-and-the-risk-it-guards)
- [10. Governed AI behavior](#10-governed-ai-behavior)
- [11. Validators and fixtures](#11-validators-and-fixtures)
- [12. Open questions](#12-open-questions)
- [13. Related docs](#13-related-docs)

-----

## 1. What this register is

**PROPOSED implementation / CONFIRMED pattern.** The consent register is the tracked list of `ConsentGrant`s KFM currently holds, each with its live state. It exists so that:

- A render gate can resolve “is there a valid, in-scope, non-revoked, unexpired consent for this subject?” deterministically and on every request.
- A steward can audit, at any time, **which** consents exist, **what** each authorizes, and **what state** each is in — without touching raw PII.
- Revocation has a single authoritative place to flip state, propagating to tombstones and cache invalidation.

It follows the KFM **register pattern** (CONFIRMED — e.g., the source-descriptor / source-authority register, KFM-P1-PROG-0007): a register records *descriptors and pointers*; the heavy objects (the signed receipt, the credential, the status list) live in their own content-addressed stores and are referenced by digest.

[Back to top](#contents)

-----

## 2. Register vs model

These are two distinct docs and must not be merged:

|         |`CONSENT_MODEL.md`                                                                       |`CONSENT_REGISTER.md` (this doc)                                 |
|---------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------|
|Answers  |*How does consent work?*                                                                 |*Which consents do we hold, in what state?*                      |
|Contains |Keystone rule, object shapes, the render gate, lifecycle, VC formats, revocation doctrine|The entry schema, statuses, operating procedure, audit, placement|
|Analogue |Schema / contract                                                                        |Registry / ledger                                                |
|Authority|Doctrine                                                                                 |Operational record                                               |

The register **operationalizes** the model; the model **governs** the register. Each links the other.

[Back to top](#contents)

-----

## 3. What an entry holds

PROPOSED entry shape; field names illustrative. Every field is a **pointer, pseudonym, code, or digest** — no raw identifiers (§4).

|Field                      |Holds                                                                                                          |Never holds                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------|
|`consent_entry_id`         |Opaque register key                                                                                            |—                                         |
|`subject_pseudonym`        |Stable pseudonymous handle for the data subject                                                                |The person’s name or any direct identifier|
|`consent_sidecar_ref`      |Digest / URI of the `ConsentSidecar` (content-addressed)                                                       |The sidecar’s raw contents inline         |
|`receipt_digest`           |DSSE consent-receipt envelope digest                                                                           |The holder’s raw credential               |
|`scope`                    |Render scope (`public_render` / `generalize_render` / `restricted_render` / `review_required`) + DUO codes (§7)|Free-text PII                             |
|`obligations_ref`          |Pointer to the sidecar’s `obligations[]` (source of truth)                                                     |—                                         |
|`status`                   |Current state (§5)                                                                                             |—                                         |
|`status_list`              |`{status_list_uri, status_list_index, status_purpose}`                                                         |—                                         |
|`retention`                |`{policy, expires_at}`                                                                                         |—                                         |
|`upstream`                 |Upstream provenance: source family + **access-token fingerprint** + GA4GH Passport claim fingerprint           |The raw access token or Passport          |
|`bound_objects_ref`        |Pointers to the People/DNA/Land objects this consent scopes (by opaque id)                                     |Raw object payloads                       |
|`created_at` / `updated_at`|ISO 8601 timestamps                                                                                            |—                                         |
|`last_audit`               |Pointer to the most recent audit `ReviewRecord`                                                                |—                                         |


> [!NOTE]
> `bound_objects_ref` links a consent to the assertions/segments it authorizes **by opaque id only**, so the register can answer “what does revoking this consent invalidate?” without ever joining to raw person or DNA data. The join itself is a sensitive operation gated by policy.

[Back to top](#contents)

-----

## 4. The no-raw-data rule

CONFIRMED doctrine, drawn directly from the corpus’s consent-handling rules:

- **Token fingerprints, not tokens.** KFM records the *access-token fingerprint*, never the token itself (C9-02). The register stores the fingerprint in `upstream`.
- **Pseudonyms, not names.** Consent binds to a subject pseudonym (ConsentSidecar shape); the register never stores the person’s name or a direct identifier.
- **No genotype, ever.** Raw DTC genotype data is never republished and never enters the register; only the consent *state* over derived data is tracked (C9-03).
- **No kit/vendor IDs.** Raw DNA kit/vendor identifiers are not logged or exposed; the register references a `DNAKitToken` (opaque) at most.
- **Digests, not payloads.** The consent receipt and credential live in content-addressed stores; the register holds their digests.

> [!CAUTION]
> **The register is a re-identification surface if it leaks.** A list that maps pseudonyms to scopes and bound-object pointers is exactly the kind of artifact the risk register flags: *“living-person data exposed via inference (aggregate + context join)”* is a **High** risk (Atlas §24.10). The register MUST be `restricted`, access-controlled, and excluded from any public surface, any graph projection, and any AI context window. It is internal-only.

[Back to top](#contents)

-----

## 5. Entry statuses

PROPOSED status set, aligned to the render-gate checks and the W3C Bitstring Status List purposes.

|Status          |Meaning                                                                      |Render-gate effect                           |
|----------------|-----------------------------------------------------------------------------|---------------------------------------------|
|`active`        |Valid, in-scope, non-revoked, within retention                               |May `ALLOW` (if evidence + release also pass)|
|`suspended`     |Status-list bit flipped, `suspension` purpose (temporary, reversible)        |`DENY` until cleared                         |
|`revoked`       |Status-list bit flipped, `revocation` purpose (final, irreversible)          |`DENY` + tombstone + cache invalidation      |
|`expired`       |`now ≥ retention.expires_at`                                                 |`DENY`; re-consent required                  |
|`pending_review`|Awaiting steward decision (scope ambiguous, multi-party, or death-of-subject)|`DENY` / `ABSTAIN` while held                |
|`error`         |Receipt/sidecar fails to resolve or verify                                   |`ABSTAIN` / `ERROR`; never silent allow      |


> [!NOTE]
> `pending_review` is where the corpus’s genuine open cases land: a multi-party consent with one stakeholder unaccounted for, or a subject who has died and whose consent is now ambiguous. The register holds these **closed** (no render) until a steward resolves them — it never defaults them open.

[Back to top](#contents)

-----

## 6. Operating procedure

PROPOSED; the lifecycle gates are CONFIRMED doctrine.

|Operation     |Steps                                                                                                                                                                      |Receipts emitted                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
|**Add**       |Verify the DSSE receipt; record pseudonym, scope/DUO, status-list pointer, retention, upstream fingerprints; bind objects by opaque id; status `active`.                   |Register entry + ingest receipt                |
|**Suspend**   |Flip status-list bit (`suspension`); set status `suspended`.                                                                                                               |`ReviewRecord` (if steward-initiated)          |
|**Revoke**    |Flip status-list bit (`revocation`); set status `revoked`; emit `RevocationReceipt`; issue tombstone; trigger cache invalidation across bound objects; append ledger entry.|`RevocationReceipt` + tombstone + `run_receipt`|
|**Expire**    |On `now ≥ expires_at`, set status `expired`; deny future renders.                                                                                                          |(automatic) audit note                         |
|**Re-consent**|New `ConsentGrant` → new entry; old entry retained for lineage, not reactivated.                                                                                           |New register entry                             |
|**Audit**     |Periodic steward review of all entries; check for aged-out reviews, rights-status changes, orphaned bound-object pointers.                                                 |`ReviewRecord` per audit                       |


> [!IMPORTANT]
> **Revocation must cascade.** When an entry moves to `revoked`, every object in its `bound_objects_ref` must have its public derivatives invalidated within the published-cache TTL — the same cascade `CONSENT_MODEL.md` §6 describes. A revocation that updates the register but leaves stale tiles live is incomplete and is a finding at audit.

[Back to top](#contents)

-----

## 7. Consent scope vocabulary (GA4GH DUO)

CONFIRMED doctrine (Pass-10 C9-04): GA4GH AAI / Passports / **Data Use Ontology (DUO)** / MRCG is the canonical access-control and consent framework KFM adopts for human-subject data. The register stores consent scope as **DUO codes**, not free text, so the policy engine can act on them.

- Every consent entry carries DUO codes (e.g., research-only, no-commercial, IRB-required); the policy-as-code layer reads them and gates publication accordingly.
- Non-GA4GH consent inputs (e.g., a free-text oral-history release) are **normalized upward** into DUO codes via a documented mapping before they enter the register — the corpus warns the system must tolerate non-GA4GH inputs while normalizing them.
- The `upstream.passport_fingerprint` records the GA4GH Passport claim used at fetch time (fingerprint only).

> [!NOTE]
> DUO version handling in long-running grants is an open question (how a DUO version update affects an already-recorded consent). Pin the DUO version in the entry and reconcile on audit; flagged OQ-CREG-05.

[Back to top](#contents)

-----

## 8. Where the register lives

PROPOSED placement; genuinely open (shares the consent-lane conflict from `CANONICAL_PATHS.md` §9.3 / VB-PDL-04).

|Candidate home                           |Argument                                                                                        |Status  |
|-----------------------------------------|------------------------------------------------------------------------------------------------|--------|
|`data/registry/consent/people-dna-land/` |Registers are a `data/registry/` concern (sibling of `data/registry/sources/`); domain-segmented|PROPOSED|
|`control_plane/consent_register.yaml`    |Control-plane registers index governance state (sibling of `source_authority_register.yaml`)    |PROPOSED|
|`policy/domains/people-dna-land/consent/`|If the register is treated as policy input rather than data                                     |PROPOSED|


> [!WARNING]
> The register-home question is ADR-class and entangled with the open consent-lane question (top-level `policy/consent/` vs domain-nested). Do not create the register in two homes (§2.4(5) no parallel authority). The strongest fit by the register pattern (KFM-P1-PROG-0007, which places source registers under `data/registry/`) is `data/registry/consent/people-dna-land/`, but this needs an ADR. Tracked as OQ-CREG-01 and tied to VB-PDL-04.

[Back to top](#contents)

-----

## 9. Audit and the risk it guards

The register is the control surface for two **High** risks named in the Atlas master risk register (§24.10):

|Risk (Atlas §24.10)                                                    |How the register guards it                                                                                                                           |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|**Living-person data exposed via inference** (aggregate + context join)|The register is internal-only, pseudonymous, and excluded from public surfaces / graph projections / AI context; bound-object joins are policy-gated.|
|**Source rights/sovereignty status changes without re-evaluation**     |Audit checks each entry’s upstream against current rights status; a rights change moves the entry to `pending_review` and re-evaluates the scope.    |

Audit cadence (PROPOSED): periodic steward review producing a `ReviewRecord`, checking for (a) aged-out consents past review cadence, (b) rights-status drift, (c) orphaned `bound_objects_ref` pointers, (d) entries stuck in `pending_review`, (e) any field that should be a pointer but contains literal data (a leak finding).

[Back to top](#contents)

-----

## 10. Governed AI behavior

CONFIRMED doctrine (Atlas Ch. 16 §L; §24.10 — the register must stay out of AI context).

|AI action touching the register                                                        |Outcome                             |
|---------------------------------------------------------------------------------------|------------------------------------|
|Summarize aggregate register *statistics* (counts by status, no subjects) for a steward|`ANSWER` (internal, no subject data)|
|Return any subject pseudonym, scope, or bound-object pointer to a non-steward surface  |`DENY`                              |
|Use register contents as Focus Mode context for a public answer                        |`DENY` — register is internal-only  |
|Infer a subject’s consent state from other data                                        |`DENY`                              |
|Answer when register state cannot be resolved                                          |`ABSTAIN`                           |


> [!CAUTION]
> The consent register MUST NOT enter any AI context window that can reach a public surface. It is a re-identification surface (§4); treating it as ordinary retrievable context is a trust-membrane violation.

[Back to top](#contents)

-----

## 11. Validators and fixtures

PROPOSED; homes use the **whole-domain** `people-dna-land` segment (or the consent register home an ADR establishes).

|Validator / fixture            |Proves                                                                                                               |Status  |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------|--------|
|No-raw-PII test                |No entry field contains a name, raw token, kit/vendor ID, or genotype (only pointers/pseudonyms/digests/fingerprints)|PROPOSED|
|Token-fingerprint test         |`upstream` stores a fingerprint, never a raw access token                                                            |PROPOSED|
|Presence-not-permission test   |An `active` entry with no `ReleaseManifest` still does not publish                                                   |PROPOSED|
|Revocation-cascade test        |Moving an entry to `revoked` invalidates all `bound_objects_ref` public derivatives within TTL                       |PROPOSED|
|Status-derivation test         |Render-gate status matches the four model checks (DSSE / status list / scope / retention)                            |PROPOSED|
|Pending-review-fail-closed test|`pending_review` / multi-party / death-of-subject entries deny by default                                            |PROPOSED|
|DUO-normalization test         |Non-GA4GH consent inputs are normalized to DUO codes before entry                                                    |PROPOSED|
|Register-not-in-AI-context test|The register is excluded from any AI-reachable context and any public surface                                        |PROPOSED|
|Audit-completeness test        |Every entry has a resolvable `last_audit` `ReviewRecord` within cadence                                              |PROPOSED|

<details>
<summary><strong>Recommended negative-path fixtures</strong> (PROPOSED, illustrative)</summary>

|Fixture                              |Expected outcome                     |
|-------------------------------------|-------------------------------------|
|`entry_with_raw_name.json`           |FAIL (no-raw-PII)                    |
|`entry_with_raw_token.json`          |FAIL (fingerprint only)              |
|`entry_with_genotype.json`           |FAIL (no genotype)                   |
|`active_entry_no_release.json`       |not published (presence ≠ permission)|
|`revoked_entry_stale_tile.json`      |FAIL (cascade incomplete)            |
|`multiparty_unresolved.json`         |DENY / pending_review                |
|`register_in_focus_mode_context.json`|DENY (internal-only)                 |
|`valid_active_entry.json`            |ALLOW (with evidence + release)      |

</details>

[Back to top](#contents)

-----

## 12. Open questions

|ID        |Item                                                                                          |Evidence that would settle it           |Status            |
|----------|----------------------------------------------------------------------------------------------|----------------------------------------|------------------|
|OQ-CREG-01|Register home: `data/registry/consent/` vs `control_plane/` vs `policy/`                      |ADR (tied to VB-PDL-04 / OQ-CONSENT-01) |OPEN              |
|OQ-CREG-02|Entry schema home and exact field shape                                                       |`schemas/contracts/v1/...`; ADR         |NEEDS VERIFICATION|
|OQ-CREG-03|Pseudonymization scheme for `subject_pseudonym` (deterministic vs salted)                     |Privacy policy + schema                 |NEEDS VERIFICATION|
|OQ-CREG-04|Multi-party consent representation in a single entry (corpus does not specify)                |ADR + schema design (= OQ-CONSENT-05)   |OPEN              |
|OQ-CREG-05|DUO version handling in long-running grants                                                   |DUO compatibility profile + audit rule  |OPEN              |
|OQ-CREG-06|Retention-after-revocation: does a revoked entry’s underlying object get purged or tombstoned?|Retention policy + ADR (= OQ-CONSENT-04)|OPEN              |
|OQ-CREG-07|Access-control / SoD for who may read or mutate the register                                  |CODEOWNERS + policy (ADR-S-09)          |NEEDS VERIFICATION|
|OQ-CREG-08|Whether this register folds into `sublanes/dna/` or stays domain-level                        |`sublanes/` ADR (ADR-NNNN)              |PROPOSED          |

[Back to top](#contents)

-----

## 13. Related docs

- [`./CONSENT_MODEL.md`](./CONSENT_MODEL.md) — consent doctrine and machinery (the model this register operationalizes)
- [`./ARCHITECTURE.md`](./ARCHITECTURE.md) — domain architecture (sensitivity tiers, MUST-DENY conditions)
- [`./CANONICAL_PATHS.md`](./CANONICAL_PATHS.md) — register/consent-lane placement conflict (§9.3, VB-PDL-04)
- `./sublanes/dna/README.md` — DNA sublane *(path pending the `sublanes/` ADR, ADR-NNNN)*
- [`directory-rules.md`](../../../directory-rules.md) — placement law (§6.2 control_plane registers, §2.4 ADR triggers)
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating law (`CONTRACT_VERSION = "3.0.0"`)
- Corpus anchors: Atlas Ch. 16 §C (`ConsentGrant`, `RevocationReceipt`, `DNAKitToken`) · §24.10 (risk register: living-person inference; rights-status drift) · KFM-P1-PROG-0007 (register pattern) · Pass-10 C9-02 (token fingerprint), C9-03 (no genotype republished), C9-04 (GA4GH DUO), C6-08 (revocation/cache), C5-09 (tombstones)

-----

**Last updated:** 2026-06-06 · **Doc id:** `kfm://doc/people-dna-land/consent-register` · **Status:** `draft` · `CONTRACT_VERSION = "3.0.0"` · [Back to top](#contents)