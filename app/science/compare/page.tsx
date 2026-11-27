import { PUBLIC_SITE_ORIGIN } from "../../crawler-discovery";
import ScienceComparison from "./comparison-client";
import styles from "./comparison.module.css";

export const metadata = {
  title: "Compare Kansas science years | Kansas Frontier Matrix",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/science/compare` },
  description: "Compare years of daily precipitation, weekly drought, reported air quality and modeled sunlight for Topeka, Wichita or Dodge City.",
};

export default function ScienceComparisonPage() {
  return <main className={styles.page}><div className={styles.frame}>

    <ScienceComparison><header className={styles.hero}>
      <h1>Compare Kansas science years</h1>
      <p>Choose an area and compare two years of precipitation, drought, reported air quality and modeled sunlight from 2020–2025.</p>
    </header></ScienceComparison>
  </div></main>;
}
