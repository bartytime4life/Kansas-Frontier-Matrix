import type { Metadata } from "next";
import { headers } from "next/headers";
import "./globals.css";

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
    description: "Explore Kansas through a MapLibre vector-map-first Living Atlas, then use bounded evidence, time, reports, and Qwen context when needed.",
    metadataBase,
    openGraph: {
      title: "Kansas Frontier Matrix Explorer",
      description: "Start on a real MapLibre Kansas vector context, inspect place and time context, and ask Qwen about bounded demonstration data.",
      type: "website",
      images: [{ url: socialImage, width: 1731, height: 909, alt: "Kansas Frontier Matrix demonstration evidence network" }],
    },
    twitter: {
      card: "summary_large_image",
      title: "Kansas Frontier Matrix Explorer",
      description: "Start on a real MapLibre Kansas vector context, inspect place and time context, and ask Qwen about bounded demonstration data.",
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
      <body className="antialiased">{children}</body>
    </html>
  );
}
