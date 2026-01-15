<div align="center">

# 🗄️ Storage Adapter (Frontend)

**Path:** `web/src/adapters/storage/README.md`

![Layer](https://img.shields.io/badge/layer-adapter-6c757d)
![Runtime](https://img.shields.io/badge/runtime-browser-0b7285)
![Contract-first](https://img.shields.io/badge/contracts-first-6741d9)
![Provenance-first](https://img.shields.io/badge/provenance-first-2f9e44)
![Status](https://img.shields.io/badge/status-active-success)

A **thin persistence layer** for the KFM web UI: **versioned**, **namespaced**, **auditable**, and safe-by-default for **sensitive data**.

</div>

---

## 🧭 Quick navigation

- [Why this adapter exists](#-why-this-adapter-exists)
- [Architecture fit](#-architecture-fit)
- [What belongs here](#-what-belongs-here)
- [Storage drivers](#-storage-drivers)
- [Key + record conventions](#-key--record-conventions)
- [Port contract](#-port-contract)
- [Migrations + invalidation](#-migrations--invalidation)
- [Security + governance](#-security--governance)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [References](#-references--project-library)

---

## 🎯 Why this adapter exists

KFM’s UI needs persistence that is:

- **Swappable** (localStorage today, IndexedDB tomorrow, remote cache later)
- **Consistent** (same get/set semantics everywhere)
- **Traceable** (no “mystery layers” or unlabeled artifacts in UI)
- **Governed** (sensitivity rules respected end-to-end)
- **Performant** (avoid blocking UX & main-thread stalls)

This aligns with KFM’s **contract-first + provenance-first** rule: *anything that shows up in the UI should be traceable to cataloged sources and provable processing.* :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

## 🏗️ Architecture fit

This directory is an **adapter layer**: it implements a **Storage Port** used by UI/state logic, hiding vendor details (Web Storage, IndexedDB, remote APIs, etc.). This keeps core logic technology-agnostic and reduces ripple effects from change. :contentReference[oaicite:2]{index=2}

```mermaid
flowchart LR
  UI[🧩 UI / State / Features] -->|depends on| Port[🔌 Storage Port]
  Port --> MEM[🧠 Memory Adapter]
  Port --> LS[🗝️ localStorage Adapter]
  Port --> IDB[🗃️ IndexedDB Adapter]
  Port --> REM[🌐 Remote/HTTP Adapter]
  Port --> HYB[🧬 Hybrid Adapter (tiered)]
```

---

## 📦 What belongs here

### ✅ Good fits
- UI preferences (theme, language, accessibility toggles)
- Map/UI state (viewport, active layers, filters)
- **Cacheable** responses (STAC items, catalog fragments, search results)
- Offline-first artifacts (lightweight tiles, prefetch manifests, “recently used” lists)
- Drafts (story/focus drafts *only if non-sensitive and explicitly allowed*)

### 🚫 Non-goals
- Storing canonical datasets (those belong in KFM catalogs / API)
- Storing secrets (API keys, long-lived tokens, raw PII)
- Bypassing governance (“public UI must not persist confidential artifacts”)

> **Rule of thumb:** If a record is not safe to persist on a user’s device, it should not go through a persistent storage driver by default. :contentReference[oaicite:3]{index=3}

---

## 🧰 Storage drivers

### Decision matrix ✅

| Driver | Best for | Pros | Cons | Typical quota |
|---|---|---|---|---|
| 🧠 Memory | tests, ephemeral session state | fastest, no persistence | lost on refresh | N/A |
| 🗝️ localStorage | tiny settings + flags | simple API, cross-tab events | **sync/blocking**, strings-only | ~5–10MB (varies) :contentReference[oaicite:4]{index=4} |
| 🗃️ IndexedDB | caches, offline, larger objects | async, larger storage, structured | more complexity, schema mgmt | large (browser-managed) |
| 🍪 Cookies (rare) | server-coordinated flags | server-readable | tiny, sent every request | very small |
| 🌐 Remote/HTTP | shared cache between devices | consistent across devices | network latency, auth | server-defined |

> localStorage is **string-only** and typically requires JSON serialization. :contentReference[oaicite:5]{index=5}

### Recommended default
- **Memory** for volatile session state
- **localStorage** for tiny preferences (<= ~100KB total)
- **IndexedDB** for caches/offline artifacts

---

## 🧱 Key + record conventions

### 1) Namespaced keys 🧷

Use stable, descriptive keys to prevent collisions and simplify migrations. KFM’s broader naming conventions favor unique, descriptive IDs (e.g., `kfm.ks.landcover...v1`). :contentReference[oaicite:6]{index=6}

**Storage key pattern:**
```
kfm:<scope>:<domain>:<entity>:<version>:<id>
```

**Examples:**
- `kfm:ui:prefs:theme:v1:singleton`
- `kfm:map:state:viewport:v2:singleton`
- `kfm:cache:stac:item:v1:<stacItemId>`
- `kfm:cache:dcat:dataset:v1:<datasetId>`

### 2) Record envelope (recommended) 🧬

To support “no mystery layers” and provenance-friendly behavior, store values in a consistent envelope:

```ts
export type Sensitivity = "public" | "restricted" | "confidential";

export type StoredRecord<T> = {
  value: T;

  meta: {
    /** Schema version for this record type */
    schemaVersion: number;

    /** Timestamps */
    createdAt: string;  // ISO
    updatedAt: string;  // ISO

    /** Source + lineage hooks (lightweight pointers; not full PROV) */
    source?: {
      datasetId?: string;      // e.g. DCAT/STAC id
      stacItemId?: string;
      url?: string;
      license?: string;
    };

    /** Governance */
    sensitivity: Sensitivity;

    /** Cache controls */
    ttlMs?: number;
    expiresAt?: string; // ISO
    etag?: string;
    checksum?: string;
  };
};
```

Why this matters:
- KFM treats provenance + contract metadata as first-class (trust model, citations, no unsourced artifacts). :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8}
- Sensitivity rules must propagate and **must not be loosened downstream** (“no output less restricted than input”). :contentReference[oaicite:9]{index=9}

### 3) Serialization 📦
- **localStorage**: serialize `StoredRecord<T>` via `JSON.stringify()`
- **IndexedDB**: store structured objects directly where possible

---

## 🔌 Port contract

Keep the contract small, async-first, and testable.

```ts
export type StorageCapabilities = {
  persistent: boolean;
  supportsBinary: boolean;
  supportsTransactions: boolean;
  crossTabEvents: boolean;
};

export type StorageGetOptions = {
  /** If true, ignore ttl and return stale data (useful for debugging) */
  allowStale?: boolean;
};

export type StorageSetOptions = {
  ttlMs?: number;
  sensitivity?: "public" | "restricted" | "confidential";
  /** Optional: avoid writing if unchanged */
  ifUnchanged?: { etag?: string; checksum?: string };
};

export interface StoragePort {
  readonly name: string;
  readonly capabilities: StorageCapabilities;

  get<T>(key: string, opts?: StorageGetOptions): Promise<T | undefined>;
  set<T>(key: string, value: T, opts?: StorageSetOptions): Promise<void>;

  delete(key: string): Promise<void>;
  clear(prefix?: string): Promise<void>;

  keys(prefix?: string): Promise<string[]>;
}
```

### Example usage (UI feature) ✨

```ts
const KEY = "kfm:ui:prefs:theme:v1:singleton";

await storage.set(KEY, {
  value: "dark",
  meta: {
    schemaVersion: 1,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    sensitivity: "public",
  },
});

const themeRecord = await storage.get<{ value: string; meta: any }>(KEY);
```

---

## 🧭 Migrations + invalidation

### Versioning strategy 🗂️
- Put **schema version** in **both**:
  1) the key namespace (`...:v2:...`), and/or
  2) the record envelope (`meta.schemaVersion`)

### Invalidation strategy ♻️
When upstream catalog/API versions change, invalidate caches deterministically:

- Include release identifiers in cache keys:
  - `kfm:cache:stac:item:v1:<releaseId>:<stacItemId>`
- Or store a single “current release” key:
  - `kfm:meta:catalogRelease:v1:singleton`

This mirrors KFM’s deterministic, contract-first pipeline mindset (stable outputs for stable inputs). :contentReference[oaicite:10]{index=10}

---

## 🔐 Security + governance

### 🚫 Don’t persist secrets
- localStorage is accessible to JS and vulnerable under XSS conditions.
- Avoid persisting auth tokens or API keys.

### 🧭 Sensitivity rules (KFM-aligned)
KFM’s governance expects:
- sensitivity tagging,
- redaction/generalization where needed,
- and the invariant: **no downstream loosening of restrictions**. :contentReference[oaicite:11]{index=11}

**Storage adapter implications:**
- If `sensitivity === "confidential"`:
  - prefer **memory/session-only** storage unless explicitly allowed
  - consider encrypt-at-rest (if implemented) + TTL + aggressive eviction
- Never “upgrade” a record’s classification when copying between tiers.

### 🧾 Audit-friendly behavior
If the UI withholds/generalizes data, emit a telemetry event like:
- `focus_mode_redaction_notice_shown`
- `storage_eviction_occurred`
- `storage_quota_exceeded`

This is consistent with governance expectations for audit trails. :contentReference[oaicite:12]{index=12}

---

## 🧪 Testing

### Contract tests (recommended) ✅
Treat `StoragePort` as a contract:
- same behavior across drivers
- shared test suite
- run in:
  - Node (memory adapter)
  - Browser (localStorage/IndexedDB adapters)

What to test:
- set/get roundtrip
- delete/clear/prefix clearing
- TTL expiry logic
- schemaVersion migration behavior
- quota errors & fallback logic

---

## 🛠️ Troubleshooting

### “Quota exceeded” / silent failures
- localStorage quotas vary across browsers (mobile/desktop). :contentReference[oaicite:13]{index=13}
- Prefer IndexedDB for anything beyond tiny preferences.

### Cross-tab sync caveats
- localStorage has `storage` events for cross-window sync, but there are edge cases depending on browser and domain handling. :contentReference[oaicite:14]{index=14}

### Performance hiccups
- Avoid heavy localStorage writes in hot UI loops (it’s synchronous).
- Batch writes, debounce, or move to async storage.

---

## 📚 References & project library

> These are the core project docs that inform this adapter’s philosophy (contract-first, provenance-first, deterministic outputs, performance, and change-friendly design).

- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16}
- MARKDOWN_GUIDE v13 (contract-first, evidence-first, governance invariants) :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19}
- JavaScript Notes (Web Storage behavior + quotas + events) :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}
- Flexible Software Design (stable identifiers, flexibility under change) :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}
- Database Performance at Scale (performance mindset; measure + manage bottlenecks) :contentReference[oaicite:24]{index=24}
- Scalable Data Management for Future Hardware (performance/latency thinking; structured approaches to data processing) :contentReference[oaicite:25]{index=25}

### 🔗 Additional project files (pinned)
- MATLAB / programming compendiums (general engineering reference) :contentReference[oaicite:26]{index=26}
- Bash / scripting compendiums (tooling + automation reference) :contentReference[oaicite:27]{index=27}
- Understanding Machine Learning (modeling context for “evidence artifacts”) :contentReference[oaicite:28]{index=28}
- Archaeological 3D GIS (domain context; sensitivity + location handling implications) :contentReference[oaicite:29]{index=29}

---

## ✅ Definition of done (for this adapter)

- [ ] `StoragePort` exists and is the only dependency for UI/features
- [ ] At least **2 drivers** implemented (Memory + one persistent)
- [ ] Contract tests run against all drivers
- [ ] All persisted artifacts are **namespaced**, **versioned**, and optionally **enveloped**
- [ ] Sensitivity rules are respected (no “confidential” persistence by default)
- [ ] Clear invalidation/migration strategy documented (this file)

