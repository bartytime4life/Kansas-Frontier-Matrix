---
name: Evidence correction request
about: Report a public or semi-public KFM claim, release, layer, artifact, or AI answer that may need governed correction.
title: "[Correction]: "
labels: []
assignees: ["bartytime4life"]
---

<!--
KFM public evidence-correction intake template.

This issue is a correction candidate and routing record. Filing it does not
confirm that the published object is wrong, create a CorrectionNotice, change
release state, approve rollback, decide policy, authorize publication, or prove
that a correction is complete.

Before submitting:
1. Identify the affected claim, release, layer, artifact, answer, or public URL.
2. Distinguish "stale" from "wrong" when possible.
3. Preserve the existing public record; do not silently edit or replace it.
4. Provide public-safe evidence pointers, not restricted evidence payloads.
5. Redact secrets, private data, exact sensitive locations, unreleased lifecycle
   data, and source-restricted material.
6. Use the private-first path in SECURITY.md if the issue involves an active
   vulnerability, sensitive exposure, exploit detail, or unsafe exact location.

Use UNKNOWN or NEEDS VERIFICATION rather than guessing.
-->

> [!IMPORTANT]
> A correction request is not the correction itself. The governed correction record, evidence, review, policy decision, release manifest, supersession or withdrawal record, and rollback target live in their owning roots.

> [!CAUTION]
> Do not post credentials, tokens, private endpoints, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person records, DNA/genomic material, private-land details, restricted source payloads, or unreleased `RAW` / `WORK` / `QUARANTINE` data. Route security-sensitive material through `SECURITY.md`.

## Summary

<!-- What public or semi-public statement, artifact, layer, answer, or release appears to need correction, and why? -->

-

## Reporter preflight

- [ ] I searched existing issues, correction notices, releases, and related PRs for a duplicate.
- [ ] I identified the affected public object, release, or URL, or marked it `UNKNOWN`.
- [ ] I distinguished stale context from substantively wrong or unsupported content, or marked the distinction `NEEDS VERIFICATION`.
- [ ] I preserved public-safe links or identifiers instead of copying restricted evidence into this issue.
- [ ] I removed or generalized secrets, personal data, restricted content, and exact sensitive locations.
- [ ] This report is safe for a public issue. Security-sensitive details have been routed privately.
- [ ] I understand that filing or closing this issue does not create or approve a correction.

## Current truth posture

<!-- Apply labels per material claim. A correction candidate may contain claims with different support. -->

- [ ] `CONFIRMED` — verified from current repository evidence, source records, tests, logs, or governed artifacts.
- [ ] `PROPOSED` — suggested correction, explanation, or release response under review.
- [ ] `NEEDS VERIFICATION` — checkable, but not checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and unsafe to assume.

**Reporter-selected posture:** `NEEDS VERIFICATION`

## Affected claim or release

| Field | Value |
|---|---|
| Claim ID | `UNKNOWN` |
| Release ID / ReleaseManifest | `UNKNOWN` |
| Layer / dataset / artifact ID | `UNKNOWN` |
| Catalog / triplet / graph object | `UNKNOWN` |
| AI answer / RuntimeResponseEnvelope / receipt | `UNKNOWN` |
| Public URL, route, map view, export, or document | `UNKNOWN` |
| Domain / feature family | `UNKNOWN` |
| Current release or review state | `UNKNOWN` |
| Current `spec_hash`, digest, version, or commit | `UNKNOWN` |
| First observed date/time | `UNKNOWN` |

## Correction classification

### Stale versus wrong

- [ ] **Stale** — the content may have been supportable when released, but freshness, review, source, policy, model, geography, or time context has aged.
- [ ] **Wrong / unsupported** — the substance is incorrect, no longer supported, or violates rights, sensitivity, policy, or release requirements.
- [ ] **Both**
- [ ] `NEEDS VERIFICATION`
- [ ] `UNKNOWN`

### Defect or correction class

Check all that apply.

- [ ] Evidence gap or unresolved `EvidenceRef`
- [ ] Evidence no longer supports the published claim
- [ ] Source-role misclassification
- [ ] Source update or source-version mismatch
- [ ] Rights, license, attribution, consent, or sovereignty change
- [ ] Sensitivity, geoprivacy, or restricted-location exposure
- [ ] Geometry, CRS, topology, scale, or generalization defect
- [ ] Observation, valid, source, retrieval, processing, or release-time defect
- [ ] Policy or admissibility defect
- [ ] Validation, review, proof, receipt, or digest defect
- [ ] Rendering, style, tile, popup, Evidence Drawer, or export defect
- [ ] Governed API, catalog, graph, search, or route defect
- [ ] Focus Mode, AI answer, model adapter, or runtime-envelope defect
- [ ] Catalog closure, manifest, alias, or release-lineage defect
- [ ] Clarification only; no release-state change expected
- [ ] Other:

## What appears wrong

<!-- Describe the observed problem without overstating what is proven. -->

-

## Current published statement or behavior

<!-- Quote only the smallest necessary public-safe excerpt, or link to the affected object. -->

-

## Proposed corrected statement or posture

<!-- Examples: corrected claim, narrower scope, stale marker, caveat, ABSTAIN, DENY, redaction, generalization, supersession, withdrawal, or rollback review. Mark this PROPOSED. -->

**Status:** `PROPOSED`

-

## Evidence basis

<!-- EvidenceBundle outranks generated summaries. Use immutable paths, IDs, hashes, source versions, or public-safe authoritative links. -->

| Evidence role | Identifier or location | Observation supported | Resolution / validation state | Limitation |
|---|---|---|---|---|
| Existing published evidence | | | | |
| New or corrected evidence | | | | |
| Corroborating evidence | | | | |
| Contextual evidence | | | | |
| Conflicting evidence | | | | |

### Evidence and source objects

| Field | Value |
|---|---|
| `SourceDescriptor` / source ID | `UNKNOWN` |
| Source role | `primary / corroborating / contextual / restricted / modeled / aggregate / synthetic / UNKNOWN` |
| Source version / retrieval time | `UNKNOWN` |
| `EvidenceRef` | `UNKNOWN` |
| Resolved `EvidenceBundle` | `UNKNOWN` |
| Citation or provenance record | `UNKNOWN` |
| Validation report / proof pack | `UNKNOWN` |
| ReviewRecord | `UNKNOWN` |
| PolicyDecision | `UNKNOWN` |
| Generated receipt / run receipt | `UNKNOWN` |

- [ ] Every evidence-dependent claim resolves from `EvidenceRef` to an inspectable `EvidenceBundle`.
- [ ] Source roles remain distinct; modeled, aggregate, synthetic, administrative, or contextual material is not upcast.
- [ ] Conflicting or missing evidence is visible.
- [ ] Rights and sensitivity metadata are current.
- [ ] Evidence cannot be safely posted publicly; a restricted review path is identified.

## Verification and reproduction

<!-- Explain how a reviewer can verify the concern using public-safe inputs. -->

### Minimal verification steps

1.
2.
3.

```bash
# Optional safe, redacted commands.
```

### Expected result

-

### Observed result

-

### Verification already attempted

- [ ] Confirmed against the named published release or artifact.
- [ ] Re-resolved the cited evidence bundle.
- [ ] Compared source versions or retrieval timestamps.
- [ ] Re-ran relevant schema or contract validation.
- [ ] Re-ran policy or sensitivity checks.
- [ ] Re-ran positive and negative fixtures.
- [ ] Compared current and prior release manifests or digests.
- [ ] Checked map, UI, export, API, graph, search, and AI derivatives.
- [ ] No verification performed yet.
- [ ] `UNKNOWN`

## Spatial and temporal scope

> [!WARNING]
> Generalize locations involving archaeology, burial or sacred sites, rare species or plants, habitat, critical infrastructure, private land, living people, DNA/genomics, or steward-controlled records. Reference the restricted evidence path rather than posting exact details.

| Field | Value |
|---|---|
| Generalized geographic area | `UNKNOWN` |
| Geometry type / CRS / scale | `UNKNOWN` |
| Exact sensitive geometry involved? | `No / Yes / UNKNOWN` |
| Observation / valid time | `UNKNOWN` |
| Source publication / retrieval time | `UNKNOWN` |
| Processing / ingest time | `UNKNOWN` |
| Release time | `UNKNOWN` |
| Freshness tolerance or review cycle | `UNKNOWN` |
| Stale or future-dated context suspected? | `No / Yes / UNKNOWN` |

## Scope and derivative impact

Check every affected surface.

- [ ] Published claim or narrative
- [ ] ReleaseManifest or current release alias
- [ ] Data layer, tile set, map style, popup, or Evidence Drawer
- [ ] Catalog, triplet, graph, search index, or source registry
- [ ] Governed API response or export
- [ ] Focus Mode or public AI answer
- [ ] Documentation, story, report, or public summary
- [ ] Proof, receipt, validation report, or signed artifact
- [ ] Downstream package, pipeline, connector, or application
- [ ] No confirmed derivative impact
- [ ] `UNKNOWN`

### Known derivatives and dependents

| Dependent object or surface | Current exposure | Required action | Owner / reviewer | Status |
|---|---|---|---|---|
| | | | | |

## Trust, policy, rights, and sensitivity impact

- [ ] Could expose sensitive or restricted material.
- [ ] Could expose unreleased `RAW`, `WORK`, `QUARANTINE`, candidate, or internal data.
- [ ] Could bypass the governed API or trust membrane.
- [ ] Could make an unsupported or uncited claim appear authoritative.
- [ ] Could collapse source roles or confuse derived output with canonical truth.
- [ ] Could affect licensing, attribution, consent, redistribution rights, or sovereignty.
- [ ] Could require immediate public disablement or access restriction.
- [ ] Could require redaction, generalization, delayed access, or restricted review.
- [ ] Could require public correction, supersession, withdrawal, rollback, or release hold.
- [ ] No known trust, policy, rights, sensitivity, or release impact.
- [ ] `UNKNOWN`

**Impact explanation:**

-

## Immediate containment or public-surface action

<!-- Use only safe, reversible actions. A public issue must not contain exploit or sensitive implementation detail. -->

- [ ] No immediate containment appears necessary.
- [ ] Add a visible stale or review-pending marker.
- [ ] Disable or restrict an affected route, layer, export, answer, or alias pending review.
- [ ] Remove an unsafe answer while preserving its evidence and receipt trail.
- [ ] Hold release, promotion, or publication.
- [ ] Withdraw or roll back to a previously reviewed target.
- [ ] Private security or incident handling is required.
- [ ] `NEEDS VERIFICATION`

**Suggested containment and rollback target:**

-

## Suggested correction lineage

<!-- These are requested follow-up artifacts, not approvals. -->

- [ ] `CorrectionNotice`
- [ ] `SupersessionNotice`
- [ ] `WithdrawalNotice`
- [ ] `RollbackCard`
- [ ] Superseding `ReleaseManifest`
- [ ] Stale-state marker only
- [ ] Policy hold or review hold
- [ ] Redaction or generalization receipt
- [ ] Corrected EvidenceBundle / citation lineage
- [ ] Corrected validation report / proof pack
- [ ] Changelog or public notice
- [ ] No release-facing notice after review
- [ ] Other:

### Existing and proposed lineage

| Relationship | Current pointer | Proposed pointer | Status |
|---|---|---|---|
| Affected release / object | | | |
| Supersedes | | | |
| Superseded by | | | |
| Rollback target | | | |
| Correction notice | | | |
| Withdrawal notice | | | |
| Public notice / changelog | | | |

## Public-safe correction summary

<!-- Draft only. Do not include restricted evidence or exact sensitive details. -->

**Status:** `PROPOSED`

-

## Review and separation of duties

| Role | Proposed reviewer / owner | Required because | Independent from detector/author? |
|---|---|---|---|
| Affected domain or subsystem steward | | | |
| Evidence / source reviewer | | | |
| Correction reviewer | | | |
| Policy / rights / sensitivity reviewer | | | |
| Release authority | | | |
| Docs / public-notice reviewer | | | |
| AI surface steward, when applicable | | | |

- [ ] Detector / author is identified.
- [ ] Required reviewer roles are identified.
- [ ] Material author/approver separation is preserved.
- [ ] Missing reviewer authority produces `HOLD` / `NEEDS VERIFICATION`, not implicit approval.

## Validation and acceptance criteria

<!-- Correction is not complete merely because public wording changes. -->

| Criterion | Expected outcome | Evidence required |
|---|---|---|
| Affected object identity | Exact claim, release, layer, artifact, or answer is named | Stable ID, path, URL, or manifest pointer |
| Evidence support | Corrected posture is supported, or the system abstains/denies | Resolved evidence and source-role review |
| Prior record preservation | Original release and correction history remain inspectable | Supersession/correction lineage |
| Policy and sensitivity | Rights, sensitivity, sovereignty, and public-safe posture pass | PolicyDecision / review evidence |
| Derivative closure | Known maps, exports, APIs, search, graph, catalog, and AI derivatives are reviewed | Impact inventory and validation |
| Release state | Correction, withdrawal, supersession, or rollback is governed | ReleaseManifest / RollbackCard / decision |
| Public communication | Public-safe correction or notice is linked when required | Approved notice or no-notice decision |
| Regression protection | The defect is detectable in future | Test, fixture, validator, or monitoring evidence |
| Rollback | A clear reversal or last-known-good target exists | Commit, manifest, digest, artifact, or alias |
| Documentation | Behavior-changing guidance is updated or explicitly not applicable | Changed path or rationale |

### Acceptance outcome

- [ ] `PASS`
- [ ] `FAIL`
- [ ] `PARTIAL`
- [ ] `NOT RUN`
- [ ] `NOT APPLICABLE`
- [ ] `UNKNOWN`

## Related issues, PRs, records, runs, or artifacts

<!-- Link only public-safe material. -->

-

## Maintainer triage

### Classification

- [ ] Duplicate
- [ ] Correction candidate reproduced and `CONFIRMED`
- [ ] Stale only; route to freshness/review handling
- [ ] `NEEDS VERIFICATION`
- [ ] Existing publication is supportable; no correction required
- [ ] Security-sensitive; move details to private handling
- [ ] Rights, sensitivity, sovereignty, or consent review required
- [ ] Immediate containment or release hold required
- [ ] CorrectionNotice required
- [ ] Supersession or withdrawal required
- [ ] Rollback review required
- [ ] Drift or verification-register entry required

### Required follow-up

- [ ] Affected object, release, owner, and responsibility root are identified.
- [ ] Evidence, source role, and truth labels are recorded per material claim.
- [ ] Stale-versus-wrong classification is recorded.
- [ ] Derivative impact and public exposure are reviewed.
- [ ] Required correction, release, policy, review, proof, and rollback artifacts are linked.
- [ ] Public-safe notice or no-notice decision is recorded.
- [ ] Closure links to the governed correction outcome or explicit no-action rationale.

## Submitter acknowledgements

- [ ] I understand this issue is a correction request, not a `CorrectionNotice`, release decision, or rollback authorization.
- [ ] I have not asked maintainers to silently overwrite published history.
- [ ] I have used public-safe evidence pointers and generalized restricted details.
- [ ] I have marked inferences and unknowns instead of presenting them as confirmed facts.
- [ ] I understand issue closure is administrative state and does not prove correction completion.

---

<sub>Correction is a governed, append-only, reviewable state transition. Issue intake does not replace evidence, policy, review, release, correction, supersession, withdrawal, or rollback artifacts.</sub>
