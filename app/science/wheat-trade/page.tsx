import Link from "next/link";
import TradeReplay from "./trade-replay";
import styles from "./wheat-trade.module.css";

export const metadata = {
  title: "Kansas wheat trade and freight | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/science/wheat-trade" },
  description: "Replay dated freight and trade reports for the Kansas–Gulf hard red winter wheat market.",
};

export default function WheatTradePage() {
  return (
    <main className={styles.page}>
      <div className={styles.frame}>
        <nav className={styles.navigation} aria-label="Wheat trade navigation">
          <Link href="/science">← Science tools</Link>
          <Link href="/">KFM Explorer</Link>
        </nav>
        <header className={styles.header}>
          <h1>Kansas wheat trade and freight</h1>
          <p>Follow hard red winter wheat from the Kansas cash market to the Gulf export market. Replay what reports had been published by a selected date and compare the same price spread across two weeks.</p>
        </header>
        <TradeReplay />
      </div>
    </main>
  );
}
