import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";

export default defineConfig({
  resolve: {
    alias: {
      "@kfm/maplibre": fileURLToPath(
        new URL("../../packages/maplibre/src/index.ts", import.meta.url),
      ),
    },
  },
  build: {
    emptyOutDir: true,
    outDir: "dist",
    sourcemap: false,
  },
});
