import { NextResponse } from "next/server";
import { GLM_FLASH_WINDOWS, type GlmFlashWindow } from "../../../lightning-flashes";
import { getGlmFlashSnapshot } from "../../../lightning-flashes-server";

export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const value = Number(params.get("minutes") ?? "15");
  if ([...params.keys()].some((key) => key !== "minutes" || params.getAll(key).length !== 1) || !GLM_FLASH_WINDOWS.includes(value as GlmFlashWindow)) return NextResponse.json({ state: "error", message: "Choose a 5, 15, 30 or 60 minute GLM window." }, { status: 400, headers: { "Cache-Control": "no-store" } });
  try {
    return NextResponse.json(await getGlmFlashSnapshot(value as GlmFlashWindow), { headers: { "Cache-Control": "public, max-age=20", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    console.error("Kansas GOES GLM flash request failed", error);
    return NextResponse.json({ state: "error", message: "Time-stamped satellite flashes are unavailable. No positions were inferred from the climate or density rasters." }, { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
}
