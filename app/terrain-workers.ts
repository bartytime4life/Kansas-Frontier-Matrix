// Vite emits this same-origin module worker as a separate asset.
export const startTerrainPreparationWorker=()=>new Worker(new URL('./terrain-preparation-worker.ts',import.meta.url),{type:'module',name:'kfm-current-terrain'});
