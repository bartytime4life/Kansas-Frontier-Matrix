import type { Metadata } from "next";
import { SITE_IDENTITY } from "./site-identity";
import { PersistentSelectMenus } from "./persistent-select-menus";
import "./globals.css";
import "./map-layers.css";
import "./explorer-theme.css";
import "./local-atlas.css";
import "./scene-effects.css";

export async function generateMetadata(): Promise<Metadata> {
  // Canonical metadata is deployment identity, never caller-controlled routing input.
  const metadataBase = new URL(SITE_IDENTITY.canonicalUrl);
  return {
    title: "Kansas Frontier Matrix — Public Preview",
    description: "Explore Kansas maps, source dates, terrain and recorded-log tools. Public data delivery remains release-gated.",
    metadataBase,
    robots: { index: false, follow: false },
    openGraph: { title: "Kansas Frontier Matrix — Public Preview", description: "A separate KFM public edition under review.", type: "website" },
  };
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        {/* Not metadata.icons: metadataBase would make these absolute URLs on the
            canonical host, so every local or preview page load would fetch them
            from the hosted Site. Icons are served by this deployment. */}
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
        <link rel="shortcut icon" href="/favicon.ico" />
      </head>
      <body className="antialiased">{children}<PersistentSelectMenus /></body>
    </html>
  );
}
