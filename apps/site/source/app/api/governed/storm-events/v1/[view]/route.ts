import { governedStormEventsRead, STORM_EVENTS_HEADERS } from "../../../../../governed-storm-events-server";
import { stormEventsNegative } from "../../../../../governed-storm-events";
export async function GET(request: Request, context: { params: Promise<{ view: string }> }) {
  const { view } = await context.params;
  if (!["bootstrap", "layers", "evidence"].includes(view)) return Response.json(await stormEventsNegative("ROUTE_NOT_FOUND", new Date().toISOString()), { status: 404, headers: STORM_EVENTS_HEADERS });
  return governedStormEventsRead(request, view);
}
