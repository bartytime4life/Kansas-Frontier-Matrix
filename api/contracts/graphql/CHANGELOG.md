# 🕸️ KFM GraphQL Contract — CHANGELOG

![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.1.0-success) ![SemVer](https://img.shields.io/badge/SemVer-2.0.0-blue) ![Contract First](https://img.shields.io/badge/Contract--First-Enabled-purple)  
![GraphQL](https://img.shields.io/badge/GraphQL-SDL%20Contract-ff69b4) ![Governance](https://img.shields.io/badge/Governed-FAIR%2BCARE-informational)

> 📌 This changelog tracks **user-facing changes** to the **GraphQL contract** (SDL + directives + error conventions + persisted ops) that power KFM’s governed API boundary.  
> 💡 If it changes the schema in a way that impacts consumers, it belongs here.

---

## 🗂️ Contract Location

```text
📦 api/
└─ 📜 contracts/
   └─ 🕸️ graphql/
      ├─ 🧬 schema.graphql            # Canonical SDL (or assembled SDL entrypoint)
      ├─ 🧾 CHANGELOG.md              # ✅ you are here
      ├─ 🧩 directives.graphql        # Optional: shared directives (@auth, @sensitivity, etc.)
      ├─ 🧪 examples/                 # Optional: sample operations + fixtures
      └─ 🔒 persisted/                # Optional: persisted query manifests (hash → op)
```

> ⚠️ Even if the server implementation lives elsewhere (e.g., `src/server/...`), **this folder is the consumer contract boundary**. Keep it authoritative.

---

## 📏 Versioning Rules (SemVer) ✅

We follow **Semantic Versioning** for the GraphQL contract:

- **MAJOR** (`X.0.0`) — breaking schema changes  
  - Field/type removal  
  - Argument behavior changes  
  - Enum value removal  
  - Auth/sensitivity rule that breaks existing callers
- **MINOR** (`0.Y.0`) — additive, backwards-compatible  
  - New types/fields/queries/mutations  
  - New enum values  
  - New optional arguments
- **PATCH** (`0.0.Z`) — contract-safe fixes  
  - Documentation fixes  
  - Clarifying descriptions  
  - Bugfixes that do **not** change schema surface

### 🧯 Deprecation Policy (GraphQL-friendly)

- Prefer **deprecation over removal**:
  - Mark fields/types with `@deprecated(reason: "...")`
  - Keep deprecated fields for **≥ 2 MINOR versions** (unless critical security issue)
- Deprecation entries must include:
  - ✅ what is deprecated  
  - ✅ replacement  
  - ✅ planned removal version

---

## 🧭 What This Changelog Covers

✅ Track here:
- SDL changes (`type`, `interface`, `input`, `enum`, `union`, `scalar`)
- Directives and their semantics (`@auth`, `@sensitivity`, `@cost`, etc.)
- GraphQL error `extensions` conventions (standardized codes)
- Pagination conventions (Connection vs Offset)
- Persisted operation names/IDs if clients rely on them

🚫 Don’t track here:
- Resolver performance tweaks that don’t change behavior  
- Internal DB migrations (Neo4j/PostGIS) unless they alter schema output

---

# 🧾 Changelog

All notable changes to this contract will be documented in this file.

## [Unreleased] 🚧

### ✨ Added
- **Realtime contracts** for future live layers:
  - `Subscription` surface for sensor/telemetry-style updates (e.g., map overlays, dashboards).
- **Offline Pack manifests** for field/mobile usage:
  - A discoverable type for offline bundles (tiles + metadata + checksums + extents).
- **OCI/ORAS artifact distribution descriptors** (experimental):
  - Distribution objects that can point to artifacts stored in an OCI registry (digest-addressed).
- **Policy Gate visibility** (governance-first):
  - Optional return objects that expose *why* something is redacted/blocked (without leaking restricted info).
- **Story/Narrative contract extensions**:
  - Typed Story Node manifest fields to support map/timeline-driven narratives.

### 🔁 Changed
- Standardized pagination guidance across list fields:
  - Prefer **Connections** for graph traversals.
  - Allow offset pagination only for stable, deterministic lists.

### ⚠️ Deprecated
- None.

### 🗑️ Removed
- None.

### 🛠️ Fixed
- None.

### 🔒 Security
- Added/clarified **query complexity guardrails** guidance:
  - Depth limiting, capped list sizes, and/or cost directives for graph traversals.
- Added/clarified **sensitive attribute handling** guidance:
  - Encourage explicit sensitivity metadata and consistent redaction behavior.

---

## [0.1.0] - 2026-01-24 🎉

### ✨ Added
- **Core graph traversal types** designed for semantic/relationship queries:
  - `Person`, `Place`, `Event`, `Dataset` (and their relationship fields).
- **GraphQL-first “semantic bundle” philosophy**:
  - Callers can fetch an entity and its relationships in a single request (e.g., Person → Events → Places).
- **Governed “Evidence-first” dataset exposure**
  - Dataset records support linking to evidence catalogs (STAC/DCAT/PROV) and lineage-style relations.
- **API boundary expectations in contract language**
  - The GraphQL layer is a first-class boundary (no “UI → DB direct” coupling).
- **Foundation for AI + Focus Mode integration**
  - Contract vocabulary reserved for returning:
    - answer payloads
    - citations
    - provenance-linked context bundles
    - audit-style metadata (where applicable)
- **Security + performance expectations baked into contract guidance**
  - Encourages pagination for lists and safeguards against overly-expensive recursive queries.

### 🔁 Changed
- N/A (initial contract release).

### 🛠️ Fixed
- N/A (initial contract release).

---

## 🧪 Example Query (for sanity checks)

> Keep examples small and stable — they’re used to validate compatibility and documentation.

```graphql
query PersonWithEventsAndPlaces($name: String!) {
  person(name: $name) {
    name
    events {
      title
      date
      locations { name }
    }
  }
}
```

---

## 📚 Design Sources Used (Contract Vocabulary + Roadmap)

These project docs shaped the contract surface and what we consider “breaking” vs “additive”:

- 📄 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation**
- 🧱 **Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design**
- 🖥️ **Kansas Frontier Matrix – Comprehensive UI System Overview**
- 🧭🤖 **Kansas Frontier Matrix (KFM) – AI System Overview**
- 📚 **Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide**
- 🌟 **Kansas Frontier Matrix – Latest Ideas & Future Proposals**
- 💡 **Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)**
- 🧠 **AI Concepts & more** (reference compendium)
- 🗃️ **Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas** (reference compendium)
- 🗺️ **Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl** (reference compendium)
- 🧰 **Various programming langurages & resources 1** (reference compendium)
- 🧩 **Additional Project Ideas** (OCI/ORAS/Cosign + governance ideas)
- 🧾 **Master Guide / v13 contract-first guidance** (project standards + invariants)

---

## 🔗 Links

- Keep a Changelog: https://keepachangelog.com/en/1.1.0/
- Semantic Versioning: https://semver.org/spec/v2.0.0.html
