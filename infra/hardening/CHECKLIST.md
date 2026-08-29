<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-hardening-checklist
title: infra/hardening/CHECKLIST.md — Infrastructure Hardening Evidence Checklist
type: checklist
version: v2
status: repository-grounded review template; non-enforcement; non-approval
owners:
  - "NEEDS VERIFICATION — CODEOWNERS routes /infra/ to @bartytime4life; operational stewardship and approval authority are not established here"
created: 2026-07-03
updated: 2026-08-29
policy_label: public
related:
  - infra/hardening/README.md
  - infra/README.md
  - infra/firewall/README.md
  - infra/reverse_proxy/README.md
  - infra/vpn/README.md
  - infra/systemd/README.md
  - infra/docker/README.md
  - infra/compose/README.md
  - infra/kubernetes/README.md
  - infra/terraform/README.md
  - docs/security/EXPOSURE_PLAN.md
  - docs/security/INCIDENT_RESPONSE.md
  - docs/security/KEY_ROTATION.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - .github/CODEOWNERS
tags:
  - kfm
  - infra
  - hardening
  - evidence
  - checklist
  - exposure
  - deny-by-default
notes:
  - "Complete a copy for a specific change and evidence scope; do not mark this source template as a project-wide pass."
  - "A completed checklist records bounded review evidence. It does not approve merge, release, deployment, promotion, publication, or source activation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Infrastructure Hardening Evidence Checklist

Use this template to review an infrastructure change that may affect exposure,
host posture, service isolation, secrets, auditability, recovery, or public
delivery. Complete it against one identified change and one defined evidence
scope.

> [!IMPORTANT]
> The source template's default outcome is **HOLD / NOT ASSESSED**. An unchecked
> box, placeholder, inaccessible environment, or undocumented observation is not
> a pass. Completing this checklist does not prove that a control is deployed or
> effective and does not authorize merge, release, deployment, promotion, or
> publication.

The companion [hardening evidence boundary](README.md) defines the repository
facts and limitations inherited by this worksheet.

## 1. Choose the evidence scope

Select every scope actually reviewed:

- [ ] **Repository-only** — versioned paths, diffs, tests, workflow definitions,
      and hosted results were inspected.
- [ ] **Environment observation** — an identified environment was inspected at
      a recorded time using an authorized, redacted procedure.
- [ ] **Mixed** — repository evidence and environment observations were both
      inspected and kept distinguishable below.

A repository-only review may confirm configuration or static-test facts. It
cannot confirm deployed routes, effective firewall rules, runtime identities,
secret custody, monitoring, backup health, or operational rollback.

## 2. Evidence-state vocabulary

Use one state for every applicable item:

| State | Meaning |
|---|---|
| `CONFIRMED` | The cited path, result, or redacted observation directly supports the bounded claim. |
| `N/A` | The item is outside this change; a specific reason is recorded. |
| `UNKNOWN` | Available evidence cannot determine the state. |
| `NEEDS VERIFICATION` | A named check against a revision, artifact, or environment remains to be run. |
| `HOLD` | Do not make the affected enforcement, exposure-safety, deployment-readiness, or rollback-readiness claim. |
| `NOT_RUN` | A required command or observation was not executed. |
| `UNAVAILABLE` | A required tool or environment could not be accessed. |

Mark a checkbox only after recording its state and evidence reference. A green
workflow supports only the assertions that workflow actually checks.

## 3. Review record

| Field | Required value |
|---|---|
| PR or change | `<URL or immutable ID>` |
| Base and head | `<full commit SHAs>` |
| Reviewer | `<verified identity; do not use an unverified role placeholder>` |
| Review time | `<ISO 8601 timestamp with offset>` |
| Evidence scope | `repository-only / environment observation / mixed` |
| Environment | `<repository-only, or redacted stable environment ID>` |
| Affected paths | `<exact path list or diff link>` |
| Affected infrastructure lanes | `<exact lane list>` |
| Public exposure changed | `yes / no / UNKNOWN` |
| Model-runtime exposure changed | `yes / no / UNKNOWN` |
| RAW, WORK, QUARANTINE, or internal access changed | `yes / no / UNKNOWN` |
| Admin or steward access changed | `yes / no / UNKNOWN` |
| Release or deployment behavior changed | `yes / no / UNKNOWN` |
| Correction path | `<link or NEEDS VERIFICATION>` |
| Operational rollback path | `<link / N/A with reason / HOLD>` |

Do not place credentials, private keys, tokens, internal IPs, private hostnames,
restricted routes, exploit payloads, sensitive logs, or exact sensitive
locations in this worksheet. Link only to an approved redacted reference.

## 4. Placement and change boundary

- [ ] Every changed artifact has one responsibility owner and is placed under
      the correct root.
- [ ] Infrastructure implementation remains under `infra/`; machine policy,
      schemas, contracts, release decisions, proofs, receipts, and lifecycle
      data remain in their owning roots.
- [ ] A review checklist or README is not presented as deployed configuration,
      policy enforcement, approval, or operational evidence.
- [ ] The review names all changed ports, listeners, routes, build contexts,
      mounts, identities, service definitions, and public assets.
- [ ] CODEOWNERS is treated only as review routing, not proof of review,
      operational ownership, or approval authority.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Placement | `<state>` | `<path, Directory Rules section, or drift record>` |
| Change inventory | `<state>` | `<diff or immutable path list>` |
| Review routing | `<state>` | `<CODEOWNERS evidence and limitation>` |

## 5. Secrets and sensitive material

- [ ] No real secret, credential, private key, production certificate, token,
      private environment file, or secret-bearing backup was committed.
- [ ] Examples are unmistakably fake; configuration refers only to environment
      variables or verified secret-store references.
- [ ] Logs and traces avoid secrets, raw payloads, restricted geometry,
      living-person data, private source material, and sensitive prompts.
- [ ] Any suspected exposure is routed to containment and separately verified
      rotation; deleting Git history or reverting a commit is not sufficient.
- [ ] Rights, privacy, sovereignty, consent, provenance, and harmful-precision
      controls remain fail closed where the change touches governed material.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Repository secret boundary | `<state>` | `<scan result and reviewed paths>` |
| Runtime secret custody | `<state>` | `<redacted observation or HOLD>` |
| Sensitive-data handling | `<state>` | `<policy/release evidence or N/A reason>` |
| Exposure response | `<state>` | `<incident and rotation references>` |

## 6. Ingress, egress, and public edge

- [ ] Every new or changed listener, port, hostname, route, proxy rule, VPN
      route, firewall rule, and container publication is inventoried.
- [ ] Public routes terminate at a governed interface or released public-safe
      artifact boundary.
- [ ] No public route reaches RAW, WORK, QUARANTINE, internal stores, source
      credentials, direct model runtimes, or steward-only surfaces.
- [ ] Local-only bindings remain loopback or otherwise explicitly private.
- [ ] Ingress and egress defaults, exceptions, TLS, headers, and CORS are
      supported by versioned implementation and observation evidence.
- [ ] Negative route tests cover every changed trust-boundary path.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Listener and route inventory | `<state>` | `<versioned configuration>` |
| Public-boundary routing | `<state>` | `<route tests and observation>` |
| RAW/internal/model/admin denials | `<state>` | `<negative-test evidence>` |
| TLS, headers, and CORS | `<state>` | `<redacted result or HOLD>` |
| Egress posture | `<state>` | `<rules and negative observation>` |

## 7. Service and workload isolation

- [ ] Runtime identities and service accounts use the least privilege supported
      by the identified environment.
- [ ] Filesystem reads, writes, mounts, volumes, capabilities, and devices are
      limited to the named workload need.
- [ ] Debug behavior and unnecessary interfaces are disabled for public or
      semi-public workloads.
- [ ] Startup, dependency, restart, health-check, and failure behavior are
      documented and observed where operational readiness is claimed.
- [ ] Image or artifact identity, dependency locks, scan evidence, provenance,
      and registry custody are recorded where containers are in scope.
- [ ] Kubernetes, systemd, Compose, Docker, or Terraform evidence is not
      generalized beyond the exact implementation lane reviewed.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Runtime identity | `<state>` | `<configuration and observation>` |
| Filesystem and capability scope | `<state>` | `<configuration and observation>` |
| Startup and health | `<state>` | `<test or observation>` |
| Container or artifact integrity | `<state>` | `<digest, scan, provenance, custody>` |
| Orchestrator/service-manager controls | `<state>` | `<lane-specific evidence>` |

## 8. Governed data and public artifacts

- [ ] Public clients use governed interfaces or released public-safe artifacts,
      not canonical stores or pre-publication lifecycle paths.
- [ ] Public-serving processes do not directly mount or read RAW, WORK,
      QUARANTINE, or unpublished candidate material.
- [ ] Tiles, exports, static assets, and downloadable artifacts are bound to a
      release identity and correction or rollback target where applicable.
- [ ] Range and CORS behavior is verified for public object or tile delivery.
- [ ] Sensitive geometry and rights-uncertain material is denied, withheld,
      generalized, or redacted before any public release.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Governed client path | `<state>` | `<route and negative-test evidence>` |
| Lifecycle-store denial | `<state>` | `<mount/access review>` |
| Released artifact binding | `<state>` | `<release identity and manifest>` |
| Sensitivity and rights gate | `<state>` | `<review evidence>` |
| Correction and rollback binding | `<state>` | `<target and procedure>` |

## 9. Authentication, administration, and audit

- [ ] Admin and review surfaces are outside the normal public path.
- [ ] Steward-only paths require verified authentication and authorization.
- [ ] Emergency access is constrained, reviewable, and separately recorded.
- [ ] Security-relevant events are logged without exposing restricted content.
- [ ] Log sinks, access controls, retention, redaction, alerts, and response
      routing are identified and observed where monitoring is claimed.
- [ ] Audit evidence can reconstruct the reviewed change and material access
      events without treating a dashboard as sovereign truth.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Authentication and authorization | `<state>` | `<redacted test or observation>` |
| Admin-path isolation | `<state>` | `<negative route evidence>` |
| Audit events and redaction | `<state>` | `<redacted sample or test>` |
| Retention, alerting, and response | `<state>` | `<configuration and observation>` |

## 10. Backup, incident response, correction, and rollback

- [ ] Protected assets and state are inventoried.
- [ ] Backup location, custody, retention, integrity, and access controls are
      verified where backup readiness is claimed.
- [ ] Restore has been rehearsed against an identified environment and result.
- [ ] Detection, containment, isolation, escalation, and restoration paths are
      reachable and do not require publishing sensitive topology.
- [ ] Repository correction, release rollback, and operational rollback are
      recorded as distinct actions.
- [ ] Any exception has a verified authority, bounded scope, expiration or
      review trigger, and containment path.

**State and evidence**

| Item | State | Evidence reference or `N/A` reason |
|---|---|---|
| Backup custody and integrity | `<state>` | `<redacted evidence or HOLD>` |
| Restore rehearsal | `<state>` | `<exercise record or HOLD>` |
| Incident containment | `<state>` | `<procedure and exercise evidence>` |
| Repository correction | `<state>` | `<revert or corrective-change path>` |
| Operational rollback | `<state>` | `<environment procedure and rehearsal>` |
| Exceptions | `<state>` | `<decision record or N/A reason>` |

## 11. Bounded repository checks

Run only checks relevant to the changed paths and record the exact revision and
result. These commands inspect repository configuration; they do not inspect a
deployed environment.

```bash
git ls-tree -r --name-only HEAD -- infra/hardening
git grep -n -E \
  'infra-compose-smoke|test_compose_static|test_docker_security_overrides' \
  HEAD -- .github tests Makefile infra
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_compose_static.py' \
  --verbose
python -m unittest discover \
  --start-directory tests/infra \
  --pattern 'test_docker_security_overrides.py' \
  --verbose
docker compose -f infra/compose/docker-compose.yml config --quiet
```

| Check | Revision | Result | Bounded interpretation |
|---|---|---|---|
| Hardening-lane inventory | `<SHA>` | `<result>` | Confirms tracked paths only. |
| Compose static tests | `<SHA>` | `<result / NOT_RUN>` | Confirms only enumerated source-level assertions. |
| Docker overlay tests | `<SHA>` | `<result / NOT_RUN>` | Confirms only declared lock and Dockerfile assertions. |
| Compose render | `<SHA>` | `<result / NOT_RUN / UNAVAILABLE>` | Confirms the file renders; does not start services. |
| Hosted image build or scan | `<run URL and SHA>` | `<result / NOT_RUN>` | Point-in-time evidence for the built bytes and configured scanner policy. |

Do not substitute generic firewall, proxy, VPN, `systemctl`, `kubectl`, or
`terraform` commands. Operational commands require an adopted technology,
versioned implementation, identified environment, authorization, validation,
and a tested recovery path.

## 12. Findings and disposition

### Blocking findings

| ID | Finding | State | Evidence | Required resolution |
|---|---|---|---|---|
| `<ID>` | `<description>` | `<UNKNOWN / NEEDS VERIFICATION / HOLD>` | `<reference>` | `<action>` |

### Non-blocking follow-up

| ID | Follow-up | Evidence | Tracking reference |
|---|---|---|---|
| `<ID>` | `<description>` | `<reference>` | `<issue, backlog, or drift record>` |

### Review outcome

| Outcome | Meaning |
|---|---|
| `EVIDENCE_COMPLETE` | Every applicable item has bounded evidence and no checklist blocker remains. |
| `EVIDENCE_COMPLETE_WITH_FOLLOW_UP` | Bounded review evidence is complete; explicitly non-blocking follow-up remains tracked. |
| `HOLD` | Required evidence is missing, stale, inaccessible, conflicting, or unsafe to disclose. |
| `ESCALATE` | A separate security, infrastructure, release, governance, or ADR decision is required. |

**Outcome:** `<HOLD / EVIDENCE_COMPLETE / EVIDENCE_COMPLETE_WITH_FOLLOW_UP / ESCALATE>`

**Outcome scope:** `<repository-only / identified environment / mixed>`

**Outcome rationale and evidence:** `<references>`

**Recorded by:** `<verified identity and timestamp>`

The outcome describes completion of this bounded evidence review only. It is not
a merge approval, security certification, release decision, deployment record,
promotion receipt, publication decision, or proof that a control is effective
outside the observed scope.

## Current repository holds

At the repository checkpoint documented by the companion README:

- operational stewardship and accountable approval authority remain
  `NEEDS VERIFICATION`;
- deployed environments and their authoritative inventories are `UNKNOWN`;
- no aggregate hardening validator exists;
- firewall, reverse-proxy, VPN, systemd, Kubernetes, and Terraform lanes
  document holds rather than deployed enforcement; and
- Docker and Compose evidence is bounded to static checks and review-image
  build or scan behavior.

Re-check those facts at the review head. Do not copy them forward as permanent
state.

[Back to top](#top)
