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
  {
    slug: "storms-and-severe-weather",
    title: "Kansas severe storms, outlooks and storm reports",
    description: "See today's Storm Prediction Center outlook for Kansas with preliminary storm reports, active NWS alerts and past-day radar rainfall.",
    kicker: "WEATHER · STORMS",
    intro: [
      "Kansas sits in the heart of the Great Plains, where warm Gulf moisture meets dry western air. Spring and early summer bring most of the state's tornadoes, large hail and damaging winds, but severe storms can form in any month.",
      "This map sets the Storm Prediction Center's Day 1 outlook beside the National Weather Service's preliminary local storm reports from the past three days, the alert areas in effect now, and radar-estimated rainfall for the past 24 hours. Click a report or an alert area for its details.",
    ],
    layers: ["noaa-spc-convective-outlook", "nws-storm-reports", "nws-alerts", "noaa-mrms-qpe-24h"],
    center: [-98.3, 38.5], zoom: 6.3,
    ideas: [
      "Check which outlook category covers your county today, from thunder to high risk.",
      "Compare where hail and wind reports landed with the areas that saw the heaviest radar rainfall.",
      "Click an alert area to read the warning or advisory text the National Weather Service issued.",
    ],
    caution: "Outlooks are forecasts, storm reports are preliminary and rainfall is a radar estimate. This map is not a warning service; follow National Weather Service warnings and local officials when storms threaten.",
  },
  {
    slug: "fire-and-smoke",
    title: "Kansas wildfire weather, heat detections and smoke",
    description: "Map the Storm Prediction Center fire-weather outlook with satellite heat detections, interagency fire reports and smoke plumes over Kansas.",
    kicker: "HAZARDS · FIRE",
    intro: [
      "Grass fires spread quickly on windy, dry Kansas days. Ranchers burn the Flint Hills each spring to keep the tallgrass prairie open, and wind-driven wildfires such as the 2016 Anderson Creek and 2017 Starbuck fires burned hundreds of thousands of acres across Kansas and Oklahoma.",
      "This map shows the Storm Prediction Center's fire-weather outlook for today, satellite heat detections, fire reports from the interagency fire centre and the smoke plumes NOAA analysts traced on satellite imagery.",
    ],
    layers: ["noaa-spc-fire-weather", "nasa-firms-active-fire", "nifc-fire-reports", "noaa-hms-smoke"],
    center: [-98.0, 38.4], zoom: 6.3,
    ideas: [
      "See whether elevated or critical fire weather is forecast over western Kansas today.",
      "In March and April, look for clusters of heat detections over the Flint Hills during the spring burn season.",
      "Follow a smoke plume back toward the heat detections it may have come from.",
    ],
    caution: "A heat detection is not a confirmed wildfire, a report may describe a different incident, and a smoke outline is not an air-quality reading. Check county burn restrictions and red-flag warnings before any burn.",
  },
  {
    slug: "aquifers-and-groundwater",
    title: "Kansas aquifers and groundwater levels",
    description: "Explore the High Plains aquifer under western Kansas with Kansas Geological Survey saturated thickness, depth to water and monitoring wells.",
    kicker: "WATER · GROUNDWATER",
    intro: [
      "Much of western and central Kansas sits over the High Plains aquifer, the sand and gravel layers that include the Ogallala formation. Irrigated farms and many towns depend on its water, and in parts of southwest Kansas the water table has fallen sharply since irrigation expanded in the mid-twentieth century.",
      "Each winter the Kansas Geological Survey and the state Division of Water Resources measure water levels in about 1,400 wells. This map shows the aquifer's mapped extent, the Survey's classified saturated thickness and depth to water for 2022–2024, and the measured well locations.",
    ],
    layers: ["kgs-aquifer-high-plains", "kgs-saturated-thickness", "kgs-depth-to-water", "kgs-monitoring-wells"],
    center: [-100.2, 38.3], zoom: 6.6,
    ideas: [
      "Find where the saturated sediments are thickest and where they thin toward the aquifer's edges.",
      "Find where groundwater sits more than 150 feet below the surface.",
      "Click a monitoring location to see which well the regional estimate draws on.",
    ],
    caution: "Thickness and depth classes are regional estimates from measured wells, not parcel measurements, current water levels or advice for drilling or pumping. Contact the Kansas Geological Survey or a licensed driller for a local answer.",
  },
  {
    slug: "earthquakes-in-kansas",
    title: "Earthquakes in Kansas",
    description: "Map recent U.S. Geological Survey earthquake reports in and around Kansas beside community Raspberry Shake seismometers and shaded terrain.",
    kicker: "EARTH · EARTHQUAKES",
    intro: [
      "Kansas is not earthquake-free. The largest known Kansas earthquake shook the Manhattan area in 1867. From about 2013, small earthquakes became far more frequent in south-central Kansas, especially Harper and Sumner counties, and state scientists and regulators linked the increase to deep disposal of oil-field wastewater.",
      "This map shows the earthquakes the U.S. Geological Survey has reported recently, the community seismometers volunteers run on the Raspberry Shake network, and shaded terrain for orientation. Click an earthquake for its magnitude, depth and time.",
    ],
    layers: ["usgs-earthquakes", "raspberry-shake-stations", "usgs-3dep-hillshade"],
    center: [-97.9, 37.6], zoom: 6.8,
    ideas: [
      "Look along the Oklahoma border in Harper and Sumner counties, where most recent Kansas earthquakes have occurred.",
      "Compare an earthquake's reported depth with the others nearby.",
      "Find the community seismometer closest to your town.",
    ],
    caution: "The U.S. Geological Survey revises locations and magnitudes as it reviews each event. A station marker is not a reading, and shaded terrain does not show faults or explain why an earthquake happened.",
  },
  {
    slug: "land-cover-and-public-lands",
    title: "Kansas land cover, prairie and public lands",
    description: "See Kansas cropland, grassland, forest and towns from 2021 national land cover with public and protected lands and watershed boundaries.",
    kicker: "ECOLOGY · LAND COVER",
    intro: [
      "Most of Kansas is cropland and grassland. The Flint Hills of eastern Kansas hold the largest remaining tallgrass prairie in North America, while wheat, corn, sorghum and soybeans cover much of the rest of the state.",
      "This map draws the 2021 National Land Cover Database, which sorts every 30-metre cell into a class such as cropland, pasture, grassland, forest, water or developed land. Public and protected lands and watershed boundaries are shown for context.",
    ],
    layers: ["mrlc-nlcd-land-cover", "usgs-padus-lands", "usgs-wbd-watersheds"],
    center: [-97.5, 38.4], zoom: 6.6,
    ideas: [
      "Trace the band of grassland through the Flint Hills between Manhattan and the Oklahoma border.",
      "Compare forest along eastern river valleys with the open cropland of western Kansas.",
      "Find federal reservoirs, state parks and wildlife areas among the public and protected lands.",
    ],
    caution: "Land-cover classes are mapped from satellite imagery and contain errors; they are not species records or a description of current farming. Public and protected land outlines do not grant access, hunting permission or title.",
  },
  {
    slug: "rivers-and-floods",
    title: "Kansas rivers, flood forecasts and rainfall",
    description: "Follow Kansas rivers with National Weather Service forecast gauges, 18-hour modeled river flow, radar rainfall and the mapped stream network.",
    kicker: "WATER · RIVERS",
    intro: [
      "Kansas rivers can rise fast after heavy rain. The July 1951 flood on the Kansas, Neosho and Marais des Cygnes rivers was one of the most damaging in the state's history and hastened federal reservoirs, such as Tuttle Creek, that now help regulate eastern Kansas rivers.",
      "This map shows National Weather Service river gauges with their forecasts, the National Water Model's 18-hour streamflow outlook, radar-estimated rainfall for the past day and the national high-resolution stream network.",
    ],
    layers: ["noaa-nwps-gauges", "noaa-nwm-short-range", "noaa-mrms-qpe-24h", "usgs-3dhp-hydrography"],
    center: [-96.6, 38.7], zoom: 7.2,
    ideas: [
      "Click a forecast gauge to read its latest stage, forecast and flood category.",
      "After a storm, see whether the heaviest radar rainfall fell upstream of a river town.",
      "Zoom in on a creek to follow it downstream into a larger river.",
    ],
    caution: "Gauge forecasts, model guidance and radar rainfall are separate products, each on its own clock. This map is not a flood warning; follow National Weather Service warnings and local emergency officials.",
  },
  {
    slug: "roads-and-railroads",
    title: "Kansas roads and railroads through time",
    description: "Compare the 1918 Kansas road map and abandoned railroad lines with today's state highways and active railroads.",
    kicker: "HISTORY · ROUTES",
    intro: [
      "Railroads made modern Kansas. Towns grew where the lines ran, and the state's rail network was at its largest in the early twentieth century before many branch lines were abandoned as roads and trucks took over.",
      "This map sets a 1918 state road map and the Kansas Department of Transportation's record of abandoned railroads beside today's active rail lines and highway network.",
    ],
    layers: ["kdot-roads-1918", "kdot-rail-abandoned", "kdot-rail-active", "kdot-roads"],
    center: [-97.6, 38.6], zoom: 7.2,
    ideas: [
      "Find a small town that lost its railroad and see which highway serves it now.",
      "Compare a 1918 road with the modern highway that follows the same corridor.",
      "Look for abandoned branch lines that once ran between neighbouring county seats.",
    ],
    caution: "The 1918 map and the rail records differ in date, scale and accuracy. An abandoned line is not a public trail, and a mapped road is not a report of current conditions.",
  },
  {
    slug: "land-survey-and-soils",
    title: "Kansas survey townships, sections and soils",
    description: "See the Public Land Survey townships and sections that divide Kansas into square miles, with NRCS soil survey map units and counties.",
    kicker: "LAND · SURVEY",
    intro: [
      "Federal surveyors divided Kansas into a grid from the 1850s, measuring from the Sixth Principal Meridian and the baseline at the Kansas–Nebraska border. Each township is six miles square and holds 36 sections of about one square mile, or 640 acres. Those lines still shape county roads and field edges.",
      "This map shows Bureau of Land Management townships and sections with the Natural Resources Conservation Service soil survey map units and county boundaries. Sections appear as you zoom in, and soil map units appear closer still.",
    ],
    layers: ["blm-plss-townships", "blm-plss-sections", "nrcs-ssurgo-soils", "census-counties"],
    center: [-97.4, 38.9], zoom: 8.5,
    ideas: [
      "Zoom in until section lines appear and compare them with the roads on the base map.",
      "Keep zooming to see soil map-unit boundaries follow creeks and slopes rather than survey lines.",
      "Find where townships shift at a correction line, where the survey grid was reset.",
    ],
    caution: "Survey divisions and soil map units are references. They are not parcel boundaries, deeds, proof of ownership or a soil test for a field.",
  },
] satisfies LandingGuide[]);

export const landingGuide = (slug: string) => LANDING_GUIDES.find(guide => guide.slug === slug);

/** Explorer deep link with the guide's layers on and the view framed on Kansas. */
export const guideMapHref = (guide: LandingGuide) =>
  `/?ctx=${guide.layers.join(",")}&c=${guide.center[0]},${guide.center[1]}&z=${guide.zoom}`;
