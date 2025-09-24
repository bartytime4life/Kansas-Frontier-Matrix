# Kansas-Frontier-Matrix — Treaty & Land Transfer Sources

This directory stores **treaty boundaries, land cessions, and reservation maps**  
relevant to Kansas history. These layers connect **documents** (treaty texts, oral
histories, legal records) with **geospatial features** (boundary polygons, dates, 
and attributes).

---

## Purpose

- Document the **changing geography** of Native American lands in Kansas.
- Provide **vector layers** (GeoJSON, Shapefiles) that can be overlaid in the map UI.
- Link treaties to their **source documents** (scans, transcriptions, legal texts).
- Support **timeline queries** (treaty year, reservation boundaries by date).
- Maintain **provenance** with checksums and license details.

---

## Directory Layout

```

data/sources/treaties/
├── treaties\_1854\_kansas.json      # Example: Kansas–Nebraska Act treaty boundaries
├── treaties\_1867\_medicine\_lodge.json
├── tribal\_cessions\_index.json     # Master index of all treaties and cessions
├── scans/                         # Scanned originals (PDF, TIFF, JPG)
├── vectors/                       # GeoJSON / Shapefile boundary layers
└── README.md                      # This file

````

---

## Metadata Requirements

Each treaty dataset (`.json` or `.yml`) should follow the **STAC-like schema**:

```json
{
  "id": "treaty_kansas_nebraska_1854",
  "title": "Kansas–Nebraska Act Treaty Boundaries (1854)",
  "type": "vector",
  "description": "Polygons representing tribal lands and cessions as defined by the 1854 Kansas–Nebraska Act.",
  "temporal": {
    "start": "1854-05-30",
    "end": "1867-10-21"
  },
  "spatial": {
    "bbox": [-102.05, 36.99, -94.61, 40.00]
  },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://www.archives.gov/…/treaties/1854_kansas.pdf"
      ]
    }
  ],
  "lineage": [
    "Scanned from NARA microfilm",
    "Digitized boundary via QGIS",
    "Saved as GeoJSON"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "abc123…"
  }
}
````

---

## Recommended Sources

* **National Archives (NARA)** — treaty texts, scanned microfilm.
* **Kansas Historical Society** — maps, manuscripts, tribal records.
* **Library of Congress** — 19th-century treaty maps.
* **Bureau of Indian Affairs (BIA)** — reservation boundary records.
* **Tribal archives** — oral histories and community-provided boundary definitions.

---

## Integration Notes

* Treaties should be **time-enabled**: each polygon tagged with start/end dates.
* Link to **knowledge graph** via:

  * `Document` node → treaty text.
  * `Event` node → treaty signing.
  * `Place` node → boundary polygon.
  * `Organization` node → tribes, U.S. government.
* Support **story map layers** (e.g., timeline of land transfers, narrative tours).

---

## Best Practices

* Always keep **raw scans** (`scans/`) separate from **digitized vectors** (`vectors/`).
* Record **confidence scores** if boundaries are approximate.
* Reference **tribal historians** and oral accounts, not just federal records.
* Document every edit in `data/provenance/`.

---

## References

* [STAC 1.0.0 Specification](https://stacspec.org/)
* [Kansas Frontier Matrix — Design Audit: Tribal Land Transfers & Treaties]: contentReference[oaicite:1]{index=1}
* [Historical Dataset Integration Report]: contentReference[oaicite:2]{index=2}
* [Kansas Historical Knowledge Hub — System Design]: contentReference[oaicite:3]{index=3}

---

