# Promotion Gates Runbook

## Purpose

This runbook explains how to operate the governed promotion gates A→G for KFM release candidates.

The normative promotion contract lives at:

```text
docs/governance/gates/PROMOTION_CONTRACT.md
````

The machine-readable gate map lives at:

```text
control_plane/promotion_contract.json
```

or, if your repo is using YAML for governance registers:

```text
control_plane/policy_gate_register.yaml
```

This runbook is operational guidance. It does not replace the promotion contract, policy packs, schemas, validators, receipts, release manifests, or review decisions.

## Starter package contents

This starter provides the working pieces for governed promotion gates A→G:

* Rego policy packs under `policy/<gate>/main.rego`
* ADRs under `docs/adr/`
* the human-facing contract at `docs/governance/gates/PROMOTION_CONTRACT.md`
* the machine-readable contract at `control_plane/promotion_contract.json`
* validators under `tools/validators/`
* generated gate inputs under `.promotion/`
* a GitHub Actions starter workflow at `.github/workflows/promotion.yml`

## Gate execution model

The workflow does not run Conftest directly against the raw `artifacts/` directory.

Instead, it first creates a small gate input JSON file. This keeps `.txt` files, directories, parse errors, missing artifacts, policy denials, and integrity failures visible to policy and validators.

Example for Gate A:

```bash
python tools/validators/build_gate_input.py \
  --gate A \
  --contract control_plane/promotion_contract.json \
  --out .promotion/gate_A.json

conftest test .promotion/gate_A.json --policy policy/evidence
```

Every gate fails closed. Promotion stops on:

* missing required artifact
* malformed JSON artifact
* policy `deny`
* canonical `spec_hash` mismatch
* signature verification failure
* release manifest hash mismatch
* missing release approval
* missing attestation directory
* missing or invalid generated gate input

## Gate map

| Gate | Purpose                   | Policy pack          | Typical command                  |
| ---- | ------------------------- | -------------------- | -------------------------------- |
| A    | Evidence integrity        | `policy/evidence`    | `tools/validators/run_gate.sh A` |
| B    | Run provenance            | `policy/provenance`  | `tools/validators/run_gate.sh B` |
| C    | Rights and sensitivity    | `policy/rights`      | `tools/validators/run_gate.sh C` |
| D    | Obligations applied       | `policy/obligations` | `tools/validators/run_gate.sh D` |
| E    | Stewardship approvals     | `policy/approvals`   | `tools/validators/run_gate.sh E` |
| F    | Deploy preflight          | `policy/preflight`   | `tools/validators/run_gate.sh F` |
| G    | Final publish and archive | `policy/release`     | `tools/validators/run_gate.sh G` |

## Local usage

Install Conftest and any repo-required validator dependencies first.

Then run the gates locally:

```bash
tools/validators/run_gate.sh A
tools/validators/run_gate.sh B
tools/validators/run_gate.sh C
tools/validators/run_gate.sh D
tools/validators/run_gate.sh E
tools/validators/run_gate.sh F
tools/validators/run_gate.sh G
```

Gate A also runs canonical `spec_hash` validation.

Gate B verifies run provenance and the evidence Sigstore bundle.

Gate G verifies every `release_manifest.artifacts[].sha256` against the referenced local files and checks the release Sigstore bundle.

## Expected artifact paths

Promotion expects the release candidate to provide these artifacts:

```text
artifacts/EvidenceBundle.json
artifacts/spec_hash.txt
artifacts/run_receipt.json
artifacts/decision_log.json
artifacts/redaction_receipt.json
artifacts/preflight_report.json
artifacts/release_manifest.json
artifacts/signatures/evidence.sigstore.json
artifacts/signatures/release_manifest.sigstore.json
artifacts/attestations/
LICENSE
```

These paths are release-candidate artifact paths, not canonical source-of-truth paths.

The promotion contract defines which gates require which artifacts.

## Generated gate inputs

Generated gate inputs should be treated as disposable validator material.

Use:

```text
.promotion/
```

Example generated files:

```text
.promotion/gate_A.json
.promotion/gate_B.json
.promotion/gate_C.json
.promotion/gate_D.json
.promotion/gate_E.json
.promotion/gate_F.json
.promotion/gate_G.json
```

Recommended `.gitignore` entry:

```gitignore
.promotion/
```

Do not treat generated `.promotion/` files as release evidence unless a later ADR explicitly changes that rule.

## Sigstore and Cosign

This starter uses Sigstore bundle files for blob signatures.

Sign the evidence bundle:

```bash
cosign sign-blob artifacts/EvidenceBundle.json \
  --bundle artifacts/signatures/evidence.sigstore.json \
  --yes
```

Verify the evidence bundle:

```bash
cosign verify-blob artifacts/EvidenceBundle.json \
  --bundle artifacts/signatures/evidence.sigstore.json \
  --certificate-identity "$COSIGN_CERTIFICATE_IDENTITY" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
```

Sign the release manifest:

```bash
cosign sign-blob artifacts/release_manifest.json \
  --bundle artifacts/signatures/release_manifest.sigstore.json \
  --yes
```

Verify the release manifest:

```bash
cosign verify-blob artifacts/release_manifest.json \
  --bundle artifacts/signatures/release_manifest.sigstore.json \
  --certificate-identity "$COSIGN_CERTIFICATE_IDENTITY" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
```

## GitHub Actions identity

Set `COSIGN_CERTIFICATE_IDENTITY` as a repository variable before enabling the workflow.

A typical GitHub Actions keyless identity is:

```text
https://github.com/OWNER/REPO/.github/workflows/promotion.yml@refs/heads/main
```

Adjust this value when the signing workflow, branch, tag, or protected release policy differs.

Examples:

```text
https://github.com/OWNER/REPO/.github/workflows/promotion.yml@refs/heads/main
https://github.com/OWNER/REPO/.github/workflows/promotion.yml@refs/tags/v1.0.0
```

## GitHub Actions workflow

The starter workflow belongs at:

```text
.github/workflows/promotion.yml
```

The workflow should run the same gate commands used locally:

```bash
tools/validators/run_gate.sh A
tools/validators/run_gate.sh B
tools/validators/run_gate.sh C
tools/validators/run_gate.sh D
tools/validators/run_gate.sh E
tools/validators/run_gate.sh F
tools/validators/run_gate.sh G
```

The workflow should fail when any gate fails.

Do not allow publish/archive jobs to run unless Gate G succeeds.

## Contract and policy split

Use this split:

| Surface                     | Location                                      | Purpose                                                                            |
| --------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| Human promotion contract    | `docs/governance/gates/PROMOTION_CONTRACT.md` | Explains the binding promotion contract                                            |
| Operational runbook         | `docs/runbooks/promotion-gates.md`            | Explains how to operate gates locally and in CI                                    |
| Machine-readable gate map   | `control_plane/promotion_contract.json`       | Defines gates, required artifacts, policy packs, and integrity checks              |
| Policy packs                | `policy/<gate>/main.rego`                     | Decide allow/deny obligations for each gate                                        |
| Validators                  | `tools/validators/`                           | Build gate input, check hashes, verify signatures, and run gates                   |
| Workflow                    | `.github/workflows/promotion.yml`             | Runs gate commands in CI                                                           |
| Release candidate artifacts | `artifacts/`                                  | Holds candidate evidence, receipts, signatures, attestations, and release manifest |

## Customization checklist

The starter policies intentionally begin with minimum enforceable fields.

Tighten them before production release by adding:

* approved license identifiers
* source authority rules
* sensitivity labels
* rights-status rules
* CODEOWNERS or steward approval checks
* environment-specific preflight checks
* release artifact allowlists
* artifact size and type checks
* signature identity checks
* attestation requirements
* rollback target requirements
* correction path requirements
* public-safe geometry rules for sensitive domains
* domain-specific deny-by-default controls

## Safety notes

Do not promote a release candidate when rights, sensitivity, source authority, review state, or artifact integrity is unclear.

Do not treat generated text, model output, map tiles, search indexes, graph projections, or derived visualizations as root truth.

Do not publish from `RAW`, `WORK`, `QUARANTINE`, unpublished candidates, direct model output, or direct source-system side effects.

Promotion is a governed state transition, not a file move.

## Troubleshooting

### Gate input was not generated

Check that the contract path exists:

```bash
test -f control_plane/promotion_contract.json
```

Check that the gate exists in the contract:

```bash
python tools/validators/build_gate_input.py \
  --gate A \
  --contract control_plane/promotion_contract.json \
  --out .promotion/gate_A.json
```

### Conftest cannot parse an artifact

Raw artifact parsing should happen through `build_gate_input.py`, not by pointing Conftest directly at the full `artifacts/` directory.

Use:

```bash
conftest test .promotion/gate_A.json --policy policy/evidence
```

Do not use:

```bash
conftest test artifacts/ --policy policy/evidence
```

### Spec hash mismatch

Rebuild the candidate artifacts from the declared source inputs, then regenerate `artifacts/spec_hash.txt`.

Do not manually edit `spec_hash.txt` to force a pass.

### Signature verification failed

Check:

* the bundle file exists
* the signed blob has not changed
* `COSIGN_CERTIFICATE_IDENTITY` matches the workflow identity
* the OIDC issuer matches the signing environment
* the workflow branch or tag matches the expected identity

### Release manifest hash mismatch

Recalculate the SHA-256 for each referenced file and compare it to:

```text
release_manifest.artifacts[].sha256
```

Do not publish until the manifest matches the actual local artifact bytes.

## Definition of done

A promotion-gate starter is ready when:

* `docs/governance/gates/PROMOTION_CONTRACT.md` exists
* `docs/runbooks/promotion-gates.md` exists
* `control_plane/promotion_contract.json` exists
* all policy packs exist under `policy/`
* `tools/validators/build_gate_input.py` exists
* `tools/validators/run_gate.sh` exists
* `.github/workflows/promotion.yml` exists
* gate inputs are generated under `.promotion/`
* all gates fail closed on missing artifacts
* Gate A catches `spec_hash` mismatch
* Gate B catches missing or invalid evidence signature bundle
* Gate G catches release manifest hash mismatch
* CI blocks publish/archive when any gate fails
