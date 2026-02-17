# KFM Web UI — Third‑Party Licenses & Attributions

[![Governed](https://img.shields.io/badge/Governed-yes-2b6cb0)](#governance-rules)
[![Evidence-first](https://img.shields.io/badge/Evidence--first-required-2f855a)](#what-belongs-here)
[![Public directory](https://img.shields.io/badge/Served%20from-web%2Fpublic-important-d69e2e)](#critical-this-folder-is-public)

This folder is the **public, user-visible “licenses shelf”** for the KFM web client. It contains third‑party
license texts and attribution notices for software and assets that ship with (or are referenced by) the
web app.

## Critical: This Folder Is Public

Anything under `web/public/` is served to end users.

- **Do not** place secrets, API keys, tokens, private email addresses, or internal-only documents here.
- **Do not** place content you are not allowed to redistribute (for example: proprietary PDFs/books).
- **Do** include license texts and attribution notices that users are entitled to see.

> [!NOTE]
> This directory is primarily for compliance (OSS license notices, attribution requirements) and user trust.

## What Belongs Here

Typical contents:

- **Third‑party dependency notices** for the web app’s runtime and build dependencies (npm/pnpm/yarn).
- **Vendored assets** that live in `web/public/` (fonts, icons, client-side libraries) along with their license files.
- **External service attributions** required by terms (for example basemaps / tiles / imagery providers), even if
  the bytes are not hosted here.

## Suggested Layout

```text
web/public/_licenses/
├─ README.md                         # You are here
├─ THIRD_PARTY_NOTICES.md            # Human-readable rollup shown in the UI (generated)
├─ licenses.json                     # Machine-readable index (generated)
└─ licenses/                         # Optional: one file per dependency (generated or curated)
   ├─ react__LICENSE.txt
   ├─ maplibre-gl__LICENSE.txt
   └─ ...
```

> [!TIP]
> Prefer generating `THIRD_PARTY_NOTICES.md` and `licenses.json` in CI to avoid drift.

## How To Update Licenses (Recommended Workflow)

### 1) Generate notices for JS dependencies

Pick the command that matches your package manager:

```bash
# pnpm (example)
pnpm licenses list --prod --json > web/public/_licenses/licenses.json

# yarn (example)
yarn licenses list --production --json > web/public/_licenses/licenses.json

# npm (example using license-checker)
npx license-checker --production --json > web/public/_licenses/licenses.json
```

Then render a human-readable rollup (example script idea):

```bash
node scripts/licenses/render-notices.mjs \
  --in web/public/_licenses/licenses.json \
  --out web/public/_licenses/THIRD_PARTY_NOTICES.md
```

### 2) Add (or update) non-npm asset attributions

If the web UI uses assets that are not captured by package manager tooling (fonts, icons, raster imagery,
basemap providers), add them to the rollup and ensure the **exact** attribution text and link required by
the upstream license/terms are present.

Use (and keep current) a table like this in `THIRD_PARTY_NOTICES.md`:

| Asset / Service | Where used | License / Terms | Required attribution | Evidence link |
|---|---|---|---|---|
| Example: “Basemap Provider X” | Map UI | CC BY 4.0 | “© Provider X” | Link to terms |
| Example: “Icon Set Y” | UI icons | MIT | Include MIT text | Link to LICENSE |

### 3) Run a governance sanity check

- Ensure every entry has:
  - **Name** (and version if applicable)
  - **License identifier** (SPDX where possible)
  - **Upstream source link**
  - **License text** (or a link to canonical license text)
  - **Where/how it’s used** (so reviewers can validate necessity)

- Flag anything that is:
  - **Non‑redistributable**
  - **Non‑commercial (NC)** / **No‑derivatives (ND)**
  - **Copyleft** that may impose requirements on distribution
  - **Custom/EULA** terms

## Governance Rules

KFM treats licensing as a first-class governance concern:

1. **Evidence-first:** every attribution claim must be traceable to an upstream license file or terms page.
2. **Fail-closed:** if a dependency’s license cannot be determined, it should block release until resolved.
3. **No surprise sharing:** do not host or distribute content you do not have rights to redistribute.
4. **Review required:** any new dependency with restrictive terms must be surfaced in PR review.

### License Risk Categories (Guidance)

| Category | OK to ship? | Typical examples | Notes |
|---|---:|---|---|
| Green | ✅ Yes | MIT, BSD-2/3-Clause, Apache-2.0, ISC | Keep notices and attribution requirements. |
| Yellow | ⚠️ Review | MPL-2.0, LGPL-2.1/3.0, CC BY, custom terms | May require specific distribution steps or source offer. |
| Red | ⛔ Block until approved | “All rights reserved”, CC BY-NC, CC BY-ND, unknown | Likely incompatible with redistribution or commercial use. |

> [!IMPORTANT]
> This table is a triage aid, not legal advice. When in doubt, escalate to governance review.

## Definition of Done (DoD) for a License Update PR

- [ ] `licenses.json` updated via a repeatable command
- [ ] `THIRD_PARTY_NOTICES.md` regenerated from `licenses.json`
- [ ] Non-npm assets/services captured with correct attribution text
- [ ] New/changed licenses reviewed and classified (Green/Yellow/Red)
- [ ] CI check added or passing (no unknown licenses, no missing notices)
- [ ] UI “Licenses” screen (if present) still renders and links work

---

### FAQ

**Why is this in `web/public/`?**  
So end users can view notices and attribution texts from the running app.

**Can we link instead of embedding full license text?**  
Some licenses/terms allow linking, some require inclusion. Default to including text when it’s short and
clearly licensed for redistribution.

**Where should build tooling live?**  
Prefer `web/scripts/` or a repo-level `scripts/` directory with CI integration; keep the outputs here in
`web/public/_licenses/`.

[Back to top](#kfm-web-ui--thirdparty-licenses--attributions)
