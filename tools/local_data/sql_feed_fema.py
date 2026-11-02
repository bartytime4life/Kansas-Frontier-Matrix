"""OpenFEMA feed: Kansas extracts of five FEMA datasets, each replaced whole when FEMA refreshes it.

OpenFEMA (https://www.fema.gov/api/open/; terms https://www.fema.gov/about/openfema/terms-conditions) serves
these as public data FEMA has already redacted: the NFIP datasets are FEMA's redacted claims and policies (no
names or street addresses, city withheld, coordinates rounded to 0.1 degree, census block group kept), and the
grant datasets name public applicants (governments, tribes, non-profits). Every record and every field is kept
as FEMA serves it; nothing is left out here.

Datasets (version, Kansas filter; Kansas records on 2026-11-02; FEMA's refresh):
- DisasterDeclarationsSummaries v2, state eq 'KS' (1,969; every 20 minutes)
- NfipClaims v3, state eq 'KS' (7,901; monthly)
- NfipPolicies v3, propertyState eq 'KS' (183,484; monthly)
- PublicAssistanceFundedProjectsDetails v2, stateAbbreviation eq 'KS' (14,476; daily)
- HmaSubapplications v2 (673; daily). It replaced HazardMitigationAssistanceProjects, which OpenFEMA no longer
  lists or serves. 73 Kansas rows, older grants among them, have no state abbreviation, so the filter is
  subapplicantState eq 'Kansas' or subapplicantStateAbbreviation eq 'KS'.

Each record is stored whole as canonical JSON (record_json) beside key columns: ids, dates, the county GEOID
and amounts. An extract is paged in key order ($orderby on the primary key, "$filter=<Kansas> and key gt
<last>", $top 10,000): $skip deep into NfipPolicies times out, keyset paging does not. Pages stream into a
gzipped JSON Lines file outside data/, one record per line in key order, so the largest extract is never held
in memory. The record count must equal FEMA's $inlinecount with no key twice, or the run stops with
FEMA_EXTRACT_SHIFTED (FEMA refreshed the dataset mid-extract; the next run retries).

Schedule and revisions: each run reads the dataset list (v1/OpenFemaDataSets) once. A dataset is extracted
again when its lastDataSetRefresh changed, at most as often as its accrualPeriodicity allows (20 minutes or
daily: daily; monthly: every 25 days). The Kansas extract replaces the version loaded before (key = dataset
name); an unchanged extract has the same SHA-256 and is not loaded again. A dataset FEMA no longer lists in
this version stops the run after the others are done (FEMA_DATASET_RETIRED); a planned retirement (depDate)
is reported in the summary as "retiring".
"""
from __future__ import annotations

from dataclasses import dataclass
import gzip
import json
from pathlib import Path
import re
from typing import Callable
import urllib.parse

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feed_hazards import age_days, ddl, keep_version, save_state, snake
from tools.local_data.sql_feeds import FeedError

API = "https://www.fema.gov/api/open/"
LISTING = API + "v1/OpenFemaDataSets?$select=name,version,lastDataSetRefresh,accrualPeriodicity,depDate&$top=1000"
PAGE = 10_000                # OpenFEMA's $top maximum
PAGE_BYTES = 256_000_000
MAX_RECORDS = 2_000_000      # a larger Kansas extract means the filter failed


@dataclass(frozen=True)
class Dataset:
    name: str
    version: str
    kansas: str                                 # OData filter
    is_kansas: Callable[[dict], bool]
    key: str                                    # primary key, for keyset paging
    table: str
    spec: str                                   # key columns: "field[:TYPE] ...", stored as snake_case
    county: tuple | None                        # ((fields...), geoid from their values)
    indexes: tuple

    @property
    def fields(self) -> list[str]:
        return [token.split(":")[0] for token in self.spec.split()]

    @property
    def columns(self) -> list[str]:
        return [snake(f) for f in self.fields] + (["county_geoid"] if self.county else []) + ["record_json"]

    def ddl(self) -> str:
        types = {snake(f): t for f, _, t in (token.partition(":") for token in self.spec.split()) if t}
        return ddl(self.table, self.columns, {**types, "record_json": "TEXT NOT NULL"}, self.indexes)


def _nonzero(code) -> bool:
    return bool(code) and bool(str(code).strip("0"))


DATASETS = (
    Dataset("DisasterDeclarationsSummaries", "v2", "state eq 'KS'", lambda r: r.get("state") == "KS", "id",
            "kfm_fema_disaster_declarations",
            "id disasterNumber:INTEGER femaDeclarationString declarationType declarationDate fyDeclared:INTEGER incidentType "
            "declarationTitle incidentBeginDate incidentEndDate designatedArea placeCode",
            (("fipsStateCode", "fipsCountyCode"), lambda s, c: s + c if s and _nonzero(c) else None),
            (("disaster_number",), ("county_geoid", "declaration_date"))),
    Dataset("NfipClaims", "v3", "state eq 'KS'", lambda r: r.get("state") == "KS", "id", "kfm_fema_nfip_claims",
            "id:INTEGER dateOfLoss yearOfLoss:INTEGER censusGeoid nfipCommunityNumberCurrent floodEvent causeOfDamage "
            "amountPaidOnBuildingClaim:REAL amountPaidOnContentsClaim:REAL amountPaidOnIncreasedCostOfComplianceClaim:REAL "
            "buildingDamageAmount:INTEGER contentsDamageAmount:INTEGER asOfDate",
            (("countyCode",), lambda c: c if c and len(c) == 5 else None),
            (("county_geoid", "date_of_loss"), ("year_of_loss",))),
    Dataset("NfipPolicies", "v3", "propertyState eq 'KS'", lambda r: r.get("propertyState") == "KS", "id", "kfm_fema_nfip_policies",
            "id:INTEGER policyEffectiveDate policyTerminationDate censusGeoid nfipCommunityNumberCurrent ratedFloodZone "
            "occupancyType:INTEGER policyCount:INTEGER totalBuildingInsuranceCoverage:INTEGER totalContentsInsuranceCoverage:INTEGER "
            "totalInsurancePremiumOfThePolicy:INTEGER policyCost:INTEGER asOfDate",
            (("censusGeoid",), lambda g: g[:5] if g and len(g) >= 5 else None),
            (("county_geoid", "policy_effective_date"),)),
    Dataset("PublicAssistanceFundedProjectsDetails", "v2", "stateAbbreviation eq 'KS'", lambda r: r.get("stateAbbreviation") == "KS",
            "gmProjectId", "kfm_fema_pa_projects",
            "gmProjectId:INTEGER disasterNumber:INTEGER pwNumber:INTEGER declarationDate incidentType applicantId applicationTitle "
            "damageCategoryCode projectSize projectStatus county projectAmount:REAL federalShareObligated:REAL totalObligated:REAL "
            "firstObligationDate lastObligationDate",
            (("stateNumberCode", "countyCode"), lambda s, c: s.zfill(2) + c.zfill(3) if s and _nonzero(c) else None),
            (("disaster_number",), ("county_geoid",))),
    Dataset("HmaSubapplications", "v2", "subapplicantState eq 'Kansas' or subapplicantStateAbbreviation eq 'KS'",
            lambda r: r.get("subapplicantState") == "Kansas" or r.get("subapplicantStateAbbreviation") == "KS", "id",
            "kfm_fema_hma_subapplications",
            "id subapplicationIdentifier program fiscalYear:INTEGER disasterNumber status subapplicantName subapplicantType "
            "benefitingCounties primaryHazard dateSubmittedToFema federalShareAmount:REAL totalSubapplicationAmount:REAL "
            "totalObligatedAmount:REAL totalPaymentAmount:REAL",
            None, (("fiscal_year",), ("disaster_number",))),
)


def gap_days(periodicity) -> int:
    """Least days between extracts, from FEMA's ISO 8601 accrualPeriodicity (R/PT20M, R/P1D, R/P1M, irregular)."""
    found = re.fullmatch(r"R/P(\d+)([DWMY])", periodicity or "")
    return int(found.group(1)) * {"D": 1, "W": 6, "M": 25, "Y": 330}[found.group(2)] if found else 1


def _literal(value) -> str:
    return str(value) if isinstance(value, int) else "'" + str(value).replace("'", "''") + "'"


def page_url(ds: Dataset, last=None) -> str:
    where = ds.kansas if last is None else f"({ds.kansas}) and {ds.key} gt {_literal(last)}"
    return (f"{API}{ds.version}/{ds.name}?$filter={urllib.parse.quote(where, safe='')}&$orderby={ds.key}&$top={PAGE}"
            + ("&$inlinecount=allpages" if last is None else ""))


def extract(ctx, ds: Dataset, temp: Path) -> tuple[int, str, int]:
    """Stream the Kansas records into temp as gzipped canonical JSON Lines: (records, first page URL, bytes downloaded)."""
    needed = set(ds.fields) | set(ds.county[0] if ds.county else ())
    keys, last, total, first, downloaded = set(), None, None, None, 0
    with open(temp, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as out:
        while True:
            url = page_url(ds, last)
            body = ctx.fetch(url, limit=PAGE_BYTES, timeout=600).body
            downloaded += len(body)
            try:
                payload = json.loads(body)
            except ValueError:
                raise FeedError(f"FEMA_RESPONSE_SHAPE {ds.name}") from None
            records = payload.get(ds.name) if isinstance(payload, dict) else None
            if not isinstance(records, list):
                raise FeedError(f"FEMA_RESPONSE_SHAPE {ds.name}")
            if last is None:
                first, total = url, (payload.get("metadata") or {}).get("count")
            for record in records:
                if not isinstance(record, dict) or not needed <= record.keys():
                    raise FeedError(f"FEMA_COLUMNS_CHANGED {ds.name} {sorted(needed - set(record))[:5] if isinstance(record, dict) else ''}")
                if not ds.is_kansas(record):
                    raise FeedError(f"FEMA_NOT_KANSAS {ds.name} {record[ds.key]}")
                if record[ds.key] in keys:
                    raise FeedError(f"FEMA_EXTRACT_SHIFTED {ds.name} {ds.key} {record[ds.key]} twice")
                keys.add(record[ds.key])
                out.write((core.canonical(record) + "\n").encode())
            if len(keys) > MAX_RECORDS:
                raise FeedError(f"FEMA_EXTRACT_TOO_LARGE {ds.name}")
            if len(records) < PAGE:
                break
            last = records[-1][ds.key]
    if total != len(keys):
        raise FeedError(f"FEMA_EXTRACT_SHIFTED {ds.name} {len(keys)} of {total}")
    return len(keys), first, downloaded


def rows(path: Path, ds: Dataset):
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            county = (ds.county[1](*(record[f] for f in ds.county[0])),) if ds.county else ()
            yield (*(record[f] for f in ds.fields), *county, line.rstrip("\n"))


def fema(ctx, datasets=DATASETS) -> dict:
    db = core.open_db(ctx)
    try:
        with core.pipeline_lock(ctx):
            db.executescript("".join(ds.ddl() for ds in datasets))
        state, today = core.get_state(db, "fema"), ctx.now().date()
        listing = json.loads(ctx.fetch(LISTING, limit=16_000_000).body).get("OpenFemaDataSets") or []
        listing = {(r.get("name"), f"v{r.get('version')}"): r for r in listing if isinstance(r, dict)}
        summary, problems = {"rows": 0}, []
        for ds in datasets:
            meta, seen = listing.get((ds.name, ds.version)), state.get(ds.name, {})
            if meta is None:
                problems.append(f"FEMA_DATASET_RETIRED {ds.name}/{ds.version}")
                continue
            if meta.get("depDate"):
                summary.setdefault("retiring", {})[ds.name] = meta["depDate"]
            refresh, age = meta.get("lastDataSetRefresh"), age_days(seen, "fetched", today)
            if (refresh and refresh == seen.get("refresh")) or (age is not None and age < gap_days(meta.get("accrualPeriodicity"))):
                summary[ds.name] = "not_due"
                continue
            temp = core.temp_path(ctx, f"fema-{ds.name}.jsonl.gz")
            try:
                count, url, downloaded = extract(ctx, ds, temp)
                if not count and seen.get("records"):
                    problems.append(f"FEMA_KANSAS_EMPTY {ds.name}")
                    continue
                result = {"state": "empty", "rows": 0} if not count else keep_version(
                    ctx, db, feed="fema", source_id=f"openfema-{ds.name}", key=ds.name, name=f"{ds.name}/{ds.name}-{ds.version}-KS",
                    ext=".jsonl.gz", body=temp, url=url, table=ds.table, width=len(ds.columns), rows=lambda path, ds=ds: rows(path, ds),
                    extra={"dataset": ds.name, "version": ds.version, "filter": ds.kansas, "records": count, "downloaded_bytes": downloaded,
                           "dataset_refresh": refresh})
            finally:
                temp.unlink(missing_ok=True)
            state = save_state(ctx, db, "fema", {**state, ds.name: {"refresh": refresh, "fetched": str(today), "records": count}})
            summary[ds.name] = f"{result['state']} {count}"
            summary["rows"] += result["rows"]
        if problems:
            raise FeedError("; ".join(problems))
        return summary
    finally:
        db.close()
