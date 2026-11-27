// One acre-foot lifted one foot, expressed as hydraulic kWh.
// K-State MF2360 uses 43,560 ft³/ac-ft, 62.4 lbf/ft³, and 1,980,000 ft-lbf/hp-h.
const HYDRAULIC_KWH_PER_ACRE_FOOT_FOOT = (43560 * 62.4 / 1980000) * 0.746;

function decimal(text, min, max) {
  const value = typeof text === "string" && /^\s*(?:\d+(?:\.\d*)?|\.\d+)\s*$/.test(text)
    ? Number(text)
    : NaN;
  return Number.isFinite(value) && value >= min && value <= max ? value : null;
}

/** @param {{ acres: string, depth: string, head: string, efficiency: string, rate: string }} input */
export function pumpingScenario(input) {
  const acres = decimal(input.acres, 0.01, 100000);
  const depth = decimal(input.depth, 0, 120);
  const head = decimal(input.head, 0, 3000);
  const efficiency = decimal(input.efficiency, 1, 100);
  const rate = decimal(input.rate, 0, 10);
  if (acres === null || depth === null || head === null || efficiency === null || rate === null) return null;

  if (depth > 0 && head === 0) return null;
  const acreFeet = acres * depth / 12;
  const energyKwh = acreFeet * head * HYDRAULIC_KWH_PER_ACRE_FOOT_FOOT / (efficiency / 100);
  const energyCost = energyKwh * rate;
  return { acreFeet, energyKwh, energyCost, costPerAcre: energyCost / acres };
}

/** @param {{ acres: string, production: string, utilization: string, headCount: string, intake: string, days: string }} input */
export function forageScenario(input) {
  const acres = decimal(input.acres, 0.01, 100000);
  const production = decimal(input.production, 0, 50000);
  const utilization = decimal(input.utilization, 0, 100);
  const headCount = decimal(input.headCount, 1, 100000);
  const intake = decimal(input.intake, 0.01, 100);
  const days = decimal(input.days, 1, 366);
  if (acres === null || production === null || utilization === null || headCount === null ||
    !Number.isInteger(headCount) || intake === null || days === null || !Number.isInteger(days)) return null;

  const usablePounds = acres * production * utilization / 100;
  const dailyDemand = headCount * intake;
  const demandPounds = dailyDemand * days;
  return { usablePounds, demandPounds, balancePounds: usablePounds - demandPounds, daysOfSupply: usablePounds / dailyDemand };
}
