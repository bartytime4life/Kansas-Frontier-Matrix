<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/web-acquisition-conduct-assessment
title: WebAcquisitionConductAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Source steward · Rights reviewer · Acquisition steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; source; acquisition; terms; robots; anti-evasion
responsibility: Define fixture-only conduct checks for a proposed web-acquisition route without fetching a source or creating legal, policy, activation, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./source_descriptor.md
  - ./source_rights_currentness_assessment.md
  - ./source_terms_drift_disposition.md
  - ./source_activation_decision.md
  - ../../schemas/contracts/v1/source/web_acquisition_conduct_assessment.schema.json
  - ../../fixtures/contracts/v1/source/web_acquisition_conduct_assessment/cases.json
  - ../../tools/validators/source/validate_web_acquisition_conduct_assessment.py
  - ../../tests/validators/test_validate_web_acquisition_conduct_assessment.py
  - ../../docs/intake/exploratory/pass-18-web-acquisition-conduct-source-map.md
[/KFM_META_BLOCK_V2] -->

# WebAcquisitionConductAssessmentCandidate

`WebAcquisitionConductAssessmentCandidate` is an additive, fixture-only profile for reviewing the declared conduct of one proposed web-acquisition route before any connector or operator attempts a fetch.

It adapts the smallest reviewable intersection of supplied Pass 18 cards `KFM-P18-INV-100`, `KFM-P18-INV-247`, and `KFM-P18-INV-423`: terms and robots constraints are acquisition gates, while disguised identity, rotating-proxy evasion, and unreviewed distributed acquisition are denied by default.

## Boundary

The profile is `PROPOSED_INACTIVE`, deterministic, no-network, and non-authoritative. A validator `PASS` means only that the fixture declaration is closed, internally coherent, content-addressed, and does not assert a prohibited conduct posture.

It does **not** retrieve or interpret live terms or `robots.txt`, make a legal determination, prove permission, negotiate a source agreement, fetch bytes, activate a connector, schedule work, create credentials, select a proxy, write lifecycle data, decide evidence or policy, approve review, release, deploy, publish, or authorize public use.

## Conduct axes

| Axis | Closed declaration |
|---|---|
| Route | Official API, documented download, browser automation, HTML scrape, or unresolved. |
| Terms | Permits, restricts, prohibits, or unknown, with an opaque evidence reference when resolved. |
| Robots | Allowed, disallowed, not applicable, or unknown, with an opaque evidence reference when applicable and resolved. |
| Rate limit | Declared local bounds, a source-default policy reference, or unresolved. |
| Identity | Declared user-agent posture plus no proxy, a source-authorized proxy, rotating evasion, or unresolved. |
| Distribution | Disabled, source-authorized, unreviewed, or unresolved distributed acquisition. |
| Review | Complete, pending, or unknown, with canonical review-record references. |

An official API or documented download declares robots as `NOT_APPLICABLE`. Browser automation and HTML scraping require an `ALLOWED` robots declaration. A source-authorized proxy or distributed route requires a source-agreement reference, terms that permit automation, and complete review references. These are declaration-coherence checks only.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Route, terms, robots, rate, identity, proxy, distribution, and review declarations are coherent and non-evasive. |
| `ABSTAIN` | One or more route, terms, robots, rate, identity, distribution, or review declarations remains unresolved. |
| `DENY` | Terms restrict or prohibit automation, robots disallow access, stealth/evasion is declared, distributed acquisition is unreviewed, or resolved declarations contradict their required support. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema. |

These outcomes are preflight routing signals only. They are not permission, legal advice, source admission, connector activation, policy, review, release, deployment, or publication decisions.

## Directory Rules basis

Accepted Directory Rules place source-acquisition meaning under `contracts/source/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable conformance under `tests/`, CI orchestration under `.github/`, source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

This object composes `SourceDescriptor`, rights-currentness, terms-drift, and source-activation responsibilities by opaque reference. It does not create a parallel source registry, rights authority, connector, scheduler, policy surface, credential store, lifecycle lane, release lane, or public API.

## Validation

```bash
python -m unittest tests.validators.test_validate_web_acquisition_conduct_assessment -v
python tools/validators/source/validate_web_acquisition_conduct_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no source, connector, registry record, credential, schedule, data, evidence, policy, review, lifecycle, release, deployment, or public artifact.
