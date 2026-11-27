const gtr = "https://www.ams.usda.gov/sites/default/files/media";

export const replays = [
  {
    id: "kansas-gulf-2026",
    label: "Kansas–Gulf wheat freight · November 2026",
    dates: ["2026-11-18", "2026-11-19", "2026-11-26"],
    entries: [
      {
        published: "2026-11-19",
        kind: "USDA freight analysis",
        title: "Third-quarter wheat landed costs and November rail tariffs",
        detail: "The November 19 report describes selected wheat shipping routes and lists a Wichita–Houston hard red winter wheat shuttle tariff. The tariff and fuel surcharge describe a published lane reference. A particular shipment can incur additional costs.",
        source: `${gtr}/GTR11192026.pdf`,
        observations: ["2026-11-06", "2026-11-13"],
      },
      {
        published: "2026-11-26",
        kind: "USDA market report",
        title: "New weekly Kansas–Gulf wheat prices and Gulf inspections",
        detail: "Table 2a gives another weekly spread observation. Table 18 reports inspections by commodity and port region. The inspection totals do not identify the Kansas origin of any cargo.",
        source: `${gtr}/GTR11262026.pdf`,
        observations: ["2026-11-13", "2026-11-20"],
      },
    ],
  },
  {
    id: "panama-2023",
    label: "Panama Canal booking restrictions · 2023–24",
    dates: ["2023-10-29", "2023-10-30", "2023-11-09", "2023-11-23", "2023-12-15", "2024-01-16"],
    entries: [
      {
        published: "2023-10-30",
        effective: "2023-11-03",
        kind: "Official restriction",
        title: "Panama Canal announces fewer booking slots",
        detail: "The Canal Authority scheduled successive reductions in ship reservations as water availability fell. The order covers Canal booking slots. Exposure for a Kansas wheat shipment depends on the actual port, destination and itinerary.",
        source: "https://pancanal.com/wp-content/uploads/2023/01/ADV48-2023-Reduction-in-Transits-Due-to-the-Ongoing-Deficit-in-Precipitation-in-the-Canal-Watershed.pdf",
      },
      {
        published: "2023-11-09",
        kind: "USDA market report",
        title: "Weekly spread observations surrounding the first slot reduction",
        detail: "Table 2a lets you compare the Kansas–Gulf wheat spread before and on the date the first slot reduction began. The dates alone cannot establish a price effect.",
        source: `${gtr}/GTR11092023.pdf`,
        observations: ["2023-10-27", "2023-11-03"],
      },
      {
        published: "2023-11-23",
        kind: "USDA shipping context",
        title: "USDA assesses impacts on U.S. dry-bulk grain routes",
        detail: "The feature describes restrictions on Gulf-to-East Asia shipping and discusses corn and soybean exposure. Use Table 2a separately for Kansas wheat market context.",
        source: `${gtr}/GTR11232023.pdf`,
        observations: ["2023-11-10", "2023-11-17"],
      },
      {
        published: "2023-12-15",
        effective: "2024-01-16",
        kind: "Official amendment",
        title: "New advisory replaces the October reduction plan",
        detail: "The Canal Authority announced increased daily transit availability beginning January 16, 2024. Compare the announcement date with the planned start to see when the revised schedule became known.",
        source: "https://pancanal.com/en/panama-canal-to-increase-daily-transits-to-24-starting-in-january/",
      },
    ],
  },
];

export const sourceGuides = [
  {
    title: "USDA AMS grain transportation datasets",
    href: "https://www.ams.usda.gov/services/transportation-analysis/gtr-datasets",
    description: "Find the Kansas–Gulf hard red winter wheat spread in Table 2a and selected rail tariffs in Table 6. Use the archived issue when replaying an earlier date.",
  },
  {
    title: "Surface Transportation Board rail service",
    href: "https://www.stb.gov/reports-data/rail-service-data/",
    description: "Compare weekly Class I rail performance at the published carrier or network scope. Check the scope before applying it to a specific lane.",
  },
  {
    title: "USDA FAS export sales and trade data",
    href: "https://apps.fas.usda.gov/opendatawebv2/",
    description: "Check export commitments, reported shipments and trade data separately. Match commodity, destination and marketing year before comparing.",
  },
  {
    title: "Kansas road conditions and detours",
    href: "https://www.ksdot.gov/travel/travel-conditions/kandrive",
    description: "Inspect current road closures and restrictions before comparing your own truck delivery costs.",
  },
  {
    title: "Kansas crop progress and condition",
    href: "https://www.nass.usda.gov/Statistics_by_State/Kansas/Publications/Crop_Progress_and_Condition/",
    description: "Compare the report week with harvest progress. State estimates describe the season at statewide scale.",
  },
  {
    title: "Midwest diesel history",
    href: "https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=W&n=PET&s=EMD_EPD2D_PTE_R20_DPG",
    description: "Use the weekly regional series as context. Enter your own hauling charge in the calculator.",
  },
  {
    title: "U.S. trade notices in the Federal Register",
    href: "https://www.federalregister.gov/agencies/trade-representative-office-of-united-states",
    description: "Read the notice and linked official PDF for product scope, publication date and effective dates. Check subsequent amendments.",
  },
  {
    title: "USDA FGIS grain inspection reports",
    href: "https://fgisonline.ams.usda.gov/exportgrainreport/",
    description: "Check grain inspected for export by date, commodity and port. Inspections also have a separate reporting window from cash-market observations.",
  },
];

/** @param {(typeof replays)[number]} replay @param {string} cutoff */
export function evidenceByDate(replay, cutoff) {
  return replay.entries.filter((entry) => entry.published <= cutoff);
}

/** @param {string} earlier @param {string} later */
export function compareSpreads(earlier, later) {
  // Convert signed dollars per bushel to integer cents before subtracting.
  /** @param {string} input */
  const cents = (input) => {
    const value = input.trim();
    if (!/^[+-]?\d{1,3}(?:\.\d{1,2})?$/.test(value)) return null;
    const [whole, fractional = ""] = value.replace(/^[+-]/, "").split(".");
    const amount = Number(whole) * 100 + Number(fractional.padEnd(2, "0"));
    return amount && value.startsWith("-") ? -amount : amount;
  };

  const first = cents(earlier);
  const second = cents(later);
  if (first === null || second === null) return null;
  return second - first;
}
