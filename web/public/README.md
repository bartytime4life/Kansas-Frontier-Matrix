# `web/public/` — Public, Unbundled Static Assets 🌾🗺️

![Layer](https://img.shields.io/badge/layer-Web%20UI-blue)
![Exposure](https://img.shields.io/badge/exposure-PUBLIC-success)
![Governance](https://img.shields.io/badge/governance-trust%20membrane-critical)
![Rule](https://img.shields.io/badge/rule-no%20secrets%20in%20public-important)

This directory holds **static files that are served directly** by the KFM Web UI host (copied “as-is” to the built site). These files are **not** governed by API policy at request time the way PostGIS/object-store/GraphQL responses are — they’re simply *downloaded by every browser*.

> [!WARNING]
> **Everything in `web/public/` is public.**  
> Treat it like you’re publishing it to the open internet (because you are).

---

## What belongs here ✅

Typical examples (toolchain-agnostic; React/TS setups commonly treat `public/` this way):

- Favicons / app icons
- `manifest.json` (PWA metadata)
- `robots.txt`
- Static UI images (logos, UI icons, illustrations)
- Fonts **licensed** for web distribution
- Public-only “runtime config” JSON **with zero secrets** (optional pattern)

> [!NOTE]
> In common React toolchains, `public/` files are **not part of the compilation/bundling step** and remain untouched during the build; `index.html`, `manifest.json`, icons, and `robots.txt` are typical residents.  
> (If KFM’s actual build differs, update this README.)  

---

## What must NEVER be here ❌ (fail-closed)

| Category | Examples | Why this is forbidden |
|---|---|---|
| **Governed datasets / exports** | DCAT, STAC, GeoJSON exports, PMTiles, parquet, raw imagery, “sample datasets” | Bypasses the trust membrane (no auth/policy/redaction/audit) |
| **Sensitive-location content** | precise archaeology sites, protected resources, exact coordinates or “helpful” debug layers | Increases harm/risk; violates KFM sensitivity handling |
| **Secrets or credentials** | API keys, tokens, `.env`, service creds, private endpoints, internal URLs | Immediately compromised (public download) |
| **PII / private individuals** | names, emails, addresses, phone numbers, “temporary” spreadsheets | Privacy/compliance risk |
| **Unlicensed assets** | copied photos/maps/icons without clear reuse rights | IP/compliance risk |

> [!IMPORTANT]
> If it needs a sensitivity classification other than **public**, it does **not** belong in `web/public/`.

---

## KFM governance reminder: “static ≠ governed”

KFM enforces a trust membrane through the API gateway and policy-as-code. **Frontend and static assets must not bypass this boundary.** Anything requiring:
- policy filtering,
- redaction/generalization,
- evidence resolution,
- audit/provenance logging,

…must be fetched through governed endpoints (not embedded in static files).  

---

## Suggested directory layout 📁

> [!TIP]
> Keep a small, predictable tree. Prefer **content-addressed / hashed** filenames for anything cacheable.

```text
web/public/
  README.md                 # you are here
  robots.txt
  manifest.json
  favicon.ico

  icons/                    # app icons (PWA, favicons, apple-touch)
    icon-192.png
    icon-512.png

  images/
    brand/                  # logos, wordmarks
    ui/                     # UI illustrations/icons not handled by bundler

  fonts/                    # ONLY if web redistribution is allowed

  _licenses/                # third-party license texts / notices (recommended)
  _provenance/              # asset provenance notes (recommended)
```

---

## Provenance & licensing for assets 🧾

KFM is evidence-first. That mindset applies to UI assets too:

### Required for third-party assets (images/fonts/icons)
Create a small provenance note:

- `web/public/_provenance/<asset-basename>.md`

Suggested template:

```md
# Asset provenance: <filename>

- Source: <URL or archive reference>
- Retrieved: <YYYY-MM-DD>
- License: <SPDX-ish name or exact license text reference>
- Attribution required: <yes/no + exact attribution language>
- Modifications: <none | cropped | compressed | recolored | etc.>
- Notes: <any restrictions or cautions>
```

> [!WARNING]
> Do not add assets if you cannot document **reuse rights**.

---

## Security rules 🔒

- **No secrets** in this folder. Ever.
- Treat **SVG as code**:
  - Avoid inline scripts/events.
  - Prefer vetted/sanitized SVGs (or rasterize to PNG/WebP if unsure).
- Don’t ship files that imply “backend trust” (e.g., “public debug endpoints list”).
- If adding client-side integrity features (SRI, CSP), keep them consistent with the web host’s headers.

---

## Performance rules ⚡

- Prefer **WebP/AVIF** for large images (where acceptable).
- Optimize:
  - SVG: `svgo`
  - PNG/JPG: lossless/lossy compression as appropriate
- Keep icons small; prefer vectors when safe.
- Use **hashed filenames** for long-lived caching (e.g., `logo.3f2a1c.svg`) when possible.

---

## Definition of Done ✅ (for any PR that touches `web/public/`)

- [ ] Asset is **public-safe** (no restricted/sensitive-location/aggregate-only content).
- [ ] No secrets (review + secret scanning passes).
- [ ] License/provenance recorded for any third-party asset (`_provenance/` + `_licenses/` if needed).
- [ ] Asset optimized (size/perf) and named consistently.
- [ ] Build output verified locally (asset reachable, correct paths).
- [ ] Accessibility checked (e.g., icons used with appropriate labels/alt text in UI code).
- [ ] No governance bypass introduced (no embedded datasets / no direct DB access patterns).

---

## Related (expected) docs 🔗

- `web/README.md` — Web UI overview (React/TS + MapLibre + Cesium) and UI contracts
- `docs/search/` and `docs/pipelines/` — data catalogs and promotion gates
- `docs/runbooks/` — operational and reliability practices