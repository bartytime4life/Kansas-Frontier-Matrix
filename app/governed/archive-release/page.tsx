import Link from "next/link";
import { requireChatGPTUser } from "../../chatgpt-auth";
import { ReleaseConsole } from "../../water-release-console";
export const dynamic = "force-dynamic";
export const metadata = { title: "Manage authorized archive releases" };
export default async function Page() {
  await requireChatGPTUser("/governed/archive-release");
  return <main style={{ maxWidth: 780, margin: "40px auto", padding: 24, lineHeight: 1.6, display: "grid", gap: 16 }}>
    <Link href="/">← Explorer</Link>
    <h1 style={{ margin: 0 }}>Manage authorized archive releases</h1>
    <p style={{ margin: 0 }}>Owner access is required. Upload only the exact packages and objects authorized by the reviewed delivery list, then select a package below. This page cannot create or approve a publication decision.</p>
    <ReleaseConsole kind="archive" />
  </main>;
}
