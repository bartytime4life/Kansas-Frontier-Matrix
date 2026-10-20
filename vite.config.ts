import vinext from "vinext";
import { defineConfig } from "vite";
import { fileURLToPath } from "node:url";
import { welcomeDemoCapturePlugin } from "./scripts/welcome-demos/capture-sink.mjs";

// Separate Node composition; the preserved Sites source and bindings are unchanged.
export default defineConfig(({ command }) => {
  const recorderEnabled = command === "serve" && process.env.KFM_WELCOME_DEMO_RECORDER === "1";
  return {
  define: {
    __KFM_WELCOME_RECORDER__: JSON.stringify(recorderEnabled),
    __KFM_BUILD_UTC_YEAR__: JSON.stringify(Math.max(2026, new Date().getUTCFullYear())),
  },
  resolve: {
    alias: {
      "cloudflare:workers": fileURLToPath(new URL("./server/godaddy-env.ts", import.meta.url)),
    },
  },
  server: { host: recorderEnabled ? "127.0.0.1" : "0.0.0.0" },
  plugins: [vinext(), ...(recorderEnabled ? [welcomeDemoCapturePlugin()] : [])],
  };
});
