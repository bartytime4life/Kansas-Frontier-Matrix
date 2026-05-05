# Fauna Rollback Runbook

Purpose: quickly and safely withdraw or revert a fauna release when policy, evidence, rights, or quality issues are discovered.

## Rollback triggers

- Sensitive location exposure risk.
- Incorrect legal/status claim in released outputs.
- Evidence reference broken or non-resolving.
- Corrupt or incomplete release manifest.

## Immediate actions

1. Stop new publication/promotions for fauna lane.
2. Repoint public aliases to prior known-good release.
3. Invalidate affected caches and public artifacts.
4. Publish correction notice with scope and user impact.

## Recovery checklist

- [ ] Incident ticket opened with timestamp and owner.
- [ ] Impacted artifacts/layers/endpoints enumerated.
- [ ] Known-good release confirmed and restored.
- [ ] Correction lineage recorded in release notes.
- [ ] Follow-up validation and prevention action assigned.

