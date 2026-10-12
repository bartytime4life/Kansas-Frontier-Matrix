<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sources/local-upload
title: Local upload: downloaded files and private captures
type: source-guide
version: v0.2
status: repository-integrated; private offline quarantine only
owners: ["@bartytime4life"]
created: 2026-09-17
updated: 2026-09-24
policy_label: public-documentation
owning_root: docs/
responsibility: Explain the local upload transport and quarantine boundary without treating capture as source admission.
truth_posture: CONFIRMED main@bb08d3e9b9 source and exact-schema policy decision; independent implementation and native-host acceptance need verification.
notes: ["Directory Rules ADR-0029 and owner decision #4613 apply only to private offline capture. No source admission, release, deployment, or publication authority."]
[/KFM_META_BLOCK_V2] -->

# Local upload: downloaded files and private captures

KFM can preserve explicitly selected local maps, images, documents, and archives
in a private QUARANTINE store using the
[local-PC data workflow](../../runbooks/local-pc-data-store.md).
The operator previews changes, verifies exact size and SHA-256, copies bounded
regular files, retains capture metadata and process receipts, and reuses verified
objects on later runs. It never extracts archives, fetches a remote URI, or
publishes a file.

The [owner decision #4613](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4613)
accepts the exact manifest schema and contract for private, offline,
operator-selected `QUARANTINE` capture. The [successor receipt](../../../data/receipts/generated/genrec-local-pc-data-policy-decision-20260917.json)
records that bounded decision while leaving independent implementation review,
native-PC acceptance, and all downstream source and public gates separate.

## Implementation and source identity

- Operator and storage inspection: [`tools/local_data/`](../../../tools/local_data/).
- Local capture helper: [`tools/local_data/file_io.py`](../../../tools/local_data/file_io.py).
- Input meaning: [`Local data manifest`](../../../contracts/source/local_data_manifest.md).
- Machine shape: [`local_data_manifest.schema.json`](../../../schemas/contracts/v1/source/local_data_manifest.schema.json).
- Canonical registered source identities: [`data/registry/sources/`](../../../data/registry/sources/).

The prior page claimed `data/registry/sources/local_upload.yaml` existed. No such
file exists at the reviewed base. A local upload is a transport path, not a
blanket authoritative source. Preserve each provider's identity and rights;
uploading a photograph or downloading a ZIP does not register or activate that
source. The colocated connector descriptor remains a historical, nonconforming
placeholder and is not consumed by the capture tool.

## Review boundary

All captures remain quarantined, including files whose manifest says `public`
or redistribution `allowed`. Unknown rights and sensitivity remain unknown.
The operator does not implement the connector admission gate. Source admission,
normalization, spatial/temporal validation, EvidenceBundle closure, policy,
release, and map delivery remain separate reviewed operations.

Follow [source admission guidance](../ADMISSION_PROCESS.md) and the accepted
[Directory Rules](../../doctrine/directory-rules.md). Bulk bytes and private
manifests belong on the operator's external disk, not in Git or the Site's
public assets. Synchronization preserves old captures; retention and legal-hold
decisions remain with the operator.
