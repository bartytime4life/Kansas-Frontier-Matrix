import { governedWeatherRead, WEATHER_HEADERS } from "../../../../../governed-weather-server";
import { weatherNegative } from "../../../../../governed-weather";
export async function GET(request: Request, context: { params: Promise<{ view: string }> }) {
  const { view } = await context.params;
  if (!["bootstrap", "layers", "evidence"].includes(view)) return Response.json(await weatherNegative("ROUTE_NOT_FOUND", new Date().toISOString()), { status: 404, headers: WEATHER_HEADERS });
  return governedWeatherRead(request, view);
}
