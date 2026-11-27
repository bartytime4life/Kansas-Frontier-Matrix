import { PUBLIC_SITE_ORIGIN } from "../../crawler-discovery";
import ScienceComparison from "./comparison-client";
import styles from "./comparison.module.css";

export const metadata = {
  title: "Compare Topeka science years | Kansas Frontier Matrix",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/science/compare` },
  description: "Compare two years of Topeka precipitation and modeled sunlight alongside Shawnee County drought assessments and reported air quality.",
};

export default function ScienceComparisonPage() {
  return <main className={styles.page}><div className={styles.frame}>

    <ScienceComparison><header className={styles.hero}>
      <h1>Compare Topeka science years</h1>
      <p>Put Topeka and Shawnee County on the same monthly timeline. Compare two years of precipitation, drought, reported air quality and modeled sunlight from 2020–2025.</p>
    </header></ScienceComparison>
  </div></main>;
}
