---
name: Source admission proposal
about: Propose a source for governed KFM admission with identity, role, rights, sensitivity, cadence, access, validation, and fail-closed handling.
title: "[Source Admission]: "
labels: []
assignees: ["bartytime4life"]
---

<!--
KFM public source-admission intake template.

This issue is a proposal and routing record. Filing it does not admit a source,
create or approve a SourceDescriptor, activate a connector, authorize a fetch,
grant rights, assign source authority, move data into RAW, approve public release,
or prove that downstream evidence is valid.

Before submitting:
1. Search existing source descriptors, registry entries, connectors, issues, PRs,
   ADRs, and domain source documentation for duplicates or superseded work.
2. Describe the source and intended use before prescribing repository paths.
3. Provide public-safe metadata and terms links; do not paste credentials,
   restricted payloads, private records, exact sensitive locations, or licensed
   content that cannot be redistributed.
4. Use synthetic or minimized examples. Do not test live endpoints, scrape data,
   bypass access controls, or fetch restricted material from this issue.
5. Use the private-first path in SECURITY.md when endpoint details, credentials,
   vulnerability information, private records, or immediate harmful exposure are
   involved.
6. Mark uncertainty as UNKNOWN or NEEDS VERIFICATION rather than guessing.

Admission is distinct from promotion and publication:
external source -> admission review -> RAW or QUARANTINE / DENY
-> later governed lifecycle and release gates.
-->

> [!IMPORTANT]
> A source-admission issue is not a `SourceDescriptor`, `SourceActivationDecision`, `SourceIntakeRecord`, rights decision, sensitivity decision, connector authorization, ingest receipt, evidence bundle, or release approval. Governed artifacts must be created and reviewed in their owning roots.

> [!CAUTION]
> Do not post API keys, tokens, private endpoints, access-control bypass details, exact rare-species or archaeology locations, critical-infrastructure vulnerability information, living-person records, genealogy, DNA/genomic material, private-land details, source-restricted payloads, unreleased data, or full copyrighted datasets. Route sensitive or security-relevant details through `SECURITY.md`.

## Proposal summary

<!-- In one or two sentences: what source is proposed, for which KFM purpose, and why is admission review needed? -->

-

## Reporter preflight

- [ ] I searched existing issues, PRs, source descriptors, registry entries, connector directories, and domain source documents for duplicate or superseded work.
- [ ] I identified the source's publisher or steward, intended KFM use, and public-safe upstream reference.
- [ ] I separated current evidence from proposed role, implementation, and repository placement.
- [ ] I did not include secrets, restricted payloads, exact sensitive locations, private records, or unauthorized copies of source content.
- [ ] I did not perform or request unauthorized scraping, authentication bypass, live-system testing, or access outside the source's terms.
- [ ] I understand that filing, assigning, labeling, prioritizing, or closing this issue does not admit or activate the source.
- [ ] I understand that admission does not authorize promotion or publication.

## Current truth posture

<!-- Apply the strongest support available to each material claim. -->

- [ ] `CONFIRMED` — verified from current repository evidence, official source materials, governed records, tests, logs, or generated artifacts.
- [ ] `PROPOSED` — intended source role, descriptor, connector, path, activation, or use under review.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and unsafe to assume.

**Overall proposal posture:** `PROPOSED`

## Source identity

| Field | Public-safe value |
|---|---|
| Proposed KFM source ID | `PROPOSED / UNKNOWN` |
| Source title / display name | |
| Publisher / issuing organization | |
| Owner, steward, or accountable organization | |
| Official source landing page | |
| Official documentation or data dictionary | |
| Terms, license, or use-policy URL | |
| Upstream dataset / feed / API / collection ID | |
| Upstream version or revision | `UNKNOWN` |
| Proposed descriptor version | `PROPOSED` |
| Domain scope | |
| Geographic scope | |
| Temporal coverage | |
| First available / publication date | `UNKNOWN` |
| Current availability status | `active / archived / intermittent / restricted / UNKNOWN` |
| Existing KFM descriptor or registry pointer | `NONE / UNKNOWN / path` |
| Related connector or pipeline | `NONE / UNKNOWN / path` |

> [!NOTE]
> A proposed source ID or descriptor path is not reserved by this issue. Identity and placement remain `PROPOSED` until collision checks, Directory Rules review, and governed admission review pass.

## Source discovery and need

### How was the source discovered?

- [ ] Official agency, institution, publisher, or steward documentation
- [ ] Existing KFM documentation, registry, issue, ADR, or source dossier
- [ ] Related connector or pipeline work
- [ ] Research publication or authoritative catalog
- [ ] Community, domain-steward, or rights-holder recommendation
- [ ] Existing public product or release
- [ ] Other:
- [ ] `UNKNOWN`

**Public-safe discovery evidence:**

-

### Intended KFM use

<!-- Describe the specific questions, products, validation needs, or evidence gaps this source may support. -->

-

### Who or what benefits?

- [ ] Source or domain stewards
- [ ] Researchers, educators, or community users
- [ ] Governed API / map / explorer users
- [ ] Evidence, validation, or catalog workflows
- [ ] Connector or pipeline maintainers
- [ ] Policy, rights, sensitivity, or release reviewers
- [ ] Correction, audit, or rollback workflows
- [ ] Other:
- [ ] `UNKNOWN`

## Descriptor-level versus record-level admission

KFM distinguishes the source-level decision from the per-record minimum bar.

### Descriptor-level admission

<!-- Is this source eligible to enter KFM, in what role, under what rights, sensitivity, access, cadence, and review posture? -->

- Proposed descriptor outcome:
- Required source-review roles:
- Required policy or rights review:
- Required sensitivity or sovereignty review:
- Proposed activation scope:
- Open descriptor questions:

### Record-level admission

<!-- What must each record satisfy before it may enter normalized processing? What must fail closed? -->

**Minimum record bar:**

1.
2.
3.

**Fail-closed triggers:**

- [ ] Missing or invalid stable record identity
- [ ] Missing provenance or source linkage
- [ ] Rights, license, attribution, redistribution, or consent unresolved
- [ ] Sensitivity, exact-location, privacy, sovereignty, or community authority unresolved
- [ ] Source role or authority cannot be determined
- [ ] Required geometry, time, units, taxonomy, or domain fields invalid
- [ ] Payload malformed, truncated, corrupt, or inconsistent with source documentation
- [ ] Upstream version, checksum, ETag, revision, or source-head identity changed unexpectedly
- [ ] Record is outside declared geographic, temporal, or thematic scope
- [ ] Rate limit, authentication, access posture, or terms prohibit the attempted use
- [ ] Record is candidate, modeled, synthetic, aggregate, or administrative material being upcast as observed or authoritative truth
- [ ] Other:
- [ ] `UNKNOWN`

**Expected failure disposition:** `QUARANTINE / DENY / HOLD / RETRY / ABSTAIN / UNKNOWN`

## Source type, role, and authority

### Source type

- [ ] Government or regulatory publication
- [ ] Scientific observation or monitoring dataset
- [ ] Administrative or operational record
- [ ] Archive, library, museum, herbarium, collection, or historical record
- [ ] Aggregator or index
- [ ] Model, forecast, simulation, or derived product
- [ ] Community- or steward-maintained source
- [ ] Commercial or licensed source
- [ ] User-contributed or manually curated source
- [ ] Synthetic fixture or test-only source
- [ ] Other:
- [ ] `UNKNOWN`

### Proposed primary source role

Use the current schema/contract vocabulary when verified. Do not silently translate older or domain-specific role labels.

- [ ] Authoritative for a bounded claim
- [ ] Regulatory or legal context
- [ ] Observation or occurrence evidence
- [ ] Aggregator
- [ ] Candidate signal
- [ ] Modeled or derived public product
- [ ] Steward-review source
- [ ] Citation source
- [ ] Fixture only
- [ ] Contextual / administrative / aggregate / synthetic role requiring vocabulary reconciliation
- [ ] `NEEDS VERIFICATION`
- [ ] `UNKNOWN`

**Proposed source-role value as it would appear in the current descriptor schema:**

-

### Authority and limits

| Field | Value |
|---|---|
| Authority rank or posture | `PROPOSED / UNKNOWN` |
| Authority basis | |
| Allowed claim roles | |
| Prohibited claim roles | |
| Confidence posture | |
| Required corroboration | |
| Aggregation unit, when applicable | |
| Model run or method reference, when applicable | |
| Candidate disposition, when applicable | |
| Reality-boundary note, when synthetic | |
| Known limitations or caveats | |

> [!IMPORTANT]
> Source role is fixed at admission and must not be upgraded by promotion, mapping, summarization, graph projection, or AI generation. A descriptor records how KFM may treat a source; it does not make every statement in that source true.

## Rights, terms, consent, and sovereignty

| Question | Answer / evidence |
|---|---|
| Rights status | `verified open / verified restricted / permission required / unknown / noassertion / denied / NEEDS VERIFICATION` |
| License or governing terms | |
| Terms version / retrieval date | |
| Attribution required | `No / Yes / UNKNOWN` |
| Redistribution allowed | `No / Yes / Restricted / UNKNOWN` |
| Commercial use allowed | `No / Yes / Restricted / UNKNOWN` |
| Derivative works allowed | `No / Yes / Restricted / UNKNOWN` |
| Bulk download or caching allowed | `No / Yes / Restricted / UNKNOWN` |
| Automated access allowed | `No / Yes / Restricted / UNKNOWN` |
| Retention or deletion obligations | |
| Embargo or time limits | |
| Consent or purpose limitation | |
| Community, sovereign, cultural, or custodial authority | |
| Rights verifier / reviewer | `UNKNOWN` |
| Rights re-review date or trigger | `UNKNOWN` |

- [ ] Official terms or license were reviewed.
- [ ] Attribution text or citation requirement is known.
- [ ] Redistribution and derivative-use posture is known.
- [ ] Automated access and caching posture is known.
- [ ] Consent, community authority, sovereignty, and purpose limitations were considered.
- [ ] Rights remain unresolved; admission must fail closed or remain under review.
- [ ] Private or legal review is required.
- [ ] `UNKNOWN`

## Sensitivity, privacy, and public-safety posture

### Proposed default sensitivity

Record only the vocabulary supported by the current descriptor schema or a cited governed policy. Do not resolve the documented 0–5 versus proposed T0–T4 scheme from this issue.

- Current source sensitivity notation:
- Proposed schema value:
- Governing policy or review pointer:
- Status: `CONFIRMED / PROPOSED / NEEDS VERIFICATION / UNKNOWN`

### Concern classes

- [ ] Public or low-sensitivity material
- [ ] Exact rare-species, rare-plant, habitat, nesting, roosting, or denning locations
- [ ] Archaeology, paleontology, burial, sacred, cultural, or collection-site locations
- [ ] Living-person, genealogy, identity-linkage, health, biometric, DNA, or genomic information
- [ ] Critical infrastructure, facility, utility, transport, emergency, or operational detail
- [ ] Private-land, stewardship, ownership, access, or landholder information
- [ ] Source-restricted field notes, unpublished research, confidential records, or licensed media
- [ ] Community-controlled, sovereign, Indigenous, traditional-knowledge, or CARE-governed material
- [ ] Information that becomes sensitive through joins, graph inference, maps, labels, dates, or other reconstruction
- [ ] No known sensitivity concern
- [ ] `UNKNOWN`

**Required public-safe treatment:** `none / generalize / aggregate / redact / delay / restrict / deny / steward review / UNKNOWN`

**Private review required:** `No / Yes / NEEDS VERIFICATION`

## Access and endpoint posture

> [!CAUTION]
> Never include credentials, tokens, private endpoint details, or access-control bypass instructions. Describe authentication type and approved access method only.

| Field | Value |
|---|---|
| Access method | `download / API / feed / portal / upload / manual / other / UNKNOWN` |
| Access posture | `public / authenticated / restricted / closed / permission required / UNKNOWN` |
| Public-safe endpoint or landing URL | |
| Authentication type | `none / API key / OAuth / account / signed URL / other / UNKNOWN` |
| Credentials required | `No / Yes / UNKNOWN` |
| Rate limits | `UNKNOWN` |
| Robots / automated-access restrictions | `UNKNOWN` |
| Expected formats | |
| Expected compression / packaging | |
| Pagination or partitioning | |
| Estimated volume | `UNKNOWN` |
| Update mechanism | `poll / webhook / snapshot / manual / other / UNKNOWN` |
| Network allowlist or egress implications | `UNKNOWN` |
| Approved test environment | `UNKNOWN` |

- [ ] No credential or restricted endpoint is disclosed here.
- [ ] Access method is permitted by the source terms.
- [ ] Rate limits and operational constraints are understood.
- [ ] A no-network fixture can represent the source shape.
- [ ] Live access must remain disabled until descriptor, review, fixtures, validator, and activation requirements pass.
- [ ] `UNKNOWN`

## Cadence, freshness, and source-head identity

| Field | Value |
|---|---|
| Upstream update cadence | `real-time / hourly / daily / weekly / monthly / annual / irregular / static / UNKNOWN` |
| Expected KFM retrieval cadence | `PROPOSED / UNKNOWN` |
| Freshness tolerance | `UNKNOWN` |
| Staleness policy | `mark stale / hold / re-review / disable / other / UNKNOWN` |
| Source publication time field | `UNKNOWN` |
| Observation / valid-time field | `UNKNOWN` |
| Retrieval time required | `No / Yes / UNKNOWN` |
| Time zone / calendar semantics | `UNKNOWN` |
| ETag or revision ID available | `No / Yes / UNKNOWN` |
| Last-Modified available | `No / Yes / UNKNOWN` |
| Upstream checksum available | `No / Yes / UNKNOWN` |
| Content length / source-head method | `UNKNOWN` |
| Upstream version field | `UNKNOWN` |
| Drift or change-detection plan | |

**Re-admission or re-review triggers:**

- [ ] Terms or license change
- [ ] Publisher, steward, endpoint, or source identity change
- [ ] Schema, fields, geometry, units, taxonomy, or format change
- [ ] Source role or authority posture change
- [ ] Sensitivity, consent, sovereignty, or access posture change
- [ ] Cadence or freshness expectation change
- [ ] Checksum, ETag, revision, or source-head drift
- [ ] Quality or reliability degradation
- [ ] Connector behavior or network posture change
- [ ] Other:
- [ ] `UNKNOWN`

## Citation and evidence posture

| Field | Value |
|---|---|
| Citation required | `No / Yes / UNKNOWN` |
| Citation template | |
| Preferred citation URL or identifier | |
| Publisher attribution text | |
| Version/date citation requirements | |
| License or rights notice required in citation | |
| Persistent identifier / DOI / accession | |
| EvidenceRef strategy | `PROPOSED / UNKNOWN` |
| EvidenceBundle resolution requirements | |
| Public caveat or reality-boundary note | |
| Citation re-review trigger | |

- [ ] Downstream claims must identify this source and preserve its role.
- [ ] Citation does not substitute for evidence sufficiency.
- [ ] The source can support an `EvidenceBundle` under the proposed use.
- [ ] Missing citation or evidence support must produce `ABSTAIN`, `HOLD`, or `DENY`.
- [ ] `UNKNOWN`

## Data shape and interoperability

<!-- Provide metadata and schema observations, not the restricted source payload. -->

| Field | Value |
|---|---|
| Record granularity | |
| Primary identifiers | |
| Geometry type / CRS | |
| Spatial resolution | |
| Temporal resolution | |
| Units and measurement standards | |
| Taxonomy / controlled vocabularies | |
| Null / missing-value conventions | |
| Quality flags | |
| Revision / deletion semantics | |
| Duplicate or merge behavior | |
| Upstream schema or data-dictionary version | |
| Expected transformations | |
| Domain extension needs | |
| Known joins or crosswalks | |
| Known ambiguity or loss risk | |

## Connector, watcher, and pipeline plan

<!-- Optional implementation proposal. Keep paths and behavior PROPOSED until verified. -->

| Step | Proposed artifact or action | Owning root | Dependency | Output | Reversible? | Status |
|---|---|---|---|---|---|---|
| 1 | Draft `SourceDescriptor` | `data/registry/sources/` or verified registry home | Identity and terms review | Candidate descriptor | Yes | `PROPOSED` |
| 2 | Rights / sensitivity / authority review | Governed review and policy homes | Descriptor draft | Review records / decisions | Yes | `PROPOSED` |
| 3 | Synthetic source-shaped fixture | Verified fixture root | Source schema documentation | No-network fixture | Yes | `PROPOSED` |
| 4 | Descriptor / record validator | `tools/validators/` plus tests | Contract and schema | Validation results | Yes | `PROPOSED` |
| 5 | Connector or intake adapter | `connectors/` | Activated descriptor and fixture | Candidate RAW capture only | Yes | `PROPOSED` |
| 6 | Dry run and receipt | `data/receipts/ingest/` or verified lane | Safe test plan | Run/ingest receipt | Yes | `PROPOSED` |
| 7 | Activation decision | Governed control/review lane | All gates | Allow/restrict/hold/deny decision | Yes | `PROPOSED` |

### Watcher-as-non-publisher checks

- [ ] Connector or watcher outputs only candidates, diagnostics, receipts, RAW captures, or quarantine entries.
- [ ] No connector, watcher, issue automation, or ordinary CI path writes directly to catalog, triplet, published, release, map, API, or AI authority.
- [ ] Public use remains downstream of evidence, validation, policy, review, release, correction, and rollback gates.
- [ ] Unknown or changed source posture fails closed.
- [ ] Live network access is explicitly activated and separately reviewed.
- [ ] `UNKNOWN`

## Fixtures, tests, and validation

### Fixture plan

- [ ] Minimal valid fixture
- [ ] Missing-identity fixture
- [ ] Invalid-rights or unresolved-terms fixture
- [ ] Sensitive or restricted fixture using synthetic/generalized data
- [ ] Source-role anti-collapse fixture
- [ ] Malformed / truncated / corrupt payload fixture
- [ ] Schema or version drift fixture
- [ ] Stale source-head / cadence fixture
- [ ] Duplicate / revision / deletion fixture
- [ ] Rate-limit / timeout / unavailable-source simulation
- [ ] No-network default test
- [ ] Other:
- [ ] `UNKNOWN`

### Validation gates

| Gate | Expected outcome | Evidence required | Status |
|---|---|---|---|
| Source identity | Stable source ID and collision check | Descriptor and registry search | `NOT RUN` |
| Descriptor shape | Current schema-required fields pass | Schema validation | `NOT RUN` |
| Source role | Role and limits are explicit; no upcast | Contract/policy/test evidence | `NOT RUN` |
| Rights and terms | Rights posture and obligations resolved | Rights review | `NOT RUN` |
| Sensitivity and sovereignty | Safe treatment or fail-closed decision | Policy/reviewer evidence | `NOT RUN` |
| Access and network | Access permitted; secrets excluded | Terms and security review | `NOT RUN` |
| Record minimum bar | Valid records pass; invalid records quarantine/deny | Positive/negative fixtures | `NOT RUN` |
| Freshness and source head | Drift and stale behavior are deterministic | Fixture and validation result | `NOT RUN` |
| Connector boundary | RAW/QUARANTINE only; no publication path | Boundary test / code review | `NOT RUN` |
| Receipts and provenance | Intake attempt and outputs are traceable | Receipt path and hash | `NOT RUN` |
| Documentation | Registry, source dossier, connector docs, and runbook updated as applicable | Paths or N/A rationale | `NOT RUN` |
| Rollback / disable | Connector and activation can be safely disabled | Rollback target and procedure | `NOT RUN` |

### Commands or checks already performed

```text
List only commands actually run and their exact outcomes.
```

## Directory Rules and placement

| Proposed or affected path | Owning responsibility root | Responsibility | Status | Directory Rules / ADR / local evidence basis |
|---|---|---|---|---|
| | | | `PROPOSED` | |

- [ ] Existing `data/registry/sources/` admission lane was checked.
- [ ] The documented sibling or compatibility relationship with any `source_descriptors/` lane was checked rather than assumed.
- [ ] Meaning stays in `contracts/`; machine shape stays in `schemas/`; allow/deny/restrict decisions stay in `policy/`.
- [ ] Source instances and registry entries stay in the governed registry root.
- [ ] Raw payloads stay in `data/raw/` or `data/quarantine/`, not the registry.
- [ ] Connectors live under `connectors/`; pipeline configuration and logic remain in their owning roots.
- [ ] Tests, fixtures, validators, receipts, proofs, and release artifacts remain separate.
- [ ] No new parallel source, descriptor, registry, schema, policy, proof, receipt, or release home is proposed without ADR or migration support.
- [ ] Placement remains `NEEDS VERIFICATION`.

## Activation, admission, and release outcomes

### Requested admission posture

These are requests for review, not decisions.

- [ ] Draft descriptor and continue evidence gathering
- [ ] Admit for fixture and internal validation only
- [ ] Activate internal-only connector use
- [ ] Admit as a public-release candidate, subject to all downstream gates
- [ ] Restrict to a named domain, purpose, geography, time, access tier, or claim role
- [ ] Hold for rights, sensitivity, sovereignty, consent, access, or security review
- [ ] Quarantine records pending resolution
- [ ] Deny admission
- [ ] Retire or supersede an existing descriptor
- [ ] Route to ADR before admission can proceed
- [ ] `UNKNOWN`

### Explicitly not authorized by this issue

- [ ] Live connector activation
- [ ] Credential provisioning
- [ ] RAW write
- [ ] Promotion to PROCESSED, CATALOG, or TRIPLET
- [ ] Public map, API, export, search, graph, or AI use
- [ ] Release or publication
- [ ] Silent descriptor mutation
- [ ] Source-role upgrade
- [ ] Rights, sensitivity, or consent override
- [ ] Other:

## Reviewers and separation of duties

| Role | Proposed reviewer / authority | Why required | Verified authority? | Independent from proposer? |
|---|---|---|---|---|
| Repository / governance steward | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Source steward | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Affected domain steward | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Rights / licensing reviewer | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Sensitivity / privacy / geoprivacy reviewer | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Community / sovereign / consent authority | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Security / infrastructure reviewer | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Contract / schema / validator reviewer | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |
| Release / correction authority | | | `No / Yes / UNKNOWN` | `No / Yes / UNKNOWN` |

- [ ] Required roles are identified.
- [ ] Repository ownership is not treated as rights-holder, community, sovereign, legal, or domain authority.
- [ ] Material author/approver separation is preserved.
- [ ] Missing reviewer identity or authority produces `HOLD`, `DENY`, or `NEEDS VERIFICATION`, not implicit approval.

## Acceptance criteria for admission readiness

A proposal is not ready merely because the source is useful or publicly reachable.

| Criterion | Expected outcome | Evidence required |
|---|---|---|
| Identity | Stable source identity, publisher, steward, version, and collision checks are resolved | Descriptor draft and registry search |
| Role and authority | Source role, authority, allowed/prohibited claim roles, and limitations are explicit | Contract-aligned descriptor and review |
| Rights and terms | License, attribution, redistribution, automation, caching, and purpose limits are resolved or fail closed | Rights assessment |
| Sensitivity and sovereignty | Sensitivity, consent, community authority, exact-location, and inference risks are reviewed | Policy/review record |
| Access | Approved method, authentication type, rate limits, and network posture are documented without secrets | Access/security review |
| Cadence and source head | Freshness, staleness, version, ETag/checksum/revision, and re-review triggers are deterministic | Descriptor and fixture evidence |
| Record-level bar | Minimum valid record and fail-closed conditions are testable | Valid and invalid fixtures |
| Connector boundary | Connector can fetch only within approved scope and cannot publish | Dry run, boundary test, and review |
| Quarantine | Invalid, ambiguous, restricted, stale, or changed material routes deterministically | Negative-path fixture and receipt |
| Provenance | Intake and every captured payload are traceable to descriptor, source head, run, and receipt | Receipt/provenance evidence |
| Citation and evidence | Downstream use preserves role, citation, and EvidenceBundle requirements | Citation/evidence test |
| Documentation | Registry entry, source dossier, connector docs, and operational guidance are updated or N/A | Paths and review |
| Disable / rollback | Activation can be disabled and prior descriptor state remains inspectable | Rollback target and procedure |
| No publication by admission | Admission and issue closure do not grant public use | Explicit review and downstream gate evidence |

## Related public-safe issues, PRs, docs, and records

<!-- Link only public-safe material. -->

-

## Maintainer triage

### Triage outcome

- [ ] `DUPLICATE_OR_ALREADY_REGISTERED`
- [ ] `NEEDS_MORE_INFORMATION`
- [ ] `NEEDS_DESCRIPTOR_DRAFT`
- [ ] `NEEDS_IDENTITY_OR_COLLISION_REVIEW`
- [ ] `NEEDS_SOURCE_ROLE_REVIEW`
- [ ] `NEEDS_RIGHTS_REVIEW`
- [ ] `NEEDS_SENSITIVITY_OR_SOVEREIGNTY_REVIEW`
- [ ] `NEEDS_ACCESS_OR_SECURITY_REVIEW`
- [ ] `NEEDS_FIXTURES_AND_VALIDATION`
- [ ] `NEEDS_CONNECTOR_DRY_RUN`
- [ ] `READY_FOR_ADMISSION_REVIEW`
- [ ] `INTERNAL_ONLY_CANDIDATE`
- [ ] `PUBLIC_CANDIDATE_SUBJECT_TO_DOWNSTREAM_GATES`
- [ ] `QUARANTINE_OR_HOLD`
- [ ] `DENY_ADMISSION`
- [ ] `ROUTE_TO_ADR`
- [ ] `NOT_ACTIONABLE_WITH_AVAILABLE_EVIDENCE`

### Required follow-up

- [ ] Source identity and registry collision check completed.
- [ ] Descriptor-level and record-level admission requirements separated.
- [ ] Current schema/contract vocabulary and documented conflicts reviewed.
- [ ] Rights, sensitivity, sovereignty, consent, and access reviews assigned.
- [ ] Fixture-before-connector requirement assigned.
- [ ] Source role, claim limits, citation, cadence, and source-head posture verified.
- [ ] Activation decision, quarantine reason codes, and disable/rollback path assigned.
- [ ] Closure links to the governed descriptor, activation decision, denial/hold rationale, connector PR, or explicit not-planned outcome.

## Submitter acknowledgements

- [ ] I understand this issue does not admit or activate the source.
- [ ] I understand a public source can still be restricted, unsuitable, stale, non-authoritative, or denied.
- [ ] I understand source role cannot be upgraded by AI, a connector, a map, or downstream promotion.
- [ ] I understand unresolved rights, sensitivity, consent, sovereignty, or access must fail closed.
- [ ] I understand fixtures and validation precede live connector activation.
- [ ] I understand admission does not authorize promotion, release, or publication.
- [ ] I understand issue closure does not prove admission, implementation, validation, or release.

---

<sub>Source admission is a governed pre-RAW state transition. An issue, label, assignment, automation, connector fetch, file copy, PR, merge, or closure is not admission or publication authority.</sub>
