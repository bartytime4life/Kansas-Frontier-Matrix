<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-needs-verification>
title: Evidence Integrity & Run Receipt Diagnostics
type: standard
version: v1
status: draft
owners: [@bartytime4life]
created: 2026-04-10
updated: 2026-04-10
policy_label: NEEDS_VERIFICATION
related: [data/receipts/README.md, tools/validators/README.md, tools/attest/README.md, contracts/README.md, schemas/README.md, policy/README.md]
tags: [kfm, evidence, receipts, integrity, diagnostics]
notes: [Target file path was not explicitly provided in the request; the uploaded draft was treated as the redesign baseline. Repo-relative paths and CLI surfaces remain NEEDS VERIFICATION unless verified against mounted repo evidence.]
[/KFM_META_BLOCK_V2] -->

# Evidence Integrity & Run Receipt Diagnostics

Diagnose and remediate broken `EvidenceRef`, `EvidenceBundle`, and run-receipt conditions before they leak into governed promotion or runtime evidence resolution.

![Status: experimental](https://img.shields.io/badge/status-experimental-F0AD4E)
![Evidence: corpus-grounded](https://img.shields.io/badge/evidence-corpus--grounded-2B6CB0)
![Repo path: needs verification](https://img.shields.io/badge/repo_path-needs--verification-9CA3AF)
![Review: required](https://img.shields.io/badge/review-required-D97706)

| Field | Value |
| --- | --- |
| **Status** | `experimental` |
| **Owners** | `@bartytime4life` |
| **Repo fit** | Path: `NEEDS VERIFICATION` |
| **Quick jump** | [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Diagnostic flow](#diagnostic-flow) · [Integrity checks](#integrity-checks) · [Remediation matrix](#remediation-matrix) · [Definition of done](#definition-of-done) · [FAQ](#faq) |

> [!IMPORTANT]
> This README is intentionally narrower than a release or promotion guide. It is for **pre-proof integrity** and **evidence-resolution readiness**. A passing run receipt can prove a concrete run occurred; it does **not** by itself replace release closure, policy decision objects, review state, or a full proof pack.

> [!NOTE]
> Example paths, filenames, and command surfaces below are written to be reviewable and adaptable. Treat them as `NEEDS VERIFICATION` unless they match mounted repo reality or emitted artifacts in the current session.

## Scope

This README covers the integrity layer where KFM moves from a reference like `EvidenceRef` to inspectable support objects that can survive review, correction, and runtime use.

It is concerned with four questions:

1. Did the referenced files actually exist?
2. Did the declared metadata still match those files?
3. Did the bundle close cleanly, or were there missing or stray objects?
4. Is the next action **repair**, **quarantine**, **re-run**, or **correction/rollback**?

### What this README is for

| Concern | Covered here? | Why |
| --- | ---: | --- |
| Broken `EvidenceRef` resolution | Yes | Broken refs undermine evidence inspection and runtime trust. |
| Broken `EvidenceBundle` closure | Yes | Missing members, malformed manifests, or orphan files weaken inspectability. |
| Run-receipt integrity | Yes | Run-level proof objects must remain auditable and reproducible. |
| Release-proof completeness | Partly | Only as an adjacent check when integrity issues affect already released surfaces. |

## Repo fit

**Path:** `NEEDS VERIFICATION`

The request did not name a target file path. The uploaded baseline suggests this is a README that belongs near receipts, validators, or evidence-resolution tooling.

**Likely upstream neighbors**  
`contracts/README.md` · `schemas/README.md` · `policy/README.md`

**Likely downstream or adjacent docs**  
`data/receipts/README.md` · `tools/validators/README.md` · `tools/attest/README.md`

**Operational role**  
This README should sit between contract/schema docs and release/promotion docs. It is the place where an operator or reviewer decides whether a receipt/bundle issue is a contained integrity defect or an event that must escalate into correction, rollback, or denial.

## Accepted inputs

| Input | What belongs here | Notes |
| --- | --- | --- |
| `receipt.json` or equivalent run receipt | Run-level emitted proof object for one acquisition/build/transform event | Exact schema fields remain project-specific. |
| `manifest.json` or equivalent bundle manifest | Declared bundle members and their integrity metadata | Must be compared against actual files, not trusted on sight. |
| Artifact files or immutable object refs | The bytes the receipt/manifest claims exist | Digest and size checks belong here. |
| Validation outputs | Prior check results, reason codes, quarantine flags | Useful for triage; not a substitute for re-checking bytes. |
| Run logs | Fetch/build timing, warnings, failure context | Secondary evidence only. |
| Release or correction refs | Only when an integrity issue may already affect public or steward-facing surfaces | Escalation context, not the primary object of this README. |

## Exclusions

| Excluded concern | Why it stays out of this README | Where it belongs instead |
| --- | --- | --- |
| Full attestation/signature verification | This README stops short of full release-proof assembly. | `tools/attest/` and release/promotion docs |
| Policy authoring and obligation design | Policy logic should be defined elsewhere, then consumed here. | `policy/` |
| Contract and schema design authority | This doc uses contracts; it does not define the schema registry. | `contracts/` and `schemas/` |
| Public-shell UX behavior | Evidence Drawer / Focus behavior depends on intact bundles, but UX doctrine belongs elsewhere. | UI / shell doctrine docs |
| Domain admission or rights adjudication | This doc can surface a problem, but it should not silently decide rights posture. | source-descriptor and policy review artifacts |

## Core terms and boundaries

| Term | Role in this README | Minimum expectation |
| --- | --- | --- |
| `EvidenceRef` | Stable resolver input | Identifies support indirectly; it is not the support itself. |
| `EvidenceBundle` | Governed support package | Should carry bundle identity, source basis, dataset refs, lineage summary, preview policy, transform receipts, rights/sensitivity state, and an audit reference. |
| Run receipt | Run-level proof object | Should make one concrete fetch/build/transform event accountable. It is stronger than a prose note, but weaker than full release closure on its own. |
| Release proof / release manifest | Promotion-facing proof object | Out of scope here except where integrity failures force escalation. |
| Correction / rollback | Visible lineage-preserving response | Required when already-released surfaces may have been affected. |

## Diagnostic flow

```mermaid
flowchart LR
    A[Claim / export / runtime answer] --> B[EvidenceRef[]]
    B --> C[Resolver]
    C --> D[EvidenceBundle]
    D --> E{Bundle + receipt integrity pass?}

    H[Run receipt / validation outputs] --> D
    I[Release / correction objects<br/>adjacent, out of scope] -. informs .-> E

    E -- Yes --> F[Runtime / review surface may proceed]
    E -- No --> G[Hold / quarantine / re-run / correction]
```

## Failure classes

| Class | Description | Default outcome |
| --- | --- | --- |
| Missing artifact | Referenced object is absent | `FAIL` |
| Hash mismatch | Declared digest differs from recomputed digest | `FAIL` |
| Size drift | Declared byte count differs from actual bytes | `FAIL` |
| Orphan ref | Ref does not resolve cleanly to bundle support | `REVIEW` |
| Orphan file | File exists but no declared bundle member points to it | `REVIEW` |
| Malformed manifest | JSON invalid, required fields absent, or object shape unusable | `FAIL` |
| Duplicate / divergent bundle | Repeated run or retry emitted conflicting outputs | `REVIEW` |
| Receipt / bundle disagreement | Receipt points to members the manifest does not declare, or vice versa | `FAIL` |
| Stale public linkage | Integrity issue may already touch a released surface | `ESCALATE` |

## Where to inspect

> [!WARNING]
> The layout below is **illustrative**. It came from the uploaded draft, not from a directly mounted repo tree.

<details>
<summary><strong>Illustrative path pattern</strong></summary>

```text
data/
  receipts/
    <pipeline_id>/
      <run_id>/
        receipt.json
        evidence/
          <bundle_id>/
            manifest.json
            artifacts...
        logs/
```

</details>

## Quickstart

This is a fast first pass for local triage. It is intentionally smaller than a full promotion gate.

```bash
# Illustrative bash. Verify RUN_ROOT before use.
RUN_ROOT="${RUN_ROOT:-data/receipts}"   # NEEDS VERIFICATION

find "$RUN_ROOT" -type f -name 'receipt.json' | while read -r receipt; do
  jq -e '.artifacts | type == "array"' "$receipt" >/dev/null || {
    echo "[BAD] missing artifacts[] :: $receipt"
    continue
  }

  run_dir="$(dirname "$receipt")"

  find "$run_dir" -type f -name 'manifest.json' | while read -r manifest; do
    jq -e '.artifacts | type == "array" and length > 0' "$manifest" >/dev/null \
      || echo "[BAD] malformed manifest :: $manifest"
  done
done
```

> [!IMPORTANT]
> Do **not** treat a quickstart pass as publishability proof. It only tells you whether you have enough integrity to continue into deeper validation.

## Usage

### 1. Freeze the inspection scope

Pick a recent run window first. For most triage passes, inspect the last `20–50` runs or the exact run IDs implicated by a failed review, export, or runtime answer.

### 2. Confirm the receipt object exists and parses

For each candidate run:

- locate exactly one canonical run receipt
- parse it successfully
- record whether the receipt shape is usable enough to inspect outputs

### 3. Confirm the bundle manifest exists and parses

Each bundle manifest should parse and should declare at least one artifact member. A manifest that parses but carries no usable members is still functionally broken.

### 4. Cross-link declared members

For every declared bundle member:

- verify the file or object ref exists
- verify the declared URI/path resolves to the intended member
- confirm receipt members and bundle members do not drift apart

### 5. Recompute a bounded digest sample

Prioritize:

- small to medium artifacts
- edge formats
- the object most likely to be cited or previewed
- any member that looks newly rebuilt, suspiciously tiny, or unexpectedly duplicated

### 6. Classify the failure

Choose one of:

- metadata-only defect
- missing-byte defect
- divergent retry / duplicate emission
- release-facing correction event

### 7. Take the smallest safe next action

Prefer the narrowest reversible move that preserves lineage and keeps failure visible.

## Integrity checks

| Check | What to compare | Pass rule | If it fails |
| --- | --- | --- | --- |
| Receipt parse | `receipt.json` vs expected object shape | JSON parses and receipt is inspectable | `FAIL` |
| Manifest parse | `manifest.json` vs expected object shape | JSON parses and manifest declares members | `FAIL` |
| Artifact presence | Declared URI/path vs actual file/object | Every declared member exists | `FAIL` |
| Digest integrity | Declared digest vs recomputed digest | All sampled members match | `FAIL` |
| Size integrity | Declared bytes vs actual bytes | All sampled members match | `FAIL` |
| Bundle closure | Receipt members vs manifest members | No declared member gap | `FAIL` |
| Orphan detection | Files vs declarations | Every extra file classified, not ignored | `REVIEW` |
| Retry divergence | Same logical run vs conflicting outputs | Deterministic or explicitly superseded | `REVIEW` |
| Release impact | Integrity issue vs current release scope | Either no release impact, or correction path opened | `ESCALATE` |

## Remediation matrix

| Condition | Primary action | Allowed follow-up | Avoid |
| --- | --- | --- | --- |
| Missing artifact or digest mismatch | Quarantine the run or candidate dataset | Gather evidence, compare upstream source-of-truth, re-run deterministically if needed | Regenerating the receipt over suspect bytes |
| Receipt metadata incomplete but bytes are verifiably correct | Regenerate or supersede the receipt through a governed workflow | Attach a new receipt, note correction/supersession, keep lineage visible | Hand-editing a published receipt in place |
| Duplicate or divergent bundle from retry | Hold and compare run inputs, timestamps, and deterministic inputs | Re-run the producing step or explicitly supersede one bundle | Choosing a winner by recency alone |
| Orphan file or orphan ref | Classify the gap first | Add missing declaration, retire stale member through correction path, or document intentional non-membership | Silent deletion |
| Already released surface may be affected | Escalate into correction / rollback review | Update correction note, stale-visible state, or rollback reference | Silent replacement of published objects |

## Doctrine alignment

| KFM principle | Why it changes this README |
| --- | --- |
| Inspectable claim | The goal is not merely “files exist.” It is that a consequential claim or surface can still route to inspectable support. |
| EvidenceRef → EvidenceBundle resolution | Evidence integrity is a resolver problem, not just a file-system problem. |
| Truth path as governed movement | Broken integrity should stop movement forward into governed publication. |
| Negative outcomes are first-class | `FAIL`, `HOLD`, `QUARANTINE`, `DENY`, and correction are valid outcomes, not embarrassing edge cases. |
| Run receipts are not full release closure | A run receipt can be valid and still be insufficient for public-safe release by itself. |
| Visible correction lineage | If a released surface is touched, fix it with visible supersession, narrowing, withdrawal, or replacement—never silent erasure. |

## Definition of done

A triage pass is complete when:

- [ ] the inspection window is explicitly named
- [ ] every targeted receipt parsed or failed with a recorded reason
- [ ] every targeted manifest parsed or failed with a recorded reason
- [ ] every declared member is either verified or explicitly classified
- [ ] sampled digest and size checks are recorded
- [ ] orphan files/refs are classified rather than ignored
- [ ] a next action is chosen for every failing run
- [ ] any release-facing impact is escalated into correction/rollback review
- [ ] the final note preserves lineage instead of smoothing uncertainty away

## FAQ

### Does a passing run receipt mean the release is safe to publish?

No. A run receipt can be a valid proof object for one concrete run, but promotion still depends on adjacent objects such as decision/policy outcomes, catalog closure, review state, and release-level proof.

### When should I **not** regenerate a receipt?

Do not regenerate when underlying bytes are suspect. First prove the artifacts are correct. Otherwise regeneration can overwrite the only visible trace of corruption with fresh-looking metadata.

### Are orphan files always bad?

Not automatically. They may be stale retries, retained diagnostics, or incomplete closure. What makes them risky is leaving them **unclassified**.

### Where do attestations fit?

Outside the narrow scope of this README. They belong in the adjacent attestation / promotion layer and should be checked there, especially once an integrity issue touches a release-bearing surface.

## Appendix

<details>
<summary><strong>Illustrative minimal object shapes</strong></summary>

### Minimal receipt-like shape

```json
{
  "run_id": "string",
  "pipeline_id": "string",
  "started_at": "timestamp",
  "finished_at": "timestamp",
  "artifacts": [
    {
      "uri": "string",
      "hash": "sha256:...",
      "size": 123
    }
  ]
}
```

### Minimal bundle-manifest shape

```json
{
  "bundle_id": "string",
  "artifacts": [
    {
      "uri": "string",
      "hash": "sha256:...",
      "size": 123
    }
  ]
}
```

### Closure rule

```text
receipt.artifacts[*].uri ∈ bundle.manifest.artifacts[*].uri
```

</details>

<details>
<summary><strong>Adjacent proof objects outside this README’s core scope</strong></summary>

| Object | Purpose | Why it matters here |
| --- | --- | --- |
| `SourceDescriptor` | Intake contract for a source or endpoint | Helps determine whether the broken object was fetched from the right origin at all |
| `IngestReceipt` | Fetch/landing proof object | Useful when the defect begins at source intake rather than bundle assembly |
| `ValidationReport` | Check pass/fail/quarantine record | Gives failure codes and severity context |
| `ReleaseManifest` / `ReleaseProofPack` | Public-safe release and proof assembly | Needed when an integrity issue may already affect a released surface |
| `CorrectionNotice` | Visible supersession / withdrawal / replacement | Prevents silent history erasure |

</details>

<details>
<summary><strong>Illustrative S3 adaptation</strong></summary>

```bash
# Illustrative only. Verify bucket layout and IAM behavior first.
runs=$(aws s3 ls "s3://$BUCKET/pipelines/$PIPELINE/runs/" --recursive \
  | sort -k1,2 \
  | tail -n 200 \
  | awk '{print $4}' \
  | cut -d/ -f1-5 \
  | uniq)

for r in $runs; do
  receipt="s3://$BUCKET/$r/receipt.json"

  if ! aws s3 ls "$receipt" >/dev/null 2>&1; then
    echo "[MISS] $r :: no receipt"
    continue
  fi

  for m in $(aws s3 ls "s3://$BUCKET/$r/evidence/" --recursive \
    | awk '{print $4}' \
    | grep 'manifest.json$'); do
    tmp=$(mktemp)
    aws s3 cp "s3://$BUCKET/$m" "$tmp" >/dev/null
    jq -e '.artifacts | type == "array" and length > 0' "$tmp" >/dev/null \
      || echo "[BAD] $r :: malformed manifest $m"
    rm -f "$tmp"
  done
done
```

</details>

[Back to top](#evidence-integrity--run-receipt-diagnostics)
