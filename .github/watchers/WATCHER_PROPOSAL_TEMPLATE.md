# Watcher Proposal Template

Use this template for PRs that add or change watcher behavior.

## 1) Truth posture
- **Status:** `PROPOSED` / `CONFIRMED`
- **Owner surface (runtime code):** `<path>`
- **Workflow orchestration path:** `.github/workflows/<file>.yml`

## 2) Scope and source
- **Source family:**
- **Scope window / cadence:**
- **Claim class:**

## 3) Bounded paths
- **Work path:** `data/work/<lane>`
- **Receipt path:** `data/receipts/<lane>`
- **Optional proof path:** `data/proofs/<lane>`

## 4) Validation and policy
- **Contract/schema validation command(s):**
- **Policy gate command(s):**
- **Failure behavior:** fail-closed / deny-by-default

## 5) Rollback and supersession
- **Rollback trigger:**
- **Supersession process:**
- **Human review checkpoint:**

## 6) Evidence checklist
- [ ] Runtime owner path exists and is linked.
- [ ] Workflow YAML exists and is linked.
- [ ] Validation/policy command outputs included.
- [ ] Receipt example attached.
- [ ] Rollback notes included.
- [ ] No autonomous publish authority introduced.
