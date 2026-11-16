import type { OfficialContextId } from "./live-context";

/** Plain-language, crawlable entry pages. Each guide links into the Explorer with
 * fixed public-context layers turned on; it adds no source, claim or evidence. */
export type LandingGuide = Readonly<{
  slug: string;
  title: string;
  description: string;
  kicker: string;
  intro: readonly string[];
  layers: readonly OfficialContextId[];
  center: readonly [number, number];
  zoom: number;
  ideas: readonly string[];
  caution: string;
}>;

export const LANDING_GUIDES: readonly LandingGuide[] = Object.freeze([
  {
    slug: "frontier-trails",
    title: "Frontier trails across Kansas",
    description: "Map the Santa Fe, Oregon, California and Pony Express trails and the Chisholm and Western cattle trails across Kansas, with forts, crossings and ruts.",
    kicker: "HISTORY · TRAILS",
    intro: [
      "Kansas sat on the main overland routes west. The Santa Fe Trail carried trade between Missouri and Santa Fe from 1821 until the railroad replaced it around 1880. Emigrants on the Oregon and California trails crossed northeast Kansas from the 1840s, and Pony Express riders followed much of the same corridor in 1860–1861.",
      "After the Civil War, cattle were driven north from Texas to Kansas railheads such as Abilene and Ellsworth on the Chisholm Trail, and later to Dodge City on the Western Trail.",
      "This map draws the National Park Service's mapped alignments where they cross Kansas, with public trail sites you can click for their story.",
    ],
    layers: ["nps-historic-trails", "nps-trail-places"],
    center: [-97.4, 38.6], zoom: 6.2,
    ideas: [
      "Follow the Santa Fe Trail from Council Grove to the Arkansas River crossings near Dodge City.",
      "See where the Oregon, California and Pony Express routes share a path near Topeka and Marysville.",
      "Compare the dashed cattle-trail routes with the railroad towns they led to.",
    ],
    caution: "Trail lines are approximate alignments and most of the land along them is private. A line or marker is not permission to enter land.",
  },
  {
    slug: "historic-places",
    title: "Historic places in Kansas",
    description: "Find Kansas buildings, districts, sites and landmarks listed on the National Register of Historic Places, alongside the frontier trails.",
    kicker: "HISTORY · PLACES",
    intro: [
      "The National Register of Historic Places is the federal list of buildings, districts, sites, structures and objects judged worth preserving. Kansas has well over a thousand listings, from courthouses and schoolhouses to bridges and ranches.",
      "This map shows the public point locations the National Park Service publishes for Kansas listings, with the frontier trails for context. Click a point for its type, place and listing date.",
    ],
    layers: ["nps-nrhp-places", "nps-historic-trails"],
    center: [-98.2, 38.5], zoom: 6.4,
    ideas: [
      "Zoom into a county seat to see its listed downtown buildings and districts.",
      "Look for National Historic Landmarks, shown with an outer ring.",
      "Find listed places that sit along the old trail corridors.",
    ],
    caution: "Points are representative locations, not property boundaries. Sensitive and restricted sites are withheld by the National Park Service, and listing does not mean a place is open to visitors.",
  },
  {
    slug: "hunting-and-wildlife-areas",
    title: "Kansas wildlife areas and walk-in hunting access",
    description: "Map Kansas Department of Wildlife and Parks public wildlife areas and Walk-In Hunting Access tracts with public and protected lands.",
    kicker: "OUTDOORS · ACCESS",
    intro: [
      "Most of Kansas is privately owned. The Kansas Department of Wildlife and Parks manages public wildlife areas and runs the Walk-In Hunting Access program, which opens enrolled private land to public hunting during set seasons.",
      "This map shows KDWP's public wildlife areas and current Walk-In Hunting Access tracts, with the national inventory of public and protected lands for context. Click an area or tract for its name, acres and species.",
    ],
    layers: ["kdwp-wildlife-areas", "kdwp-wiha-access", "usgs-padus-lands"],
    center: [-98.3, 38.5], zoom: 6.4,
    ideas: [
      "Find wildlife areas and walk-in tracts near you before checking KDWP's current atlas.",
      "Compare walk-in tracts with public and protected lands nearby.",
      "Click a tract to see its acres and listed species.",
    ],
    caution: "Boundaries are simplified for display. Seasons, closures and rules change; check KDWP's current atlas and regulations before entering or hunting. Walk-in tracts are private land open only under program rules.",
  },
  {
    slug: "drought-and-water",
    title: "Kansas drought outlook, rivers and groundwater",
    description: "See the seasonal drought outlook for Kansas beside live river gauges and the mapped High Plains aquifer extent.",
    kicker: "WATER · CLIMATE",
    intro: [
      "Water shapes Kansas farming and towns. Western Kansas relies heavily on groundwater from the High Plains aquifer, while rivers and reservoirs supply much of the east.",
      "This map sets NOAA's seasonal drought outlook beside current U.S. Geological Survey river gauges and the mapped extent of the High Plains aquifer. Each layer keeps its own date and limits.",
    ],
    layers: ["noaa-cpc-drought-outlook", "usgs-streamflow", "kgs-aquifer-high-plains"],
    center: [-98.4, 38.5], zoom: 6.3,
    ideas: [
      "Check whether the seasonal outlook expects drought to develop, persist or improve over Kansas.",
      "Click river gauges to read their latest provider observations.",
      "See how far the High Plains aquifer extends across western Kansas.",
    ],
    caution: "The drought outlook is a forecast of change, not current drought conditions or a designation. Gauge readings and the aquifer extent are separate products on their own clocks, not irrigation or well advice.",
  },
  {
    slug: "kansas-bridges",
    title: "Kansas bridges on one map",
    description: "Map Kansas highway and local road bridges as counted circles that split into single bridges, with build year, length, traffic and recorded status.",
    kicker: "ROADS · BRIDGES",
    intro: [
      "Kansas has close to 25,000 bridges longer than 20 feet. In November 2026 the Kansas Department of Transportation's inventory listed about 5,600 on state highways and about 19,300 on county and city roads.",
      "This map counts nearby bridges in numbered circles that split apart as you zoom in, until each bridge sits at its recorded point. Colour shows the recorded build year, larger dots are longer bridges, a red ring means recorded closed and an amber ring means posted with a restriction.",
      "Select a bridge for its record: what it carries and crosses, when it was built, its material and design, length, lanes and daily traffic.",
    ],
    layers: ["kdot-bridges-state", "kdot-bridges-historic", "kdot-bridges-closed"],
    center: [-97.6, 38.6], zoom: 6.3,
    ideas: [
      "Find the longest state highway structure in the inventory, the Interstate 135 viaduct in Wichita at about 12,500 feet.",
      "Zoom into a river town such as Topeka and compare the build years of its Kansas River crossings.",
      "Turn on Bridges · local roads in Map layers to add the county and city bridges, including about 4,500 with a recorded build year before 1950.",
    ],
    caution: "Bridge records are the provider's inventory and may lag. A recorded status or rating is not a live closure notice, a safety determination or navigation advice, and a point is not the deck footprint.",
  },
] satisfies LandingGuide[]);

export const landingGuide = (slug: string) => LANDING_GUIDES.find(guide => guide.slug === slug);

/** Explorer deep link with the guide's layers on and the view framed on Kansas. */
export const guideMapHref = (guide: LandingGuide) =>
  `/?ctx=${guide.layers.join(",")}&c=${guide.center[0]},${guide.center[1]}&z=${guide.zoom}`;
