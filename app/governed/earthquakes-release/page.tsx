import Link from "next/link";
import { requireChatGPTUser } from "../../chatgpt-auth";
import { ReleaseConsole } from "../../water-release-console";
export const dynamic = "force-dynamic";
export const metadata = { title: "Release an earthquake package" };

export default async function Page() {
  await requireChatGPTUser("/governed/earthquakes-release");
  return <main style={{ maxWidth: 780, margin: "40px auto", padding: 24, lineHeight: 1.6, display: "grid", gap: 16 }}>
    <Link href="/">← Explorer</Link>
    <h1 style={{ margin: 0 }}>Release an earthquake package</h1>
    <p style={{ margin: 0 }}>Owner-only (ADR-0049). Stage a prepared USGS ComCat earthquake package from your computer, then activate it here with its release decision. The reviewed earthquake layer serves only the active package, and only while its decision is valid. Records are catalog solutions, not shaking estimates or alerts, and the Kansas context envelope is not the state boundary. Earthquake, other hazard, soil, weather and water packages, decisions and routes are separate.</p>
    <ol style={{ margin: 0 }}>
      <li>On your computer, with <code>KFM_WATER_WORKER_TOKEN</code> set: <code>tools/release/earthquake_release.py cycle --root /absolute/private/KFM-data --year 2025 --owner @your-login --site-url https://this-site</code> (captures the year&apos;s twelve ComCat months, packages, decides and stages here).</li>
      <li>Paste the decision file below and press <strong>Activate package</strong>.</li>
      <li>If something is wrong, press <strong>Withdraw active package</strong>; the layer stops serving at once.</li>
    </ol>
    <ReleaseConsole kind="earthquakes" />
  </main>;
}
