<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-hosting
title: Connect kansasfrontiermatrix.com to GoDaddy web hosting
type: runbook
version: v1
status: repository-ready; hosting account, secrets, DNS cutover and first live deploy not yet verified
owners: ["@bartytime4life"]
created: 2026-10-12
updated: 2026-10-12
policy_label: public
current_path: docs/runbooks/godaddy-hosting.md
owning_root: docs/
responsibility: Operator steps to serve the static public front door from GoDaddy cPanel hosting, move the Explorer to a subdomain, deploy from GitHub Actions, verify and roll back
truth_posture: DNS state recorded 2026-10-12 by public lookup; GoDaddy account settings, cPanel host name, document root and SSH availability are UNKNOWN until the owner reads them from the GoDaddy dashboard
related:
  - ../../apps/public-site/README.md
  - ../../infra/godaddy/README.md
  - ../../.github/workflows/godaddy-public-site.yml
  - ../../apps/site/README.md
[/KFM_META_BLOCK_V2] -->

# Connect kansasfrontiermatrix.com to GoDaddy web hosting

> **Scope update — 2026-10-14:** The owner selected the existing GoDaddy Node.js
> app `q9r9beo47t` to host the full Explorer. Its dashboard shows the published
> Node composition at `f44ce0cf0d72c019252bb93efc4f138f671107de`. The cPanel/front-door
> topology below records the earlier plan; it is not the current Node deployment
> procedure and must not replace that app with monorepo `main`. The separate
> [hosted capture runbook](godaddy-hosted-capture.md) covers the proposed scheduler
> and its pending gates. This update performs no DNS or hosting change.

This runbook connects the repository to GoDaddy so that:

| Address | Serves | Hosted by |
|---|---|---|
| `kansasfrontiermatrix.com` | Public front door built from [`apps/public-site/`](../../apps/public-site/README.md) | GoDaddy web hosting (cPanel / Apache) |
| `www.kansasfrontiermatrix.com` | 301 redirect to the apex | GoDaddy web hosting |
| `explorer.kansasfrontiermatrix.com` | The KFM Explorer (owner-private preview) | ChatGPT Sites, unchanged |
| `kansasfrontiermatrix.com/explorer` | 302 redirect to the Explorer | GoDaddy web hosting |

The front door is static HTML, CSS and artwork. It is rebuilt from the repository on every change to its inputs, so the feature list, counts and build commit stay current with `main`. GoDaddy shared hosting cannot run the Explorer itself, which is a Cloudflare Worker with D1, R2 and server routes; the Explorer stays on ChatGPT Sites.

> [!IMPORTANT]
> Deploying the front door is not a KFM data release. The page restates repository facts at the built commit; it does not admit sources, release datasets or change the Explorer's audience.

## Current DNS (recorded 2026-10-12)

The domain's nameservers are GoDaddy's (`ns55.domaincontrol.com`, `ns56.domaincontrol.com`), so all changes below are made in **GoDaddy → My Products → kansasfrontiermatrix.com → DNS**.

| Type | Name | Value | Purpose today |
|---|---|---|---|
| A | `@` | `162.159.143.30` | ChatGPT Sites (Explorer) |
| A | `@` | `172.66.3.26` | ChatGPT Sites (Explorer) |
| CNAME | `www` | `custom-domains.chatgpt.site` | ChatGPT Sites (Explorer) |
| CNAME | `_acme-challenge` | `kansasfrontiermatrix.com.a2a5947319618a50.dcv.cloudflare.com` | Certificate validation for the Sites custom domain |
| TXT | `_cf-custom-hostname` | `63efc09c-…` | Sites custom-hostname ownership |
| TXT | `@` | `v=spf1 include:secureserver.net ~all` | GoDaddy email SPF — **keep** |

Today both apex and `www` return HTTP 401 to the public because the Explorer is owner-only.

## 1. Prepare GoDaddy hosting

1. In GoDaddy, open the **Web Hosting** plan and attach `kansasfrontiermatrix.com` as the primary domain (or as an addon domain). Note its **document root**: `public_html` for a primary domain, or a folder such as `public_html/kansasfrontiermatrix.com` for an addon.
2. Open **cPanel** and record from the right-hand **General Information** panel:
   - the **Shared IP Address** (used for the apex `A` record);
   - the **server host name** (used as `GODADDY_HOST`);
   - the cPanel **user name** (used as `GODADDY_USER`).
3. Turn on **SSH access** (GoDaddy dashboard → Hosting → Settings → Server → SSH access). Then in cPanel → **SSH Access → Manage SSH Keys**:
   - generate a new key or import a public key you created with `ssh-keygen -t ed25519 -C kfm-deploy -f kfm-deploy`;
   - **Authorize** it.
   Keep the private key for the GitHub secret below. If SSH is unavailable on your plan, use FTPS instead (cPanel → **FTP Accounts**, create an account limited to the document root).
4. Record the server's SSH host key so the deploy pins it:

   ```bash
   ssh-keyscan -p 22 YOUR-CPANEL-HOST
   ```

   Compare a fingerprint (`ssh-keyscan -p 22 YOUR-CPANEL-HOST | ssh-keygen -lf -`) with the one shown on your first interactive login before you trust it.
5. If the document root holds GoDaddy's default placeholder or an older site, download a backup through cPanel → **File Manager** first.

## 2. Configure GitHub

In **GitHub → Settings → Environments**, create an environment named **`godaddy-production`**. Under **Deployment branches and tags**, choose **Selected branches and tags** and allow only `main`. This is required, not optional: it keeps the hosting credentials away from any other branch even if the workflow file is edited there. The workflow also refuses to deploy from any ref but `main`. Optionally add yourself as a required reviewer. Then add the following to that environment.

To create the environment with the `main`-only policy from a terminal:

```bash
gh api -X PUT repos/bartytime4life/Kansas-Frontier-Matrix/environments/godaddy-production --input - <<<'{"deployment_branch_policy":{"protected_branches":false,"custom_branch_policies":true}}'
```

```bash
gh api -X POST repos/bartytime4life/Kansas-Frontier-Matrix/environments/godaddy-production/deployment-branch-policies -f name=main -f type=branch
```

**Environment secrets**

| Secret | Value |
|---|---|
| `GODADDY_HOST` | cPanel server host name |
| `GODADDY_USER` | cPanel user name (or the FTP account for FTPS) |
| `GODADDY_SSH_KEY` | Private key text authorized in cPanel (SFTP; preferred) |
| `GODADDY_KNOWN_HOSTS` | Output of `ssh-keyscan` from step 1.4 (SFTP only) |
| `GODADDY_PASSWORD` | Only when not using a key, or for FTPS |

**Repository variables** (Settings → Secrets and variables → Actions → Variables)

| Variable | Value | Default |
|---|---|---|
| `GODADDY_DEPLOY_ENABLED` | `true` to allow deploys; anything else keeps them off | off |
| `GODADDY_REMOTE_DIR` | Document root from step 1.1, relative to the home directory | `public_html` |
| `GODADDY_PROTOCOL` | `sftp` or `ftps` | `sftp` |
| `GODADDY_PORT` | Only if not the default | 22 / 21 |
| `GODADDY_DELETE` | `true` to delete remote files not in the bundle on every deploy | `false` |
| `KFM_SITE_ORIGIN` | Canonical public origin | `https://kansasfrontiermatrix.com` |
| `KFM_EXPLORER_URL` | Explorer address; set to `https://explorer.kansasfrontiermatrix.com` after step 4 | the stable `*.chatgpt.site` address |

Secrets live only in the `godaddy-production` environment and are passed to the single deploy step; nothing is written to the repository.

Before enabling deployments, inspect the environment's **complete** policy list:

```bash
gh api repos/bartytime4life/Kansas-Frontier-Matrix/environments/godaddy-production
gh api --paginate repos/bartytime4life/Kansas-Frontier-Matrix/environments/godaddy-production/deployment-branch-policies
```

Require `custom_branch_policies: true`, `protected_branches: false`, and exactly
one allowed policy: branch `main`. Remove extra branch patterns and all tag
policies before enabling deployments. Protect `main` against direct unreviewed
changes to the workflow, transfer script, and site inputs. Keep hosting secrets
in this environment only; repository or organization copies would bypass its
ref restrictions. These are mandatory operator checks, not state verified by
the repository tests. Leave `GODADDY_DEPLOY_ENABLED` unset or `false` until those
checks and separate production authorization are complete. The workflow also
requires GitHub to report `main` as protected (`github.ref_protected`). A credential-bearing
dry run needs the same protections as an upload.

## 3. First deploy (before DNS changes)

The site can be uploaded and checked before any DNS moves.

1. Actions → **godaddy-public-site** → **Run workflow** with **dry_run** checked. The log lists every file that would be uploaded.
2. Run again without dry run. The final step, *Verify the live site serves this commit*, will fail until DNS points at GoDaddy. That is expected on this first run.
3. Preview the uploaded site before DNS moves by sending the real host name to the GoDaddy IP. Any other host name, such as a cPanel preview domain, redirects to `kansasfrontiermatrix.com` by design. Until AutoSSL runs after the DNS move, the certificate won't match, so `-k` is needed for this check only:

   ```bash
   curl -skI --resolve kansasfrontiermatrix.com:443:SHARED-IP https://kansasfrontiermatrix.com/
   ```

## 4. Move the Explorer to `explorer.kansasfrontiermatrix.com`

Do this first so the Explorer is never unreachable.

1. In ChatGPT Sites, open the Explorer site's domain settings and **add the custom domain** `explorer.kansasfrontiermatrix.com`. Sites shows the records it needs.
2. In GoDaddy DNS, add what Sites asks for. Typically that is:

   | Type | Name | Value |
   |---|---|---|
   | CNAME | `explorer` | `custom-domains.chatgpt.site` |
   | TXT / CNAME | names Sites gives for `explorer` validation | values Sites gives |

3. Wait until Sites reports the domain active and `https://explorer.kansasfrontiermatrix.com` loads (owner sign-in still applies).
4. Set the repository variable `KFM_EXPLORER_URL` to `https://explorer.kansasfrontiermatrix.com`.

## 5. Point the apex and `www` at GoDaddy

In GoDaddy DNS:

1. **Delete** both apex `A` records (`162.159.143.30`, `172.66.3.26`).
2. **Add** `A @ → <Shared IP Address from step 1.2>`, TTL 600 (1 hour also works).
3. **Edit** `CNAME www` to point to `@` (GoDaddy's usual default), or to `kansasfrontiermatrix.com`.
4. **Delete** the apex `_acme-challenge` CNAME and the `_cf-custom-hostname` TXT. They belong to the old Sites apex certificate and can block GoDaddy's certificate issuance. Leave any new `explorer` validation records from step 4 in place.
5. **Keep** the SPF `TXT @` record and any MX records.
6. Remove `kansasfrontiermatrix.com` and `www` from the ChatGPT Sites domain list so Sites stops expecting them.

Then:

- Check propagation: `dig +short kansasfrontiermatrix.com A` should return only the GoDaddy IP.
- In cPanel → **SSL/TLS Status**, run **AutoSSL** for `kansasfrontiermatrix.com` and `www.kansasfrontiermatrix.com`. The bundle's `.htaccess` lets `/.well-known/acme-challenge/` through, and deploys never delete those paths.
- Re-run the workflow (or push to `main`). The verify step now passes when `https://kansasfrontiermatrix.com/kfm-site.json` reports the deployed commit.

## 6. Verify

```bash
curl -sI https://kansasfrontiermatrix.com/
```

Expect `200`, plus `strict-transport-security` and `content-security-policy` headers.

```bash
curl -sI https://www.kansasfrontiermatrix.com/
```

Expect a `301` to `https://kansasfrontiermatrix.com/`.

```bash
curl -s https://kansasfrontiermatrix.com/kfm-site.json
```

Expect the `commit` field to match the deployed `main` commit.

Also confirm that `/explorer` redirects to the Explorer, that a missing page shows the KFM 404, and that `/.well-known/security.txt` is served.

## What the repository now provides to the site and app

| Path | Content | Consumer |
|---|---|---|
| `/` | Front page: purpose, Explorer walkthrough, the live feature registry by status, data themes, trust model, contribution links | Visitors, search engines |
| `/features.json` | Every Explorer feature with status, outcome and limits from `apps/site/source/app/site-features.ts` (CORS-open) | The Explorer, other apps, partners |
| `/kfm-site.json` | Build manifest: commit, build time, counts, endpoint list (CORS-open) | Deploy verification, monitoring, apps |
| `/explorer` | Redirect to the Explorer | Short link for print and talks |
| `/sitemap.xml`, `/robots.txt` | Search indexing | Search engines |
| `/.well-known/security.txt` | Points to the repository's private vulnerability reporting | Security researchers |

## Rollback

- **Content:** revert the offending commit on `main` through a reviewed pull request. The merge deploys the reverted bundle. Deploys never run from other branches or tags, so a rollback always goes through `main`.
- Revert only the affected content paths when practical. Retain the deployment
  gate, environment protections, transport checks, and hosting security rules;
  never roll back by dispatching an old branch/tag or checking out arbitrary
  rollback code inside the credential-bearing job. Build and test the revert
  before review and merge. With deployments disabled, merging a revert remains
  a code correction and does not upload anything.
- **Turn deploys off:** set `GODADDY_DEPLOY_ENABLED` to `false`. The site keeps serving the last upload.
- **DNS:** restore the two apex `A` records and the `www` CNAME from the [Current DNS](#current-dns-recorded-2026-10-12) table, re-add the apex custom domain in ChatGPT Sites, and let it re-issue its validation records. Allow for the record TTL to expire.

## Notes

- Deploys never remove `.well-known/acme-challenge/`, `.well-known/pki-validation/`, `cgi-bin/`, `.user.ini` or `.htpasswd` on the server. With `GODADDY_DELETE` off (the default), they also leave any other existing remote file in place.
- HSTS is sent without `includeSubDomains`, so it cannot affect other subdomains.
- The build is reproducible: it stamps the commit time, not the wall-clock time.
- HTTPS redirects trust Apache's TLS state, not caller forwarding headers.
  A future TLS-terminating proxy requires a separately reviewed trusted-proxy
  configuration before use.
- Mutable CSS, artwork, favicon, and social-preview paths require cache
  revalidation; pages also retain their content-hash asset queries.
