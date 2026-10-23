// Opt-in diagnostic: instrument actual route GET calls with a synthetic provider.
// Never sends network traffic and is intentionally outside the ordinary test glob.
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { loadRoute, request, deferred, tick } from "./flowline-request-harness.mjs";

const baselinePath = process.argv[2];
const cases = [];
const original = globalThis.fetch;
try {
  for (const [variant, source] of [
    ...(baselinePath ? [["baseline", await readFile(baselinePath, "utf8")]] : []),
    ["candidate", await readFile("app/api/hydrology/flowlines/route.ts", "utf8")],
  ]) {
    for (const scenario of ["duplicate", "different-cells"]) {
      const GET = await loadRoute(source), gate = deferred();
      let calls = 0, active = 0, peak = 0;
      globalThis.fetch = async (url, { signal }) => {
        assert.equal(new URL(url).hostname, "3dhp.nationalmap.gov");
        assert.equal(signal.aborted, false);
        calls++; active++; peak = Math.max(peak, active);
        try { await gate.promise; return Response.json({ features: [] }); }
        finally { active--; }
      };
      const queries = Array.from({ length: 24 }, (_, i) => scenario === "duplicate" ? undefined : "cell=" + [-101 + (i % 12) * .25, 37 + Math.floor(i / 12) * .25].join(","));
      const pending = queries.map(q => GET(request(q)));
      await tick(); const startedBeforeRelease = calls; gate.resolve();
      const responses = await Promise.all(pending); await tick();
      const firstWaveCalls = calls;
      const statuses = responses.reduce((counts, r) => ({ ...counts, [r.status]: (counts[r.status] ?? 0) + 1 }), {});
      const bodies = await Promise.all(responses.filter(r => r.ok).map(r => r.text()));
      if (scenario === "duplicate") {
        if (variant === "candidate") assert.equal(new Set(bodies).size, 1);
        const replay = await Promise.all(queries.map(q => GET(request(q))));
        assert.ok(replay.every(r => r.status === 200));
      }
      cases.push({ variant, scenario, clients: 24, startedBeforeRelease, firstWaveCalls, peakUpstreamReads: peak, statuses, replayAdditionalCalls: calls - firstWaveCalls,
        routeSha256: createHash("sha256").update(source).digest("hex") });
    }
  }
} finally { globalThis.fetch = original; }
console.log(JSON.stringify({ profile: "kfm.synthetic-flowline-capacity/v1", node: process.version,
  poolSha256: createHash("sha256").update(await readFile("app/flowline-request-pool.ts")).digest("hex"),
  limitation: "Synthetic in-process route instances and gated fetch instrumentation only; no provider or production traffic, real latency, host capacity or cross-instance guarantee.", cases }, null, 2));
