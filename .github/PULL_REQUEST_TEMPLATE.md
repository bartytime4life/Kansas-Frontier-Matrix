<!--
Title: [PR] <concise summary>
Tip: Keep it actionable (“Add…”, “Fix…”, “Update…”). Reference issues: Fixes #123 / Closes #456.
Labels: Prefer ones defined in .github/roadmap/roadmap.yaml when helpful.
-->

## Summary
**What does this change do, and why now?**  
_Context + links. Keep it outcome-oriented. If user-visible, add a one-line release note below._

**Release note (user-visible):** _Optional, concise message for changelog._

---

## Related Issues
- Fixes #
- Closes #
- Relates to #

---

## Type of change
- [ ] Feature (new capability)
- [ ] Fix (bug / regression)
- [ ] Data (new layer / catalog entry / data update)
- [ ] Docs (README, SOPs, model cards, glossary)
- [ ] Build/CI (workflows, tooling, pre-commit)
- [ ] Refactor (no functional change)
- [ ] Performance
- [ ] Chore / housekeeping

---

## Scope & Impact
- **Area(s):** `web` | `web/config` | `scripts` | `src` | `stac` | `data` | `ci` | `docs`
- **Breaking change?** yes/no  
  _If **yes**: describe migration steps & update docs._
- **User-visible?** yes/no  
  _Attach screenshots/GIFs for UI changes (before/after)._

### Screenshots / GIF (optional)
<!-- drag & drop or paste images here -->

---

## Validation (what you ran)
_Check all that apply and paste exact commands._

- [ ] `pre-commit run -a` passes locally
- [ ] Tests green: `pytest -q`
- [ ] Web config schemas pass (`make config-validate`)  
      _(validates `web/config/legend.json`, `categories.json`, `sources.json`)_
- [ ] Viewer configs parse: `web/app.config.json` / `web/layers.json`
- [ ] STAC validation green (items/collections): `make stac-validate`
- [ ] Site preview builds locally (`make site`) and serves (`python -m http.server -d web 8080` or `docker compose --profile dev up -d site`)
- [ ] Link check (lychee) no critical failures
- [ ] JSON/YAML parse clean for `stac/**` and `data/sources/**`
- [ ] (optional) Docker image builds locally
- [ ] Docs render (MkDocs) if changed

**Commands to reproduce**
```bash
# minimal steps to regenerate outputs / site
make prebuild          # stac-validate + config-validate + site (if present)
make stac-validate     # STAC + sources checks
make site              # writes fallback web/layers.json (tiles-only) + mirrors small vectors
make site-config       # render web/app.config.json from STAC (requires kgt)
````

---

## Data & Catalog (if adding/updating datasets)

* [ ] Added/updated **STAC** under `stac/items/**` and/or `stac/collections/**`
* [ ] Updated source descriptors in `data/sources/*.json|yml` (if applicable)
* [ ] License/provenance verified and cited in collection/item metadata
* [ ] Storage plan chosen: **DVC** / **Git LFS** / small in-repo
* [ ] Checksums present where applicable (`checksum:sha256` / `file:size`)
* [ ] Viewer wiring updated: `web/app.config.json`/`web/layers.json` and `web/config/legend.json` `layerBindings` / `legendKey`
* [ ] Story/time presets updated if applicable: `web/config/story_layers.json`, `web/config/time_config.json`

**Paths/IDs**

* STAC: `stac/items/<id>.json`, `stac/collections/<id>.json`
* Sources: `data/sources/<file>.json|yml`
* DVC/LFS: list any tracked files

---

## Reproducibility (MCP)

* [ ] Deterministic pipeline (documented commands / Make targets)
* [ ] Updated/added **SOP** in `mcp/sops/` (if workflow changed)
* [ ] Experiment log in `mcp/experiments/` (if model/analysis)
* [ ] Model card in `mcp/model_cards/` (if ML involved)

---

## Security Considerations

* Secrets handled safely (no tokens committed; `.env*` ignored)
* CI permissions minimal (no new write scopes)
* Dependency changes reviewed (pip/npm/docker)
* Containers pinned to trusted bases
* Any potential injection/vector surfaces addressed (e.g., user-provided GeoJSON/HTML)

---

## Risks & Rollback

* **Risks:** *brief list (perf, correctness, UX, data integrity, CI breakage)*
* **Rollback plan:** *how to revert / disable if needed (e.g., `git revert`, layer toggle, feature flag)*

---

## Reviewer Notes

*Context for reviewers: areas to focus, known trade-offs, follow-ups slated for next PR.*

<!-- End of template -->

```
```
