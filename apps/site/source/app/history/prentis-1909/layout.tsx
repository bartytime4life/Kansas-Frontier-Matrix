import type { Metadata } from "next";
import type { ReactNode } from "react";

// The page is a client component, so its title is set here.
export const metadata: Metadata = {
  title: "A History of Kansas (1909) · Kansas Frontier Matrix",
  description: "Read and search Noble L. Prentis's 1909 A History of Kansas, edited and revised by Henrietta V. Race.",
};

export default function Layout({ children }: { children: ReactNode }) {
  return children;
}
