import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = { title: "Prentis 1909 reader · Kansas Frontier Matrix" };

export default function PrentisReaderLayout({ children }: { children: ReactNode }) {
  return <>{children}</>;
}
