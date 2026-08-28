<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/github-issue-template-readme
title: .github/ISSUE_TEMPLATE README
type: README
version: v0.5
status: draft; repository-grounded issue-intake governance; live settings selectively verified
owners: ["@bartytime4life"]
created: 2026-07-17
updated: 2026-08-27
policy_label: public; issue-intake; governance; security-aware; non-authoritative
owning_root: .github/
responsibility: GitHub public issue chooser templates and routing into governed KFM work
truth_posture: CONFIRMED repository evidence / NEEDS VERIFICATION live rendering and enforcement / issue intake is non-authoritative
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix main@ef7f2fbd523af5d803fadf92504d7f734c82c2ca
evidence_root_tree: 989b76bea75e30d275a7cd515ea3f6cab4f6adec
evidence_github_tree: 245bd98cf05ac3f5afd9765db34ef0c9393639b6
evidence_issue_template_tree: 7a0dfe35ba99fb1eb6eafac16e0b8410c3510107
evidence_target_prior_blob: f689cad3a3c66e4e201208c66bbe4e218c5edea5
evidence_adr_blob: 8fc79fe67bfb84fa9feb287670478a5a374fb068
evidence_chooser_templates: 6 Markdown files
evidence_issue_forms: 0
evidence_chooser_config: absent
evidence_issues: enabled
evidence_discussions: disabled
evidence_private_vulnerability_reporting: NEEDS VERIFICATION; last confirmed enabled 2026-08-10
verified_template_labels: ["needs-review"]
related:
  - ../README.md
  - ../CODEOWNERS
  - ../PULL_REQUEST_TEMPLATE.md
  - ../../CONTRIBUTING.md
  - ../../SECURITY.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../docs/prompts/kfm-repository-build-markdown-modernization-agent.md
  - ../../data/receipts/generated/README.md
  - ../../tools/validators/validate_generated_receipt.py
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
notes:
  - "The tracked inventory is complete for .github/ISSUE_TEMPLATE at the pinned baseline."
  - "Repository Issues, Discussions, the six-template inventory, chooser configuration, current assignee routing, and the needs-review label were checked at the pinned baseline on 2026-08-27."
  - "Private vulnerability reporting was last confirmed enabled on 2026-08-10; the current setting could not be read through the connected capability and remains NEEDS VERIFICATION."
  - "This edition changes this README and a generated provenance receipt; it does not change a chooser template, label, assignee, setting, workflow, policy, ADR state, source state, release, deployment, promotion, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `.github/ISSUE_TEMPLATE/`

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b)](#status)
[![Templates: 6](https://img.shields.io/badge/templates-6-7c3aed)](#confirmed-template-inventory)
[![Authority: intake only](https://img.shields.io/badge/authority-intake%20only-b91c1c)](#authority-boundary)
[![Private reporting: verify current](https://img.shields.io/badge/private%20reporting-verify%20current-f59e0b)](#public-safety-boundary)

> Public-safe issue intake for bugs, features, ADR proposals, evidence corrections, sensitivity concerns, and source-admission proposals. Issues route work; they do not become KFM authority objects or independently authorize repository mutation.

> [!IMPORTANT]
> This subtree is an intake surface. A filed, labeled, assigned, linked, automated, or closed issue does not confirm a claim, accept an ADR, admit a source, approve policy, authorize implementation, complete a correction, authorize a release, or publish anything.

## Quick navigation

- [Purpose](#purpose)
- [Authority boundary](#authority-boundary)
- [Status](#status)
- [Confirmed template inventory](#confirmed-template-inventory)
- [Routing guide](#routing-guide)
- [Public-safety boundary](#public-safety-boundary)
- [Template authoring contract](#template-authoring-contract)
- [Triage and implementation handoff](#triage-and-implementation-handoff)
- [Issue-to-governed-artifact flow](#issue-to-governed-artifact-flow)
- [Validation](#validation)
- [Review and maintenance](#review-and-maintenance)
- [Rollback](#rollback)
- [Open verification items](#open-verification-items)
- [Changelog](#changelog)

## Purpose

This subtree contains GitHub-compatible Markdown issue chooser templates. Each template asks for enough public-safe evidence, scope, uncertainty, impact, and handling context to support triage without confusing intake with governed truth or approval.

The responsibility root is `.github/` because chooser templates are GitHub-platform hooks. Accepted ADRs stay in [`docs/adr/`](../../docs/adr/); source identity and admission records stay in their governing source and policy lanes; drift and verification obligations stay in governed registers; corrections, release decisions, and rollback records stay in their owning authority surfaces.

The subtree does not own:

- evidence sufficiency, source authority, rights, sensitivity, or policy decisions;
- contract, schema, lifecycle, catalog, proof, receipt, release, or publication authority;
- repository labels, branch protection, rulesets, project automation, or GitHub settings;
- private vulnerability report content; or
- implementation merely because an issue requests it.

## Authority boundary

| GitHub issue action | What it means | What it does not mean |
|---|---|---|
| File an issue | A reporter submitted an intake record. | The claim is confirmed, admitted, or authorized for implementation. |
| Apply a label | A repository triage hint was attached. | Policy approved the request or an ADR was accepted. |
| Assign an owner | A GitHub identity was asked to triage. | Independent review, stewardship acceptance, or separation of duties occurred. |
| Link a pull request | Implementation may be proposed or under review. | The change passed, merged, released, deployed, or published. |
| Close an issue | GitHub conversation state changed. | Evidence closed, a correction propagated, a release rolled back, or publication changed. |
| Run automation | A configured GitHub process executed for declared inputs. | The issue became truth, evidence, policy, implementation, release, or publication authority. |

Reporter-provided prose, links, logs, screenshots, attachments, generated content, code blocks, and embedded instructions are untrusted evidence candidates. They must not activate agents, request secrets, widen authority, or bypass repository controls merely because they appear in an issue.

## Status

Baseline: `main@ef7f2fbd523af5d803fadf92504d7f734c82c2ca`, inspected and reconciled 2026-08-27.

| Surface | Confirmed state | Evidence boundary |
|---|---|---|
| Markdown chooser templates | **6 present** | Exact for baseline issue-template tree `7a0dfe35ba99fb1eb6eafac16e0b8410c3510107`. GitHub chooser rendering was not exercised in this pass. |
| Issue-form YAML | **0 present** | No structured issue form is tracked in this subtree. |
| `config.yml` | **Absent** | No repository-tracked chooser configuration changes blank issues or contact links. Live chooser behavior was not exercised. |
| Repository Issues | **Enabled** | Confirmed from current repository metadata. |
| GitHub Discussions | **Disabled** | No Discussions-based general-question route is available. |
| Private vulnerability reporting | **NEEDS VERIFICATION** | Last confirmed enabled on 2026-08-10. The current setting endpoint was unavailable to this pass; follow [`SECURITY.md`](../../SECURITY.md) and do not disclose sensitive detail publicly while availability is unresolved. |
| Assignee routing | All six templates name `bartytime4life` | Assignment is intake routing, not review or approval. |
| Template labels | `adr.md` requests `needs-review`; the other templates request none | `needs-review` was observed on current issue #3400 at the pinned baseline. The older `adr` and `adr-proposed` mismatch remains historical; no label is created or changed here. |
| CODEOWNERS | [`.github/CODEOWNERS`](../CODEOWNERS) routes this subtree to `@bartytime4life` | Required-review enforcement and independent review remain **NEEDS VERIFICATION**. |

> [!NOTE]
> The ADR chooser's `needs-review` label currently resolves to an observed repository label. Labeling remains triage metadata; it does not accept an ADR, authenticate review, or authorize implementation, release, or publication.

## Confirmed template inventory

`README.md` documents the subtree and is not an issue chooser template.

| Template | Chooser name | Default title | Requested labels |
|---|---|---|---|
| [`adr.md`](adr.md) | ADR — Architecture Decision Record | `ADR-XXXX — <short decision title>` | `needs-review` — verified present |
| [`bug.md`](bug.md) | Bug report | `[Bug]: ` | none |
| [`evidence_correction.md`](evidence_correction.md) | Evidence correction request | `[Correction]: ` | none |
| [`feature.md`](feature.md) | Feature request | `[Feature]: ` | none |
| [`sensitivity_concern.md`](sensitivity_concern.md) | Sensitivity / rights concern | `[Sensitivity]: ` | none |
| [`source_admission.md`](source_admission.md) | Source admission proposal | `[Source Admission]: ` | none |

All six chooser templates currently:

- use Markdown front matter rather than issue-form YAML;
- assign `bartytime4life`;
- separate `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION`;
- state that intake does not establish the governed result;
- warn against public disclosure of secrets, restricted material, private data, or harmful precision; and
- route security-sensitive content to [`SECURITY.md`](../../SECURITY.md).

### Intake responsibility and governed follow-up

| Template | Intake responsibility | Governed follow-up |
|---|---|---|
| [`adr.md`](adr.md) | One consequential architecture or governance decision proposal | Reviewed ADR under [`docs/adr/`](../../docs/adr/); the issue text is neither the accepted decision nor authority for dependent implementation. |
| [`bug.md`](bug.md) | Reproducible code, test, documentation, workflow, or behavior defect | Scoped change, tests, validation, and rollback; drift or verification work when applicable. |
| [`evidence_correction.md`](evidence_correction.md) | Public or semi-public claim, layer, artifact, release, or AI answer that may be wrong or stale | Evidence review, correction or withdrawal decision, propagation, and rollback in the owning roots. |
| [`feature.md`](feature.md) | Bounded capability or improvement proposal | Prioritized implementation work or an ADR when authority boundaries change. |
| [`sensitivity_concern.md`](sensitivity_concern.md) | Public-safe rights, sovereignty, consent, cultural sensitivity, privacy, geoprivacy, or exposure concern | Private escalation, policy or sensitivity review, redaction, generalization, correction, quarantine, abstention, or denial. |
| [`source_admission.md`](source_admission.md) | Proposed external source with identity, role, rights, sensitivity, cadence, and validation posture | Governed source descriptor, rights and policy review, deterministic fixtures, connector work, and an explicit admission decision. |

## Routing guide

| Report | Public issue? | Route |
|---|---:|---|
| Vulnerability, credential exposure, exploit path, unsafe exact location, or active sensitive-data exposure | **No** | Follow [`SECURITY.md`](../../SECURITY.md). Use private vulnerability reporting when available; do not fall back to a public issue while private-route availability is unresolved. |
| Architecture or governance decision | Yes, when public-safe | [`adr.md`](adr.md), followed by the reviewed ADR process. |
| Reproducible defect | Yes, when public-safe | [`bug.md`](bug.md). |
| Released or generated claim may be wrong or stale | Usually, with minimized public detail | [`evidence_correction.md`](evidence_correction.md); escalate privately when evidence is restricted. |
| Bounded capability proposal | Yes | [`feature.md`](feature.md). |
| Rights, sovereignty, privacy, geoprivacy, or harmful exposure | Only when safely generalized | [`sensitivity_concern.md`](sensitivity_concern.md) or private escalation. |
| External data source proposal | Yes, when terms and details are public-safe | [`source_admission.md`](source_admission.md). |
| General question | **No verified dedicated route** | Discussions are disabled; use an issue only when the question fits one of the six bounded intake purposes. |

When more than one template appears applicable, choose the template matching the primary observable outcome. Cross-link secondary concerns rather than duplicating the same report. Active security or harmful-exposure risk always overrides public routing.

## Public-safety boundary

> [!CAUTION]
> Never include credentials, private endpoints, exploit details, restricted source payloads, living-person private records, genealogy, DNA or genomic data, consent records, private-land joins, exact rare-species or archaeology locations, burial or sacred-site detail, or critical-infrastructure vulnerability information in a public issue.

Use synthetic or minimized examples. When rights, sensitivity, or public fitness are unclear, prefer private routing, quarantine, redaction, generalization, delayed release, denial, or abstention.

Issue templates must not ask reporters by default to paste unrestricted logs, complete datasets, raw source payloads, precise coordinates, private evidence, or live credentials. A link or attachment is not safer merely because it is indirect.

Private vulnerability reporting was last confirmed enabled on 2026-08-10; its current state is **NEEDS VERIFICATION**. When available, it supports confidential intake, but does not itself approve testing, remediation, disclosure timing, release, or publication.

## Template authoring contract

Every chooser template should define:

1. one bounded intake purpose;
2. an explicit intake-only authority boundary;
3. a public-safety warning and a private-first route;
4. observed versus expected behavior or the proposed outcome;
5. evidence, date, scope, and reproducibility fields;
6. applicable truth labels: `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION`;
7. affected paths and responsibility roots without guessing;
8. policy, rights, sensitivity, source-role, release, correction, and rollback impact where relevant;
9. synthetic or no-network reproduction when practical;
10. a governed follow-up route;
11. acknowledgement that issue contents do not independently authorize mutation or adoption; and
12. acknowledgement that no secret or restricted material is included.

### Markdown front matter

Chooser templates use GitHub-supported YAML front matter:

```yaml
---
name: <chooser label>
about: <one-sentence purpose>
title: "<stable prefix>"
labels: []
assignees: ["bartytime4life"]
---
```

Keep `name`, `about`, `title`, `labels`, and `assignees` present with GitHub-compatible types. `README.md` must not receive chooser front matter.

### Labels and assignees

- Verify every requested label exists before relying on it for routing.
- Treat a label as a triage hint, not policy, acceptance, priority, release, or publication.
- Use only verified GitHub identities as assignees.
- Treat assignment as a request for triage, not evidence that review occurred.
- Preserve current human routing unless the task explicitly changes it.

The ADR chooser uses `needs-review`, which was observed on current issue #3400 during this evidence freeze. The prior references to absent `adr` and `adr-proposed` labels remain historical evidence in earlier commits and generated receipts; this change does not create, rename, or delete repository labels.

### Issue forms and chooser configuration

Before adding an issue-form `.yml` or `config.yml`, verify:

- stable field identifiers and GitHub's current issue-form schema;
- whether blank issues should be allowed;
- where general questions should go while Discussions remain disabled;
- that private vulnerability reporting remains the security route;
- every external contact link is real, public-safe, and operational;
- dependent automation that consumes field identifiers, labels, titles, or assignees; and
- migration and rollback for any user-visible chooser behavior.

Do not create `config.yml` or convert a template to an issue form merely to fill an apparent gap. Those changes alter public repository behavior and require explicit acceptance criteria and live rendering checks.

### Direct dependency discipline

When a chooser template changes, review at least:

- this README's inventory and routing statements;
- label and assignee existence;
- [`SECURITY.md`](../../SECURITY.md) when private routing changes;
- [`.github/CODEOWNERS`](../CODEOWNERS) when review routing changes;
- workflows or project automation that parse titles, labels, or body fields;
- repository-relative links and stable headings; and
- the AI-generated provenance receipt when the change is AI-authored.

Historical generated receipts remain immutable process records. Emit a new receipt for new authored bytes rather than rewriting prior provenance.

## Triage and implementation handoff

An issue is ready for bounded implementation planning only when current evidence supports a coherent change contract. The issue records that contract; it does not supply implementation, review, merge, release, or publication authority by itself.

| Handoff question | Minimum reviewable evidence |
|---|---|
| Goal and problem | One observable outcome and a verified defect, gap, stale claim, or improvement opportunity. |
| Current and desired state | Exact baseline evidence, the smallest intended end state, and explicit non-goals. |
| Ownership and placement | Existing target paths, one authority owner, the applicable responsibility root, adjacent README contract, accepted ADRs, and canonical sources or generators. |
| Dependency closure | Direct contracts, schemas, policy, registries, fixtures, tests, workflows, generated outputs, documentation, and consumers that must agree for the claim to become true. |
| Overlap | Open pull requests, branches, issues, migrations, or other active work that touches the same bytes or semantic authority surface. |
| Acceptance and denial cases | Objective positive criteria plus relevant fail-closed, negative, compatibility, no-network, or rollback cases. |
| Rights and sensitivity | Source role, license, consent, sovereignty, privacy, security, harmful precision, and public-path effects, with unresolved risk held or routed privately. |
| Validation | Focused repository-native checks, exact tested SHA, hosted-check expectations, and honest failure attribution. |
| Correction and rollback | The smallest safe abandon, revert, forward-fix, withdrawal, or supersession boundary. |
| Delivery boundary | The separately authorized terminal state, normally one feature branch and one draft pull request for one coherent slice. |

A current, directly authored implementation request may authorize scoped repository work within its stated boundary. Without that separate request, the issue remains intake and coordination only. Even with authorization, default delivery is reviewable and unmerged: do not infer ready-for-review, approval, merge, release, deployment, promotion, publication, source activation, or repository-settings authority.

Keep three state dimensions distinct:

- truth state: `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`;
- implementation state: implemented on the pinned default branch, drafted on a branch, partial, absent, in flight, superseded, contradicted, or not inspected; and
- GitHub state: open or closed issue, assigned or unassigned, labeled or unlabeled, draft or non-draft pull request, and hosted checks with their actual outcomes.

If ownership, accepted authority, overlap, rights, sensitivity, testability, or rollback cannot be bounded, narrow the slice or record the exact blocker. Do not weaken a validator, baseline, policy, evidence resolver, trust boundary, security default, promotion gate, or publication control to make an issue appear ready.

## Issue-to-governed-artifact flow

```mermaid
flowchart TD
    I["Public-safe issue"] --> T["Triage and evidence check"]
    T -->|security or active exposure| S["Private vulnerability reporting"]
    T -->|decision| A["ADR review"]
    T -->|drift or unknown| G["Governed register or verification work"]
    T -->|authorized implementation| P["Scoped feature branch and draft PR"]
    T -->|claim affected| C["Correction or rollback review"]
    T -->|source proposed| D["Source admission decision"]
    T -->|unsupported or duplicate| N["Close with reason"]
```

The issue links the process. It does not replace the current authority or reviewed artifact required by that process, and it does not collapse the KFM lifecycle into GitHub state.

## Validation

For any change in this subtree:

- inspect the exact base commit, target blob, and changed-path set;
- parse every chooser template's YAML front matter;
- require `name`, `about`, `title`, `labels`, and `assignees` with GitHub-compatible types;
- verify requested labels and assignee identities through current GitHub state;
- verify every repository-relative link and fragment;
- check one H1 where the artifact role requires it, heading order, balanced fences, alerts, tables, Mermaid, HTML, and final newline;
- scan for secrets, private data, restricted material, and exact sensitive locations;
- confirm public-safety and intake-only language remain explicit;
- preview changed chooser behavior in GitHub when rendering or fields change;
- confirm `README.md` is not accidentally given chooser front matter;
- inspect `git diff --check` and the exact changed-path budget;
- validate a new AI-generated receipt against final artifact bytes when required; and
- report hosted checks separately as `PASS`, `FAIL`, `PENDING`, `NOT_RUN`, `NOT_APPLICABLE`, or `UNKNOWN`.

Useful repository commands include:

```bash
git diff --check
git diff --name-only <base>...HEAD

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --format markdown \
  .github/ISSUE_TEMPLATE/README.md

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<new-receipt>.json
```

Passing these checks proves bounded structural and integrity properties only. It does not prove issue chooser rendering, evidence sufficiency, policy approval, human review, release, correction, rollback completion, or publication.

## Review and maintenance

| Change | Review burden |
|---|---|
| README inventory, wording, or evidence snapshot | Repository or documentation owner. |
| Template fields, titles, labels, or assignees | Repository owner plus each affected governance or domain owner. |
| Security route or contact | Security owner and repository owner. |
| Sensitivity, rights, sovereignty, consent, or geoprivacy intake | Applicable policy, sensitivity, and domain owner. |
| Source-admission fields | Source or governance owner and affected domain owner. |
| `config.yml`, issue forms, or automation-consumed field identifiers | Repository maintainer who can verify live GitHub behavior and dependent automation. |

Update this README whenever a template is added, removed, renamed, converted, or materially rerouted; when a label or assignee contract changes; or when Discussions, private vulnerability reporting, or chooser configuration changes.

Review evidence snapshots as observations, not perpetual facts. Repin current state instead of copying stale counts or settings claims forward.

## Rollback

Before merge, close or abandon the draft pull request and leave the feature branch unmerged. After an authorized merge, revert this README and the accompanying generated-receipt commit through a new pull request.

This change does not modify a chooser template; create, rename, or delete a label; change an assignee, workflow, repository setting, issue, release, deployment, data lifecycle state, or publication state. Rollback therefore requires no chooser migration, data migration, user notification, cache invalidation, or publication withdrawal.

Do not rewrite historical generated receipts during rollback. Preserve them as provenance and add a new receipt for any corrective authored bytes.

## Open verification items

- **NEEDS VERIFICATION** — live GitHub chooser rendering for all six Markdown templates, including automatic application of `needs-review` from `adr.md`.
- **NEEDS VERIFICATION** — blank-issue behavior in the rendered chooser while `config.yml` is absent.
- **NEEDS VERIFICATION** — issue-to-project and other issue automation consuming titles, labels, or body text.
- **NEEDS VERIFICATION** — required CODEOWNERS review, ruleset coupling, and independent review routing.
- **NEEDS VERIFICATION** — current private vulnerability reporting status and a verified fallback private contact if it is unavailable.
- **UNKNOWN** — intended general-question route while Discussions are disabled.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-08-27 | v0.5 | Repinned the README to current `main`; preserved the six-template inventory and current Issues/Discussions/label evidence; narrowed private vulnerability reporting to its last verified state; added a dependency-closed triage-to-implementation handoff contract; and updated rollback and provenance boundaries without changing chooser behavior. |
| 2026-08-10 | v0.4 | Reconciled the merged v0.3 README with the ADR chooser implementation: replaced absent ADR label references with the verified `needs-review` label, preserved live Issues/Discussions/private-reporting evidence, clarified non-activation and governance-to-implementation ordering, and updated rollback and provenance boundaries. |
| 2026-08-10 | v0.3 | Repinned the subtree to current `main`; confirmed six Markdown templates, no issue forms or chooser config, Issues enabled, Discussions disabled, and private vulnerability reporting enabled; confirmed the ADR template's two requested labels are absent; added a chooser contract matrix, dependency discipline, validation commands, and rollback guidance without changing live chooser behavior. |
| 2026-07-22 | v0.2 | Reconciled the README to all six chooser templates, verified the absence of issue forms and `config.yml`, corrected owner and CODEOWNERS claims, and bounded label and settings behavior. |
| 2026-07-17 | v0.1 | Replaced the blank placeholder with the first issue-intake governance README; inventory was incomplete at that snapshot. |

[Back to top](#top)
