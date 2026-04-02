<!--
doc_id: NEEDS VERIFICATION
title: KFM Overlay Consent Tokens & Revocation Enforcement
type: standard
version: v1
status: draft
owners: @bartytime4life (NEEDS VERIFICATION)
created: 2026-04-01
updated: 2026-04-01
policy_label: public (NEEDS VERIFICATION)
related: [docs/governance/ROOT_GOVERNANCE.md, docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md]
tags: [kfm, overlays, consent, governance, geoprivacy, security, odrl]
notes: [Baseline PROPOSED until in‑repo enforcement visible; integrate with EvidenceBundle receipts]
-->

# KFM Overlay Consent Tokens & Revocation Enforcement

> One‑line: **Short‑lived, scope‑bounded consent tokens, verified at read/publish time, with fail‑closed revocation and run receipts that carry consent provenance.**

---

## 1) Scope
- **Applies to:** Any KFM map/timeline overlay that could reveal sensitive location, person, species, site, or cultural information.
- **Out of scope:** Internal non‑materialized debug layers; synthetic fixtures that cannot map back to real world subjects (document any exceptions explicitly).

## 2) Problem (Why this exists)
We must not publish or materialize overlays unless the data subject(s) or steward(s) have granted consent **for a specific place, time, and use**—and we must be able to **revoke** that permission later with visible evidence.

## 3) Design (High level)
We issue **KMS‑signed, short‑lived consent tokens** (JWT‑style) that carry only minimal claims. Every overlay build/read/publish path:
1) **Validates signature + expiry.**
2) **Asserts scope** (geographic bucket, time window, overlay IDs, permitted uses).
3) **Checks revocation** (daily manifest + realtime introspection).
4) **Emits a run receipt** that embeds consent metadata and the *checked* revocation root.
5) **Fails closed** if anything is invalid or revoked.

---

## 4) Token Format (Minimal Claims)
**Token header**
- `alg`: signing algorithm (e.g., ES256)
- `kid`: KMS key id
- `typ`: `JWT`

**Token claims (payload)**
| Claim | Type | Required | Notes |
|---|---:|:---:|---|
| `iss` | str | ✓ | Issuer (KFM consent service) |
| `sub` | str | ✓ | Subject (steward record id or bundle id) |
| `aud` | str | ✓ | `kfm/overlays` |
| `overlay_ids` | array<str> | ✓ | Allowed overlay identifiers |
| `geobucket` | obj | ✓ | Coarse geography only (e.g., `{"standard":"geohash","precision":5}` or `{"standard":"us_admin","level":"county"}`) |
| `time_window` | obj | ✓ | `{ "start":"YYYY-MM-DD", "end":"YYYY-MM-DD" }` |
| `permitted_uses` | array<str> | ✓ | e.g., `["research-generalized","steward-review"]` |
| `obligations` | array<obj> | ✓ | ODRL‑style (see §6) |
| `iat` | int | ✓ | Issued at (epoch seconds) |
| `exp` | int | ✓ | Short TTL (e.g., <= 7 days) |
| `spec_hash` | str | ✓ | Hash of this spec version adhered to |
| `consent_token_hash` | str | ✓ | Self‑hash for receipts (redundant but helpful) |

> **IMPORTANT**  
> - **No precise geometry** in the token.  
> - Geobucket precision must be **coarser than any published map scale** unless a restricted path is proven.

---

## 5) Revocation (Fail‑closed)
Two complementary checks **every time** before materializing/publishing:
1) **Daily Revocation Manifest**  
   - Signed file containing: `revocation_root` (Merkle root), optional Bloom filter or explicit TRL (token revocation list), issuance timestamp.
   - Bundled into builds; stored next to receipts.
2) **Realtime Introspection Endpoint**  
   - Input: `consent_token_hash`  
   - Output: `{ status: active|revoked|unknown, seen_at: ts, revocation_root: hash }`

**Rule:** If **either** check indicates revoked or unknown → **DENY** (fail‑closed).

---

## 6) Obligations (ODRL‑style mini‑schema)
Each obligation is an object with:
```json
{
  "action": "redact|generalize|retain-until|provenance|purge-on-revoke",
  "target": "geometry|attributes|evidence_links|run_artifacts",
  "params": { "retain_until": "YYYY-MM-DD", "generalize_to": "geohash/5|county", "redact_fields": ["owner_name","precise_coord"] }
}
```
**Enforcement points**
- **At build:** apply `generalize`/`redact` before writing tiles/frames.
- **At publish:** assert obligations satisfied (policy gate).
- **On revocation:** execute `purge-on-revoke` and emit a **rollback run receipt**.

---

## 7) Steward Record + Verify Checklist (UI‑light, mandatory)
Store alongside token (keyed by `consent_token_hash`):

- **Steward record (required fields)**
  - `consent_token_hash`
  - `issuer`
  - `spec_hash`
  - `scope`: `{ geobucket, time_window, overlay_ids }`
  - `permitted_uses[]`
  - `obligations[]`
  - `issued_at`, `expires_at`
  - `revocation_root_at_issue`

- **Verification steps (must pass)**
  1. Verify **signature** with KMS public key (by `kid`).
  2. Assert **geobucket enforcement** matches requested output scale(s).
  3. Run **revocation checks** (daily manifest + introspection).
  4. Embed **consent metadata** in every **run receipt**.
  5. On **revocation event**: emit **rollback run receipt**; execute obligations (purge/generalize/redact); log retention actions.

---

## 8) Run Receipt (what we write every time)
A `run_receipt.json` (or YAML) adjacent to outputs:

```json
{
  "run_id": "UUID",
  "when": "2026-04-01T12:34:56Z",
  "inputs": ["EvidenceBundle:..."],
  "outputs": ["tiles://...","frames://..."],
  "consent": {
    "consent_token_hash": "sha256-...",
    "issuer": "kfm-consent",
    "scope": { "overlay_ids": ["..."], "geobucket": {"standard":"geohash","precision":5}, "time_window": {"start":"...","end":"..."} },
    "permitted_uses": ["research-generalized"],
    "obligations": [{"action":"generalize","target":"geometry","params":{"generalize_to":"geohash/5"}}],
    "token_status": "active|revoked|unknown",
    "revocation_root_checked": "merkle-root-hex"
  },
  "policy": {
    "spec_hash": "sha256-...",
    "checks": ["sig_ok","scope_ok","revocation_ok","obligations_ok"],
    "decision": "ANSWER|ABSTAIN|DENY|ERROR"
  }
}
```

**Publish rule:** If `token_status != active` → **block publishing**.

---

## 9) CI & Runtime Policy Gates
- **Conftest/OPA Gate (CI):**  
  - Regressions fail if receipts are missing consent blocks, if scope > allowed output precision, or if a revoked token appears.
- **Runtime PDP/PEP:**  
  - PDP evaluates consent + obligations + scope.  
  - PEP in publishers/renderers **enforces** the decision; **no bypass**.

---

## 10) Implementation Sketch (INFERRED)
```mermaid
flowchart TD
  A[Request overlay build/read] --> B[Load consent token]
  B --> C[Verify KMS sig + exp]
  C --> D[Assert scope: overlay_ids, geobucket, time window]
  D --> E[Revocation checks: daily manifest + introspection]
  E -->|revoked/unknown| X[DENY (fail-closed)]
  E -->|active| F[Apply obligations (redact/generalize)]
  F --> G[Materialize outputs]
  G --> H[Write run_receipt with consent + revocation root]
  H --> I[OPA/Conftest gate]
  I -->|pass| J[Publish]
  I -->|fail| X
```

---

## 11) Security & Privacy Notes
- **Short TTLs** reduce blast radius; rely on re‑issuance for extended work.
- **Coarse geobuckets** by default; precise views must route through **restricted** paths with additional policy and logging.
- **No subject PII** in tokens; steward records keep linkage privately.
- **Receipts are evidence**—do not ship without them.

---

## 12) Ops Playbook (Day‑2)
- Rotate KMS keys quarterly; pin acceptable `kid` set in policy.
- Regenerate and publish **revocation manifest** daily (or more often).
- Alert if an introspection says `unknown` for any in‑flight run.
- Periodic audit: sample receipts; replay OPA decisions; verify purge on historical revocations.

---

## 13) Interfaces (PROPOSED)
- **POST** `/consent/introspect` → `{consent_token_hash} -> {status, revocation_root, seen_at}`
- **GET** `/consent/revocation-manifest.json` → `{revocation_root, bloom|trl, issued_at, sig}`

---

## 14) Migration Guidance
- Start by wrapping **publishers** first (fail‑closed at the edge).
- Backfill **run_receipts** for recent outputs; mark legacy items as `UNKNOWN` status and quarantine if necessary.
- Add **geobucket assertions** to all renderer configs (unit tests + policy tests).

---

## 15) FAQs
**Q: Why both manifest and introspection?**  
A: Defense‑in‑depth. Manifests cover offline/air‑gapped runs; introspection covers near‑real‑time revocations.

**Q: Can a single token cover multiple overlays?**  
A: Yes, but list them explicitly in `overlay_ids` and keep TTL short.

**Q: What if obligations conflict with a renderer capability?**  
A: DENY and open a remediation ticket; never silently degrade obligations.

---

## 16) Definition of Done (for adoption)
- [ ] Conftest/OPA policies merged; CI fails on missing/invalid consent blocks  
- [ ] Publishers call introspection and verify manifest root  
- [ ] Run receipts emitted and archived for every run  
- [ ] Purge/generalization job wired for `purge-on-revoke`  
- [ ] Ops rotation + alerting in place

---
[Back to top](#kfm-overlay-consent-tokens--revocation-enforcement)