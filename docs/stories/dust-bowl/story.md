# Dust Bowl in Kansas 🌪️🌾  
**When drought met broken sod — and the wind did the rest.**

![status](https://img.shields.io/badge/status-draft-yellow)
![story](https://img.shields.io/badge/KFM-story-blue)
![license](https://img.shields.io/badge/license-CC--BY--4.0-green)

</div>

---

## 🎯 What this story does

This Story Node is designed for a **scroll-driven “map + timeline” experience** inside Kansas Frontier Matrix (KFM). Each section is written to pair with a `story.json` that can:

- 🗺️ fly the camera to relevant places in Kansas  
- 🧭 toggle data layers (drought, land use, wind erosion risk, county outlines, etc.)  
- 🧷 drop annotations on towns, farms, photo points, and agency projects  
- 🕰️ snap the timeline to key years and storms  

**Theme:** The Dust Bowl wasn’t “just weather.” It was a collision of climate variability, economics, land-use choices, and policy responses — and **Kansas sits right inside the core geography of that collision**.[^ndmc-overview]

---

## 🧩 Scene index

Use these scene keys (or headings) in `story.json` so choreography stays stable even if paragraph text changes.

| Scene Key | Section Title | Time |
|---|---|---|
| `grassland` | Before the Dust: Wind, Grass, and a Semi‑Arid Plains | ~pre‑1900 → 1920s |
| `broken-sod` | Wheat Boom & Broken Sod | 1900–1929 |
| `drought-1930` | Drought Begins | 1930–1931 |
| `heat-1934` | 1934: Heat, Wind, and Exposure | 1934 |
| `dust-across-kansas-1935` | 1935: Dust Crosses Kansas | Spring 1935 |
| `black-sunday` | Black Sunday (April 14, 1935) | 1935‑04‑14 |
| `drifts-liberal-1936` | 1936: Drifts at Liberal | 1936 |
| `fighting-back` | Fighting Back: Conservation & Relief | 1933–1940 |
| `recovery-legacy` | Recovery & Legacy | 1941 → |

---

## 🌾 Before the Dust: Wind, Grass, and a Semi‑Arid Plains

Long before the 1930s, the Great Plains were **built for wind** — and stabilized by deep-rooted prairie grasses. Where the land stayed covered, the soil stayed put.

But settlement patterns and agricultural expansion rewired the system. By the early 20th century, dryland farming and grazing intensified across Kansas and the Southern Plains. The Library of Congress notes how settlers plowed prairie grasses and planted wheat, expanding cultivation as demand grew — a change that left more ground exposed when drought hit.[^loc-dustbowl]

> 🗺️ **Map cue (KFM idea):**  
> Start with *landcover / prairie-to-cropland change* + county outlines. Let users feel the scale of conversion before the drought timeline even begins.

---

## 🚜 Wheat Boom & Broken Sod (1900–1929)

In the 1920s, much of the Plains experienced conditions that made expansion look safe — and profitable. More acres went under the plow, and conservation practices often lost the tug-of-war against debt, markets, and momentum.[^ndmc-overview]

The result wasn’t immediate catastrophe. It was **risk stored in the landscape**:
- fewer perennial roots holding soil  
- more finely-tilled ground that could dry out fast  
- wider areas of bare surface that wind could lift  

> 🌬️ On the Plains, “wind” isn’t an event — it’s a constant.  
> The question is whether the land is armored when it arrives.

---

## ☀️ Drought Begins (1930–1931)

The Dust Bowl era is often remembered as one long drought, but the National Drought Mitigation Center describes **multiple distinct drought episodes** during the 1930s (including 1930–31, 1934, 1936, and 1939–40).[^ndmc-drought-events]

Kansas was not spared — especially the western and southwestern parts of the state that sit inside the region most associated with the Dust Bowl.[^ndmc-overview]

> 🧭 **KFM interaction idea:**  
> Put the user on a timeline scrubber that shows precipitation anomaly by year, and make the “bare soil / cropland exposure” layer fade in and out with seasonality.

---

## 🔥 1934: Heat, Wind, and Exposure

By 1934 the Plains were deep in trouble. Hot temperatures, deficient rainfall, and high winds amplified each other — and dust storms became part of the rhythm of life.[^ndmc-overview]

This is where the story becomes spatial:
- Which counties were most exposed?  
- Which soils were most erodible?  
- Where did drought severity align with cropland expansion?  
- Which towns became “dust nodes” in the public memory?

> 🗺️ **Map cue (KFM idea):**  
> Split-screen layer compare:  
> **(A) Drought severity** vs **(B) cropland / bare soil proxy**, with a linked cursor over southwest Kansas.

---

## 🌫️ 1935: Dust Crosses Kansas

Dust storms did not stay “out west.” In March 1935, dust from the southern plains blew into Lawrence, Kansas, blocking the sun and cutting visibility — a reminder that the Dust Bowl’s reach extended far beyond the core counties.[^ku-lawrence]

> 🧭 **KFM interaction idea:**  
> Turn on a “dust plume” / narrative overlay: show Kansas as connected — not isolated — by wind, rail, newspapers, and policy response.

---

## 🌓 Black Sunday (April 14, 1935)

**April 14, 1935** became one of the defining days of the Dust Bowl. Accounts describe a clear day that turned ominous as a massive wall of dust approached — a storm later remembered as **Black Sunday**.[^pbs-drought][^nws-black-sunday]

The storm is commonly associated with the Oklahoma and Texas panhandles, but Kansas sits inside the geography that the Dust Bowl name came to represent.[^ndmc-overview] The National Weather Service also notes that reporting around Black Sunday helped cement the phrase “Dust Bowl” in print.[^nws-black-sunday]

And Kansas has its own vivid anchors of memory. The National Endowment for the Humanities describes Black Sunday engulfing a church in **Ulysses, Kansas**, an image that captures the fear and disbelief people experienced in real time.[^neh-ulysses]

> 🗺️ **Map cue (KFM idea):**  
> Fly-to Ulysses, KS → roll the timeline to **1935‑04‑14** → show drought severity + wind direction arrows + “dust storm event” markers.

---

## 🏚️ 1936: Drifts at Liberal

By 1936, the Dust Bowl had a physical texture — not just a headline. Library of Congress photographs by Arthur Rothstein show soil blown by Dust Bowl winds piling into **large drifts near Liberal, Kansas (Seward County)**.[^loc-liberal-1936]

This isn’t metaphor. It’s geomorphology at human scale:
- fence lines buried  
- doorways blocked  
- barns banked with soil  
- daily life reshaped by the wind’s new inventory  

> 📸 **Media cue:**  
> Consider adding a photo stop that pins the Rothstein image(s) to the map as clickable points, with full credit + link back to LOC.

---

## 🛠️ Fighting Back: Conservation & Relief (1933–1940)

The Dust Bowl story includes emergency response — but also long-term institutional change. The National Drought Mitigation Center’s timeline highlights how dire conditions pushed the region toward aid and new approaches.[^ndmc-overview]

This is where Kansas becomes a case study in **adaptation under pressure**:
- changing tillage practices  
- stabilizing soil with cover and contouring  
- planting windbreaks / shelterbelts  
- strengthening the idea that land stewardship is infrastructure  

> 🧩 **KFM layer idea:**  
> Add “policy footprint” layers: where conservation districts formed, where shelterbelt projects ran, where relief programs concentrated (as data becomes available).

---

## 🌧️ Recovery & Legacy (1941 →)

The Dust Bowl era did not end because people “got better at enduring dust.” It ended when the drought cycle broke and conditions returned closer to normal — the NDMC places the end around **1941**.[^ndmc-overview]

But the legacy is bigger than the decade:
- conservation became policy, not just advice  
- the Plains became a living reminder that **land-use + climate** is a coupled system  
- later droughts were still severe, but the region carried lessons forward[^ndmc-overview]  

> 🌾 **Core takeaway:**  
> The Dust Bowl is a Kansas story about *systems* — environmental, economic, and political — and KFM is built to let users explore those systems on a map.

---

## 🧠 Try this in KFM (reader prompts)

- 🕰️ Scrub the timeline from **1930 → 1936** and watch drought severity expand/contract.[^ndmc-drought-events]  
- 🗺️ Zoom to **southwest Kansas** and compare:
  - drought severity vs cropland exposure vs wind erosion risk  
- 📸 Click historic photo points near **Liberal, KS** and read captions as primary sources.[^loc-liberal-1936]  
- 🌫️ Jump to **March 1935** and notice dust impacts reach deep into Kansas.[^ku-lawrence]  

---

## 📚 References (human-readable)

> These sources are also good candidates for ingestion into KFM’s catalogs (documents, media, and dataset metadata).

- National Drought Mitigation Center — *The Dust Bowl* (overview, timeline, references).[^ndmc-overview]  
- National Drought Mitigation Center — Distinct drought events in the 1930s.[^ndmc-drought-events]  
- Library of Congress — *The Dust Bowl* (primary source timeline + context).[^loc-dustbowl]  
- National Weather Service — Black Sunday (April 14, 1935) event overview and “Dust Bowl” term origin notes.[^nws-black-sunday]  
- PBS American Experience — “The Drought” (Dust Bowl narrative and Black Sunday context).[^pbs-drought]  
- NEH — “Children of the Dust” (Kansas-specific Black Sunday reference at Ulysses).[^neh-ulysses]  
- Library of Congress — Rothstein photo near Liberal, KS (1936).[^loc-liberal-1936]  
- University of Kansas Memorial Unions — Dust reaches Lawrence, KS (March 20, 1935).[^ku-lawrence]  

---

<details>
<summary>🗂️ For maintainers: suggested folder layout</summary>

```text
📁 docs/
  📁 stories/
    📁 dust-bowl/
      📄 story.md              ✅ (this file)
      📄 story.json            ⏳ (map choreography; recommended next)
      📁 media/                ⏳ (downloaded/curated assets)
        📷 loc_liberal_ks_1936_rothstein.jpg
        📷 (optional) rolla_ks_dust_storm_1935.jpg
        📄 CREDITS.md          (asset-level attribution + licenses)
```

</details>

<details>
<summary>🗺️ For maintainers: suggested <code>story.json</code> skeleton</summary>

> This is intentionally **illustrative**. Replace layer IDs with actual KFM layer keys and dataset references.

```json
[
  {
    "section": "Before the Dust: Wind, Grass, and a Semi‑Arid Plains",
    "mapState": {
      "center": [-100.92, 37.04],
      "zoom": 6,
      "layers": {
        "county_boundaries": { "on": true },
        "landcover_cropland": { "year": 1920, "opacity": 0.7 }
      }
    },
    "timeline": "1920-01-01"
  },
  {
    "section": "Drought Begins (1930–1931)",
    "mapState": {
      "center": [-100.92, 37.04],
      "zoom": 6,
      "layers": {
        "drought_severity": { "year": 1931, "opacity": 0.85 }
      }
    },
    "timeline": "1931-07-01"
  },
  {
    "section": "Black Sunday (April 14, 1935)",
    "mapState": {
      "center": [-101.35, 37.57],
      "zoom": 7,
      "annotations": [
        { "type": "marker", "coordinates": [-101.35, 37.57], "text": "Ulysses, KS (Black Sunday reference)" }
      ],
      "layers": {
        "drought_severity": { "year": 1935, "opacity": 0.9 },
        "wind_direction": { "date": "1935-04-14", "opacity": 0.6 }
      }
    },
    "timeline": "1935-04-14"
  },
  {
    "section": "1936: Drifts at Liberal",
    "mapState": {
      "center": [-100.92, 37.04],
      "zoom": 8,
      "annotations": [
        { "type": "photo", "coordinates": [-100.92, 37.04], "media": "loc_liberal_ks_1936_rothstein.jpg", "caption": "Dust drifts near Liberal, Kansas (1936)" }
      ],
      "layers": {
        "historic_photos_fsa": { "on": true }
      }
    },
    "timeline": "1936-03-01"
  }
]
```

</details>

---

## ✅ Definition of Done (story node)

- [x] YAML front-matter present (title, id, path, time range, license)
- [x] Clear section structure aligned to story scene keys
- [x] External references included and suitable for ingestion
- [ ] `story.json` implemented + validated against UI contract
- [ ] Media assets downloaded to `media/` with `CREDITS.md`
- [ ] All map cues tested in KFM story player (desktop + mobile)
- [ ] Accessibility pass (alt text, heading order, link clarity)

---

[^ndmc-overview]: National Drought Mitigation Center (University of Nebraska–Lincoln), “The Dust Bowl” (overview; includes term origin and the technical geographic definition). https://drought.unl.edu/dustbowl/
[^ndmc-drought-events]: National Drought Mitigation Center, “The Dust Bowl” (notes multiple distinct drought events: 1930–31, 1934, 1936, 1939–40). https://drought.unl.edu/dustbowl/
[^loc-dustbowl]: Library of Congress, “The Dust Bowl” (U.S. history primary source timeline; discusses settlement, plowing prairie grasses, and wheat cultivation). https://www.loc.gov/classroom-materials/united-states-history-primary-source-timeline/great-depression-and-world-war-ii-1929-1945/dust-bowl/
[^nws-black-sunday]: National Weather Service (Norman, OK), “The Black Sunday Dust Storm of April 14, 1935” (event overview; includes notes about early “dust bowl” usage after Black Sunday). https://www.weather.gov/oun/events-19350414
[^pbs-drought]: PBS American Experience, “The Drought” (Dust Bowl feature; narrative context including Black Sunday). https://www.pbs.org/wgbh/americanexperience/features/dustbowl-drought/
[^neh-ulysses]: National Endowment for the Humanities, “Children of the Dust” (mentions Black Sunday engulfing a church in Ulysses, Kansas). https://www.neh.gov/humanities/2012/novemberdecember/feature/children-the-dust
[^loc-liberal-1936]: Library of Congress, Arthur Rothstein (photographer), “Soil blown by ‘dust bowl’ winds piled up in large drifts near Liberal, Kansas” (1936). https://www.loc.gov/item/2017759854/
[^ku-lawrence]: University of Kansas Memorial Unions, “Dust Bowl” (notes dust from the southern plains blowing into Lawrence, Kansas on March 20, 1935). https://union.ku.edu/dust-bowl