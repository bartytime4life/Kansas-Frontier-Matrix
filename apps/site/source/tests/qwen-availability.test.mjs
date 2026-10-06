import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import {
  QWEN_LOCAL_HEALTH_TIMEOUT_MS,
  localQwenAskEnvelope,
  localQwenHealthEnvelope,
} from "../scripts/qwen-local-contract.mjs";

const source = await readFile(new URL("../app/qwen-availability.ts", import.meta.url), "utf8");
const contractSource = await readFile(new URL("../scripts/qwen-local-contract.mjs", import.meta.url), "utf8");
const contractUrl = `data:text/javascript;base64,${Buffer.from(contractSource).toString("base64")}`;
const compiled = ts.transpileModule(source.replace("../scripts/qwen-local-contract.mjs", contractUrl), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const {
  QWEN_LOCAL_BROWSER_CONFIG,
  isQwenAskEnvelope,
  isQwenHealthEnvelope,
  parseQwenAskEnvelope,
  qwenStateFromAsk,
  qwenStateFromHealth,
  qwenStateFromTransportFailure,
  qwenStatusLabel,
  shouldUseLocalQwen,
} = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

const health = localQwenHealthEnvelope;

test("only the exact pinned local health envelope becomes ready", () => {
  assert.ok(QWEN_LOCAL_BROWSER_CONFIG.healthTimeoutMs > QWEN_LOCAL_HEALTH_TIMEOUT_MS);
  assert.equal(isQwenHealthEnvelope(health("ready")), true);
  assert.equal(qwenStateFromHealth(health("ready")), "ready");
  assert.equal(shouldUseLocalQwen("ready"), true);
  assert.equal(qwenStatusLabel("ready"), "LOCAL QWEN READY");
  assert.equal(shouldUseLocalQwen("answered"), true);
  assert.equal(qwenStatusLabel("abstained"), "LOCAL QWEN ABSTAINED");
  assert.equal(shouldUseLocalQwen("abstained"), true);
});

test("finite local failure states remain non-answering", () => {
  for (const [state, label] of [
    ["bridge-unavailable", "LOCAL BRIDGE UNREACHABLE"],
    ["ollama-unavailable", "OLLAMA NOT RUNNING"],
    ["model-missing", "QWEN3:8B NOT INSTALLED"],
    ["denied", "LOCAL REQUEST DENIED"],
    ["busy", "LOCAL QWEN BUSY"],
    ["timeout", "LOCAL QWEN TIMED OUT"],
    ["error", "LOCAL QWEN REQUEST FAILED"],
  ]) {
    assert.equal(qwenStatusLabel(state), label);
    assert.equal(shouldUseLocalQwen(state), false);
  }
  assert.equal(qwenStateFromHealth(health("model_missing")), "model-missing");
  assert.equal(qwenStateFromHealth(health("ollama_unavailable")), "ollama-unavailable");
  assert.equal(qwenStateFromHealth(health("error", "OLLAMA_VERSION_MISMATCH")), "error");
  assert.equal(qwenStateFromTransportFailure(true, false), "timeout");
  assert.equal(qwenStateFromTransportFailure(false, false), "bridge-unavailable");
  assert.equal(qwenStateFromTransportFailure(false, true), "error");
});

test("ask envelopes share the pinned contract and map only finite local outcomes", () => {
  const answered = localQwenAskEnvelope("ANSWER", "SUPPORTED_SELECTION_INTERPRETATION", {
    answer: "Supported by kfm:evidence:test:one.",
    evidenceRefs: ["kfm:evidence:test:one"],
  });
  assert.equal(isQwenAskEnvelope(answered), true);
  assert.deepEqual(parseQwenAskEnvelope(answered), {
    outcome: "ANSWER",
    reasonCode: "SUPPORTED_SELECTION_INTERPRETATION",
    answer: "Supported by kfm:evidence:test:one.",
    evidenceRefs: ["kfm:evidence:test:one"],
  });
  assert.equal(qwenStateFromAsk(answered), "answered");
  assert.equal(qwenStateFromAsk(localQwenAskEnvelope("ABSTAIN", "MODEL_ABSTAINED")), "abstained");
  assert.equal(qwenStateFromAsk(localQwenAskEnvelope("DENY", "POLICY_WITHHELD")), "denied");
  assert.equal(qwenStateFromAsk(localQwenAskEnvelope("ERROR", "OLLAMA_UNAVAILABLE")), "ollama-unavailable");
  assert.equal(qwenStateFromAsk(localQwenAskEnvelope("ERROR", "MODEL_MISSING")), "model-missing");
  assert.equal(qwenStateFromAsk(localQwenAskEnvelope("ERROR", "BRIDGE_BUSY")), "busy");
  assert.equal(qwenStateFromAsk(localQwenAskEnvelope("ERROR", "REQUEST_TIMEOUT")), "timeout");
  assert.equal(isQwenAskEnvelope({ ...answered, endpoint: "https://model.test" }), false);
});

test("hosted, malformed and extended envelopes are never assumed as fallback state", () => {
  for (const value of [
    null,
    { ...health("ready"), mode: "hosted" },
    { ...health("ready"), model: "qwen2.5:7b-instruct-fp16" },
    { ...health("ready"), modelDigest: "sha256:" + "0".repeat(64) },
    { ...health("ready"), bridgeVersion: "1.0.0" },
    { ...health("ready"), endpoint: "https://model.test" },
    { ...health("ready"), status: "hosted-answered" },
  ]) {
    assert.equal(isQwenHealthEnvelope(value), false);
    assert.equal(qwenStateFromHealth(value), "error");
  }
  assert.doesNotMatch(source, /hosted-answered|successfulQwenState\s*=\s*\(local/);
});
