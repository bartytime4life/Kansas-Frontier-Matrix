<!--
KFM_WIKI_SOURCE
page_id: Governance-and-Evidence
title: Governance and Evidence
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Governance-and-Evidence.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Governance and Evidence

KFM's trust posture is simple to state and demanding to implement:

> **A consequential claim cites resolvable, admissible evidence or the system abstains.**

Governance does not make source material true. It records how evidence, rights, sensitivity, validation, review, release, correction, and rollback affect what may be asserted or shown.

## Truth labels

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current-session evidence or an accepted decision |
| `PROPOSED` | Designed or requested, but not verified as current implementation |
| `UNKNOWN` | Evidence is insufficient |
| `NEEDS VERIFICATION` | A concrete check can resolve the question |
| `CONFLICTED` | Relevant sources or authorities disagree |
| `LINEAGE` | Historical context retained without current authority by itself |

Truth labels describe knowledge. They are not runtime outcomes, review decisions, or placement results.

## Evidence chain

A typical claim path is:

```text
SourceDescriptor
    -> immutable source capture or locator
    -> EvidenceRef
    -> EvidenceBundle
    -> policy and sensitivity checks
    -> review and validation
    -> release state
    -> governed public claim
```

`EvidenceRef` identifies support. `EvidenceBundle` resolves the source role, scope, provenance, limitations, and citation support needed by the claim. A broken or denied resolution does not become a best guess.

## Source-role anti-collapse

KFM should keep these roles explicit:

- observation;
- authoritative interpretation;
- regulatory or administrative record;
- forecast;
- model or derived surface;
- aggregate or index;
- community report;
- historical source;
- contextual or corroborative source;
- synthetic fixture.

A model cannot silently masquerade as an observation. A permit does not prove a physical deposit. A map visualization does not replace the source it depicts.

## Policy and review

Policy may allow, deny, restrict, hold, redact, generalize, delay, or require additional review. It must remain separate from:

- schema validation;
- factual evidence;
- generated prose;
- UI styling;
- a successful test or workflow;
- the presence of a file under `data/published/`.

Higher-risk release may require separation of duties, domain or legal review, source-rights verification, sensitivity transformation, and explicit rollback support.

## Promotion and release

Promotion is a decision against evidence, not a file operation:

```text
candidate
  + validation
  + policy
  + provenance and integrity
  + review
  + proof and catalog closure
  + correction path
  + rollback target
  -> governed promotion/release decision
```

A receipt records process memory. A proof supports a verifiable condition. A catalog enables discovery. A release manifest records a release. None substitutes for another.

## Corrections are first-class

KFM should preserve:

- prior identity and content digests;
- correction reason and effective time;
- supersession and withdrawal links;
- affected claims and public carriers;
- cache, map, search, export, and AI propagation;
- rollback target and replay evidence.

Silent replacement hides the knowledge history and makes public correction unverifiable.

## AI boundary

AI may help retrieve, compare, summarize, classify, and draft. It does not decide source authority, rights, sensitivity, policy, review, release, or truth. Governed AI follows:

```text
define scope
  -> retrieve released evidence
  -> resolve EvidenceRef to EvidenceBundle
  -> apply policy and sensitivity checks
  -> return cited finite outcome
```

## Wiki boundary

This wiki explains governance and points to authority. It cannot itself:

- adopt doctrine or an ADR;
- define a contract or schema;
- authorize source use;
- clear rights or sensitivity;
- approve a release;
- promote data;
- publish a claim as KFM truth.

## Canonical reading

- [Doctrine index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/README.md)
- [Evidence First](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/evidence-first.md)
- [Authority Ladder](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/authority-ladder.md)
- [Lifecycle Law](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/lifecycle-law.md)
- [Corrections First Class](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/corrections-first-class.md)
- [AI Build Operating Contract](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/ai-build-operating-contract.md)
