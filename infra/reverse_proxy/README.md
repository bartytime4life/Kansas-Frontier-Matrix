<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-reverse-proxy-readme
title: infra/reverse_proxy/ — Public Edge Routing Hold Boundary
type: per-directory-readme; infrastructure-boundary; operational-hold
version: v1.1.0
status: draft; repository-grounded; documentation-only; configuration-absent; deployment-unverified; deny-by-default; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; accountable infrastructure, security, and operations stewardship remains unverified
created: 2026-07-03
updated: 2026-08-29
policy_label: repository-facing; infra; reverse-proxy; public-edge; deny-by-default; no-public-raw-path; no-public-model-path
current_path: infra/reverse_proxy/README.md
owning_root: infra/
responsibility: document the repository-visible public-edge routing boundary without claiming an adopted proxy engine, applied routes, or deployed enforcement
truth_posture: >
  CONFIRMED same-path target; accepted Directory Rules v2 through ADR-0029; infra/ as the
  deployment, host, network, and exposure responsibility root; this README plus one one-line
  Caddy placeholder; two Explorer application families; three governed API route registrations;
  application-level boundary tests; a Sites hosting identity; and a placeholder development
  Compose file / UNKNOWN the active edge provider, proxy engine, public domains, upstream
  bindings, TLS, CORS, headers, caching, authentication, logging, monitoring, applied deny rules,
  deployed state, and operational rollback / NEEDS VERIFICATION accountable stewards, route
  inventory, release bindings, independent review, and runtime evidence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  target_prior_blob: fd061eb31ba9c71ca6815d76b46a26864bb0f91c
  caddy_placeholder_blob: ab07d5d6f7e34c63c4bda81f1ee62cc1081de119
  compose_blob: 8a45891700a501f6e18a921ce8d260956441e4b3
  governed_api_registry_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_main_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  sites_hosting_identity_blob: a0e5c285c2789c8dce4465350bef8438c79efeb3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  inspection_method: current main tree and direct file reads; no host, edge provider, deployment, DNS, certificate store, network, access log, or runtime inspected
related:
  - ../README.md
  - ../compose/docker-compose.yml
  - ../firewall/README.md
  - ../hardening/CHECKLIST.md
  - ../../apps/explorer-web/
  - ../../apps/kansas-frontier-matrix-explorer/
  - ../../apps/kansas-frontier-matrix-explorer/.openai/hosting.json
  - ../../apps/governed-api/
  - ../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../apps/governed-api/src/governed_api/main.py
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/security/EXPOSURE_PLAN.md
  - ../../.github/CODEOWNERS
  - ../../.github/workflows/deny-test.yml
tags:
  - kfm
  - infra
  - reverse-proxy
  - public-edge
  - exposure
  - deny-by-default
  - trust-membrane
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Public edge routing hold

`infra/reverse_proxy/` is the repository lane for reverse-proxy and public-edge
routing evidence. It is currently a **documentation-only hold boundary**, not a
configured or deployed proxy.

Current repository evidence does not select an edge provider or proxy engine,
bind a public domain to an application, apply TLS or HTTP controls, or prove a
route in a running environment. Treat every public-route claim as `UNKNOWN`
until an adoption packet and runtime evidence establish it.

> [!IMPORTANT]
> A route must not be inferred from an application directory, route handler,
> Compose port, hosting identity, diagram, or this README. Those artifacts can
> identify candidates; they do not prove public exposure or enforcement.

## Current repository state

The tracked lane contains exactly two files:

| Path | Observed content | What it establishes |
|---|---|---|
| [`README.md`](README.md) | This boundary document | Repository guidance only |
| [`caddy.example.caddyfile`](caddy.example.caddyfile) | One-line `Greenfield Caddy placeholder` comment | A placeholder name, not Caddy adoption, syntax, routing, or deployment |

No reverse-proxy configuration, route manifest, domain inventory, certificate
reference, header policy, CORS policy, edge test, log sample, deployment record,
or rollback procedure is tracked in this lane at the pinned evidence snapshot.

The repository does contain adjacent implementation candidates, but none is an
observed upstream binding:

| Candidate surface | Confirmed repository evidence | Edge conclusion |
|---|---|---|
| [`apps/explorer-web/`](../../apps/explorer-web/) | A Vite application family exists | No public route is proved |
| [`apps/kansas-frontier-matrix-explorer/`](../../apps/kansas-frontier-matrix-explorer/) | A separate Sites-oriented application family exists; its [hosting identity](../../apps/kansas-frontier-matrix-explorer/.openai/hosting.json) names a Sites project | The identity is not proxy configuration or runtime proof |
| [`apps/governed-api/`](../../apps/governed-api/) | The [route registry](../../apps/governed-api/src/governed_api/routes/registry.py) registers `/bootstrap`, `/layers`, and `/evidence`; the [WSGI application](../../apps/governed-api/src/governed_api/main.py) binds locally in its direct entry point | Handler presence and a local bind do not prove an edge route |
| [`infra/compose/docker-compose.yml`](../compose/docker-compose.yml) | A greenfield development Compose placeholder maps loopback ports for two named services | Static port text does not prove a runnable service, selected Explorer family, public ingress, or deployment |

Because two Explorer families exist, future edge work must identify the intended
application by exact path and artifact identity. This README does not choose or
normalize either family.

## Authority and scope

[Accepted ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the Directory Rules standard. The current
[Directory Rules](../../docs/doctrine/directory-rules.md) and
[`infra/` index](../README.md) place deployment, host, network, and exposure
mechanics under `infra/`. That placement does not grant this lane policy,
application, evidence, release, or publication authority.

This lane may hold reviewed, non-secret edge configuration and directly related
route, validation, and rollback documentation after an engine and topology are
adopted. It must not become:

- an application route registry;
- a policy or sensitivity decision surface;
- a source, evidence, lifecycle, or canonical-data store;
- a release, deployment, promotion, or publication decision;
- a secret store for private keys, certificates, tokens, credentials, host
  inventories, or unredacted incident material; or
- a bypass around governed interfaces or released public-safe artifacts.

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `infra/` changes to
`@bartytime4life`. That is a GitHub review route, not proof of accountable
infrastructure, security, or operations stewardship and not proof that review
occurred.

## Required posture

Until applied configuration and runtime evidence exist, the only supportable
repository posture is **hold**:

| Surface | Required default | Evidence needed before a different claim |
|---|---|---|
| Public UI | `HOLD` | Exact application artifact, domain, upstream, release identity, applied config, and request proof |
| Governed API | `HOLD` | Exact route inventory, upstream identity, policy boundary, applied config, and positive/negative request proof |
| Released public-safe artifacts | `HOLD` | Release identity, rights and sensitivity clearance, public carrier, integrity, cache/range behavior, correction path, and rollback target |
| Health endpoint | `HOLD` | Explicit non-sensitive response contract, authentication posture, applied route, and leakage tests |
| Admin, review, metrics, or operator surface | `DENY` from the public edge | Separately authorized private-access design, authentication, audit, and negative public-route proof |
| Model or AI runtime | `DENY` from the public edge | No direct-public exception is established here; public clients use governed interfaces |
| RAW, WORK, or QUARANTINE data | `DENY` from the public edge | No exception belongs in this lane |
| Canonical/internal stores, credentials, debug routes, or unpublished candidates | `DENY` from the public edge | No exception belongs in this lane |

`HOLD` is not an applied deny rule. It means the repository cannot substantiate
an exposure claim and must not be used as authority to create one.

The [Exposure Plan](../../docs/security/EXPOSURE_PLAN.md) remains the relevant
security posture reference, while current application code and emitted runtime
evidence determine implementation facts. Rights, privacy, sovereignty,
sensitivity, and harmful precision must be resolved before an artifact or API
response becomes eligible for public routing.

## Adoption packet

A proxy or hosted-edge change should not replace this hold with operational
claims until one coherent review packet records:

1. **Decision and ownership** — selected edge provider or engine, accountable
   maintainers, exact configuration home, environments, and the accepted ADR or
   architecture decision when required.
2. **Route inventory** — public, private, and denied paths; exact upstream
   application path and immutable artifact or release identity; method and
   authentication expectations; and finite failure behavior.
3. **Trust boundary** — evidence that public clients reach only governed
   interfaces or released public-safe artifacts, with direct model, lifecycle,
   canonical-store, admin, and debug access denied.
4. **Transport and browser controls** — DNS and certificate ownership, TLS
   termination, trusted-forwarding behavior, security headers, CORS, cache and
   range semantics, size and timeout limits, and any rate controls.
5. **Data protection** — rights, sensitivity, precision, privacy, redaction,
   logging, retention, and secret-reference handling for every exposed class.
6. **Validation** — engine-native parse or plan result, configuration identity,
   positive route tests, negative denial tests, header and CORS captures, log
   hygiene checks, and evidence from the intended environment.
7. **Operations** — health and monitoring signals, incident escalation, prior
   configuration identity, rollback or forward-fix procedure, rollback
   rehearsal, and post-change verification.

Do not add example commands for an unselected engine. Once an engine is adopted,
pin commands to the tracked configuration and supported version instead of
publishing interchangeable Nginx, Caddy, Traefik, or platform examples.

## Repository-only inspection

The following commands inspect the current repository boundary; they do not
test an edge or deployment:

```bash
git ls-tree -r --name-only HEAD -- infra/reverse_proxy
git show HEAD:infra/reverse_proxy/caddy.example.caddyfile
git grep -n -E 'reverse[_ -]?proxy|caddy|nginx|traefik|envoy' HEAD -- \
  infra apps .github docs/security
```

The governed API [boundary tests](../../apps/governed-api/tests/test_boundary_guards.py)
and repository [`deny-test` workflow](../../.github/workflows/deny-test.yml) are
useful adjacent evidence. They do not parse a proxy configuration, inject an
edge, inspect a deployed route, or prove network enforcement. A passing result
must remain scoped to the behavior that the test actually executes.

## Failure and incident response

If a future edge change exposes an unintended surface or leaks restricted
material:

1. stop or withdraw the affected public route using the separately approved
   operational procedure;
2. preserve the configuration and runtime evidence needed to identify the
   exact exposure without copying secrets or harmful precision into GitHub;
3. rotate compromised credentials or keys through the responsible secret
   system;
4. invalidate affected caches or released carriers when authorized;
5. trace affected evidence, source, release, correction, and consumer records;
6. restore only from a reviewed configuration identity and verify both allowed
   and denied paths; and
7. record the incident, correction, and rollback outcome in their governing
   systems.

This README cannot authorize a production change, withdrawal, credential
rotation, cache purge, correction, rollback, release, deployment, promotion, or
publication.

## Open verification

- [ ] Identify the active public edge provider or confirm that none exists.
- [ ] Decide whether `caddy.example.caddyfile` should become an adopted,
  validated template or be removed in a separately reviewed change.
- [ ] Identify the intended Explorer family, governed API artifact, and released
  artifact carriers by exact identity.
- [ ] Record public and private domains, upstreams, paths, methods, auth, and
  environment boundaries without committing sensitive infrastructure detail.
- [ ] Establish TLS, trusted-forwarding, headers, CORS, cache, range, timeout,
  size, and rate-control requirements.
- [ ] Establish executable positive and negative edge tests with exact
  configuration and environment attribution.
- [ ] Establish access-log redaction, retention, monitoring, alerting, incident,
  and rollback procedures.
- [ ] Verify accountable infrastructure, security, operations, application, and
  release review responsibilities.

Closing an item requires direct evidence. A documentation commit, passing
repository check, pull request, merge, release record, deployment, and public
route are distinct states.
