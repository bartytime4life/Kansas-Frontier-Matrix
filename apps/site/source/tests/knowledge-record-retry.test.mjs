import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

test("a knowledge record can recover from an unavailable read without leaving the page", async () => {
  const requests = [];
  const h = await componentHarness("app/knowledge/record/page.tsx", {
    "next/link": { default: "a" }, "next/navigation": { useSearchParams: () => new URLSearchParams() },
    "../knowledge.module.css": { default: {} },
    "../../knowledge-read": {
      knowledgeUnavailable: () => ({ envelope: { outcome: "ERROR", reason_code: "STORAGE_UNAVAILABLE" } }),
      readKnowledge: (query, signal) => new Promise((resolve, reject) => requests.push({ query, signal, resolve, reject })),
    },
  }, {}, "\nexport { KnowledgeRecordContent as TestRecord };\n");
  const render = () => { const tree = h.render(h.exports.TestRecord, { id: "record-1" }); h.commit(); return tree; };
  render(); requests[0].reject(new Error("Temporary outage")); await settle();
  findNode(render(), n => n.type === "button" && n.props.children === "Retry record").props.onClick();
  const loading = render();
  assert.equal(findNode(loading, n => n.props?.['aria-busy'] === true).props['aria-busy'], true);
  assert.equal(requests.length, 2);
  assert.equal(requests[0].signal.aborted, true);
  assert.equal(requests[1].query.id, "record-1");
  requests[1].resolve({ envelope: { outcome: "ABSTAIN", reason_code: "NO_APPROVED_KNOWLEDGE" } }); await settle();
  const recovered = render();
  assert.equal(findNode(recovered, n => n.type === "button" && n.props.children === "Retry record"), undefined);
  assert.ok(findNode(recovered, n => n.type === "p" && n.props.children === "No knowledge release is active yet."));
  h.dispose();
});
