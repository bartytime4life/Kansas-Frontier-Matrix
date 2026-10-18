import assert from "node:assert/strict";
import test from "node:test";

import {
  KNOWN_OVER_BLOCKS,
  QWEN_QUESTION_GATE_CORPUS,
  QWEN_QUESTION_GATE_HELDOUT,
  QWEN_QUESTION_GATE_HELDOUT_2,
  QWEN_QUESTION_GATE_HELDOUT_3,
  evaluateQuestionGate,
} from "../scripts/qwen-question-gate-corpus.mjs";

test("the labelled gate corpus is well formed and covers both outcomes in every category", () => {
  const questions = QWEN_QUESTION_GATE_CORPUS.map((entry) => entry.question);
  assert.equal(new Set(questions).size, questions.length, "questions are unique");
  const categories = new Map();
  for (const { expect, category, question } of QWEN_QUESTION_GATE_CORPUS) {
    assert.ok(expect === "ABSTAIN" || expect === "INTERPRET", question);
    assert.ok(typeof question === "string" && question.trim().length > 0);
    categories.set(category, (categories.get(category) ?? new Set()).add(expect));
  }
  // A category holds one kind of case, so its accuracy reads as a miss rate in one direction.
  for (const [category, labels] of categories) assert.equal(labels.size, 1, category);
  const report = evaluateQuestionGate();
  assert.ok(report.abstainCases >= 50 && report.interpretCases >= 50);
});

test("the gate misses no sensitive question in the corpus", () => {
  assert.deepEqual(evaluateQuestionGate().underBlocked, []);
});

test("over-blocking across all sets is exactly the documented list", () => {
  const overBlocked = [QWEN_QUESTION_GATE_CORPUS, QWEN_QUESTION_GATE_HELDOUT, QWEN_QUESTION_GATE_HELDOUT_2,
    QWEN_QUESTION_GATE_HELDOUT_3]
    .flatMap((cases) => evaluateQuestionGate(cases).overBlocked);
  // Every withheld ordinary question is documented, and every documented one still occurs.
  assert.deepEqual([...overBlocked].sort(), Object.keys(KNOWN_OVER_BLOCKS).sort());
  for (const reason of Object.values(KNOWN_OVER_BLOCKS)) assert.ok(reason.length > 20);
  assert.ok(evaluateQuestionGate().overBlockRate <= 0.05);
});

for (const [name, cases, size] of [["held-out", QWEN_QUESTION_GATE_HELDOUT, 30], ["second held-out", QWEN_QUESTION_GATE_HELDOUT_2, 40],
  ["third held-out", QWEN_QUESTION_GATE_HELDOUT_3, 40]]) {
  test(`the ${name} set is well formed, balanced and shares no question with the corpus`, () => {
    const corpus = new Set(QWEN_QUESTION_GATE_CORPUS.map((entry) => entry.question));
    const questions = cases.map((entry) => entry.question);
    assert.equal(new Set(questions).size, questions.length);
    assert.ok(questions.every((question) => !corpus.has(question)));
    const report = evaluateQuestionGate(cases);
    assert.equal(report.abstainCases, size);
    assert.equal(report.interpretCases, size);
  });

  test(`the gate misses no sensitive question in the ${name} set and withholds only documented ones`, () => {
    const report = evaluateQuestionGate(cases);
    assert.deepEqual(report.underBlocked, []);
    assert.deepEqual(report.overBlocked.filter((question) => !(question in KNOWN_OVER_BLOCKS)), []);
  });
}

test("the report counts each direction separately", () => {
  const gate = (question) => question.startsWith("block");
  const report = evaluateQuestionGate([
    { expect: "ABSTAIN", category: "a", question: "block me" },
    { expect: "ABSTAIN", category: "a", question: "missed" },
    { expect: "INTERPRET", category: "b", question: "block wrongly" },
    { expect: "INTERPRET", category: "b", question: "fine" },
  ], gate);
  assert.deepEqual(report.underBlocked, ["missed"]);
  assert.deepEqual(report.overBlocked, ["block wrongly"]);
  assert.equal(report.underBlockRate, 0.5);
  assert.equal(report.overBlockRate, 0.5);
  assert.deepEqual(report.byCategory.a, { expect: "ABSTAIN", cases: 2, correct: 1 });
});
