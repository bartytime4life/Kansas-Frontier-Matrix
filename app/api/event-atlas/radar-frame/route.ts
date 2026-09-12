import { EVENT_BOUNDS, exactUtc, radarDirectory, parseRadarDirectory } from "../../../event-atlas";
import { boundedFetch } from "../upstream";
export const dynamic = "force-dynamic";
const directories = new Map<string, { at: number; text: string }>();

export async function GET(request: Request) {
  try {
    const params = new URL(request.url).searchParams;
    if ([...params.keys()].some((key) => key !== "time") || params.getAll("time").length !== 1) throw new Error("One exact time is required.");
    const time = exactUtc(params.get("time") ?? "");
    if (!time || time < "1995-01-01" || Date.parse(time) > Date.now() || new Date(time).getUTCMinutes() % 5 || new Date(time).getUTCSeconds()) throw new Error("Invalid archived radar time.");
    const day = time.slice(0,10);
    let directory = directories.get(day);
    if (!directory || Date.now() - directory.at > 120_000) {
      const response = await boundedFetch(radarDirectory(day), 1024 * 1024);
      directory = { at: Date.now(), text: response.text() };
      if (directories.size >= 4) directories.delete(directories.keys().next().value!);
      directories.set(day, directory);
    }
    const scan = parseRadarDirectory(directory.text, day, time, new Date(Date.parse(time) + 300_000).toISOString())[0];
    if (!scan) return Response.json({ message: "No admitted radar artifact exists at this time." }, { status: 404 });
    const upstream = new URL(`https://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/${scan.product}-t.cgi`);
    // Match MapLibre's Mercator image projection, not a linearly sampled
    // latitude image that would drift between the four corner anchors.
    const x = (lng: number) => lng * 20037508.342789244 / 180;
    const y = (lat: number) => Math.log(Math.tan(Math.PI/4 + lat*Math.PI/360)) * 6378137;
    const bbox = [x(EVENT_BOUNDS[0]), y(EVENT_BOUNDS[1]), x(EVENT_BOUNDS[2]), y(EVENT_BOUNDS[3])].join(",");
    const query = { service: "WMS", version: "1.1.1", request: "GetMap", layers: `nexrad-${scan.product}-wmst`, styles: "", format: "image/png", transparent: "true", srs: "EPSG:3857", bbox, width: "1024", height: "600", time: time.replace(".000Z", "Z") };
    for (const [key,value] of Object.entries(query)) upstream.searchParams.set(key,value);
    const frame = await boundedFetch(upstream.toString(), 4 * 1024 * 1024);
    if (!frame.headers.get("content-type")?.includes("image/png") || frame.bytes.length < 24 || ![137,80,78,71,13,10,26,10].every((byte,index) => frame.bytes[index] === byte)) throw new Error("Source did not return a valid radar PNG.");
    const dimensions = new DataView(frame.bytes.buffer);
    if (dimensions.getUint32(16) !== 1024 || dimensions.getUint32(20) !== 600) throw new Error("Unexpected radar image dimensions.");
    return new Response(frame.bytes, { headers: { "Content-Type": "image/png", "Cache-Control": "public, max-age=3600", "X-Content-Type-Options": "nosniff", "X-Radar-Mosaic-Time": time, "X-Radar-Product": scan.product, "X-Source-Artifact": scan.artifact } });
  } catch { return Response.json({ message: "The exact historical radar frame is unavailable. No latest-image fallback was used." }, { status: 502, headers: { "Cache-Control": "no-store" } }); }
}
