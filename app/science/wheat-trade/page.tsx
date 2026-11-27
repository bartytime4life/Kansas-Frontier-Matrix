import Link from "next/link";
import { GrainMarketBudget } from "../../field-decision-tools";
import TradeReplay from "./trade-replay";
import styles from "./wheat-trade.module.css";

export const metadata = {
  title: "Kansas grain markets and freight | Kansas Frontier Matrix",
  alternates: { canonical: "https://kansasfrontiermatrix.com/science/wheat-trade" },
  description: "Compare reviewed Kansas grain bids, estimate delivery and production costs, and replay dated freight and trade reports.",
};

export default function WheatTradePage() {
  return (
    <main className={styles.page}>
      <div className={styles.frame}>
        <nav className={styles.navigation} aria-label="Wheat trade navigation">
          <Link href="/science">← Science tools</Link>
          <Link href="/">KFM Explorer</Link>
          <Link href="/topics#agriculture">Agriculture &amp; soils</Link>
          <Link href="/farm-season">Farm season planner</Link>
        </nav>
        <header className={styles.header}>
          <h1>Kansas grain markets and freight</h1>
          <p>Compare reported cash bids by Kansas region, work out what a delivery pays after costs, and follow the wheat market from Kansas to the Gulf.</p>
        </header>
        <section className={`${styles.section} ${styles.market}`} aria-labelledby="grain-bids">
          <h2 id="grain-bids">Kansas cash bids &amp; break-even</h2>
          <p>Choose wheat, corn, sorghum or soybeans. Use a reviewed regional average or enter your own offer. For basis quoted against a futures contract, see the original USDA report.</p>
          <GrainMarketBudget />
        </section>
        <TradeReplay />
      </div>
    </main>
  );
}
