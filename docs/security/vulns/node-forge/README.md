# `node-forge` vulnerability lane

Package-specific triage, verification, and remediation guidance for `node-forge` under KFM’s security vulnerability subtree.

> **Status:** active directory · README revision  
> **Owners:** `@bartytime4life`  
> ![status](https://img.shields.io/badge/status-active-0a7d5a) ![package](https://img.shields.io/badge/package-node--forge-1f6feb) ![path](https://img.shields.io/badge/path-docs%2Fsecurity%2Fvulns%2Fnode--forge-8250df) ![trust](https://img.shields.io/badge/trust-fail--closed-red) ![evidence](https://img.shields.io/badge/evidence-repo%20tree%20%2B%20official%20advisories-lightgrey) ![owner](https://img.shields.io/badge/owner-bartytime4life-blue)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `docs/security/vulns/node-forge/README.md` → parent [`../README.md`](../README.md) · security hub [`../../README.md`](../../README.md) · policy context [`../../vulnerability-management.md`](../../vulnerability-management.md) · disclosure policy [`../../../../SECURITY.md`](../../../../SECURITY.md) · child advisory [`./CVE-2025-12816.md`](./CVE-2025-12816.md)

> [!IMPORTANT]
> This README documents the **`node-forge` vulnerability lane**. It does **not** prove that `node-forge` is currently present in the active KFM dependency graph.
>
> Current repo evidence confirms the lane directory, this README path, the child advisory stub, `/docs/` ownership via `/.github/CODEOWNERS`, and npm-focused Dependabot coverage for `/`, `/apps/*`, and `/packages/*`. Direct or transitive package presence still requires branch-local verification against manifests and lockfiles.

## Scope

This README exists to keep **package-level vulnerability handling** for `node-forge` readable and reviewable without pretending that a package alert is the same thing as a proven runtime exposure.

Use this file to answer five questions quickly:

1. Does the active branch actually contain `node-forge`, directly or transitively?
2. Which official advisory or advisory cluster is relevant?
3. Which KFM app, package, or image owns the remediation?
4. What evidence closes the lane: manifest diff, lockfile diff, scan output, test result, release note, or rollback note?
5. What remains **CONFIRMED**, **INFERRED**, **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION** after review?

In KFM terms, this directory is a **security documentation surface**, not a substitute for executable enforcement. The vulnerability lane should stay aligned with the trust membrane, fail-closed publication, release evidence, and correction discipline already established in `docs/security/` and the root security policy.

[Back to top](#node-forge-vulnerability-lane)

## Repo fit

**Path:** `docs/security/vulns/node-forge/README.md`

**Role in repo:** package-specific vulnerability lane for `node-forge` under the `docs/security/vulns/` subtree.

| Direction | Path | Status | Why it matters |
|---|---|---|---|
| Upstream | [`../README.md`](../README.md) | **CONFIRMED path** · **scaffold content** | Parent vulnerability index currently exists but remains minimal; this lane must therefore carry its own practical context. |
| Upstream | [`../../README.md`](../../README.md) | **CONFIRMED** | Cross-cutting security doctrine, trust membrane rules, subtree map, and security documentation expectations. |
| Upstream | [`../../vulnerability-management.md`](../../vulnerability-management.md) | **CONFIRMED path** · **scaffold content** | Future home for broader vulnerability process; keep lane-specific content here until that surface is expanded. |
| Upstream | [`../../../../SECURITY.md`](../../../../SECURITY.md) | **CONFIRMED** | Public disclosure and coordinated-reporting policy. |
| Downstream | [`./CVE-2025-12816.md`](./CVE-2025-12816.md) | **CONFIRMED path** · **scaffold content** | Current child advisory file already reserved for the package-specific CVE note. |
| Adjacent owner surface | [`../../../../.github/CODEOWNERS`](../../../../.github/CODEOWNERS) | **CONFIRMED** | `/docs/` currently resolves to `@bartytime4life`, which is the strongest visible owner signal for this lane. |

### Current truth posture for this lane

| Label | What it means here |
|---|---|
| **CONFIRMED** | The repo currently contains `docs/security/vulns/node-forge/`, a scaffold README, a scaffold `CVE-2025-12816.md`, `/docs/` ownership in `CODEOWNERS`, and Dependabot coverage for npm ecosystems in `/`, `/apps/*`, and `/packages/*`. |
| **INFERRED** | If `node-forge` is present, it is most likely to appear in a JavaScript workspace under root, `apps/`, or `packages/`, because those are the npm-scanned surfaces currently declared in `.github/dependabot.yml`. |
| **PROPOSED** | Expand this lane from a single-CVE placeholder into a durable package-level review surface that can survive future advisories without restarting from zero. |
| **UNKNOWN** | Whether the active branch currently ships `node-forge` at all, and if so where it enters the dependency graph. |
| **NEEDS VERIFICATION** | Exact manifest path, exact lockfile owner, exact runtime exposure, exact remediation PR, and release evidence linkage. |

[Back to top](#node-forge-vulnerability-lane)

## Accepted inputs

Content that belongs in this package lane:

- official advisory references for `node-forge` affecting KFM review or remediation
- direct vs. transitive dependency findings
- sanitized manifest or lockfile evidence that proves where the package enters the graph
- remediation notes tied to a real branch change
- test, scan, and release evidence that closes the lane
- rollback or supersession notes if a remediation is reverted or replaced
- cross-links to package-specific child advisory files in this directory

## Exclusions

Content that does **not** belong here:

| Keep out of this README | Where it goes instead |
|---|---|
| Claims that KFM currently uses `node-forge` without manifest or lockfile proof | Record as **UNKNOWN** until branch-local verification exists |
| Generic cryptography guidance not tied to `node-forge` review | Broader security docs or architecture references |
| Secrets, tokens, private incident payloads, or sensitive scan artifacts | Secret-handling boundaries, restricted evidence stores, or steward-only review lanes |
| Full disclosure policy, inbound reporting mailbox, or SLA details | Root [`SECURITY.md`](../../../../SECURITY.md) |
| Package-manager-specific commands presented as universal truth | Mark them as illustrative and run only after confirming the active workspace toolchain |
| Final release proof-pack content | Release evidence, changelog, PR, or owning runbook |

[Back to top](#node-forge-vulnerability-lane)

## Directory tree

```text
docs/security/vulns/node-forge/
├── README.md
└── CVE-2025-12816.md
```

### Current lane condition

The package lane already exists, but both visible files started as **scaffold-only placeholders**. This README is intended to convert the directory from “path reserved” into “path useful.”

[Back to top](#node-forge-vulnerability-lane)

## Quickstart

1. **Verify package presence before saying anything stronger than `UNKNOWN`.**
2. **Determine whether the path is direct, transitive, or absent.**
3. **Check the official advisory cluster, not just the first CVE you noticed.**
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

[Back to top](#node-forge-vulnerability-lane)

## Usage

Use this README when:

- GitHub Advisory / Dependabot / SBOM / manual review flags `node-forge`
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
- this README updated with direct/transitive/absent status
- child advisory file(s) updated with package-specific notes
- validation evidence (scan, audit, or `why` / `ls` output)
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
| `README.md` exists | **CONFIRMED** | Started as a scaffold-only file. |
| `CVE-2025-12816.md` exists | **CONFIRMED** | Started as a scaffold-only file. |
| `/docs/` ownership resolves to `@bartytime4life` | **CONFIRMED** | Current `CODEOWNERS` uses `/docs/ @bartytime4life`. |
| Dependabot has npm ecosystem coverage for `/`, `/apps/*`, and `/packages/*` | **CONFIRMED** | Good review surface for JavaScript dependency alerts. |
| Active branch contains `node-forge` | **UNKNOWN** | Must be proven by manifest / lockfile inspection. |
| Exact owning app or package | **UNKNOWN** | Not visible from current repo-adjacent evidence alone. |

### Official advisory cluster worth checking

| Advisory | Severity | Affected versions | Patched version | Lane status |
|---|---:|---|---|---|
| [`CVE-2025-12816`](./CVE-2025-12816.md) / [`GHSA-5gfm-wpxj-wjgq`][ghsa-12816] | High | `< 1.3.2` | `1.3.2` | **CONFIRMED child path** |
| [`CVE-2025-66030`][nvd-66030] / [`GHSA-65ch-62r8-g69g`][ghsa-66030] | Moderate | `< 1.3.2` | `1.3.2` | **PROPOSED child note** |
| [`CVE-2025-66031`][nvd-66031] / [`GHSA-554w-wpv2-vw27`][ghsa-66031] | High | `< 1.3.2` | `1.3.2` | **PROPOSED child note** |

> [!TIP]
> For the currently observed late-November 2025 official `node-forge` ASN.1 advisory cluster, **`1.3.2` is the minimum patched floor**. If KFM already targets a newer compatible safe version, prefer the newer reviewed version rather than downgrading back to the minimum.

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
- [ ] official advisory scope checked against the full late-November 2025 `node-forge` cluster, not just one CVE
- [ ] minimum safe version or reviewed newer safe version recorded
- [ ] child CVE note(s) updated with package-specific impact or absence findings
- [ ] validation evidence attached: audit output, `why` / `ls` output, SBOM diff, or equivalent
- [ ] release, rollback, or correction linkage noted when the change is release-bearing
- [ ] no sentence in this lane silently upgrades `UNKNOWN` package presence into asserted repo fact

> [!WARNING]
> A dependency bump is **not** “done” in KFM merely because the manifest changed. The lane closes only when the package path, advisory scope, validation evidence, and release or rollback linkage are all readable together.

## FAQ

### Does this README prove KFM currently ships `node-forge`?

No.

The lane exists in the repo, but current evidence does **not** yet prove a direct or transitive `node-forge` path in the active branch.

### What version should remediation target?

For the official late-November 2025 `node-forge` advisory cluster referenced here, the minimum patched version is **`1.3.2`**. If the active repo already targets a newer reviewed safe version, use the newer version after normal compatibility review.

### Why keep a package README when there is already a child CVE file?

Because package lanes age across **multiple advisories**. The README keeps the package-level logic, ownership questions, verification workflow, and remediation matrix in one place, while child files hold alert-specific detail.

### What if the parent `docs/security/vulns/README.md` stays minimal?

That is acceptable for now. This lane README should remain usable on its own, while still linking back to the parent index and wider security subtree.

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

1. flesh out `./CVE-2025-12816.md`
2. add child notes for `CVE-2025-66030` and `CVE-2025-66031` if `node-forge` is actually relevant to the active branch
3. add one short “absence confirmed” note if the package is not present, rather than letting the lane drift silently

</details>

[ghsa-12816]: https://github.com/advisories/GHSA-5gfm-wpxj-wjgq
[ghsa-66030]: https://github.com/advisories/GHSA-65ch-62r8-g69g
[ghsa-66031]: https://github.com/advisories/GHSA-554w-wpv2-vw27
[nvd-66030]: https://nvd.nist.gov/vuln/detail/CVE-2025-66030
[nvd-66031]: https://nvd.nist.gov/vuln/detail/CVE-2025-66031
