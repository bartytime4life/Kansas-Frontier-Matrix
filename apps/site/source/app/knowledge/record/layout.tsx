import type { Metadata } from "next";
import type { ReactNode } from "react";

// The page is a client component, so its title is set here.
export const metadata: Metadata = {
  title: "Reviewed record · Kansas knowledge · Kansas Frontier Matrix",
  description: "A single reviewed Kansas knowledge record with its sources, evidence and release.",
};

export default function Layout({ children }: { children: ReactNode }) {
  return children;
}
