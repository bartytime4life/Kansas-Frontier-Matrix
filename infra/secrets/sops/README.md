<!--
KFM Governed Artifact
Path: infra/secrets/sops/README.md
Status: scaffold (enforcement not proven end-to-end)
-->

# 🔐 SOPS Secrets (GitOps-safe)

![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![Secrets](https://img.shields.io/badge/secrets-encrypted-blue)
![KFM](https://img.shields.io/badge/KFM-evidence--first-success)

This directory defines **how KFM stores and handles infrastructure/application secrets** in a way that supports GitOps workflows **without committing plaintext secrets to Git**.

We use **SOPS** to keep secrets **encrypted at rest in the repository** and decrypted **only at the last responsible moment** (developer workstation, CI runner, or cluster-side automation).

> [!IMPORTANT]
> **Never commit plaintext secrets.** If a secret was ever committed in plaintext, assume it is compromised: rotate it, revoke it, and treat Git history as hostile.

---

## Contents

- [What belongs here](#what-belongs-here)
- [Non-negotiable rules](#non-negotiable-rules)
- [Directory layout](#directory-layout)
- [Quick start](#quick-start)
- [Workflows](#workflows)
  - [Create a new secret](#create-a-new-secret)
  - [Edit an existing secret](#edit-an-existing-secret)
  - [Decrypt for local use](#decrypt-for-local-use)
  - [CI/CD usage](#cicd-usage)
- [Key management](#key-management)
- [Rotation and revocation](#rotation-and-revocation)
- [Guardrails (pre-commit + CI)](#guardrails-pre-commit--ci)
- [Risks and tradeoffs](#risks-and-tradeoffs)
- [Troubleshooting](#troubleshooting)

---

## What belongs here

✅ **Secrets and credentials** needed to run KFM infrastructure and services, such as:

- Database passwords / connection strings
- Service-to-service tokens
- Object store credentials
- Third-party API tokens (only if truly required)
- Deployment keys (scoped, minimal privileges)

❌ **What does *not* belong here:**

- Dataset content (even if “sensitive”)
- Sensitive cultural/tribal knowledge that should be governed via KFM’s **data zones + policy gates**  
  *(Encrypting restricted knowledge is not a substitute for governance review.)*
- Anything that the browser/UI could ever receive (trust membrane)

---

## Non-negotiable rules

> [!WARNING]
> These are merge-blocking invariants. If we can’t enforce them yet, treat this README as a **to-do list for governance gates**.

1. **No plaintext secrets in Git. Ever.**
2. **SOPS keys do not live in the repo.**
3. **Decryption happens only in controlled execution contexts**:
   - local developer machine (interactive)
   - CI runner (ephemeral)
   - cluster-side automation (if configured)
4. **Do not print decrypted content** to logs or terminals that are captured.
5. **Least privilege** for every credential:
   - scope per environment (dev/stage/prod)
   - rotate on schedule or incident
6. **PR review required** (CODEOWNERS) for:
   - `.sops.yaml` changes
   - any secret file changes
   - any CI changes that touch decryption/apply steps

---

## Directory layout

> [!NOTE]
> Some items below are recommended companion artifacts (not confirmed in repo yet). Add them as needed.

```text
infra/
└─ secrets/
   └─ sops/
      ├─ README.md                 # (this file)
      ├─ .sops.yaml                # SOPS creation rules (recommended)
      ├─ encrypted/                # Encrypted artifacts committed to Git
      │  ├─ dev/
      │  ├─ stage/
      │  └─ prod/
      ├─ templates/                # Non-sensitive templates/examples (no real secrets)
      └─ scripts/                  # Helper scripts (no secret material)
```

**Conventions**
- Encrypted secrets live under: `infra/secrets/sops/encrypted/<env>/...`
- Templates (safe to share) live under: `infra/secrets/sops/templates/...`

---

## Quick start

### Prereqs

- Install `sops` locally.
- Choose an encryption backend (one of):
  - **age** (recommended for local simplicity)
  - **GPG**
  - **KMS** (cloud KMS, if applicable)

> [!TIP]
> If you don’t know which backend KFM uses yet, treat it as **TBD** and add a small decision record (ADR) later. This README is compatible with any SOPS backend.

### Verify SOPS works

```bash
sops --version
```

---

## Workflows

### Create a new secret

**Preferred (avoids ever writing plaintext to disk):**
1. Create the encrypted file directly:
   ```bash
   mkdir -p infra/secrets/sops/encrypted/dev
   sops infra/secrets/sops/encrypted/dev/example.secret.yaml
   ```
2. Your editor opens. Add the secret content (e.g., a Kubernetes Secret manifest).
3. Save/exit. The file stays encrypted on disk.

> [!IMPORTANT]
> Do **not** copy/paste secrets into Slack issues, PR descriptions, CI logs, or screenshots.

---

### Edit an existing secret

```bash
sops infra/secrets/sops/encrypted/dev/example.secret.yaml
```

---

### Decrypt for local use

For debugging or local application (do not persist decrypted output):

```bash
sops -d infra/secrets/sops/encrypted/dev/example.secret.yaml | kubectl apply -f -
```

> [!WARNING]
> Avoid saving decrypted output to a file. If you must, store it in a temp location that is:
> - excluded by `.gitignore`
> - excluded by backup/sync tooling
> - deleted immediately after use

---

### CI/CD usage

**Goal:** CI can decrypt and apply secrets **without** ever committing plaintext or printing secret values.

Common patterns:
- Store the decryption key material in the CI platform’s secret store.
- Scope secrets to environments (dev/stage/prod).
- Ensure logs do not echo decrypted content (disable `set -x`; avoid printing env vars).

Example (conceptual):
```bash
# 1) Acquire decryption credentials from CI secret store (platform-specific)
# 2) Decrypt in-memory / pipe to apply
sops -d infra/secrets/sops/encrypted/${ENV}/example.secret.yaml | kubectl apply -f -
```

> [!NOTE]
> If your GitOps controller supports in-cluster SOPS decryption, you may shift decryption from CI → cluster.
> Keep the same invariants: keys protected, no plaintext in Git, no plaintext in logs.

---

## Key management

> [!IMPORTANT]
> Keys are the **root of trust**. Treat key handling as a governed process.

### Key rules

- **Never commit private keys** (or exported key material) to Git.
- Prefer **separate keys per environment** (at minimum: prod separate from non-prod).
- Limit who/what can decrypt:
  - developer keys for dev only
  - CI keys for staging/prod only
  - cluster keys (if used) namespace-scoped and tightly RBAC’d

### Recommended practice

- Store keys in:
  - a password manager / vault
  - a hardware-backed store (if available)
  - CI secret store (environment-scoped)
- Keep an access roster (who can decrypt which environment).

---

## Rotation and revocation

> [!WARNING]
> If a plaintext secret ever leaked, rotation is mandatory.

### Rotation (planned)

Checklist:
- [ ] Generate new key material (backend-specific)
- [ ] Update `.sops.yaml` recipients/rules (if used)
- [ ] Re-encrypt all secrets (SOPS updatekeys)
- [ ] Deploy updated secrets
- [ ] Deprecate old key (and confirm nothing still depends on it)
- [ ] Remove old key access and document the change (audit trail)

### Rotation (incident response)

If compromise suspected:
- [ ] Revoke credentials at the source system (DB, cloud IAM, API provider)
- [ ] Rotate secrets immediately
- [ ] Confirm new secrets deployed
- [ ] Purge leaked values from logs/artifacts
- [ ] Consider Git history remediation if plaintext was committed
- [ ] Record an incident note (governed)

---

## Guardrails (pre-commit + CI)

> [!NOTE]
> This section is a “build me” list if enforcement isn’t wired yet.

### Local guardrails

- Pre-commit scanning to detect accidental plaintext secrets
- Git ignore patterns for any temp plaintext files

### CI guardrails (merge-blocking)

Minimum gates:
- [ ] Secret scanning (fail build on high-confidence hits)
- [ ] Block any `kind: Secret` YAML outside `infra/secrets/sops/encrypted/**`
- [ ] Verify that committed secret files are SOPS-encrypted (presence of SOPS metadata)
- [ ] Restrict who can modify `.sops.yaml` + prod secrets (CODEOWNERS)

---

## Risks and tradeoffs

### Known risks with “encrypted secrets in Git”

- **Plaintext commit hazard**: the secret exists before encryption, so humans/automation can accidentally commit it.
- **Key distribution (“key 0”) problem**: you must securely distribute and rotate the decryption key across all places that need it.

### Alternative approach: store only secret *references* in Git

Instead of encrypted secrets, store pointers to an external secrets manager. Tradeoff: the secret lifecycle/versioning may live outside Git and can require separate operational ownership.

> [!TIP]
> It’s common to use SOPS for bootstrapping and a secrets manager for scale. Choose intentionally.

---

## Troubleshooting

### “SOPS can’t decrypt: no matching keys”
- Confirm your environment has access to the correct decryption key.
- Confirm you’re using the correct environment file (dev vs prod).
- Confirm `.sops.yaml` rules match the target path (if present).

### “Decrypted secrets appear in logs”
- Remove `set -x` in scripts.
- Never `echo` secret env vars.
- Ensure CI log masking is enabled (platform-specific).

### “I accidentally committed a plaintext secret”
1. Rotate/revoke the secret immediately.
2. Treat the repo history as compromised.
3. Apply history rewrite *only if required* (still rotate either way).
4. Add/strengthen scanners and gates so it can’t happen again.

---
