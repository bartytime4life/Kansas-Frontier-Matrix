import { defineConfig } from "playwright/test";
import browser from "./playwright.config";

// Explicit local integration lane. The normal browser lane has no API server.
export default defineConfig({
  ...browser,
  testMatch: "governed-api-negative.api.ts",
  webServer: [
    {
      command: 'python3 -c "import sys; sys.path.insert(0, \'../governed-api/src\'); from governed_api.main import serve; serve(port=4174)"',
      url: "http://127.0.0.1:4174/evidence",
      reuseExistingServer: false,
      timeout: 30_000,
    },
    {
      command: "pnpm exec vite --config tests/browser/governed-api.vite.config.ts --host 127.0.0.1 --port 4173 --strictPort",
      url: "http://127.0.0.1:4173/tests/browser/map-evidence-drawer.html",
      reuseExistingServer: false,
      timeout: 30_000,
    },
  ],
});
