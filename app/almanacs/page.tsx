import type { Metadata } from "next";
import AlmanacLibrary from "./library";
import { restoreAlmanacFilters } from "../almanac-resources";

export const metadata: Metadata = {
  title: "Almanac references · Kansas Frontier Matrix",
  description: "Farmers’ Almanac and The Old Farmer’s Almanac source references, a permitted seasonal map, and a historical title page with clear access and reuse limits.",
};

export default async function AlmanacsPage({ searchParams }: { searchParams: Promise<{ publisher?: string | string[]; topic?: string | string[] }> }) {
  const params = await searchParams;
  const query = new URLSearchParams();
  for (const key of ["publisher", "topic"] as const) if (typeof params?.[key] === "string") query.set(key, params[key]);
  return <AlmanacLibrary initialFilters={restoreAlmanacFilters(query.toString())} />;
}
