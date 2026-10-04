#!/usr/bin/env bash
set -euo pipefail

site_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/source" && pwd)"
cd "$site_dir"

if [[ ! -x node_modules/.bin/wrangler || ! -f dist/server/wrangler.json ]]; then
  printf 'Install and build the Site first: cd apps/site/source && npm run install:ci && npm run build\n' >&2
  exit 1
fi

local_state="${SITE_STATE_DIR:-$site_dir/.wrangler/local-state}"
export XDG_CONFIG_HOME="$site_dir/.wrangler/config"
export WRANGLER_LOG_PATH="$site_dir/.wrangler/wrangler.log"
export WRANGLER_WRITE_LOGS=false
export MINIFLARE_REGISTRY_PATH="$site_dir/.wrangler/registry"
mkdir -p "$XDG_CONFIG_HOME" "$local_state"

wrangler="$site_dir/node_modules/.bin/wrangler"
config=dist/server/wrangler.json
database=site-creator-d1

schema_count="$("$wrangler" d1 execute "$database" --local --config "$config" \
  --persist-to "$local_state" \
  --command "SELECT COUNT(*) AS count FROM sqlite_master WHERE type = 'table' AND name IN ('data_submissions', 'data_submission_reviews')" \
  --json | node -e 'const result = JSON.parse(require("fs").readFileSync(0, "utf8")); const count = result[0]?.results?.[0]?.count; if (!Number.isInteger(count)) process.exit(2); process.stdout.write(String(count));')"

if [[ "$schema_count" == 0 ]]; then
  "$wrangler" d1 execute "$database" --local --config "$config" \
    --persist-to "$local_state" --file drizzle/0000_tired_swordsman.sql >/dev/null
elif [[ "$schema_count" != 2 ]]; then
  printf 'Local D1 schema is incomplete; inspect %s before continuing.\n' "$local_state" >&2
  exit 1
fi

# Later journal entries back the governed water, Kansas knowledge and crop
# CASMA routes. They are additive, so reapply them on every launch; refuse any
# entry whose statements are not all CREATE ... IF NOT EXISTS.
additive_migrations="$(node -e '
const fs = require("fs");
const journal = JSON.parse(fs.readFileSync("drizzle/meta/_journal.json", "utf8"));
for (const { idx, tag } of [...journal.entries].sort((a, b) => a.idx - b.idx)) {
  if (idx === 0) continue;
  const file = `drizzle/${tag}.sql`;
  const statements = fs.readFileSync(file, "utf8").replace(/^\s*--(?! *> *statement-breakpoint).*$/gm, "")
    .split(/--> *statement-breakpoint|;/).map((part) => part.trim()).filter(Boolean);
  if (!statements.length || statements.some((sql) => !/^CREATE\s+(?:TABLE|(?:UNIQUE\s+)?INDEX)\s+IF\s+NOT\s+EXISTS\s/i.test(sql))) {
    process.stderr.write(`${file} is not additive; apply it deliberately before launching.\n`);
    process.exit(2);
  }
  process.stdout.write(`${file}\n`);
}')"

while IFS= read -r migration; do
  [[ -n "$migration" ]] || continue
  "$wrangler" d1 execute "$database" --local --config "$config" \
    --persist-to "$local_state" --file "$migration" >/dev/null
done <<<"$additive_migrations"

exec "$wrangler" dev --config "$config" --local \
  --persist-to "$local_state" --ip "${SITE_HOST:-127.0.0.1}" \
  --port "${SITE_PORT:-4173}"
