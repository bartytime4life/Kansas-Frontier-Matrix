import type { Metadata } from "next";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import { OFFICIAL_CONTEXT_SOURCES } from "../live-context";
import { SOURCE_DOWNLOADS } from "../source-downloads";
import { SCIENCE_EVENTS } from "../science-events";
import { discoverySources, readDiscoveryState } from "./discovery";
import ResearchDiscovery from "./workspace";

export const metadata: Metadata = {
  title: "Research Discovery · Kansas Frontier Matrix",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/research` },
  description: "Find Kansas data, compare source clocks and limitations, and start an investigation across water, earth, ecology and history.",
};

export default async function ResearchPage({ searchParams }: { searchParams: Promise<Record<string, string | string[] | undefined>> }) {
  const params = new URLSearchParams();
  for (const [key, value] of Object.entries(await searchParams)) if (typeof value === "string") params.set(key, value);
  const sources = discoverySources(OFFICIAL_CONTEXT_SOURCES, SOURCE_DOWNLOADS);
  return <ResearchDiscovery sources={sources} instruments={SCIENCE_EVENTS} initialState={readDiscoveryState(params, sources)} />;
}
