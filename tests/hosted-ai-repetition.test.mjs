import assert from "node:assert/strict";
import test from "node:test";
import { hasRepeatedPhrase } from "../server/hosted-ai.mjs";

const santaFe = "The Santa Fe Trail was a commercial route between Missouri and Santa Fe. Traders used the Santa Fe Trail from 1821, "
  + "and Council Grove became a key stop. Railroads replaced the Santa Fe Trail by 1880.";

test("a correct answer may repeat a proper name or the asked subject", () => {
  assert.equal(hasRepeatedPhrase(santaFe), false, "a capitalized name repeated three times is not a loop");
  assert.equal(hasRepeatedPhrase(santaFe, "What was the Santa Fe Trail?"), false);
  const pivot = "Center pivot irrigation works by rotating pipes. center pivot irrigation works well on flat land, and center pivot irrigation works with sprinklers.";
  assert.equal(hasRepeatedPhrase(pivot, "how center pivot irrigation works"), false, "the subject the visitor asked about may recur");
  assert.equal(hasRepeatedPhrase(pivot), true, "the same lowercase phrase without that context still counts");
});

test("degenerate loops are still rejected", () => {
  assert.equal(hasRepeatedPhrase("I cannot answer that. I cannot answer that. I cannot answer that."), true);
  assert.equal(hasRepeatedPhrase("and so on and so on and so on and so on"), true);
  const nameLoop = Array(5).fill("the Santa Fe Trail").join(" and ");
  assert.equal(hasRepeatedPhrase(nameLoop), true, "a name repeated five times is a loop");
  assert.equal(hasRepeatedPhrase(nameLoop, "What was the Santa Fe Trail?"), true);
  assert.equal(hasRepeatedPhrase("A short distinct answer."), false);
});
