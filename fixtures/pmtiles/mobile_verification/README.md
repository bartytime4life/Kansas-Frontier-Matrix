# Synthetic mobile PMTiles verification fixtures

## Purpose

This lane is the fixture-first, no-network continuation of source idea
`ML-Y-111` from *Master MapLibre Components-Functions-Features*. It provides
one tiny synthetic PMTiles v3 archive packet and a compact mutation manifest
for mobile-emulated archive verification, PNG decode, and canvas rendering.

The fixture is planning-to-implementation input. It does not make the source
atlas, fixture bytes, validator, browser test, or a passing workflow into
evidence, policy, release, deployment, publication, or public-use authority.

## Directory Rules basis

Accepted ADR-0029 makes `docs/doctrine/directory-rules.md` the placement
authority. This fixture remains under the existing root-owned `fixtures/`
responsibility lane and the established `fixtures/pmtiles/` family. It creates
no schema, contract, policy, source, registry, proof, release, or publication
home.

## Packet

`cases.json` contains:

- a deterministic 347-byte synthetic PMTiles v3 archive encoded as base64;
- one PMIDX v1 sidecar with archive SHA-256, one Merkle leaf, one tile range,
  and the tile SHA-256;
- one PMSIG v1 subject whose signature is an explicit development placeholder;
- one PMTiles RunReceipt subject;
- canonical SHA-256 bindings for the three JSON sidecars;
- a 390 x 844, device-scale-factor 3, touch-capable mobile profile;
- archive, tile, verification, and decode/render budgets;
- one 1 x 1 PNG pixel with expected RGBA `[17, 34, 51, 255]`;
- eight finite positive and negative cases.

The archive bytes are synthetic and contain no Kansas source payload,
coordinate-sensitive record, person, species occurrence, infrastructure
location, credential, or external URL.

## Finite cases

| Case | Expected result |
|---|---|
| Valid verify/decode/render | `PASS / MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS` |
| Archive byte altered | `DENY / MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH` |
| PMIDX root altered | `DENY / MOBILE_PMTILES_MERKLE_ROOT_MISMATCH` |
| PMSIG subject altered | `DENY / MOBILE_PMTILES_SIGNATURE_SUBJECT_MISMATCH` |
| Tile range outside archive | `DENY / MOBILE_PMTILES_RANGE_OUT_OF_BOUNDS` |
| Tile digest altered | `DENY / MOBILE_PMTILES_TILE_DIGEST_MISMATCH` |
| MapLibre readiness overclaimed | `DENY / MOBILE_PMTILES_MAPLIBRE_AUTHORITY_OVERCLAIM` |
| Release authority overclaimed | `DENY / MOBILE_PMTILES_AUTHORITY_OVERCLAIM` |

## Explicit holds

A valid fixture still carries:

- `CRYPTOGRAPHIC_VERIFICATION_UNWIRED`;
- `MAPLIBRE_RUNTIME_UNADMITTED`;
- `RELEASE_AUTHORIZATION_NOT_EVALUATED`.

The browser test proves an injected PNG decode/render handoff. It does **not**
load or boot MapLibre because the current repository keeps the
`@kfm/maplibre` package and runtime dependency under an explicit readiness
hold. A future MapLibre-boot slice requires separately reviewed dependency,
adapter, protocol, browser-budget, and rollback evidence.

## Validation

```bash
python -m unittest -v   tests.validators.test_pmtiles_mobile_verification_fixture

python tools/validators/pmtiles/validate_mobile_verification_fixture.py   --fixtures

pnpm --filter explorer-web exec vitest run   tests/mobile-pmtiles-verification.test.ts

pnpm --filter explorer-web exec playwright test   --config=playwright.config.ts   tests/browser/mobile-pmtiles-verification.spec.ts
```

All checks are synthetic and no-network after dependency installation. A green
result is fixture integrity and browser-handoff evidence only.

## Rollback

Before merge, close the draft pull request and leave its branch unmerged. After
an authorized merge, revert the fixture, validator, tests, workflow, feature
module, documentation, and generated receipt together. No live source, cache,
release, deployment, or publication state exists to unwind.
