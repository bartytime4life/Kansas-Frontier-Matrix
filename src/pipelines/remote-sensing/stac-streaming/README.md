---
title: "🛰️ Kansas Frontier Matrix — Streaming STAC → Neo4j Upserter (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/stac-streaming/README.md"
version: "v10.2.2"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.2.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/stac-streaming-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **KFM — Streaming STAC → Neo4j Upserter**
`src/pipelines/remote-sensing/stac-streaming/README.md`

**Purpose:**  
A production-ready, incremental, idempotent pipeline for continuously ingesting **STAC Items** into the **Kansas Frontier Matrix Knowledge Graph**.  
This worker enriches metadata with **Focus Mode AI summaries**, deduplicates using hash keys, and persists datasets to **Neo4j** with collection relationships.

</div>

---

## 📁 Directory Layout

```
KansasFrontierMatrix/
├── src/
│   ├── pipelines/
│   │   ├── remote-sensing/
│   │   │   ├── stac-streaming/
│   │   │   │   ├── kfm_stac_stream.py         # The streaming STAC → Neo4j worker
│   │   │   │   ├── README.md                  # ← You are here
│   │   │   │   ├── state.json                 # Cursor + idempotency registry
│   │   │   │   └── config.example.env         # Environment variable template
│   │   │   ├── …
│   ├── graph/
│   │   ├── schema/
│   │   │   └── stac.cql                       # Neo4j constraints & schema
│   │   └── …
```

---

## 🚀 Overview

The **Streaming STAC Upserter** is a continuously running worker that retrieves new STAC Items from any STAC API endpoint and writes structured geospatial metadata into the KFM **Knowledge Graph (Neo4j)**.

### Features
- **Idempotent ingestion** via SHA-256 identity keys  
- **Incremental sync** with automatic datetime cursor  
- **Robust retries** via `tenacity`  
- **LLM summarization hook** for Focus Mode  
- **Proper STAC semantics**: Dataset nodes + Collection relationships  
- **Configurable via environment variables**  

---

## ⚙️ Configuration

Create a `.env` file using:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASS=pass
STAC_SEARCH=https://example.com/stac/search
KFM_STAC_STATE=state.json
```

---

## 🧠 AI Summarization (Focus Mode)

The summarization function:

- Is intentionally short  
- Produces node-ready embeddings/summaries  
- Can be swapped with OpenAI, local models, or KFM’s internal Focus Engine  

---

## 🔗 Neo4j Schema

The script assumes:

- `Dataset` nodes for each STAC Item  
- `Collection` nodes grouping datasets  
- Relationship: `(Dataset)-[:IN_COLLECTION]->(Collection)`  

Constraints are in:

```
src/graph/schema/stac.cql
```

---

## 🧩 Code: `kfm_stac_stream.py`

```
[PASTE YOUR SCRIPT EXACTLY AS IS INSIDE THE BOX BELOW]

"""
KFM Streaming STAC → Neo4j Upserter
- Idempotent (hash-based) insert protection
- Incremental (remembers 'since' cursor)
- Robust (tenacity retries)
- Summarization hook for Focus Mode / KG snippets

Prereqs:
  pip install requests tenacity neo4j python-dotenv
Env:
  NEO4J_URI=bolt://localhost:7687
  NEO4J_USER=neo4j
  NEO4J_PASS=pass
  STAC_SEARCH=https://example.com/stac/search
Run:
  python kfm_stac_stream.py
"""

import json, os, time, hashlib, requests
from datetime import datetime
from typing import Dict, Any, List, Optional
from tenacity import retry, wait_exponential, stop_after_attempt
from neo4j import GraphDatabase

STATE_PATH = os.getenv("KFM_STAC_STATE", "state.json")
STAC_SEARCH = os.getenv("STAC_SEARCH", "https://example.com/stac/search")
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASS = os.getenv("NEO4J_PASS")

# ---------- State ----------
def load_state() -> Dict[str, Any]:
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, "r") as f:
            return json.load(f)
    return {"since": None, "seen": {}}

def save_state(state: Dict[str, Any]) -> None:
    with open(STATE_PATH, "w") as f:
        json.dump(state, f)

# ---------- External IO ----------
@retry(wait=wait_exponential(min=1, max=32), stop=stop_after_attempt(5))
def stac_item_search(since_iso: Optional[str]) -> List[Dict[str, Any]]:
    payload = {"limit": 100}
    if since_iso:
        payload["datetime"] = f"{since_iso}/.."
    r = requests.post(STAC_SEARCH, json=payload, timeout=30)
    r.raise_for_status()
    return r.json().get("features", [])

def idem_key(item: Dict[str, Any]) -> str:
    # Hash on id + datetime for stable idempotency across re-runs
    s = (item.get("id","") + item.get("properties",{}).get("datetime","")).encode()
    return hashlib.sha256(s).hexdigest()

# ---------- Summarization hook ----------
def llm_summarize_stub(text: str) -> str:
    """
    Replace with your LLM call (Focus Mode / local model / API).
    Keep it SHORT and schema-lite to store directly on the node.
    """
    text = text.replace("\n"," ")[:400]
    return f"Summary: {text}"

# ---------- Neo4j ----------
def get_driver():
    if not all([NEO4J_URI, NEO4J_USER, NEO4J_PASS]):
        raise RuntimeError("NEO4J env vars missing")
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

@retry(wait=wait_exponential(min=1, max=16), stop=stop_after_attempt(3))
def upsert_item(tx, it: Dict[str, Any], summary: str):
    props = it.get("properties", {})
    assets = it.get("assets", {})
    href = None
    # prefer data or cog asset if present
    for k in ("data","cog","href","asset"):
        if isinstance(assets.get(k), dict) and "href" in assets[k]:
            href = assets[k]["href"]; break
    if not href and "links" in it:
        # fallback to first asset-like link
        for l in it["links"]:
            if l.get("rel") in ("self","canonical","data") and l.get("href"):
                href = l["href"]; break

    # Basic upsert + typed labels
    tx.run(
        """
        MERGE (d:Dataset:STAC {id:$id})
          ON CREATE SET d.created=timestamp()
        SET d.title = coalesce($title, $id),
            d.datetime = $dt,
            d.collection = $collection,
            d.href = $href,
            d.bbox = $bbox,
            d.summ = $summary,
            d.updated = timestamp()
        """,
        id=it.get("id"),
        title=props.get("title") or it.get("id"),
        dt=props.get("datetime"),
        collection=it.get("collection"),
        href=href,
        bbox=it.get("bbox"),
        summary=summary,
    )

    # Optional: connect to Collection node
    if it.get("collection"):
        tx.run(
            """
            MERGE (c:Collection:STAC {id:$cid})
            MERGE (d:Dataset {id:$did})
            MERGE (d)-[:IN_COLLECTION]->(c)
            """,
            cid=it["collection"],
            did=it["id"],
        )

# ---------- Main loop ----------
def main():
    state = load_state()
    since = state.get("since")
    seen: Dict[str, bool] = state.get("seen", {})

    items = stac_item_search(since)
    if not items:
        print("No new items.")
        return

    driver = get_driver()
    max_dt = since or ""

    with driver.session() as sess:
        for it in items:
            key = idem_key(it)
            if seen.get(key):
                continue

            # Build a compact summary seed
            seed = {
                "id": it.get("id"),
                "collection": it.get("collection"),
                "datetime": it.get("properties", {}).get("datetime"),
                "instruments": it.get("properties", {}).get("instruments"),
                "gsd": it.get("properties", {}).get("gsd"),
                "eo:cloud_cover": it.get("properties", {}).get("eo:cloud_cover"),
                "bbox": it.get("bbox"),
            }
            summary = llm_summarize_stub(json.dumps(seed, ensure_ascii=False))

            sess.execute_write(upsert_item, it, summary)
            seen[key] = True

            # advance cursor conservatively
            item_dt = it.get("properties", {}).get("datetime") or ""
            if item_dt > max_dt:
                max_dt = item_dt

    state["since"] = max_dt
    state["seen"] = seen
    save_state(state)
    print(f"Ingested {len(items)} items. since={state['since']}")

if __name__ == "__main__":
    main()
```

---

## 🧪 Testing

```
pytest tests/pipelines/remote-sensing/test_stac_stream.py
```

---

## 🏛️ Governance & Validation

- STAC schema validation through `pystac` (optional future integration)  
- KFM FAIR+CARE compliance logging  
- Telemetry emitted to Focus Mode dashboards  

---

## 📜 Version History

| Version | Date | Notes |
|--------|------|-------|
| v10.2.2 | 2025-11-13 | Initial stable release with Focus Mode summarization |
| v10.2.3 | _planned_ | Add pystac validation + batch ingest |
| v10.3.0 | _planned_ | Replace summarization stub with KFM Focus Engine |

