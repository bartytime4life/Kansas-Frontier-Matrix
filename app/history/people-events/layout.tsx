import type { Metadata } from "next";
import type { ReactNode } from "react";

export const metadata: Metadata = { alternates: { canonical: "https://kansasfrontiermatrix.com/history/people-events" }, title: "People & events · Kansas Frontier Matrix" };

export default function PeopleEventsLayout({ children }: { children: ReactNode }) {
  return <>{children}</>;
}
