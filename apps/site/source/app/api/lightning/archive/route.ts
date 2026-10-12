import { NextResponse } from "next/server";
import { archiveInterval, type GlmArchiveQuery } from "../../../lightning-archive";
import { getArchiveManifest, getArchivePart } from "../../../lightning-archive-server";
export const dynamic = "force-dynamic";

export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const query = { day: params.get("day") ?? "", hour: Number(params.get("hour")), minute: Number(params.get("minute")), duration: Number(params.get("duration")) } as GlmArchiveQuery;
  const partText = params.get("part"), manifestId = params.get("manifest");
  try {
    if ([...params.keys()].some(key => !["day", "hour", "minute", "duration", "part", "manifest"].includes(key) || params.getAll(key).length !== 1)
      || ["day", "hour", "minute", "duration"].some(key => !params.has(key))
      || (partText !== null && (!/^\d{1,3}$/.test(partText) || !/^[a-f0-9]{64}$/.test(manifestId ?? "")))
      || (partText === null && manifestId !== null)) throw new Error("Invalid archive query.");
    archiveInterval(query);
  } catch {
    return NextResponse.json({ message: "Choose a valid completed interval from July 5, 2017 onward." }, { status: 400 });
  }
  const signal = AbortSignal.any([request.signal, AbortSignal.timeout(25_000)]);
  try {
    const manifest = await getArchiveManifest(query, signal);
    if (partText === null) return NextResponse.json(manifest, { headers: { "Cache-Control": "no-store" } });
    if (manifestId !== manifest.id) return NextResponse.json({ message: "Archive listing changed. Reload the interval." }, { status: 409 });
    if (Number(partText) >= manifest.parts) return NextResponse.json({ message: "Invalid archive part." }, { status: 400 });
    const bytes = await getArchivePart(manifest, Number(partText), signal);
    return new Response(bytes.buffer as ArrayBuffer, { headers: { "Content-Type": "application/x-netcdf", "Content-Length": String(bytes.length), "X-GLM-Manifest": manifest.id, "Cache-Control": "private, max-age=600", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return NextResponse.json({ message: "NOAA files could not be loaded for this interval. Try another date or retry; no lightning observations were inferred." }, { status: 502, headers: { "Cache-Control": "no-store" } });
  }
}
