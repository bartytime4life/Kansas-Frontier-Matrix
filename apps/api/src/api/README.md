# apps/api/src/api
_Deeper API-module README for KFM route families, middleware seams, evidence-first response shaping, and verification-first maintenance inside the `apps/api/` subtree._

> **Status:** experimental  
> **Doc state:** draft  
> **Owners:** `@bartytime4life` *(fallback via [`../../../../.github/CODEOWNERS`](../../../../.github/CODEOWNERS); subtree-specific ownership still needs verification)*  
> ![status](https://img.shields.io/badge/status-experimental-orange?style=flat-square) ![doc](https://img.shields.io/badge/doc-draft-blue?style=flat-square) ![surface](https://img.shields.io/badge/surface-apps%2Fapi%2Fsrc%2Fapi-6f42c1?style=flat-square) ![posture](https://img.shields.io/badge/posture-verification--first-0a7?style=flat-square) ![trust](https://img.shields.io/badge/trust-membrane%20preserved-444?style=flat-square)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#reference-tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `apps/api/src/api/README.md` → app-root [`../../README.md`](../../README.md) · source subtree [`../README.md`](../README.md) · boundary sibling [`../../../governed-api/README.md`](../../../governed-api/README.md) · routes [`./routes/README.md`](./routes/README.md) · middleware [`./middleware/README.md`](./middleware/README.md) · tests [`../../tests/README.md`](../../tests/README.md) · upstream contract/policy/schema/test surfaces [`../../../../contracts/README.md`](../../../../contracts/README.md), [`../../../../schemas/README.md`](../../../../schemas/README.md), [`../../../../schemas/contracts/README.md`](../../../../schemas/contracts/README.md), [`../../../../policy/README.md`](../../../../policy/README.md), [`../../../../tests/README.md`](../../../../tests/README.md)  
> **Accepted here:** deeper API-lane structure, route-family taxonomy, middleware boundary rules, response-envelope expectations, app-local verification-first editing guidance, and subtree navigation.  
> **Not here:** whole-boundary doctrine already owned by [`../../../governed-api/README.md`](../../../governed-api/README.md), direct storage logic, policy authoring, guessed package-manager or port claims, or endpoint inventories not proven on the branch under review.
>
> [!IMPORTANT]
> This README should stay **implementation-facing** without pretending that doctrine, sibling docs, or historical snapshots are proof of current mounted runtime depth.
>
> [!WARNING]
> If the checked-out branch only proves scaffolding, describe scaffolding.  
> Do not turn route-family doctrine into a claim that concrete handlers, DTOs, middleware, or tests are already complete.
>
> [!NOTE]
> In KFM, even this deeper API module surface still sits **inside the trust membrane**.  
> Route and middleware notes must preserve policy evaluation, evidence resolution, release linkage, and fail-closed behavior.

---

## Scope

This directory is the deeper API-module lane beneath `apps/api/`. It should explain how local route groups, middleware seams, response shaping, and subtree-facing conventions fit together **after** the governed API boundary has already established the larger trust model.

This file is not the place to restate all of KFM doctrine or to invent runtime facts that the branch does not prove. Its job is narrower and more practical:

1. make the local subtree easier to inspect,
2. keep route and middleware responsibilities clean,
3. preserve evidence-first response behavior, and
4. stop adjacent docs from collapsing into one blurry “API” surface.

### Truth posture used in this README

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Visible in the checked-in subtree or directly established by adjacent repo docs. |
| **INFERRED** | Strongly implied by adjacent KFM API docs and current subtree shape, but not directly proven by mounted implementation files in this directory. |
| **PROPOSED** | Recommended documentation shape or future-facing structure that should only be adopted if the branch evidence supports it. |
| **NEEDS VERIFICATION** | Likely important, but not yet proven on the branch under review. |
| **UNKNOWN** | Not verifiable from the current subtree and surrounding docs alone. |

### Stable local laws carried into this subtree

| Rule | Local consequence |
|---|---|
| **Trust membrane stays intact** | No client-facing shortcut language that implies direct storage access, policy bypass, or evidence bypass. |
| **Truth path still matters** | Route notes may reference released scope and derived delivery, but must not quietly promote browsing assets into canonical truth. |
| **Evidence is operational** | Responses should either carry evidence linkage directly or make the EvidenceRef → EvidenceBundle path explicit. |
| **Fail closed** | `ABSTAIN`, `DENY`, `ERROR`, stale-visible, and correction-linked outcomes are valid contract behavior, not embarrassing exceptions. |
| **Branch proof outranks prose confidence** | Startup commands, ports, handlers, DTOs, and route inventories belong here only after they are visible on the target branch. |

[Back to top](#appsapisrcapi)

---

## Repo fit

This file lives at a seam that is easy to misread, so the repo relationship needs to stay explicit.

| Surface | Role | Why it matters here |
|---|---|---|
| [`../../README.md`](../../README.md) | App-root API README | Owns subtree identity, high-level API fit, and app-level constraints. |
| [`../README.md`](../README.md) | `src/` subtree README | Should explain how the broader source subtree is partitioned once it is populated. |
| [`../../../governed-api/README.md`](../../../governed-api/README.md) | Boundary-first sibling README | Owns the governed API boundary, route-family law, trust membrane framing, and public/internal surface split. |
| [`./routes/README.md`](./routes/README.md) | Route-layer child doc | Owns route registration, request parsing, policy invocation, and response-shaping conventions. |
| [`./middleware/README.md`](./middleware/README.md) | Middleware child doc | Owns cross-cutting request/response concerns once there is more than a reserved scaffold. |
| [`../../tests/README.md`](../../tests/README.md) | App-local tests README | Should own app-local test scope once it is no longer a placeholder surface. |
| [`../../../../contracts/README.md`](../../../../contracts/README.md) | Upstream contract lane | Where endpoint and payload contracts belong once explicitly surfaced. |
| [`../../../../schemas/contracts/README.md`](../../../../schemas/contracts/README.md) | Schema lane | Where request/response/example fixtures should eventually become machine-checkable. |
| [`../../../../policy/README.md`](../../../../policy/README.md) | Policy lane | Policy definition lives there, not here. This subtree should invoke policy, not author it. |
| [`../../../../data/catalog/stac/README.md`](../../../../data/catalog/stac/README.md) | Catalog surface | Relevant for catalog/discovery route families and released asset lookup behavior. |

### Current subtree signal

| Path | Current role | Reading note |
|---|---|---|
| `apps/api/src/api/README.md` | Local owner document | This file should explain the subtree without overclaiming runtime depth. |
| `apps/api/src/api/routes/README.md` | Most specific child guidance currently visible | Read this first when documenting route grouping or request flow. |
| `apps/api/src/api/middleware/README.md` | Reserved seam | Keep expectations modest until a real middleware inventory exists. |
| `apps/api/src/api/**` beyond those docs | **NEEDS VERIFICATION** | Do not imply handlers, DTOs, errors, or adapters exist unless the target branch proves them. |

[Back to top](#appsapisrcapi)

---

## Inputs

These inputs belong here because they help maintain or explain the deeper API lane without inflating branch reality.

| Accepted input | What “good” looks like |
|---|---|
| Verified local tree snapshots | Real file/directory inventory for `apps/api/src/api/` on the working branch. |
| Route-family grouping notes | Clear mapping from doctrine-backed route families to local route organization. |
| Middleware responsibilities | Cross-cutting concerns such as auth context, audit correlation, request normalization, or stale/correction headers — but only when branch files exist. |
| Response-shaping guidance | Outcome rules, envelope expectations, evidence-link requirements, and local error/denial/abstention behavior. |
| Adjacent-doc reconciliation | Tight coordination with `apps/api/README.md`, `apps/governed-api/README.md`, and `routes/README.md`. |
| Local inspection commands | Safe, reproducible commands that verify the subtree before making claims. |
| Branch-backed examples | Minimal request/response examples anchored to visible code, contracts, or fixtures. |

---

## Exclusions

This README gets weaker, not stronger, if it tries to own everything around it.

| Exclusion | Where it should go instead |
|---|---|
| Whole-system trust doctrine | [`../../../governed-api/README.md`](../../../governed-api/README.md) and higher-order KFM architecture docs |
| App-wide ownership / runtime boot details | [`../../README.md`](../../README.md) once verified on the target branch |
| Policy definitions and reason registries | [`../../../../policy/README.md`](../../../../policy/README.md) |
| Contract and schema source of truth | [`../../../../contracts/README.md`](../../../../contracts/README.md) and [`../../../../schemas/contracts/README.md`](../../../../schemas/contracts/README.md) |
| Direct database or object-store access guidance | Repository/use-case docs, not route or middleware docs |
| ETL, indexing, or catalog build logic | `packages/ingest`, `packages/catalog`, `packages/indexers` |
| Guessed endpoint inventory | Only after visible route files, OpenAPI, or tests confirm it |
| Ports, env vars, package manager, or scripts not proven here | App-root or runtime docs after verification |

[Back to top](#appsapisrcapi)

---

## Directory tree

### Current verified snapshot

```text
apps/api/src/api/
├── README.md
├── middleware/
│   └── README.md
└── routes/
    └── README.md
```

### How to read this tree

- `README.md` should explain the **local API module surface**.
- `routes/` should explain how HTTP-facing route groups are organized and what routes are allowed to do.
- `middleware/` should explain request/response cross-cuts once there is more than a reserved scaffold.
- Anything deeper than that is **NEEDS VERIFICATION** until the branch under review exposes it.

### Reading order

1. [`../../../governed-api/README.md`](../../../governed-api/README.md)
2. [`../../README.md`](../../README.md)
3. [`./routes/README.md`](./routes/README.md)
4. [`./middleware/README.md`](./middleware/README.md)
5. this file
6. upstream contracts, schemas, policy, and tests

[Back to top](#appsapisrcapi)

---

## Quickstart

This README is easiest to maintain when branch inspection happens **before** prose changes.

### 1) Verify the local subtree

```bash
find apps/api/src/api -maxdepth 3 -type f | sort
```

### 2) Re-read the adjacent owner docs

```bash
sed -n '1,260p' apps/governed-api/README.md
sed -n '1,260p' apps/api/README.md
sed -n '1,260p' apps/api/src/api/routes/README.md
sed -n '1,160p' apps/api/src/api/middleware/README.md
```

### 3) Re-check the upstream contract and policy lanes

```bash
find contracts schemas policy tests -maxdepth 2 -type f | sort | sed -n '1,160p'
```

### 4) Only then add branch-specific runtime notes

```bash
# Example verification loop once concrete files exist
find apps/api/src/api -maxdepth 4 \( -name '*.ts' -o -name '*.tsx' -o -name '*.js' -o -name '*.mjs' \) | sort
```

> [!TIP]
> Keep local inspection commands here.
> Put guessed boot commands, ports, and package-manager assumptions somewhere else — or nowhere yet.

[Back to top](#appsapisrcapi)

---

## Usage

### Responsibility split inside this subtree

| Surface | Owns | Must not quietly become |
|---|---|---|
| `apps/api/src/api/README.md` | Local subtree navigation, route-family framing, middleware seams, response-shaping expectations | Whole-system doctrine or unverified endpoint inventory |
| `apps/api/src/api/routes/README.md` | Route registration, request parsing/validation, policy invocation, response-return rules | Business logic, direct storage access, policy authoring |
| `apps/api/src/api/middleware/README.md` | Cross-cutting request/response concerns | A grab-bag for business logic or route-local hacks |
| `apps/api/README.md` | App-root fit and subtree boundary | Low-level route or middleware detail |
| `apps/governed-api/README.md` | Trust membrane, public/internal route-family law, outward boundary posture | Implementation-facing local module inventory |

### Request handling sequence

A good local API request path should read in this order:

1. **accept and normalize request context**  
   parse input, role context, scope, and versioning expectations.

2. **validate shape before work begins**  
   reject malformed input early and visibly.

3. **evaluate policy before serving data**  
   route logic should invoke policy, not postpone it to a downstream afterthought.

4. **call use-case or service code**  
   route code should orchestrate, not become the business layer.

5. **attach evidence linkage**  
   either return evidence-bearing data directly or keep the EvidenceRef path explicit.

6. **shape a bounded runtime outcome**  
   `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, stale-visible, generalized, or correction-linked behavior must remain visible.

7. **emit audit / correction / freshness cues**  
   release scope, stale state, correction linkage, and audit correlation are not optional decoration.

### Local writing rule

When this subtree gains more files, update this README **after** confirming:

- what actually exists,
- what is child-owned by `routes/` or `middleware/`,
- which payload examples are backed by visible contracts, and
- which endpoint names are proven by code or tests.

[Back to top](#appsapisrcapi)

---

## Diagram

```mermaid
flowchart LR
    Client["Map / Story / Focus / Steward shell"] --> Boundary["apps/governed-api<br/>boundary-first trust membrane"]
    Boundary --> API["apps/api/src/api<br/>deeper module surface"]
    API --> MW["middleware/"]
    API --> RT["routes/"]
    RT --> Policy["policy evaluation"]
    RT --> UseCases["use-cases / services"]
    RT --> Evidence["EvidenceRef → EvidenceBundle<br/>or evidence-linked response"]
    UseCases --> Repos["repos / adapters"]
    Repos --> Released["released scope<br/>(catalog, evidence, portrayals, exports)"]
    Repos -. no direct client bypass .-> Canon["canonical/internal stores"]
    RT --> Audit["audit / request correlation"]
    Evidence --> Audit
```

**Reading note:** this diagram is intentionally boundary-preserving. It shows where this subtree sits, not a claim that every box is already populated by visible files under `apps/api/src/api/`.

[Back to top](#appsapisrcapi)

---

## Reference tables

### Local surface matrix

| Surface | Current confidence | What can be said safely |
|---|---|---|
| `README.md` | **CONFIRMED** | This is the correct location for the deeper API-module README. |
| `routes/README.md` | **CONFIRMED** | Route responsibilities, exclusions, `/api/v1` versioning, and evidence-first response expectations are already documented there. |
| `middleware/README.md` | **CONFIRMED** | The middleware lane currently reads as reserved/empty, so inventory claims should stay modest. |
| concrete handler modules | **UNKNOWN** | Do not name them without branch proof. |
| concrete middleware implementations | **UNKNOWN** | Do not imply they exist because the folder exists. |
| wired OpenAPI from this subtree | **NEEDS VERIFICATION** | Contract ownership is upstream; local wiring must be proven branch-by-branch. |

### Doctrine-backed route families for this subtree

These families are worth documenting here because they affect local route grouping and response behavior, but their **concrete implementation depth still needs verification**.

| Route family | Primary local concern | Boundary profile to honor | Local status |
|---|---|---|---|
| Catalog and discovery | discovery endpoints, collection/item lookup, release metadata shaping | DCAT, STAC, OGC API Records, OpenAPI | doctrine-backed; concrete handler inventory **NEEDS VERIFICATION** |
| Feature or subject read | place/feature/detail reads | OGC API Features where fit; KFM-specific OpenAPI where needed | doctrine-backed; concrete implementation **NEEDS VERIFICATION** |
| Map / tile / portrayal | released maps, tiles, legends, style-linked outputs | OGC API Maps/Tiles plus internal portrayal contracts | doctrine-backed; concrete implementation **NEEDS VERIFICATION** |
| Evidence resolution | EvidenceRef → EvidenceBundle and sibling trust objects | KFM-specific governed API described in OpenAPI | doctrine-backed and central |
| Story / dossier / compare | narrative or comparison calls that remain inside the same shell | KFM-specific governed API | doctrine-backed |
| Export and report | policy-safe previews and packaged outward objects | governed API plus release-manifest references | doctrine-backed |
| Focus / governed assistance | bounded natural-language investigation over released scope | governed API plus runtime response envelope | doctrine-backed |
| Review / stewardship | moderation, quarantine, promotion, denial, rollback, rights handling | internal governed API, not a public route family | doctrine-backed |
| Ops / status | health, metrics, traces, audit joins | internal ops endpoints only | doctrine-backed; exact exposure **NEEDS VERIFICATION** |

### Runtime outcome cues

Exact contract files belong upstream, but the local subtree should still preserve these outcome classes visibly.

| Outcome | When it is valid | Minimum local burden |
|---|---|---|
| `ANSWER` | admissible released evidence supports the result | evidence linkage, release scope, audit/reference hooks |
| `ABSTAIN` | support is partial, missing, or not admissible enough | explicit limit, no bluffing prose, visible reason or scope note |
| `DENY` | policy, rights, sensitivity, or scope rules block the request | visible decision state without leaking protected details |
| `ERROR` | bounded runtime or dependency failure | request/audit correlation, non-deceptive failure shape |
| `stale-visible` | data may still be shown, but freshness burden must remain visible | stale cue, freshness basis, correction/rebuild linkage |
| `correction-linked` | a prior release or answer was superseded, narrowed, or withdrawn | correction notice or replacement linkage |

[Back to top](#appsapisrcapi)

---

## Task list — definition of done

Use this checklist before treating this README as “finished” for a branch:

- [ ] top-of-file impact block matches the actual branch state
- [ ] subtree tree snapshot reflects the real checked-in paths
- [ ] `routes/` and `middleware/` descriptions match their current child docs
- [ ] any `/api/v1` naming here is backed by visible route docs, contracts, or tests
- [ ] endpoint or payload examples are linked to visible schemas/contracts where available
- [ ] no guessed ports, package-manager commands, or runtime flags slipped in
- [ ] no direct-storage or policy-authoring guidance is presented as route responsibility
- [ ] evidence linkage, stale/correction cues, and fail-closed outcomes remain visible
- [ ] relative links resolve in GitHub
- [ ] adjacent docs that describe this subtree have been checked for drift

> [!CAUTION]
> A prettier README is **not** a completed README if it causes trust drift.
> In this subtree, visual polish is subordinate to scope discipline and branch-backed truth.

[Back to top](#appsapisrcapi)

---

## FAQ

### Why do both `apps/governed-api/README.md` and this file exist?
Because they solve different documentation problems. The governed-api README is boundary-first and system-facing. This file is subtree-facing and implementation-oriented.

### Does this file prove live endpoints exist?
No. It documents how this subtree should be read and maintained. Concrete endpoint claims need visible route files, contracts, or tests on the branch under review.

### Should policy rules be written here?
No. This subtree should explain **where policy is invoked**. Policy definitions and registries belong in upstream policy lanes.

### Should startup commands, ports, or package-manager details live here?
Only when the target branch proves them and when this subtree is the right owner. Otherwise keep them out or move them to app-root/runtime docs.

### What if the branch already contains a deeper handler layout than this README describes?
Update the tree, responsibility split, and examples to match the branch. Do **not** force code to mimic placeholder documentation or stale neighboring snapshots.

### What if neighboring docs still describe this lane as thinner than it is?
Treat that as documentation drift to fix next. This file should stay internally honest, and adjacent owner docs should be aligned in the same series when possible.

[Back to top](#appsapisrcapi)

---

## Appendix

<details>
<summary><strong>Illustrative response-envelope sketch (PROPOSED)</strong></summary>

This is an illustrative shape only.  
It belongs here as a reading aid, not as a substitute for upstream schemas or OpenAPI.

```jsonc
{
  "object_type": "RuntimeResponseEnvelope",
  "schema_version": "TBD",
  "request_id": "req_...",
  "audit_ref": "audit_...",
  "evaluated_at": "2026-04-08T00:00:00Z",
  "surface_class": "focus", // or catalog | feature_read | export | review
  "result": "ANSWER",       // or ABSTAIN | DENY | ERROR
  "surface_state": "current",
  "decision_ref": "decision_...",
  "data": {},
  "evidence_refs": ["evidence://..."],
  "policy": {
    "label": "public",
    "obligations": []
  },
  "freshness": {
    "state": "current"
  },
  "correction": null
}
```

### Helpful local reading rule

If this subtree eventually gains concrete envelope builders, serializers, or DTOs, document them here only after:

1. the files exist,
2. their owner surface is clear,
3. their schema authority is linked, and
4. a test or fixture proves the behavior.

</details>

<details>
<summary><strong>Illustrative local growth pattern (PROPOSED, not current tree proof)</strong></summary>

Only add these families if the branch actually surfaces them.

```text
apps/api/src/api/
├── README.md
├── middleware/
├── routes/
├── errors/          # API-facing error mappers
├── envelopes/       # runtime response shaping
├── versioning/      # /api/v1 helpers if needed
└── observability/   # request/audit correlation helpers
```

The point is not these exact names.  
The point is to keep local API responsibilities legible and to avoid hiding route, middleware, response, and observability logic inside arbitrary utility folders.

</details>

[Back to top](#appsapisrcapi)
