---
name: Bug report
about: Report a reproducible KFM defect with evidence, scope, impact, and safe redaction.
title: "[Bug]: "
labels: []
assignees: ["bartytime4life"]
---

<!--
KFM public bug-intake template.

This issue is a work-intake record. Filing it does not confirm the defect,
establish evidence authority, decide policy, approve a correction, authorize a
release, or prove that remediation is complete.

Before submitting:
1. Search open and closed issues for a duplicate.
2. Reproduce against a named commit, release, or artifact when practical.
3. Minimize the reproduction and remove unrelated data.
4. Redact secrets, private endpoints, personal data, restricted source payloads,
   exact sensitive locations, and unreleased RAW/WORK/QUARANTINE material.
5. Use the private-first reporting path in SECURITY.md for a security-sensitive
   vulnerability or exposure risk.

Use UNKNOWN or NEEDS VERIFICATION rather than guessing.
-->

> [!IMPORTANT]
> A public bug report is an allegation and routing record until maintainers reproduce or otherwise verify it. Labels, assignment, comments, automation, and issue closure do not by themselves prove a defect, correction, release, or rollback.

> [!CAUTION]
> Do not post credentials, tokens, private endpoints, exploit details, exact rare-species or archaeology locations, critical-infrastructure vulnerability details, living-person records, DNA/genomic material, private-land details, restricted source payloads, or unreleased `RAW` / `WORK` / `QUARANTINE` data. Route security-sensitive material through `SECURITY.md`.

## Summary

<!-- One or two sentences: what appears broken, where, and with what visible effect? -->

-

## Reporter preflight

- [ ] I searched existing issues and did not find a clear duplicate.
- [ ] I identified the commit, release, artifact, or environment involved, or marked it `UNKNOWN`.
- [ ] I provided deterministic reproduction steps, or explained why reproduction is intermittent.
- [ ] I removed or redacted secrets, private data, restricted content, and exact sensitive locations.
- [ ] This report is safe for a public issue. Security-sensitive details have been routed privately.
- [ ] I understand that filing this issue does not confirm the defect or authorize a fix, release, correction, or publication action.

## Current truth posture

<!-- Apply the strongest support available. A report may contain claims with different labels. -->

- [ ] `CONFIRMED` — directly reproduced or verified from current evidence.
- [ ] `PROPOSED` — suspected explanation, fix, or design response.
- [ ] `NEEDS VERIFICATION` — checkable, but not yet checked strongly enough to act as fact.
- [ ] `UNKNOWN` — unresolved and unsafe to assume.

**Reporter-selected posture:** `NEEDS VERIFICATION`

## Affected KFM surface

Check all that apply.

- [ ] Documentation, README, ADR, issue template, or runbook
- [ ] Repository path, package boundary, import, or build configuration
- [ ] Source intake, connector, `SourceDescriptor`, or source registry
- [ ] Pipeline, transform, normalization, or lifecycle promotion
- [ ] `RAW` / `WORK` / `QUARANTINE` / `PROCESSED` / `CATALOG` / `TRIPLET` / `PUBLISHED`
- [ ] Contract, schema, DTO, context, or fixture
- [ ] Validator, test, policy gate, review gate, or promotion gate
- [ ] `EvidenceRef`, `EvidenceBundle`, citation, provenance, or lineage
- [ ] Catalog, graph, search, triplet, receipt, proof, or manifest
- [ ] Governed API, authentication, authorization, or trust membrane
- [ ] Explorer, MapLibre, layer, popup, Evidence Drawer, or export
- [ ] Focus Mode, governed AI, model adapter, or runtime response envelope
- [ ] CI, GitHub workflow, automation, dependency, or generated artifact
- [ ] Release, publication, correction, withdrawal, or rollback
- [ ] Other:

## Repository and runtime context

<!-- Fill in what you can. Use UNKNOWN instead of guessing. -->

| Field | Value |
|---|---|
| Repository branch | `UNKNOWN` |
| Commit SHA | `UNKNOWN` |
| Release / artifact / manifest ID | `UNKNOWN` |
| File path(s), package(s), or component(s) | `UNKNOWN` |
| Command, route, workflow, or UI entrypoint | `UNKNOWN` |
| Runtime / package / browser versions | `UNKNOWN` |
| OS / architecture | `UNKNOWN` |
| Local, CI, staging, or published surface | `UNKNOWN` |
| Configuration or feature flags | `UNKNOWN` |
| First known affected version | `UNKNOWN` |
| Last known good version | `UNKNOWN` |

## Reproducibility

- [ ] Always
- [ ] Often
- [ ] Sometimes
- [ ] Rarely
- [ ] Observed once
- [ ] Cannot reproduce locally
- [ ] `UNKNOWN`

**Reproduction frequency / conditions:**

-

## Minimal steps to reproduce

<!--
Keep the sequence deterministic and bounded. Prefer synthetic, public-safe input.
Do not include commands that access restricted systems or real sensitive data.
-->

1.
2.
3.

```bash
# Optional safe, redacted commands.
```

### Minimal reproduction input

<!--
Link a small public-safe fixture, synthetic example, stable source ID, or content
hash. Do not upload large binaries, restricted data, or real sensitive records.
-->

- Fixture or example path:
- Public-safe source or dataset reference:
- Object / feature / layer / claim ID:
- Content hash, run ID, or workflow URL:
- Why this is the minimum sufficient input:

## Expected behavior

<!--
State the contract, schema, policy, doctrine, test, UI behavior, or release
expectation that should hold. Cite a repository path or accepted decision when available.
-->

-

## Actual behavior

<!-- State exactly what happened. Include exact error text only after redaction. -->

-

## Regression and change history

- [ ] This worked previously.
- [ ] This appears to be a regression.
- [ ] This has never worked in the tested environment.
- [ ] Behavior changed after a dependency, configuration, data, policy, or release update.
- [ ] `UNKNOWN`

| Field | Value |
|---|---|
| Suspected first bad commit / release | `UNKNOWN` |
| Last known good commit / release | `UNKNOWN` |
| Bisect or comparison performed | `No / Yes / UNKNOWN` |
| Related migration / ADR / dependency update | `UNKNOWN` |
| Date and time first observed | `UNKNOWN` |

**Comparison notes:**

-

## Evidence, source, and claim context

<!-- Complete when the bug affects a claim, source, citation, map layer, or released artifact. -->

| Field | Value |
|---|---|
| Public or semi-public claim affected? | `No / Yes / UNKNOWN` |
| Claim, object, feature, layer, or release ID | `UNKNOWN` |
| Source ID / `SourceDescriptor` | `UNKNOWN` |
| Source role | `UNKNOWN` |
| `EvidenceRef` | `UNKNOWN` |
| Resolved `EvidenceBundle` | `UNKNOWN` |
| Receipt / proof / validation report | `UNKNOWN` |
| Citation or authoritative source | `UNKNOWN` |
| Review state | `UNKNOWN` |
| Policy decision / sensitivity tier | `UNKNOWN` |
| Release state | `UNKNOWN` |
| Correction / withdrawal / rollback target | `UNKNOWN` |

**Evidence limitation:**

-

## Spatial and temporal context

> [!WARNING]
> Generalize locations involving archaeology, burial or sacred sites, rare species or plants, habitat, critical infrastructure, private land, living people, DNA/genomics, or steward-controlled records. Reference the private evidence path instead of posting exact details.

| Field | Value |
|---|---|
| Generalized geographic area | `UNKNOWN` |
| Geometry type / CRS / zoom or scale | `UNKNOWN` |
| Exact sensitive geometry involved? | `No / Yes / UNKNOWN` |
| Observation / valid time | `UNKNOWN` |
| Source publication / retrieval time | `UNKNOWN` |
| Processing / ingest time | `UNKNOWN` |
| Release time | `UNKNOWN` |
| Stale, expired, or future-dated context suspected? | `No / Yes / UNKNOWN` |

## Trust, policy, rights, and sensitivity impact

Check all that apply.

- [ ] Could expose sensitive or restricted material.
- [ ] Could expose unreleased `RAW`, `WORK`, `QUARANTINE`, candidate, or internal data.
- [ ] Could bypass the governed API or trust membrane.
- [ ] Could bypass identity, rights, sensitivity, evidence, review, policy, or release gates.
- [ ] Could let a watcher, workflow, intake job, or model act as a publisher.
- [ ] Could make an uncited or unsupported claim appear authoritative.
- [ ] Could confuse a derived map, tile, graph, search result, summary, or AI response with canonical truth.
- [ ] Could break deterministic identity, canonicalization, provenance, receipt, or proof linkage.
- [ ] Could affect licensing, attribution, redistribution rights, source terms, or sovereignty.
- [ ] Could require a correction notice, withdrawal, rollback, public erratum, or release hold.
- [ ] No known trust, policy, rights, sensitivity, or release impact.
- [ ] `UNKNOWN`

**Impact explanation:**

-

## Logs, screenshots, traces, and artifacts

<!--
Paste only the smallest relevant, redacted excerpt. Crop or blur private paths,
tokens, endpoint details, user data, exact sensitive locations, and steward-only
content. Prefer links to public-safe runs or artifacts over large pasted output.
-->

<details>
<summary>Safe, redacted output</summary>

```text
Paste the smallest relevant excerpt here.
```

</details>

- Screenshot / recording:
- CI or workflow run:
- Request / trace / run ID:
- Generated artifact or receipt:
- Redactions applied:

## Severity and user impact

Select the closest fit.

- [ ] `S0 — Critical`: active sensitive exposure, data loss, trust-membrane bypass, or unsafe publication. **Do not post sensitive details publicly.**
- [ ] `S1 — High`: blocks build, test, promotion, release, correction, or a major public/governed surface; no safe workaround.
- [ ] `S2 — Medium`: material behavior is wrong or partially unavailable; a bounded workaround exists.
- [ ] `S3 — Low`: limited edge case, documentation defect, cosmetic issue, or low-risk usability problem.
- [ ] `UNKNOWN`

**Who or what is affected:**

-

**Frequency / scale / blast radius:**

-

## Workaround or containment

<!-- Describe only safe, reversible steps. Do not normalize a governance bypass as a workaround. -->

- Workaround:
- Containment or feature-disable option:
- Side effects:
- Safe to use in production/public surfaces? `No / Yes / UNKNOWN`

## Validation already attempted

- [ ] Reproduced on the default branch or named release.
- [ ] Reproduced locally.
- [ ] Reproduced in CI or workflow output.
- [ ] Reduced to a minimal public-safe fixture.
- [ ] Checked relevant contract and schema.
- [ ] Checked relevant policy, sensitivity, rights, or release rule.
- [ ] Checked relevant validator, positive fixture, and negative fixture.
- [ ] Checked documentation, README, ADR, migration, or runbook.
- [ ] Checked the affected receipt, proof, catalog, manifest, correction, or rollback record.
- [ ] Compared with the last known good commit, release, or artifact.
- [ ] No validation performed yet.
- [ ] `UNKNOWN`

```bash
# Optional safe, redacted validation commands and outcomes.
```

## Suspected cause or hypothesis

<!-- Optional. Label inference as PROPOSED and do not present it as the verified cause. -->

**Status:** `PROPOSED`

-

## Suggested fix and regression protection

<!-- Optional. Prefer the smallest reversible change that restores the governed boundary. -->

- Proposed fix:
- Affected file(s) or responsibility root(s):
- Contract / schema / policy implications:
- Positive-path test:
- Negative-path test:
- Fixture or synthetic reproduction:
- Documentation / runbook update:
- Generated receipt or proof needed:
- Correction / withdrawal / rollback needed:

## Acceptance criteria

<!-- A fix is not complete merely because the symptom disappears. -->

| Criterion | Expected outcome | Evidence required |
|---|---|---|
| Reproduction | Original minimal reproduction no longer fails | Test or deterministic command |
| Regression protection | A test or fixture fails before the fix and passes after it | Test/fixture path and result |
| Governance boundary | No policy, rights, sensitivity, evidence, release, or trust control is weakened | Review and validation evidence |
| Public-surface safety | No unreleased, sensitive, unsupported, or direct-runtime output reaches public clients | Negative-path proof where applicable |
| Documentation | Behavior-changing guidance is updated or explicitly not applicable | Changed path or rationale |
| Rollback | The change has a clear reversal target | Commit, config, artifact, or release target |

## Related issues, PRs, docs, runs, or artifacts

<!-- Link only public-safe material. -->

-

## Maintainer triage

<!-- Maintainers may update this section after review. -->

### Classification

- [ ] Duplicate
- [ ] Reproduced and `CONFIRMED`
- [ ] `NEEDS VERIFICATION`
- [ ] Cannot reproduce with available evidence
- [ ] Expected behavior / documentation clarification
- [ ] Feature or architecture request; route to the appropriate process
- [ ] Security-sensitive; move details to private handling
- [ ] Rights / sensitivity / sovereignty review required
- [ ] Drift or verification-register entry required
- [ ] Correction / withdrawal / rollback review required

### Required follow-up

- [ ] Owner and affected responsibility root identified.
- [ ] Reproduction or abstention rationale recorded.
- [ ] Evidence and truth labels assigned per material claim.
- [ ] Trust, policy, rights, sensitivity, and release impact classified.
- [ ] Fix includes tests, fixtures, validators, policy checks, or documentation where relevant.
- [ ] Public claims, maps, exports, or AI outputs have a correction or rollback path when affected.
- [ ] Closure links to the implementing PR, accepted governing artifact, or explicit not-planned rationale.

---

<sub>Issue closure is administrative state. It does not by itself prove implementation, validation, correction, release, publication, or rollback completion.</sub>
