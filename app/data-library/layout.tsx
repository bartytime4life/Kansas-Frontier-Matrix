import type { Metadata } from "next";
import type { ReactNode } from "react";

// The page is a client component, which cannot declare its own title. This route has no child pages,
// so the canonical address here applies to it alone.
export const metadata: Metadata = {
  title: "Public data library · Kansas Frontier Matrix",
  description: "Browse the recovered public data collections behind the Kansas map: what each one holds, where it came from and how fresh it is.",
  alternates: { canonical: "https://kansasfrontiermatrix.com/data-library" },
};

export default function Layout({ children }: { children: ReactNode }) { return children; }
