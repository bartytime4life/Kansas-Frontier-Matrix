# CHANGELOG

Repository-wide record of governed, release-significant, and behavior-significant changes across doctrine, contracts, data and evidence workflows, public surfaces, verification, and operations.

**Quick jumps:** [Scope](#scope) · [Entry rules](#entry-rules) · [Unreleased](#unreleased) · [2026-03-14](#2026-03-14) · [2026-03-13](#2026-03-13) · [2026-03-12](#2026-03-12) · [2026-03-10](#2026-03-10)

> This file is evidence-first.
>  
> When a repo-wide release tag or mounted implementation history is not directly verified, entries use dated milestones instead of invented version numbers.

## Scope

This changelog tracks project-level changes that materially affect one or more of the following:

- doctrine, invariants, or trust posture
- contract families, schemas, or route classes
- lifecycle, promotion, correction, or review behavior
- public or steward-facing product surfaces
- verification, policy, release, or evidence-resolution behavior
- deployment or runtime boundary posture

Do not use this file for minor wording-only edits unless they materially change behavior, governance posture, or release meaning.

## Entry rules

- Keep entries reverse chronological.
- Prefer one concise bullet per change.
- Use the smallest truthful scope.
- When available, link each entry to the governing artifact: ADR, PR, schema diff, workflow run, release receipt, proof pack, or correction notice.
- If implementation evidence is missing, say so explicitly instead of implying live behavior.
- Use these labels when helpful: `Added`, `Changed`, `Clarified`, `Removed`, `Deprecated`, `Security`, `Verification`.

## Unreleased

### Added

- Established a root-level repository changelog structure for governed, project-wide change tracking.
- Added entry rules that prioritize evidence-linked, release-significant updates over narrative summaries.

### Clarified

- Historical entries below are limited to milestones directly evidenced in the attached KFM corpus.
- Dates are used in place of repo-wide release tags where a mounted tag history was not verified.
- Repo, CI, deployment, schema, and runtime facts should remain explicit when they are still unknown.

## 2026-03-14

### Changed

- Ratified one central master-reference direction that treats KFM as a governed spatial evidence system rather than a loose set of maps, stories, graphs, and assistant surfaces.
- Consolidated the documentation center of gravity around governed publication, the canonical truth path, the trust membrane, authoritative-versus-derived separation, map-first and time-aware product logic, and documentation as a production surface.
- Reframed the master manual as the central source of truth for system identity, doctrine, domain model, interfaces, governance, operations, and roadmap sequencing.

### Added

- Made the five-plane system model, contract families, runtime outcomes, surface states, verification backlog, and minimal next-artifact plan explicit in the canonical documentation layer.
- Deepened shell choreography, dossier / story / Focus relationships, 2D-versus-3D discipline, and trust-visible surface-state handling.

### Clarified

- Kept live repo, schema, workflow, manifest, and runtime claims explicit as `UNKNOWN` where the current session verified PDF evidence only.

## 2026-03-13

### Added

- Expanded the contract / surface / artifact realization layer with standards-profile recommendations, route-class mapping, visible surface-state semantics, repo/file backlog, and change-controlled standards pinning.
- Formalized verification as a cross-cutting governance layer spanning intake, canonical truth, catalog / policy / review, derived delivery, and runtime trust surfaces.
- Added a phase-one local Ubuntu runtime design that keeps Ollama behind a governed API, local-only, replaceable, and downstream of evidence resolution and policy enforcement.

### Clarified

- Strengthened the rule that fluent architecture prose is not proof of implementation.
- Preserved rollback posture: if later direct repo inspection contradicts additive realization detail, downgrade that detail back to `PROPOSED` or `UNKNOWN`.

## 2026-03-12

### Changed

- Shifted the highest-value documentation move from broad re-description to consolidation and artifactization.
- Re-centered primary documentation around a joint doctrinal baseline, sharper executable structure, an integrated map-first surface model, and an explicit verification backlog.

### Added

- Prioritized the next build layer: executable contract families, one governed thin slice, verified implementation baseline, source-onboarding and metadata closure, Kansas data-gap closure, and operational rights / sensitivity workflows.
- Strengthened the domains and source atlas with clearer source-role discipline, publication burdens, and domain-specific verification pressure.

### Clarified

- Marked overclaim-prone areas more explicitly, especially literal repo paths, DTO names, workflow names, deployment overlays, and other implementation-shaped claims not directly visible in the session.

## 2026-03-10

### Added

- Published the March 2026 doctrinal anchor set that defines KFM as an evidence-first, map-first, time-aware, governed spatial evidence system.
- Strengthened lifecycle language around the canonical path from source edge through publication and the distinction between authoritative truth and derived projections.
- Added a security-first runtime direction for local model serving: least-privilege, private-first, governed API boundary, and cite-or-abstain behavior for model-assisted responses.

### Security

- Made direct public exposure of the model runtime a non-default posture.
- Reaffirmed that UI and clients must not bypass governed APIs or access canonical stores directly.

## Maintenance notes

- Keep entries reverse chronological.
- Prefer dated sections until repo-wide release tags are directly verified.
- When a future tagged release process exists, add version headings above or in place of dated milestones rather than rewriting history.
- Preserve negative outcomes as first-class changes when they materially alter release posture: `abstain`, `deny`, `withdraw`, `generalize`, `quarantine`, `supersede`, or `rollback`.
