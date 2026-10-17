import Link from "next/link";
import { headers } from "next/headers";
import { getChatGPTUser } from "./chatgpt-auth";
import styles from "./data/workspace.module.css";

// This host check selects explanatory content only. It never grants data access.
export async function localSignInNotice(destination: "/data" | "/stewards") {
  const host = (await headers()).get("host");
  if (await getChatGPTUser()) return null;
  const local = Boolean(host && ["127.0.0.1:4173", "localhost:4173", "127.0.0.1:5173", "localhost:5173"].includes(host));
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/" className={styles.brand}>KFM <span>{local ? "Local Explorer" : "Explorer"}</span></Link></header>
    <section className={styles.intro}>
      <p className={styles.eyebrow}>PRIVATE WORKSPACE</p>
      <h1>{local ? "Sign in on the private Site" : "Private workspace unavailable on this host"}</h1>
      <p>{local ? "Data submissions and steward review require the private Site’s sign-in service. That service is unavailable at this local address." : "Data submissions and steward review use the separate private Site. Its identity and storage services are not connected to this application."}</p>
      {!local && <p>Public chat remains available without login. Administrator sign-in on the map does not grant access to this private workspace.</p>}
      <p><a href={`https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site${destination}`} target="_blank" rel="noopener noreferrer">Open the private {destination === "/data" ? "Data" : "Steward"} workspace ↗</a></p>
      <Link href="/">{local ? "Return to the local map" : "Return to the public map"}</Link>
    </section>
  </main>;
}
