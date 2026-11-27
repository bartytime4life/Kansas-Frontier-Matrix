import assert from "node:assert/strict";
import { readFile, access } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import ts from "typescript";

const modules = new Map();
async function moduleUrl(file) {
  file = path.resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, "utf8"), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) js = js.replace(match[0], `from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file), match[1]) + ".ts"))}`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  modules.set(file, url); return url;
}

test("the sitemap lists only public entry pages that exist, including every guide", async () => {
  const sitemap = await import(await moduleUrl("app/sitemap.ts"));
  const guides = await import(await moduleUrl("app/landing-guides.ts"));
  const identity = await import(await moduleUrl("app/site-identity.ts"));
  const entries = sitemap.default();
  assert.equal(entries.length, sitemap.SITEMAP_PATHS.length);
  assert.ok(sitemap.SITEMAP_PATHS.includes("/labs/daily-air-quality"));
  assert.ok(sitemap.SITEMAP_PATHS.includes("/labs/sunlight-and-sky"));
  for (const guide of guides.LANDING_GUIDES) assert.ok(sitemap.SITEMAP_PATHS.includes(`/explore/${guide.slug}`), guide.slug);
  for (const pathName of sitemap.SITEMAP_PATHS) {
    assert.doesNotMatch(pathName, /^\/(api|data|acquisition|downloads|stewards|governed)(\/|$)/, "no owner or API route");
    await access(`app${pathName === "/" ? "" : pathName}/page.tsx`);
  }
  for (const entry of entries) assert.ok(entry.url.startsWith(identity.PUBLIC_SITE_ORIGIN));
});

test("robots keeps API and owner workspaces out of indexes and points at the sitemap", async () => {
  const robots = await import(await moduleUrl("app/robots.ts"));
  const identity = await import(await moduleUrl("app/site-identity.ts"));
  const config = robots.default();
  assert.deepEqual(config.rules[0].disallow, ["/api/", "/data/", "/acquisition", "/downloads", "/stewards", "/governed/"]);
  assert.equal(config.sitemap, `${identity.PUBLIC_SITE_ORIGIN}/sitemap.xml`);
});

test("not-found, About and the layer panel link the map guides", async () => {
  assert.match(await readFile("app/not-found.tsx", "utf8"), /\["\/explore", "Map guides"/);
  assert.match(await readFile("app/about/page.tsx", "utf8"), /<Link href="\/explore">Map guides<\/Link>/);
  assert.match(await readFile("app/page.tsx", "utf8"), /<Link href="\/explore">Map guides →<\/Link>/);
  assert.match(await readFile("app/page.tsx", "utf8"), /<Link href="\/labs\/daily-air-quality">Daily air quality →<\/Link>/);
  assert.match(await readFile("app/page.tsx", "utf8"), /<Link href="\/labs\/sunlight-and-sky">Sunlight &amp; sky →<\/Link>/);
});
