"use client";

import { useState } from "react";
import { forageScenario, pumpingScenario } from "./scenario-model.mjs";
import styles from "./farm-season.module.css";

const number = new Intl.NumberFormat("en-US", { maximumFractionDigits: 2 });
const dollars = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" });

const pumpingFields = [
  ["acres", "Irrigated acres", "0.01–100,000 acres"],
  ["depth", "Pumped depth", "0–120 inches per acre, including application losses"],
  ["head", "Total dynamic head", "Up to 3,000 ft. Include pumping lift, pressure, elevation and friction."],
  ["efficiency", "Combined pump and motor efficiency", "1–100%. Use a pumping-plant test if available."],
  ["rate", "Energy rate", "$0–$10 per kWh. Check the current utility tariff."],
] as const;

const forageFields = [
  ["acres", "Grazeable acres", "0.01–100,000 acres"],
  ["production", "Forage dry matter over the period", "0–50,000 lb/acre. Use a local estimate or measurement."],
  ["utilization", "Share the herd can consume", "0–100%. Account for residue and losses."],
  ["headCount", "Animals", "1–100,000 head, whole number"],
  ["intake", "Dry-matter intake", "0.01–100 lb per head per day"],
  ["days", "Planning period", "1–366 days, whole number"],
] as const;

function ScenarioField({ label, hint, value, onChange }: {
  label: string;
  hint: string;
  value: string;
  onChange: (value: string) => void;
}) {
  return <label className={styles.field}>
    <span>{label}</span>
    <small>{hint}</small>
    <input value={value} onChange={event => onChange(event.target.value)}
      type="text" inputMode="decimal" autoComplete="off" maxLength={20} />
  </label>;
}

function PumpingScenario() {
  const [input, setInput] = useState({ acres: "", depth: "", head: "", efficiency: "", rate: "" });
  const [calculated, setCalculated] = useState(false);
  const result = calculated ? pumpingScenario(input) : null;
  return <section className={styles.panel} id="pumping" aria-labelledby="pumping-heading">
    <h2 id="pumping-heading">Irrigation pumping cost</h2>
    <p>Estimate seasonal electricity use and cost from your own pumping conditions.</p>
    <div className={styles.fields}>
      {pumpingFields.map(([key, label, hint]) => <ScenarioField key={key}
        label={label} hint={hint} value={input[key]} onChange={value => {
          setInput(previous => ({ ...previous, [key]: value }));
          setCalculated(false);
        }} />)}
    </div>
    <button type="button" onClick={() => setCalculated(true)}>Estimate pumping cost</button>
    <div className={styles.results} role="status" aria-atomic="true">
      {calculated && (result ? <dl>
        <div><dt>Water pumped</dt><dd>{number.format(result.acreFeet)} acre-ft</dd></div>
        <div><dt>Electricity use</dt><dd>{number.format(result.energyKwh)} kWh</dd></div>
        <div><dt>Energy cost</dt><dd>{dollars.format(result.energyCost)}</dd></div>
        <div><dt>Energy cost per acre</dt><dd>{dollars.format(result.costPerAcre)}</dd></div>
      </dl> : <p>Enter a number within each field’s range. Pumping water requires a head greater than zero.</p>)}
    </div>
    <p>Energy charges only. Demand fees, fixed charges and equipment costs are separate. An observed well depth can differ from the pumping lift.</p>
    <a href="https://bookstore.ksre.ksu.edu/pubs/comparing-irrigation-energy-costs_MF2360.pdf">K-State Research and Extension method (PDF)</a>
  </section>;
}

function ForageScenario() {
  const [input, setInput] = useState({ acres: "", production: "", utilization: "", headCount: "", intake: "", days: "" });
  const [calculated, setCalculated] = useState(false);
  const result = calculated ? forageScenario(input) : null;
  const balanceLabel = result?.balancePounds === 0 ? "Forage balance" :
    (result?.balancePounds ?? 0) < 0 ? "Estimated shortfall" : "Estimated surplus";
  return <section className={styles.panel} id="forage" aria-labelledby="forage-heading">
    <h2 id="forage-heading">Pasture forage budget</h2>
    <p>Compare dry matter available for grazing with the herd’s intake over the same period.</p>
    <div className={styles.fields}>
      {forageFields.map(([key, label, hint]) => <ScenarioField key={key}
        label={label} hint={hint} value={input[key]} onChange={value => {
          setInput(previous => ({ ...previous, [key]: value }));
          setCalculated(false);
        }} />)}
    </div>
    <button type="button" onClick={() => setCalculated(true)}>Estimate forage balance</button>
    <div className={styles.results} role="status" aria-atomic="true">
      {calculated && (result ? <dl>
        <div><dt>Usable dry matter</dt><dd>{number.format(result.usablePounds)} lb</dd></div>
        <div><dt>Herd demand</dt><dd>{number.format(result.demandPounds)} lb</dd></div>
        <div><dt>{balanceLabel}</dt><dd>{number.format(Math.abs(result.balancePounds))} lb</dd></div>
        <div><dt>Days of supply at entered intake</dt><dd>{number.format(result.daysOfSupply)}</dd></div>
      </dl> : <p>Enter a number within each field’s range. Use whole numbers for animals and days.</p>)}
    </div>
    <p>Dry-matter quantity only. Forage quality, regrowth and animal needs can change during the period.</p>
    <a href="https://eupdates.agronomy.k-state.edu/eupdates/eUpdate071124.pdf">K-State Extension Agronomy stocking-rate method (PDF)</a>
  </section>;
}

export default function SeasonScenarios() {
  return <div className={styles.scenarios}><PumpingScenario /><ForageScenario /></div>;
}
