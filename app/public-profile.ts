/** This isolated copy never inherits the private Explorer's operator capabilities. */
export const IS_PUBLIC_COPY = true;
export const PUBLIC_RELEASE_RECHECK_MS = 60_000;

export function publicDataAsset(path: string): string {
  if (!IS_PUBLIC_COPY) return path;
  const match = /^\/data\/(subsurface|groundwater|archive)\/([A-Za-z0-9][A-Za-z0-9._-]*)$/.exec(path);
  if (!match || match[2].includes("..")) throw new Error("PUBLIC_ASSET_PATH_INVALID");
  return `/api/governed/public/assets/${match[1]}/${match[2]}`;
}

/** Provider overlays need an explicit approved delivery manifest before exposure. */
export const publicContextSourceAllowed = (id: string): boolean => !IS_PUBLIC_COPY && id.length > 0;
export const publicBasemap = <T extends string>(key: T): T | "standard" =>
  IS_PUBLIC_COPY && !["standard", "midnight", "prairie"].includes(key) ? "standard" : key;

export type PublicAssetLease = { packageId: string; expiresAt: number };
export function publicAssetLease(response: Response, now = Date.now()): PublicAssetLease {
  if (!response.ok) throw new Error("No approved public artifact is available.");
  const packageId = response.headers.get("X-KFM-Public-Release-ID") ?? "";
  const expiresAt = Date.parse(response.headers.get("X-KFM-Public-Expires-At") ?? "");
  if (!/^sha256:[a-f0-9]{64}$/.test(packageId) || !Number.isFinite(expiresAt) || expiresAt <= now)
    throw new Error("Public release approval is unavailable or expired.");
  return { packageId, expiresAt };
}

/** Export revalidates the active pointer; cached bytes are never release authority. */
export async function publicFamilyAvailable(family: string, signal?: AbortSignal, packageId?: string): Promise<boolean> {
  if (!IS_PUBLIC_COPY) return true;
  try {
    const response = await fetch("/api/governed/public/catalog", { cache: "no-store", signal, credentials: "same-origin" });
    const text = await response.text();
    if (!response.ok || text.length > 256_000) return false;
    const value = JSON.parse(text);
    return value?.envelope?.outcome === "ANSWER" && Array.isArray(value?.data?.entries)
      && value.data.entries.some((entry: { family?: unknown; package_id?: unknown; expires_at?: unknown }) =>
        entry?.family === family && (!packageId || entry.package_id === packageId) && typeof entry.package_id === "string" && /^sha256:[a-f0-9]{64}$/.test(entry.package_id)
        && typeof entry.expires_at === "string" && Date.parse(entry.expires_at) > Date.now());
  } catch { return false; }
}
