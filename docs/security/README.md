<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<REVIEW-REQUIRED-UUID>
title: Kansas Frontier Matrix Security & Supply Chain Governance
type: standard
version: v1
status: review
owners: @bartytime4life
created: <REVIEW-REQUIRED>
updated: 2026-04-05
policy_label: <REVIEW-REQUIRED>
related: [../README.md, ../../SECURITY.md, ../../.github/SECURITY.md, ./threat-model.md, ./vulnerability-management.md, ./promotion-contract.md, ./prompt-injection/README.md, ./prompt-injection-defense.md, ./ai-supply-chain/README.md, ./ai-receipts/README.md, ./supply-chain/README.md, ./vulns/README.md, ./bulletins/README.md, ./react2shell/README.md, ./react2shell-advisory/README.md]
tags: [kfm, security, supply-chain, governance, docs]
notes: [target inferred from uploaded draft; current public main tree rechecked; doc_id, created date, policy_label, and finer-grained security ownership still need verification]
[/KFM_META_BLOCK_V2] -->

# Kansas Frontier Matrix Security & Supply Chain Governance

Evidence-first entry point for KFM security doctrine, supply-chain trust, promotion discipline, advisories, and bounded runtime-security guidance under `docs/security/`.

> [!IMPORTANT]
> **Status:** active  
> **Owners:** `@bartytime4life` *(confirmed broad `/docs/` CODEOWNERS coverage; any narrower security-specific split is still `NEEDS VERIFICATION`)*  
> ![Status](https://img.shields.io/badge/status-active-brightgreen) ![Path](https://img.shields.io/badge/path-docs%2Fsecurity%2FREADME.md-blue) ![Tree](https://img.shields.io/badge/tree-public__main-2ea44f) ![Posture](https://img.shields.io/badge/posture-fail--closed-critical) ![Trust](https://img.shields.io/badge/trust-membrane-informational) ![Evidence](https://img.shields.io/badge/evidence-public__tree%2Bdoctrine-success) ![Owners](https://img.shields.io/badge/owners-bartytime4life-lightgrey)  
> **Repo fit:** `docs/security/README.md` → upstream [`../README.md`](../README.md) · disclosure entrypoint [`../../SECURITY.md`](../../SECURITY.md) · canonical disclosure [`../../.github/SECURITY.md`](../../.github/SECURITY.md)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Security lanes](#security-lanes--control-areas) · [Task list](#task-list--quality-gates--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

> [!WARNING]
> This revision is grounded in two visible layers: attached KFM doctrine and the current public `main` tree under `docs/security/`. Checked-in Markdown and directory shape can be treated as `CONFIRMED`. Platform-only settings, required checks, unpublished workflow YAML, runtime exposure, app permissions, secrets, and enforcement wiring remain `UNKNOWN` or `NEEDS VERIFICATION` until reverified in a live checkout and runtime context.

> [!CAUTION]
> Older subtree inventory in this README drifted toward corpus-only paths such as `./secrets-policy.md` and `./supply-chain.md`. The current public tree instead exposes `./ai-receipts/` and `./promotion-contract.md`, while those older sibling paths are not currently visible here. Keep cross-links aligned to the checked-in tree, not to older index assumptions.

## Scope

`docs/security/` is KFM’s cross-lane security hub.

This directory exists so contributors, reviewers, operators, and future maintainers can answer five questions quickly:

1. What security laws govern KFM?
2. Which deeper lane owns the topic I am changing?
3. What must change together when security-significant behavior changes?
4. Which statements here are current checked-in repo fact, and which are still doctrine, target state, or unknown?
5. Where should disclosure, promotion, runtime-boundary, advisory, and proof-object guidance live without collapsing into one shapeless security blob?

KFM’s security posture is not perimeter-first. It is publication-first, evidence-first, and fail-closed:

- security begins with governed publication, not surface polish
- public and normal clients do not bypass governed APIs
- authoritative truth stays distinct from rebuildable derivatives
- policy belongs in merge gates **and** runtime behavior
- negative outcomes such as **deny**, **abstain**, **generalize**, **withdraw**, and **correction-pending** are valid trust-preserving states
- docs, contracts, receipts, and runbooks are production security surfaces

### KFM security laws this README must preserve

| KFM rule | What it means for `docs/security/` |
|---|---|
| Trust membrane | Security docs must keep client, reviewer, and runtime boundary rules inspectable: public and normal clients stay downstream of governed APIs, policy, release state, and evidence resolution. |
| Fail-closed posture | Missing evidence, broken provenance, unresolved rights, weak redaction, or failed gates should block publish, promote, respond, or disclose rather than degrade silently. |
| Authoritative vs. derived separation | Graph, vector, tile, cache, search, summary, embedding, and AI outputs must not be documented as sovereign truth. |
| Evidence remains operational | Security guidance must preserve drill-through from claim to evidence path, not only conceptual commentary. |
| Policy in CI and runtime | This subtree should explain both merge/promotion controls and request-time enforcement expectations, without pretending prose is the enforcement layer. |
| Docs as production surface | Security-significant changes should update docs, contracts, tests, runbooks, and release evidence together. |
| UNKNOWN stays visible | Unverified repo or runtime claims must be called out, not polished into certainty. |

[Back to top](#kansas-frontier-matrix-security--supply-chain-governance)

## Repo fit

| Field | Value |
|---|---|
| Path | `docs/security/README.md` |
| Role in repo | Root README for the security documentation subtree; routing surface into narrower lanes for supply-chain trust, promotion, bounded AI, advisories, bulletins, and package-family issues |
| Upstream docs | [`../README.md`](../README.md) |
| Disclosure surfaces | [`../../SECURITY.md`](../../SECURITY.md) → public entrypoint; [`../../.github/SECURITY.md`](../../.github/SECURITY.md) → canonical disclosure policy |
| Adjacent governed surfaces | [`../../contracts/`](../../contracts/) · [`../../policy/`](../../policy/) · [`../../schemas/`](../../schemas/) · [`../../tests/`](../../tests/) · [`../../tools/`](../../tools/) · [`../../pipelines/`](../../pipelines/) · [`../../.github/`](../../.github/) |
| Primary downstream lanes currently visible | [`./threat-model.md`](./threat-model.md) · [`./vulnerability-management.md`](./vulnerability-management.md) · [`./promotion-contract.md`](./promotion-contract.md) · [`./prompt-injection/README.md`](./prompt-injection/README.md) · [`./prompt-injection-defense.md`](./prompt-injection-defense.md) · [`./ai-supply-chain/README.md`](./ai-supply-chain/README.md) · [`./ai-receipts/README.md`](./ai-receipts/README.md) · [`./supply-chain/README.md`](./supply-chain/README.md) · [`./vulns/README.md`](./vulns/README.md) · [`./bulletins/README.md`](./bulletins/README.md) · [`./react2shell/README.md`](./react2shell/README.md) · [`./react2shell-advisory/README.md`](./react2shell-advisory/README.md) |
| What this file should not do | Replace executable policy, duplicate the full disclosure policy, or act like proof that hidden platform controls already exist |

### How this README fits the wider KFM docs set

Use this file as the subtree map and evidence boundary statement.

Do **not** use it as a substitute for:

- the actual disclosure policy
- the promotion contract
- lane-specific package or bulletin leaves
- executable policy bundles
- machine-readable contracts and validation fixtures
- runtime proof

## Accepted inputs

Content that belongs here or under this subtree:

- threat-model and trust-boundary documentation
- cross-cutting security doctrine tied to KFM concepts such as trust membrane, fail-closed promotion, evidence-bearing rollback, and citation-negative testing
- supply-chain integrity guidance: signatures, attestations, SBOMs, provenance, release manifests, digest-first identity, dependency-confusion controls
- security-facing promotion and runtime-admission guidance when documented as reviewer/operator material
- prompt-injection, hostile-input, secure-AI, and AI runtime provenance controls
- AI receipt and proof-object guidance for AI-assisted runs, runtime answers, and AI-derived artifacts
- vulnerability-management, advisory, and bulletin-routing guidance
- package-family or framework issue-family lanes such as `react2shell/` or `vulns/node-forge/`
- secret-boundary, signing-key, and credential-handling guidance **as boundary rules**, not as secret material
- reviewer/operator-facing guidance for promotion gates, rollback, correction, evidence reconstruction, and release-visible trust behavior

## Exclusions

Content that does **not** belong here:

| Keep out of `docs/security/` | Where it goes instead |
|---|---|
| Secrets, private keys, tokens, live credentials, signed URLs | Secret manager, deployment environment, or another controlled runtime secret boundary — never docs |
| Executable policy as prose-only documentation | Keep enforcement in policy bundles, contracts, schemas, tests, and runtime decision paths; mirror intent here |
| Raw incident artifacts, restricted evidence, exact sensitive locations | Governed evidence stores and steward-only review lanes |
| Broad canonical architecture copied verbatim | Canonical KFM manuals and architecture references |
| Package or framework exposure claims without manifest, lockfile, SBOM, or runtime proof | Keep them `UNKNOWN` until the checked-out branch proves them |
| Disclosure instructions that drift from root security policy | Keep canonical disclosure in [`../../.github/SECURITY.md`](../../.github/SECURITY.md) and keep [`../../SECURITY.md`](../../SECURITY.md) aligned |
| Repo/runtime claims not directly evidenced | Mark as `UNKNOWN` / `NEEDS VERIFICATION` until reverified |

## Current verified snapshot

| Surface | Current public `main` evidence | What not to infer from that evidence |
|---|---|---|
| `docs/security/` root | `README.md`, `promotion-contract.md`, `prompt-injection-defense.md`, `threat-model.md`, `vulnerability-management.md`, plus `ai-receipts/`, `ai-supply-chain/`, `bulletins/`, `prompt-injection/`, `react2shell/`, `react2shell-advisory/`, `supply-chain/`, and `vulns/` | Do not infer runtime enforcement, hidden workflow YAML, or platform-side rulesets |
| `promotion-contract.md` | Public file is visible and self-describes as one governed, fail-closed contract from build to release to runtime admission | Do not treat it as proof of live-tree ownership, workflow anchors, or mounted enforcement wiring |
| `ai-receipts/` | README-only lane currently visible; the lane itself marks `AIReceipt` as a standard draft / proposed object family | Do not infer mounted `AIReceipt` implementation from the docs lane alone |
| `ai-supply-chain/` | README-only lane currently visible | Do not infer live signing, eval gates, or runtime containment from prose alone |
| `prompt-injection/` | README-only lane currently visible | Do not infer live retrieval guards or runtime prompt filters without code/policy proof |
| `react2shell/` and `react2shell-advisory/` | Both lanes are visible and README-backed | Do not infer current framework exposure without manifest, lockfile, or runtime evidence |
| `supply-chain/` | README plus visible `dependency-confusion/`, `reference-repos/`, `shai-hulud-2.0/`, and `sigstore-cosign-v3/` | Do not infer checked-in workflow execution from lane docs |
| `vulns/` | README, `apache-tika-cve-2025-66516.md`, and `node-forge/` are visible | Advisory docs do not prove active dependency reachability |
| `bulletins/` | README plus `android/` bulletin subtree are visible | Do not infer broader vendor or platform coverage beyond checked-in leaves |
| Disclosure surfaces | Both [`../../SECURITY.md`](../../SECURITY.md) and [`../../.github/SECURITY.md`](../../.github/SECURITY.md) are public | Do not let subtree docs invent a third canonical disclosure path |
| Ownership | Broad `/docs/` coverage resolves to `@bartytime4life` on current public `CODEOWNERS` | Do not infer narrower security-specific owner splits without direct proof |

[Back to top](#kansas-frontier-matrix-security--supply-chain-governance)

## Directory tree

> [!NOTE]
> This is a **current public-main snapshot** re-opened during this revision, not a guess from the earlier PDF-only corpus boundary.

```text
docs/security/
├── README.md
├── promotion-contract.md
├── prompt-injection-defense.md
├── threat-model.md
├── vulnerability-management.md
├── ai-receipts/
│   └── README.md
├── ai-supply-chain/
│   └── README.md
├── bulletins/
│   ├── README.md
│   └── android/
│       ├── README.md
│       └── 2025-12-android-security-bulletin.md
├── prompt-injection/
│   └── README.md
├── react2shell/
│   └── README.md
├── react2shell-advisory/
│   └── README.md
├── supply-chain/
│   ├── README.md
│   ├── dependency-confusion/
│   │   ├── README.md
│   │   ├── checks/
│   │   ├── examples/
│   │   └── policy/
│   ├── reference-repos/
│   │   └── README.md
│   ├── shai-hulud-2.0/
│   │   ├── README.md
│   │   ├── indicators/
│   │   ├── protections/
│   │   └── workflows/
│   └── sigstore-cosign-v3/
│       └── README.md
└── vulns/
    ├── README.md
    ├── apache-tika-cve-2025-66516.md
    └── node-forge/
        ├── README.md
        └── CVE-2025-12816.md
```

## Quickstart

Start here when a change touches trust, release, runtime exposure, advisories, or supply-chain integrity.

1. Read this README first to identify the owning lane.
2. Re-open the current tree and disclosure surfaces before widening any claim.
3. Update the narrower security doc that owns the topic.
4. Change executable artifacts in the same governed stream when behavior changes: policy bundles, contracts, fixtures, tests, runbooks, and release evidence.
5. Keep checked-in tree facts `CONFIRMED` and keep platform/runtime state `UNKNOWN` until reverified.
6. Repair link drift in the same PR when the subtree shape changes.

```bash
# Verify the live security tree before widening claims
find docs/security -maxdepth 4 -type f | sort

# Re-open the core subtree router and disclosure surfaces
sed -n '1,240p' docs/security/README.md
sed -n '1,240p' SECURITY.md
sed -n '1,260p' .github/SECURITY.md
sed -n '1,220p' .github/CODEOWNERS

# Re-open adjacent enforcement surfaces when behavior changes
find contracts policy schemas tests tools pipelines -maxdepth 4 -type f 2>/dev/null | sort | sed -n '1,240p'
```

```text
Minimum security-doc change set for one governed PR

- docs/security/README.md                       # orientation and cross-links
- affected deeper security doc(s)              # threat model / prompt injection / AI / advisories / supply chain
- affected contracts or policy bundles         # executable enforcement, not prose only
- affected test fixtures or gates              # especially negative fixtures and denial paths
- affected runbook / rollback / correction note
- release-evidence references updated together
```

## Usage

### Use this README when you need to…

| Task | Start here | Then go deeper |
|---|---|---|
| Explain KFM’s cross-cutting security posture | This README | [`./threat-model.md`](./threat-model.md) |
| Route a private report or disclosure question | This README | [`../../SECURITY.md`](../../SECURITY.md) → [`../../.github/SECURITY.md`](../../.github/SECURITY.md) |
| Document runtime-boundary or bypass risks | This README | [`./threat-model.md`](./threat-model.md) |
| Work on promotion, release proof, or runtime admission language | This README | [`./promotion-contract.md`](./promotion-contract.md) and [`./supply-chain/README.md`](./supply-chain/README.md) |
| Add signing, attestation, digest, SBOM, or provenance guidance | This README | [`./supply-chain/sigstore-cosign-v3/README.md`](./supply-chain/sigstore-cosign-v3/README.md) |
| Document dependency-confusion or package-origin defenses | This README | [`./supply-chain/dependency-confusion/README.md`](./supply-chain/dependency-confusion/README.md) |
| Add prompt-injection or hostile-input guidance | This README | [`./prompt-injection/README.md`](./prompt-injection/README.md) and [`./prompt-injection-defense.md`](./prompt-injection-defense.md) |
| Add AI runtime provenance or bounded-model guidance | This README | [`./ai-supply-chain/README.md`](./ai-supply-chain/README.md) |
| Document AI run receipts or answer-proof objects | This README | [`./ai-receipts/README.md`](./ai-receipts/README.md) |
| Document secret, signing-key, or credential boundary rules | This README | [`./threat-model.md`](./threat-model.md) and [`./promotion-contract.md`](./promotion-contract.md) |
| Add or update advisories / CVE leaves | This README | [`./vulns/README.md`](./vulns/README.md) or the package/framework-specific leaf lane |
| Route date-keyed platform bulletins | This README | [`./bulletins/README.md`](./bulletins/README.md) |
| Document framework-issue families like React2Shell | This README | [`./react2shell/README.md`](./react2shell/README.md) and [`./react2shell-advisory/README.md`](./react2shell-advisory/README.md) |

### Review posture for this subtree

| Label | Use it when… |
|---|---|
| **CONFIRMED** | The statement is directly supported by attached doctrine or current public-tree evidence |
| **INFERRED** | The statement is a conservative read of current evidence, but not directly re-proved as live runtime/platform fact |
| **PROPOSED** | The statement describes target-state contracts, controls, or file organization consistent with KFM doctrine |
| **UNKNOWN** | The statement is not supported strongly enough to present as current reality |
| **NEEDS VERIFICATION** | Exact path, owner, policy label, workflow, check, enforcement hook, or runtime linkage still needs direct proof |

> [!TIP]
> If a link is not visible in the checked-in tree, do not quietly keep it because an older corpus index once mentioned it. Fix the router now, and preserve the older path only as historical context in the appendix if it still matters.

## Diagram

```mermaid
flowchart LR
    A[Attached KFM doctrine<br/>trust membrane / fail-closed / evidence-first] --> B[docs/security/README.md]
    C[Current public main<br/>docs/security tree] --> B

    B --> D[threat-model.md]
    B --> E[promotion-contract.md]
    B --> F[supply-chain/README.md]
    B --> G[prompt-injection/README.md]
    B --> H[prompt-injection-defense.md]
    B --> I[ai-supply-chain/README.md]
    B --> J[ai-receipts/README.md]
    B --> K[vulnerability-management.md]
    B --> L[vulns/README.md]
    B --> M[bulletins/README.md]
    B --> N[react2shell/README.md]
    B --> O[react2shell-advisory/README.md]

    P[/SECURITY.md] --> Q[/.github/SECURITY.md]
    Q -.canonical disclosure.-> B

    D --> R[Contracts / Policy / Tests / Release proof]
    E --> R
    F --> R
    G --> R
    I --> R
    J --> R
    K --> R
    L --> R
    M --> R
```

## Security lanes & control areas

| Area | Core concern | KFM-specific obligation | Primary doc lane |
|---|---|---|---|
| Disclosure path | Private intake, canonical handoff, public reporting drift | Keep subtree docs aligned with root and gatehouse security policy; do not invent a third canonical lane | [`../../SECURITY.md`](../../SECURITY.md), [`../../.github/SECURITY.md`](../../.github/SECURITY.md) |
| Threat model | Bypass, direct store access, over-privileged runtime, rights leakage | Keep the trust membrane explicit and test non-bypass | [`./threat-model.md`](./threat-model.md) |
| Promotion contract | Build → release → runtime admission trust | Keep promotion fail-closed and evidence-backed; missing receipt, signature, policy, approval, or runtime recheck should deny | [`./promotion-contract.md`](./promotion-contract.md) |
| Supply-chain integrity | Mutable tags, weak provenance, unsigned artifacts, build drift | Prefer digest identity, SBOMs, attestations, signatures, and evidence-bearing promotion | [`./supply-chain/README.md`](./supply-chain/README.md) |
| Secure AI / prompt injection | Scope creep, hostile input, unsafe retrieval, uncited synthesis | Retrieve, cite, verify, abstain; keep model runtime subordinate to evidence and policy | [`./prompt-injection/README.md`](./prompt-injection/README.md), [`./prompt-injection-defense.md`](./prompt-injection-defense.md), [`./ai-supply-chain/README.md`](./ai-supply-chain/README.md) |
| AI receipts / proof objects | AI-assisted runs, runtime answers, AI-derived artifacts | Keep AI-bearing outputs auditable, typed, and reviewable without implying they already drive production gates | [`./ai-receipts/README.md`](./ai-receipts/README.md) |
| Vulnerability lifecycle | Intake, triage, remediation, correction visibility | Keep remediation and correction linked to real evidence rather than to advisory prose alone | [`./vulnerability-management.md`](./vulnerability-management.md), [`./vulns/README.md`](./vulns/README.md) |
| Bulletins | Date-keyed platform/vendor advisories | Keep bulletin routing distinct from package-family remediation and from the canonical disclosure lane | [`./bulletins/README.md`](./bulletins/README.md) |
| Package / framework issue families | Specific packages or framework families such as `node-forge` or React2Shell | Use narrow leaf lanes so remediation stays precise without overstating exposure | [`./vulns/node-forge/README.md`](./vulns/node-forge/README.md), [`./react2shell/README.md`](./react2shell/README.md), [`./react2shell-advisory/README.md`](./react2shell-advisory/README.md) |
| Docs as production surface | Drift between docs, contracts, tests, and runtime | Security-significant behavior changes must update docs in the same governed stream | this README |

[Back to top](#kansas-frontier-matrix-security--supply-chain-governance)

## Task list — quality gates & definition of done

A security-doc change in this subtree is not done when prose looks finished. It is done when the relevant trust obligations are still inspectable and the router still matches the checked-in tree.

### Definition of done

- [ ] The affected document states the **security boundary** or trust obligation clearly.
- [ ] The README links resolve against the current checked-in tree.
- [ ] Any behavior-significant change is reflected in the matching contract, policy, test, runbook, or release-evidence reference.
- [ ] The change does not silently turn a **PROPOSED** or **UNKNOWN** repo/runtime claim into asserted fact.
- [ ] Public-surface implications are documented where relevant: evidence state, freshness, denial/abstention, review-required, redaction/generalization.
- [ ] Negative paths are documented where relevant, not only the happy path.
- [ ] Disclosure routing remains aligned with [`../../SECURITY.md`](../../SECURITY.md) and [`../../.github/SECURITY.md`](../../.github/SECURITY.md).
- [ ] Security-significant docs remain usable as operational material, not just narrative commentary.

### Release-sensitive gates this README assumes exist or should exist

| Gate family | Why it matters to this subtree |
|---|---|
| Schema / contract gate | Security docs should not drift away from machine-checkable envelopes, receipts, and fixtures. |
| Policy bundle gate | Missing evidence, broken provenance, insufficient redaction, or unresolved rights should block merge/promotion. |
| Documentation gate | Security-significant behavior changes should update docs, examples, and runbooks together. |
| Citation-negative / runtime denial tests | The system should prove it abstains, denies, or errors rather than fabricating support. |
| Release assembly gate | Visibility change should require a complete release manifest or proof pack. |
| Correction drill | Withdrawal, supersession, or narrowing should preserve lineage and update surface state. |
| Supply-chain verification gate | Security-sensitive artifacts should have visible provenance, digest identity, and verification hooks where applicable. |
| Link / tree drift gate | Subtree routers must match checked-in paths; stale links should fail review early. |

> [!TIP]
> KFM’s strongest doctrine still points toward a small next-artifact set rather than broader conceptual prose: contract starter files, policy bundles, valid/invalid fixtures, proof objects, and one governed thin slice proved end to end. Keep this README aligned with that bias.

## FAQ

### Is this README proof that the controls are implemented?

No. This README is a governed orientation surface. It explains doctrine, current public-tree shape, and where narrower security material lives. It is not a substitute for mounted contracts, executable policy, tests, manifests, platform configuration, or runtime proof.

### Why does this revision remove links to `secrets-policy.md` and `supply-chain.md`?

Because those sibling paths are not currently visible in the public `docs/security/` tree that was re-opened for this revision. Keeping them here as live links would overstate current repo shape. If either path returns in a checked-out branch, add it back in the same PR that restores the file.

### Why link both `/SECURITY.md` and `/.github/SECURITY.md`?

Because both are public today, and the root file routes reporters into the canonical disclosure policy in `/.github/SECURITY.md`. This README should preserve that handoff rather than improvise a competing disclosure route.

### Why link `promotion-contract.md` from the security root?

Because the current public subtree exposes it as a security-adjacent contract surface for build, release, and runtime admission. That makes it part of the router, even though its own file still declares live enforcement wiring `NEEDS VERIFICATION`.

### Why keep calling out `UNKNOWN` and `NEEDS VERIFICATION`?

Because KFM’s trust posture is evidence-first. Public-tree visibility is not the same thing as runtime proof, and substantive prose is not the same thing as enforcement.

## Appendix

<details>
<summary><strong>Current public-tree drift repaired by this revision</strong></summary>

- Added now-visible security surfaces to the router: `ai-receipts/`, `promotion-contract.md`, `bulletins/README.md`, `bulletins/android/README.md`, and `vulns/node-forge/README.md`.
- Removed live links to sibling paths that are not visible in the current public `docs/security/` tree: `secrets-policy.md` and `supply-chain.md`.
- Collapsed the earlier corpus-index speculative tree into a public-main snapshot and moved non-public/runtime claims back to `UNKNOWN` or `NEEDS VERIFICATION`.

</details>

<details>
<summary><strong>Compact KFM security doctrine checklist</strong></summary>

```text
Use this subtree to keep these KFM rules visible:

- Security begins with governed publication.
- Public and normal clients do not bypass governed APIs.
- Derived layers are not authoritative by default.
- Policy belongs in CI and runtime, not only in prose.
- Missing evidence, broken provenance, unresolved rights, or weak redaction should fail closed.
- Promotion is a governed state transition, not a file move.
- Model runtimes stay behind the trust membrane.
- Correction and rollback must be evidence-bearing.
- Docs, contracts, receipts, and runbooks are production security surfaces.
- UNKNOWN stays visible until direct proof exists.
```

</details>

<details>
<summary><strong>Verification backlog for this README</strong></summary>

- Confirm the canonical `kfm://` document identifier.
- Confirm created date and repo-preferred updated-date convention.
- Confirm whether the repo wants `policy_label: public` or a narrower internal label for public docs.
- Re-check whether security subtree ownership becomes narrower than broad `/docs/` fallback.
- Verify whether `secrets-policy.md` is intentionally retired, relocated, or simply absent on current public `main`.
- Verify whether current or private branches expose workflow YAML, policy bundles, contracts, schemas, fixtures, or release proof objects that should be cross-linked from this README.
- Verify whether `promotion-contract.md` becomes a mounted enforcement surface or remains a doctrine/documentation contract.
- Replace any remaining `NEEDS VERIFICATION` markers during the merge PR if stronger branch-local evidence is available.

</details>

[Back to top](#kansas-frontier-matrix-security--supply-chain-governance)
