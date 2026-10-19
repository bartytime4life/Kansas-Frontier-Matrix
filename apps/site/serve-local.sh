#!/usr/bin/env bash
set -euo pipefail

site_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/source" && pwd)"
cd "$site_dir"

# Every serving path must reject caller-supplied hosted identity headers. Check
# direct-runtime eligibility before Wrangler can load local secrets or write D1.
host="${SITE_HOST:-127.0.0.1}"
port="${SITE_PORT:-4173}"
if [[ "$host" != 127.0.0.1 ]]; then
  printf 'SITE_HOST must be 127.0.0.1 for the protected local runtime.\n' >&2
  exit 2
fi
SITE_PORT="$port" node --input-type=module -e '
import { assertNodeVersion, assertNoLocalSecretFiles, parseArguments } from "./scripts/serve-local-worker.mjs";
assertNodeVersion();
assertNoLocalSecretFiles(process.cwd());
parseArguments(["--state", ".", "--port", process.env.SITE_PORT]);
'

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

# Later journal entries back the governed water, weather, soil, storm events and earthquakes,
# Kansas knowledge and crop CASMA routes. They are additive, so reapply them on every launch; refuse any
# entry whose statements are not all CREATE ... IF NOT EXISTS.
# Published archive and connection migrations stay immutable; a hash-bound local
# replay adds only IF NOT EXISTS so fresh and repeated local starts are safe.
migration_workspace="$(mktemp -d)"
trap 'rm -rf "$migration_workspace"' EXIT
additive_migrations="$(node -e '
const fs = require("fs");
const journal = JSON.parse(fs.readFileSync("drizzle/meta/_journal.json", "utf8"));
// A migration file missing from the hand-edited journal would be skipped here
// and wherever else the journal drives migration; fail instead.
const listed = journal.entries.map(({ tag }) => `${tag}.sql`);
const present = fs.readdirSync("drizzle").filter((name) => name.endsWith(".sql"));
const unlisted = present.filter((name) => !listed.includes(name));
const missing = listed.filter((name) => !present.includes(name));
// Check array order as written: consumers may apply entries in that order.
const misnumbered = journal.entries
  .filter(({ idx, tag }, position) => idx !== position || !tag.startsWith(`${String(idx).padStart(4, "0")}_`));
if (unlisted.length || missing.length || misnumbered.length) {
  process.stderr.write(`drizzle/*.sql and drizzle/meta/_journal.json disagree:${
    unlisted.length ? ` not in the journal: ${unlisted.join(", ")};` : ""}${
    missing.length ? ` listed but missing: ${missing.join(", ")};` : ""}${
    misnumbered.length ? ` out of sequence: ${misnumbered.map(({ tag }) => tag).join(", ")};` : ""
  } fix the journal before launching.\n`);
  process.exit(2);
}
for (const { idx, tag } of [...journal.entries].sort((a, b) => a.idx - b.idx)) {
  if (idx === 0) continue;
  let file = `drizzle/${tag}.sql`;
  const replayHashes = {
    "0005_daily_archive": "669ca0011a044c77479ea842c1fabd040f344a4d49826949a43fbd882f34801c",
    "0010_api_connections": "b020a360d8764b28dc2459a897bf43ff0311931166c66717e0bdd51337e8f8b8",
  };
  if (Object.hasOwn(replayHashes, tag)) {
    const original = fs.readFileSync(file, "utf8");
    const expected = replayHashes[tag];
    if (require("crypto").createHash("sha256").update(original).digest("hex") !== expected) {
      throw new Error(`Published migration ${tag} changed; review before local replay.`);
    }
    file = require("path").join(process.argv[1], `${tag}.sql`);
    fs.writeFileSync(file, original.replace(/CREATE (TABLE|INDEX) /g, "CREATE $1 IF NOT EXISTS "), { flag: "wx", mode: 0o600 });
  }
  const statements = fs.readFileSync(file, "utf8").replace(/^\s*--(?! *> *statement-breakpoint).*$/gm, "")
    .split(/--> *statement-breakpoint|;/).map((part) => part.trim()).filter(Boolean);
  if (!statements.length || statements.some((sql) => !/^CREATE\s+(?:TABLE|(?:UNIQUE\s+)?INDEX)\s+IF\s+NOT\s+EXISTS\s/i.test(sql))) {
    process.stderr.write(`${file} is not additive; apply it deliberately before launching.\n`);
    process.exit(2);
  }
  process.stdout.write(`${file}\n`);
}' "$migration_workspace")"

while IFS= read -r migration; do
  [[ -n "$migration" ]] || continue
  "$wrangler" d1 execute "$database" --local --config "$config" \
    --persist-to "$local_state" --file "$migration" >/dev/null
done <<<"$additive_migrations"
rm -rf "$migration_workspace"
trap - EXIT

node scripts/validate-subsurface-public.mjs dist/client

# Never fall back to raw Wrangler: it trusts the hosted identity headers that
# the direct runtime rejects before dispatching any application request.
mkdir -p "$local_state/v3/d1" "$local_state/v3/r2"
printf 'Starting the direct local Worker runtime on http://%s:%s\n' "$host" "$port" >&2
exec node scripts/serve-local-worker.mjs --state "$(realpath "$local_state")" --port "$port"
