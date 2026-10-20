import assert from "node:assert/strict";
import test from "node:test";
import { isStaleInterceptionCancellation } from "./browser-interception.mjs";

test("browser navigation cancellation never hides live-request or unrelated protocol failures", () => {
  const canceled = new Error(JSON.stringify({ code: -32602, message: "Invalid InterceptionId." }));
  assert.equal(isStaleInterceptionCancellation(canceled, 1, 2), true);
  assert.equal(isStaleInterceptionCancellation(canceled, 2, 2), false, "same-document failure remains fatal");
  assert.equal(isStaleInterceptionCancellation(canceled, 3, 2), false, "only earlier navigation is eligible");
  for (const error of [
    new Error("CDP timeout: Fetch.fulfillRequest"),
    new Error('not JSON: {"code":-32602,"message":"Invalid InterceptionId."}'),
    new Error(JSON.stringify({ code: -32000, message: "Invalid InterceptionId." })),
    new Error(JSON.stringify({ code: -32602, message: "Invalid parameters" })),
    new Error(JSON.stringify({ code: -32602, message: "Invalid InterceptionId. Additional failure" })),
  ]) assert.equal(isStaleInterceptionCancellation(error, 1, 2), false);
});
