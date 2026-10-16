import type { Metadata } from "next";
import Link from "next/link";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";

export const metadata: Metadata = {
  title: "Privacy and contact · Kansas Frontier Matrix",
  description: "Website privacy, external map services, optional accounts, device storage and contact for Kansas Frontier Matrix.",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/privacy` },
};

export default function PrivacyPage() {
  return <div className="about-page">
    <nav className="about-nav" aria-label="Privacy page navigation"><div className="brand-lockup"><span className="mark" aria-hidden="true">KFM</span><span><strong>Kansas Frontier Matrix</strong><small>Privacy + contact</small></span></div><Link href="/">Open the map</Link><Link href="/about">About</Link></nav>
    <main className="about-content">
      <header className="about-hero"><div><span>WEBSITE INFORMATION</span><h1>Privacy and contact</h1><p>Last updated October 16, 2026. This notice describes this GoDaddy-hosted website. Linked services have their own privacy practices.</p></div></header>
      <section className="about-section"><h2>Who to contact</h2><p>Kansas Frontier Matrix is an owner-built spatial knowledge project by Andy Barta. For website, privacy or correction questions, email <a href="mailto:Andy.barta.pro@gmail.com">Andy.barta.pro@gmail.com</a>. Please start with a general description and leave out passwords, private records and precise sensitive locations.</p></section>
      <section className="about-section"><h2>Public maps and external services</h2><p>You can browse public map context and this information without an account. Map tiles, imagery and some source requests contact external providers. Those providers and the hosting service can receive connection information such as IP addresses and request URLs. A map request can reveal the geographic area being viewed. Source attribution and provider links appear with the map content.</p></section>
      <section className="about-section"><h2>Information on your device</h2><p>Supported saved map views, settings, reports and stories can use browser storage. Local report downloads save files on your device. Clear this site's browser storage to remove its saved browser state; downloaded files are managed separately through your device. Local-file preview and any separate upload or submission workflow have different purposes: read the relevant control before providing a file.</p></section>
      <section className="about-section"><h2>Optional location and accounts</h2><p>The Locate control asks your browser for location permission. You can decline it and use the map manually. Signing in to an enabled account service uses session cookies and server-side account records. Optional PC-assisted research, when configured, sends submitted questions and bounded evidence to the owner's separate worker. Avoid including sensitive personal information in research questions. The public map does not require that optional service.</p></section>
      <section className="about-section"><h2>Retention, email and your choices</h2><p>Hosting security and request-log retention is controlled by the provider. Private account and operational records have service-specific controls; this notice does not promise immediate deletion or a fixed host retention period. Contact the address above about access, correction or deletion requests. Opening an email link uses your email application; you choose whether to send the message. Email and external services are processed by their respective providers.</p><p><Link href="/about">Read the project guide and evidence limitations</Link></p></section>
    </main>
  </div>;
}
