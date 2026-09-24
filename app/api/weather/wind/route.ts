import { NextResponse } from "next/server";
import { readBoundedJson } from "../../../bounded-json";
import { parseWindForecast, windRequest, WIND_GRID, type WindLevel } from "../../../wind-field";

export const dynamic = "force-dynamic";
const API = "https://api.open-meteo.com/v1/forecast";

export async function GET(request: Request) {
  const requestedLevel = new URL(request.url).searchParams.get("level") ?? "10m";
  if (requestedLevel !== "10m" && requestedLevel !== "1000hPa") {
    return NextResponse.json({ state: "invalid", message: "Choose the 10 m or 1000 hPa wind level." },
      { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
  const level: WindLevel = requestedLevel;
  const selection = windRequest(level);
  const url = new URL(API);
  url.searchParams.set("latitude", WIND_GRID.map((point) => point[1]).join(","));
  url.searchParams.set("longitude", WIND_GRID.map((point) => point[0]).join(","));
  url.searchParams.set("hourly", selection.variables);
  if (selection.model) url.searchParams.set("models", selection.model);
  url.searchParams.set("forecast_hours", "7");
  url.searchParams.set("timezone", "GMT");
  url.searchParams.set("wind_speed_unit", "kmh");
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 12_000);
  try {
    const response = await fetch(url, { signal: controller.signal, redirect: "manual", cache: "no-store", headers: { Accept: "application/json" } });
    if (!response.ok || !response.headers.get("content-type")?.toLowerCase().includes("application/json")) throw new Error("Wind provider unavailable.");
    const field = parseWindForecast(await readBoundedJson(response, 96 * 1024), new Date().toISOString(), level);
    return NextResponse.json(field, { headers: { "Cache-Control": "public, max-age=600, stale-while-revalidate=300", "X-Content-Type-Options": "nosniff" } });
  } catch {
    return NextResponse.json({ state: "unavailable", message: "The forecast wind field is unavailable. No substitute vectors were drawn." },
      { status: 502, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  } finally {
    clearTimeout(timer);
  }
}
