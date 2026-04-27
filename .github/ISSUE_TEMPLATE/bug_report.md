---
name: Bug report
about: Report a reproducible KFM problem with evidence, scope, policy posture, and safe redaction.
title: "[Bug]: "
labels: ""
assignees: ""
---

<!--
KFM bug reports should help maintainers reproduce the problem, understand the evidence boundary,
and avoid accidental exposure of sensitive or unpublished material.

Before submitting:
- Redact secrets, credentials, private endpoints, tokens, keys, cookies, and internal URLs.
- Do not post exact sensitive locations, steward-only data, living-person details, DNA/genomics data,
  private landowner details, unpublished RAW/WORK/QUARANTINE material, or active exploit details.
- If this is an active security vulnerability or exposure risk, do not file a public issue. Use the
  repository's private security reporting path or maintainer contact path if available.
-->

## Safety check

> [!CAUTION]
> Do not include secrets, credentials, private endpoints, exact sensitive locations, steward-only data, living-person details, DNA/genomics data, private landowner details, unpublished `RAW` / `WORK` / `QUARANTINE` material, or active exploit details in a public issue.

- [ ] I have redacted sensitive, private, steward-only, or unpublished material.
- [ ] This is not an active security vulnerability that requires private disclosure.
- [ ] This report does not expose exact restricted geometry or unreleased source data.
- [ ] If the bug involves rights, sensitivity, source terms, or public release state, I have marked that clearly below.

## Summary

<!-- One or two sentences. What is broken? What did you expect KFM to do? -->



## Affected KFM surface

Check all that apply.

- [ ] Documentation / README / ADR / issue template
- [ ] Source intake / `SourceDescriptor` / source registry
- [ ] Data lifecycle: `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`
- [ ] Contract / schema / DTO / fixture
- [ ] Validator / policy gate / promotion gate
- [ ] `EvidenceRef` / `EvidenceBundle` / citation validation
- [ ] Catalog / triplet / graph / proof / receipt / release manifest
- [ ] Promotion / publication / correction / rollback
- [ ] MapLibre / map layer / popup / Evidence Drawer
- [ ] Focus Mode / governed AI / runtime response envelope
- [ ] Local deployment / reverse proxy / VPN / authentication / authorization
- [ ] Test / CI / workflow / generated artifact
- [ ] Other:

## Repository context

<!-- Fill in what you can. Use UNKNOWN when you do not know. -->

| Field | Value |
|---|---|
| Branch | `UNKNOWN` |
| Commit SHA | `UNKNOWN` |
| File path(s) or component(s) | `UNKNOWN` |
| Runtime or package version(s) | `UNKNOWN` |
| Browser / OS / environment | `UNKNOWN` |
| Local, CI, staging, or published release? | `UNKNOWN` |

## Steps to reproduce

<!-- Keep this deterministic where possible. Include commands only if they are safe and redacted. -->

1.
2.
3.

```bash
# Optional: paste safe, redacted commands here.
```

## Expected behavior

<!-- What should have happened? Include the relevant evidence, policy, release, or UI expectation if applicable. -->



## Actual behavior

<!-- What happened instead? Include error messages, screenshots, or logs only after redaction. -->



## Evidence, source, and claim context

<!-- Use this section when the bug affects a claim, source, citation, policy decision, release, or map layer. -->

| Field | Value |
|---|---|
| Does this affect a public or semi-public claim? | `No / Yes / UNKNOWN` |
| Claim, object, feature, or release ID | `UNKNOWN` |
| Source ID / `SourceDescriptor` | `UNKNOWN` |
| `EvidenceRef` / `EvidenceBundle` | `UNKNOWN` |
| Receipt / proof / manifest path | `UNKNOWN` |
| Citation or source link involved | `UNKNOWN` |
| Review state | `UNKNOWN` |
| Release state | `UNKNOWN` |
| Correction or rollback target | `UNKNOWN` |

## Spatial and temporal scope

> [!WARNING]
> If the issue involves archaeology, rare species, habitat, critical infrastructure, private land, living people, DNA/genomics, or steward-controlled records, generalize the location and describe the private evidence path instead of posting exact details.

| Field | Value |
|---|---|
| Geographic area | `UNKNOWN` |
| Exact sensitive geometry involved? | `No / Yes / UNKNOWN` |
| Observation time / valid time | `UNKNOWN` |
| Source publication time | `UNKNOWN` |
| Release time | `UNKNOWN` |
| Stale or expired context suspected? | `No / Yes / UNKNOWN` |

## Policy, rights, and sensitivity impact

Check all that apply.

- [ ] Could publish or reveal sensitive material.
- [ ] Could expose unpublished `RAW`, `WORK`, or `QUARANTINE` data.
- [ ] Could bypass governed API, policy, review, or release state.
- [ ] Could allow direct model-runtime or direct canonical-store access.
- [ ] Could make an uncited or unsupported claim appear authoritative.
- [ ] Could confuse derived map/tile/search/summary output with canonical truth.
- [ ] Could affect rights, license, attribution, source terms, or redistribution posture.
- [ ] Could require a correction notice, withdrawal, rollback, or public erratum.
- [ ] No known policy, rights, sensitivity, or release impact.
- [ ] UNKNOWN.

## Logs, screenshots, and artifacts

<!-- Paste only safe, redacted output. For screenshots, crop or blur private paths, tokens, endpoints, user data, exact sensitive locations, and steward-only details. -->

```text
Paste safe, redacted logs or validation output here.
```

## Validation already attempted

<!-- Include tests, validators, linting, schema checks, or manual checks already run. Use UNKNOWN if none. -->

- [ ] Reproduced locally.
- [ ] Reproduced in CI or workflow output.
- [ ] Checked relevant schema or contract.
- [ ] Checked relevant policy or validator.
- [ ] Checked relevant docs / README / ADR.
- [ ] Checked released artifact, manifest, receipt, proof pack, or catalog record.
- [ ] Not yet validated.
- [ ] UNKNOWN.

```bash
# Optional: paste safe, redacted validation commands and outputs here.
```

## Severity and impact

Choose the closest fit.

- [ ] Blocks build, test, CI, release, or promotion.
- [ ] Breaks evidence traceability, citation resolution, or claim reconstruction.
- [ ] Risks unsafe publication, sensitive exposure, or policy bypass.
- [ ] Produces incorrect map, time, layer, geometry, or Evidence Drawer behavior.
- [ ] Produces incorrect Focus Mode / governed AI outcome.
- [ ] Causes documentation confusion or contributor misdirection.
- [ ] Cosmetic or low-risk usability issue.
- [ ] UNKNOWN.

## Suggested correction or rollback path

<!-- Optional. Do not guess beyond your evidence. -->

- Last known good commit / release / artifact:
- Proposed fix:
- Proposed test or negative-path fixture:
- Public correction, withdrawal, or rollback needed? `No / Yes / UNKNOWN`

## Related issues, PRs, docs, or artifacts

<!-- Link only public-safe material. -->

-
-

## Maintainer triage checklist

<!-- Maintainers may update this after the issue is reviewed. -->

- [ ] Reproduction is confirmed, or non-reproducibility is documented.
- [ ] Evidence basis is classified as `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, `DENY`, `ABSTAIN`, or `ERROR`.
- [ ] Policy, rights, sensitivity, release, and rollback impact are classified.
- [ ] Fix path includes tests, fixtures, validators, policy checks, or documentation updates where relevant.
- [ ] Public claims, maps, exports, or AI outputs affected by the bug have a correction or rollback path.
