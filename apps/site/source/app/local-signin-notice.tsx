import Link from "next/link";
import { headers } from "next/headers";
import { getChatGPTUser } from "./chatgpt-auth";
import styles from "./data/workspace.module.css";

// This host check selects explanatory content only. It never grants data access.
export async function localSignInNotice(destination: "/data" | "/stewards") {
  const host = (await headers()).get("host");
  if (!host || !["127.0.0.1:4173", "localhost:4173", "127.0.0.1:5173", "localhost:5173"].includes(host)) return null;
  if (await getChatGPTUser()) return null;
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/" className={styles.brand}>KFM <span>Local Explorer</span></Link></header>
    <section className={styles.intro}>
      <p className={styles.eyebrow}>PRIVATE WORKSPACE</p>
      <h1>Sign in on the private Site</h1>
      <p>Data submissions and steward review require the private Site’s sign-in service. That service is unavailable at this local address.</p>
      <p><a href={`https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site${destination}`} target="_blank" rel="noopener noreferrer">Open the private {destination === "/data" ? "Data" : "Steward"} workspace ↗</a></p>
      <Link href="/">Return to the local map</Link>
    </section>
  </main>;
}
