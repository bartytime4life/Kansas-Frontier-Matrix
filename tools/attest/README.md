# attest

Proof-pack, digest, and attestation helper surface for governed KFM release evidence.

> [!IMPORTANT]
> **Status:** experimental  
> **Owners:** `@bartytime4life` *(current `/tools/` owner inherited from visible `CODEOWNERS`; narrower lane-specific ownership is not separately declared in the public tree)*  
> **Path:** `tools/attest/README.md`  
> **Repo fit:** child lane of [`../README.md`](../README.md) · upstream [`../../README.md`](../../README.md) · governance [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) · downstream callers [`../../.github/workflows/README.md`](../../.github/workflows/README.md) and [`../../scripts/README.md`](../../scripts/README.md) · authority neighbors [`../../contracts/README.md`](../../contracts/README.md), [`../../policy/README.md`](../../policy/README.md), and [`../../tests/README.md`](../../tests/README.md)  
> **Evidence posture:** doctrine-grounded · repo-grounded for current public `main` subtree fact · deeper local checkout, workflow settings, and mounted helper inventory remain bounded  
> **Current public snapshot:** `tools/attest/` is **README-only** on the current public tree; this README is already substantive and should be revised in place rather than reset to scaffold text  
> **Role:** reusable helper lane for verification, summarization, proof-pack inspection, and attestation-adjacent release-evidence support  
> **Not this lane:** canonical policy storage, schema authority, secret custody, or hidden publish logic
>
> ![status](https://img.shields.io/badge/status-experimental-orange)
> ![owner](https://img.shields.io/badge/owner-%40bartytime4life-6f42c1)
> ![lane](https://img.shields.io/badge/lane-tools%2Fattest-4051b5)
> ![subtree](https://img.shields.io/badge/public%20subtree-README--only-lightgrey)
> ![posture](https://img.shields.io/badge/posture-read--only%20by%20default-red)
>
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Attest helper behavior contract](#attest-helper-behavior-contract) · [Diagram](#diagram) · [Operating tables](#operating-tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!NOTE]
> The parent [`tools/README.md`](../README.md) remains the family contract for the wider helper surface. This file narrows that contract to `attest/` while grounding sibling-family context in the live public `tools/` listing.

---

## Scope

`tools/attest/` is the narrow KFM helper lane for reusable commands that inspect, verify, summarize, or package **release-evidence support artifacts** without quietly becoming the release system itself.

In KFM terms, this lane belongs **downstream of doctrine** and **adjacent to** — not above — the contract, policy, workflow, script, and runtime trust surfaces.

### What belongs here

Helpers in this directory should generally do one or more of the following:

- verify digests, manifests, proof objects, or attestation payloads
- summarize release evidence for reviewers or CI logs
- assemble small support bundles for review or release checks
- check that declared proof objects are present, shaped correctly, and internally consistent
- emit machine-readable pass/fail results that higher-level callers can consume

### What this lane must protect

- **fail-closed behavior** over best-effort ambiguity
- **read-only verification by default**
- **discoverability** of release-evidence support logic
- **clear caller boundaries** between tools, scripts, tests, and workflows
- **no secret ownership drift** into helper code
- **no silent publish path**

### Evidence posture used in this README

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Directly supported by the current public repo tree or by adjacent repo/doctrine material already visible |
| **INFERRED** | Strongly implied by repo structure and KFM doctrine, but not directly implemented here yet |
| **PROPOSED** | Recommended starter pattern for this lane |
| **UNKNOWN** | Not proven strongly enough from current public repo evidence |
| **NEEDS VERIFICATION** | Important enough to surface before merge or rollout |

[Back to top](#attest)

---

## Repo fit

`tools/attest/` should feel native inside the existing repo lattice, not like an isolated scripts bin.

| Direction | Surface | Why it matters |
|---|---|---|
| Parent | [`../README.md`](../README.md) | Defines the overall `tools/` family contract and helper-lane boundaries |
| Upstream | [`../../README.md`](../../README.md) | Root repo posture: governed, evidence-first, map-first, time-aware |
| Governance | [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | Current visible ownership coverage for `/tools/` |
| Downstream caller | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Workflow YAML may call helpers here, but should not become the only place their logic exists |
| Downstream caller | [`../../scripts/README.md`](../../scripts/README.md) | Scripts may orchestrate helper use, but reusable attestation logic should remain inspectable here |
| Adjacent authority | [`../../contracts/README.md`](../../contracts/README.md) | Contracts define proof-object shape; `tools/attest/` may verify them, not replace them |
| Adjacent authority | [`../../policy/README.md`](../../policy/README.md) | Policy owns allow/deny logic, reasons, and obligations |
| Adjacent proof | [`../../tests/README.md`](../../tests/README.md) | Fixtures and negative-path coverage belong here |
| Neighbor lane | [`../validators/README.md`](../validators/README.md) | General deterministic validation helpers |
| Neighbor lane | [`../ci/README.md`](../ci/README.md) | Reviewer-facing CI summaries over already-governed artifacts |
| Neighbor lane | [`../diff/README.md`](../diff/README.md) | Deterministic comparison helpers for manifests, receipts, and snapshots |
| Neighbor lane | [`../catalog/README.md`](../catalog/README.md) | Metadata and catalog QA helpers |
| Neighbor lane | [`../probes/README.md`](../probes/README.md) | Read-mostly inspection and freshness helpers |
| Neighbor lane | [`../docs/README.md`](../docs/README.md) | Documentation-tooling lane for README/report maintenance and structure checks |

### Working interpretation

`tools/attest/` is a **helper surface**, not a sovereign authority surface.

- **Contracts** define the shape.
- **Policy** defines allowed outcomes and obligations.
- **Tests** prove pass/fail behavior.
- **Workflows** call helpers.
- **Scripts** orchestrate local or operator flows.
- **`tools/attest/`** should provide the reusable verification or summarization building blocks.

[Back to top](#attest)

---

## Accepted inputs

The parent `tools/` guidance and adjacent repo surfaces imply that this lane should accept **evidence-support inputs**, not arbitrary application data.

### Accepted here

| Input class | Examples | Status |
|---|---|---|
| Digests and checksum material | `sha256` digests, spec-hash outputs, checksum manifests, manifest-linked file hashes | **CONFIRMED / INFERRED** |
| Release proof metadata | `ReleaseManifest`, `ReleaseProofPack`, run receipts, rollback refs, correction refs | **INFERRED** |
| Runtime and review trust objects | `DecisionEnvelope`, `EvidenceBundle`, `RuntimeResponseEnvelope`, `CorrectionNotice` | **INFERRED** |
| Review-safe fixtures | valid/invalid sample objects for local checks and tests | **INFERRED** |
| CI/local invocation parameters | input paths, output report paths, strict/fail flags, format selectors | **PROPOSED** |
| Optional provenance attachments | SBOMs, attestation statements, provenance JSON, transparency-log refs, support bundles | **PROPOSED** |

### Preferred input posture

- explicit file paths over hidden discovery
- declared schema/profile versions over implicit assumptions
- release-scoped references over ad hoc loose files
- public-safe fixtures over production secrets

[Back to top](#attest)

---

## Exclusions

This directory should stay sharp. The following do **not** belong here as primary responsibility:

| Excluded from `tools/attest/` | Put it here instead |
|---|---|
| Canonical schema authority | `../../contracts/` |
| Policy bundles, reason codes, obligation registries | `../../policy/` |
| Long-lived review artifacts or release objects as storage | canonical release / data / evidence surfaces |
| Secret keys, signing identities, private trust roots | infra / secret manager / environment-specific secure storage |
| Key-management policy or workload-identity ownership | security / infra / runtime boundary |
| Workflow orchestration logic | `../../.github/workflows/` or `../../scripts/` |
| Runtime publish/promote logic | governed runtime / release lane |
| Ad hoc “misc signing helpers” scattered across repo | centralize in `tools/attest/` once real helpers exist |
| Hidden enforcement by UI or shell behavior alone | `../../policy/`, `../../tests/`, and caller lanes |

> [!CAUTION]
> A helper in `tools/attest/` may **support** release evidence. It must not quietly become the release authority, the policy engine, or the only place where provenance meaning survives.

[Back to top](#attest)

---

## Current verified snapshot

| Evidence item | Status | Why it matters |
|---|---|---|
| `tools/attest/README.md` exists on current public `main` | **CONFIRMED** | This is a real lane surface, not a hypothetical path |
| No additional public files are currently visible under `tools/attest/` | **CONFIRMED** | Keeps executable helper claims bounded |
| This README is already substantive on public `main` | **CONFIRMED** | Future edits should revise in place rather than revert to scaffold text |
| The live public `tools/` listing confirms sibling families `attest/`, `catalog/`, `ci/`, `diff/`, `docs/`, `probes/`, and `validators/` | **CONFIRMED** | Grounds relative links and current family context from the tree itself |
| The parent `tools/README.md` still reserves attestation helpers as a named lane | **CONFIRMED** | Keeps this README anchored to the broader family contract even where older snapshot prose has drifted |
| `/tools/` ownership is covered by current visible `CODEOWNERS` | **CONFIRMED** | Grounds the owners line for this file |
| Public `.github/workflows/` remains README-only on visible `main` | **CONFIRMED** | Prevents overclaiming checked-in workflow callers |
| Public Actions history, as documented in the workflows README, includes deleted filenames such as `release-evidence.yml` | **CONFIRMED historical signal** | Useful naming/context clue, but not proof that current public `main` contains those YAML files |
| Exact executable helper inventory, workflow callers, trust-root handling, and any live attestation pipeline | **UNKNOWN / NEEDS VERIFICATION** | These are not derivable from current public tree inspection alone |
| Any repo-ratified Cosign / in-toto / OCI attestation profile | **UNKNOWN / NEEDS VERIFICATION** | Doctrine and idea packets discuss them, but the checked-in public lane does not yet prove adoption here |
| Any live release proof-pack examples on current public `main` | **UNKNOWN / NEEDS VERIFICATION** | Promotion, rollback, and publication proof remain conceptual until a real example is surfaced |

[Back to top](#attest)

---

## Directory tree

### Current public subtree

```text
tools/attest/
└── README.md
```

### Confirmed parent family context

```text
tools/
├── attest/
├── catalog/
├── ci/
├── diff/
├── docs/
├── probes/
├── validators/
└── README.md
```

### PROPOSED landing shape for the first real helper set

> [!NOTE]
> The shape below is **PROPOSED**, not a claim about the mounted tree.

```text
tools/attest/
├── README.md
├── verify_*.py|sh|mjs         # narrow verification entrypoints
├── summarize_*.py|mjs         # reviewer-facing summaries
├── fixtures/                  # tiny public-safe examples only if needed
└── examples/                  # optional invocation examples
```

The key rule is not the filename pattern itself. The key rule is that the helper inventory stays:

- small
- explicit
- reviewable
- easy to invoke from CI or scripts
- impossible to confuse with canonical storage or secret custody

[Back to top](#attest)

---

## Quickstart

Start by verifying the current repo state before you add executable content.

### 1) Inspect the surrounding surfaces

```bash
sed -n '1,260p' tools/README.md
sed -n '1,180p' .github/CODEOWNERS
sed -n '1,260p' .github/workflows/README.md
sed -n '1,240p' contracts/README.md
sed -n '1,240p' policy/README.md
sed -n '1,240p' tests/README.md
sed -n '1,240p' scripts/README.md
```

### 2) Confirm the current subtree and live sibling-family context

```bash
find tools/attest -maxdepth 2 \( -type f -o -type d \) | sort
find tools -maxdepth 2 -type d | sort
```

### 3) Search for existing release-evidence terminology before inventing anything new

```bash
rg -n "attest|attestation|proof[- ]pack|release manifest|ReleaseManifest|EvidenceBundle|RuntimeResponseEnvelope|CorrectionNotice|SBOM|cosign|in-toto|provenance" \
  tools contracts policy tests scripts .github docs -S 2>/dev/null
```

### 4) Verify whether workflow callers actually exist

```bash
find .github/workflows -maxdepth 2 -type f | sort
```

### 5) Add the smallest useful helper first

Good first helpers usually look like one of these:

1. **Verifier** — checks that required proof objects or digests are present and consistent
2. **Summarizer** — emits reviewer-friendly and CI-friendly structured results
3. **Bundle checker** — verifies that a release-evidence support bundle is complete enough to review

[Back to top](#attest)

---

## Usage

### Use this lane for narrow, testable helper responsibilities

A helper added here should answer a small question cleanly.

Examples:

- “Does this release manifest point to all required proof objects?”
- “Do declared digests match the referenced files?”
- “Is a required provenance artifact missing?”
- “Can we emit one structured summary for CI logs and reviewers?”

### Keep the call chain explicit

A recommended call pattern is:

```text
workflow / script / local operator command
            ↓
     tools/attest helper
            ↓
 machine-readable result + human-readable summary
            ↓
 review / gate / follow-up action
```

### Prefer verification before signing

In this repo state, the safer first move is usually:

- verify
- summarize
- gate
- only then consider richer signing or attestation flows

That order keeps the lane useful without overclaiming secret custody, key management, or supply-chain authority that the current public repo does not yet prove.

### Illustrative output shape

```json
{
  "tool": "verify_release_evidence",
  "status": "fail",
  "blocking": true,
  "subject": "release_manifest.json",
  "checks": [
    {
      "id": "digest-present",
      "result": "pass"
    },
    {
      "id": "proof-pack-linked",
      "result": "fail",
      "message": "no reviewable proof object linked from manifest"
    }
  ]
}
```

> [!NOTE]
> The JSON above is an **illustrative example**, not a confirmed mounted contract.

[Back to top](#attest)

---

## Attest helper behavior contract

A helper in this lane should keep its behavior small, explicit, and safe to reason about in Git review.

| Rule | Expected posture |
|---|---|
| Subject selection | The thing being checked should be explicit: manifest path, bundle path, receipt path, or equivalent ref |
| Determinism | Same inputs should produce the same result shape, exit status, and blocking posture |
| Read-only default | A helper may write only a caller-chosen report path; it should not mutate canonical truth or promotion state |
| Machine-readable first | Primary output should be stable JSON or equivalent structured output suitable for CI, tests, or scripts |
| Reviewer-readable second | Optional human summary should be concise, safe to print, and easy to link from PR or release review |
| Profile visibility | Declared profile/schema/version assumptions should be echoed rather than buried |
| Secret posture | Helpers must not become owners of signing keys, trust roots, or private identity material |
| Unsupported state | Unknown formats or unsupported profiles should fail clearly rather than bluff verification |
| Log safety | CI-facing summaries should avoid leaking unpublished evidence, private bundle contents, or secret-bearing internals |

### Minimal result classes worth preserving

| Condition | Expected helper behavior |
|---|---|
| Required artifact missing | fail clearly; blocking when caller says the artifact is mandatory |
| Digest mismatch or broken linkage | fail clearly; include the failed check id and subject |
| Optional artifact absent | emit an explicit non-pass state only if the caller marked it optional |
| Unsupported profile/version | return a clear unsupported result instead of pretending to verify |
| Signing or trust-root ownership required to continue | stop and hand control back to the proper security/runtime lane |

> [!WARNING]
> An attestation helper may eventually wrap external verifiers. It must still remain a reusable helper boundary, not the sovereign owner of release trust.

[Back to top](#attest)

---

## Diagram

```mermaid
flowchart LR
  C[contracts/]
  P[policy/]
  T[tests/fixtures]
  S[scripts/]
  W[.github/workflows/]
  D[manifests / receipts / proof-pack members]
  A[tools/attest/]

  R[machine-readable result]
  H[human-readable summary]
  G[review / merge gate / release check]

  C --> A
  P --> A
  T -->|exercise| A
  S -->|invoke| A
  W -->|invoke when present| A
  D --> A

  A --> R
  A --> H
  R --> G
  H --> G

  G -. must not bypass .-> U[governed publication path]
```

### Interpretation

- `tools/attest/` sits in the **helper** layer.
- It may block or inform a gate.
- It must **not** become a hidden publish path.
- It should remain legible to both machines and reviewers.

[Back to top](#attest)

---

## Operating tables

### Helper classes for this lane

| Helper class | Primary job | Typical outputs | Status |
|---|---|---|---|
| Verification helper | Check integrity, presence, linkage, and consistency of proof-support objects | pass/fail JSON, exit code, concise report | **PROPOSED first-wave** |
| Summary helper | Turn raw verification state into reviewer-facing summaries | markdown/text/JSON summary | **PROPOSED first-wave** |
| Support-bundle checker | Confirm a review bundle is complete enough to inspect | completeness report | **PROPOSED** |
| Advanced signing wrapper | Call external signing / attestation tooling without owning trust roots | wrapped execution report | **NEEDS VERIFICATION / governance-heavy** |

### Design obligations

| Concern | Required posture |
|---|---|
| Determinism | Same inputs should yield the same verification result |
| Failure behavior | Block clearly; do not bluff |
| Output shape | Machine-readable first, human-readable second |
| Secret handling | No committed secrets; no hidden key ownership |
| Reviewability | Small CLI surface, narrow purpose, explicit inputs |
| Caller clarity | Document whether the helper is called by scripts, tests, or workflows |
| Boundary integrity | Never replace contracts, policy, tests, or governed publication logic |

### KFM object touchpoints

| Object family | Likely contact with `tools/attest/` |
|---|---|
| `ReleaseManifest` / `ReleaseProofPack` | Primary verification target |
| `ReviewRecord` | Optional approval-chain continuity checks |
| `DecisionEnvelope` | Policy-result linkage checks |
| `ProjectionBuildReceipt` | Derived-surface linkage checks when promoted scope is packaged downstream |
| `EvidenceBundle` | Support-path or completeness checks where relevant |
| `RuntimeResponseEnvelope` | Optional downstream linkage checks |
| `CorrectionNotice` | Continuity / supersession verification after release changes |

[Back to top](#attest)

---

## Task list

### Definition of done for the first executable helper

- [ ] The helper has **one narrow job**
- [ ] Caller surface is documented (`scripts/`, workflow, local operator, or tests)
- [ ] Inputs are explicit and reviewable
- [ ] Exit behavior is fail-closed for blocking checks
- [ ] Machine-readable output shape is stable enough to test
- [ ] At least one valid and one invalid example exists where appropriate
- [ ] Adjacent docs are updated if the helper adds a new repo expectation
- [ ] No secret material or environment-specific trust roots are committed
- [ ] The helper does **not** publish, promote, or mutate canonical truth directly
- [ ] Any advanced signing or provenance pattern is clearly labeled **PROPOSED** until ratified and evidenced

### Merge checks worth asking before landing code here

- [ ] Does this belong in `tools/attest/`, or is it actually a contract, policy, test, workflow, or script concern?
- [ ] Is the helper verifying or merely asserting?
- [ ] Could a reviewer understand what failed from the output alone?
- [ ] Does the helper keep KFM’s trust membrane intact?
- [ ] Does it stay useful even if supply-chain tooling changes later?

[Back to top](#attest)

---

## FAQ

### Why a dedicated `tools/attest/` instead of scattered helper scripts?

Because the parent `tools/` guidance already gives this family a stable purpose. Centralizing this helper class makes release-evidence support easier to discover, test, and govern.

### Does this README claim active attestation automation already exists?

No. The current public tree evidences a README-only subtree and a substantive lane contract, not a checked-in executable helper inventory or current public workflow wiring.

### Should this directory own signing keys or trust roots?

No. That would collapse helper logic and sensitive operational authority into one place.

### What is the safest first helper to add?

Usually a **verification** or **summary** helper around manifests, digests, receipts, or proof-support completeness.

### Can this lane emit blocking CI results?

Yes — that is a good fit. But the caller lane should still be explicit, and the helper should remain a reusable building block rather than the whole workflow.

### Do proof objects live here?

Helpers live here. Durable proof objects should live in the appropriate governed release / evidence / data surfaces instead of accumulating as ad hoc tool-side storage.

[Back to top](#attest)

---

## Appendix

<details>
<summary><strong>Appendix A — Current-state reading rule</strong></summary>

Treat this README as:

1. a **directory contract**
2. a **boundary clarifier**
3. a **landing guide** for the first real helper

Do **not** treat it as proof that executable attestation tooling, CI wiring, signing identity management, or release-proof automation is already implemented.

</details>

<details>
<summary><strong>Appendix B — Historical workflow signal is not current inventory</strong></summary>

The public workflows README documents prior GitHub Actions history and deleted filenames such as `release-evidence.yml`.

Use that as:

- a naming and scope clue
- a hint that release-evidence automation has been thought about before
- a reason to keep future helper naming legible

Do **not** use it as proof that the current public `main` branch still ships those YAML files.

</details>

<details>
<summary><strong>Appendix C — Optional advanced patterns (explicitly PROPOSED)</strong></summary>

These patterns may eventually become relevant here, but none should be implied as current repo fact without direct evidence:

- Cosign-based signing or verification wrappers
- in-toto / SLSA-style provenance verification
- OCI-attached geospatial artifact proof flows
- SBOM verification helpers
- reviewer-facing provenance bundle assembly for release lanes

Use them only when:

- the repo has chosen the pattern explicitly
- adjacent contracts, policy, and tests exist
- the caller lane is documented
- secret handling and trust-root ownership are resolved elsewhere

</details>

<details>
<summary><strong>Appendix D — Recommended writing style for future helper docs</strong></summary>

When new helpers are added under this lane, prefer:

- one helper = one responsibility
- one short example invocation
- one expected pass path
- one expected fail path
- one machine-readable output example
- one caller note describing where it is used

</details>
