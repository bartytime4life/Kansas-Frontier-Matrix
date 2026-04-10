# Heritage Lane Roadmap and Verification Backlog

Scope: prioritized follow-on artifacts and open verification tasks for making the heritage lane fully enforcement-ready.

## Phase 1 survey summary (current-state audit)

### Strong docs to preserve

- `README.md` lane framing and evidence-first posture.
- GEDCOM intake and downstream pipeline docs.
- examples/fixtures lane-local companion docs.

### Thin or redundant areas to repair

- Source-role guidance was distributed but not consolidated into one lane reference.
- Rights/sensitivity rules were present but not centralized for reviewer use.
- Entity/evidence artifact mapping to trust objects needed explicit lane-level table.

### Gaps now filled in this pass

- Added dedicated docs for source roles, rights/sensitivity, entity/evidence model, and publication/review.
- Added explicit open unknowns rather than implied implementation certainty.

## Priority roadmap

| Priority | Artifact | Status | Why it matters |
|---|---|---|---|
| P0 | Heritage source descriptor examples tied to lane roles | PROPOSED | Converts doctrine into reviewable, machine-adjacent examples. |
| P0 | Rights/sensitivity decision templates for steward review | PROPOSED | Reduces inconsistent publication decisions. |
| P1 | Heritage contract/fixture alignment pass with schemas/contracts | NEEDS VERIFICATION | Prevents doc-contract drift. |
| P1 | Publication checklist runbook for dossier/story/focus/export | PROPOSED | Makes trust-critical visibility testable before release. |
| P2 | Lane-specific CI checks for quote-safety and precision narrowing | UNKNOWN | Moves heritage policy from prose to enforcement. |
| P2 | Canonical split decision: `archives-heritage` vs standalone `heritage` | NEEDS VERIFICATION | Clarifies long-term lane topology. |

## Open unknowns

- **UNKNOWN:** exact schema and policy bundles currently enforcing heritage rights/sensitivity gates.
- **NEEDS VERIFICATION:** active workflow/CI checks for lane-specific publication constraints.
- **NEEDS VERIFICATION:** maintainer and steward ownership map for this lane.
- **UNKNOWN:** full registry of heritage source families with machine-usable descriptors.

## Definition of done (for next pass)

- Heritage source-role and rights rules reflected in fixtures/tests (not prose only).
- At least one lane-specific publication review checklist runnable in CI or review tooling.
- Contract/schema references for lane-critical artifacts are path-accurate and verified.
- Unknowns reduced; remaining uncertainty explicitly tracked.

