/** Existing public tools and source context, grouped by question rather than one field site. */
export type ResearchPathway = {
  id: string;
  title: string;
  question: string;
  summary: string;
  scope: string;
  tools: readonly { label: string; href: string; scope: string }[];
  sourceIds: readonly string[];
  boundary: string;
  connections: readonly string[];
  topicHref: string;
};

export const RESEARCH_PATHWAYS: readonly ResearchPathway[] = [
  {
    id: "water", title: "Water & watersheds",
    question: "How do rivers, drought and water samples tell different parts of the story?",
    summary: "Compare measured flow, assessed drought and sampled chemistry, then inspect their geographic context.",
    scope: "105-county drought record · 3 river gauges · 1 chemistry station",
    tools: [
      { label: "River Flow Lab", href: "/labs/river-flow", scope: "Daily mean discharge at three selected Kansas gauges; compare dates when both gauges reported." },
      { label: "County Drought Lab", href: "/labs/county-drought", scope: "105 Kansas counties · 313 weekly assessments · 2020–2025." },
      { label: "Water Chemistry", href: "/labs/water-chemistry", scope: "Dissolved nitrate near Sedgwick · 2019–2020 compared with 2021–2022." },
    ],
    sourceIds: ["usgs-streamflow", "usgs-wbd-watersheds", "noaa-nwps-gauges"],
    boundary: "Three gauges are not statewide flow coverage. Drought percentages describe county area, not drought days; one station’s nitrate samples do not describe a whole watershed. Observations and forecasts remain separate.",
    connections: ["agriculture", "weather"], topicHref: "/topics#water",
  },
  {
    id: "weather", title: "Weather, climate & air",
    question: "Which changes were observed, and which were modeled?",
    summary: "Inspect daily heat, rain, reported air quality and sunlight on each source’s own clock.",
    scope: "3 weather stations · 12 reporting AQI counties · 3 modeled sunlight points",
    tools: [
      { label: "Heat & Rain Lab", href: "/labs/heat-and-rain", scope: "Dodge City, Wichita and Topeka · daily station observations · 2020–2025." },
      { label: "Daily Air Quality Lab", href: "/labs/daily-air-quality", scope: "12 Kansas counties reported during 2020–2025; reporting coverage varies by year and date." },
      { label: "Sunlight & Sky Lab", href: "/labs/sunlight-and-sky", scope: "Three NASA POWER query points · modeled daily horizontal sunlight energy · 2020–2025." },
    ],
    sourceIds: ["nws-radar", "nws-forecast-wind", "noaa-goes-geocolor"],
    boundary: "Weather stations do not represent every county. Reported monitor AQI is not personal exposure. Sunlight uses a nominal 1° model grid, not a station reading or panel yield; forecasts and observations retain different valid times.",
    connections: ["water", "ecology"], topicHref: "/topics#weather",
  },
  {
    id: "agriculture", title: "Agriculture & soils",
    question: "What changes below ground, across the season and along the route to market?",
    summary: "Connect measured soil conditions with season scenarios and reported grain markets without turning context into advice.",
    scope: "2 soil stations · 5 measured depths · Kansas regional bids and season scenarios",
    tools: [
      { label: "Soil Profile Lab", href: "/labs/soil-profile", scope: "Manhattan 6 SSW and Oakley 19 SSW · five sensor depths · daily records · 2020–2025." },
      { label: "Farm season planner", href: "/farm-season", scope: "Planting, grazing and pumping scenarios using named references and your assumptions." },
      { label: "Grain markets & freight", href: "/science/wheat-trade", scope: "Reported Kansas regional grain bids, delivery-cost scenarios and selected historical freight cases." },
    ],
    sourceIds: ["nrcs-ssurgo-soils", "noaa-cpc-drought-outlook", "kgs-depth-to-water"],
    boundary: "Five sensor depths are not a continuous soil column or plant-available water. Soil map units are mixtures, not a field test. Seasonal forecasts and High Plains 2022–2024 depth estimates are separate context, not agronomic advice or current well levels.",
    connections: ["water", "infrastructure"], topicHref: "/topics#agriculture",
  },
  {
    id: "geology", title: "Geology & terrain",
    question: "What can recorded events and rendered landforms establish?",
    summary: "Explore earthquake records, elevation context and mapped subsurface references while preserving their different scales.",
    scope: "Earthquakes around Kansas · statewide terrain and subsurface display context",
    tools: [
      { label: "Earthquake Catalog Lab", href: "/labs/earthquakes", scope: "Four-year comparisons within 2010–2025 · M ≥1 USGS snapshot around Kansas." },
      { label: "Terrain & elevation", href: "/topics#terrain", scope: "Kansas map controls for elevation, slope and hillshade; acquisition dates vary by source." },
      { label: "Geology & subsurface", href: "/topics#geology", scope: "KGS well, core and resource map references; query completeness and source dates vary." },
    ],
    sourceIds: ["usgs-earthquakes", "usgs-3dep-hillshade", "usgs-3dep-slope"],
    boundary: "The snapshot includes nearby states; catalog detection varies. Magnitude types vary and reported depths are estimates; counts do not establish cause or predict shaking. Hillshade and slope images are display context, not numerical terrain measurements, surveyed work units or certified accuracy.",
    connections: ["water", "infrastructure"], topicHref: "/topics#geology",
  },
  {
    id: "ecology", title: "Land cover & ecosystems",
    question: "Where do records, mapped land and sampled vegetation overlap?",
    summary: "Read broad ecological context first, then inspect one prairie tile as a bounded case study.",
    scope: "Provider occurrence aggregates and land areas · no reviewed statewide species inventory",
    tools: [
      { label: "Flora & fauna in the Observatory", href: "/observatory", scope: "GBIF annual plant and animal record density in coarse hexagons; source tiles capped at zoom 6." },
      { label: "Ecology & land cover", href: "/topics#ecology", scope: "Land-cover, imagery and public/protected-land context; provider dates and availability differ." },
      { label: "Konza terrain case study", href: "/labs/terrain", scope: "One sampled Konza Prairie NEON tile · historical provider preview · scientific review pending." },
    ],
    sourceIds: ["usgs-padus-lands", "kdwp-wildlife-areas", "usgs-3dhp-hydrography"],
    boundary: "Record density is not species abundance, absence or movement. Land-cover classes do not establish habitat condition, and mapped land areas do not grant access. The Konza case does not establish statewide vegetation or change.",
    connections: ["weather", "agriculture"], topicHref: "/topics#ecology",
  },
  {
    id: "history", title: "History & cultural landscapes",
    question: "Which places, dates and accounts survive in the record?",
    summary: "Follow selected postal, architectural and newspaper records beside their original sources and historical map context.",
    scope: "Douglas County post offices · Fort Larned buildings · 2 Abilene newspaper issues",
    tools: [
      { label: "Boom & Ghost Towns", href: "/labs/ghost-towns", scope: "Documented Douglas County post-office events from the Blevins–Helbock V1 (2021) source." },
      { label: "Fort Larned photographs", href: "/labs/fort-larned", scope: "Three selected buildings · July 1965 survey photographs · Library of Congress and NPS context." },
      { label: "Newspaper Pulse", href: "/labs/newspaper-pulse", scope: "Two terms across two digitized issues of the Abilene Weekly Reflector." },
    ],
    sourceIds: ["kdot-roads-1918", "nps-historic-trails", "nps-nrhp-places"],
    boundary: "These are selected cases, not complete statewide history. Postal events do not prove town abandonment; OCR and digitization shape term counts. Approximate trails and representative historic-place points are not boundaries or access permission.",
    connections: ["communities", "infrastructure"], topicHref: "/topics#history",
  },
  {
    id: "infrastructure", title: "Infrastructure & energy",
    question: "How do built networks and energy records change the picture?",
    summary: "Inspect bridge inventory, long energy series and a selected crossing without confusing inventory with live condition.",
    scope: "KDOT bridge inventory · 26 energy series · 1 Garden City aerial comparison",
    tools: [
      { label: "Built Kansas", href: "/labs?story=built-kansas", scope: "24,877 returned state/local bridge inventory records in the bundled KDOT snapshot." },
      { label: "Energy Shift", href: "/labs?story=energy-shift", scope: "26 Kansas EIA energy production and consumption series · 1960–2024." },
      { label: "Kansas Then & Now", href: "/labs/then-now", scope: "Two aligned aerial editions at one Arkansas River crossing in Garden City." },
    ],
    sourceIds: ["kdot-bridges-state", "kdot-bridges-local", "kdot-rail-active"],
    boundary: "Inventory records can repeat structures and are not current safety findings or complete construction history. Energy accounting series overlap; do not add them indiscriminately. Aerial edition labels do not establish exact local flight dates.",
    connections: ["communities", "geology"], topicHref: "/topics#engineering",
  },
  {
    id: "communities", title: "People, counties & places",
    question: "How do population and living conditions differ across Kansas?",
    summary: "Compare county estimates, inspect uncertainty and bring connected indicators into one place-based workspace.",
    scope: "105 counties · 2020–2025 population · 3 nonoverlapping ACS five-year periods",
    tools: [
      { label: "County Pulse", href: "/labs?story=census-mosaic", scope: "105 counties · annual population estimates, births, deaths and migration · 2020–2025." },
      { label: "County Conditions", href: "/labs?story=county-conditions", scope: "105 counties · three ACS five-year periods spanning 2010–2024 · 90% margins of error." },
      { label: "County Observatory", href: "/labs/observatory", scope: "County and peer comparisons with linked indicators; coverage differs by measure. Private CSV joins stay local." },
    ],
    sourceIds: ["census-counties", "census-congress-119"],
    boundary: "ACS five-year estimates describe periods, not single years; dollar values use each vintage’s dollars. The 2020 population components cover a partial year. Map Census counts retain their 2020 edition. Area aggregates do not identify individuals.",
    connections: ["history", "water"], topicHref: "/topics#people",
  },
] as const;

/** Compare the registered context behind a pathway; tool data keep their separate scopes. */
export function pathwayComparisonHref(pathway: ResearchPathway): string {
  return `/research?${new URLSearchParams({ compare: pathway.sourceIds.join(",") })}#comparison`;
}
