import type { Metadata } from "next";
import { SITE_IDENTITY } from "./site-identity";
import { PersistentSelectMenus } from "./persistent-select-menus";
import "./globals.css";
import "./map-layers.css";

export async function generateMetadata(): Promise<Metadata> {
  // Canonical metadata is deployment identity, never caller-controlled routing input.
  const metadataBase = new URL(SITE_IDENTITY.canonicalUrl);
  const socialImage = new URL("/og-guided.png", metadataBase).toString();

  return {
    title: "Kansas Frontier Matrix Explorer",
    description: "Explore Kansas through a MapLibre vector-map-first Living Atlas, then use bounded evidence, time, reports, and Qwen context when needed.",
    metadataBase,
    openGraph: {
      title: "Kansas Frontier Matrix Explorer",
      description: "Start on a real MapLibre Kansas vector context, inspect place and time context, and ask Qwen about bounded map context.",
      type: "website",
      images: [{ url: socialImage, width: 1731, height: 909, alt: "Kansas Frontier Matrix map and source context" }],
    },
    twitter: {
      card: "summary_large_image",
      title: "Kansas Frontier Matrix Explorer",
      description: "Start on a real MapLibre Kansas vector context, inspect place and time context, and ask Qwen about bounded map context.",
      images: [socialImage],
    },
    icons: {
      icon: "/favicon.svg",
      shortcut: "/favicon.ico",
    },
  };
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}<PersistentSelectMenus /></body>
    </html>
  );
}
