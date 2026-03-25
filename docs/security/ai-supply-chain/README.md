<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: KFM AI Supply-Chain & Governed Model Runtime
type: standard
version: v1
status: review
owners: @bartytime4life
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related: [../../README.md, ../README.md, ../threat-model.md, ../vulnerability-management.md, ../prompt-injection/README.md, ../prompt-injection-defense.md, ../supply-chain/README.md, ../../../contracts/README.md, ../../../policy/README.md, ../../../schemas/README.md, ../../../.github/workflows/README.md, ../../../.github/SECURITY.md]
tags: [kfm, security, ai, supply-chain, model-runtime, prompt-injection]
notes: [doc_id and dates require merge-time verification; current public main exposed this directory as scaffold-only during drafting]
[/KFM_META_BLOCK_V2] -->

# KFM AI Supply-Chain & Governed Model Runtime

Public-safe guidance for model provenance, adapter boundaries, prompt/input hardening, evaluation, and evidence-bounded AI behavior under `docs/security/ai-supply-chain/`.

> Status: `experimental`
> Owners: `@bartytime4life`
> Path: `docs/security/ai-supply-chain/README.md`
> Repo fit: secure-AI lane under [`../README.md`](../README.md), adjacent to prompt-injection and broader supply-chain docs, downstream into contracts, policy, tests, and workflow gates.
>
> ![Status](https://img.shields.io/badge/status-experimental-9ca3af?style=flat-square)
> ![Owner](https://img.shields.io/badge/owner-%40bartytime4life-2563eb?style=flat-square)
> ![Docs lane](https://img.shields.io/badge/lane-secure%20AI%20%2B%20supply%20chain-7c3aed?style=flat-square)
> ![Repo](https://img.shields.io/badge/repo-public-16a34a?style=flat-square)
> ![Posture](https://img.shields.io/badge/posture-doctrine%20grounded%20%7C%20implementation%20cautious-b45309?style=flat-square)
>
> Quick jumps: [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Control surfaces](#control-surfaces) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This lane is **repo-grounded for currently visible public Markdown surfaces** and **doctrine-grounded for KFM’s AI/runtime rules**. It does **not** claim that signed builds, SBOM export, evaluation gates, policy bundles, or model-runtime enforcement are already active in checked-in automation.

> [!WARNING]
> In KFM, “AI supply chain” is broader than dependency CVEs. It includes model or embedding artifacts, tokenizer/config provenance, inference adapters, runtime containment, retrieved-context shaping, prompt/input boundaries, accountable output envelopes, release proof, and correction lineage.

---

## Scope

This directory defines the **secure-AI and model-runtime lane** for KFM.

The lane exists because KFM treats AI as a **bounded helper inside a governed evidence system**, not as a sovereign truth source. In practical terms, that means this README is about the part of the system where model artifacts, adapters, policy checks, evidence resolution, runtime outcomes, and release/correction visibility meet.

This file should help maintainers answer four questions quickly:

1. What belongs in the AI supply-chain lane?
2. What belongs in neighboring lanes instead?
3. What is **CONFIRMED**, what is **INFERRED**, and what remains **UNKNOWN**?
4. What should be added next without pretending the repo already enforces it?

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Repo fit

| Relation | Path | Why it matters here | Posture |
|---|---|---|---|
| Docs index | [`../../README.md`](../../README.md) | Wider docs conventions and navigation context | `CONFIRMED` |
| Parent security index | [`../README.md`](../README.md) | Security subtree map; entry point into secure-AI and adjacent lanes | `CONFIRMED` |
| Adjacent threat model | [`../threat-model.md`](../threat-model.md) | Cross-cutting trust boundary, failure-mode, and attack-surface context | `CONFIRMED` |
| Adjacent vulnerability lane | [`../vulnerability-management.md`](../vulnerability-management.md) | Intake, triage, remediation, and disclosure path for discovered issues | `CONFIRMED` |
| Adjacent prompt-injection lane | [`../prompt-injection/README.md`](../prompt-injection/README.md) | Hostile-input, retrieval-scope, and instruction-conflict guidance | `CONFIRMED` |
| Adjacent prompt defense note | [`../prompt-injection-defense.md`](../prompt-injection-defense.md) | Narrow defensive guidance for input and prompt-boundary controls | `CONFIRMED` |
| Adjacent broader supply-chain lane | [`../supply-chain/README.md`](../supply-chain/README.md) | Provenance, release integrity, attestation, SBOM, and artifact trust | `CONFIRMED` |
| Contract surface | [`../../../contracts/README.md`](../../../contracts/README.md) | AI/runtime trust objects should stay typed and machine-checkable | `CONFIRMED` |
| Policy surface | [`../../../policy/README.md`](../../../policy/README.md) | AI behavior must stay deny-by-default and runtime-enforced | `CONFIRMED` |
| Schema boundary | [`../../../schemas/README.md`](../../../schemas/README.md) | Avoids inventing a second schema home for trust-bearing objects | `CONFIRMED` |
| Workflow lane | [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) | Any future merge gates, attestation, eval, or proof automation belong here | `CONFIRMED` |
| GitHub security policy | [`../../../.github/SECURITY.md`](../../../.github/SECURITY.md) | Canonical GitHub-facing disclosure/reporting path | `CONFIRMED` |

### Upstream / downstream reading order

```text
../../README.md
  └─ ../README.md
      ├─ ../threat-model.md
      ├─ ../prompt-injection/README.md
      ├─ ../prompt-injection-defense.md
      ├─ ../supply-chain/README.md
      ├─ ../vulnerability-management.md
      └─ THIS FILE
             ├─ ../../../contracts/README.md
             ├─ ../../../policy/README.md
             ├─ ../../../schemas/README.md
             └─ ../../../.github/workflows/README.md
```

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Accepted inputs

This lane accepts material that is specifically about **AI-bearing trust surfaces**.

| Accepted input | What belongs here |
|---|---|
| Model origin and admission notes | Where a model, embedding model, tokenizer, or adapter came from; intended role; digest/provenance expectations; review burden |
| Runtime boundary rules | Local/private runtime placement, governed API membrane, no-direct-client-path rules, container/runtime isolation notes |
| Prompt/input hardening links | Secure handling of retrieved text, user prompts, tool context, and model-facing instructions when discussed as part of the AI runtime chain |
| AI-specific release proof expectations | What an AI-bearing release must prove before promotion or public exposure |
| Evaluation expectations | Negative-path tests, citation-failure tests, abstain/deny behavior, stale-scope or partial-coverage behavior |
| AI-specific advisories | Public-safe warnings about model/runtime misuse, provenance drift, prompt-boundary failure, or uncited answer risk |
| Trust-object guidance | `EvidenceBundle`, `RuntimeResponseEnvelope`, `DecisionEnvelope`, `CorrectionNotice`, and related AI-relevant object families |
| Public-safe mitigation notes | Contributor instructions that reduce AI/runtime risk without exposing secrets or exploitable internals |

---

## Exclusions

This lane is **not** the dumping ground for everything adjacent to AI.

| Exclusion | Put it here instead |
|---|---|
| General dependency or container provenance docs with no AI/runtime angle | [`../supply-chain/README.md`](../supply-chain/README.md) |
| Generic threat-model text not specific to AI/runtime boundaries | [`../threat-model.md`](../threat-model.md) |
| Prompt-injection content focused on user input, retrieval attacks, or system-prompt conflict | [`../prompt-injection/README.md`](../prompt-injection/README.md) and [`../prompt-injection-defense.md`](../prompt-injection-defense.md) |
| Vulnerability intake, disclosure, or remediation process docs | [`../vulnerability-management.md`](../vulnerability-management.md) |
| Live secrets, endpoints, tokens, hostnames, internal registries, or unpublished incident evidence | keep out of public docs |
| Machine-readable schemas themselves | [`../../../contracts/README.md`](../../../contracts/README.md) or verified schema home after merge-time confirmation |
| Rego bundles, test harnesses, or workflow YAML | `../../../policy/`, `../../../tests/`, `../../../.github/workflows/` |
| Free-form benchmark marketing or uncited vendor capability claims | do not place in repo docs |

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Current verified snapshot

During this revision, the current public `main` view of this lane was still very thin.

| Item | Current public posture |
|---|---|
| `docs/security/ai-supply-chain/README.md` | Scaffold-only README observed |
| `docs/security/ai-supply-chain/` | No additional child files were directly visible from the directory page during drafting |
| `/docs/` ownership | Docs ownership resolves to `@bartytime4life` |
| `.github/workflows/` | README visible; checked-in workflow YAML was not visible on current public `main` during drafting |
| `contracts/` | README-backed contract surface exists |
| `schemas/` | README-only public surface still visible; schema-home ambiguity remains a live documentation concern |

> [!NOTE]
> This README is intentionally written so it can replace a scaffold **without** pretending the lane already has mounted policy bundles, fixture-backed evaluation, or merge-blocking automation.

---

## Directory tree

### Current verified snapshot

```text
docs/security/ai-supply-chain/
└── README.md
```

### PROPOSED growth shape

Only add narrower files when there is both a named owner and an executable neighbor surface to keep them honest.

```text
docs/security/ai-supply-chain/
├── README.md
├── model-origin-and-admission.md
├── runtime-containment.md
├── adapter-boundary.md
├── evaluation-and-negative-fixtures.md
└── provenance-and-correction.md
```

> [!TIP]
> Keep this lane compact. If a proposed file mostly duplicates prompt-injection, supply-chain, policy, or vulnerability material, link outward instead of branching inward.

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Quickstart

Use this sequence before editing or extending the lane.

```bash
# 1) Read the wider security subtree first
sed -n '1,240p' docs/security/README.md
sed -n '1,240p' docs/security/threat-model.md
sed -n '1,240p' docs/security/supply-chain/README.md
sed -n '1,240p' docs/security/vulnerability-management.md

# 2) Read secure-AI neighbors
sed -n '1,240p' docs/security/prompt-injection/README.md
sed -n '1,240p' docs/security/prompt-injection-defense.md

# 3) Inspect this lane as it exists on your branch
find docs/security/ai-supply-chain -maxdepth 3 -type f | sort
sed -n '1,260p' docs/security/ai-supply-chain/README.md

# 4) Inspect the enforcement-adjacent surfaces
sed -n '1,240p' contracts/README.md
sed -n '1,240p' policy/README.md
sed -n '1,240p' schemas/README.md
sed -n '1,240p' .github/workflows/README.md
sed -n '1,240p' .github/SECURITY.md

# 5) Before claiming implementation, verify the tree directly
git ls-files docs/security/ai-supply-chain
git ls-files .github/workflows
git ls-files contracts
git ls-files schemas
```

### Minimum review questions

1. Does the change describe a **trust-bearing AI/runtime surface**, or is it really a prompt-injection, supply-chain, policy, or vulnerability doc?
2. Does the change keep **implementation claims proportional** to visible repo evidence?
3. Does the change preserve the **governed API membrane** and fail-closed posture?
4. Does the change make negative outcomes easier to test and explain?
5. Does the change avoid creating a second, drifting schema vocabulary?

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Usage

| Task | Start here | Then verify |
|---|---|---|
| Explain what “AI supply chain” means in KFM | this file | [`../README.md`](../README.md), [`../threat-model.md`](../threat-model.md) |
| Document model/runtime containment | this file | [`../../../policy/README.md`](../../../policy/README.md), branch-local runtime/config surfaces |
| Document prompt-boundary and hostile-input risk | [`../prompt-injection/README.md`](../prompt-injection/README.md) | [`../prompt-injection-defense.md`](../prompt-injection-defense.md), then return here for runtime chain implications |
| Document dependency, base-image, attestation, or release provenance concerns | [`../supply-chain/README.md`](../supply-chain/README.md) | workflow lane and release docs |
| Document AI-specific vulnerability discovery or remediation | [`../vulnerability-management.md`](../vulnerability-management.md) | then add cross-link here only if the vulnerability changes the AI/runtime trust model |
| Draft machine-checkable AI/runtime objects | [`../../../contracts/README.md`](../../../contracts/README.md) | [`../../../schemas/README.md`](../../../schemas/README.md) and verified schema location |
| Describe future merge gates or eval automation | this file for lane intent | [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) for actual workflow placement |

---

## Diagram

```mermaid
flowchart TD
    U[User or calling surface] --> API[Governed API membrane]
    API --> POL[Policy evaluation]
    API --> EV[Evidence resolution<br/>EvidenceRef -> EvidenceBundle]
    EV --> ADAPT[Inference adapter]
    ADAPT --> MODEL[Local or private model runtime]
    MODEL --> ADAPT
    ADAPT --> ENV[RuntimeResponseEnvelope]
    POL --> ENV
    ENV --> OUT{Primary runtime outcome}
    OUT -->|ANSWER| A[Bounded cited response]
    OUT -->|ABSTAIN| B[Insufficient support]
    OUT -->|DENY| C[Policy-blocked action]
    OUT -->|ERROR| D[Operational failure]
    A --> PUB[Release proof / correction lineage]
    B --> PUB
    C --> PUB
    D --> PUB

    U -. no direct path .-> MODEL
    MODEL -. no direct read .-> CANON[Canonical stores / RAW / WORK / unpublished state]
```

### Reading rule

The diagram is the governing mental model for this lane:

- clients talk to the **governed API**, not to the model runtime
- the model runtime works only on **admissible scoped context**
- outputs become accountable through a **typed response envelope**
- negative outcomes are **valid system behavior**
- release proof and correction visibility continue **after** the answer is generated

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Control surfaces

### AI supply-chain control map

| Control area | KFM obligation | Primary neighbor surface | Current posture |
|---|---|---|---|
| Model origin and identity | Track source, digest, intended role, and review burden before admission | [`../supply-chain/README.md`](../supply-chain/README.md) | `CONFIRMED doctrine` / implementation depth `UNKNOWN` |
| Runtime containment | Keep model runtime behind the governed API; no direct client path | [`../threat-model.md`](../threat-model.md), [`../../../policy/README.md`](../../../policy/README.md) | `CONFIRMED doctrine` / implementation depth `UNKNOWN` |
| Prompt and input boundary | Prevent hostile or stale input from silently changing scope, policy, or release visibility | [`../prompt-injection/README.md`](../prompt-injection/README.md) | adjacent lane `CONFIRMED` |
| Evidence-bounded synthesis | Retrieve, cite, verify, and abstain rather than improvise | [`../../../contracts/README.md`](../../../contracts/README.md), `tests/` when verified | `CONFIRMED doctrine` / executable proof `UNKNOWN` |
| Runtime accountability | Emit bounded primary outcomes and visible surface state | this file + contract surfaces | `CONFIRMED doctrine` / schema inventory `UNKNOWN` |
| Release and correction | Preserve proof, rollback, stale-state, and correction lineage for AI-bearing surfaces | [`../supply-chain/README.md`](../supply-chain/README.md), [`../vulnerability-management.md`](../vulnerability-management.md) | `CONFIRMED doctrine` / automation `UNKNOWN` |
| Dependency/container trust | Watch packages, base images, registries, and build artifacts without confusing them with epistemic trust | [`../supply-chain/README.md`](../supply-chain/README.md) | broader lane `CONFIRMED` |
| Policy vocab and fixtures | Keep reasons, obligations, valid/invalid samples, and negative-path tests machine-checkable | [`../../../policy/README.md`](../../../policy/README.md), [`../../../contracts/README.md`](../../../contracts/README.md), [`../../../.github/workflows/README.md`](../../../.github/workflows/README.md) | docs visible, enforcement `UNKNOWN` |

### Minimum trust objects for this lane

| Object family | Why this lane cares | Current posture |
|---|---|---|
| `EvidenceBundle` | The bounded support package for any answer, story excerpt, or export preview | doctrinally named; repo implementation `UNKNOWN` |
| `RuntimeResponseEnvelope` | Makes AI/runtime outcomes accountable instead of implicit | doctrinally named; schema inventory `UNKNOWN` |
| `DecisionEnvelope` | Carries machine-readable policy result, reasons, obligations, and audit linkage | doctrinally named; execution surface `UNKNOWN` |
| `ReleaseManifest` / `ReleaseProofPack` | Prevents AI-bearing release from becoming a trust-the-docs gesture | doctrinally named; checked-in proof example `UNKNOWN` |
| `CorrectionNotice` | Keeps stale, withdrawn, replaced, or corrected AI-bearing outputs visibly linked | doctrinally named; mounted examples `UNKNOWN` |
| Valid / invalid fixtures | Proves fail-closed behavior under missing evidence, citation failure, denial, and stale scope | `PROPOSED` but high-priority |

### Allowed vs disallowed posture

| Allowed in KFM | Not allowed in KFM |
|---|---|
| Local/private model runtime behind the membrane | Direct public client traffic to the model runtime |
| Bounded synthesis over admissible evidence | Model improvisation in place of evidence |
| Derived retrieval/search/vector layers as helpers | Derived layers becoming sovereign truth |
| Visible negative outcomes (`ABSTAIN`, `DENY`, `ERROR`) | Hiding failure behind confident prose |
| Public-safe summaries with correction lineage | Publishing uncited answers as authoritative |
| Replaceable inference adapter | Hard-coding the product around one runtime vendor |
| Role-aware, policy-aware release | Model access to RAW, WORK, QUARANTINE, or unpublished candidate state |

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Task list & definition of done

### Immediate tasks for this README

- [ ] Replace the scaffold with lane-specific substance.
- [ ] Keep cross-links aligned to live neighbor docs.
- [ ] State the current public-branch snapshot plainly.
- [ ] Preserve the no-direct-client-to-model rule.
- [ ] Name the trust objects this lane depends on.
- [ ] Keep workflow, schema, and policy claims proportional to visible evidence.
- [ ] Avoid inventing a second schema-home or duplicate trust vocabulary.
- [ ] Keep all mitigation guidance public-safe.

### Definition of done for this lane

A change in this directory is ready when all of the following are true:

| Gate | What must be true |
|---|---|
| Scope gate | The content is genuinely about AI-bearing trust surfaces, not a duplicate of another security lane |
| Evidence gate | Confirmed repo state is separated from doctrine and from proposed next steps |
| Boundary gate | The governed API membrane and fail-closed posture remain explicit |
| Linkage gate | The lane points readers to contracts, policy, workflows, and adjacent secure-AI docs without inventing implementation |
| Testability gate | Negative outcomes, reason/obligation vocab, and proof objects are easier to test after the change |
| Drift gate | The change does not create a parallel schema, policy, or terminology universe |
| Publication gate | The document stays public-safe and does not reveal secrets, sensitive endpoints, or unpublished incident evidence |

> [!IMPORTANT]
> A polished README is not sufficient evidence of a live control. For KFM, the lane only becomes operationally strong when documentation, contracts, fixtures, policy, and workflow gates agree.

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## FAQ

### Is this the same as dependency security?

No. Dependency and container provenance are part of this lane, but KFM’s AI supply chain is wider: it includes model admission, runtime containment, evidence access, accountable outputs, and correction lineage.

### Does this README prove the repo already runs AI-specific workflow gates?

No. This file documents the lane and its required posture. It should not be read as proof that attestation, evaluation, or merge-blocking automation is already checked in and active.

### Why is prompt injection only adjacent, not central, here?

Because prompt injection is one attack class inside a larger chain. This lane stays focused on the whole governed AI/runtime path; the narrower hostile-input tactics live in the prompt-injection docs.

### Why do negative outcomes get so much space?

Because fail-closed behavior is part of KFM’s trust model. An honest abstain, deny, or visible error is more correct than a polished unsupported answer.

### Why keep AI behind the governed API membrane?

Because KFM’s model runtime is subordinate to evidence, policy, release state, and correction state. Direct client-to-model paths would bypass those trust-bearing layers.

[Back to top](#kfm-ai-supply-chain--governed-model-runtime)

---

## Appendix

<details>
<summary><strong>Current evidence used to shape this lane</strong></summary>

### Public repo surfaces inspected during drafting

- `docs/security/ai-supply-chain/README.md`
- `docs/security/README.md`
- `docs/security/supply-chain/README.md`
- `docs/security/threat-model.md`
- `docs/security/vulnerability-management.md`
- `docs/security/prompt-injection/README.md`
- `docs/security/prompt-injection-defense.md`
- `contracts/README.md`
- `schemas/README.md`
- `policy/README.md`
- `.github/CODEOWNERS`
- `.github/workflows/README.md`
- `.github/SECURITY.md`

### Doctrine overlays used for lane depth

- KFM canonical master-reference material
- KFM secure-AI / Ollama integration guidance
- KFM repo-grounded research sprint
- KFM components / category atlas material

### Merge-time verification reminders

- Replace `YYYY-MM-DD` placeholders in the KFM meta block.
- Replace `doc_id` placeholder with the repo’s chosen durable document identifier.
- Re-check whether this directory now contains child files before merging.
- Re-check whether `.github/workflows/` now contains live YAML so the snapshot text stays truthful.
- Re-check whether `contracts/` vs `schemas/` ownership or placement rules have been resolved.
- Re-check whether any narrower AI lane docs were added elsewhere first, to avoid duplication.

</details>
