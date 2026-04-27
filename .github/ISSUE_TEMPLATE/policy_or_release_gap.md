---
name: Policy or release gap
about: Report a missing, unclear, unsafe, or unverifiable KFM policy, promotion, publication, or release-control gap.
title: "[Policy/Release Gap]: "
labels: ""
assignees: ""
---

> [!CAUTION]
> Do **not** paste secrets, credentials, private endpoints, exact sensitive locations, living-person details, DNA/genomic details, unpublished source data, restricted archaeology records, rare-species coordinates, or private landowner exposure details into this issue. Use redacted references, internal artifact IDs, or steward-controlled links instead.

## Gap summary

**What is the gap?**

<!-- Briefly describe the policy, promotion, release, evidence, rights, sensitivity, rollback, or trust-state gap. -->

**Affected surface**

- Lane / domain:
- Repo path, artifact, layer, route, workflow, issue, PR, ADR, release, or doc:
- Public, semi-public, steward, admin, or internal surface:
- Current lifecycle state: `RAW` / `WORK` / `QUARANTINE` / `PROCESSED` / `CATALOG` / `TRIPLET` / `PUBLISHED` / `UNKNOWN`

**Gap type**

- [ ] Policy gate is missing, unclear, stale, or unenforced.
- [ ] Release or promotion state is missing, unclear, or unsupported.
- [ ] Rights, license, attribution, source terms, or redistribution posture is unresolved.
- [ ] Sensitivity, redaction, geoprivacy, access tier, or steward review is unresolved.
- [ ] EvidenceRef does not resolve to an EvidenceBundle.
- [ ] Citation, claim support, source role, or source authority is incomplete.
- [ ] Review state, reviewer role, or separation-of-duty expectation is unclear.
- [ ] ReleaseManifest, ProofPack, CatalogMatrix, PromotionDecision, or related proof object is missing.
- [ ] CorrectionNotice, RollbackPlan, withdrawal path, or supersession path is missing.
- [ ] Public client, UI, map layer, Focus Mode, Evidence Drawer, export, or API can see something it should not.
- [ ] RAW, WORK, QUARANTINE, unpublished candidate, direct model output, or canonical/internal store may be exposed.
- [ ] Other:

## Safe default requested

Until this is closed, the safest default should be:

- [ ] `DENY` publication or public/semi-public exposure.
- [ ] `ABSTAIN` from making the claim until evidence or policy is resolved.
- [ ] `ERROR` because a required validator, resolver, proof object, or workflow failed.
- [ ] Keep the material in `WORK`.
- [ ] Move or keep the material in `QUARANTINE`.
- [ ] Redact, generalize, delay, or stage access.
- [ ] Repoint to a prior release or withdraw a published surface.
- [ ] Other:

## Evidence and source role

**Known EvidenceRef / EvidenceBundle / SourceDescriptor references**

<!-- Use IDs or redacted links. Do not paste restricted content. -->

- EvidenceRef:
- EvidenceBundle:
- SourceDescriptor / source ID:
- DatasetVersion / release candidate:
- Catalog / triplet / graph reference:
- RunReceipt / ValidationReport:
- PolicyDecision / DecisionEnvelope:

**Source role involved**

- [ ] Authoritative / steward source.
- [ ] Direct observation or measurement.
- [ ] Statutory, regulatory, legal, or administrative record.
- [ ] Operational context feed.
- [ ] Documentary or archival evidence.
- [ ] Modeled, assimilated, inferred, interpolated, or derived surface.
- [ ] Discovery mirror, index, aggregator, or convenience source.
- [ ] Community / volunteered / contributed source.
- [ ] Generated summary, AI output, search index, vector index, tile, scene, or other derivative.
- [ ] Unknown source role.

**What is missing or questionable?**

- [ ] Source role is unknown or overstated.
- [ ] Rights or redistribution terms are unknown.
- [ ] Evidence is stale, unavailable, incomplete, or unresolved.
- [ ] Citation does not support the claim.
- [ ] Claim scope is broader than the evidence supports.
- [ ] Temporal basis, update cadence, freshness, or valid time is unclear.
- [ ] Spatial support, CRS, precision, uncertainty, or geometry transform is unclear.
- [ ] Observation, model, regulatory status, interpretation, and public representation may be collapsed.

## Rights, sensitivity, and public-safety review

**Potential sensitivity classes**

- [ ] Archaeology, sacred site, burial, cultural heritage, or steward-controlled location.
- [ ] Rare species, habitat, nest, den, roost, hibernacula, spawning, or exact occurrence location.
- [ ] Living person, genealogy, private family record, DNA, genomics, or reidentification risk.
- [ ] Private landowner, parcel, assessor, tax, title, or tenure exposure.
- [ ] Critical infrastructure, facility, route, restriction, emergency, or operational-security exposure.
- [ ] Hazards, warning, advisory, or life-safety-adjacent content.
- [ ] Source terms, license, attribution, or redistribution uncertainty.
- [ ] Credentials, private endpoint, local-host exposure, VPN, reverse proxy, or firewall boundary.
- [ ] Other:

**Public-safe transform likely needed**

- [ ] No transform needed; evidence and policy support public release.
- [ ] Redaction.
- [ ] Generalization.
- [ ] Obfuscation / precision reduction.
- [ ] Delayed publication.
- [ ] Staged access.
- [ ] Steward-only or restricted access.
- [ ] Public denial / no public surface.
- [ ] Unknown.

## Release and promotion gap

**Current publication state**

- [ ] Not published.
- [ ] Candidate only.
- [ ] Published internally.
- [ ] Published to trusted third parties.
- [ ] Publicly visible.
- [ ] Unknown.

**Required proof objects or gates**

- [ ] SourceDescriptor complete.
- [ ] SourceIntakeRecord or source admission note complete.
- [ ] IngestReceipt present.
- [ ] ValidationReport present, including failure/quarantine cases.
- [ ] EvidenceBundle resolves and supports the claim.
- [ ] PolicyDecision or DecisionEnvelope present.
- [ ] Rights and sensitivity posture recorded.
- [ ] ReviewRecord present where required.
- [ ] RedactionReceipt or transform receipt present where required.
- [ ] CatalogMatrix / STAC / DCAT / PROV closure present where required.
- [ ] ReleaseManifest present.
- [ ] ProofPack or release proof present.
- [ ] PromotionDecision present.
- [ ] RuntimeResponseEnvelope has finite outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
- [ ] CorrectionNotice, RollbackPlan, or withdrawal path present where required.
- [ ] Public UI, map layer, Evidence Drawer, Focus Mode, export, or API shows trust state and negative state correctly.

## Reproduction or review steps

<!-- Give the smallest safe way to observe the gap. Avoid live-source calls unless they are approved and necessary. -->

1.
2.
3.

**Observed behavior**

<!-- What happened? -->

**Expected governed behavior**

<!-- What should happen under KFM invariants? -->

## Impact

**Who or what could be affected?**

- [ ] Public user.
- [ ] Trusted third-party user.
- [ ] Steward / reviewer.
- [ ] Contributor / maintainer.
- [ ] Source partner.
- [ ] Domain lane:
- [ ] Release artifact / published layer:
- [ ] AI / Focus Mode / Evidence Drawer response:
- [ ] Other:

**Impact level**

- [ ] `P0` — Active or likely unsafe public/semi-public exposure; release should be blocked, withdrawn, or rolled back.
- [ ] `P1` — Trust-critical gate missing before intended release; release must not proceed until fixed.
- [ ] `P2` — Governance gap with bounded internal impact; fix before promotion or broad reuse.
- [ ] `P3` — Documentation, clarity, or follow-up gap; no immediate release risk known.
- [ ] Unknown.

## Proposed closure criteria

This issue can close only when:

- [ ] The affected claim, artifact, layer, route, workflow, release, or document is identified.
- [ ] The relevant source role and evidence basis are recorded.
- [ ] EvidenceRef resolves to EvidenceBundle, or the workflow explicitly abstains.
- [ ] Rights and sensitivity posture are recorded.
- [ ] Required policy decision is present and finite.
- [ ] Required review state is present or the issue records why review is not required.
- [ ] Release and promotion state is unambiguous.
- [ ] Public/semi-public surface is denied, redacted, generalized, corrected, rolled back, or safely promoted.
- [ ] Negative-path behavior is tested where the risk is trust-critical.
- [ ] Correction, rollback, or withdrawal path is documented if the issue affected an already published surface.
- [ ] Documentation, schema, policy, validator, fixture, or workflow updates are linked if behavior changed.

## Validation plan

**Tests or checks expected**

- [ ] Schema validation.
- [ ] Policy test.
- [ ] Validator test.
- [ ] Negative fixture.
- [ ] No-network dry run.
- [ ] Citation validation.
- [ ] EvidenceBundle resolution test.
- [ ] Rights/sensitivity deny test.
- [ ] No public RAW / WORK / QUARANTINE access test.
- [ ] No direct model-client bypass test.
- [ ] Release dry run.
- [ ] Rollback or correction rehearsal.
- [ ] Manual steward review.
- [ ] Other:

**Validation notes**

<!-- Include command names only if they are already repo-supported or clearly marked as proposed. -->

## Rollback, correction, or withdrawal

If a release or public/semi-public surface is already affected:

- Affected release / artifact / layer / route:
- Current alias or public pointer:
- Prior safe release or rollback target:
- Required CorrectionNotice:
- Required public note:
- Required cache / tile / search / graph / vector / scene rebuild:
- Required steward or maintainer approval:

## Maintainer triage

<!-- Maintainers fill this section. -->

**Triage determination**

- [ ] Confirmed policy or release gap.
- [ ] Needs more evidence.
- [ ] Needs source-rights verification.
- [ ] Needs sensitivity or steward review.
- [ ] Needs schema / contract work.
- [ ] Needs validator / policy / fixture work.
- [ ] Needs release rollback, correction, or withdrawal.
- [ ] Not a policy or release gap.
- [ ] Duplicate of:

**Decision**

- [ ] `DENY`
- [ ] `ABSTAIN`
- [ ] `ERROR`
- [ ] Proceed after required closure criteria are met.
- [ ] Other:

**Owner / reviewer placeholders**

- Owner:
- Reviewer:
- Steward:
- Policy reviewer:
- Release reviewer:
- Related PR:
- Related ADR:
