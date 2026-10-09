import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import test from "node:test";

const read = (path) => readFile(new URL(`../${path}`, import.meta.url), "utf8");
const sqlite = await import("node:sqlite").catch(() => null);

async function migratedDatabase() {
  const db = new sqlite.DatabaseSync(":memory:");
  const files = (await readdir(new URL("../drizzle/", import.meta.url))).filter((name) => name.endsWith(".sql")).sort();
  for (const file of files) {
    for (const statement of (await read(`drizzle/${file}`)).split("--> statement-breakpoint").map((part) => part.trim()).filter(Boolean)) db.exec(statement);
  }
  return db;
}

test("submission list indexes are additive and journaled", async () => {
  const sql = await read("drizzle/0004_submission_list_order.sql");
  const statements = sql.replace(/^\s*--(?! *> *statement-breakpoint).*$/gm, "").split(/--> *statement-breakpoint|;/).map((part) => part.trim()).filter(Boolean);
  assert.equal(statements.length, 2);
  for (const statement of statements) assert.match(statement, /^CREATE INDEX IF NOT EXISTS idx_submissions_\w+ ON data_submissions \(/);
  const journal = JSON.parse(await read("drizzle/meta/_journal.json"));
  assert.deepEqual(journal.entries.at(-1), { idx: 4, version: "6", when: 1790797081529, tag: "0004_submission_list_order", breakpoints: true });
  journal.entries.forEach((entry, position) => assert.equal(entry.idx, position));
});

test("submission keyset pages in index order without gaps or repeats", { skip: !sqlite && "node:sqlite unavailable" }, async () => {
  const route = await read("app/api/data-submissions/route.ts");
  assert.match(route, /"\(created_at, id\) < \(\?, \?\)"/, "row-value keyset predicate");
  assert.match(route, /\[createdAt, id\]/);
  assert.match(route, /ORDER BY created_at DESC, id DESC LIMIT 31/);

  const db = await migratedDatabase();
  const insert = db.prepare("INSERT INTO data_submissions (id, owner_key, owner_name, title, source_id, source_url, description, license, sensitivity, start_date, end_date, file_name, file_bytes, file_sha256, object_key, status, version, created_at, updated_at) VALUES (?, ?, 'n', 't', 's', 'https://example.test/', 'd', 'l', 'public', '2020-01-01', '2020-01-02', 'f.csv', 1, 'h', ?, 'submitted', 1, ?, ?)");
  const ids = [];
  for (let index = 0; index < 75; index += 1) {
    // Groups of three share a timestamp so the id tie-break is exercised.
    const createdAt = new Date(Date.UTC(2026, 9, 1, 0, Math.floor(index / 3))).toISOString();
    const id = `00000000-0000-4000-8000-${String(index).padStart(12, "0")}`;
    insert.run(id, index % 2 ? "owner-a" : "owner-b", `k/${id}`, createdAt, createdAt);
    ids.push({ id, createdAt, owner: index % 2 ? "owner-a" : "owner-b" });
  }

  for (const owner of [null, "owner-a"]) {
    const expected = ids.filter((row) => !owner || row.owner === owner).sort((a, b) => (b.createdAt.localeCompare(a.createdAt) || b.id.localeCompare(a.id))).map((row) => row.id);
    const seen = [];
    let cursor = null;
    for (let page = 0; page < 10; page += 1) {
      const predicates = [owner ? "owner_key = ?" : "1=1", ...(cursor ? ["(created_at, id) < (?, ?)"] : [])];
      const args = [...(owner ? [owner] : []), ...(cursor ?? [])];
      const query = `SELECT id, created_at AS createdAt FROM data_submissions WHERE ${predicates.join(" AND ")} ORDER BY created_at DESC, id DESC LIMIT 31`;
      const plan = db.prepare(`EXPLAIN QUERY PLAN ${query}`).all(...args).map((row) => row.detail).join(" | ");
      assert.match(plan, owner ? /idx_submissions_owner_created_id/ : /idx_submissions_created_id/);
      assert.doesNotMatch(plan, /TEMP B-TREE/, "no sort step");
      const rows = db.prepare(query).all(...args);
      const items = rows.slice(0, 30);
      seen.push(...items.map((row) => row.id));
      if (rows.length <= 30) break;
      cursor = [items.at(-1).createdAt, items.at(-1).id];
    }
    assert.deepEqual(seen, expected);
  }
});

test("unknown and withheld paths share one accessible 404", async () => {
  const notFound = await read("app/not-found.tsx");
  assert.match(notFound, /<main className="kfm-not-found">/);
  assert.equal((notFound.match(/<h1>/g) ?? []).length, 1);
  assert.match(notFound, /<nav aria-label="Where to go next">/);
  const rendered = notFound.slice(notFound.indexOf("return ("));
  assert.doesNotMatch(rendered, /owner|sign in|signed out/i, "the page does not reveal why a path is withheld");
  for (const [, href] of notFound.matchAll(/\["(\/[^"]*)",/g)) {
    const page = href === "/" ? "app/page.tsx" : `app${href}/page.tsx`;
    await assert.doesNotReject(read(page), `${href} exists`);
  }
  const theme = await read("app/explorer-theme.css");
  assert.match(theme, /\.kfm-not-found \{/);
  assert.match(theme, /@media \(prefers-reduced-motion: reduce\)[\s\S]*\.kfm-not-found-card \{ animation: none; \}/);
});

test("baseline headers cover the root and never forbid platform framing", async () => {
  const config = await read("next.config.ts");
  assert.match(config, /\{ source: "\/", headers \}, \{ source: "\/:path\*", headers \}/);
  assert.match(config, /"X-Content-Type-Options", value: "nosniff"/);
  assert.match(config, /"Referrer-Policy", value: "strict-origin-when-cross-origin"/);
  assert.match(config, /geolocation=\(self\)/, "the locate control keeps working");
  assert.doesNotMatch(config, /X-Frame-Options|frame-ancestors/);
});

test("audit fixes keep landmarks, roles and in-text links valid", async () => {
  const page = await read("app/page.tsx");
  const about = await read("app/about/page.tsx");
  for (const source of [page, about]) assert.doesNotMatch(source, /className="brand-lockup" aria-label=/, "no aria-label on a role-less div");
  assert.match(page, /<div className="timeline-frame-status" role="status" aria-live="polite" aria-atomic="true">/);
  assert.doesNotMatch(page, /<header role="status"/);
  assert.match(page, /<section ref=\{qwenPanelRef\} id="qwen-map-panel" className="qwen-panel" role="dialog"/);
  assert.match(page, /className="qwen-messages" aria-live="polite" aria-label="Qwen conversation" role="log" tabIndex=\{0\}/);
  assert.match(await read("app/globals.css"), /\.timeline-detail > section > :is\(header, \.timeline-frame-status\) \{/);
  assert.match(await read("app/observatory/sources/page.tsx"), /return <main className="event-research">/);

  const downloads = await read("app/download-library.tsx");
  const summary = downloads.slice(downloads.indexOf("<dl className={s.librarySummary}"), downloads.indexOf("</dl>"));
  assert.doesNotMatch(summary, /<small>/, "dl groups hold only dt and dd");
  assert.equal((summary.match(/<dd className=\{s\.summaryNote\}>/g) ?? []).length, 2);

  assert.match(await read("app/acquisition/workspace.module.css"), /\.page :is\(p,li,dd,td\)>a\{text-decoration:underline\}/);
  assert.match(await read("app/data/workspace.module.css"), /\.page :is\(p,li,dd,section\)>a:not\(\.download,\.brand\)\{text-decoration:underline\}/);
  assert.match(await read("app/downloads/workspace.module.css"), /\.page :is\(p,li,dd,td\)>a:not\(\.primaryLink\) \{ text-decoration:underline; \}/);
});
