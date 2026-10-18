import { governedSoilRead, SOIL_HEADERS } from "../../../../../governed-soil-server";
import { soilNegative } from "../../../../../governed-soil";
export async function GET(request: Request, context: { params: Promise<{ view: string }> }) {
  const { view } = await context.params;
  if (!["bootstrap", "layers", "evidence"].includes(view)) return Response.json(await soilNegative("ROUTE_NOT_FOUND", new Date().toISOString()), { status: 404, headers: SOIL_HEADERS });
  return governedSoilRead(request, view);
}
