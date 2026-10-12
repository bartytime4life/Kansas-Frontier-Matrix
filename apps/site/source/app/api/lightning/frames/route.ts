import { NextResponse } from "next/server";
import { getLightningManifest } from "../../../lightning-server";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    return NextResponse.json(await getLightningManifest(), { headers: { "Cache-Control": "public, max-age=60", "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    console.error("NOAA lightning manifest request failed", error);
    return NextResponse.json({ state: "error", message: "NOAA lightning frames are unavailable; no untimed or simulated fallback was used." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
