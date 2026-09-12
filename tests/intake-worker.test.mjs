import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { Miniflare, convertV4MiniflareOptions } from "miniflare";

test("private intake persists bytes and audit history, scopes reads, and serializes competing reviews", async () => {
  const root = path.resolve("dist/server");
  const files = readdirSync(root, { recursive: true }).filter((p) => p.endsWith(".js"));
  const modules = ["index.js", ...files.filter((p) => p !== "index.js")].map((p) => ({ type: "ESModule", path: path.join(root, p) }));
  const mf = new Miniflare(convertV4MiniflareOptions({ modules, modulesRoot: root, compatibilityDate: "2026-08-28", compatibilityFlags: ["nodejs_compat"], d1Databases: ["DB"], r2Buckets: ["BUCKET"], bindings: { KFM_STEWARD_EMAILS: "steward@example.test" } }));
  try {
    const db = await mf.getD1Database("DB");
    for (const file of readdirSync("drizzle").filter((p) => p.endsWith(".sql")).sort()) for (const sql of readFileSync(`drizzle/${file}`, "utf8").split("--> statement-breakpoint").map((v) => v.trim()).filter(Boolean)) await db.prepare(sql).run();
    const origin = (await mf.ready).origin;
    const headers = (email) => ({ "oai-authenticated-user-email": email, "oai-authenticated-user-id": `test-${email}`, Origin: origin });
    const request = async (url, email, init = {}) => {
      // Serialize browser-native FormData before crossing Miniflare's separate
      // fetch implementation; preserve the generated multipart boundary.
      const req = new Request(origin + url, { ...init, headers: { ...headers(email), ...init.headers } });
      return mf.dispatchFetch(req.url, { method: req.method, headers: Object.fromEntries(req.headers), body: ["GET","HEAD"].includes(req.method) ? undefined : await req.arrayBuffer() });
    };
    const form = (overrides = {}, file = "readings.csv") => {
      const data = new FormData();
      const fields = { title: "Kansas station readings", sourceId: "usgs-streamflow", sourceUrl: "https://waterdata.usgs.gov/", description: "Public historical stream observations with units and source dates.", license: "US public domain", sensitivity: "public", startDate: "1917-06-12", endDate: "1917-06-12", permission: "yes", ...overrides };
      for (const [k,v] of Object.entries(fields)) data.set(k,v);
      data.set("file", new File(["date,flow_cfs\n1917-06-12,12400\n"], file, { type: "text/csv" })); return data;
    };
    assert.equal((await mf.dispatchFetch(origin + "/api/data-submissions")).status, 401);
    assert.equal((await request("/api/data-submissions?scope=review", "contributor@example.test")).status, 403);
    assert.equal((await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form(), headers: { Origin: "https://other.test" } })).status, 403);
    const badFile = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form({}, "payload.html") });
    assert.equal(badFile.status, 400, await badFile.text());
    assert.equal((await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form({ sourceUrl: "javascript:alert(1)" }) })).status, 400);
    const upload = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form() });
    assert.equal(upload.status, 201, await upload.clone().text());
    const receipt = await upload.json(); assert.match(receipt.fileSha256, /^[0-9a-f]{64}$/);
    const id = receipt.id; const url = `/api/data-submissions/${id}`;
    assert.equal((await request(url, "other@example.test")).status, 404);
    assert.equal((await request(url + "?download=1", "other@example.test")).status, 404);
    const file = await request(url + "?download=1", "contributor@example.test");
    assert.equal(file.status, 200); assert.match(file.headers.get("content-disposition"), /^attachment;/); assert.equal(file.headers.get("cache-control"), "private, no-store");
    assert.equal(await file.text(), "date,flow_cfs\n1917-06-12,12400\n");
    const initial = await (await request(url, "steward@example.test")).json();
    assert.equal(initial.submission.version, 1); assert.equal(initial.reviews.length, 0); assert.equal(initial.canReview, true);
    assert.equal("objectKey" in initial.submission, false); assert.equal("ownerKey" in initial.submission, false);
    const patch = (version, status) => ({ method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ version, status, note: "Inspected source, public reuse terms, units and completeness." }) });
    assert.equal((await request(url, "contributor@example.test", patch(1,"accepted"))).status, 403);
    assert.equal((await request(url, "steward@example.test", patch(1,"accepted"))).status, 200);
    const reviewed = await (await request(url, "contributor@example.test")).json();
    assert.equal(reviewed.submission.status, "accepted"); assert.equal(reviewed.submission.version, 2); assert.equal(reviewed.reviews.length, 1);
    const competition = await Promise.all([request(url, "steward@example.test", patch(2,"under_review")), request(url, "steward@example.test", patch(2,"changes_requested"))]);
    assert.deepEqual(competition.map((r) => r.status).sort(), [200,409]);
    const final = await (await request(url, "contributor@example.test")).json(); assert.equal(final.reviews.length, 2); assert.equal(final.submission.version, 3);
    const mine = await (await request("/api/data-submissions", "contributor@example.test")).json(); assert.equal(mine.items.length, 1);
    const others = await (await request("/api/data-submissions", "other@example.test")).json(); assert.equal(others.items.length, 0);
    const queue = await (await request("/api/data-submissions?scope=review", "steward@example.test")).json(); assert.equal(queue.items.length, 1);
    const heldUpload = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: form({ license: "Unknown", sensitivity: "unknown" }) });
    const held = await heldUpload.json(); assert.equal(heldUpload.status,201);
    assert.equal((await request(`/api/data-submissions/${held.id}`, "steward@example.test", patch(1,"accepted"))).status,400);
    assert.equal((await request(`/api/data-submissions/${held.id}`, "steward@example.test", patch(1,"changes_requested"))).status,200);
    const larger = form(); larger.set("file", new File(["a,b\n".repeat(300_000)], "larger.csv", { type: "text/csv" }));
    const largeResponse = await request("/api/data-submissions", "contributor@example.test", { method: "POST", body: larger });
    assert.equal(largeResponse.status,201,await largeResponse.text());
  } finally { await mf.dispose(); }
});
