import { governedEarthquakesRead, EARTHQUAKE_HEADERS } from "../../../../../governed-earthquakes-server";
import { earthquakesNegative } from "../../../../../governed-earthquakes";
export async function GET(request: Request, context: { params: Promise<{ view: string }> }) {
  const { view } = await context.params;
  if (!["bootstrap", "layers", "evidence"].includes(view)) return Response.json(await earthquakesNegative("ROUTE_NOT_FOUND", new Date().toISOString()), { status: 404, headers: EARTHQUAKE_HEADERS });
  return governedEarthquakesRead(request, view);
}
