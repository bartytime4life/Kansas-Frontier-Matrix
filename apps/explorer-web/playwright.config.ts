import { defineConfig } from "playwright/test";

export default defineConfig({
  testDir: "./tests/browser",
  testMatch: "*.spec.ts",
  fullyParallel: false,
  workers: 1,
  retries: 0,
  reporter: "list",
  use: {
    baseURL: "http://127.0.0.1:4173",
    browserName: "chromium",
    headless: true,
    ...(process.env.CI === "true" ? { channel: "chrome" as const } : {}),
    ...(process.env.KFM_CHROMIUM_EXECUTABLE
      ? {
          launchOptions: {
            executablePath: process.env.KFM_CHROMIUM_EXECUTABLE,
            args: ["--no-sandbox"],
          },
        }
      : {}),
  },
  webServer: {
    command: "pnpm exec vite --host 127.0.0.1 --port 4173 --strictPort",
    url: "http://127.0.0.1:4173/tests/browser/evidence-drawer.html",
    reuseExistingServer: false,
    timeout: 30_000,
  },
});
