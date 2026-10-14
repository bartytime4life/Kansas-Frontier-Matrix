import assert from "node:assert/strict";
import test from "node:test";

import {
  KNOWN_OVER_BLOCKS,
  QWEN_QUESTION_GATE_CORPUS,
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

test("over-blocking in the corpus is exactly the documented list", () => {
  const report = evaluateQuestionGate();
  assert.deepEqual([...report.overBlocked].sort(), Object.keys(KNOWN_OVER_BLOCKS).sort());
  for (const reason of Object.values(KNOWN_OVER_BLOCKS)) assert.ok(reason.length > 20);
  assert.ok(report.overBlockRate <= 0.05, `over-block rate ${report.overBlockRate}`);
});

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
