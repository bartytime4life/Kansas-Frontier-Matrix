# Review and Stewardship Authority-Binding Source Map

**Status:** PROPOSED source adaptation; implementation evidence is the accompanying contract/schema/fixture/validator/test packet.

## Goal

Close the machine-checkable dependency between a declared review event and a declared stewardship assignment before attempting an authority-aware, no-write steward-apply preflight.

## Source-derived pressure

The KFM Pipeline Living Implementation Manual defines a controlled `query -> save -> validate -> compile -> review -> promote -> recompile` loop and requires auditable review, deterministic identity, finite outcomes, and rollback references. It also denies autonomous self-modification and direct loop output to `PUBLISHED`.

The KFM AI Build Operating Contract requires evidence over plausibility, Directory Rules placement checks, separation of generation from approval, bounded authority, deterministic validation, and no claim that generated artifacts authenticate human authority.

Directory Governance Standard v2 treats paths as authority claims and routes semantic contracts, machine schemas, fixtures, validators, tests, workflows, and receipts to separate responsibility roots.

Current repository evidence at implementation start showed:

- merged fixture-only `QueryRunRecord`;
- merged no-write `RecompileManifest`;
- merged fixture-only conditional-write preflight;
- semantic `ReviewRecord` and `StewardshipAssignment` contracts;
- permissive machine stubs for review and stewardship;
- no executable pair validator proving actor, role, subject, effective-window, disposition, and separation-of-duties agreement.

## Adaptation decision

Implement one inactive `ReviewAuthorityBinding` profile with closed, strict review, stewardship, and subject projections. The existing semantic contracts remain the meaning authority; this packet does not replace their standalone machine stubs or claim that referenced objects were independently resolved.

The binding returns `BOUND`, `HOLD`, or `DENY`, but creates no actor authentication or write authority. This is intentionally narrower than the originally proposed authority-aware apply preflight: the assay found that jumping directly to apply would rely on permissive authority stubs and overstate trust.

## Directory Rules basis

| Responsibility | Path family |
|---|---|
| semantic meaning | `contracts/governance/` |
| machine shape | `schemas/contracts/v1/governance/` |
| synthetic examples | `fixtures/contracts/v1/governance/` |
| deterministic validation | `tools/validators/governance/` |
| executable proof | `tests/validators/governance/` |
| CI orchestration | `.github/workflows/` |
| source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root or parallel policy, review, receipt, proof, release, or publication authority is created.

## Follow-up boundary

A later no-write steward-apply preflight should consume the `BOUND` report together with exact `RecompileManifest`, conditional-write preflight, independently resolved policy decision, current subject state, destination ownership, and future operational-receipt requirements. It must still stop before mutation.
