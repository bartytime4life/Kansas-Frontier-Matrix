import type { Metadata } from "next";
import type { ReactNode } from "react";

// The page is a client component, which cannot declare its own title. This route has no child pages,
// so the canonical address here applies to it alone.
export const metadata: Metadata = {
  title: "Data lab · Kansas Frontier Matrix",
  description: "Explore source fields, missing values and measurement groups in the archive's public collections, and build a reproducible research brief from actual records.",
  alternates: { canonical: "https://kansasfrontiermatrix.com/data-lab" },
};

export default function Layout({ children }: { children: ReactNode }) { return children; }
