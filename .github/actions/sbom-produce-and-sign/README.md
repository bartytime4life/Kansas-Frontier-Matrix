<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: SBOM Produce and Sign
type: standard
version: v1
status: draft
owners: NEEDS VERIFICATION
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: NEEDS VERIFICATION
related: [./action.yml, ../kfm__metadata__validate/, ../provenance-guard/, ../../workflows/kfm__policy_gates.yml]
tags: [kfm, github-actions, sbom, cosign, supply-chain]
notes: [Grounded in the attached March-April 2026 KFM reusable-action proposals; mounted repo verification of adjacent files is still needed.]
[/KFM_META_BLOCK_V2] -->

# SBOM Produce and Sign

Composite action README for generating an SBOM, signing it with Cosign, and running a local provenance-attestation step inside KFM policy-gated workflows.

> [!NOTE]
> **Status:** experimental  
> **Owners:** NEEDS VERIFICATION  
> ![Status: Experimental](https://img.shields.io/badge/status-experimental-orange) ![Type: Composite Action](https://img.shields.io/badge/type-composite%20action-blue) ![Supply Chain](https://img.shields.io/badge/focus-supply--chain-6f42c1) ![Repo Verification](https://img.shields.io/badge/repo%20verification-NEEDS%20VERIFICATION-yellow)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Current documented contract](#current-documented-contract) · [Definition of done](#task-list--definition-of-done) · [FAQ](#faq)  
> **Repo fit:** `.github/actions/sbom-produce-and-sign/` → documented upstream / adjacent paths: [`../kfm__metadata__validate/`](../kfm__metadata__validate/), [`../provenance-guard/`](../provenance-guard/), [`../../workflows/kfm__policy_gates.yml`](../../workflows/kfm__policy_gates.yml) · primary local contract: [`./action.yml`](./action.yml)

> [!IMPORTANT]
> This README is grounded in the **documented** `sbom-produce-and-sign` action contract carried in the March-April 2026 KFM reusable-action proposals. It is written for direct repo use, but mounted verification of `./action.yml`, sibling action directories, and the caller workflow is still **NEEDS VERIFICATION**.

> [!WARNING]
> The attached action snippet supports an explicit `cosign_key` path and a no-key path, but the exact **keyless / OIDC** behavior is not proven by the snippet alone. Confirm the mounted workflow, Cosign version, and runner identity setup before treating keyless signing as settled behavior.

## Scope

This directory owns the README for the `sbom-produce-and-sign` composite action.

Its job is narrow and specific:

- generate an SBOM from a caller-provided subject using **Syft**
- sign the generated SBOM with **Cosign**
- run a local **SLSA / provenance attestation** command against the SBOM
- act as one supply-chain proof step inside a broader KFM gate chain

This directory is **not** the owner of metadata schema validation, PROV bundle linkage checks, cross-repo policy orchestration, or artifact publication policy.

## Verification posture

Use these labels literally in this README when precision matters.

| Label | Meaning here |
| --- | --- |
| **CONFIRMED** | Directly supported by the attached action proposal snippets |
| **INFERRED** | Small structural completion added to make the README usable without overstating repo reality |
| **PROPOSED** | Recommended operator guidance or next step, not yet proven in mounted implementation |
| **UNKNOWN** | Not verified strongly enough in the current session |
| **NEEDS VERIFICATION** | Mounted repo file, workflow, output path, or runtime behavior should be checked before commit |

## Repo fit

| Path | Role | Relationship | Verification |
| --- | --- | --- | --- |
| `./README.md` | this file | operator-facing README for the composite action directory | **CONFIRMED** target path from task |
| `./action.yml` | composite action contract | primary executable surface this README is expected to describe | **NEEDS VERIFICATION** in mounted repo; contract is documented in attached proposals |
| [`../kfm__metadata__validate/`](../kfm__metadata__validate/) | sibling action | validates STAC / DCAT / PROV metadata and policy, not SBOM generation | **NEEDS VERIFICATION** |
| [`../provenance-guard/`](../provenance-guard/) | sibling action | checks that changed outputs have PROV bundles / run manifests | **NEEDS VERIFICATION** |
| [`../../workflows/kfm__policy_gates.yml`](../../workflows/kfm__policy_gates.yml) | documented caller workflow | composes metadata validation, provenance guard, and this action | **NEEDS VERIFICATION** |

## Accepted inputs

Use this action when the caller wants an SBOM for one concrete build subject and wants the result signed in the same workflow.

### Action inputs

| Input | Required | Accepted values | Notes |
| --- | --- | --- | --- |
| `subject` | yes | Artifact directory, dist folder, image reference, or other Syft-readable subject | Documented description says “Path to artifact dir (e.g., `dist/`, docker image ref, etc.)” |
| `format` | no | `spdx-json` or `cyclonedx-json` | Defaults to `spdx-json` |
| `cosign_key` | no | Base64-encoded Cosign key material | Used only when caller chooses an explicit key path |

### Runtime expectations

| Requirement | Why it matters |
| --- | --- |
| `pipx` available in the runner | The action uses `pipx run syft ...` |
| `cosign` available on `PATH` | The action calls `cosign sign-blob` and `cosign attest-blob` directly |
| Write access to the workspace | The action writes `sbom.json`, `sbom.sig`, `predicate.json`, and possibly a temporary `cosign.key` |
| Caller-controlled identity / secrets setup | Needed to make the no-key path reliable and reviewable |

## Exclusions

Do **not** use this action as the owner of any of the following:

| Out of scope here | Where it goes instead |
| --- | --- |
| STAC / DCAT / PROV schema validation | documented sibling action: [`../kfm__metadata__validate/`](../kfm__metadata__validate/) |
| PROV bundle presence and changed-artifact linkage | documented sibling action: [`../provenance-guard/`](../provenance-guard/) |
| full policy orchestration across reusable actions | documented caller workflow: [`../../workflows/kfm__policy_gates.yml`](../../workflows/kfm__policy_gates.yml) |
| vulnerability triage, package-policy decisions, or exception handling | caller workflow / security policy lane (**NEEDS VERIFICATION**) |
| artifact upload, registry attach, or release publication | publish / release workflow outside this directory (**NEEDS VERIFICATION**) |
| claims that keyless signing is fully wired, audited, and enforced | verify mounted workflow and runner identity setup first |

## Directory tree

```text
.github/actions/sbom-produce-and-sign/
├── README.md
└── action.yml                 # composite contract described in attached proposals; NEEDS VERIFICATION in mounted repo
```

## Quickstart

The clearest documented caller pattern is the reusable gate workflow that installs CLI dependencies first and then invokes this action.

```yaml
jobs:
  gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }

      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }

      - name: Setup CLI deps
        run: |
          pipx install jsonschema==4.23.0
          pipx install conftest
          curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
          curl -sSfL https://raw.githubusercontent.com/sigstore/cosign/main/install.sh | sh -s -- -b /usr/local/bin

      - name: SBOM + Sign
        uses: ./.github/actions/sbom-produce-and-sign
        with:
          subject: dist/
```

> [!TIP]
> Keep the first caller simple. Verify the default `spdx-json` path end-to-end before adding alternate formats, registry publishing, or stronger attestation policy.

## Usage

### What the documented action does

| Step | Documented command shape | Confirmed side effect | Trust note |
| --- | --- | --- | --- |
| Generate SBOM | `pipx run syft ${{ inputs.subject }} -o ${{ inputs.format }} > sbom.json` | writes `sbom.json` | Subject compatibility depends on Syft and caller environment |
| Export env hint | `echo "SBOM_PATH=sbom.json" >> $GITHUB_ENV` | sets `SBOM_PATH` for later steps | Only the env write is shown; downstream consumer use is outside this action |
| Sign | `cosign sign-blob ... --output-signature sbom.sig` | writes `sbom.sig` | If `cosign_key` exists, action decodes it first; otherwise it uses the no-key path |
| Prepare predicate | `echo '{}' > predicate.json` | writes `predicate.json` | Current predicate body is placeholder-grade |
| Attest | `cosign attest-blob --predicate predicate.json --type slsaprovenance --no-upload sbom.json` | runs a local attestation command | Post-command output capture or publication is not shown |

### Input interface

| Input | Default | Behavior |
| --- | --- | --- |
| `subject` | none | Required. Passed directly to Syft |
| `format` | `spdx-json` | Controls Syft output format |
| `cosign_key` | unset | When present, decoded from base64 to `cosign.key` and used with `--key` |

### Artifacts and side effects

| Artifact / side effect | Status | Notes |
| --- | --- | --- |
| `sbom.json` | **CONFIRMED** | Primary generated SBOM file |
| `sbom.sig` | **CONFIRMED** | Signature output from `cosign sign-blob` |
| `predicate.json` | **CONFIRMED** | Placeholder predicate created before attestation |
| `SBOM_PATH=sbom.json` in `$GITHUB_ENV` | **CONFIRMED** | Exposed for later workflow steps |
| `cosign.key` temp file when `cosign_key` is provided | **CONFIRMED** | Cleanup behavior is not shown |
| persisted attestation bundle file | **UNKNOWN** | Not shown in the documented action snippet |
| registry upload / attachment of SBOM or attestation | **UNKNOWN** | Not part of the documented action |

### Operator cautions

> [!IMPORTANT]
> This action is a **proof-producing** step, not a full promotion step. In the documented KFM composition, metadata validation and provenance guard happen in separate actions before or alongside this one.

> [!WARNING]
> The placeholder predicate body is currently `{}` in the documented contract. Treat any downstream claim about rich SLSA provenance content as **NEEDS VERIFICATION** until the mounted `action.yml` or caller workflow proves otherwise.

## Diagram

```mermaid
flowchart LR
    A[Caller workflow<br/>subject + format + optional cosign_key] --> B[Syft<br/>generate sbom.json]
    B --> C[Export SBOM_PATH<br/>to GITHUB_ENV]
    B --> D{cosign_key<br/>provided?}
    D -- yes --> E[Decode base64<br/>to cosign.key]
    E --> F[Cosign sign-blob<br/>write sbom.sig]
    D -- no --> F
    F --> G[Write predicate.json<br/>currently {}]
    G --> H[Cosign attest-blob<br/>type=slsaprovenance<br/>--no-upload]
    H --> I[Caller workflow decides<br/>store / publish / gate]
```

## Current documented contract

This README is based on a documented composite action contract, not on directly mounted repo verification.

| Surface | Status | Notes |
| --- | --- | --- |
| Action name `sbom-produce-and-sign` | **CONFIRMED** | Present in the attached proposal snippet |
| `runs.using: "composite"` | **CONFIRMED** | Present in the documented action |
| Inputs `subject`, `format`, `cosign_key` | **CONFIRMED** | Names, descriptions, and defaults shown |
| Syft command shape | **CONFIRMED** | `pipx run syft ... > sbom.json` |
| Signature command shape | **CONFIRMED** | `cosign sign-blob ... --output-signature sbom.sig` |
| Attestation command shape | **CONFIRMED** | `cosign attest-blob ... --type slsaprovenance --no-upload sbom.json` |
| Default no-key path is fully keyless / OIDC-backed | **NEEDS VERIFICATION** | Intent is implied; exact runner setup is not shown |
| Attestation artifact retention | **UNKNOWN** | No output capture or upload step shown |
| Mounted caller workflow path is live in repo | **NEEDS VERIFICATION** | Path is documented, not directly inspected |
| Mounted sibling action directories exist as linked | **NEEDS VERIFICATION** | Documented neighbors only |

## Task list / definition of done

- [ ] `./action.yml` is mounted and matches the documented interface in this README
- [ ] the caller workflow confirms how `cosign` is installed and how the no-key path is intended to authenticate
- [ ] the mounted repo documents where `sbom.json`, `sbom.sig`, and attestation outputs are retained or uploaded
- [ ] cleanup behavior for temporary key material is explicit if `cosign_key` is used
- [ ] relative links to sibling actions and `../../workflows/kfm__policy_gates.yml` resolve in the mounted repo
- [ ] any stronger claim about keyless signing, Rekor logging, or promotion consequences is source-grounded before merge
- [ ] README examples stay synchronized with the mounted `action.yml`

## FAQ

### Does this action install Syft and Cosign itself?

Not completely. The documented action invokes **Syft** via `pipx run`, but it still expects **Cosign** to be available as a direct CLI command. The documented caller workflow installs both before use.

### What happens when `cosign_key` is omitted?

The documented contract takes a no-key path and still runs `cosign sign-blob`. That suggests an ambient or keyless-friendly flow, but the exact authentication behavior is **NEEDS VERIFICATION** until the mounted workflow and runner setup are inspected.

### Does this action upload the SBOM or attestation anywhere?

No upload step is shown in the documented snippet. This README therefore treats publication, attachment, or registry storage as outside the scope of this action.

### Is this action enough to satisfy KFM policy gates by itself?

No. The documented composition puts this action beside metadata validation and provenance guarding. Treat it as one supply-chain proof step inside a larger fail-closed workflow.

## Appendix

<details>
<summary><strong>Documented <code>action.yml</code> snapshot</strong></summary>

```yaml
name: sbom-produce-and-sign

description: Generate SBOM and sign + attest with Cosign.

inputs:
  subject:
    description: Path to artifact dir (e.g., dist/, docker image ref, etc.)
    required: true

  format:
    description: spdx-json|cyclonedx-json
    default: spdx-json

  cosign_key:
    description: Base64-encoded Cosign key (if not using keyless)
    required: false

runs:
  using: "composite"
  steps:
    - name: Generate SBOM
      shell: bash
      run: |
        pipx run syft ${{ inputs.subject }} -o ${{ inputs.format }} > sbom.json
        echo "SBOM_PATH=sbom.json" >> $GITHUB_ENV

    - name: Sign (Cosign)
      shell: bash
      env:
        COSIGN_EXPERIMENTAL: "1"
      run: |
        if [ -n "${{ inputs.cosign_key }}" ]; then
          echo "${{ inputs.cosign_key }}" | base64 -d > cosign.key
          cosign sign-blob --key cosign.key sbom.json --output-signature sbom.sig
        else
          cosign sign-blob sbom.json --output-signature sbom.sig
        fi

    - name: SLSA/Provenance Attestation
      shell: bash
      run: |
        echo '{}' > predicate.json
        cosign attest-blob --predicate predicate.json --type slsaprovenance --no-upload sbom.json
```

</details>

<details>
<summary><strong>Documented caller workflow excerpt</strong></summary>

```yaml
name: kfm__policy_gates

on:
  workflow_call:
    inputs:
      metadata_globs:
        required: true
        type: string
      schema_dir:
        required: true
        type: string
      prov_dir:
        required: false
        type: string
        default: data/prov
      sbom_subject:
        required: false
        type: string
        default: dist/

jobs:
  gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }

      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }

      - name: Setup CLI deps
        run: |
          pipx install jsonschema==4.23.0
          pipx install conftest
          curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
          curl -sSfL https://raw.githubusercontent.com/sigstore/cosign/main/install.sh | sh -s -- -b /usr/local/bin

      - name: Metadata Validate
        uses: ./.github/actions/kfm__metadata__validate
        with:
          paths: ${{ inputs.metadata_globs }}
          schema_dir: ${{ inputs.schema_dir }}

      - name: Provenance Guard
        uses: ./.github/actions/provenance-guard
        with:
          prov_dir: ${{ inputs.prov_dir }}

      - name: SBOM + Sign
        if: ${{ inputs.sbom_subject != '' }}
        uses: ./.github/actions/sbom-produce-and-sign
        with:
          subject: ${{ inputs.sbom_subject }}
```

</details>

[Back to top](#sbom-produce-and-sign)
