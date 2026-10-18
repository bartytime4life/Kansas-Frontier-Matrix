<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/infra/godaddy
title: infra/godaddy — GoDaddy web hosting exposure
type: README
subtype: boundary-compact
version: v1
status: retained cPanel alternative; not the active Node deployment
owners: ["@bartytime4life"]
created: 2026-10-12
updated: 2026-10-17
policy_label: public
current_path: infra/godaddy/README.md
owning_root: infra/
responsibility: Retained Apache configuration and transfer implementation for the earlier static-front-door alternative; secret references only
truth_posture: CONFIRMED retained Apache and transfer implementation; this alternative does not establish the active Node deployment
related:
  - ../../docs/runbooks/godaddy-hosting.md
  - ../../apps/public-site/README.md
  - ../../.github/workflows/godaddy-public-site.yml
[/KFM_META_BLOCK_V2] -->

# `infra/godaddy/`

Historical cPanel/Apache exposure for the static-front-door alternative. The active public Explorer uses a separate Node application; use the [Node runbook](../../docs/runbooks/godaddy-node-hosting.md). Do not run this alternative transfer process against the active Node deployment. The application lives in [`apps/public-site/`](../../apps/public-site/README.md); operator steps are in the [GoDaddy hosting runbook](../../docs/runbooks/godaddy-hosting.md).

| File | Role |
|---|---|
| [`htaccess.template`](htaccess.template) | Rendered into the bundle's `.htaccess`. It enforces HTTPS and redirects `www` and any other host to the canonical apex. It provides the `/explorer` redirect, denies dotfiles, and leaves AutoSSL validation untouched. It also sets HSTS, a strict CSP with no scripts, `nosniff`, deny framing, cache rules, compression and CORS for the two JSON endpoints. |
| [`deploy.sh`](deploy.sh) | Mirrors `apps/public-site/dist/` to the document root with `lftp`. It uses SFTP with a pinned host key (preferred) or explicit FTPS with certificate verification. Remote deletion is opt-in, and cPanel-owned paths are always excluded. |

No credentials are stored here. The deploy reads `GODADDY_*` values from the `godaddy-production` GitHub environment; the runbook lists each one.

Run a local dry run against the real host. The values come from your own shell, never from files in the repository:

```bash
GODADDY_HOST=… GODADDY_USER=… GODADDY_KNOWN_HOSTS="$(ssh-keyscan -p 22 …)" GODADDY_SSH_KEY="$(cat ~/.ssh/kfm-deploy)" DRY_RUN=true bash infra/godaddy/deploy.sh
```
