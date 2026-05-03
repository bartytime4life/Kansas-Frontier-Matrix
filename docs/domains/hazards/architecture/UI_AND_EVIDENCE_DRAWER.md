# Hazards UI and Evidence Drawer

UI surfaces must preserve source-role semantics and policy posture.

## Drawer minimums

- Claim title and hazard type.
- `source_role` badge.
- “What this is” and “What this is not”.
- Time basis + freshness signal.
- Evidence links (`EvidenceBundle`/references).
- Rights/sensitivity posture.
- Review/correction/supersession state.
- Operational disclaimer when role is warning/advisory/watch.

## Map requirements

- Layers read governed released artifacts only.
- No browser-to-raw-source fetch paths.
- Legends and chips are role-aware.
- Hidden/blocked states show explicit denial or abstain messaging.

## Negative states

| State | User-visible behavior |
| --- | --- |
| `ABSTAIN` | Explain insufficient support and offer evidence drill-through. |
| `DENY` | Show policy-safe denial category, no sensitive leakage. |
| `ERROR` | Show stable error shell and audit reference. |
