# Releases

This directory is the canonical home for **packaged release artifacts** for the Kansas Frontier Matrix (KFM) repository.

KFM’s day-to-day “source of truth” remains the repository itself (data + metadata + provenance + code + governed docs). A **release** is an **immutable, versioned snapshot** of that state that is packaged for:

- distribution (offline / air-gapped use, mirroring, archiving),
- deployment (bootstrapping derivative stores like PostGIS/Neo4j from canonical repo outputs),
- citation (pinning research, reports, or downstream products to a specific version).

> **Important:** Official releases may include **signed artifacts** (e.g., SBOMs and provenance attestations). These are produced **at release time** (not on every PR).

---

## What belongs in `releases/`

A release directory typically contains:

- **Release manifest** describing the snapshot + listing all artifacts
- **Checksums** for every artifact in the release
- **SBOM(s)** for official releases (format is implementation-defined; keep it machine-readable)
- **Provenance attestation(s)** for official releases (format is implementation-defined; keep it machine-readable)
- **Bundle archives** (e.g., “repo snapshot”, “data bundle”, “graph export bundle”) and/or **pointers** to externally stored large artifacts, each with content hashes recorded in the manifest

---

## What must NOT be placed in `releases/`

- **Raw sources** or intermediate working files (those belong in canonical data staging locations, per the Master Guide)
- **Secrets** (API keys, tokens, passwords)
- Anything that violates KFM’s sovereignty/classification invariants (no “downgrading” restrictions between inputs and outputs)

---

## Directory layout

Each release is stored under a directory named for its git tag:

```text
releases/
  vX.Y.Z/
    manifest.json
    checksums.sha256
    sbom.*                (optional per policy; REQUIRED for official releases)
    provenance.*          (optional per policy; REQUIRED for official releases)
    bundles/
      <bundle files...>
    release-notes.md
```

**Conventions**
- Use **semantic version tags** like `v13.0.0`, `v13.1.0`, `v13.1.1`.
- Treat each `releases/<tag>/` directory as **immutable** once published.
  - If something must change, publish a **new patch release** rather than editing an existing release.

---

## Release identity and versioning rules

KFM is versioned at multiple layers; releases must respect each:

### 1) Repository release versioning (tags)
- Tags follow **semantic versioning**.
  - **Major** version: significant structural changes (breaking or coordinated changes).
  - **Minor** version: backwards-compatible feature additions.
  - **Patch** version: backwards-compatible fixes.

### 2) Dataset versioning (catalog + provenance)
When datasets are updated or reprocessed:
- New dataset versions should be **linked to prior versions** in DCAT/PROV.
- PROV should capture lineage and “how it was produced” (inputs, activities, agents, parameters), ideally including a run identifier and/or commit hash.

### 3) Graph & ontology versioning
- Graph schemas should remain backwards-compatible unless a deliberate migration is performed.
- Ontology changes require migration scripts and must be recorded in version history.

### 4) API versioning
- Breaking API changes require either a new versioned endpoint or a negotiated deprecation strategy.
- The OpenAPI/GraphQL schema is the contract; breaking it implies a version increment.

---

## Required “boundary artifacts” before data is considered publishable

For any dataset included in a release snapshot, KFM requires:
- STAC Collection and Item(s)
- DCAT Dataset entry
- PROV activity bundle

These “boundary artifacts” are the interface from data → graph → API → UI. If the dataset has no provenance record, that is a red flag.

---

## CI, security, and governance gates for release readiness

A release must be cut from a state that passes (or is explicitly waived under policy) KFM’s minimum quality and safety gates. This includes:

- API contract tests (OpenAPI / GraphQL lint + contract tests)
- Security & governance scans (examples include secret scanning, PII/sensitive content scans, sensitive location checks, and classification consistency checks)

### Governance review triggers (manual)
Certain changes should trigger a manual governance review before release, including:
- Introducing sensitive data / sovereignty-related layers
- New AI-driven narrative features that could be perceived as factual
- New external data sources (license/provenance/standards review)
- New public-facing outputs that might expose sensitive info
- Classification or sensitivity changes

Document outcomes in `docs/governance/REVIEW_GATES.md` (if present) or the canonical governance record.

---

## Release artifact checklist

### Minimum contents (REQUIRED for every release directory)
- [ ] `manifest.json` present
- [ ] `checksums.sha256` present (covers every bundle and every machine-readable artifact)
- [ ] `release-notes.md` present (see template below)

### Official-release additions (REQUIRED for official releases)
- [ ] SBOM present (e.g., `sbom.spdx.json` or equivalent)
- [ ] Provenance attestation present (e.g., `provenance.intoto.jsonl` or equivalent)
- [ ] Any signatures / verification material present (format/policy defined by maintainers)

### Data integrity / governance (REQUIRED when data is included)
- [ ] All included datasets have STAC + DCAT + PROV boundary artifacts
- [ ] Classification is not “downgraded” across processing/output boundaries
- [ ] Redaction/generalization applied across every layer where required (processed data, STAC/DCAT, API, UI)
- [ ] Governance review completed when triggers apply (and documented)

---

## Manifest format (recommended)

KFM does not mandate a single manifest schema here, but **the manifest must be machine-readable** and must allow a user to verify:

- which git tag + commit it corresponds to,
- what bundles exist,
- cryptographic hashes for each artifact,
- (if applicable) where external artifacts live and how to verify them.

Example `manifest.json` (illustrative):

```json
{
  "release_tag": "v13.0.0",
  "commit": "abc123def456...",
  "created_at": "2026-02-08T00:00:00Z",
  "artifacts": [
    {
      "path": "bundles/kfm-repo-snapshot-v13.0.0.tar.gz",
      "role": "repo_snapshot",
      "sha256": "<sha256-hex>",
      "notes": "Snapshot of code + docs + governed metadata for this tag."
    },
    {
      "path": "bundles/kfm-data-bundle-v13.0.0.tar.zst",
      "role": "data_bundle",
      "sha256": "<sha256-hex>",
      "notes": "Processed data + STAC/DCAT/PROV boundary artifacts."
    },
    {
      "path": "sbom.spdx.json",
      "role": "sbom",
      "sha256": "<sha256-hex>"
    },
    {
      "path": "provenance.intoto.jsonl",
      "role": "provenance_attestation",
      "sha256": "<sha256-hex>"
    }
  ]
}
```

---

## How to cut a release (maintainer procedure)

1. **Choose the version**
   - Determine whether the change is major/minor/patch.
   - Confirm graph/ontology/API changes comply with versioning expectations (migrations + versioned endpoints if needed).

2. **Confirm governance**
   - Check whether review triggers apply (sensitive data, classification changes, new public outputs, new external sources, AI narrative changes).
   - Ensure redaction and “no downgraded restrictions” invariants are upheld.

3. **Run/confirm CI gates**
   - Ensure contract tests, validators, and security/governance scans pass on the release commit.

4. **Build bundles**
   - Create the bundle(s) you intend to distribute.
   - Generate a `manifest.json`.
   - Generate checksums covering **every** artifact.
   - For official releases: generate SBOM + provenance attestations (and signatures if policy requires).

5. **Publish**
   - Create and push the git tag.
   - Attach artifacts to the release channel used by maintainers (e.g., GitHub Releases) and/or commit the `releases/<tag>/` folder, per repo policy.

6. **Post-release verification**
   - Validate checksums.
   - Validate manifests/SBOM/provenance files are parseable.
   - Perform a clean bootstrap from the bundle(s) and confirm derivative stores (e.g., PostGIS/Neo4j) can be regenerated from canonical outputs.

---

## How to verify a release (consumer procedure)

1. Verify you have:
   - `manifest.json`
   - `checksums.sha256`

2. Verify checksums (example):
```bash
sha256sum -c checksums.sha256
```

3. If present, verify signatures / provenance attestations according to project policy.

4. Confirm the tag + commit in `manifest.json` match the release you intended to consume.

---

## Release notes template (recommended)

Create `release-notes.md` with:

- Summary (what changed)
- Breaking changes (if any) + migration steps
- Data changes (new datasets, updated datasets, removals)
- Governance notes (any reviews performed; any sensitivity/classification notes)
- Verification notes (hashes, signatures, SBOM/provenance presence)

---

## Related canonical references

- Master Guide (system source of truth): `../docs/MASTER_GUIDE_v13.md`
- Standards (profiles, schemas): `../docs/standards/`
- Governance (review gates, sovereignty/ethics): `../docs/governance/`
- Data catalogs/provenance roots:
  - `../data/stac/`
  - `../data/catalog/dcat/`
  - `../data/prov/`

---

