# Roadmap → GitHub sync

This folder holds the **single source of truth** for your project roadmap and the
automation that syncs it to **GitHub labels, milestones, and issues**.

- `roadmap.yaml` — declarative roadmap (human-edited)
- The workflow **`.github/workflows/roadmap.yml`** reads `roadmap.yaml` and runs
  `scripts/sync-roadmap.js` to create/update labels, milestones, and issues.

> On **pull requests** the workflow runs in **DRY RUN** (no writes).  
> On **pushes to `main`** and **manual dispatch** (unless `dry_run=true`) it **applies** changes.

---

## How it works (idempotent sync)

1. Parse `roadmap.yaml`.
2. Ensure **labels** exist (create/update color & description).
3. Ensure **milestones** exist (create/update title, due date, state).
4. Ensure **issues** exist or are updated (title, body, labels, milestone, assignees).
5. Track items by a stable **`key`** you define. The sync script writes a hidden marker
   into each synced issue body:

```html
<!-- roadmap:key=<your-key> -->
````

This makes the sync **repeatable** and safe to run anytime.

---

## Minimal example: `roadmap.yaml`

```yaml
version: 1

labels:
  - name: area:web
    color: 1f6feb
    description: Web viewer / UI
  - name: area:data
    color: 0e8a16
    description: Data & STAC
  - name: type:feature
    color: fbca04
  - name: type:chore
    color: a7a7a7
  - name: priority:p1
    color: d73a4a
  - name: status:planned
    color: 8a2be2
  - name: status:doing
    color: 5319e7
  - name: status:done
    color: 0e8a16

milestones:
  - key: m25q4
    title: 2025 Q4
    due_on: 2025-12-31
    state: open

epics:
  - key: epic-web-v1
    title: Web Viewer v1 (MapLibre + time)
    milestone: m25q4
    labels: [area:web, type:feature, priority:p1, status:planned]
    body: |
      Goals:
      - Time slider across layers
      - Schema-validated configs
      - Pages deploy CI
    issues:
      - key: web-config-schema
        title: Schema: app.config.json & layers.json
        labels: [area:web, type:chore, status:doing]
        assignees: [bartytime4life]
        body: |
          Validate app/layers configs against JSON Schema in CI.
          <!-- roadmap:key=web-config-schema -->
      - key: web-pages-deploy
        title: Pages: Build & Deploy workflow
        labels: [area:web, type:feature, status:planned]
        body: |
          Build _site and deploy via actions/deploy-pages@v4.
          <!-- roadmap:key=web-pages-deploy -->

# You can also define top-level issues (not in an epic):
issues:
  - key: stac-validate-ci
    title: STAC validation workflow
    milestone: m25q4
    labels: [area:data, type:chore, status:planned]
    body: |
      Validate catalog/collections/items with pystac + json sanity.
      <!-- roadmap:key=stac-validate-ci -->
```

**Notes**

* `key` is your stable identifier (letters, digits, dashes).
* `milestone` references a `milestones[].key`.
* `labels` are strings that must match `labels[].name` (the sync will create them if missing).
* `assignees` are GitHub usernames (optional).
* The sync script adds `<!-- roadmap:key=... -->` to issues so it can find and update them safely.

---

## Running the sync

### In CI (recommended)

* The workflow `.github/workflows/roadmap.yml` runs automatically:

  * **PRs** → **DRY RUN** (no writes), shows a log in the job summary.
  * **Push to `main`** → **APPLY** changes.
  * **Manual**: `Run workflow` with `dry_run: true|false`.

### Locally (advanced)

```bash
# In project root
export GITHUB_TOKEN=ghp_xxx   # classic or fine-grained token with 'repo' scope
npm ci                        # from ROADMAP_WORKDIR (default: .)
DRY_RUN=true node scripts/sync-roadmap.js   # simulate (logs only)
DRY_RUN=false node scripts/sync-roadmap.js  # apply (creates/updates on GitHub)
```

> The workflow passes `DRY_RUN` via environment; prefer `DRY RUN` on PRs.

---

## Conventions

**Label taxonomy (suggested)**

* `area:*` — code/data area (`area:web`, `area:data`, `area:ci`, `area:docs`)
* `type:*` — change type (`type:feature`, `type:bug`, `type:chore`, `type:refactor`)
* `priority:p{1..3}` — P1 (highest) to P3
* `status:*` — `planned`, `doing`, `blocked`, `done`
* optional: `risk:*`, `needs:review`, `good first issue`

**Milestones**

* Timeboxed (`YYYY Q#`) or release tags (`vX.Y`).
* Use a `key` for stable references (e.g., `m25q4`, `v1-0`).

**Epics**

* High-level containers with an `issues:` list.
* The sync does **not** create GitHub “epic” objects (GitHub has Projects/Iterations); it creates a normal issue for the epic, then normal issues for its children. (If your script supports parent/child linking, it can reference the epic’s issue number after creation.)

---

## FAQ

**Q: What if I rename a label or milestone?**
A: Update `roadmap.yaml`. The sync updates titles/descriptions/colors but cannot safely “rename” labels in bulk across existing issues; it will create the new label and apply it to synced issues. You can remove old labels manually if needed.

**Q: How are issues matched across runs?**
A: By the `<!-- roadmap:key=... -->` marker in the body. If missing, the script may match by title (best-effort), then writes the marker.

**Q: Can I close issues via the roadmap?**
A: If your `scripts/sync-roadmap.js` supports a `state: closed` attribute on issues, you can use it. Otherwise, close them manually—future runs won’t reopen unless the script is written to do so.

---

## Gotchas

* YAML is whitespace-sensitive. Validate with `yamllint` or your IDE if you see parse errors.
* Usernames in `assignees` must have access to the repo.
* Labels must be unique by `name`.
* Keep `key` stable—changing it creates a *new* issue.

---

## Changelog for this folder

* **2025-09-23**: Initial roadmap sync docs. Supports DRY RUN on PRs, apply on `main`/manual.

```
