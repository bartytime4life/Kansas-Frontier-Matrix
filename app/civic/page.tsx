import type { Metadata } from "next";
import CivicAtlas from "./civic-atlas";

export const metadata: Metadata = {
  title: "Kansas Civic Atlas · Kansas Frontier Matrix",
  description: "Find official Kansas government, voting, finance, legislation, jobs and service sources, with county map context and neutral research tools.",
};

export default function CivicPage() { return <CivicAtlas />; }
