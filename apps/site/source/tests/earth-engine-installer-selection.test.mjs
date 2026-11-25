import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const PREFIX = "earth-engine-context";
const folder = (setId, pointerText) => [
  { webkitRelativePath: `pick/${PREFIX}/active.json`, text: () => pointerText ?? Promise.resolve(JSON.stringify({ setId })) },
  { webkitRelativePath: `pick/${PREFIX}/sets/${setId}/manifest.json`, arrayBuffer: async () => new TextEncoder().encode(JSON.stringify({ setId })).buffer },
  { webkitRelativePath: `pick/${PREFIX}/sets/${setId}/tile.png` },
];

test("a slow earlier folder check cannot replace the newer selected display set", async () => {
  const h = await componentHarness("app/earth-engine-context/install/installer.tsx", {
    "../../earth-engine-context": {
      EARTH_ENGINE_CONTEXT_PREFIX: PREFIX,
      parseEarthEnginePointer: value => ({ setId: value.setId, manifestSha256: "ab" }),
      parseEarthEngineManifest: value => ({ setId: value.setId, layers: [] }),
    },
  }, { TextDecoder, TextEncoder, crypto: { subtle: { digest: async () => new Uint8Array([0xab]).buffer } } });
  const render = () => { const tree = h.render(h.exports.EarthEngineInstaller, {}); h.commit(); return tree; };
  const input = () => findNode(render(), n => n.type === "input" && n.props.id === "ee-display-folder");
  let releaseOld;
  input().props.onChange({ target: { files: folder("older-set", new Promise(resolve => { releaseOld = resolve; })) } });
  input().props.onChange({ target: { files: folder("newer-set") } });
  await settle();
  releaseOld(JSON.stringify({ setId: "older-set" }));
  await settle();
  const tree = render();
  const set = findNode(tree, n => n.type === "p" && [n.props.children].flat().some(c => c?.type === "b" && c.props.children === "Set:"));
  assert.ok(set, "a prepared set is shown");
  assert.ok([set.props.children].flat().includes("newer-set"), "the newer selection stays prepared");
  h.dispose();
});
