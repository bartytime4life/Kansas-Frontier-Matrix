<div align="center">

# 📑 Kansas-Frontier-Matrix — OCR Workspace (`data/work/ocr/`)

**Mission:** Provide a staging area for **raw OCR text outputs**  
from scanned maps, treaties, newspapers, and documents.  

This folder captures **machine-extracted text** before cleanup,  
normalization, and promotion into canonical directories.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)

📌 Subdirectory of `data/work/` (scratch + staging).  
📌 Files here are **ephemeral by default**.  
📌 Promote cleaned text to `data/processed/` or `data/sources/`.  

</div>

---

## 🎯 Purpose

- Hold **raw OCR text dumps** (pre-cleaning).  
- Stage **trial OCR runs** before normalization.  
- Support **NLP/ETL pipelines** (entity extraction, geocoding).  
- Prevent clutter in canonical `data/processed/` directories.  

---

## 📂 Typical Contents

- `.txt` files from Tesseract or other OCR engines.  
- JSON outputs with OCR bounding boxes.  
- Sidecar logs from OCR runs (confidence, language models).  
- Trial OCR exports from historical scans (treaties, plats, maps).  

---

## 🚦 Rules

- 🚫 **Not canonical** — raw OCR here should not be cited or published.  
- ✅ **Promote if valuable:**  
  - → `data/processed/` for cleaned, normalized text.  
  - → `data/sources/` for curated historical transcription datasets.  
  - Always update **provenance + STAC Item** when promoting.  
- 🧹 **Safe to delete anytime** — regenerate with OCR pipelines.  

---

## 🔄 Lifecycle Position

```mermaid
flowchart LR
  A["OCR raw text\n(data/work/ocr)"] --> B["Processed text\n(data/processed/)"]
  B --> C["Knowledge extraction\n(NLP / entities)"]
  C --> D["Catalog\n(stac/items)"]
  D --> E["Web Viewer\n(web/)"]

<!-- END OF MERMAID -->



⸻

🛠️ Usage Examples

OCR from treaty scan

# Extract raw text from a treaty PDF
tesseract data/raw/docs/treaty_osage_1825.pdf \
  data/work/ocr/treaty_osage_1825 -l eng

Batch OCR run

# Run OCR on all scanned TIFFs in a folder
for f in data/raw/scans/*.tif; do
  out="data/work/ocr/$(basename "$f" .tif).txt"
  tesseract "$f" "$out" -l eng
done


⸻

🧹 Cleanup Policy
	•	Clear OCR workspace with:

clean-ocr:
	rm -rf data/work/ocr/*

	•	Promote cleaned outputs before cleanup.
	•	CI/CD pipelines may automatically purge this folder.

⸻

✅ Summary:
data/work/ocr/ = raw OCR staging area.
Use it for machine-extracted text dumps;
promote only after cleaning + documentation.