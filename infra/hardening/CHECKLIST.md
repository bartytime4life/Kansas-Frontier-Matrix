<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra-hardening-checklist
title: infra/hardening/CHECKLIST.md — Infrastructure Hardening Review Checklist
type: checklist
version: v1
status: draft
owners:
  - <infra-steward>
  - <security-owner>
  - <ops-steward>
created: 2026-07-03
updated: 2026-07-03
policy_label: public
related:
  - infra/hardening/README.md
  - infra/README.md
  - infra/firewall/
  - infra/reverse_proxy/
  - infra/vpn/
  - infra/systemd/
  - configs/
  - runtime/
  - apps/governed-api/
  - docs/security/README.md
  - docs/security/EXPOSURE_PLAN.md
  - docs/security/INCIDENT_RESPONSE.md
  - docs/security/KEY_ROTATION.md
  - docs/doctrine/directory-rules.md
  - policy/
  - release/
  - data/published/
tags:
  - kfm
  - infra
  - hardening
  - checklist
  - exposure
  - deny-by-default
  - least-privilege
  - trust-membrane
  - auditability
notes:
  - "Use this checklist before merging infrastructure changes that affect exposure, host hardening, reverse proxy, firewall, VPN, systemd, model runtime, raw-data boundaries, admin surfaces, or audit logging."
  - "This checklist records review evidence. It does not store secrets, policy bundles, release manifests, firewall configs, or incident working data."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Infrastructure Hardening Review Checklist

> **Purpose.** Give reviewers a repeatable, evidence-producing checklist for infrastructure changes that might expose KFM services, data, models, admin surfaces, or release artifacts.

![status](https://img.shields.io/badge/status-draft-yellow)
![posture](https://img.shields.io/badge/posture-deny--by--default-red)
![raw](https://img.shields.io/badge/raw_data-public_access_DENY-red)
![model](https://img.shields.io/badge/model_endpoint-direct_access_DENY-red)
![secrets](https://img.shields.io/badge/secrets-never_commit-red)

---

## How to use this checklist

Use this file in PRs that touch any of these areas:

- `infra/hardening/`
- `infra/firewall/`
- `infra/reverse_proxy/`
- `infra/vpn/`
- `infra/systemd/`
- `infra/docker/`, `infra/compose/`, `infra/kubernetes/`, or `infra/terraform/`
- public route exposure or asset hosting
- model/runtime network access
- raw-data, internal-store, catalog, or release artifact exposure
- admin/review-console/operator access
- logging, audit, backup, restore, or secret-boundary behavior

For each item, mark one of:

- `[x]` checked and supported by evidence
- `[ ]` not yet checked
- `N/A — <reason>` not applicable for this PR

Do not paste secrets, internal IPs, private hostnames, exploit payloads, or sensitive operational data into this checklist. Link to redacted evidence or approved runbook records instead.

---

## 0. Review header

| Field | Value |
|---|---|
| PR / change ID | `<link or ID>` |
| Reviewer | `<name>` |
| Review date | `<YYYY-MM-DD>` |
| Deployment scope | `local-only / VPN-only / steward-only / public-facing / mixed / unknown` |
| Affected infra lane(s) | `<firewall / reverse_proxy / vpn / systemd / docker / compose / kubernetes / terraform / hardening>` |
| Public exposure changed? | `yes / no / unknown` |
| Model runtime exposure changed? | `yes / no / unknown` |
| Raw/internal data access changed? | `yes / no / unknown` |
| Admin/review access changed? | `yes / no / unknown` |
| Rollback path recorded? | `yes / no / N/A` |

---

## 1. Directory and authority placement

- [ ] The changed file belongs under the correct responsibility root.
- [ ] `infra/` changes are deployment, host, network, or exposure posture changes, not policy, schema, source, release, or data lifecycle artifacts.
- [ ] No enforceable policy bundle was added under `infra/hardening/`; policy lives in `policy/`.
- [ ] No schema or machine contract was added under `infra/hardening/`; machine-checkable schemas live under `schemas/contracts/v1/...`.
- [ ] No release manifest, rollback card, correction notice, proof, receipt, or signed artifact was added under `infra/hardening/`.
- [ ] Any conflict with Directory Rules or existing repo convention is recorded in the drift register or PR notes.

**Evidence / notes:**

```text
<paths reviewed, Directory Rules reference, drift note if any>
```

---

## 2. Secret boundary

- [ ] No real secrets were committed.
- [ ] No private keys, certificates, password files, `.env` files, tokens, API keys, OAuth secrets, webhook secrets, or production credentials were added.
- [ ] Secret references are by environment variable name, secret-store key name, or deployment secret reference only.
- [ ] Example values are clearly fake and cannot be used against a real service.
- [ ] Any accidental secret exposure triggered rotation, audit, and incident/runbook handling.
- [ ] `configs/` remains non-secret; no hardening note tells maintainers to store real secrets in repo config files.

**Evidence / notes:**

```text
<secret scan result, files checked, rotation note if applicable>
```

---

## 3. Default ingress and network exposure

- [ ] Default ingress remains deny-by-default.
- [ ] Only explicitly reviewed public routes are allowed.
- [ ] Public HTTP routes terminate at the governed public boundary or released static artifact hosting.
- [ ] No public route points directly to raw stores, work stores, quarantine stores, internal stores, source credentials, model runtimes, or admin paths.
- [ ] Any new listener, port, host, container port, service binding, VPN route, firewall rule, or reverse-proxy location is named in the PR.
- [ ] Local-only services bind to loopback or private interfaces as appropriate.
- [ ] Public-facing services are separated from steward-only services.
- [ ] CORS is explicit and not wildcarded for sensitive or credentialed routes.

**Evidence / notes:**

```text
<route inventory, port/listener review, firewall/proxy diff, CORS check>
```

---

## 4. Governed API trust membrane

- [ ] Browser/public clients reach KFM through `apps/governed-api/` or released public assets, not internal stores.
- [ ] Public UI does not call model-runtime endpoints directly.
- [ ] Public UI does not call raw data, work data, quarantine data, unpublished candidates, source credentials, or internal/canonical stores directly.
- [ ] Public API responses preserve finite outcome behavior: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
- [ ] Routes that cannot resolve evidence or policy state abstain or deny; they do not silently answer.
- [ ] Infrastructure does not add a bypass route around governed API checks.
- [ ] Any public asset route serves only released artifacts tied to release state and rollback target.

**Required negative-state checks:**

- [ ] Browser -> model runtime is denied.
- [ ] Browser -> `data/raw/` is denied.
- [ ] Browser -> `data/work/` is denied.
- [ ] Browser -> `data/quarantine/` is denied.
- [ ] Browser -> unpublished release candidates is denied.
- [ ] Browser -> internal/canonical store is denied.
- [ ] Browser -> admin/review console without steward auth is denied.

**Evidence / notes:**

```text
<negative tests, proxy deny evidence, API route inventory, release route notes>
```

---

## 5. Raw, work, quarantine, and internal-store denial

- [ ] No public-serving process mounts or reads `data/raw/` directly.
- [ ] No public-serving process mounts or reads `data/work/` directly.
- [ ] No public-serving process mounts or reads `data/quarantine/` directly.
- [ ] No public-serving process reads unpublished release candidates directly.
- [ ] No public route exposes catalog/triplet/internal stores without governed API mediation.
- [ ] If a service needs data, it consumes released artifacts, governed API payloads, or policy-approved internal service calls.
- [ ] Mounts and container volumes are scoped to the minimum needed paths.
- [ ] File permissions and service accounts follow least privilege.

**Evidence / notes:**

```text
<mount review, service account review, volume diff, path-denial test>
```

---

## 6. Model runtime isolation

- [ ] Model runtimes are not publicly exposed.
- [ ] Model runtimes are not directly reachable from browser code.
- [ ] Model runtimes are behind governed API adapters and policy checks.
- [ ] Runtime services cannot read RAW, WORK, QUARANTINE, source credentials, or internal stores directly unless an explicitly reviewed internal path requires it.
- [ ] Model prompts, outputs, and traces are not logged with secrets, raw payloads, restricted geometry, living-person data, or private source material.
- [ ] Generated language is never treated as root truth, release authority, or evidence.
- [ ] AI-related errors fail closed through finite outcome envelopes.

**Evidence / notes:**

```text
<runtime binding, proxy deny evidence, adapter route review, log redaction evidence>
```

---

## 7. Admin, review, and steward surfaces

- [ ] Admin and review consoles are not on the normal public path.
- [ ] Steward-only paths require authentication and role checks.
- [ ] Admin shortcuts are justified, constrained, documented, and audited.
- [ ] Emergency access is time-bounded or separately reviewed.
- [ ] Admin paths do not bypass publication, policy, evidence, or review state for normal public outputs.
- [ ] Logs record admin actions without leaking restricted data or secrets.
- [ ] Public users cannot discover or access admin routes through default navigation, wildcard proxy rules, or static file serving.

**Evidence / notes:**

```text
<auth review, route review, proxy rules, audit event sample, exception note>
```

---

## 8. Public artifacts, tiles, exports, and static hosting

- [ ] Static hosting serves only released public artifacts.
- [ ] PMTiles, COGs, GeoParquet, styles, sprites, glyphs, manifests, and exports are tied to release state where applicable.
- [ ] Public asset routes do not expose build caches, temporary artifacts, proof internals, unpublished candidates, or local workspace files.
- [ ] Range/CORS behavior is reviewed for tile and object hosting.
- [ ] Sensitive geometry, living-person, DNA, archaeology, rare-species exact location, critical infrastructure, or rights-uncertain material fails closed or is generalized/redacted before release.
- [ ] Exported files carry or reference rights, sensitivity, provenance, evidence, and rollback information as required by the release process.

**Evidence / notes:**

```text
<asset route list, release manifest refs, Range/CORS review, sensitivity gate evidence>
```

---

## 9. Logging, telemetry, and auditability

- [ ] Security-relevant events are logged: auth failures, admin actions, denied public access, proxy denials, secret-rotation events, release-route changes, and model-runtime access attempts.
- [ ] Logs do not include real secrets, raw payloads, private geometry, source credentials, unrestricted EvidenceBundle bodies, living-person data, prompt text, or sensitive incident details.
- [ ] Audit logs are access-controlled.
- [ ] Retention expectations are named or marked `NEEDS VERIFICATION`.
- [ ] Logs are useful enough to reconstruct what happened during an exposure incident.
- [ ] Telemetry is minimized and safe-by-construction.

**Evidence / notes:**

```text
<sample redacted log, retention note, access control review, telemetry schema note>
```

---

## 10. Service hardening

- [ ] Services run with least privilege.
- [ ] Services use dedicated service accounts where practical.
- [ ] Write access is limited to required directories only.
- [ ] Read access is limited to required directories only.
- [ ] Restart behavior is documented for critical services.
- [ ] Service units or containers do not expose unnecessary capabilities.
- [ ] Health checks do not leak internal details.
- [ ] Debug modes are disabled on public or semi-public deployments.
- [ ] Dependency/network access is constrained to known needs.

**Evidence / notes:**

```text
<systemd/container/compose/kubernetes/terraform review notes>
```

---

## 11. Backup, restore, and rollback

- [ ] The infrastructure change has a rollback procedure or a documented forward-fix-only reason.
- [ ] Rollback does not require exposing secrets or bypassing the trust membrane.
- [ ] Backup location and access control are reviewed where applicable.
- [ ] Restore path is documented for critical state.
- [ ] Release-impacting infrastructure changes link to release/rollback records where applicable.
- [ ] Recovery procedures preserve auditability.

**Evidence / notes:**

```text
<rollback steps, backup/restore note, release or runbook link>
```

---

## 12. Incident response readiness

- [ ] The change does not weaken incident detection.
- [ ] The change does not hide security-relevant logs.
- [ ] The change does not remove the path to disable or isolate a public route quickly.
- [ ] The change does not remove the path to isolate model runtimes quickly.
- [ ] The change does not remove the path to block raw/internal store exposure quickly.
- [ ] Reporting and escalation paths remain linked from security/runbook docs.
- [ ] Any security exception includes an expiration date or review trigger.

**Evidence / notes:**

```text
<incident path review, emergency isolation step, exception review trigger>
```

---

## 13. Final hardening decision

| Decision | Meaning |
|---|---|
| `PASS` | All required checks passed; evidence is recorded. |
| `PASS_WITH_WARNINGS` | Non-blocking warnings exist and are tracked. |
| `BLOCK` | Do not merge until listed items are fixed. |
| `ESCALATE` | Requires security, infra, release, governance, or ADR review before merge. |

**Decision:** `<PASS / PASS_WITH_WARNINGS / BLOCK / ESCALATE>`

**Blocking items:**

```text
<list blockers or N/A>
```

**Warnings / follow-up:**

```text
<list follow-up issues, drift entries, ADRs, or N/A>
```

**Reviewer sign-off:**

```text
<name / role / date>
```

---

## Open verification backlog

- [ ] Confirm CODEOWNERS for all hardening-adjacent paths.
- [ ] Confirm exact firewall, reverse-proxy, VPN, systemd, container, and hosting stack.
- [ ] Confirm executable validation commands for route denial checks.
- [ ] Confirm secret-scanning command used in CI.
- [ ] Confirm audit-log retention and redaction policy.
- [ ] Confirm model-runtime network binding and denial tests.
- [ ] Confirm public artifact hosting headers and Range/CORS behavior.
- [ ] Confirm rollback template for infrastructure changes.

[Back to top](#top)
