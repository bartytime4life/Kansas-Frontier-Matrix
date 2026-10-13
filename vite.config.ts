import vinext from "vinext";
import { defineConfig } from "vite";
import { fileURLToPath } from "node:url";

// Separate Node composition; the preserved Sites source and bindings are unchanged.
export default defineConfig({
  define: {
    __KFM_BUILD_UTC_YEAR__: JSON.stringify(Math.max(2026, new Date().getUTCFullYear())),
  },
  resolve: {
    alias: {
      "cloudflare:workers": fileURLToPath(new URL("./server/godaddy-env.ts", import.meta.url)),
    },
  },
  server: { host: "0.0.0.0" },
  plugins: [vinext()],
});
