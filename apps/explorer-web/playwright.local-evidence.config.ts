import { fileURLToPath } from "node:url";
import { defineConfig } from "playwright/test";
import base from "./playwright.config";

// Both processes are owned by this test run; an unrelated running service
// cannot silently supply its evidence. No provider or external source is used.
export default defineConfig({
  ...base,
  testMatch: "local-http-evidence.spec.ts",
  testIgnore: [],
  webServer: [
    {
      command: "python -m governed_api.local_fixture",
      cwd: fileURLToPath(new URL("../../", import.meta.url)),
      env: { PYTHONPATH: "apps/governed-api/src" },
      url: "http://127.0.0.1:8765/__local__/health",
      reuseExistingServer: false,
      timeout: 15_000,
    },
    {
      command: "pnpm run dev:local-evidence",
      url: "http://127.0.0.1:4173",
      reuseExistingServer: false,
      timeout: 30_000,
    },
  ],
});
