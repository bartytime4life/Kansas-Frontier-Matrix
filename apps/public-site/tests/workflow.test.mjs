import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
const workflow = readFileSync(new URL("../../../.github/workflows/godaddy-public-site.yml", import.meta.url), "utf8");

test("historical static workflow cannot deploy or access hosting credentials", () => {
  assert.doesNotMatch(workflow, /^  deploy:/m);
  assert.doesNotMatch(workflow, /\$\{\{ secrets\.|environment:|deployments: write/);
  assert.doesNotMatch(workflow, /infra\/godaddy\/deploy\.sh|Install lftp|Mirror bundle/);
  assert.doesNotMatch(workflow, /GODADDY_DEPLOY_ENABLED|inputs\.(?:dry_run|delete_remote)/);
  assert.doesNotMatch(workflow, /secrets: inherit|pull_request_target:|inputs\.(?:ref|commit|branch|tag)/);
  assert.match(workflow, /name: godaddy-public-site/);
  assert.match(workflow, /--test apps\/public-site\/tests\/\*\.test\.mjs/);
  assert.match(workflow, /actions\/upload-artifact@/);
  assert.match(workflow, /persist-credentials: false/);
  const runbook = readFileSync(new URL("../../../docs/runbooks/godaddy-hosting.md", import.meta.url), "utf8");
  assert.match(runbook, /build-only/);
  assert.match(runbook, /urdng3v1vk/);
});
