import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = { title: "Reviewed record · Kansas Frontier Matrix" };

export default function KnowledgeRecordLayout({ children }: { children: ReactNode }) {
  return <>{children}</>;
}
