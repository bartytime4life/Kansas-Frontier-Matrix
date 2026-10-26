// Verified tours rendered with actual Explorer layers. Source clocks and playback durations
// come from the preserved capture evidence in scripts/welcome-demos/runtime-assets.json.
export const MAP_DEMOS = {
  "weather": [
    {
      "id": "weather-1",
      "category": "weather",
      "title": "A map of lightning over the years",
      "caption": "Explore the broad 0.5° historical lightning flash-rate field.",
      "sourceTime": "NASA LIS/OTD · 1995–2014",
      "limitation": "Coarse 0.5° multi-year climatology. Broad regional patterns, not fine local variation, a current storm or a live lightning warning.",
      "destination": {
        "kind": "topic",
        "value": "weather"
      },
      "src": "/welcome/demos/weather-1.webm",
      "poster": "/welcome/demos/weather-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "weather-2",
      "category": "weather",
      "title": "Follow the forecast wind",
      "caption": "Inspect model-driven wind direction across Kansas.",
      "sourceTime": "Open-Meteo NCEP GFS · 10 m forecast · valid 2026-10-20T22:00:00.000Z · Retrieved 2026-10-20T22:16:42.593Z",
      "limitation": "10 m forecast model on a bounded 16-sample grid; trail motion is illustrative, not measured wind parcels.",
      "destination": {
        "kind": "topic",
        "value": "weather"
      },
      "src": "/welcome/demos/weather-2.webm",
      "poster": "/welcome/demos/weather-2.jpg",
      "durationSeconds": 7
    }
  ],
  "rivers": [
    {
      "id": "rivers-1",
      "category": "rivers",
      "title": "Trace the Kansas River valley",
      "caption": "Follow USGS mapped waterways through northeastern Kansas.",
      "sourceTime": "USGS 3D Hydrography Program · provider reference mosaic",
      "limitation": "Mapped channels and waterbodies; not present discharge, inundation or measured water speed.",
      "destination": {
        "kind": "topic",
        "value": "water"
      },
      "src": "/welcome/demos/rivers-1.webm",
      "poster": "/welcome/demos/rivers-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "rivers-2",
      "category": "rivers",
      "title": "Explore Tuttle Creek in 3D",
      "caption": "Orbit mapped waterbodies and tributaries above the surrounding terrain.",
      "sourceTime": "USGS 3D Hydrography Program · Mapzen mixed-source display DEM",
      "limitation": "Mixed-date imagery, DEM and mapped waterbodies. 1.0× terrain display; not current water level, discharge, flood extent or lake-bed depth.",
      "destination": {
        "kind": "topic",
        "value": "water"
      },
      "src": "/welcome/demos/rivers-2.webm",
      "poster": "/welcome/demos/rivers-2.jpg",
      "durationSeconds": 7
    }
  ],
  "science": [
    {
      "id": "science-1",
      "category": "science",
      "title": "Read the Flint Hills in 3D",
      "caption": "Orbit actual elevation relief above the tallgrass landscape.",
      "sourceTime": "Mapzen Terrarium · mixed-source display DEM",
      "limitation": "Source-dependent elevation mosaic. 1.0× vertical display; not a survey or a dated landform change.",
      "destination": {
        "kind": "topic",
        "value": "terrain"
      },
      "src": "/welcome/demos/science-1.webm",
      "poster": "/welcome/demos/science-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "science-2",
      "category": "science",
      "title": "See the slopes beneath the landscape",
      "caption": "Compare the actual USGS slope display with terrain context.",
      "sourceTime": "USGS 3DEP · mixed-resolution and mixed-date source mosaic",
      "limitation": "Provider slope visualization; exact work-unit dates, datum and certified accuracy are not identified by this map.",
      "destination": {
        "kind": "topic",
        "value": "terrain"
      },
      "src": "/welcome/demos/science-2.webm",
      "poster": "/welcome/demos/science-2.jpg",
      "durationSeconds": 7
    }
  ],
  "underground": [
    {
      "id": "underground-1",
      "category": "underground",
      "title": "Look below the western plains",
      "caption": "Map regional depth-to-water classes alongside monitoring locations.",
      "sourceTime": "KGS · 2022–2024 estimates; 2026 monitoring locations · retrieved 2026-10-04",
      "limitation": "Regional classified estimates, not present conditions or parcel measurements. Monitoring locations do not include water-level readings.",
      "destination": {
        "kind": "action",
        "value": "underground"
      },
      "src": "/welcome/demos/underground-1.webm",
      "poster": "/welcome/demos/underground-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "underground-2",
      "category": "underground",
      "title": "Explore the aquifer in layers",
      "caption": "Reveal classified saturated thickness in the High Plains aquifer.",
      "sourceTime": "KGS High Plains Atlas · 2022–2024 · retrieved 2026-10-04",
      "limitation": "Regional classified estimates, not present conditions or parcel measurements. Monitoring locations do not include water-level readings.",
      "destination": {
        "kind": "topic",
        "value": "groundwater"
      },
      "src": "/welcome/demos/underground-2.webm",
      "poster": "/welcome/demos/underground-2.jpg",
      "durationSeconds": 7
    }
  ],
  "history": [
    {
      "id": "history-1",
      "category": "history",
      "title": "Trace Kansas roads from 1918",
      "caption": "Brick-red lines trace routes digitized from 1918 maps over modern imagery.",
      "sourceTime": "KDOT · digitized 1918 named routes · modern imagery background",
      "limitation": "Modern imagery is not the 1918 landscape. Approximate route digitization; not exact alignment, ownership or today’s road conditions.",
      "destination": {
        "kind": "topic",
        "value": "history"
      },
      "src": "/welcome/demos/history-1.webm",
      "poster": "/welcome/demos/history-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "history-2",
      "category": "history",
      "title": "Follow traces of the railway",
      "caption": "Inspect KDOT’s references to abandoned railway corridors.",
      "sourceTime": "KDOT · provider-current reference to former routes; dates vary",
      "limitation": "Current abandoned designation is not a reconstruction at a selected past year, proof of track removal or public access.",
      "destination": {
        "kind": "topic",
        "value": "history"
      },
      "src": "/welcome/demos/history-2.webm",
      "poster": "/welcome/demos/history-2.jpg",
      "durationSeconds": 7
    }
  ],
  "transport": [
    {
      "id": "transport-1",
      "category": "transport",
      "title": "Discover the connected landscape",
      "caption": "Explore KDOT roads and active railway reference lines.",
      "sourceTime": "KDOT · provider-current reference; feature dates vary",
      "limitation": "Provider reference geography; not live traffic, train positions, access or safety.",
      "destination": {
        "kind": "topic",
        "value": "transport"
      },
      "src": "/welcome/demos/transport-1.webm",
      "poster": "/welcome/demos/transport-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "transport-2",
      "category": "transport",
      "title": "Find the bridges along the river",
      "caption": "Inspect state-highway bridge inventory locations near Topeka.",
      "sourceTime": "KDOT · provider-current inventory; inspection dates vary",
      "limitation": "Inventory points, not deck footprints, live closures or structural-safety findings.",
      "destination": {
        "kind": "topic",
        "value": "transport"
      },
      "src": "/welcome/demos/transport-2.webm",
      "poster": "/welcome/demos/transport-2.jpg",
      "durationSeconds": 7
    }
  ],
  "farming": [
    {
      "id": "farming-1",
      "category": "farming",
      "title": "See the patterns of Kansas fields",
      "caption": "Fly above actual fields in high-resolution Kansas aerial imagery.",
      "sourceTime": "Kansas NG911 · February–April 2024 aerial campaign",
      "limitation": "Approximately 1-foot source imagery; local flight date unresolved. Not live crops, crop identification or a yield estimate.",
      "destination": {
        "kind": "topic",
        "value": "agriculture"
      },
      "src": "/welcome/demos/farming-1.webm",
      "poster": "/welcome/demos/farming-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "farming-2",
      "category": "farming",
      "title": "Connect fields with water context",
      "caption": "Explore KGS water-table classes and monitoring locations.",
      "sourceTime": "KGS · 2022–2024 estimates; 2026 monitoring locations · retrieved 2026-10-04",
      "limitation": "Regional classified estimates, not present conditions or parcel measurements. Monitoring locations do not include water-level readings. Not irrigation advice or well yield.",
      "destination": {
        "kind": "topic",
        "value": "agriculture"
      },
      "src": "/welcome/demos/farming-2.webm",
      "poster": "/welcome/demos/farming-2.jpg",
      "durationSeconds": 7
    }
  ],
  "government": [
    {
      "id": "government-1",
      "category": "government",
      "title": "Put counties in context",
      "caption": "Explore Kansas county boundaries and the Census baseline.",
      "sourceTime": "U.S. Census Bureau · 2020 decennial baseline · U.S. Census Bureau · retrieved 2026-10-20T22:29:21.962Z",
      "limitation": "2020 county geography and counts; not current population, parcels or a historical reconstruction.",
      "destination": {
        "kind": "topic",
        "value": "places"
      },
      "src": "/welcome/demos/government-1.webm",
      "poster": "/welcome/demos/government-1.jpg",
      "durationSeconds": 7
    },
    {
      "id": "government-2",
      "category": "government",
      "title": "Zoom into the survey grid",
      "caption": "See BLM township and section reference geography near Salina.",
      "sourceTime": "BLM CadNSDI · provider-current reference; edition varies",
      "limitation": "Survey reference context does not establish ownership, mineral rights, access or exact parcel boundaries.",
      "destination": {
        "kind": "topic",
        "value": "land"
      },
      "src": "/welcome/demos/government-2.webm",
      "poster": "/welcome/demos/government-2.jpg",
      "durationSeconds": 7
    }
  ]
};
export function mapDemos(category) { return MAP_DEMOS[category] || []; }
export function demoDuration(seconds) {
  if (!Number.isFinite(seconds) || seconds <= 0) return 'Short demo';
  const rounded = Math.round(seconds);
  return `${Math.floor(rounded / 60)}:${String(rounded % 60).padStart(2, '0')}`;
}
