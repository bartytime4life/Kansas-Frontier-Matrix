<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<REVIEW-REQUIRED-UUID>
title: node-forge vulnerability lane
type: standard
version: v1
status: review
owners: @bartytime4life
created: 2026-03-22
updated: 2026-03-30
policy_label: public
related: [docs/security/vulns/README.md, docs/security/README.md, docs/security/vulnerability-management.md, SECURITY.md, .github/SECURITY.md, .github/CODEOWNERS, .github/dependabot.yml, .github/workflows/README.md, docs/security/vulns/node-forge/CVE-2025-12816.md]
tags: [kfm, security, vulnerability, node-forge]
notes: [doc_id still needs direct assignment; dates are taken from current public file history; policy_label is inferred from the public-main checked-in doc surface; direct or transitive package presence still requires branch-local verification]
[/KFM_META_BLOCK_V2] -->

# `node-forge` vulnerability lane

Package-specific triage, verification, and remediation guidance for `node-forge` under KFM’s security vulnerability subtree.

> **Status:** active directory · README revision  
> **Owners:** `@bartytime4life`  
> ![status](https://img.shields.io/badge/status-active-0a7d5a) ![package](https://img.shields.io/badge/package-node--forge-1f6feb) ![path](https://img.shields.io/badge/path-docs%2Fsecurity%2Fvulns%2Fnode--forge-8250df) ![trust](https://img.shields.io/badge/trust-fail--closed-red) ![evidence](https://img.shields.io/badge/evidence-public__main%20%2B%20official%20advisories-lightgrey) ![owner](https://img.shields.io/badge/owner-bartytime4life-blue)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `docs/security/vulns/node-forge/README.md` → parent [`../README.md`](../README.md) · security hub [`../../README.md`](../../README.md) · lifecycle lane [`../../vulnerability-management.md`](../../vulnerability-management.md) · disclosure handoff [`../../../../SECURITY.md`](../../../../SECURITY.md) · canonical disclosure [`../../../../.github/SECURITY.md`](../../../../.github/SECURITY.md) · workflow posture [`../../../../.github/workflows/README.md`](../../../../.github/workflows/README.md) · child advisory [`./CVE-2025-12816.md`](./CVE-2025-12816.md)

> [!IMPORTANT]
> This README documents the **`node-forge` vulnerability lane**. It does **not** prove that `node-forge` is currently present in the active KFM dependency graph.
>
> Current public-main evidence confirms the lane directory, the child advisory note, the parent vulnerability index, the root-to-`.github` security-policy handoff, `/docs/` ownership via `/.github/CODEOWNERS`, npm-focused Dependabot coverage for `/`, `/apps/*`, and `/packages/*`, and a workflow lane whose public directory listing is currently `README.md` only.
>
> Direct or transitive package presence still requires branch-local verification against manifests, lockfiles, SBOM output, or dependency-tree evidence.

## Scope

This README keeps **package-family vulnerability handling** for `node-forge` readable, reviewable, and repo-native without pretending that an advisory is the same thing as a proven runtime exposure.

Use this file to answer five questions quickly:

1. Does the active branch actually contain `node-forge`, directly or transitively?
2. Which official advisory or advisory cluster is relevant?
3. Which KFM app, package, or image owns the remediation?
4. What evidence closes the lane: manifest diff, lockfile diff, scan output, SBOM diff, test result, release note, or rollback note?
5. What remains **CONFIRMED**, **INFERRED**, **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION** after review?

In KFM terms, this directory is a **security documentation surface**, not a substitute for executable enforcement. The lane should stay aligned with the trust membrane, fail-closed release behavior, disclosure discipline, correction visibility, and evidence-first review posture already established under `docs/security/` and the repository security-policy surfaces.

[Back to top](#node-forge-vulnerability-lane)

## Repo fit

**Path:** `docs/security/vulns/node-forge/README.md`

**Role in repo:** package-family vulnerability lane for `node-forge` under the governed `docs/security/vulns/` subtree.

| Direction | Path | Status | Why it matters |
|---|---|---|---|
| Upstream | [`../README.md`](../README.md) | **CONFIRMED** | Parent vulnerability index is substantive and currently lists `node-forge/README.md` and `node-forge/CVE-2025-12816.md` in the visible directory tree. |
| Upstream | [`../../README.md`](../../README.md) | **CONFIRMED** | Cross-cutting security doctrine, supply-chain posture, trust-membrane language, and subtree expectations live here. |
| Upstream | [`../../vulnerability-management.md`](../../vulnerability-management.md) | **CONFIRMED** · **draft lifecycle surface** | Broader intake, triage, containment, remediation, validation, disclosure, and correction guidance belongs there; this file stays dependency-specific. |
| Upstream | [`../../../../SECURITY.md`](../../../../SECURITY.md) | **CONFIRMED** · **handoff surface** | Root security entrypoint exists to route readers quickly into the canonical GitHub security policy. |
| Upstream | [`../../../../.github/SECURITY.md`](../../../../.github/SECURITY.md) | **CONFIRMED** · **canonical disclosure path** | Public repository policy treats `/.github/SECURITY.md` as the canonical disclosure surface and prefers GitHub Security reporting first. |
| Upstream | [`../../../../.github/CODEOWNERS`](../../../../.github/CODEOWNERS) | **CONFIRMED** | `/docs/` currently resolves to `@bartytime4life`, which is the strongest visible ownership signal for this lane. |
| Upstream | [`../../../../.github/dependabot.yml`](../../../../.github/dependabot.yml) | **CONFIRMED** | npm dependency-update coverage for `/`, `/apps/*`, and `/packages/*` is the strongest visible public signal for where a `node-forge` alert would likely surface. |
| Upstream | [`../../../../.github/workflows/README.md`](../../../../.github/workflows/README.md) | **CONFIRMED** · **docs-only workflow lane** | Public `main` currently shows `.github/workflows/README.md` only. Treat workflow claims as bounded unless checked-in YAMLs or live settings prove more. |
| Downstream | [`./CVE-2025-12816.md`](./CVE-2025-12816.md) | **CONFIRMED** · **draft advisory note** | Child note already records advisory IDs, the fixed floor `>= 1.3.2`, and keeps KFM repo impact at `UNKNOWN` until real dependency evidence is attached. |

### Current truth posture for this lane

| Label | What it means here |
|---|---|
| **CONFIRMED** | Public `main` contains `docs/security/vulns/node-forge/`, the child `CVE-2025-12816.md` note, the parent `docs/security/vulns/README.md`, root and `.github` security-policy surfaces with explicit handoff, `/docs/` ownership in `CODEOWNERS`, npm Dependabot coverage for `/`, `/apps/*`, and `/packages/*`, and a public `.github/workflows/` directory listing that is currently `README.md` only. |
| **INFERRED** | If `node-forge` is present, it is most likely to appear in a JavaScript workspace under repo root, `apps/`, or `packages/`, because those are the npm-scanned surfaces currently declared in `.github/dependabot.yml`. |
| **PROPOSED** | Add child notes for the broader November 2025 `node-forge` ASN.1 advisory cluster only if the package is actually relevant to the checked-out branch. |
| **UNKNOWN** | Whether the active branch currently ships `node-forge` at all, where it enters the dependency graph, and whether any reachable KFM path accepts vulnerable ASN.1-bearing input through it. |
| **NEEDS VERIFICATION** | Exact manifest path, exact lockfile owner, exact runtime reachability, exact remediation PR, active alert state, and any merge-blocking automation tied specifically to this lane. |

[Back to top](#node-forge-vulnerability-lane)

## Accepted inputs

Content that belongs in this package lane:

- official advisory references for `node-forge` that materially affect KFM review or remediation
- direct vs. transitive dependency findings
- sanitized manifest, lockfile, SBOM, dependency-review, or dependency-tree evidence that proves where the package enters the graph
- remediation notes tied to a real branch change
- test, scan, validation, and release evidence that closes the lane
- rollback, supersession, or correction notes if a remediation is reverted or replaced
- cross-links to package-specific child advisory files in this directory

## Exclusions

Content that does **not** belong here:

| Keep out of this README | Where it goes instead |
|---|---|
| Claims that KFM currently uses `node-forge` without manifest, lockfile, SBOM, or dependency-tree proof | Record as **UNKNOWN** until branch-local verification exists |
| Generic cryptography guidance not tied to `node-forge` review | Broader security docs or architecture references |
| Secrets, tokens, private incident payloads, or sensitive scan artifacts | Secret-handling boundaries, restricted evidence stores, or steward-only review lanes |
| Full disclosure policy, inbound reporting mailbox, or SLA details | Root [`SECURITY.md`](../../../../SECURITY.md) and canonical [`../../../../.github/SECURITY.md`](../../../../.github/SECURITY.md) |
| Package-manager-specific commands presented as universal truth | Mark them as illustrative and run only after confirming the active workspace toolchain |
| Workflow-enforcement claims without checked-in or platform-level proof | Keep in `/.github/workflows/README.md` or label **UNKNOWN / NEEDS VERIFICATION** |
| Final release proof-pack content | Release evidence, changelog, PR, or owning runbook |

[Back to top](#node-forge-vulnerability-lane)

## Current verified snapshot

This table records the public-branch evidence used to revise this file. It is intentionally narrow.

| Surface | Public `main` state used for this rewrite | Status |
|---|---|---|
| `docs/security/vulns/node-forge/README.md` | Present as the package-lane README path under `docs/security/vulns/node-forge/` | **CONFIRMED** |
| `docs/security/vulns/node-forge/CVE-2025-12816.md` | Present; child note records package, advisory IDs, and fixed floor `>= 1.3.2` while keeping repo impact at `UNKNOWN` | **CONFIRMED** |
| `docs/security/vulns/README.md` | Present; parent lane is a governed index and the visible directory tree includes `node-forge/README.md` and `node-forge/CVE-2025-12816.md` | **CONFIRMED** |
| `/.github/CODEOWNERS` | Present; `/docs/` is assigned to `@bartytime4life` | **CONFIRMED** |
| `/.github/dependabot.yml` | Present; npm updates are configured for `/`, `/apps/*`, and `/packages/*` | **CONFIRMED** |
| `/.github/workflows/README.md` | Present; public `.github/workflows/` directory listing shows `README.md` only | **CONFIRMED** |
| `/SECURITY.md` + `/.github/SECURITY.md` | Both present; root file delegates to `/.github/SECURITY.md`, and the `.github` file declares itself canonical | **CONFIRMED** |
| Direct or transitive `node-forge` package presence in the active branch | Not proven from the public-main evidence opened for this rewrite | **UNKNOWN** |

[Back to top](#node-forge-vulnerability-lane)

## Directory tree

```text
docs/security/vulns/node-forge/
├── README.md
└── CVE-2025-12816.md
```

### Current lane condition

The package lane already exists, and the current public directory listing shows exactly two files at this path.

That means the remaining gap is **dependency-graph proof**, not lane existence.

No additional `node-forge` child advisory files are currently visible in the public-main directory listing.

[Back to top](#node-forge-vulnerability-lane)

## Quickstart

1. **Verify package presence before saying anything stronger than `UNKNOWN`.**
2. **Determine whether the path is direct, transitive, or absent.**
3. **Check the full official advisory cluster, not just the first CVE you noticed.**
4. **If present, update the owning manifest or lockfile path and record the evidence here and in the child advisory note(s).**
5. **Close the lane with validation and release evidence, not only with a version bump.**

### Repo-wide verification loop

```bash
# repo-wide package search
find . \( -name package.json -o -name package-lock.json -o -name pnpm-lock.yaml -o -name yarn.lock \) -print | sort

git grep -n "node-forge" -- . ':!docs/security/**' || true

grep -RIn '"node-forge"' apps packages . 2>/dev/null | sed -n '1,120p'
```

### Workspace-specific follow-up (illustrative)

```bash
# run only the command family that matches the verified workspace toolchain
npm ls node-forge || true
pnpm why node-forge || true
yarn why node-forge || true
```

> [!NOTE]
> Do **not** run all three package-manager command families blindly in the same workspace. First confirm what the owning app or package actually uses.

### Workflow-boundary reminder

```bash
# verify what the public workflow lane actually shows before documenting enforcement
sed -n '1,220p' .github/workflows/README.md 2>/dev/null || true
find .github/workflows -maxdepth 2 -mindepth 1 | sort
```

[Back to top](#node-forge-vulnerability-lane)

## Usage

Use this README when:

- GitHub Advisory, Dependabot, SBOM, dependency review, or manual package review flags `node-forge`
- a PR changes a manifest or lockfile in a way that introduces, upgrades, or removes `node-forge`
- a release review needs a short package-level answer before diving into a child CVE note
- a maintainer needs to know whether the repo has already documented the `node-forge` advisory cluster

### Working rule

If the active branch does **not** contain `node-forge`, say so plainly.

Do not leave the lane ambiguous. Either:

- keep it as a historical or watchlist reference and mark absence clearly, or
- remove / archive the lane with review if the package is irrelevant to KFM’s current dependency graph

### Minimum useful change set when `node-forge` is actually present

- owning manifest or lockfile diff
- this README updated with direct / transitive / absent status
- child advisory file(s) updated with package-specific notes
- validation evidence such as audit output, `why` / `ls` output, SBOM diff, or equivalent
- release note, correction note, or rollback note if the change is release-bearing

## Diagram

```mermaid
flowchart TD
    A[GHSA / NVD alert<br/>or manual package review] --> B[Search manifests and lockfiles]
    B --> C{Is `node-forge` present?}
    C -- No --> D[Record absence clearly<br/>or archive the lane]
    C -- Direct dependency --> E[Update the owning manifest]
    C -- Transitive dependency --> F[Update the parent package<br/>or lockfile path]
    E --> G[Run security checks and tests]
    F --> G
    G --> H[Update README + child CVE doc(s)]
    H --> I[Attach release / rollback / correction evidence]
```

[Back to top](#node-forge-vulnerability-lane)

## Tables

### Repo-grounded lane status

| Item | Status | Notes |
|---|---|---|
| `docs/security/vulns/node-forge/` directory exists | **CONFIRMED** | Present in the public repo tree. |
| `README.md` exists at this path | **CONFIRMED** | Present as the package-lane README path. |
| `CVE-2025-12816.md` exists | **CONFIRMED** | Current child note records advisory facts and keeps repo impact at `UNKNOWN` until proof is attached. |
| Parent `docs/security/vulns/README.md` references this lane | **CONFIRMED** | Parent index and visible tree include both `node-forge/README.md` and `node-forge/CVE-2025-12816.md`. |
| `/docs/` ownership resolves to `@bartytime4life` | **CONFIRMED** | Current `CODEOWNERS` uses `/docs/ @bartytime4life`. |
| Dependabot has npm ecosystem coverage for `/`, `/apps/*`, and `/packages/*` | **CONFIRMED** | Strongest visible public review surface for JavaScript dependency alerts. |
| Canonical disclosure handoff is explicit | **CONFIRMED** | Root `SECURITY.md` delegates to `/.github/SECURITY.md`, and `/.github/SECURITY.md` declares itself canonical. |
| Public `main` exposes checked-in workflow YAML proving merge-blocking vulnerability automation for this lane | **NEEDS VERIFICATION** | Public `.github/workflows/` currently lists `README.md` only. |
| Active branch contains `node-forge` | **UNKNOWN** | Must be proven by manifest, lockfile, SBOM, or dependency-tree inspection. |
| Exact owning app or package | **UNKNOWN** | Not visible from the current public-main evidence opened for this lane. |

### Official advisory cluster worth checking

| Advisory | Severity | Affected versions | Patched version | Lane status |
|---|---:|---|---|---|
| [`CVE-2025-12816`](./CVE-2025-12816.md) / [`GHSA-5gfm-wpxj-wjgq`][ghsa-12816] | High | `< 1.3.2` | `1.3.2` | **CONFIRMED child note** |
| [`CVE-2025-66030`][nvd-66030] / [`GHSA-65ch-62r8-g69g`][ghsa-66030] | Moderate | `< 1.3.2` | `1.3.2` | **PROPOSED child note** |
| [`CVE-2025-66031`][nvd-66031] / [`GHSA-554w-wpv2-vw27`][ghsa-66031] | High | `< 1.3.2` | `1.3.2` | **PROPOSED child note** |

> [!TIP]
> For the current November 2025 official `node-forge` ASN.1 advisory cluster, **`1.3.2` is the minimum patched floor**. If KFM already targets a newer compatible safe version, prefer the newer reviewed version rather than downgrading back to the minimum.

### Remediation decision matrix

| Dependency result | What to do next | What must update together |
|---|---|---|
| **Absent** | Record the absence clearly; decide whether to keep the lane as historical/watchlist material or remove/archive it with review. | README note, issue/PR note if one exists |
| **Direct dependency** | Upgrade the owning manifest to a safe version and regenerate the matching lockfile. | Manifest, lockfile, this README, child CVE note(s), validation evidence |
| **Transitive dependency** | Update the parent package or lockfile path that resolves the vulnerable subtree. | Parent manifest/lockfile, this README, child CVE note(s), validation evidence |
| **Present but not runtime-reachable** | Do not assume “safe enough”; record why exposure is limited and who approved that reasoning. | README, owning advisory note, review evidence |
| **Unclear** | Keep status at **UNKNOWN / NEEDS VERIFICATION** until the graph is proven. | README and PR truth-posture summary |

[Back to top](#node-forge-vulnerability-lane)

## Task list / definition of done

- [ ] direct / transitive / absent status recorded
- [ ] owning manifest or lockfile path named if present
- [ ] official advisory scope checked against the full November 2025 `node-forge` cluster, not just one CVE
- [ ] minimum safe version or reviewed newer safe version recorded
- [ ] child CVE note(s) updated with package-specific impact or absence findings
- [ ] validation evidence attached: audit output, `why` / `ls` output, SBOM diff, or equivalent
- [ ] release, rollback, or correction linkage noted when the change is release-bearing
- [ ] any workflow-enforcement claim is tied to checked-in YAML, platform evidence, or explicitly labeled `NEEDS VERIFICATION`
- [ ] no sentence in this lane silently upgrades `UNKNOWN` package presence into asserted repo fact

> [!WARNING]
> A dependency bump is **not** “done” in KFM merely because the manifest changed. The lane closes only when the package path, advisory scope, validation evidence, and release or rollback linkage are all readable together.

## FAQ

### Does this README prove KFM currently ships `node-forge`?

No.

The lane exists in the repo, but current evidence does **not** yet prove a direct or transitive `node-forge` path in the active branch.

### What version should remediation target?

For the official November 2025 `node-forge` advisory cluster referenced here, the minimum patched version is **`1.3.2`**. If the active repo already targets a newer reviewed safe version, use the newer version after normal compatibility review.

### Why keep a package README when there is already a child CVE file?

Because package lanes age across **multiple advisories**.

The README keeps the package-level logic, ownership questions, verification workflow, and remediation matrix in one place, while child files hold alert-specific detail.

### Why keep this lane self-sufficient even though the parent vulnerability index is now substantive?

Because the parent README is still an index and routing surface.

It should point readers here, but this file remains the home for `node-forge`-specific dependency verification, advisory clustering, and remediation closure criteria.

[Back to top](#node-forge-vulnerability-lane)

## Appendix

<details>
<summary><strong>Package-manager note</strong></summary>

KFM’s currently visible repo evidence confirms **npm ecosystem** Dependabot coverage, but it does **not** by itself prove whether the owning workspace uses npm, pnpm, Yarn, or a mixed setup.

Treat these rules as load-bearing:

- use the command family that matches the checked-out workspace
- regenerate the lockfile that actually governs installation
- do not present a scan from one package manager as proof for another without explaining the boundary
- record the exact file path that changed

</details>

<details>
<summary><strong>Recommended next expansion for this lane</strong></summary>

The current directory already has one child CVE file.

The next useful expansions are small and concrete:

1. keep `./CVE-2025-12816.md` synchronized with actual repo impact, remediation, and closure evidence
2. add child notes for `CVE-2025-66030` and `CVE-2025-66031` if `node-forge` is actually relevant to the active branch
3. add one short “absence confirmed” note if the package is not present, rather than letting the lane drift silently

</details>

[ghsa-12816]: https://github.com/advisories/GHSA-5gfm-wpxj-wjgq
[ghsa-66030]: https://github.com/advisories/GHSA-65ch-62r8-g69g
[ghsa-66031]: https://github.com/advisories/GHSA-554w-wpv2-vw27
[nvd-66030]: https://nvd.nist.gov/vuln/detail/CVE-2025-66030
[nvd-66031]: https://nvd.nist.gov/vuln/detail/CVE-2025-66031
