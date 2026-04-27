---
name: Source intake
about: Propose onboarding a new source or updating source terms
title: "[source-intake] "
labels: ["source-intake"]
assignees: ""
---

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Source Intake Issue Template
type: standard
version: v1
status: draft
owners: @bartytime4life
created: NEEDS-VERIFICATION
updated: 2026-04-27
policy_label: NEEDS-VERIFICATION
related: [
  ./README.md,
  ./bug_report.md,
  ./documentation_drift.md,
  ./policy_or_release_gap.md,
  ../README.md,
  ../CODEOWNERS,
  ../PULL_REQUEST_TEMPLATE.md,
  ../SECURITY.md,
  ../../README.md,
  ../../docs/README.md,
  ../../docs/standards/README.md,
  ../../contracts/README.md,
  ../../schemas/README.md,
  ../../policy/README.md,
  ../../data/registry/README.md
]
tags: [kfm, github, issue-template, source-intake, source-descriptor, evidence, policy, data-registry]
notes: [
  GitHub issue-template YAML front matter is kept first so the template remains parseable; this KFM meta block follows immediately after the front matter.
  doc_id, created date, policy_label, label existence, and active branch enforcement still need verification.
  This revision preserves the existing source-intake headings while expanding the template into a reviewable KFM source-admission record.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Source Intake Issue Template

Use this issue to evaluate a **new source**, **changed endpoint**, **dataset family**, or **source-term update** before KFM treats it as admissible, schedulable, publishable, or safe to expose.

> [!IMPORTANT]
> Source intake is not a connector request. It is an evidence, rights, sensitivity, source-role, cadence, and release-posture review before live ingestion, automation, map exposure, AI use, or publication.

**Quick jumps:** [Use this when](#use-this-when) · [Do not use this when](#do-not-use-this-when) · [Source summary](#source-summary) · [Source role](#source-role) · [Rights and usage terms](#rights-and-usage-terms) · [Sensitivity considerations](#sensitivity-considerations) · [Expected cadence](#expected-cadence) · [Proposed target paths](#proposed-target-paths) · [Evidence and verification](#evidence-and-verification) · [Intake decision requested](#intake-decision-requested) · [Submission checks](#submission-checks)

---

## Use this when

| Accepted input | Use this template when… | Minimum posture |
|---|---|---|
| New source family | A publisher, steward, agency, archive, sensor network, API, dataset, or document family may become part of KFM. | State the source role, rights, sensitivity, cadence, and evidence basis. |
| Source-term update | License, terms, access mode, attribution, redistribution, or rate-limit behavior changed. | Link to current terms and mark unresolved items `NEEDS_VERIFICATION`. |
| Endpoint or feed change | A URL, API route, file location, version, schema, refresh signal, or source identity changed. | Keep ingestion blocked or staged until source identity and policy posture are clear. |
| SourceDescriptor candidate | A source needs a descriptor, registry entry, fixture, validation rule, or policy review. | Label proposed paths and objects as `PROPOSED` unless already verified. |
| Source-role dispute | A source may be authoritative, supplemental, observational, modeled, regulatory, interpretive, derived, or contextual. | Do not collapse roles; record the narrowest truthful role. |

## Do not use this when

| Need | Use instead | Why |
|---|---|---|
| Defect in behavior, validation, or automation | [`bug_report.md`](./bug_report.md) | Bugs need reproduction steps and current runtime/tool evidence. |
| Documentation no longer matches implementation | [`documentation_drift.md`](./documentation_drift.md) | Drift should identify the stronger source of truth and proposed correction. |
| Missing policy, release, rollback, or sensitivity gate | [`policy_or_release_gap.md`](./policy_or_release_gap.md) | Policy gaps should not be hidden inside source intake. |
| Secret, credential, token, private endpoint, sensitive geometry, or exposure path | [`../SECURITY.md`](../SECURITY.md) | Public issue text must not expose secrets or sensitive locations. |

> [!CAUTION]
> Do not paste private credentials, API keys, unpublished private endpoints, exact sensitive coordinates, private landowner details, living-person data, DNA/genomic material, or controlled cultural/archaeological locations into this issue.

---

## Intake posture at a glance

| Field | Value |
|---|---|
| Source family / working name |  |
| Submitter |  |
| Domain lane(s) affected |  |
| Requested action | `capture` / `admit` / `update terms` / `quarantine` / `deny` / `needs verification` |
| Current truth label | `CONFIRMED` / `INFERRED` / `PROPOSED` / `UNKNOWN` / `NEEDS_VERIFICATION` |
| Public exposure requested? | `no` / `yes` / `unknown` |
| Live ingestion requested? | `no` / `yes` / `unknown` |
| Sensitive material possible? | `no` / `yes` / `unknown` |
| Rights / redistribution clear? | `no` / `yes` / `unknown` |
| Existing KFM source or descriptor? |  |

### Truth labels for this issue

| Label | Use it when… |
|---|---|
| `CONFIRMED` | The claim is directly supported by inspected source text, official metadata, current repo files, or retained evidence. |
| `INFERRED` | The claim is a bounded conclusion from evidence, but not directly proven. |
| `PROPOSED` | The item is a recommended KFM destination, role, object, or workflow that still needs review. |
| `UNKNOWN` | The issue does not yet contain enough evidence to make the claim. |
| `NEEDS_VERIFICATION` | The item must be checked against current source terms, repo state, owner records, policy, fixtures, or platform settings. |

---

## Source summary

<!-- Preserve this section: it is the existing source_intake.md anchor. -->

- **Source name:**
- **Publisher / steward / owner:**
- **Official source URL(s):**
- **Access mode:** `public web` / `API` / `download` / `portal` / `authenticated` / `manual upload` / `other`
- **Source family:** `agency` / `archive` / `sensor` / `field observation` / `model` / `regulatory` / `catalog` / `documentary` / `community` / `other`
- **Domain lane(s):**
- **Geographic scope:**
- **Temporal scope:**
- **Why KFM needs this source:**
- **What KFM must not infer from this source:**
- **Known related KFM docs, descriptors, fixtures, tests, or issues:**

## Source role

<!-- Preserve this section: it is the existing source_intake.md anchor. -->

Select the narrowest truthful role. A source may have more than one role, but each role needs a clear boundary.

- [ ] Authoritative / official record
- [ ] Regulatory or legal boundary
- [ ] Observational measurement
- [ ] Sensor or station feed
- [ ] Model, forecast, projection, or estimate
- [ ] Derived or transformed layer
- [ ] Archival or documentary evidence
- [ ] Supplemental context only
- [ ] Community, steward, or user-submitted material
- [ ] AI-assisted or machine-classified interpretation
- [ ] Unknown / needs review

**Role explanation:**

**Known caveats, limits, or interpretation hazards:**

**Competing or corroborating sources:**

## Rights and usage terms

<!-- Preserve this section: it is the existing source_intake.md anchor. -->

| Rights question | Answer / evidence |
|---|---|
| License or terms URL |  |
| Redistribution allowed? | `yes` / `no` / `unknown` |
| Public display allowed? | `yes` / `no` / `unknown` |
| Caching or snapshotting allowed? | `yes` / `no` / `unknown` |
| Attribution required? |  |
| Commercial or reuse restriction? |  |
| API key, account, or token required? | `yes` / `no` / `unknown` |
| Rate limits or access constraints? |  |
| Terms changed recently? | `yes` / `no` / `unknown` |
| Rights reviewer needed? | `yes` / `no` / `unknown` |

> [!WARNING]
> If rights, redistribution, attribution, sensitivity, or access terms are unclear, the safest KFM posture is `ABSTAIN`, `DENY`, or `QUARANTINE` until policy review resolves the gap.

## Sensitivity considerations

<!-- Preserve this section: it is the existing source_intake.md anchor. -->

Check any class that may apply. When uncertain, mark `UNKNOWN` and describe the review needed.

- [ ] Archaeology, sacred sites, burial sites, cultural heritage, or controlled community knowledge
- [ ] Rare species, sensitive habitat, critical habitat, nesting sites, or precision-sensitive occurrence data
- [ ] Critical infrastructure, private facilities, emergency systems, utilities, or security-relevant geometry
- [ ] Private landowner, parcel, tenancy, address, or property exposure risk
- [ ] Living-person data, minors, genealogy, DNA, genomics, health, or family relationship material
- [ ] Indigenous data sovereignty, tribal stewardship, or protected knowledge concerns
- [ ] Exact coordinates that should be generalized, withheld, delayed, or role-limited
- [ ] Private endpoint, credential, access token, or restricted service URL
- [ ] No known sensitivity issue
- [ ] Unknown / needs review

**Sensitivity notes:**

**Public-safe transform needed?** `none` / `generalize` / `aggregate` / `redact` / `withhold` / `embargo` / `role-limit` / `unknown`

**Who should review sensitivity before public exposure?**

## Expected cadence

<!-- Preserve this section: it is the existing source_intake.md anchor. -->

| Cadence question | Answer / evidence |
|---|---|
| Update frequency |  |
| Freshness expectation |  |
| Change signal | `versioned release` / `timestamp` / `ETag` / `hash` / `RSS` / `API metadata` / `manual check` / `unknown` |
| Snapshot or checksum strategy |  |
| Deactivation / supersession behavior |  |
| Known data-quality warnings |  |
| Stale-data risk if not refreshed |  |
| Proposed refresh owner | `NEEDS_VERIFICATION` |

## Proposed target paths

<!-- Preserve this section: it is the existing source_intake.md anchor. -->

Do not mark a path `CONFIRMED` unless it exists in the current branch or a maintainer verifies it.

| Target surface | Proposed path or object | Truth label | Why this belongs there |
|---|---|---:|---|
| Source descriptor / intake record |  | `PROPOSED` | Records source identity, role, rights, cadence, access, sensitivity, and review posture. |
| Registry entry |  | `PROPOSED` | Keeps source admission visible before ingestion or publication. |
| RAW / WORK / QUARANTINE landing |  | `PROPOSED` | Routes material through lifecycle state instead of direct publication. |
| Contract or object meaning |  | `PROPOSED` | Defines stable object semantics if a new source object is needed. |
| Schema or machine validation |  | `PROPOSED` | Validates descriptor, payload, fixture, or receipt shape. |
| Policy rule or obligation |  | `PROPOSED` | Handles rights, sensitivity, access, publication, or review state. |
| Fixture or test |  | `PROPOSED` | Provides valid/invalid examples before connector confidence grows. |
| Tool / validator / pipeline |  | `PROPOSED` | Keeps implementation testable outside GitHub workflow YAML. |
| Documentation / runbook |  | `PROPOSED` | Explains source role, review burden, refresh behavior, and correction path. |
| Release / proof / catalog surface |  | `PROPOSED` | Only after validation, policy, review, and publication readiness are satisfied. |

---

## Evidence and verification

List only evidence that was actually inspected. Use `UNKNOWN` instead of guessing.

| Evidence item | Link, path, or retained reference | Truth label | Notes |
|---|---|---:|---|
| Official source page or documentation |  |  |  |
| License / terms / usage policy |  |  |  |
| Metadata, schema, sample record, or endpoint response |  |  |  |
| Source owner or steward record |  |  |  |
| Existing KFM repo file or issue |  |  |  |
| Related fixture, validator, test, or proof object |  |  |  |
| Public-safety or sensitivity review reference |  |  |  |

### Verification needed before stronger claims

- [ ] Source identity is clear enough to create or update a descriptor.
- [ ] Source role is separated from derived, modeled, supplemental, or interpretive use.
- [ ] Rights, license, terms, attribution, redistribution, and access limits are recorded.
- [ ] Sensitivity and public-exposure risk are reviewed or explicitly marked `UNKNOWN`.
- [ ] Cadence, freshness, versioning, and staleness risk are documented.
- [ ] Proposed target paths are verified or truth-labeled as `PROPOSED`.
- [ ] Valid and invalid examples are identified or listed as follow-up work.
- [ ] Policy review is requested where rights, sensitivity, access, or release posture is unresolved.
- [ ] No live connector, scheduler, public map layer, AI answer path, or release workflow is assumed from this issue alone.
- [ ] Rollback, quarantine, correction, or withdrawal path is named if the source is later found unsafe or wrong.

## Intake decision requested

What should maintainers decide from this issue?

- [ ] Capture source candidate only.
- [ ] Create or update a SourceDescriptor / source intake record.
- [ ] Update rights, terms, attribution, or access notes for an existing source.
- [ ] Route to policy review.
- [ ] Route to sensitivity or steward review.
- [ ] Route to contract/schema/fixture work.
- [ ] Route to connector, validator, or pipeline work after source posture is resolved.
- [ ] Quarantine pending rights, sensitivity, source-role, or evidence review.
- [ ] Deny or block this source for KFM use.
- [ ] Other:

**Requested outcome and rationale:**

**Blocking unknowns:**

**Suggested follow-up issue, PR, ADR, descriptor, policy, fixture, or test:**

---

## Submission checks

Before submitting, confirm the issue is reviewable and safe.

- [ ] I did not include secrets, tokens, credentials, private service URLs, or sensitive exact coordinates.
- [ ] I used `UNKNOWN` or `NEEDS_VERIFICATION` where evidence is missing.
- [ ] I separated source role from desired KFM use.
- [ ] I included rights, terms, attribution, and redistribution evidence where available.
- [ ] I identified sensitivity risks or explicitly marked them unknown.
- [ ] I did not request live ingestion, publication, AI use, or public map exposure before policy and source review.
- [ ] I listed proposed paths as `PROPOSED` unless the current repo verifies them.
- [ ] I stated what KFM should not infer from this source.

[Back to top](#top)
