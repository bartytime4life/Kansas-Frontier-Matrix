# Sealed Secrets (Bitnami) — KFM Infra

![Kubernetes](https://img.shields.io/badge/Kubernetes-compatible-326CE5?logo=kubernetes&logoColor=white)
![GitOps](https://img.shields.io/badge/GitOps-friendly-success?logo=git)
![Secrets](https://img.shields.io/badge/Secrets-Sealed--Secrets-blue)
![Governed](https://img.shields.io/badge/KFM-governed-important)

> 🚫 **Hard rule:** Do **not** commit plaintext Kubernetes `kind: Secret` manifests to this repo.  
> ✅ Commit only:
> - `kind: SealedSecret` (ciphertext), **or**
> - secret *references* (e.g., External Secrets objects with no sensitive values)
>
> 🔎 CI is expected to enforce this (see **Governance gates**).

---

## What is this?

This folder documents how KFM stores **Kubernetes/OpenShift runtime secrets** in Git **safely** using **Bitnami Sealed Secrets**.

Sealed Secrets has two components:

- **Controller** (in-cluster): manages the sealing keypair and turns `SealedSecret` → `Secret`.
- **`kubeseal` CLI** (workstation/CI): encrypts a `Secret` into a `SealedSecret`.

Upstream docs: https://github.com/bitnami-labs/sealed-secrets

---

## KFM stance (policy)

KFM’s default posture is:

1. **Prefer external secret managers** (Vault / cloud secret managers) and keep only *references* in Git.
2. Use **Sealed Secrets** when we need Git-native delivery of secrets, especially:
   - bootstrap secrets for GitOps or secret-store access
   - small-scope runtime secrets in lower environments
   - environments where an external secret manager is not available yet

> ⚖️ **Governance note:** Storing encrypted secrets in Git is acceptable only when:
> - the secret values are never committed in plaintext
> - the blast radius is minimized (strict or namespace-wide scope)
> - key backup + rotation runbooks exist
> - repo access + reviews are enforced
>
> If in doubt: open a governance PR/issue and prefer External Secrets.

---

## Risks & tradeoffs (read before adopting)

Storing encrypted secrets in Git is practical, but not “free”:

- There’s a **human/process risk**: the plaintext secret must exist briefly to be sealed, which increases the risk it’s accidentally committed. [oai_citation:2‡Docker-GitOps-OpenShift.pdf](sediment://file_00000000004c71f8a55fb8ae2e980ace)
- There’s a **key-management (“key 0”) problem** at scale, and the sealing private key ultimately lives inside the cluster control plane storage (etcd), increasing attack surface. [oai_citation:3‡Docker-GitOps-OpenShift.pdf](sediment://file_00000000004c71f8a55fb8ae2e980ace)

> ✅ Mitigations:
> - enforce secret scanning + PR review
> - minimize scope (strict/namespace-wide)
> - back up sealing keys securely
> - rotate real secret values periodically

---

## Folder layout

```text
infra/
  secrets/
    sealed-secrets/
      README.md                 # you are here
      controller/               # (recommended) install manifests / Helm values / kustomize
      certs/                    # (optional) PUBLIC cert(s) for offline sealing (commit-safe)
      scripts/                  # (optional) helper scripts for fetch-cert / linting
      examples/                 # (optional) example SealedSecret manifests (NO real secrets)
```

> 🧩 **Where do SealedSecrets live?**  
> Prefer storing the resulting `SealedSecret` manifests *next to the workload that consumes them* (app overlays), not in this infra folder.

---

## How it works (GitOps flow)

```mermaid
flowchart LR
  Dev[Developer/CI] -->|create local Secret (dry-run)| S[Secret manifest (local only)]
  S -->|kubeseal| SS[SealedSecret manifest (ciphertext)]
  SS -->|commit + PR| Git[(Git repo)]
  Git -->|GitOps sync| Cluster[K8s / OpenShift]
  Cluster -->|Sealed Secrets controller| K8sSecret[Secret]
  K8sSecret -->|env/mount| Workload[Pods/Deployments]
```

---

## 1) Install the controller

> This is typically a **cluster admin / platform** responsibility.  
> Your GitOps controller must apply CRDs + controller **before** any `SealedSecret` resources are synced.

### Option A — Helm (official)

```bash
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm repo update
```

**Name/namespace defaults matter:**

- `kubeseal` defaults to controller name `sealed-secrets-controller` in namespace `kube-system`.
- The Helm chart may install the controller with name `sealed-secrets` unless overridden.

If you want `kubeseal` to work without extra flags, install like:

```bash
helm install sealed-secrets \
  -n kube-system \
  --set-string fullnameOverride=sealed-secrets-controller \
  sealed-secrets/sealed-secrets
```

### Option B — Manifest / Kustomize

Upstream provides a `controller.yaml` manifest. Use Kustomize when you need to change:

- namespace
- controller args (e.g., key renew period)
- RBAC or resource limits

See upstream releases for the manifest for your version:  
https://github.com/bitnami-labs/sealed-secrets/releases

---

## 2) Install `kubeseal` (client)

Install `kubeseal` from upstream release artifacts (or a trusted package manager).

Examples:

- macOS (Homebrew): `brew install kubeseal`
- source: `go install github.com/bitnami-labs/sealed-secrets/cmd/kubeseal@<tag>`

> 🧠 Tip: Keep `kubeseal` and controller reasonably in sync and read release notes for breaking changes.

---

## 3) Create a `SealedSecret` (developer workflow)

> On OpenShift you can use `oc` instead of `kubectl` (commands are equivalent for these resources).

### Step 0 — set controller location (if not `kube-system`)

If the controller is **not** in `kube-system`, tell `kubeseal` where it is:

```bash
# Option 1: per-command flag
kubeseal --controller-namespace sealed-secrets < mysecret.json > mysealedsecret.json

# Option 2: environment variable
export SEALED_SECRETS_CONTROLLER_NAMESPACE=sealed-secrets
kubeseal < mysecret.json > mysealedsecret.json
```

If the controller name differs from `sealed-secrets-controller`, pass:

```bash
kubeseal --controller-name sealed-secrets <args>
```

### Step 1 — create a local Secret manifest (DO NOT COMMIT)

Create a Secret manifest locally using `--dry-run=client`:

```bash
# Example: build a local Secret JSON (safe: local file only)
echo -n "<value>" | kubectl create secret generic mysecret \
  --dry-run=client \
  --from-file=foo=/dev/stdin \
  -o json > mysecret.json
```

> 🔐 Safer input options:
> - Prefer reading secret values from a secure file, stdin, or a password manager.
> - Avoid putting secret literals directly on the command line (shell history / process list risk).

### Step 2 — seal it

```bash
kubeseal -f mysecret.json -w mysealedsecret.json
```

At this point `mysealedsecret.json` (or YAML) is safe to commit.

### Step 3 — commit + let GitOps apply it

Place the resulting `SealedSecret` manifest next to the workload that consumes it (recommended):

- `apps/<service>/overlays/<env>/secrets/<name>.sealed.yaml` *(example; adjust to your repo layout)*

Commit via PR, get reviews, and let your GitOps controller sync.

---

## Offline sealing (CI without cluster access)

If CI cannot reach the cluster, you can store the **public** certificate in the repo and seal offline:

```bash
# Fetch the public certificate from the controller (commit-safe)
kubeseal --fetch-cert > certs/sealed-secrets-cert.pem

# Use it offline
kubeseal --cert certs/sealed-secrets-cert.pem -f mysecret.json -w mysealedsecret.json
```

> ✅ The certificate is public and safe to commit.  
> 🚫 Never commit private keys.

If you operate multiple clusters, store one cert per cluster/environment, and make it explicit which one to use.

---

## Scopes (blast-radius control)

By default, Sealed Secrets uses **strict** scope: sealed to both **namespace + name**.

| Scope | Bound to | How to set | When to use |
|---|---|---|---|
| `strict` (default) | namespace + name | (none) | ✅ Default; smallest blast radius |
| `namespace-wide` | namespace | `--scope namespace-wide` or annotation | When secret name may change inside same namespace |
| `cluster-wide` | cluster | `--scope cluster-wide` or annotation | Avoid unless absolutely required |

Raw-mode examples (single value):

```bash
# strict (default)
echo -n foo | kubeseal --raw --namespace bar --name mysecret

# namespace-wide
echo -n foo | kubeseal --raw --namespace bar --scope namespace-wide

# cluster-wide
echo -n foo | kubeseal --raw --scope cluster-wide
```

Annotations (on the SealedSecret) can also request a scope:

```yaml
metadata:
  annotations:
    sealedsecrets.bitnami.com/namespace-wide: "true"
    # or:
    sealedsecrets.bitnami.com/cluster-wide: "true"
```

---

## Validate, re-encrypt, rotate

### Validate a SealedSecret

```bash
cat mysealedsecret.yaml | kubeseal --validate
```

### Re-encrypt with the latest sealing key

Useful after key renewal:

```bash
kubeseal --re-encrypt < mysealedsecret.json > tmp.json && mv tmp.json mysealedsecret.json
```

### Key renewal & real secret rotation

- Sealing keys are renewed automatically (default every 30 days).
- **Key renewal is not a substitute** for rotating your actual secret values.

If a sealing key is suspected compromised, renew the key **before** you rotate and reseal actual secret values.

---

## Disaster recovery: backup & restore (HIGHLY SENSITIVE)

The controller’s private keys live in a Kubernetes `Secret`. If you lose them, you cannot decrypt past SealedSecrets.

### Backup keys

```bash
kubectl get secret -n kube-system \
  -l sealedsecrets.bitnami.com/sealed-secrets-key \
  -o yaml > main.key
```

> 🚨 `main.key` contains **private keys**. Treat it like a root credential:
> - **NEVER** commit to Git
> - store in an approved secret manager / encrypted offline vault
> - restrict access and audit retrieval
>
> After sealing key renewal, refresh the backup (or it won’t be able to decrypt newly sealed secrets).

### Restore keys

```bash
kubectl apply -f main.key
kubectl delete pod -n kube-system -l app.kubernetes.io/name=sealed-secrets
```

---

## Governance gates (expected)

### Required controls

- [ ] **Secret scanning** enabled (pre-commit + CI; e.g., gitleaks/trufflehog/GitHub secret scanning)
- [ ] CI rejects any committed plaintext `kind: Secret` outside approved exceptions
- [ ] PR review + CODEOWNERS for `infra/secrets/**`
- [ ] SealedSecret scope is `strict` unless documented otherwise
- [ ] Backup + restore procedure verified (tabletop at least once per environment)

### Suggested policy checks

<details>
<summary>Example: reject plaintext Secret manifests (pseudo-policy)</summary>

```text
Fail the build if:
- kind: Secret
- apiVersion: v1
...and file path is not in an explicit allowlist (e.g. test fixtures).
```

</details>

---

## Troubleshooting

### `kubeseal: error: ... cannot find sealed-secrets controller`

- Confirm controller is installed and healthy
- If not in `kube-system`, set `--controller-namespace` or `SEALED_SECRETS_CONTROLLER_NAMESPACE`
- If controller name differs, use `--controller-name`

### `kubeseal --validate` → `unable to decrypt sealed secret`

Common causes:

- wrong namespace/name or scope mismatch (strict binding)
- sealed with a cert from a different cluster/controller
- sealing key was lost/rotated without preserving old keys (restore backup)

---

## References

- Bitnami Sealed Secrets: https://github.com/bitnami-labs/sealed-secrets
- External Secrets (secret references): https://github.com/external-secrets/external-secrets
