<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/redaction-determinism
title: Redaction Determinism — Seed, PRNG, and Reproducibility Rules
type: standard
version: v1
status: draft
owners: NEEDS VERIFICATION (proposed: Sensitivity & Geoprivacy stewards + Policy WG)
created: 2026-05-14
updated: 2026-05-14
policy_label: public
related:
  - docs/standards/SENSITIVITY_RUBRIC.md
  - docs/standards/CANONICALIZATION.md
  - docs/standards/RUN_RECEIPT.md
  - policy/redaction/profiles.yaml
  - contracts/runtime/redaction_receipt.md
  - schemas/contracts/v1/runtime/redaction_receipt.schema.json
tags: [kfm, geoprivacy, redaction, determinism, prng, jitter, receipts]
notes:
  - Operationalizes C6-03 (Seeded Reproducible Jitter) and pins the seed concatenation contract referenced by C6-02 named profiles.
  - Live repository not mounted at draft time; all path, validator, and profile-name claims are PROPOSED pending repo verification and ADR.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Redaction Determinism — Seed, PRNG, and Reproducibility Rules

> **PROPOSED standard.** Canonical, byte-level rules for deterministic display-redaction transforms (seeded jitter, hex/grid generalization with PRNG-driven tie-breakers) used by KFM redaction profiles. Operationalizes the doctrine in **C6-03 — Seeded, Reproducible Jitter** and binds every redaction profile to a verifier that can re-run the transform from a `RedactionReceipt` and confirm bit-identical output.

![status](https://img.shields.io/badge/status-draft-yellow)
![authority](https://img.shields.io/badge/authority-standard-blue)
![policy](https://img.shields.io/badge/policy_label-public-brightgreen)
![invariant](https://img.shields.io/badge/invariant-fail--closed-critical)
![spec](https://img.shields.io/badge/spec-v1_PROPOSED-lightgrey)
![reviewed](https://img.shields.io/badge/last_reviewed-2026--05--14-informational)

| Status | Owners | Policy label | Last updated |
|---|---|---|---|
| `draft` (v1, PROPOSED) | NEEDS VERIFICATION | `public` | 2026-05-14 |

---

## Quick jump

1. [Purpose & scope](#1-purpose--scope)
2. [Doctrinal anchor](#2-doctrinal-anchor)
3. [Vocabulary](#3-vocabulary)
4. [Core invariants](#4-core-invariants)
5. [Seed construction](#5-seed-construction)
6. [PRNG selection](#6-prng-selection)
7. [Distributions & geometry transforms](#7-distributions--geometry-transforms)
8. [Salting policy (open)](#8-salting-policy-open)
9. [`RedactionReceipt` contract](#9-redactionreceipt-contract)
10. [Verifier obligations](#10-verifier-obligations)
11. [Finite outcomes & failure modes](#11-finite-outcomes--failure-modes)
12. [Versioning & migration](#12-versioning--migration)
13. [Threat model & limitations](#13-threat-model--limitations)
14. [Test vectors](#14-test-vectors)
15. [Related docs](#15-related-docs)
16. [Appendix — reference algorithms](#16-appendix--reference-algorithms)

---

## 1. Purpose & scope

This document pins the **byte-level** rules that make KFM display-redaction reproducible across runs, machines, languages, and review cycles. It exists because two reviewers — and the CI verifier — must be able to take a published `RedactionReceipt` and reconstruct the **exact** redacted geometry that a public client saw. Without that property, redaction is neither auditable nor falsifiable.

In scope:

- Seed material composition for any redaction transform that draws pseudo-random values.
- PRNG algorithm choice and cross-language parity requirements.
- Geometry-side algorithms used by the canonical profiles (`point_10km_hex_seeded_v1`, `point_3km_jitter_v1`, `centroid_1km_v1`, `kfm:redact:none`).
- Verifier obligations and the finite outcomes a verifier may emit.
- Receipt-side fields needed to make a transform replayable.

Out of scope:

- The **policy** decision that selects a profile for a given record (lives in `policy/redaction/*.rego` and the sensitivity rubric).
- True differential privacy guarantees for **aggregates** (see C6-05; this document covers display jitter only).
- Encryption, signing, and transport (covered by run-receipt / DSSE / cosign standards).

> [!NOTE]
> This standard is **PROPOSED**. The C6-03 idea entry is CONFIRMED doctrine; the concrete byte-level rules below are this document's contribution. Anything labelled PROPOSED requires an accepted ADR before it can be cited as repo fact.

[Back to top](#top)

---

## 2. Doctrinal anchor

The doctrine this document operationalizes (CONFIRMED, from the Pass 10 Idea Index):

> **C6-03 — Seeded, Reproducible Jitter for Display Redaction.** Display-redaction jitter uses a PRNG seeded by `spec_hash` plus `occurrence_id` so the same record always receives the same offset; distributions can be uniform within a radius or Laplace. Determinism matters for two reasons: it lets reviewers reproduce the redacted geometry from the receipt, and it prevents temporal triangulation (multiple snapshots over time would otherwise reveal the true location).

Adjacent CONFIRMED doctrine this standard binds against:

| Doctrine | Carry-in obligation here |
|---|---|
| **C6-01 Sensitivity Rubric 0–5** | A profile is admissible only for the ranks listed in `policy/redaction/profiles.yaml`. |
| **C6-02 Named Redaction Profiles** | Each profile carries its method doc, Rego fixture, and a verifier — this standard defines what the verifier must check. |
| **C6-04 Grid Generalization** | Grid snapping is deterministic by construction; PRNG involvement is limited to documented tie-breakers. |
| **C6-05 DP for Aggregates Only** | Per-record jitter **is not** differential privacy, even when Laplace-shaped. This standard reinforces that boundary. |
| **C1-02 spec_hash via JCS + SHA-256** | Seed material consumes `spec_hash` only in its canonical `jcs:sha256:<hex>` form. |
| **Lifecycle law** | Redaction is a transform on the way to PUBLISHED; the receipt is the auditable artifact. |
| **Trust membrane** | Public clients consume the **redacted** carrier and the receipt — never the unredacted source. |

[Back to top](#top)

---

## 3. Vocabulary

| Term | Meaning in this document |
|---|---|
| **Profile** | A named, versioned redaction transform registered in `policy/redaction/profiles.yaml` (e.g. `point_3km_jitter_v1`). |
| **Seed material** | The deterministic byte string passed to a hash function to derive the PRNG seed. |
| **Seed digest** | `SHA-256(seed material)` — 32 bytes. |
| **PRNG** | A counter-mode stream cipher used as a pseudo-random byte generator. See §6. |
| **`occurrence_id`** | The stable identifier of the source record being redacted (e.g. a GBIF `occurrenceID`, a site identifier, a person identifier). |
| **`spec_hash`** | The canonical `jcs:sha256:<hex>` digest of the bundle/spec carrying the record (per C1-02). |
| **Salt** | Optional, profile-scoped value mixed into seed material. See §8 for the open salting decision. |
| **`RedactionReceipt`** | The receipt class that pins inputs, parameters, and outputs of a single redaction transform. See §9. |
| **Verifier** | A tool (proposed home: `tools/validators/redaction/`) that recomputes the transform from the receipt and compares against the published geometry. |

[Back to top](#top)

---

## 4. Core invariants

These are the non-negotiable rules every conforming profile must respect.

> [!IMPORTANT]
> **R1. Same inputs → same bytes.** For a given `(profile_id@version, spec_hash, occurrence_id, salt?)`, every conforming implementation MUST produce byte-identical output geometry. No locale, no wall-clock, no host entropy, no floating-point ambiguity may enter the transform.

> [!IMPORTANT]
> **R2. Receipt-replayable.** Given only the `RedactionReceipt` and access to the unredacted source record, a verifier MUST be able to recompute the output and confirm equality. If it cannot, the receipt is invalid.

> [!WARNING]
> **R3. Jitter is not privacy.** Seeded jitter obfuscates **display**; it does not provide a privacy guarantee. Ranks that require strong protection (rare species exact occurrences, archaeology coords, living-person identifiers, sacred sites) MUST use grid generalization, centroid replacement, or denial — not jitter alone. This restates C6-03 and the sensitivity register.

> [!CAUTION]
> **R4. Fail closed on uncertainty.** If a profile's PRNG, seed rule, or distribution cannot be deterministically resolved at runtime (missing parameter, unrecognized algorithm tag, locale-sensitive parsing detected), the runtime MUST emit `ERROR` and the policy gate MUST `DENY` publication. Never substitute a "reasonable default."

[Back to top](#top)

---

## 5. Seed construction

This section defines the **byte-level** rule the corpus calls for under C6-03's "seed concatenation rule" — PROPOSED in this document, pending ADR.

### 5.1 Seed material

The seed material is the UTF-8 byte string formed by concatenating the following fields, each separated by a single **`0x1F`** byte (ASCII Unit Separator), in this exact order:

```text
profile_id_at_version  ⟨0x1F⟩
spec_hash              ⟨0x1F⟩
occurrence_id          ⟨0x1F⟩
salt                   ← present only if salting is enabled for this profile
```

Field requirements:

| Field | Type | Form | Notes |
|---|---|---|---|
| `profile_id_at_version` | string | e.g. `point_3km_jitter_v1` | Must equal the catalog entry exactly; case-sensitive. |
| `spec_hash` | string | `jcs:sha256:<64 lowercase hex>` | Full prefixed form; never the bare hex. |
| `occurrence_id` | string | source-native, lowercased and NFC-normalized | See §5.2. |
| `salt` | hex string | 32 lowercase hex chars (16 random bytes) | Omitted entirely (no trailing separator) when salting is disabled. |

> [!NOTE]
> **Why `0x1F`?** It is reserved for record-internal separation in ASCII, cannot appear inside a hex digest, and is forbidden inside `occurrence_id` by §5.2 normalization. This eliminates the "is the separator inside the field?" ambiguity that would otherwise rotate seeds for benign string differences.

### 5.2 `occurrence_id` normalization

Before entering seed material, `occurrence_id`:

1. MUST be encoded as **UTF-8**.
2. MUST be Unicode-normalized to **NFC**.
3. MUST be **case-folded to lowercase** using the Unicode default casing (no locale-specific `tr` for Turkish dotted-I, etc.; profiles MUST pin `und` locale semantics).
4. MUST NOT contain `0x00`, `0x1F`, or `0x1E`. Records whose ID contains these bytes are quarantined with `ERROR.invalid_occurrence_id`.
5. MUST NOT be trimmed of leading/trailing whitespace silently — whitespace is significant and is folded only if the source authority documents it. Profiles MUST declare the trimming rule.

### 5.3 Seed digest

```text
seed_digest = SHA-256( seed_material )    // 32 bytes
```

The 32 bytes of `seed_digest` are the canonical PRNG key. Implementations MUST NOT truncate, re-hash, or post-process them before passing to the PRNG (with the single exception of split key/nonce as defined in §6).

```mermaid
flowchart LR
    A[profile_id@version] --> Z[Concat with 0x1F separator]
    B[spec_hash &#40jcs:sha256:hex&#41] --> Z
    C[occurrence_id &#40NFC, lowercased&#41] --> Z
    D[salt &#40hex, optional&#41] --> Z
    Z --> H["SHA-256<br/>(32 bytes)"]
    H --> K[PRNG key]
    K --> P["ChaCha20 keystream<br/>(deterministic bytes)"]
    P --> U[Uniform draws u1, u2, …]
    U --> G[Geometry transform]
    G --> R[(RedactionReceipt)]
    G --> O[Published geometry]
    R -. replay .-> P
```

[Back to top](#top)

---

## 6. PRNG selection

Cross-language byte parity is the binding constraint. Most language-stdlib PRNGs (Mersenne Twister, PCG, xoshiro variants) differ across platforms and versions; none is acceptable here.

### 6.1 Primary PRNG: ChaCha20 keystream

**PROPOSED v1 choice:** ChaCha20 in counter mode, used as a keystream generator.

- **Key:** first 32 bytes of `seed_digest` (i.e. all 32 bytes).
- **Nonce:** the constant 12-byte value `0x00 00 00 00 00 00 00 00 00 00 00 00`.
- **Counter:** starts at `0`, increments per 64-byte block.
- **Output:** raw keystream bytes consumed in stream order.

Rationale:

- Specified by **RFC 8439**; every conforming implementation produces byte-identical output for the same key/nonce/counter.
- Available with audited implementations in Python (`cryptography`), TypeScript/JS (`@noble/ciphers`), Go (`golang.org/x/crypto/chacha20`), and Rust (`chacha20`).
- No floating-point or platform-word dependence.
- Output is uniform over `{0, …, 255}` for each byte, so derivation of `u ∈ [0, 1)` is straightforward (§7.1).

### 6.2 Alternative: HMAC-DRBG (SHA-256)

Profiles MAY specify HMAC-DRBG (NIST SP 800-90A Rev. 1) instead of ChaCha20. The receipt's `prng_algorithm` field disambiguates. HMAC-DRBG is included for environments where ChaCha20 implementations are not available; it MUST NOT be mixed with ChaCha20 inside one profile.

### 6.3 Cross-language parity gate

> [!IMPORTANT]
> The CI suite MUST include a multi-language parity test that draws the first 64 bytes from a fixed `seed_digest` in Python, TypeScript, and Go, and asserts byte-equality. A failure is a release-blocking ERROR.

[Back to top](#top)

---

## 7. Distributions & geometry transforms

### 7.1 Deriving uniform draws from keystream bytes

A uniform `u ∈ [0, 1)` is derived as follows:

1. Read the next 8 bytes from the PRNG keystream.
2. Interpret as a big-endian unsigned 64-bit integer `n`.
3. Compute `u = n / 2^64` using **IEEE 754 binary64**.

Implementations MUST use this exact rule. They MUST NOT call language-provided `random()` helpers that wrap the keystream, because such helpers vary in their bit-extraction order.

### 7.2 Uniform-in-disc jitter

Used by profiles like `point_3km_jitter_v1`. Given radius `R` (meters):

```text
u1 = next_uniform()
u2 = next_uniform()
theta = 2π · u1
r     = R · sqrt(u2)
dx    = r · cos(theta)
dy    = r · sin(theta)
```

- `dx, dy` are added to the source point in a **local equal-area projection** centered on the source point (PROPOSED: an azimuthal-equidistant projection pinned per profile to ensure `R` is measured in meters, not degrees).
- The result is reprojected to the published CRS.
- All trigonometric calls MUST use IEEE 754 binary64. Profiles MUST NOT use `long double`, `binary128`, or hardware-accelerated paths that diverge from the IEEE 754 baseline.

### 7.3 Laplace jitter (per-axis)

Used when the profile specifies `distribution: laplace`. Given scale `b` (meters):

```text
u   = next_uniform()
shifted = u − 0.5             // ∈ [−0.5, 0.5)
sign    = +1 if shifted ≥ 0 else −1
mag     = sign · b · ln(1 − 2·|shifted|)    // inverse CDF
```

Apply per axis (draw `u` separately for `x` and `y`). Clamp `mag` to `±5·b` to prevent pathological tails.

> [!WARNING]
> Laplace-shaped jitter is **not** differential privacy. It does not provide an ε guarantee against an adversary with auxiliary information. Profiles that need DP must operate on aggregates (C6-05), not per-record points.

### 7.4 Grid and hex generalization

Per C6-04, snap-to-grid is deterministic by construction (PostGIS `ST_SnapToGrid` or H3 indexing). The PRNG is only invoked for documented **tie-breakers** (e.g., a record sitting exactly on a cell boundary). When invoked, the tie-breaker MUST consume one uniform draw and be documented in the profile.

### 7.5 Centroid replacement

Per the canonical `centroid_1km_v1` style profiles, the point is replaced by the centroid of its enclosing administrative or grid unit. No PRNG is invoked. The receipt records the unit identifier; verifier confirms the centroid by recomputation from the named unit.

[Back to top](#top)

---

## 8. Salting policy (open)

C6-03's open question — *"Should seeds be salted with a server-side secret to prevent third-party reproduction of jittered points?"* — is unresolved in the corpus. This section presents the trade-off; the final decision is **NEEDS VERIFICATION** and belongs in an ADR.

| Option | What it buys | What it costs |
|---|---|---|
| **A. No salt (open determinism)** | Any third party with the receipt and source can recompute the redacted geometry; trivially auditable; no key management. | An attacker with the source record can reproduce KFM's jitter and confirm whether a published point matches a guessed source — only meaningful when the attacker already has the source, but worth noting. |
| **B. Per-profile public salt** | Pins the seed across releases without secrecy; rotates with profile version. | Provides no protection against an attacker with the receipt + salt. Mostly cosmetic. |
| **C. Server-side secret salt** | Third parties cannot reproduce the redacted geometry without the secret; verifier runs only inside KFM. | Reproduction becomes an internal-only operation; reviewers outside the trust boundary lose offline replay. Key management becomes a publication dependency. |

> [!NOTE]
> **PROPOSED default for v1:** Option A (no salt). Rationale: KFM's primary defense against re-identification is **rank-appropriate transform choice** (grid generalization, centroid replacement, denial), not seed secrecy. Open auditability is the larger prize. Profiles MAY opt into Option C via the receipt field `salt_class: "server_secret"`, but that opt-in suspends offline reproducibility and MUST be flagged in the receipt.

Track this decision in `docs/registers/VERIFICATION_BACKLOG.md` and open an ADR before any rank-4 or rank-5 profile is shipped.

[Back to top](#top)

---

## 9. `RedactionReceipt` contract

This standard pins the **redaction-specific** fields a receipt must carry to be replayable. It defers to the master receipt catalog and `contracts/runtime/redaction_receipt.md` for the full shape.

```json
{
  "object_type": "RedactionReceipt",
  "schema_version": "v1",
  "receipt_id": "rr-…",
  "profile_id": "point_3km_jitter_v1",
  "profile_version": "v1",
  "spec_hash": "jcs:sha256:…",
  "occurrence_id_norm": "abc-123",
  "salt_class": "none | profile_public | server_secret",
  "salt_ref": "kfm://salts/…  (only if salt_class != none)",
  "prng_algorithm": "chacha20" ,
  "prng_nonce_hex": "000000000000000000000000",
  "seed_digest_sha256": "…",
  "distribution": "uniform_in_disc | laplace_per_axis | grid | centroid | none",
  "parameters": { "radius_m": 3000 },
  "projection": "azimuthal-equidistant-local",
  "input_geom_hash": "…",
  "output_geom_hash": "…",
  "policy_ref": "policy/redaction/profiles.yaml#point_3km_jitter_v1",
  "reviewer": "NEEDS VERIFICATION (steward role)",
  "time": "2026-05-14T00:00:00Z"
}
```

Required fields (PROPOSED v1):

| Field | Purpose |
|---|---|
| `profile_id` + `profile_version` | Disambiguate the profile and pin its version. |
| `spec_hash` | Anchor to the source bundle (C1-02 form). |
| `occurrence_id_norm` | The post-§5.2 normalized form — what actually entered the seed. |
| `salt_class` (+ `salt_ref`) | Replayability mode. |
| `prng_algorithm` | `chacha20` or `hmac_drbg_sha256`. |
| `seed_digest_sha256` | The 32-byte digest, hex-encoded. Lets a verifier check seed construction without re-running normalization. |
| `distribution` + `parameters` | What was drawn and with what scale. |
| `input_geom_hash` / `output_geom_hash` | SHA-256 over canonical WKB; lets the verifier compare without WKT whitespace noise. |
| `policy_ref` | The policy rule that selected this profile. |

> [!NOTE]
> `seed_digest_sha256` is **derived** from the other inputs and is redundant in a strict sense, but it accelerates verification and lets reviewers detect normalization drift without sharing the raw `occurrence_id`.

[Back to top](#top)

---

## 10. Verifier obligations

A conforming verifier (PROPOSED home: `tools/validators/redaction/replay_verify.py`) MUST:

1. **Re-normalize** `occurrence_id` per §5.2 and compare against `occurrence_id_norm`.
2. **Reconstruct** seed material per §5.1 and recompute `SHA-256`.
3. **Compare** the recomputed digest with `seed_digest_sha256`.
4. **Re-instantiate** the PRNG named by `prng_algorithm` per §6.
5. **Replay** the distribution per §7 with `parameters`.
6. **Hash** the recomputed output geometry (canonical WKB → SHA-256) and compare with `output_geom_hash`.
7. **Emit** a `ValidationReport` with one of the finite outcomes in §11.

Verifiers MUST run with **no network access**. All inputs are local files plus the original source record. Network calls are a hard failure.

[Back to top](#top)

---

## 11. Finite outcomes & failure modes

Verification outcomes align with the KFM finite-outcome contract (`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`).

| Outcome | When | Downstream effect |
|---|---|---|
| `ANSWER` | All seven verifier checks pass; output geom hash matches. | Receipt is **admissible** for publication. |
| `ABSTAIN` | Missing input (e.g., source record not available offline). | Re-queue or escalate; publication blocked until resolved. |
| `DENY` | A check fails: seed digest mismatch, geom hash mismatch, unknown profile, profile-version mismatch, unsupported PRNG, parameter out of range. | Publication is blocked; record is quarantined; review required. |
| `ERROR` | Verifier itself failed: malformed receipt, IO error, missing PRNG implementation, locale-sensitive parsing detected, network attempted. | Quarantine; fail closed; verifier bug or environment defect. |

> [!CAUTION]
> A `DENY` from the redaction verifier is **not** discretionary. Promotion gates MUST honor it without manual override. Override paths require a tombstone (C5-09) plus a steward-approved correction notice.

[Back to top](#top)

---

## 12. Versioning & migration

Per C6-02, **profile changes are breaking changes** for any record produced under the old version. This standard formalizes the rule:

- Profile names carry a `@vN` suffix. `point_3km_jitter_v1` and `point_3km_jitter_v2` are **different profiles** and produce different seeds and different geometry, even with identical parameters.
- A change to **any** of `{seed construction (§5), PRNG (§6), distribution algorithm (§7)}` requires a major version bump and an ADR.
- A change to **profile parameters** (radius, scale, grid cell size) also requires a major version bump, because the seed material includes `profile_id_at_version`.
- Documentation-only changes (typos, clarification) MAY keep the version. The receipt's `profile_version` field is the source of truth.

> [!NOTE]
> Migration when a profile rotates: every existing `RedactionReceipt` referencing the old version remains valid for its publication window; the new version regenerates output for records re-promoted after the cutover. Old and new outputs are not expected to match — they are different transforms.

[Back to top](#top)

---

## 13. Threat model & limitations

This standard does **not** claim to defend against:

- **Re-identification by an adversary with the source dataset.** If an attacker already has the unredacted record, seeded jitter is reproducible by definition (Option A, §8). Defense in depth requires rank-appropriate transform choice and access controls.
- **Cross-source linkage.** A record may be jittered consistently in KFM but appear unjittered in another publication; the union exposes the source. KFM cannot enforce upstream behavior.
- **Side-channel disclosure via the receipt itself.** Receipts publish `occurrence_id_norm` (or its hash) and `seed_digest_sha256`. Profiles dealing with rank-4 or rank-5 ranks MUST hash `occurrence_id_norm` before persistence (PROPOSED: `sha256(salt_class || occurrence_id_norm)` exposed instead).
- **Floating-point drift at the geographic projection stage.** The projection step (§7.2) involves trigonometry; bit-exact reproducibility across IEEE 754 implementations is the assumption, not a proof. Test vectors (§14) are how this is enforced.
- **Privacy in any formal sense.** Per C6-05 and C6-03, jitter is for display obfuscation only. It is not differential privacy and must not be presented as such in policy, UI, or AI explanations.

[Back to top](#top)

---

## 14. Test vectors

PROPOSED CI gate: `tools/validators/redaction/test_vectors.py` (NEEDS VERIFICATION).

Each profile MUST ship at least:

| Vector | Purpose |
|---|---|
| `vec_uniform_disc_001` | Known `(profile, spec_hash, occurrence_id)` → known `(dx, dy)` to ≤ 1 mm. |
| `vec_laplace_001` | Same, for Laplace per-axis. |
| `vec_cross_language` | Same vector executed in Python, TypeScript, Go → byte-identical. |
| `vec_normalize_001` | NFC + lowercasing applied to a non-ASCII `occurrence_id`; expected `occurrence_id_norm` known. |
| `vec_bad_separator` | `occurrence_id` containing `0x1F` → ERROR. |
| `vec_unknown_prng` | Receipt declaring `prng_algorithm: pcg64` → DENY. |
| `vec_geom_drift` | Same inputs, tampered output → DENY with `geom_hash_mismatch`. |

> [!NOTE]
> Vector files are PROPOSED to live under `policy/redaction/fixtures/vectors/` so they sit alongside the Rego fixtures called for in C6-02.

[Back to top](#top)

---

## 15. Related docs

- [`docs/standards/SENSITIVITY_RUBRIC.md`](./SENSITIVITY_RUBRIC.md) — the rank-to-obligation mapping that selects which profile applies. *(PROPOSED — not yet authored at draft time.)*
- [`docs/standards/CANONICALIZATION.md`](./CANONICALIZATION.md) — JCS vs URDNA2015 decision matrix, source of the `spec_hash` form consumed in §5.1. *(PROPOSED.)*
- [`docs/standards/RUN_RECEIPT.md`](./RUN_RECEIPT.md) — receipt envelope that wraps `RedactionReceipt` for promotion. *(PROPOSED.)*
- [`docs/registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) — tracks the open salting decision and any per-profile open items.
- [`policy/redaction/profiles.yaml`](../../policy/redaction/profiles.yaml) — the profile catalog. *(PROPOSED path.)*
- [`contracts/runtime/redaction_receipt.md`](../../contracts/runtime/redaction_receipt.md) — `RedactionReceipt` semantic contract. *(PROPOSED path.)*
- [`schemas/contracts/v1/runtime/redaction_receipt.schema.json`](../../schemas/contracts/v1/runtime/redaction_receipt.schema.json) — machine schema (per ADR-0001). *(PROPOSED path.)*

[Back to top](#top)

---

## 16. Appendix — reference algorithms

<details>
<summary><b>A.1 — Python reference (illustrative, not the canonical implementation)</b></summary>

```python
"""
Illustrative reference for KFM RedactionDeterminism v1.
NOT the canonical implementation. Provided for reviewer
intuition and cross-language parity discussions only.
"""
import hashlib, math, struct, unicodedata
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

US = b"\x1f"  # unit separator

def normalize_occurrence_id(s: str) -> str:
    s = unicodedata.normalize("NFC", s).casefold()
    for bad in ("\x00", "\x1f", "\x1e"):
        if bad in s:
            raise ValueError("invalid_occurrence_id")
    return s

def build_seed_material(profile_id_at_version, spec_hash,
                        occurrence_id_norm, salt_hex=None):
    parts = [
        profile_id_at_version.encode("utf-8"),
        spec_hash.encode("utf-8"),
        occurrence_id_norm.encode("utf-8"),
    ]
    if salt_hex is not None:
        parts.append(salt_hex.encode("utf-8"))
    return US.join(parts)

def seed_digest(material: bytes) -> bytes:
    return hashlib.sha256(material).digest()

def chacha20_stream(seed_key: bytes):
    # 12-byte zero nonce; counter starts at 0; per RFC 8439.
    nonce = b"\x00" * 16  # cryptography lib uses 16-byte (counter || nonce)
    algo = algorithms.ChaCha20(seed_key, nonce)
    enc = Cipher(algo, mode=None).encryptor()
    while True:
        yield enc.update(b"\x00" * 64)

def next_uniform(stream_buf):
    # Pull 8 bytes from the keystream buffer, big-endian uint64
    bs = stream_buf.read(8)
    n = int.from_bytes(bs, "big", signed=False)
    return n / float(1 << 64)

def jitter_uniform_in_disc(R_meters, stream_buf):
    u1 = next_uniform(stream_buf)
    u2 = next_uniform(stream_buf)
    theta = 2.0 * math.pi * u1
    r = R_meters * math.sqrt(u2)
    return r * math.cos(theta), r * math.sin(theta)
```

</details>

<details>
<summary><b>A.2 — Canonical WKB hashing for geom comparison</b></summary>

Geometry comparison MUST use SHA-256 over the **canonical** Well-Known Binary form:

1. Serialize to ISO WKB with **little-endian** byte order, **with** SRID prefix (EWKB form), coordinate precision pinned at IEEE 754 binary64.
2. Strip M and Z components if the profile is 2D-only (declare in the profile).
3. SHA-256 over the resulting bytes.

PROPOSED reference tool: `tools/validators/redaction/canon_wkb.py`. NEEDS VERIFICATION pending repo mount.

</details>

<details>
<summary><b>A.3 — Why not <code>random.seed(...)</code>?</b></summary>

Language stdlib PRNGs almost always vary across runtimes:

- **Python** `random` uses Mersenne Twister with stdlib-specific seeding semantics (the seeding algorithm changed between 3.1 and 3.2; behavior under string seeds is not guaranteed across point releases of CPython).
- **Node.js** `Math.random` is V8-internal (xorshift128+, but explicitly not specified to be reproducible across V8 versions).
- **Go** `math/rand` is reproducible within a Go major version but is not portable to other languages.

Any of these break R1 (same inputs → same bytes) across the KFM toolchain. ChaCha20 keystream output is byte-defined and identical wherever RFC 8439 is implemented.

</details>

<details>
<summary><b>A.4 — Open items at v1 draft</b></summary>

- Salting policy: §8, requires ADR.
- `occurrence_id_norm` whitespace folding: per-profile declaration, requires per-profile review.
- Hashing `occurrence_id_norm` for receipts in rank-4/5 contexts: §13, requires ADR.
- Whether to allow profile-specified IEEE 754 trig wrappers (e.g., `fdlibm`) versus relying on platform `libm`: NEEDS VERIFICATION.
- Whether `centroid_1km_v1` admits any PRNG-driven tie-breaker for points exactly on unit borders: NEEDS VERIFICATION.

</details>

[Back to top](#top)

---

**Related:** [Sensitivity rubric](./SENSITIVITY_RUBRIC.md) · [Canonicalization](./CANONICALIZATION.md) · [Run receipt](./RUN_RECEIPT.md) · [Redaction profile catalog](../../policy/redaction/profiles.yaml)

**Last updated:** 2026-05-14 · **Version:** v1 (PROPOSED) · [Back to top](#top)
