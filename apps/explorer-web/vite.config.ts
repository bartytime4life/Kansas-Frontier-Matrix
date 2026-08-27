import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";

export default defineConfig({
  resolve: {
    alias: [
      {
        find: "@kfm/maplibre/vite-adapter",
        replacement: fileURLToPath(
          new URL(
            "../../packages/maplibre/src/maplibre-vite-adapter.ts",
            import.meta.url,
          ),
        ),
      },
      {
        find: "@kfm/maplibre",
        replacement: fileURLToPath(
          new URL("../../packages/maplibre/src/index.ts", import.meta.url),
        ),
      },
    ],
  },
  build: {
    emptyOutDir: true,
    outDir: "dist",
    sourcemap: false,
  },
});
