/** Module workers for the underground views. They prepare data only and never load the map renderer. */
export const startSubsurfaceWorker = () => new Worker(new URL("./subsurface-worker.ts", import.meta.url), { type: "module" });
export const startAquiferVolumeWorker = () => new Worker(new URL("./aquifer-volume-worker.ts", import.meta.url), { type: "module" });
