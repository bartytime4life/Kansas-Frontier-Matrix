<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/0ed8c96a-bff4-44d6-8629-289d99c15965
title: TEMPLATE — Steward Signoff
type: standard
version: v1
status: draft
owners: ["@data-stewards", "@governance-approvers"]
created: 2026-03-05
updated: 2026-03-05
policy_label: public
related: ["docs/governance/ROOT_GOVERNANCE.md", "docs/governance/ETHICS.md", "docs/governance/SOVEREIGNTY.md"]
tags: ["kfm", "governance", "template", "steward", "signoff", "promotion-gate"]
notes: ["Use this template to approve or block dataset promotion or publication in a traceable, fail-closed way."]
[/KFM_META_BLOCK_V2] -->

# TEMPLATE — Steward Signoff

One-line purpose: capture a **human steward decision** for a dataset or artifact promotion in a way that is **auditable**, **machine-linkable**, and **fail-closed**.

> **Status:** draft template  
> **Owners:** @data-stewards, @governance-approvers  
> **Applies to:** RAW → WORK → PROCESSED → PUBLISHED promotions, and any publish-tier change

## Quick nav

- [How to use](#how-to-use)
- [Signoff header](#signoff-header)
- [Decision](#decision)
- [Evidence checklist](#evidence-checklist)
- [Policy evaluation](#policy-evaluation)
- [Sensitivity and CARE review](#sensitivity-and-care-review)
- [Release and rollback](#release-and-rollback)
- [Signatures](#signatures)
- [Machine-readable summary](#machine-readable-summary)

---

## How to use

1. Copy this file to a concrete signoff record, for example:

   - `docs/governance/signoffs/SIGNOFF__<dataset_id>__<YYYY-MM-DD>.md`

2. Fill in **every field** that applies.
3. If any required evidence is missing, set **Decision = BLOCK** and list the minimum remediation steps.

---

## Signoff header

| Field | Value |
|---|---|
| Signoff ID | `S-YYYY-NNN` |
| Dataset ID | `<dataset_id>` |
| Dataset name | `<human_name>` |
| Scope | `promotion` \| `publication` \| `waiver` \| `other` |
| Promotion | `<from_zone>` → `<to_zone>` |
| Requested publish tier | `public` \| `restricted` \| `aggregate-only` \| `internal` |
| Sensitivity class | `public` \| `restricted` \| `sensitive-location` \| `aggregate-only` |
| Steward | `@handle` |
| Steward role | `data steward` \| `governance approver` \| `tribal liaison` \| `security` |
| Date | `YYYY-MM-DD` |
| PR or ticket | `<link>` |
| Pipeline run ID | `<run_id>` |
| Evidence bundle root | `<path or uri>` |

### Contacts

| Role | Name / handle | Contact |
|---|---|---|
| Data owner | `<name>` | `<email/handle>` |
| Maintainer | `<name>` | `<email/handle>` |
| On-call | `<name>` | `<pager/handle>` |

---

## Decision

- **Decision:** ✅ APPROVE \| ⚠️ APPROVE WITH CONDITIONS \| 🛑 BLOCK
- **Rationale:** `<2–6 sentences. Link to evidence, not opinions.>`
- **Conditions:** `<if any; include due dates and owners>`
- **Time-boxed approval:** `<optional: expires YYYY-MM-DD>`

### Follow-up tasks

- [ ] `<task 1>`
- [ ] `<task 2>`

---

## Evidence checklist

> Fill this section as if an auditor will read it later. Prefer **paths + hashes + validator output links** over prose.

### A. Checksums match

- [ ] Manifest present
  - Path: `<data/audit/checksums.json>`
  - Digest algorithm: `SHA-256`
- [ ] Verified against all promotion artifacts
  - Verification command: `<sha256sum -c ...>`
  - Result: `<pass/fail>`  
- Notes: `<optional>`

### B. Catalog record exists

- [ ] STAC present and valid
  - Collection path: `<data/stac/<dataset_id>/collection.json>`
  - Items path: `<data/stac/<dataset_id>/items/*.json>`
  - Validator output: `<link or path>`
- [ ] DCAT present and valid
  - DCAT path: `<data/catalog/dcat/<dataset_id>.jsonld>`
  - Validator output: `<link or path>`

### C. Provenance attached

- [ ] W3C PROV bundle present
  - Path: `<data/prov/<dataset_id>/bundle.json>`
- [ ] Lineage covers inputs → transforms → outputs
  - Inputs enumerated: ✅ \| ❌
  - Agents enumerated: ✅ \| ❌
  - Timestamps present: ✅ \| ❌

### D. License declared

- [ ] SPDX license ID declared: `<SPDX-ID>`
- [ ] Attribution text included where required
  - Location: `<path or url>`
- [ ] Use-conditions captured if license is not sufficient
  - Location: `<path or url>`

### E. Sensitivity classification

- [ ] Sensitivity class selected and justified
  - Class: `public` \| `restricted` \| `sensitive-location` \| `aggregate-only`
  - Justification: `<short>`
- [ ] Redaction policy noted and implemented where required
  - Redaction profile: `<profile name or path>`
  - Transform evidence: `<before/after diff link or hash list>`

### F. Run receipt present

- [ ] run_record present
  - Path: `<data/audit/run_record.json>`
- [ ] run_manifest present
  - Path: `<data/audit/run_manifest.json>`
- [ ] spec_hash recorded
  - Value: `<sha256...>`
  - Where recorded: `<path>`

### G. Pipeline run ID

- [ ] Stable run ID / URI exists and links outputs to logs
  - Run ID: `<runs/<uuid>>`
  - CI link: `<link>`
  - Artifact list: `<link or path>`

### H. Schema conformance

- [ ] Schema ref pinned
  - Schema ref: `<schemas/<id>@vX.Y>`
- [ ] Validation output recorded (pass/fail + warnings)
  - Output: `<path or link>`

### I. Sample inspection

- [ ] At least N=3 diverse samples inspected
  - N: `<3+>`
  - Evidence: `<screenshots/quicklooks/tiles>`  
- Notes: `<what you checked: geometry, attrs, time, joins, etc.>`

### J. Automated tests passed

- [ ] Data tests: ✅ \| ❌
- [ ] Contract tests: ✅ \| ❌
- [ ] Policy tests: ✅ \| ❌
- [ ] Catalog / PROV validators: ✅ \| ❌
- Test run link: `<link>`

### K. CI attestation available

- [ ] Build provenance attestation present
  - Attestation path or URI: `<attestations/<run>.intoto.jsonl>`
- [ ] Artifact signature present
  - Signature path or URI: `<signatures/<digest>.sig>`
- [ ] Verification performed
  - Command: `<cosign verify-attestation ...>`
  - Result: `<pass/fail>`

### L. CODEOWNERS review completed

- [ ] Required reviewers approved
  - Approvers: `<@handles>`
- [ ] Promotion PR references evidence
  - PR link: `<link>`
  - Evidence references: `<links>`

---

## Policy evaluation

- [ ] Policy engine evaluated this change
  - Policy package: `<policy/...>`
  - Tool: `OPA` \| `Conftest` \| `other`
  - Decision output: ✅ allow \| 🛑 deny
  - Decision artifact: `<path or link to decision JSON>`
- [ ] Any waivers are recorded, time-boxed, and signed
  - Waiver IDs: `<W-YYYY-NNN, ...>`
  - Waiver paths: `<policy/waivers/...>`
  - Expiry checked: ✅ \| ❌

---

## Sensitivity and CARE review

> Use this section for anything involving Indigenous data sovereignty, protected locations, minors, PII, or safety-sensitive targets.

- [ ] CARE label reviewed
  - care_label: `<Public | Restricted · Tribal Sensitive | ...>`
  - Notes: `<short>`
- [ ] Sensitive-location risk assessed
  - Does this dataset enable targeting or harm if misused: ✅ \| ❌
  - Mitigation applied: `<masking/aggregation/withholding>`
- [ ] Access tier matches risk
  - Tier: `<public/restricted/...>`
  - Rationale: `<short>`

---

## Release and rollback

- Publish / promotion action:
  - Action: `<promote / publish / reclassify>`
  - Effective at: `<YYYY-MM-DDTHH:MM:SSZ>`
- Rollback plan:
  - Rollback trigger: `<what would make us revert>`
  - Rollback command or procedure: `<exact commands>`
  - Permissions required: `<who can execute>`

---

## Signatures

### Steward signoff

| Field | Value |
|---|---|
| Steward | `@handle` |
| Signed at | `YYYY-MM-DDTHH:MM:SSZ` |
| Signoff method | `GitHub review` \| `signed commit` \| `cosign attestation` \| `other` |
| Public rationale link | `<PR comment link or doc link>` |

### Additional reviewers

| Role | Name / handle | Signed at | Notes |
|---|---|---|---|
| Governance approver | `<@handle>` | `<timestamp>` | `<optional>` |
| Security | `<@handle>` | `<timestamp>` | `<optional>` |
| Tribal liaison | `<@handle>` | `<timestamp>` | `<optional>` |

---

## Machine-readable summary

> Optional but recommended: keep this block in sync with the human-readable sections above.

```yaml
steward_signoff_version: v1
signoff_id: "S-YYYY-NNN"
dataset_id: "<dataset_id>"
promotion:
  from: "<raw|work|processed|published>"
  to: "<raw|work|processed|published>"
decision: "<approve|approve_with_conditions|block>"
signed_at: "YYYY-MM-DDTHH:MM:SSZ"
steward: "@handle"
evidence:
  checksums_manifest: "<path-or-uri>"
  stac: "<path-or-uri>"
  dcat: "<path-or-uri>"
  prov: "<path-or-uri>"
  run_record: "<path-or-uri>"
  run_manifest: "<path-or-uri>"
  attestation: "<path-or-uri>"
  signatures: ["<path-or-uri>"]
waivers: ["W-YYYY-NNN"]
notes: "<short>"
```

---

[Back to top](#template--steward-signoff)
