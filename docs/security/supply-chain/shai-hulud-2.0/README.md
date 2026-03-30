<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-UUID
title: Shai-Hulud 2.0
type: standard
version: v1
status: draft
owners: @bartytime4life
created: TODO-YYYY-MM-DD
updated: TODO-YYYY-MM-DD
policy_label: public
related: [docs/README.md, docs/security/README.md, docs/security/supply-chain/README.md, docs/security/supply-chain/shai-hulud-2.0/protections/README.md, docs/security/supply-chain/shai-hulud-2.0/workflows/README.md, docs/security/supply-chain/shai-hulud-2.0/indicators/README.md, docs/security/supply-chain/shai-hulud-2.0/indicators/samples/README.md, docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/README.md, .github/CODEOWNERS, .github/workflows/README.md, policy/README.md, contracts/README.md, tests/README.md]
tags: [kfm, security, supply-chain, shai-hulud-2.0]
notes: [Owners are grounded from current public .github/CODEOWNERS fallback; doc_id and dates still need verification; live subtree shape is confirmed on current public main; no checked-in workflow YAML is claimed from this file alone; deeper semantics for the lane name remain intentionally bounded]
[/KFM_META_BLOCK_V2] -->

# Shai-Hulud 2.0

Named KFM supply-chain lane for documented protections, workflow expectations, and measurable assurance indicators.

> [!IMPORTANT]
> **Status:** experimental · **Doc maturity:** draft  
> **Owners:** `@bartytime4life` *(current public `.github/CODEOWNERS` fallback; no narrower lane rule was visible on public `main`)*  
> **Path:** `docs/security/supply-chain/shai-hulud-2.0/README.md`  
> ![Status](https://img.shields.io/badge/status-experimental-orange) ![Doc](https://img.shields.io/badge/doc-draft-lightgrey) ![Lane](https://img.shields.io/badge/lane-shai--hulud%202.0-6f42c1) ![Tree](https://img.shields.io/badge/tree-public--main-0969da) ![Workflows](https://img.shields.io/badge/workflows-README--only-lightgrey) ![Truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED-2ea043)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!WARNING]
> This lane documents **control shape**, **workflow routing**, and **measurement routing** for a named supply-chain surface.  
> Current public `main` confirms the subtree and its READMEs, but `.github/workflows/` is README-only on that branch. Do **not** use this file to imply checked-in workflow YAML, emitted SBOMs, live signatures or attestations, or merge-blocking enforcement unless another executable surface proves them.

## Scope

This directory is the README-level index for a named supply-chain documentation lane inside KFM security docs.

It exists to answer three narrow questions quickly:

1. What belongs in the lane root instead of one of its child READMEs?
2. Which adjacent repo surfaces should be re-checked before trust-bearing prose changes?
3. Which claims here are confirmed by the current public tree, and which must stay bounded as `INFERRED`, `PROPOSED`, or `NEEDS VERIFICATION`?

At present, public `main` confirms this subtree shape:

- `protections/`
- `workflows/`
- `indicators/`
  - `samples/`
  - `signatures/`

That structure supports one disciplined interpretation:

- `protections/` explains which guardrails belong to the lane.
- `workflows/` explains how those guardrails are exercised, checked, promoted, rolled back, or corrected.
- `indicators/` explains what measurable assurance looks like, how it is interpreted, and where public-safe examples live.

That interpretation is **INFERRED** from the live subtree and its surrounding security and supply-chain context. The deeper program meaning of the name **Shai-Hulud 2.0** remains **NEEDS VERIFICATION**.

### Truth posture used in this README

| Label | Meaning here |
| --- | --- |
| **CONFIRMED** | Visible in the current public repo tree or already established by adjacent repo docs |
| **INFERRED** | Strongly suggested by directory names and repo context, but not directly proven as mounted implementation |
| **PROPOSED** | Recommended structure, workflow, or documentation move for this lane |
| **NEEDS VERIFICATION** | Important but not directly established from the current visible repo state |

## Repo fit

This README sits beneath the supply-chain hub and above the lane’s child READMEs. It should stay specific enough to keep the lane maintainable, while avoiding duplication of sibling lanes, broader security doctrine, or adjacent executable surfaces.

| Direction | Link | Why it matters |
| --- | --- | --- |
| Upstream | [`../../../README.md`](../../../README.md) | `docs/` doctrine, structure, and documentation expectations |
| Upstream | [`../../README.md`](../../README.md) | security hub and trust/supply-chain framing |
| Upstream | [`../README.md`](../README.md) | parent supply-chain lane |
| Downstream | [`./protections/README.md`](./protections/README.md) | control and guardrail intent |
| Downstream | [`./workflows/README.md`](./workflows/README.md) | process and gate sequencing |
| Downstream | [`./indicators/README.md`](./indicators/README.md) | measurable assurance and interpretation |
| Downstream | [`./indicators/samples/README.md`](./indicators/samples/README.md) | release-safe examples and fixtures |
| Downstream | [`./indicators/signatures/README.md`](./indicators/signatures/README.md) | signature- and attestation-oriented reading notes |
| Sibling | [`../dependency-confusion/README.md`](../dependency-confusion/README.md) | dependency-source mix-up risks belong there |
| Sibling | [`../sigstore-cosign-v3/README.md`](../sigstore-cosign-v3/README.md) | Sigstore/Cosign-specific guidance belongs there |
| Sibling | [`../reference-repos/README.md`](../reference-repos/README.md) | external repository comparison material belongs there |
| Adjacent ownership surface | [`../../../../.github/CODEOWNERS`](../../../../.github/CODEOWNERS) | current public owner fallback for this lane |
| Adjacent workflow surface | [`../../../../.github/workflows/README.md`](../../../../.github/workflows/README.md) | current workflow inventory and README-only caveat on public `main` |
| Adjacent policy surface | [`../../../../policy/README.md`](../../../../policy/README.md) | deny-by-default posture, reasons, obligations, and outcome grammar |
| Adjacent contract surface | [`../../../../contracts/README.md`](../../../../contracts/README.md) | typed trust objects and release/correction expectations |
| Adjacent verification surface | [`../../../../tests/README.md`](../../../../tests/README.md) | proof burden, negative-path checks, and correction drills |

## Accepted inputs

Content that belongs here includes:

- lane-level scope, routing, and boundary guidance for `shai-hulud-2.0`
- short explanations of how `protections/`, `workflows/`, and `indicators/` divide responsibility
- cross-links to owning workflow, policy, contract, test, fixture, runbook, or release-evidence surfaces
- lane-level cautions about overclaiming enforcement
- public-safe notes about how to interpret redacted or synthetic signature, attestation, digest, or assurance examples

## Exclusions

| This does **not** belong here | Put it here instead |
| --- | --- |
| Private keys, secrets, tokens, credentials, or mutable live signing material | Never commit them into docs; use the repo’s secure secret-handling path |
| Canonical generated proof artifacts, emitted SBOMs, live attestations, or release evidence bundles | Their governed artifact or release-evidence home |
| Workflow YAML or CI job logic as the source of truth | [`../../../../.github/workflows/README.md`](../../../../.github/workflows/README.md) and the owning workflow files |
| Executable policy bundles or policy tests as narrative-only copy | [`../../../../policy/README.md`](../../../../policy/README.md) and owning policy/test surfaces |
| Canonical machine-readable trust objects | [`../../../../contracts/README.md`](../../../../contracts/README.md) and the eventual authoritative schema home |
| General dependency-confusion doctrine | [`../dependency-confusion/README.md`](../dependency-confusion/README.md) |
| General Sigstore / Cosign doctrine | [`../sigstore-cosign-v3/README.md`](../sigstore-cosign-v3/README.md) |
| Broad repo-wide security doctrine | [`../../README.md`](../../README.md) |
| Claims that a control is enforced in code when the visible repo evidence does not prove it | Keep it `PROPOSED` or `NEEDS VERIFICATION` until an executable surface proves it |

## Current verified snapshot

The current public `main` branch safely supports the following statements without widening into stronger enforcement claims.

| Surface | Current public status | Safe statement | Why it matters here |
| --- | --- | --- | --- |
| `docs/security/supply-chain/shai-hulud-2.0/` | **CONFIRMED** | Public `main` exposes `README.md`, `indicators/`, `protections/`, and `workflows/` | The lane structure is real, even if enforcement is not proven here |
| `docs/security/supply-chain/shai-hulud-2.0/indicators/` | **CONFIRMED** | Public `main` exposes `README.md`, `samples/`, and `signatures/` | The nested indicator surfaces exist and should be linked explicitly |
| `.github/CODEOWNERS` | **CONFIRMED** | Public CODEOWNERS uses a global fallback and assigns `/docs/` to `@bartytime4life` | The owner field here can be grounded without inventing a narrower rule |
| `.github/workflows/README.md` | **CONFIRMED** | Public `main` states `.github/workflows/` contains `README.md` only | This README must not imply checked-in workflow YAML from lane shape alone |
| `policy/README.md`, `contracts/README.md`, `tests/README.md` | **CONFIRMED** | Current public `main` exposes these as adjacent boundary docs | Lane prose can route meaning toward policy, typed objects, and verification without claiming those executable assets already exist |

## Directory tree

```text
docs/security/supply-chain/shai-hulud-2.0/
├── README.md                            # lane index, scope, and routing
├── protections/
│   └── README.md                        # guardrail and control intent
├── workflows/
│   └── README.md                        # gate, promotion, rollback, and correction choreography
└── indicators/
    ├── README.md                        # measurable assurance and interpretation
    ├── samples/
    │   └── README.md                    # public-safe examples and fixtures
    └── signatures/
        └── README.md                    # signature / attestation reading notes
```

> [!NOTE]
> This tree is intentionally limited to what is visible on the current public branch. If the checked-out branch or private repo state differs, update this section from mounted repo evidence before merge.

## Quickstart

1. Re-read the parent supply-chain README before changing this lane.
2. Decide whether the change belongs in the root lane or in one child README.
3. Re-check current public ownership, workflow, policy, contract, and test boundary docs before writing trust-bearing language.
4. Keep every newly added claim explicit as `CONFIRMED`, `INFERRED`, `PROPOSED`, or `NEEDS VERIFICATION`.
5. Never commit secrets or live signing material into this subtree.

```bash
# Read the lane root and child READMEs first
sed -n '1,240p' docs/security/supply-chain/shai-hulud-2.0/README.md
sed -n '1,240p' docs/security/supply-chain/shai-hulud-2.0/protections/README.md
sed -n '1,240p' docs/security/supply-chain/shai-hulud-2.0/workflows/README.md
sed -n '1,260p' docs/security/supply-chain/shai-hulud-2.0/indicators/README.md
sed -n '1,220p' docs/security/supply-chain/shai-hulud-2.0/indicators/samples/README.md
sed -n '1,220p' docs/security/supply-chain/shai-hulud-2.0/indicators/signatures/README.md

# Re-check adjacent current public boundary docs before changing trust-bearing prose
sed -n '1,220p' .github/CODEOWNERS
sed -n '1,240p' .github/workflows/README.md
sed -n '1,280p' policy/README.md
sed -n '1,280p' contracts/README.md
sed -n '1,260p' tests/README.md

# Search for lane-coupled trust objects and supply-chain terms
git grep -nE 'Shai-Hulud|sbom|attest|signature|digest|DecisionEnvelope|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice|ReleaseManifest' -- \
  docs .github policy contracts tests 2>/dev/null || true
```

## Usage

Use this README when the work is about **lane scope**, **ownership of meaning**, or **which adjacent surfaces must move together**.

> [!TIP]
> A change is incomplete if it only edits prose. When trust-bearing meaning shifts, re-check workflows, policy, contracts, tests, and release evidence in the same review window—or keep the change clearly marked as `PROPOSED` or `NEEDS VERIFICATION`.

| You need to… | Start here | Then re-check |
| --- | --- | --- |
| adjust lane scope, ownership, or routing | this README | parent security and supply-chain READMEs, `.github/CODEOWNERS` |
| define or tighten a guardrail | [`./protections/README.md`](./protections/README.md) | `policy/README.md`, `contracts/README.md`, `tests/README.md` |
| document a gate, promotion sequence, rollback path, or correction step | [`./workflows/README.md`](./workflows/README.md) | `.github/workflows/README.md`, `policy/README.md`, release/correction docs |
| define a measurable signal or interpretation rule | [`./indicators/README.md`](./indicators/README.md) | `tests/README.md`, samples, signatures, release-safe evidence |
| add a public-safe example or fixture | [`./indicators/samples/README.md`](./indicators/samples/README.md) | redaction, provenance, and public-safety checks |
| add signature or attestation reading notes | [`./indicators/signatures/README.md`](./indicators/signatures/README.md) | [`../sigstore-cosign-v3/README.md`](../sigstore-cosign-v3/README.md), contracts, policy |
| write general Sigstore / Cosign doctrine | [`../sigstore-cosign-v3/README.md`](../sigstore-cosign-v3/README.md) | workflow, policy, contract, and verification surfaces |
| write package-origin or namespace-trust doctrine | [`../dependency-confusion/README.md`](../dependency-confusion/README.md) | package-manager config, workflow, and review surfaces |
| capture upstream repository comparison material | [`../reference-repos/README.md`](../reference-repos/README.md) | local adoption decision docs, contracts, policy, tests |

## Diagram

```mermaid
flowchart TB
  DOCS["docs/README.md<br/>docs doctrine"] --> SEC["docs/security/README.md<br/>security hub"]
  SEC --> SUPPLY["docs/security/supply-chain/README.md<br/>supply-chain hub"]
  SUPPLY --> SH["shai-hulud-2.0/README.md<br/>lane index"]

  SH --> P["protections/README.md"]
  SH --> W["workflows/README.md"]
  SH --> I["indicators/README.md"]
  I --> S["samples/README.md"]
  I --> G["signatures/README.md"]

  SH -. owner fallback .-> CO[".github/CODEOWNERS"]
  W -. current workflow inventory .-> WF[".github/workflows/README.md"]
  P -. decision posture .-> POL["policy/README.md"]
  P -. typed trust objects .-> C["contracts/README.md"]
  I -. proof burden .-> T["tests/README.md"]
```

The solid arrows show the lane’s current documented repo fit. The dotted arrows show adjacent surfaces that should be re-checked when meaning changes. They are coupling cues, not proof that the underlying enforcement is already checked in.

## Tables

### Lane registry

| Node | Public-tree status | Primary job | Keep out |
| --- | --- | --- | --- |
| `README.md` | confirmed file | lane scope, routing, ownership of meaning, adjacent-surface cues | detailed control catalogs that belong in child docs |
| `protections/` | confirmed child dir + README | guardrail intent and control boundaries | step-by-step workflow choreography |
| `workflows/` | confirmed child dir + README | gate sequencing, promotion, rollback, correction flow | broad control taxonomy or tool-specific doctrine |
| `indicators/` | confirmed child dir + README | measurable assurance, interpretation, and signal classes | secrets, live proofs, or hidden enforcement claims |
| `indicators/samples/` | confirmed child dir + README | redacted or synthetic examples and fixture-like material | canonical generated proof objects |
| `indicators/signatures/` | confirmed child dir + README | public-safe signature and attestation reading notes | live signing material or general Sigstore doctrine |

### Coupled change surfaces

| If this changes… | Also re-check | Why |
| --- | --- | --- |
| owner, status, or path language | `.github/CODEOWNERS`, parent security/supply-chain READMEs | keep ownership and maturity cues repo-grounded |
| guardrail meaning | `protections/`, `policy/README.md`, `contracts/README.md`, `tests/README.md` | guardrails should resolve into decision grammar, typed objects, and proof burden |
| workflow meaning | `workflows/`, `.github/workflows/README.md`, rollback/correction docs | this lane must not imply automation or gates the repo does not prove |
| indicator interpretation or sample language | `indicators/`, `samples/`, `signatures/`, `tests/README.md` | assurance language should stay measurable and reviewable |
| Sigstore / attestation wording | [`../sigstore-cosign-v3/README.md`](../sigstore-cosign-v3/README.md), policy, contracts, release-proof surfaces | keep tool-specific doctrine centralized and consistent |
| sibling-lane boundaries | [`../dependency-confusion/README.md`](../dependency-confusion/README.md), [`../reference-repos/README.md`](../reference-repos/README.md) | avoid topic bleed and duplicate doctrine |

## Task list / Definition of done

- [ ] The KFM Meta Block v2 is present and any unresolved values stay clearly reviewable.
- [ ] The owner field still matches current public `.github/CODEOWNERS` fallback or is updated from a narrower verified rule.
- [ ] Every current-tree claim stays limited to what the visible public branch actually proves.
- [ ] No wording here implies checked-in workflow YAML, emitted SBOMs, or live signatures/attestations without executable proof elsewhere.
- [ ] Child README links resolve to real files.
- [ ] The change reduces drift between lane docs and adjacent workflow, policy, contract, or test surfaces.
- [ ] Samples and examples remain public-safe, redacted, or synthetic.
- [ ] Superseded or stale guidance is corrected instead of silently abandoned.

## FAQ

### Is this the canonical home for all supply-chain security guidance?

No. This is one named lane under the broader supply-chain hub. Keep broad doctrine in parent docs and tool-specific doctrine in sibling lanes.

### Does the presence of `workflows/` or `signatures/` prove active enforcement?

No. The current public branch proves those documentation surfaces exist. It does not, by itself, prove checked-in workflow YAML, live signatures, emitted attestations, or merge-blocking gates.

### Can canonical generated SBOMs, attestations, or release proof bundles live here?

This lane may hold documentation and public-safe examples. Canonical generated artifacts should live in their governed artifact or release-evidence home, not as hand-maintained documentation files here.

### Why split protections, workflows, and indicators?

Because the split makes drift easier to spot:

- **protections** explain what guardrails belong here
- **workflows** explain how those guardrails are exercised
- **indicators** explain how assurance is measured and interpreted

### Why keep the lane name semantically bounded?

Because the public repo currently proves the lane’s shape and documentation role more strongly than it proves any deeper canonical meaning for the name itself. Until a stronger source defines that meaning, this README should treat it as a named local lane and avoid mythologizing it.

## Appendix

<details>
<summary>Suggested child README contracts and proof-aware editing notes</summary>

### `protections/` should usually answer

- what the control is called
- what failure it prevents or narrows
- what evidence would show the protection is working
- what this protection does **not** cover
- which workflow, policy, contract, and test surfaces must remain aligned

### `workflows/` should usually answer

- what triggers the workflow
- which typed inputs it expects
- which negative outcomes it can emit
- what rollback or correction hooks exist
- what proof a reviewer should expect to inspect

### `indicators/` should usually answer

- what is being measured
- why that signal matters
- where the signal comes from
- how it should be interpreted
- where release-safe examples or fixture-like samples live
- what blind spots remain

### `samples/` should usually contain

- synthetic fixtures
- redacted excerpts
- negative-path examples
- reviewer aids that explain shape without pretending to be release-bearing proof

Avoid:

- mutable live proof objects
- secrets
- unverifiable copied blobs
- environment-specific credentials

### `signatures/` should usually contain

- signature and attestation reading notes
- redacted verification examples
- digest-binding interpretation notes
- narrow guidance on what a reviewer should learn from a public-safe example

Avoid:

- live signing operations
- private keys
- tool-general doctrine that belongs in the Sigstore/Cosign sibling lane
- claims that the sample equals enforcement

### Adjacent proof-aware check before merge

Before merging a trust-bearing edit here, re-check these questions:

1. Did the owner, status, or evidence boundary drift from current public repo evidence?
2. Did the edit change guardrail meaning without updating workflow, policy, contract, or test surfaces?
3. Did the edit blur documentation shape into enforcement certainty?
4. Did the edit duplicate sibling doctrine that belongs in `dependency-confusion/`, `sigstore-cosign-v3/`, or `reference-repos/`?
5. Did any example become more sensitive, less redacted, or harder to verify safely?

</details>

[Back to top](#shai-hulud-20)
