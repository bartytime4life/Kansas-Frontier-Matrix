import type { Metadata } from "next";
import type { ReactNode } from "react";

// The page is a client component, so its title is set here.
export const metadata: Metadata = {
  title: "Kansas knowledge · Kansas Frontier Matrix",
  description: "Search reviewed Kansas places, facts, people, events and stories from the active knowledge release.",
};

export default function Layout({ children }: { children: ReactNode }) {
  return children;
}
