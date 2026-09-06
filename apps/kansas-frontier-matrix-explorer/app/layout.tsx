import type { Metadata } from "next";
import { headers } from "next/headers";
import "./globals.css";
import "./transformation.css";
import "../../../packages/ui/src/layer-library.css";
import "./site-layer-library.css";
import OperationalSpine from "./operational-spine";

const fallbackBase = new URL("https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site");

export async function generateMetadata(): Promise<Metadata> {
  const requestHeaders = await headers();
  const host = requestHeaders.get("x-forwarded-host")?.split(",")[0]?.trim() ?? requestHeaders.get("host")?.trim();
  const forwardedProtocol = requestHeaders.get("x-forwarded-proto")?.split(",")[0]?.trim();
  const protocol = forwardedProtocol === "http" || forwardedProtocol === "https"
    ? forwardedProtocol
    : host?.startsWith("localhost") || host?.startsWith("127.0.0.1") ? "http" : "https";
  let metadataBase = fallbackBase;
  if (host) {
    try { metadataBase = new URL(`${protocol}://${host}`); } catch { /* Use the deployed canonical host. */ }
  }
  const socialImage = new URL("/og-guided.png", metadataBase).toString();

  return {
    title: "Kansas Frontier Matrix Explorer",
    description: "Explore Kansas map data, inspect evidence and time, and build custom public-safe reports from the active map context.",
    metadataBase,
    openGraph: {
      title: "Kansas Frontier Matrix Explorer",
      description: "Explore the map, inspect records, and build custom reports. Synthetic and generalized demonstration data only.",
      type: "website",
      images: [{ url: socialImage, width: 1731, height: 909, alt: "Kansas Frontier Matrix demonstration evidence network" }],
    },
    twitter: {
      card: "summary_large_image",
      title: "Kansas Frontier Matrix Explorer",
      description: "Explore the map, inspect records, and build custom reports. Synthetic and generalized demonstration data only.",
      images: [socialImage],
    },
    icons: {
      icon: "/favicon.svg",
      shortcut: "/favicon.svg",
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
      <body className="antialiased">
        <OperationalSpine />
        {children}
      </body>
    </html>
  );
}
