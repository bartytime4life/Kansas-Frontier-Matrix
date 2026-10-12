import { governedWaterRead, WATER_HEADERS } from "../../../../governed-water-server";
import { waterNegative } from "../../../../governed-water";
export async function GET(request: Request, context: { params: Promise<{ view: string }> }) {
  const { view } = await context.params;
  if (!["bootstrap", "layers", "evidence"].includes(view)) return Response.json(await waterNegative("ROUTE_NOT_FOUND", new Date().toISOString()), { status: 404, headers: WATER_HEADERS });
  return governedWaterRead(request, view);
}
