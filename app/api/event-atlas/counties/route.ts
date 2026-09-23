import { countyBaseline, COUNTY_EDITIONS, type CountyEdition } from "../../../county-baseline";
export const dynamic = "force-dynamic";
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const edition = params.get("edition") ?? "2020";
  if (!Object.hasOwn(COUNTY_EDITIONS, edition) || [...params.keys()].some((key) => key !== "edition" || params.getAll(key).length > 1)) return Response.json({ message: "Choose the 2010 or 2020 Census baseline." }, { status: 400 });
  try { return Response.json(await countyBaseline(edition as CountyEdition), { headers: { "Cache-Control": "public, max-age=86400", "X-Content-Type-Options": "nosniff" } }); }
  catch (error) { return Response.json({ message: error instanceof Error ? error.message : "County baseline unavailable." }, { status: 502, headers: { "Cache-Control": "no-store" } }); }
}
