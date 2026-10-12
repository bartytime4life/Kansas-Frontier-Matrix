/** Nearest image rows only: these are provider colors, never numeric readings. */
export function previewSourceRow(row: number, height: number) {
  const mercator = (lat: number) => Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360));
  const north = mercator(40.05), south = mercator(36.95);
  const latitude = (2 * Math.atan(Math.exp(north + (south - north) * (row + .5) / height)) - Math.PI / 2) * 180 / Math.PI;
  return Math.max(0, Math.min(height - 1, Math.floor((40.05 - latitude) / (40.05 - 36.95) * height)));
}
export async function loadCropPreview(day: string, signal: AbortSignal) {
  const response = await fetch(`/api/crop-casma/preview?day=${day}`, { signal });
  if (!response.ok || !response.headers.get("content-type")?.includes("image/png")) throw new Error("Preview unavailable");
  const image = await createImageBitmap(await response.blob());
  try {
    signal.throwIfAborted();
    if (image.width !== 1024 || image.height !== 512) throw new Error("Unexpected preview dimensions");
    const canvas = document.createElement("canvas"); canvas.width = image.width; canvas.height = image.height;
    const context = canvas.getContext("2d"); if (!context) throw new Error("Canvas unavailable");
    context.imageSmoothingEnabled = false;
    for (let row = 0; row < canvas.height; row++) context.drawImage(image, 0, previewSourceRow(row, canvas.height), canvas.width, 1, 0, row, canvas.width, 1);
    return canvas;
  } finally { image.close(); }
}
