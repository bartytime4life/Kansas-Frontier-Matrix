# Kubernetes Troubleshooting Runbooks (KFM)

| Field | Value |
|---|---|
| Path | `docs/runbooks/troubleshooting/kubernetes/README.md` |
| Doc type | Troubleshooting index + playbook skeletons |
| Audience | On-call • Platform/SRE • Devs supporting workloads |
| Scope | Kubernetes (kubectl) + OpenShift (oc) |
| Status | Draft (governance-aligned) |
| Last reviewed | `TODO(YYYY-MM-DD)` |
| Owners | `TODO(team/email or CODEOWNERS ref)` |

> KFM runs **governed, evidence-first** workloads. Troubleshooting must preserve the “trust membrane” and produce **auditable**, **redacted**, **reproducible** evidence bundles.

---

## What “good” looks like

### ✅ Non-negotiables for KFM operations

- **Trust membrane stays intact**
  - External clients and UIs **never** access data stores directly.
  - Troubleshooting changes should not introduce bypass paths (e.g., exposing DBs via `NodePort` / public ingress).
- **Fail-closed**
  - If policy / auth / audit dependencies are unhealthy, the correct behavior is often “deny” vs “serve unsafe.”
- **Evidence-first**
  - Your incident notes should connect symptoms → commands → outputs → conclusion/hypothesis.
- **GitOps-first**
  - Prefer remediation via GitOps (PR) over imperative fixes. If you must patch live, record and backport.

> **Runbook format requirement (KFM):** write playbooks as “inputs → commands → interpretation → next step,” using stable Kubernetes primitives so they can be reliably followed and embedded/searchable.  
> (This README follows that pattern.)  

---

## Quick triage flow

```mermaid
flowchart TD
  A[Alert / Symptom] --> B[Confirm cluster + namespace + blast radius]
  B --> C{GitOps-managed?}
  C -->|Yes| D[Check controller sync + drift]
  C -->|No / Unsure| E[Workload-level inspection]
  D --> F[Pod / Service / Ingress / Storage checks]
  E --> F
  F --> G[Mitigate safely (least risky first)]
  G --> H[Capture evidence bundle + audit_ref(s)]
  H --> I[Backport fix to GitOps + follow-ups]
```

---

## Before you run commands

### Safety & governance guardrails

- **Do not paste unredacted logs/events** into public issues or chat rooms. Assume logs may include:
  - tokens, credentials, internal URLs, sensitive locations, or personally identifying fields.
- Prefer **read-only commands** first (`get`, `describe`, `logs`).
- If a mitigation involves data loss risk (e.g., deleting PVCs), stop and escalate.

### Context checklist (30 seconds)

- [ ] Correct Kubernetes context selected (cluster + user)
- [ ] Correct namespace selected
- [ ] You can explain current “blast radius” (single workload vs namespace vs cluster-wide)
- [ ] Identify “what changed” (PRs, image tag bump, config change, node pool update)

---

## “First 5 minutes” commands

> Use `kubectl` on Kubernetes. On OpenShift, most commands translate to `oc` directly.

```bash
# 1) What is failing?
kubectl get pods -A --sort-by=.status.phase
kubectl get events -A --sort-by=.metadata.creationTimestamp | tail -n 50

# 2) Narrow to a namespace/workload (fill these in)
NS="<namespace>"
APP_LABEL="app=<labelValue>"   # or use your org’s label conventions

kubectl get all -n "$NS" -l "$APP_LABEL" -o wide
kubectl get deploy,sts,ds,job,cronjob -n "$NS" -o wide

# 3) Deep dive a single pod
POD="<pod-name>"
kubectl describe pod -n "$NS" "$POD"
kubectl logs -n "$NS" "$POD" --all-containers=true --tail=200
kubectl logs -n "$NS" "$POD" --all-containers=true --previous --tail=200

# 4) If Pending or capacity issues
kubectl get nodes -o wide
kubectl top nodes 2>/dev/null || true
kubectl top pods -A 2>/dev/null || true
```

---

## Evidence bundle (attach to incident ticket)

### Minimal evidence bundle (recommended)

Create a timestamped folder and capture outputs **as files** (easier to redact and share safely):

```bash
TS="$(date +%Y%m%dT%H%M%S)"
OUT="evidence/$TS"
mkdir -p "$OUT"

kubectl version > "$OUT/kubectl-version.txt" 2>&1 || true
kubectl config current-context > "$OUT/context.txt" 2>&1 || true

# Cluster scope
kubectl get nodes -o wide > "$OUT/nodes.txt" 2>&1 || true
kubectl get pods -A -o wide > "$OUT/pods-all.txt" 2>&1 || true
kubectl get events -A --sort-by=.metadata.creationTimestamp > "$OUT/events-all.txt" 2>&1 || true

# Namespace scope (fill in NS)
NS="<namespace>"
kubectl get all -n "$NS" -o wide > "$OUT/all-$NS.txt" 2>&1 || true
kubectl get deploy,sts,ds,job,cronjob -n "$NS" -o wide > "$OUT/workloads-$NS.txt" 2>&1 || true
kubectl get cm,secret -n "$NS" > "$OUT/config-$NS.txt" 2>&1 || true   # list only; avoid dumping secret data
```

### Redaction rules (minimum)

- Remove/blur:
  - bearer tokens, cookies, API keys, passwords
  - full internal hostnames if sharing outside the org
  - precise sensitive site coordinates/locations if they may appear in logs
- When in doubt: **share counts + error codes + timestamps**, not full payloads.

---

## Symptom → runbook picker

| Symptom | Likely state | Start here |
|---|---|---|
| Pod `Pending` | scheduling/capacity/taints/PVC | **Runbook A** |
| `CrashLoopBackOff` / restarts | app crash, config, probes | **Runbook B** |
| `ImagePullBackOff` / `ErrImagePull` | registry/auth/tag | **Runbook C** |
| Service works inside cluster but not outside | ingress/route/LB/DNS | **Runbook D** |
| NetworkPolicy seems ignored | CNI or policy mismatch | **Runbook E** |
| Secret exposure / compliance concern | RBAC/encryption/audit | **Runbook F** |
| GitOps drift or stuck sync | controller health / repo | **Runbook G** |
| PVC stuck / attach errors | storage class/CSI/node | **Runbook H** |

---

## Runbook A — Pod won’t schedule (Pending)

<details>
<summary><strong>Inputs</strong></summary>

- Namespace (`NS`)
- Pod name (`POD`)
- Workload controller (Deployment/StatefulSet/Job)
- “What changed?” (new image, new requests/limits, node pool changes)
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
kubectl get pod -n "$NS" "$POD" -o wide
kubectl describe pod -n "$NS" "$POD" | sed -n '1,200p'
kubectl describe pod -n "$NS" "$POD" | sed -n '/Events:/,$p'

kubectl get nodes -o wide
kubectl describe node <node-name> | sed -n '/Taints:/,/Non-terminated Pods:/p'

# If PVC suspected
kubectl get pvc -n "$NS" -o wide
kubectl describe pvc -n "$NS" <pvc-name>
kubectl get pv -o wide
```

**OpenShift equivalents:** replace `kubectl` with `oc`.
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

Look in **Events** for:

- `Insufficient cpu` / `Insufficient memory` → requests too high or cluster at capacity
- `node(s) had taint` → missing toleration
- `node(s) didn't match node selector` / affinity rules too strict
- `persistentvolumeclaim ... is not bound` → storage provisioning/binding issue
</details>

<details>
<summary><strong>Next step</strong></summary>

- If capacity: scale node pool / autoscaler, or reduce requests (via GitOps).
- If taints/affinity: adjust tolerations/affinity (via GitOps).
- If PVC: fix StorageClass/CSI health, or correct PVC spec (via GitOps).
- If you must patch live: document exact patch and backport to GitOps immediately.
</details>

---

## Runbook B — CrashLoopBackOff / repeated restarts

<details>
<summary><strong>Inputs</strong></summary>

- Namespace (`NS`)
- Pod (`POD`) and container name (if multi-container)
- Approx start time of failures
- Recent deploy/config changes
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
kubectl get pod -n "$NS" "$POD" -o wide
kubectl describe pod -n "$NS" "$POD" | sed -n '/State:/,/Events:/p'

# Logs (current + previous)
kubectl logs -n "$NS" "$POD" --all-containers=true --tail=300
kubectl logs -n "$NS" "$POD" --all-containers=true --previous --tail=300

# If probes are failing
kubectl describe pod -n "$NS" "$POD" | sed -n '/Liveness:/,/Readiness:/p'

# Check config referenced by pod
kubectl get deploy -n "$NS" <deploy-name> -o yaml > /tmp/deploy.yaml
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

Common causes:

- **Bad config/env** (missing ConfigMap/Secret key, wrong URL, bad schema)
- **Probe mismatch** (health endpoint slow or wrong path/port)
- **OOMKilled** (memory limit too low; leaks; large workloads)
- **Dependency outage** (DB down, cache down, DNS issues)
</details>

<details>
<summary><strong>Next step</strong></summary>

- If config regression: rollback via GitOps (preferred), or revert last commit.
- If probes: adjust thresholds/path/initialDelay (GitOps).
- If OOM: confirm via `Last State`/events; raise limit or fix memory use; consider VPA/HPA only if configured.
- If dependency: jump to Service/DNS/Storage runbooks.
</details>

---

## Runbook C — ImagePullBackOff / ErrImagePull

<details>
<summary><strong>Inputs</strong></summary>

- Namespace (`NS`)
- Pod (`POD`)
- Image name + tag
- Registry used (internal vs external)
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
kubectl describe pod -n "$NS" "$POD" | sed -n '/Containers:/,/Events:/p'
kubectl describe pod -n "$NS" "$POD" | sed -n '/Events:/,$p'

# Verify serviceAccount and imagePullSecrets
kubectl get pod -n "$NS" "$POD" -o jsonpath='{.spec.serviceAccountName}{"\n"}'
kubectl get sa -n "$NS" <service-account> -o yaml | sed -n '/imagePullSecrets:/,/secrets:/p'
kubectl get secret -n "$NS" | grep -i pull || true
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

Events often tell you exactly what failed:

- `not found` → wrong tag or repo
- `unauthorized` → missing/invalid registry credentials
- `i/o timeout` / TLS errors → networking/DNS/cert issues to registry
</details>

<details>
<summary><strong>Next step</strong></summary>

- Fix tag/manifest in GitOps.
- Repair imagePullSecret / service account bindings (GitOps).
- If registry outage: confirm other workloads pulling from same registry.
</details>

---

## Runbook D — Service reachable in-cluster but not from the Internet

<details>
<summary><strong>Inputs</strong></summary>

- Namespace (`NS`)
- Service name
- Exposure mechanism: `Ingress` / Gateway / OpenShift `Route` / `LoadBalancer`
- Hostname + path expected
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
SVC="<service>"
kubectl get svc -n "$NS" "$SVC" -o wide
kubectl describe svc -n "$NS" "$SVC"

# Do endpoints exist?
kubectl get endpoints -n "$NS" "$SVC" -o wide
kubectl get ep -n "$NS" "$SVC" -o yaml

# Ingress
kubectl get ingress -n "$NS" -o wide
kubectl describe ingress -n "$NS" <ingress-name>

# OpenShift Route (if applicable)
oc get route -n "$NS" -o wide 2>/dev/null || true
oc describe route -n "$NS" <route-name> 2>/dev/null || true
```

**Safe testing (no new exposure):** use port-forward temporarily.

```bash
kubectl port-forward -n "$NS" svc/"$SVC" 8080:80
curl -v http://127.0.0.1:8080/healthz
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

- If **no endpoints**: selector mismatch or pods not Ready.
- If endpoints exist but ingress/route fails: controller misconfig, wrong class, TLS/cert issues, DNS.
- If external exposure is required: validate the intended component (Ingress controller / OpenShift router / cloud LB) is healthy.
</details>

<details>
<summary><strong>Next step</strong></summary>

- Fix selectors, readiness, ingress class, or route config via GitOps.
- Avoid exposing internal data stores via `NodePort`; prefer port-forward for debugging and admin access.
</details>

---

## Runbook E — NetworkPolicy doesn’t work (or seems ignored)

<details>
<summary><strong>Inputs</strong></summary>

- Namespace (`NS`)
- NetworkPolicy name
- Which traffic should be allowed/denied (src/dst, ports, protocols)
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
kubectl get networkpolicy -n "$NS"
kubectl describe networkpolicy -n "$NS" <policy-name>

# Identify pods + labels involved
kubectl get pod -n "$NS" --show-labels
kubectl get svc -n "$NS" -o wide
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

- NetworkPolicy behavior depends on a policy-enforcing CNI.
- Most issues are:
  - wrong podSelector/namespaceSelector labels
  - forgetting that policies are often “deny by default once any policy selects a pod”
  - protocol/port mismatch
</details>

<details>
<summary><strong>Next step</strong></summary>

- Correct selectors and policy spec via GitOps.
- If CNI/policy engine is suspect: escalate to platform/SRE.
</details>

---

## Runbook F — Secrets compromise / compliance audit (fast containment checklist)

<details>
<summary><strong>Inputs</strong></summary>

- Secret name(s) + namespace(s)
- Suspected exposure vector (logs, RBAC, CI artifacts, image layer)
- Time window
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
# Who can read secrets in this namespace?
kubectl auth can-i get secrets -n "$NS" --as=<user-or-sa>

# RBAC inventory (namespace)
kubectl get role,rolebinding -n "$NS"
kubectl describe rolebinding -n "$NS" <binding-name>

# (Cluster scope, if authorized)
kubectl get clusterrole,clusterrolebinding | head
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

- Determine blast radius: who/what can read secrets?
- Verify whether your cluster has “encryption at rest” configured for secrets (platform-run; don’t guess).
</details>

<details>
<summary><strong>Next step</strong></summary>

- Rotate credentials immediately (vault/provider + redeploy via GitOps).
- Reduce RBAC blast radius and implement least privilege.
- Preserve audit logs and evidence bundle (sanitized).
- Escalate as a security incident if exposure confirmed.
</details>

---

## Runbook G — GitOps not syncing / drift detected (Argo CD / Flux)

<details>
<summary><strong>Inputs</strong></summary>

- Which GitOps tool controls the workload (Argo CD vs Flux vs other)
- App name / Kustomization / HelmRelease
- Suspected drift source (manual apply, controller down, repo auth)
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
# Argo CD (if installed)
kubectl get applications.argoproj.io -A 2>/dev/null || true

# Flux (if installed)
kubectl get kustomizations -A 2>/dev/null || true
kubectl get helmreleases -A 2>/dev/null || true

# Controller health (namespaces vary; check typical ones)
kubectl get pods -A | egrep -i 'argocd|flux|gitops' || true
kubectl get events -A --sort-by=.metadata.creationTimestamp | tail -n 80
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

- If controller is unhealthy → desired state won’t reconcile.
- If controller is healthy but app is OutOfSync → inspect diffs, failed hooks, missing permissions, repo auth.
</details>

<details>
<summary><strong>Next step</strong></summary>

- Restore GitOps controller health first.
- Prefer PR-based fixes; avoid `kubectl apply` unless emergency.
- If emergency patch applied: capture exact patch + open PR to reconcile.
</details>

---

## Runbook H — PVC stuck Pending / volume attach/mount failures

<details>
<summary><strong>Inputs</strong></summary>

- Namespace (`NS`)
- PVC name
- StorageClass name (if any)
- Pod(s) mounting the PVC
</details>

<details>
<summary><strong>Commands</strong></summary>

```bash
kubectl get pvc -n "$NS" -o wide
kubectl describe pvc -n "$NS" <pvc-name>

kubectl get storageclass
kubectl describe storageclass <sc-name>

kubectl describe pod -n "$NS" <pod-name> | sed -n '/Volumes:/,/Events:/p'
kubectl describe pod -n "$NS" <pod-name> | sed -n '/Events:/,$p'
```
</details>

<details>
<summary><strong>Interpretation</strong></summary>

- If PVC Pending: dynamic provisioner/CSI may be down or misconfigured.
- If attach/mount errors: node permissions, storage backend, or CSI driver issues.
</details>

<details>
<summary><strong>Next step</strong></summary>

- Escalate CSI/storage backend failures to platform/SRE.
- Avoid deleting PVC/PV unless you have a verified restore path and approvals.
</details>

---

## OpenShift notes (if applicable)

- `oc` is largely compatible with `kubectl`.
- OpenShift adds Route-based exposure and additional security constraints.
- Prefer **port-forward** for debugging rather than exposing internal services.

---

## Post-incident checklist (definition of done)

- [ ] Service restored and stable (no repeated restarts; error budget impact assessed)
- [ ] Evidence bundle captured + redacted + attached to ticket
- [ ] Root cause identified or bounded hypothesis documented
- [ ] Fix backported to GitOps (PR merged) and drift resolved
- [ ] Follow-ups filed (tests, alerts, capacity, docs/runbook updates)
- [ ] If governance/policy implicated: capture `audit_ref`(s) and route to governance review

---

## Appendix

### `kubectl` ↔ `oc` quick map

| Concept | Kubernetes | OpenShift |
|---|---|---|
| List pods | `kubectl get pods -n NS` | `oc get pods -n NS` |
| Describe pod | `kubectl describe pod POD -n NS` | `oc describe pod POD -n NS` |
| Logs | `kubectl logs POD -n NS` | `oc logs POD -n NS` |
| Port-forward | `kubectl port-forward ...` | `oc port-forward ...` |
| Expose externally | `Ingress` / `Service LoadBalancer` | `Route` / `Ingress` |

### Common pod states & what they usually mean

| Status | Usually means | First check |
|---|---|---|
| `Pending` | scheduling/storage | Events + PVCs |
| `CrashLoopBackOff` | app crash/probes | logs (current + previous), probes, env |
| `ImagePullBackOff` | registry issues | Events + imagePullSecrets |
| `Running` but not Ready | readiness probe | probe config + dependency health |
| `OOMKilled` | memory limit exceeded | last state + requests/limits |

---
