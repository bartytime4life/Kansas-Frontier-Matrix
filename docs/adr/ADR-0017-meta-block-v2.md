<!-- [KFM_META_BLOCK_V2]
meta:
  schema: meta-block-v2
  standard_id: ADR-0004-META-BLOCK-V2
  title: Meta Block V2
  version: 1.0.0
  status: accepted
  owner: TODO(kfm-verify): confirm owner
  steward: TODO(kfm-verify): confirm steward
  effective_date: 2026-05-05
  review_due_date: 2026-11-05
  sensitivity: internal
  rights:
    license_id: internal-use
    allowed_uses: [promotion, audit]
    prohibited_uses: []
  obligations:
    redaction_required: false
  evidence_bundle_ref: artifacts/EvidenceBundle.json
  decision_log_ref: artifacts/decision_log.json
  spec_hash: "<64-char-sha256>"
  supersedes: null
  references: []
  changelog:
    - version: 1.0.0
      date: 2026-05-05
      summary: Initial version
[/KFM_META_BLOCK_V2] -->

# ADR 0004: Meta Block V2

> **Status:** Accepted  
> **Repo path:** `docs/adr/ADR-0017-meta-block-v2.md`  
> **Owner/steward:** `NEEDS VERIFICATION`  
> **Implementation posture:** Metadata standard accepted; full repository enforcement remains staged.

![status: accepted](https://img.shields.io/badge/status-accepted-2ea44f)
![schema: meta-block-v2](https://img.shields.io/badge/schema-meta--block--v2-4051b5)
![gate: promotion](https://img.shields.io/badge/gate-promotion-6f42c1)
![posture: evidence-linked](https://img.shields.io/badge/posture-evidence--linked-0a7ea4)

**Quick jumps:** [Context](#context) · [Decision](#decision) · [Required fields](#required-fields) · [Examples](#examples) · [Validation / enforcement](#validation--enforcement) · [Migration](#migration) · [Rollback](#rollback) · [Open verification](#open-verification)

---

## Context

Standards and governance documents need machine-readable metadata so promotion policy can identify owners, versions, sensitivity, evidence references, and review obligations.

KFM documentation cannot rely on prose-only governance once documents become promotion inputs. A reviewer or CI gate needs a stable metadata surface for ownership, review freshness, rights, sensitivity, evidence linkage, and release linkage.

> [!NOTE]
> This ADR defines the required metadata profile. It does not by itself prove that every standards document is compliant, that every referenced evidence bundle exists, or that promotion gates are already enforcing the full profile.

---

## Decision

All standards documents that participate in promotion **MUST** include **Meta Block V2** as YAML front matter or an equivalent top-level metadata block.

New standards documents **MUST** use V2. Meta Block V1 is allowed only under an explicit migration exception recorded in the decision log.

### Normative Meta Block V2 profile

The `spec_hash` in this ADR is the SHA-256 digest of the following normalized UTF-8 profile text.

```text
Meta Block V2 normative profile v1.0.0

Applicability:
- Standards documents that participate in promotion MUST include Meta Block V2 as YAML front matter or an equivalent top-level metadata block.
- New standards documents MUST use Meta Block V2.
- Meta Block V1 MAY be accepted only through an explicit migration exception recorded in the decision log.

Required meta fields:
- schema
- standard_id
- title
- version
- status
- owner
- steward
- effective_date
- review_due_date
- sensitivity
- rights
- obligations
- evidence_bundle_ref
- decision_log_ref
- spec_hash

Required nested rights fields:
- license_id
- allowed_uses
- prohibited_uses

Required nested obligations fields:
- redaction_required

Promotion gate relationships:
- Gate C checks rights and sensitivity.
- Gate E checks decision ownership.
- Gate G checks release linkage.

Validation posture:
- A metadata block is structurally insufficient if required fields are present but owners, rights, sensitivity, review due date, evidence bundle reference, or decision log reference are false, stale, or unresolved.
- Token-only checks MAY be used as an early hygiene gate, but they MUST NOT be treated as full Meta Block V2 validation.
- Full enforcement SHOULD validate presence, type, parseability, owner/steward non-emptiness, date freshness, rights shape, obligations shape, evidence_bundle_ref, decision_log_ref, and spec_hash format.
```

[Back to top](#top)

---

## Required fields

| Field | Required | Purpose |
|---|---:|---|
| `schema` | Yes | Declares `meta-block-v2` so validators can select the correct profile. |
| `standard_id` | Yes | Stable document or standard identifier. |
| `title` | Yes | Human-readable title used in review, registers, and release notes. |
| `version` | Yes | SemVer-like version of the standard document. |
| `status` | Yes | Publication or lifecycle state such as `draft`, `active`, `accepted`, `superseded`, or `retired`. |
| `owner` | Yes | Responsible team or person for maintenance and changes. |
| `steward` | Yes | Governance steward accountable for review obligations. |
| `effective_date` | Yes | Date from which the standard applies. |
| `review_due_date` | Yes | Date by which the standard must be reviewed. |
| `sensitivity` | Yes | Handling classification for the document and its metadata. |
| `rights` | Yes | License, allowed uses, and prohibited uses. |
| `obligations` | Yes | Handling obligations, including redaction requirements. |
| `evidence_bundle_ref` | Yes | Pointer to supporting evidence bundle or evidence closure artifact. |
| `decision_log_ref` | Yes | Pointer to decision-log evidence for acceptance, exception, or migration. |
| `spec_hash` | Yes | 64-character SHA-256 digest of the governed specification basis. |

Recommended but optional fields include `supersedes`, `references`, and `changelog`. They are optional in the minimum profile but should be present in high-impact standards because they make supersession and review easier.

---

## Examples

### YAML front matter

```yaml
---
meta:
  schema: meta-block-v2
  standard_id: STD-EXAMPLE-001
  title: Example Standard
  version: 1.0.0
  status: active
  owner: team-or-person
  steward: governance-owner
  effective_date: 2026-05-05
  review_due_date: 2026-11-05
  sensitivity: internal
  rights:
    license_id: internal-use
    allowed_uses: [promotion, audit]
    prohibited_uses: []
  obligations:
    redaction_required: false
  evidence_bundle_ref: artifacts/EvidenceBundle.json
  decision_log_ref: artifacts/decision_log.json
  spec_hash: "<64-char-sha256>"
  supersedes: null
  references: []
  changelog:
    - version: 1.0.0
      date: 2026-05-05
      summary: Initial version
---
```

### Equivalent top-level metadata block

Repositories that cannot use YAML front matter may use an equivalent top-level metadata block, but the same required field names and nested shapes still apply.

```markdown
<!-- [KFM_META_BLOCK_V2]
meta:
  schema: meta-block-v2
  standard_id: STD-EXAMPLE-001
  title: Example Standard
  version: 1.0.0
  status: active
  owner: team-or-person
  steward: governance-owner
  effective_date: 2026-05-05
  review_due_date: 2026-11-05
  sensitivity: internal
  rights:
    license_id: internal-use
    allowed_uses: [promotion, audit]
    prohibited_uses: []
  obligations:
    redaction_required: false
  evidence_bundle_ref: artifacts/EvidenceBundle.json
  decision_log_ref: artifacts/decision_log.json
  spec_hash: "<64-char-sha256>"
[/KFM_META_BLOCK_V2] -->
```

> [!IMPORTANT]
> Token presence is not sufficient. A document can contain `[KFM_META_BLOCK_V2]` and still fail V2 if required fields are missing, stale, malformed, unresolved, or untrue.

[Back to top](#top)

---

## Consequences

Governance metadata is no longer prose-only. CI and reviewers can enforce document ownership, freshness, sensitivity handling, and evidence linkage.

Positive consequences:

- Promotion policy can read owners, stewards, versions, and review dates without parsing prose.
- Sensitive or internal documents can fail closed when metadata is missing or contradictory.
- Evidence and decision-log references become visible at the top of standards documents.
- Supersession, rollback, and migration reviews can use a shared metadata surface.

Costs and tradeoffs:

- Standards documents now carry structured metadata that must be maintained.
- Reviewers must distinguish token presence from full metadata validation.
- Existing documents may require a V1-to-V2 migration exception path.
- `spec_hash` requires a repository-specific canonicalization rule before strict enforcement.

---

## Validation / Enforcement

Gate C checks rights and sensitivity. Gate E checks decision ownership. Gate G checks release linkage.

Repository-specific linters should be added when standards documents become first-class promotion inputs.

### Minimum staged enforcement

| Stage | Check | Failure posture |
|---|---|---|
| 0 | Token presence for documents expected to carry metadata. | Warn or fail, depending on rollout phase. |
| 1 | Parseable YAML or equivalent block with `meta.schema: meta-block-v2`. | Fail for promotion inputs. |
| 2 | Required field presence and expected nested shapes. | Fail for promotion inputs. |
| 3 | Date format, `review_due_date` freshness, and status vocabulary. | Fail or block promotion. |
| 4 | Rights, sensitivity, and obligations are policy-readable. | Gate C `DENY` if missing or unsafe. |
| 5 | Owner and steward are non-empty and decision-log linked. | Gate E `DENY` if unresolved. |
| 6 | `evidence_bundle_ref`, `decision_log_ref`, and release refs resolve where required. | Gate G `DENY` if unresolved. |
| 7 | `spec_hash` is a 64-character SHA-256 digest reproducible under the repo hashing rule. | `ERROR` or block release candidate. |

### PROPOSED linter behavior

```text
INPUT: Markdown standards document
1. Locate YAML front matter or top-level KFM Meta Block V2 block.
2. Parse metadata.
3. Confirm meta.schema == meta-block-v2.
4. Confirm required fields exist.
5. Confirm nested rights and obligations shapes.
6. Confirm dates parse and review_due_date is not stale for active documents.
7. Confirm spec_hash format and, once canonicalization is defined, reproducibility.
8. Emit finite result: PASS, WARN, DENY, or ERROR.
```

> [!CAUTION]
> Full Meta Block V2 validation must not become a hidden policy authority. Policy meaning belongs in policy gates; the linter verifies that metadata is present, parseable, and policy-readable.

---

## Migration

Existing standards documents may temporarily accept Meta Block V1 only through an explicit migration exception recorded in `decision_log.json`.

Migration records should include:

| Field | Purpose |
|---|---|
| document path | Identifies the migrated document. |
| current metadata version | Records V1 or missing metadata state. |
| target metadata version | Records V2. |
| exception owner | Names who accepted temporary non-compliance. |
| expiration date | Prevents indefinite V1 carry-forward. |
| migration notes | Explains required corrections. |
| decision log ref | Links the exception to review evidence. |

---

## Rollback

Documents may temporarily accept Meta Block V1 only through an explicit migration exception recorded in `decision_log.json`. New documents must use V2.

If Meta Block V2 enforcement blocks necessary work because the linter is wrong or incomplete:

1. Keep V2 as the target standard.
2. Disable only the failing enforcement stage, not the metadata requirement itself.
3. Record the exception in the decision log.
4. Add a rollback card or issue that names the blocked documents, failed check, owner, and expiration date.
5. Re-enable enforcement after the linter, schema, or canonicalization bug is fixed.

[Back to top](#top)

---

## Open verification

| Item | Status | Why it matters |
|---|---|---|
| Owner and steward values for this ADR | NEEDS VERIFICATION | Metadata fields are present but not yet owner-confirmed. |
| `evidence_bundle_ref` physical path | NEEDS VERIFICATION | `artifacts/EvidenceBundle.json` follows the supplied ADR example but may need alignment with the repo artifact/release layout. |
| `decision_log_ref` physical path | NEEDS VERIFICATION | `artifacts/decision_log.json` must resolve before strict release gating. |
| `spec_hash` canonicalization rule | NEEDS VERIFICATION | This draft uses a documented normative-profile hash; repo-wide reproducibility rules should be standardized. |
| ADR numbering namespace | NEEDS VERIFICATION | The repo contains both `docs/adr/ADR-0017-meta-block-v2.md` and `docs/adr/ADR-0004-evidencebundle-contract.md`; keep both discoverable until the ADR index resolves the naming convention. |
| Full linter implementation | PROPOSED | Existing token checks are useful but insufficient for complete Meta Block V2 enforcement. |

---

## Review checklist

- [ ] Metadata block is present at the top of the document.
- [ ] `[KFM_META_BLOCK_V2]` token is present for current token-based checks.
- [ ] Required fields are present under `meta`.
- [ ] `owner` and `steward` are verified or explicitly marked `TODO(kfm-verify)`.
- [ ] `review_due_date` is no later than the required review interval.
- [ ] Rights and obligations are policy-readable.
- [ ] `evidence_bundle_ref` resolves or is explicitly blocked from release.
- [ ] `decision_log_ref` resolves or is explicitly blocked from release.
- [ ] `spec_hash` is 64 lowercase hex characters and its basis is documented.
- [ ] Migration exceptions are recorded in the decision log.
- [ ] New standards documents use V2 rather than V1.

