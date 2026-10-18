import { rm } from "node:fs/promises";
// Vite build metadata is not visitor content. Remove only the generated client copy;
// the server build already embeds its asset mappings.
await rm("dist/client/.vite", { recursive: true, force: true });
