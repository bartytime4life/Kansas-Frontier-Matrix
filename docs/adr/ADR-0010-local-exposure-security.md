<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS_VERIFICATION__adr-0010-local-exposure-security
title: ADR-0010: Local Exposure Security
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION__security_platform_or_repo_stewards
created: NEEDS_VERIFICATION__YYYY-MM-DD
updated: 2026-05-02
policy_label: NEEDS_VERIFICATION__restricted_or_internal
related: [NEEDS_VERIFICATION__docs/architecture/governed-api.md, NEEDS_VERIFICATION__docs/runbooks/local-ai-runtime.md, NEEDS_VERIFICATION__docs/runbooks/local-exposure.md, NEEDS_VERIFICATION__policy/README.md, NEEDS_VERIFICATION__schemas/contracts/v1/runtime/runtime_response_envelope.schema.json]
tags: [kfm, adr, security, local-exposure, governed-api, vpn, reverse-proxy, ollama, maplibre]
notes: [Target path retained from the attached baseline markdown; no mounted repo was available in this session to verify existing ADR numbering, CODEOWNERS, policy label, related paths, route names, service names, workflow names, branch protections, deployment manifests, runtime logs, or platform settings. Updated date is the current-session revision date. This ADR is doctrine-grounded and implementation-aware, but implementation claims remain PROPOSED or UNKNOWN until verified in the target repository and runtime.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0010: Local Exposure Security

Decision record for how KFM may be exposed from a local or home-hosted runtime without weakening the governed evidence path.

> [!IMPORTANT]
> **Decision status:** `PROPOSED`  
> **Document status:** `draft`  
> **Target path:** `docs/adr/ADR-0010-local-exposure-security.md`  
> **Default posture:** local-only first; VPN-first for trusted remote access; reverse-proxy exposure only after explicit gates  
> **Policy posture:** treat as `restricted/internal` until repository policy labels, owners, and disclosure rules are verified  
> **Truth posture:** CONFIRMED doctrine / PROPOSED decision / UNKNOWN implementation depth

**Quick jumps:** [Decision](#decision) · [Status and truth posture](#status-and-truth-posture) · [Scope](#scope) · [Context](#context) · [Exposure ladder](#exposure-ladder) · [Boundary model](#boundary-model) · [Required controls](#required-controls) · [Forbidden paths](#forbidden-paths) · [Exceptions](#exceptions) · [Validation](#validation) · [Consequences](#consequences) · [Rollback](#rollback) · [Open verification](#open-verification) · [Source map](#source-map)

---

## Decision

KFM will use a **deny-by-default local exposure model**.

A locally hosted KFM instance may be exposed only through governed, auditable, least-privilege boundaries. The normal exposed surfaces are:

1. the **governed API**, when it can enforce actor, scope, policy, release state, EvidenceBundle resolution, finite outcome envelopes, and audit IDs;
2. the **public-safe UI**, when it consumes only governed API responses and released artifacts;
3. a **VPN or overlay network**, preferred before any public reverse proxy when access is for trusted third parties, reviewers, or operators;
4. a **reverse proxy or edge gateway**, only when it forwards intended traffic to the governed API or public-safe UI and preserves auditability.

KFM will not expose canonical databases, RAW / WORK / QUARANTINE storage, artifact roots, policy bundles, model runtimes, review internals, administrative derived-store surfaces, or direct AI/model endpoints to the LAN or public internet.

> [!NOTE]
> This ADR records the security decision and minimum acceptance gates. It is **not** a deployment runbook and does not assert that any firewall, reverse proxy, VPN, auth, CI, or runtime configuration already exists.

---

## Status and truth posture

| Claim area | Label | Meaning for this ADR |
|---|---:|---|
| KFM trust law | CONFIRMED | KFM doctrine requires governed truth paths, evidence-first outputs, policy-aware release, cite-or-abstain behavior, and public clients behind governed interfaces. |
| Attached baseline | CONFIRMED | This revision preserves and strengthens the attached ADR draft rather than restarting from zero. |
| Target file path | PROPOSED / NEEDS VERIFICATION | The attached baseline names `docs/adr/ADR-0010-local-exposure-security.md`; confirm against actual ADR numbering and repo layout before commit. |
| Mounted repo evidence | UNKNOWN | No mounted target repository was available in the current visible workspace, so this file may be new or may revise an uninspected existing ADR. |
| Public repo reports | LINEAGE / NEEDS VERIFICATION | Supplied implementation-reference material reports meaningful public repo surface area, but this ADR does not treat that report as direct current runtime, deployment, or local host evidence. |
| Decision content | PROPOSED | The exposure model is a repo-ready decision draft pending owner, platform, policy, security, API, UI, and runtime review. |
| Exact implementation | UNKNOWN | Current auth stack, proxy choice, VPN arrangement, firewall rules, route tree, service names, CI workflows, branch protections, logs, and release artifacts are not verified. |
| External security details | NEEDS VERIFICATION | Tool versions, package pins, provider behavior, firewall syntax, platform hardening, CVEs, and service defaults must be refreshed before operational use. |

### Evidence boundary

This ADR states KFM doctrine where supported by the project corpus and the attached baseline. It does **not** claim current implementation behavior without mounted repository, runtime, log, workflow, dashboard, or emitted-artifact evidence.

The safest reading is:

- **CONFIRMED:** KFM requires governed evidence paths and fail-closed boundaries.
- **PROPOSED:** this ADR’s exposure ladder, gate language, waiver process, and validation plan.
- **UNKNOWN:** whether the target repo already implements any named control, route, service, workflow, or deployment pattern.
- **NEEDS VERIFICATION:** any product/version-specific hardening instruction before it is used operationally.

---

## Scope

This ADR applies to KFM deployments where a local host, home firewall, small private network, reverse proxy, VPN, overlay network, or trusted third-party access path may expose any KFM surface.

It covers:

- local-only development and proof-slice operation;
- trusted reviewer or operator access over VPN / overlay networking;
- LAN-only exposure in a small trust zone;
- allowlisted or public reverse proxy exposure;
- model runtime placement, especially Ollama or similar local model APIs;
- public-safe UI and MapLibre shell exposure;
- governed API exposure;
- canonical store and artifact-root protection;
- audit, logging, rollback, cache invalidation, and validation expectations;
- emergency shutoff expectations for exposed surfaces.

It does **not** cover:

- production identity-provider selection;
- exact firewall syntax for a specific host;
- exact reverse-proxy product configuration;
- exact VPN product configuration;
- cloud provider network design;
- emergency-alerting or life-safety delivery;
- full incident-response procedure;
- exact schema, route, package-manager, or workflow names before repo verification.

---

## Context

KFM is a governed, evidence-first, map-first, time-aware spatial knowledge system. Its public unit of value is the **inspectable claim**, not a tile, model answer, map popup, graph edge, vector index, dashboard, screenshot, or static file by itself.

That makes local exposure unusually consequential. A home firewall, trusted LAN, or reverse proxy can make an internal mistake internet-adjacent. A model runtime bound too broadly can create a second truth path. A direct route to RAW, WORK, QUARANTINE, canonical databases, policy bundles, or artifact roots can bypass the trust membrane immediately.

KFM therefore treats network exposure as a governed architectural transition, not a convenience setting.

### Decision drivers

| Driver | Consequence |
|---|---|
| Trust membrane | Normal clients must enter through governed APIs, not direct stores, model runtimes, or lifecycle roots. |
| Evidence-first output | Public or semi-public answers must resolve to release-scoped evidence and policy state. |
| Local runtime risk | Local services can become public through firewall, NAT, proxy, VPN, wildcard bind, or LAN mistakes. |
| Model runtime posture | Model APIs are interpretive helpers, not public truth surfaces. |
| Sensitive data | Exact sensitive locations, living-person/private data, cultural context, ecological/archaeological records, DNA, land/title material, and unreleased artifacts fail closed. |
| Auditability | Exposure must preserve request IDs, actor context, release scope, policy decision, outcome, and rollback target. |
| Reversibility | Exposure can be disabled quickly without moving canonical data or rewriting doctrine. |
| Separation of duty | Public or semi-public release requires review appropriate to risk. |

---

## Exposure ladder

KFM will advance exposure only through the following ladder. Higher modes do not replace lower controls; they add obligations.

| Mode | Allowed surface | Default use | Required gates |
|---|---|---|---|
| `M0_LOCAL_ONLY` | Local console, loopback services, tightly scoped SSH | First proof slices, operator-only work | Host firewall, individual operator identity, loopback binds, persistent logs |
| `M1_VPN_PRIVATE_REMOTE` | Governed API and optional public-safe UI over VPN / overlay | Trusted reviewers, trusted operators, small remote team | VPN peer inventory, role-bound access, no direct DB/model/artifact routes |
| `M2_ALLOWLISTED_REVERSE_PROXY` | HTTPS reverse proxy to governed API and/or public-safe UI | Limited external review or controlled access | TLS, auth, allowlist where practical, rate limits, audit IDs, backend private binds |
| `M3_PUBLIC_EDGE_SPLIT` | Public edge gateway and public-safe UI/API only | Public or semi-public release surface | Published-release-only access, policy checks, sensitive transform receipts, release manifest, rollback plan |
| `M4_PRODUCTION_SPLIT` | Dedicated edge, identity, governed API, workers, canonical store, artifact store, model runtime, observability | Later maturity, only when operational burden justifies it | Formal platform review, separation of duties, recovery drills, release/correction/withdrawal process |
| `M_DENY_DIRECT_INTERNAL` | None | All modes | Direct exposure of canonical stores, model runtime, RAW / WORK / QUARANTINE, policy bundles, admin ports, and direct AI endpoints is denied |

> [!CAUTION]
> Mode advancement is not an entitlement. A KFM instance that cannot prove policy, evidence resolution, release scope, logging, rollback, and no-direct-internal access remains in `M0_LOCAL_ONLY` or `M_DENY_DIRECT_INTERNAL`.

---

## Boundary model

The exposure boundary must preserve the KFM trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Public clients and ordinary UI surfaces may use only governed interfaces, released artifacts, EvidenceBundle resolution, policy decisions, review state, and appropriate citation behavior.

```mermaid
flowchart LR
  User[User / reviewer / operator]

  subgraph Edge["Allowed exposure boundary"]
    VPN[VPN / overlay access]
    Proxy[Reverse proxy / edge gateway]
    UI[Public-safe UI]
    API[Governed API]
  end

  subgraph Private["Private KFM host or subnet"]
    DB[(Canonical DB / PostGIS)]
    Artifacts[/Lifecycle artifact roots/]
    Policy[Policy bundles and runtime config]
    Model[Ollama or model runtime]
    Logs[(Audit and service logs)]
    Releases[(Published release scope)]
  end

  User -->|preferred trusted remote path| VPN
  User -->|only after explicit gates| Proxy

  VPN --> UI
  VPN --> API
  Proxy --> UI
  Proxy --> API

  UI -->|governed requests only| API
  API --> Releases
  API --> Policy
  API --> DB
  API --> Artifacts
  API --> Model
  API --> Logs

  User -. forbidden .-> DB
  User -. forbidden .-> Artifacts
  User -. forbidden .-> Model
  User -. forbidden .-> Policy
```

### PROPOSED `ExposureProfile` review record

Each exposure mode should have a reviewable record. This is a proposed shape, not a confirmed schema.

```yaml
# PROPOSED review record shape. Not executable host configuration.
exposure_profile:
  profile_id: kfm://exposure/NEEDS_VERIFICATION
  mode: M1_VPN_PRIVATE_REMOTE
  owner: OWNER_TBD
  reviewed_at: NEEDS_VERIFICATION__YYYY-MM-DD
  allowed_surfaces:
    - governed_api
    - public_safe_ui
  denied_surfaces:
    - canonical_db
    - raw_work_quarantine
    - artifact_roots_direct
    - model_runtime_direct
    - policy_bundles_direct
    - admin_ports_public
  public_hostnames: []
  vpn_peers:
    - PEER_ID_TBD
  reverse_proxy_routes: []
  release_scope: RELEASE_ID_TBD
  policy_bundle: POLICY_BUNDLE_ID_TBD
  audit_sink: AUDIT_SINK_TBD
  rollback_switch: ROLLBACK_SWITCH_TBD
  verification_status: NEEDS VERIFICATION
```

---

## Required controls

### 1. Host and network boundary

| Requirement | Minimum rule | Validation signal |
|---|---|---|
| Firewall posture | Deny incoming by default; allow only explicit ingress. | Firewall status reviewed and captured before exposure. |
| SSH | Individual operator accounts; key-based auth preferred; no shared root workflow. | Named accounts, logged elevation, config validation before restart. |
| Bind scope | Bind to the narrowest usable scope for the current mode. | API/model/DB/admin ports are loopback, socket, VPN-only, or private as required. |
| Admin surfaces | Admin ports, dashboards, debug endpoints, and metrics endpoints are private by default. | Admin endpoints are absent from public proxy route maps. |
| Time discipline | Use one authoritative time sync path. | Host reports synchronized time before emitting release/audit artifacts. |
| Logging | Preserve service logs and request/audit joins. | Logs include request ID, audit ref, actor/scope where applicable, release ID, and policy outcome. |
| Patch posture | Security updates are deliberate, logged, and reversible. | Patch window, update source, restart plan, and rollback notes exist. |
| Secrets | Secrets never appear in repo, prompts, fixtures, logs, receipts, UI payloads, or public bundles. | Secret scan or equivalent review passes before exposure. |

### 2. Governed API boundary

The governed API is the only normal client-visible truth boundary.

It must:

- evaluate actor, surface, scope, release state, source role, sensitivity, and policy before data or model access;
- resolve `EvidenceRef` to `EvidenceBundle` where a claim depends on evidence;
- return finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- expose stale, denied, restricted, or failed states honestly;
- emit audit references suitable for later reconstruction;
- fail readiness if policy, release scope, evidence resolution, source registry, or audit sinks are unavailable;
- reject requests that target RAW, WORK, QUARANTINE, internal artifact roots, or direct model runtime paths.

> [!WARNING]
> A process that is merely listening on a port is not ready for KFM. Readiness must include the minimum dependencies required for truthful behavior.

### 3. Reverse proxy boundary

A reverse proxy may exist only as an intentional exposure boundary.

It must:

- terminate TLS for public or semi-public access;
- route only intended public-safe traffic;
- forward to private upstream binds;
- preserve request IDs and headers needed for audit joins;
- enforce auth, allowlist, rate limits, and body-size limits appropriate to the mode;
- use narrow CORS policy and an explicit browser connection policy;
- never convert `DENY`, `ABSTAIN`, stale, restricted, or error states into cosmetic success;
- maintain a publication map that names public hostname, upstream, allowed paths, auth, log sink, cache behavior, and rollback switch.

### 4. VPN / overlay boundary

VPN-mediated access is the preferred first remote-access mode for trusted third parties.

It must:

- name each peer or group;
- define allowed surfaces per peer role;
- avoid broad subnet access where a narrower route is feasible;
- preserve logs sufficient to reconstruct review and operator activity;
- be revocable without changing canonical data or release artifacts;
- keep direct database, direct artifact-root, direct model-runtime, and admin access denied unless an explicit admin exception exists.

### 5. Model runtime boundary

Local model runtimes, including Ollama or compatible adapters, must remain private.

They must not:

- receive direct browser traffic;
- bind to all interfaces without an explicit, time-bounded, reviewed security exception;
- be exposed through a home router, LAN wildcard, public reverse proxy, or direct tunnel;
- read RAW, WORK, QUARANTINE, or unpublished artifact roots directly;
- become an alternate route around policy, citation validation, or release state;
- persist private chain-of-thought as a KFM truth object;
- publish raw generated language as authoritative output.

Allowed pattern:

```yaml
# Illustrative policy shape, not executable host configuration.
model_runtime_boundary:
  default: deny_direct_client_access
  bind_scope: loopback_or_private_only
  allowed_callers:
    - governed_api
  forbidden_callers:
    - browser
    - public_ui
    - reverse_proxy_direct
    - unauthenticated_lan_client
    - raw_artifact_worker_direct_public
  input_scope:
    allowed:
      - release_scoped_context
      - policy_checked_context
      - evidence_bundle_context
    forbidden:
      - RAW
      - WORK
      - QUARANTINE
      - unpublished_artifact_roots
      - unrestricted_sensitive_location_context
  output_scope:
    required:
      - structured_output_validation
      - citation_validation
      - policy_postcheck
      - runtime_response_envelope
      - audit_id
```

### 6. Store and artifact boundary

Canonical and lifecycle stores remain internal.

| Surface | Exposure decision |
|---|---|
| PostgreSQL / PostGIS | Never directly internet-exposed; use Unix socket, loopback, private bind, or tightly scoped internal network only. |
| RAW | Never public; source-native capture only. |
| WORK | Never public; repeatable transform and QA area. |
| QUARANTINE | Never public; failed, unclear, restricted, rights-uncertain, or review-needed material. |
| PROCESSED | Not automatically public; must still pass catalog/release gates. |
| CATALOG / TRIPLET | Queryable only through governed interfaces unless explicitly released. |
| PUBLISHED | May feed public-safe UI/API/tiles only with release manifest and policy state. |
| Derived stores | Rebuildable accelerators; never proof by themselves. |
| Vector indexes | Rebuildable retrieval accelerators; never sovereign truth. |
| Graph projections | Derived reasoning surfaces; never replace canonical records. |
| Policy and contract registries | Not public runtime endpoints unless explicitly reviewed and sanitized. |
| Receipts and proofs | Auditable object families; do not expose sensitive internals unless reviewed. |

### 7. UI and map boundary

MapLibre, story surfaces, popups, Focus Mode, and Evidence Drawer are downstream of trust.

They must:

- consume released layers, governed API responses, or public-safe derived artifacts;
- show evidence, policy, review, stale, denied, restricted, and correction state where consequential;
- avoid treating vector tiles, PMTiles, rendered features, style toggles, search snippets, screenshots, or generated summaries as proof;
- avoid direct browser access to model runtimes or canonical stores;
- return visible negative states instead of hiding denial or uncertainty;
- preserve accessibility and user-visible trust state in public-safe views.

### 8. Cache, static asset, and tile boundary

Public caching is allowed only for released, public-safe material.

| Cache or delivery surface | Rule |
|---|---|
| Static UI bundle | May be public if it contains no secrets, no private API base URLs, and no hardcoded internal paths. |
| PMTiles / vector tiles | Public only after release manifest, sensitivity review, source role review, and rollback target. |
| Browser caches | Must not hide withdrawal, stale state, or correction notices. |
| CDN / edge cache | Requires purge or versioned rollback path. |
| Local preview cache | Must not be treated as public release evidence. |

---

## Forbidden paths

These paths are `DENY` unless a later ADR or waiver creates a narrower, reviewed, time-bounded exception:

- public or LAN-wide Ollama / model runtime endpoint;
- browser-to-model-runtime calls;
- browser-to-database calls;
- direct public PostgreSQL / PostGIS;
- direct file sharing of `/srv/kfm` or equivalent artifact roots;
- direct access to RAW, WORK, or QUARANTINE;
- public access to graph/vector/search admin surfaces;
- public access to policy bundles or private contract registries;
- reverse proxy routes to unpublished artifacts;
- static UI caches that hide stale, denied, withdrawn, restricted, or error states;
- shared root or shared superuser workflow for normal operations;
- “trust the home router” as a complete security model;
- “temporary” port forwarding without owner, expiration, log, and rollback record;
- direct AI chat surfaces that bypass EvidenceBundle, citation validation, policy postcheck, and finite outcome envelopes.

---

## Exceptions

Admin or maintenance shortcuts may exist only when justified, documented, constrained, and prevented from becoming the normal public path.

A valid exception must include:

| Field | Requirement |
|---|---|
| Owner | Named accountable owner or team. |
| Reason | Why normal governed access is insufficient. |
| Scope | Exact host, port, route, identity, data scope, and time window. |
| Risk | What trust membrane, privacy, rights, or safety risk is introduced. |
| Compensating controls | Additional logging, allowlist, temporary firewall rule, local-only bind, or operator supervision. |
| Expiration | Date/time or event that ends the exception. |
| Review | Security/platform/governance approval appropriate to risk. |
| Rollback | Explicit shutoff action and evidence preservation step. |
| Receipt | Exception receipt or review record retained outside public surfaces. |

> [!CAUTION]
> A convenience exception without an owner, expiration, audit record, and rollback switch is not an exception. It is a policy failure.

---

## Validation

This ADR is not complete until the repository and runtime can prove the boundary.

### Proposed CI gates

| Gate | Purpose | Truth label |
|---|---|---:|
| `security-boundary` | Prove no public route or frontend code calls model runtime, DB, RAW, WORK, or QUARANTINE directly. | PROPOSED |
| `api-contract` | Prove exposed responses use finite envelopes and trust state. | PROPOSED |
| `policy-gates` | Prove actor/scope/release/sensitivity policy denies unsafe requests. | PROPOSED |
| `ui-trust-state` | Prove UI displays `DENY`, `ABSTAIN`, stale, restricted, withdrawn, and error states. | PROPOSED |
| `release-dry-run` | Prove public-safe release scope exists before public exposure. | PROPOSED |
| `proxy-smoke` | Prove public paths map only to intended UI/API upstreams. | PROPOSED |
| `no-direct-model-client` | Prove browser/client code cannot call a model runtime directly. | PROPOSED |
| `no-public-raw-path` | Prove public routes cannot reach RAW, WORK, QUARANTINE, or direct artifact roots. | PROPOSED |
| `secrets-scan` | Prove secrets are absent from exposed bundles, fixtures, prompts, logs, and config committed to repo. | PROPOSED |
| `rollback-drill` | Prove exposure can be disabled without moving canonical data. | PROPOSED |

### Minimum test checklist

- [ ] No frontend source contains direct model-runtime base URLs.
- [ ] No frontend source contains direct database, RAW, WORK, QUARANTINE, private catalog, or private policy URLs.
- [ ] No public route returns unpublished lifecycle-stage artifacts.
- [ ] API readiness fails when policy bundle, published release scope, evidence resolver, source registry, or audit sink is unavailable.
- [ ] `DENY`, `ABSTAIN`, `ERROR`, stale, withdrawn, and restricted paths are rendered visibly in UI.
- [ ] Reverse proxy route inventory exists and matches the allowed publication map.
- [ ] Firewall / bind scan confirms forbidden ports are not externally reachable.
- [ ] VPN peer list and role mapping are reviewed before trusted third-party access.
- [ ] Secrets do not appear in repo, logs, receipts, prompts, fixtures, UI payloads, static bundles, or screenshots.
- [ ] Release manifest names all public-safe artifacts exposed through UI/API/proxy.
- [ ] Cache purge or versioned rollback path exists for public-safe tiles and static bundles.
- [ ] Rollback disables exposure without moving RAW, WORK, QUARANTINE, canonical DB, or policy registry data.

### Manual review gates

Before moving from `M0_LOCAL_ONLY` to any remote exposure mode, reviewers must confirm:

1. owner and CODEOWNERS coverage;
2. policy label for this ADR and related runbooks;
3. auth and role model;
4. proxy/VPN/firewall configuration;
5. log retention and request-ID propagation;
6. sensitive data handling;
7. source role and rights posture for exposed data;
8. release manifest and rollback path;
9. backup/restore evidence for canonical data;
10. cache invalidation path;
11. incident contact and disable switch;
12. public or semi-public disclosure posture.

### Operational readiness checks

Readiness must cover more than network liveness.

| Readiness area | Required signal |
|---|---|
| API | Evidence resolver, policy bundle, release scope, source registry, and audit sink available. |
| UI | Trust-state rendering works for positive and negative outcomes. |
| Model runtime | Private bind and governed API caller path verified. |
| Proxy | Public routes match allowed publication map. |
| VPN | Peer inventory and revocation path verified. |
| Logs | Request ID can be joined across proxy, API, policy, and model call where applicable. |
| Release | Published artifacts are manifest-bound and rollback target exists. |

---

## Consequences

### Positive consequences

- Keeps KFM’s trust membrane operational, not decorative.
- Reduces local-host and home-router convenience risk.
- Prevents model runtimes from becoming unsupervised truth surfaces.
- Preserves citation, policy, release, review, and audit requirements at the network edge.
- Gives maintainers a reviewable ladder from local-only to private remote to public edge.
- Makes rollback a network/configuration/cache action rather than a data migration.
- Keeps derived layers subordinate to evidence and release state.

### Tradeoffs

- Trusted third-party access may be slower to set up because VPN/auth/proxy gates come first.
- Direct demos are less convenient because raw ports and model endpoints remain private.
- Public UI work must wait for released, policy-safe artifacts instead of reading internal stores.
- More logs and request IDs must be preserved, which increases operational discipline.
- Future exceptions require ADR or waiver work rather than informal port forwarding.
- Cache and tile publication require stricter release manifests and purge paths.

### Rejected alternatives

| Alternative | Rejection reason |
|---|---|
| Expose the full local stack through a home router | Breaks least privilege and makes internal mistakes internet-adjacent. |
| Put Ollama or model runtime on LAN for convenience | Creates a direct model path outside policy, citation validation, and release state. |
| Let static UI read artifact roots | Bypasses lifecycle and publication gates. |
| Treat MapLibre layers as proof | Rendered features and tiles are downstream representations, not evidence bundles. |
| Depend on NAT alone | NAT is not an authorization, audit, policy, or release boundary. |
| Hide failures behind friendly UI chrome | KFM requires trust-visible negative states. |
| Expose admin dashboards to trusted users by default | Admin surfaces create escalation and data-leakage risk; they need separate constrained access. |
| Allow public direct AI chat | Bypasses EvidenceBundle, policy, review, release state, and citation validation. |

---

## Rollback

Exposure rollback must be fast, observable, and reversible.

Minimum rollback actions:

1. disable public reverse proxy site or route;
2. revoke or disable affected VPN peers;
3. close firewall rules added for the exposure mode;
4. rotate credentials or tokens that may have been exposed;
5. invalidate public caches for affected UI, tiles, PMTiles, COGs, static bundles, and API responses;
6. restore the previous release manifest or mark the current release withdrawn;
7. preserve audit logs, proxy logs, policy decisions, and incident notes;
8. record a correction, withdrawal, or rollback notice where public claims may have been affected;
9. verify that RAW, WORK, QUARANTINE, canonical DB, and policy registry were not moved or exposed as part of rollback.

Rollback must not require moving canonical data or deleting evidence needed for audit.

### Rollback triggers

Rollback is required when any of the following are found:

- public route to model runtime, database, RAW, WORK, QUARANTINE, or direct artifact root;
- public route returns unpublished or rights-uncertain artifacts;
- UI hides `DENY`, `ABSTAIN`, stale, withdrawn, restricted, or error states;
- logs cannot reconstruct actor/scope/request/release/policy outcome;
- model runtime receives direct client traffic;
- release manifest cannot identify exposed artifacts;
- cache purge or version rollback cannot be performed;
- secrets appear in public bundle, logs, fixtures, prompts, or receipts;
- sensitive location or private/living-person data exposure is suspected.

---

## Open verification

The following remain `UNKNOWN` until the actual repository and deployment are inspected:

- existing ADR numbering and prior ADR-0010 history;
- whether this ADR should be accepted, superseded, merged, or renamed;
- CODEOWNERS and document owners;
- policy label for security ADRs;
- related path existence and link validity;
- actual auth stack and role model;
- actual reverse proxy, if any;
- actual VPN or remote access arrangement;
- actual firewall implementation;
- actual service names and bind addresses;
- actual API route tree and DTO names;
- actual UI framework and MapLibre integration path;
- actual model runtime service configuration;
- actual database roles and socket/bind settings;
- actual `/srv/kfm` or lifecycle artifact paths;
- actual CI workflows and branch protections;
- actual request logging, audit joins, and retention;
- actual backup/restore evidence;
- actual sensitive-location redaction policy;
- actual release manifest and cache invalidation path;
- actual secrets management;
- actual security scanning;
- actual incident contact and disable switch;
- actual public repo status versus local/private deployment status.

---

## Definition of done

This ADR can move from `draft` to an accepted KFM decision only after:

- [ ] owner and policy label are verified;
- [ ] related paths are corrected to real repo-relative links;
- [ ] the target repository is scanned for existing ADR conventions;
- [ ] the implementation boundary is tested against current app/API/UI code;
- [ ] forbidden exposure paths have static or runtime checks;
- [ ] proxy/VPN/firewall posture is documented in a companion runbook;
- [ ] model runtime bind and caller path are verified;
- [ ] rollback is tested in at least one non-production environment;
- [ ] cache invalidation is tested for any public static/tile/API delivery;
- [ ] release manifest or equivalent publication record exists for public-safe artifacts;
- [ ] security, platform, policy, API, UI, and governance reviewers sign off.

---

## Companion runbooks

This ADR intentionally avoids exact host commands. Those belong in runbooks after platform verification.

| Runbook | Status | Purpose |
|---|---:|---|
| `NEEDS_VERIFICATION__docs/runbooks/local-exposure.md` | PROPOSED | Exact mode transition steps, route maps, firewall/proxy/VPN checks, rollback switch. |
| `NEEDS_VERIFICATION__docs/runbooks/local-ai-runtime.md` | PROPOSED | Model runtime bind, caller, system service, logs, provider profile, and no-direct-client checks. |
| `NEEDS_VERIFICATION__docs/runbooks/release-cache-rollback.md` | PROPOSED | Static bundle, tile, PMTiles, API, and cache invalidation rollback. |
| `NEEDS_VERIFICATION__docs/runbooks/security-incident-local-exposure.md` | PROPOSED | Exposure incident triage, log preservation, secret rotation, peer revocation, and correction notice. |

---

## Source map

| Source | Status | Supports | Limits |
|---|---|---|---|
| Attached baseline markdown for ADR-0010 | CONFIRMED baseline | Original meta block, decision posture, exposure ladder, required controls, forbidden paths, validation, rollback, and source map. | Does not prove repo implementation or deployment behavior. |
| KFM Pipeline Living Implementation Manual v0.3 | CONFIRMED doctrine / PROPOSED implementation | Lifecycle law, governed state transitions, schema/contract uncertainty, no-autopublish posture, repo-unavailable discipline, proposed control-plane validation. | Does not prove current repo files, workflows, or runtime behavior in this session. |
| Ollama & Ubuntu Information | CONFIRMED doctrine / PROPOSED realization / NEEDS VERIFICATION for runtime specifics | Ollama behind governed API, local-first model runtime, loopback/private posture, VPN-first ladder, no public home-router exposure, finite runtime outcomes. | Product/runtime/security details must be refreshed before operational use. |
| KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual | CONFIRMED doctrine / PROPOSED implementation | Renderer downstream-of-trust rule, no direct browser model/canonical access, Evidence Drawer and Focus Mode trust surfaces, `no_direct_model_client` and `no_public_raw_path` test pressure. | Does not prove the UI implementation exists or passes tests. |
| KFM Governed AI reports and Whole-UI expansion reports | LINEAGE / PROPOSED | Provider-neutral AI adapter, citation validation, finite outcomes, EvidenceBundle-first interaction, UI trust-state obligations. | Prior reports and PDF plans are not current repo proof. |
| KFM Implementation Reference | LINEAGE / NEEDS VERIFICATION | Reports that a public repo may have meaningful implementation surface area and unresolved `contracts/` versus `schemas/` authority. | It is not a mounted target checkout, deployment manifest, runtime trace, or local exposure proof in this session. |
| Official Ubuntu / WireGuard / systemd / Ollama / NIST sources | NEEDS VERIFICATION targets | Should be consulted before exact firewall, VPN, service hardening, model runtime, or secure-delivery instructions are operationalized. | Not revalidated by this revision; do not treat as current fact inside this ADR without fresh checks. |

---

## Maintainer notes

- Keep this ADR short enough to review, but strong enough to block unsafe convenience paths.
- Put host commands, exact proxy snippets, VPN peer procedures, firewall rule examples, and package-specific settings in companion runbooks after platform verification.
- Do not downgrade `UNKNOWN` items through tone. Replace them only with inspected repository, runtime, platform, workflow, log, or emitted-artifact evidence.
- Treat exposure as a governed state transition, not a file move and not a router setting.
- Keep exceptions time-bounded, auditable, and reversible.
- Treat model runtimes, map renderers, tiles, vector indexes, graph projections, and generated language as downstream surfaces, never sovereign truth.

[Back to top](#top)
