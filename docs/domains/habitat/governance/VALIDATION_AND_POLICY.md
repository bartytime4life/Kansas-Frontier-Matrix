<!-- [KFM_META_BLOCK_V2]
doc_id: TODO(kfm://doc/<uuid>)
title: Habitat Validation and Policy Gates
type: standard
version: v1
status: draft
owners: TODO(confirm habitat lane steward and policy owner)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(confirm public|restricted)
related: [docs/domains/habitat/README.md, policy/habitat/, tools/validators/habitat/]
tags: [kfm, habitat, validation, policy, fail-closed]
notes: [Validation and policy are described at a lane level; concrete tools and rule files require checkout verification.]
[/KFM_META_BLOCK_V2] -->

# Habitat Validation and Policy

## Validation posture
Habitat validation is fail-closed. Missing rights, unresolved sensitivity, invalid source role, or incomplete catalog closure blocks promotion.

## Required gate categories
| Gate | Purpose | Block condition |
|---|---|---|
| Schema gate | Ensure descriptors and payloads match contract shape. | Missing required fields or invalid type/value constraints. |
| Source-role gate | Prevent role mixing across regulatory/modeled/occurrence/context families. | Claim attempts unsupported role inference. |
| Rights gate | Enforce license and redistribution constraints. | Rights absent, ambiguous, or incompatible with public release. |
| Geoprivacy gate | Protect sensitive exact locations. | Public output contains exact restricted/sensitive geometry. |
| Catalog-closure gate | Require STAC/DCAT/PROV resolution. | Missing or misaligned catalog references. |
| Proof gate | Ensure EvidenceBundle/ReleaseManifest consistency. | Evidence or release references fail integrity checks. |

## Runtime outcomes
The governed runtime must return only finite outcomes:
- `ANSWER`
- `ABSTAIN`
- `DENY`
- `ERROR`

## Fixture expectations
At minimum, include fixtures for:
- valid regulatory critical habitat sample
- modeled habitat used correctly as context
- modeled habitat incorrectly used as legal designation (must fail)
- occurrence without rights (must quarantine/deny)
- sensitive exact occurrence request (must deny or abstain)
- missing PROV closure in release candidate (must fail)
