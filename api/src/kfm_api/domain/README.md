# 🧠 Domain Layer — `kfm_api.domain`

![Layer](https://img.shields.io/badge/layer-domain-informational)
![Architecture](https://img.shields.io/badge/architecture-clean%20architecture-success)
![Rule](https://img.shields.io/badge/rule-no%20framework%20dependencies-critical)

Welcome to the **Domain** layer of the Kansas Frontier Matrix (KFM) API. This is the **innermost, most stable** part of the system: the place where we define the **real-world concepts** KFM cares about (fields, soils, climate records, sensor readings, users, policies) and the **rules/invariants** that must always be true ✅.

> **Core intent:** model the world 🗺️, not the web framework 🌐, not the database 🗄️, and not the UI 🎛️.

---

## 🎯 What this layer is (and why it exists)

KFM follows a layered “clean architecture” style: inner layers express **business meaning**, outer layers handle **implementation details**. In this structure, the Domain layer:

- Holds **domain entities & value objects** (the “nouns” of KFM)
- Encodes **invariants** and **domain rules** (what must never be violated)
- Defines **interfaces/ports** for external collaboration (storage, external services, messaging)
- Avoids any dependency on frameworks or infrastructure (so it’s easy to test & evolve)

**Mental model:**  
- Inner layers are **oblivious** to outer layers.
- We “talk inwards with simple data” and “talk outwards through interfaces.” 🧩

---

## 🧱 Golden rules (non‑negotiable)

✅ **DO**
- Keep Domain **framework-agnostic** (pure Python)
- Make models **lightweight** (no ORM behaviors, no JSON dumping methods)
- Validate and enforce **invariants** close to the data
- Expose collaboration points via **ports/interfaces**
- Write **fast unit tests** for domain behaviors

🚫 **DON’T**
- Import FastAPI/Flask, Pydantic, SQLAlchemy, GeoPandas, Shapely, requests, boto3, etc.
- Do I/O (DB queries, HTTP calls, file reads/writes, network)
- Serialize/deserialize API DTOs here (that’s an outer layer concern)
- Hide business rules inside repositories/adapters (rule drift 🧟)

---

## 🗂️ Suggested folder layout (illustrative)

> Your exact structure may differ — but keep the *roles* consistent.

```text
📦 kfm_api/
  └─ 🧠 domain/
     ├─ 📄 README.md
     ├─ 🧾 __init__.py
     ├─ 🧩 entities/
     │  ├─ 🌾 field.py
     │  ├─ 🧪 soil_sample.py
     │  ├─ 🌦️ climate_record.py
     │  ├─ 📡 sensor_reading.py
     │  └─ 👤 user_profile.py
     ├─ 💠 value_objects/
     │  ├─ 🗺️ geo.py
     │  ├─ ⏱️ time_range.py
     │  ├─ 📏 units.py
     │  └─ 📈 indices.py
     ├─ 🔌 ports/              # aka interfaces (repository/service contracts)
     │  ├─ 🗄️ soil_data_repo.py
     │  ├─ 🛰️ imagery_repo.py
     │  └─ 📣 notification_port.py
     ├─ 🧠 services/           # domain services (cross-entity logic)
     │  ├─ 💧 irrigation_policy.py
     │  └─ 🌵 drought_risk_policy.py
     ├─ 🧾 events/
     │  └─ 📣 domain_event.py
     ├─ 💥 errors.py
     └─ 🧷 types.py
```

---

## ✅ What belongs here vs. 🚫 what does not

| ✅ Belongs in `domain/` | 🚫 Does **not** belong in `domain/` |
|---|---|
| Entities, value objects, domain services | API routes/controllers |
| Domain invariants & validation | Pydantic request/response schemas |
| Domain events | JSON serialization concerns |
| Ports/interfaces (repo/service contracts) | SQL, ORM models, migrations |
| Domain errors/exceptions | External API clients (GEE, NOAA, etc.) |
| Pure functions for business meaning | Logging/metrics wiring, config/env |

---

## 🧬 Modeling guidelines

### 1) Entities (things with identity)
Entities represent “things” that remain the *same* even if attributes change:
- `Field` (a land plot with a boundary)
- `SoilSample` (collected at a place/time)
- `SensorReading` (time-series reading for a station/field)
- `UserProfile` (identity + preferences/permissions)

**Entity checklist**
- Has a stable `id`
- Owns invariants (e.g., valid location, valid ranges, required relations)
- Methods express **behavior** (not persistence)

---

### 2) Value objects (things defined by their value)
Value objects are immutable and comparable by value:
- `GeoPoint(lat, lon)`
- `TimeRange(start, end)`
- `NDVI(value)`
- `SoilMoisture(vwc)` (with units)

**Value object checklist**
- Prefer `@dataclass(frozen=True)`  
- Validate in `__post_init__`
- No side effects

Example:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class GeoPoint:
    lat: float
    lon: float

    def __post_init__(self) -> None:
        if not (-90.0 <= self.lat <= 90.0):
            raise ValueError("lat must be within [-90, 90]")
        if not (-180.0 <= self.lon <= 180.0):
            raise ValueError("lon must be within [-180, 180]")
```

---

### 3) Domain services (logic that doesn’t “fit” on one entity)
Use a domain service when logic:
- spans multiple entities,
- represents a policy,
- or would make an entity “too smart” / too coupled.

Examples:
- irrigation recommendation rules
- drought risk classification rules
- consent/privacy rule evaluation

Keep domain services:
- pure (or near-pure),
- deterministic,
- dependency-free (except domain models + ports).

---

### 4) Ports / interfaces (how Domain talks outward 🔌)
When Domain needs something external (DB, remote sensing catalog, messaging), define an interface here.

Example (Protocol style):

```python
from typing import Protocol, Sequence
from datetime import datetime

class SoilDataRepository(Protocol):
    def list_readings(
        self,
        field_id: str,
        start: datetime,
        end: datetime,
    ) -> Sequence["SoilMoistureReading"]:
        ...
```

✅ Domain defines the contract.  
🧱 Infrastructure implements it (PostGIS, object storage, GEE adapters, etc.).  
🧪 Tests can use in-memory fakes.

---

## 🗺️ Geospatial & time conventions (keep it boring and explicit)

Because KFM is deeply geospatial/temporal, the domain should adopt simple conventions:

- **CRS:** treat domain geometry inputs as explicitly defined (prefer WGS84 lat/lon unless stated otherwise)
- **Units:** store units in names or value objects (avoid “magic” unit assumptions)
- **Time:** be explicit about timezone handling (prefer aware datetimes at boundaries; keep domain rules consistent)

> If reprojection, raster math, tiling, or heavy GIS operations are required, that belongs outside Domain.

---

## 🧪 Testing expectations (domain should be easy to test)

Domain tests should be:
- ⚡ Fast (no DB, no network)
- 🧼 Deterministic (no time randomness unless injected)
- 🎯 Focused on invariants & behaviors
- 🧩 Able to run with simple fakes/mocks of ports

Suggested test types:
- ✅ Unit tests for value object validation
- ✅ Behavior tests for entity methods/policies
- ✅ Contract tests for ports (interface expectations)

---

## 🛠️ Adding a new domain concept (checklist)

When introducing something new (e.g., a new “Layer”, “Index”, or “Risk Model” concept):

1. 🗣️ **Name it** in KFM’s ubiquitous language (avoid vague “data” objects)
2. 🧱 Decide: **Entity** (identity) vs **Value Object** (value)
3. ✅ Write down invariants as code (range checks, required attributes, relationships)
4. 🔌 If it needs external data, create a **port** in `domain/ports/`
5. 🧪 Add domain tests first (or alongside)
6. 🔄 Wire it up in outer layers (DTO ↔ domain mapping, repo implementations)

---

## 🧯 Quick FAQ

**Q: Where do Pydantic models live?**  
A: Outside Domain (API/interface layer). Domain stays framework-free.

**Q: Where do SQLAlchemy models live?**  
A: Outside Domain (infrastructure/persistence). Domain models are not ORM models.

**Q: Can Domain import GIS libraries?**  
A: Prefer **no**. Keep geometry as simple structures/value objects; do heavy GIS work in adapters/services.

**Q: Where should “privacy/ethics” rules go?**  
A: If it’s a *business rule/policy*, Domain is a great home for it 🧭.

---

## ✅ Definition of done (for Domain PRs)

- [ ] No framework / I/O dependencies added
- [ ] Invariants enforced with tests
- [ ] Ports defined for any outward need
- [ ] Clear naming + minimal coupling
- [ ] Domain remains readable and stable over time ✨