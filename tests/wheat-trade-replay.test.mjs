import assert from "node:assert/strict";
import test from "node:test";
import { compareSpreads, evidenceByDate, replays } from "../app/science/wheat-trade/model.mjs";

test("Panama replay gates publication and preserves the amendment's distinct start date", () => {
  const replay = replays.find(({ id }) => id === "panama-2023");
  assert.deepEqual(evidenceByDate(replay, "2023-10-29"), []);
  assert.deepEqual(
    evidenceByDate(replay, "2023-10-30").map(({ kind, effective }) => [kind, effective]),
    [["Official restriction", "2023-11-03"]],
  );
  assert.equal(evidenceByDate(replay, "2023-12-14").length, 3);
  assert.equal(evidenceByDate(replay, "2023-12-15").at(-1).effective, "2024-01-16");
});

test("wheat comparison report and observation dates retain publication order", () => {
  for (const replay of replays) {
    assert.deepEqual([...replay.dates].sort(), replay.dates);
    assert.deepEqual(replay.entries.map(({ published }) => published), replay.entries.map(({ published }) => published).sort());
    for (const { observations, published } of replay.entries) {
      if (!observations) continue;
      assert.equal(observations.length, 2);
      assert.ok(observations[0] < observations[1] && observations[1] < published);
    }
  }

  const [replay] = replays;
  assert.deepEqual(evidenceByDate(replay, "2026-11-20").map(({ published }) => published), ["2026-11-19"]);
});

test("signed spread changes are exact cents and unavailable values do not become zero", () => {
  assert.equal(compareSpreads("-2.03", "-1.96"), 7);
  assert.equal(compareSpreads("-1.96", "-2.02"), -6);
  assert.equal(compareSpreads("0", "-0.00"), 0);
  assert.equal(compareSpreads(" -1 ", "+1.0"), 200);
  for (const invalid of ["", "nq", "n/a", "-", "1e1", "2.111", "Infinity", "$1.09"]) {
    assert.equal(compareSpreads(invalid, "0"), null, invalid);
  }
});
