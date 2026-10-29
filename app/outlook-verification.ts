import { outlookBandAt, outlookProductName, spcScale, type SpcOutlook } from "./spc-outlook";
import type { ReportKind, StormReports } from "./storm-reports";

/**
 * How today's preliminary storm reports fall against the Day 1 outlook shown,
 * the way SPC verifies its outlooks: only reports made inside the outlook's
 * valid period count, the categorical outlook is checked against every
 * report and a hazard outlook against reports of its own hazard, and each
 * band counts the reports inside it or a higher band (SPC's areas nest).
 */
export type OutlookVerification = Readonly<{
  /** Reports made inside the outlook's valid period, of the hazard checked. */
  total: number;
  /** Per band, lowest to highest: reports inside that band or a higher one. */
  bands: readonly Readonly<{ id: string; name: string; count: number }>[];
  since: string;
  kind: ReportKind | null;
}>;

const HAZARD_KIND = Object.freeze({ torn: "torn", wind: "wind", hail: "hail" } as const);
/** The Day 1 outlook and today's reports cover the same convective day when they end within two hours of each other. */
const SAME_DAY_MS = 2 * 3_600_000;

export function verifyOutlook(outlook: SpcOutlook, reports: StormReports): OutlookVerification | null {
  if (outlook.day !== 1 || reports.day !== "today" || !outlook.validFrom || !outlook.validUntil) return null;
  const from = Date.parse(outlook.validFrom), until = Date.parse(outlook.validUntil);
  if (!Number.isFinite(from) || !Number.isFinite(until) || Math.abs(until - Date.parse(reports.until)) > SAME_DAY_MS) return null;
  const product = outlook.product ?? "cat";
  const kind = product === "cat" ? null : HAZARD_KIND[product];
  const counted = reports.reports.filter(report => (!kind || report.kind === kind) && report.time !== null
    && Date.parse(report.time) >= from && Date.parse(report.time) <= until);
  // TSTM is general thunder, not a severe category: categorical verification starts at Marginal.
  const scale = spcScale(product).filter(step => step.id !== "TSTM");
  const ranks = counted.map(report => outlookBandAt(outlook, report.longitude, report.latitude)?.rank ?? 0);
  return Object.freeze({
    total: counted.length, since: outlook.validFrom, kind,
    bands: Object.freeze(scale.map(step => Object.freeze({ id: step.id, name: step.name, count: ranks.filter(rank => rank >= step.rank).length }))),
  });
}

const CLOCK = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", hour: "2-digit", minute: "2-digit", hourCycle: "h23" });

/** "12 reports since 16:30 UTC: 9 in Marginal or higher, 5 in Slight or higher …" — bands with none above them are left off. */
export function verificationReading(verification: OutlookVerification, product: SpcOutlook["product"]): string {
  const what = verification.kind ? `${outlookProductName(product).toLowerCase()} report` : "report";
  const head = `${verification.total} ${what}${verification.total === 1 ? "" : "s"} since the outlook's ${CLOCK.format(new Date(verification.since))} UTC start`;
  if (!verification.total) return `No ${what}s yet since the outlook's ${CLOCK.format(new Date(verification.since))} UTC start`;
  const shown = verification.bands.filter((step, i) => step.count > 0 || i === 0);
  const inside = shown.map(step => `${step.count} in ${step.name}${verification.kind ? "+" : " or higher"}`).join(", ");
  const outside = verification.total - (verification.bands[0]?.count ?? 0);
  return `${head}: ${inside}${outside ? `; ${outside} outside every ${verification.kind ? "probability" : "risk"} area` : ""}`;
}
