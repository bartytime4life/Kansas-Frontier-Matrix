"""NWM feed: one analysis-and-assimilation run a day (12Z), Kansas reaches only.

The CONUS channel_rt NetCDF (about 12 MB, 2.8 million reaches) is read once and discarded; the
kept raw copy is a CSV of the packed integers for the Kansas reaches listed in the NWM GeoPackage,
with a receipt recording the original file's size and SHA-256. Rows go to ``kfm_nwm_channel_rt``
in the shape of the 2026-10-07 load: unpacked values (NULL when missing), the exact packed integers
and each value's status. Needs netCDF4 and numpy, so run it with the private NWM environment's
Python. Days are caught up from the last loaded run, at most ``MAX_DAYS`` per run.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
import csv
import io
import sqlite3
import tempfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

URL = "https://noaa-nwm-pds.s3.amazonaws.com/nwm.{day}/analysis_assim/nwm.t{hour:02d}z.analysis_assim.channel_rt.tm00.conus.nc"
CYCLE_HOUR = 12
FIRST_DAY = date(2026, 10, 8)   # the archived load is the 2026-10-07 run
MAX_DAYS = 7
VARIABLES = ("streamflow", "velocity", "nudge")


def kansas_reaches(gpkg) -> list[int]:
    db = sqlite3.connect(f"file:{gpkg}?mode=ro", uri=True)
    try:
        return sorted({int(r[0]) for r in db.execute("SELECT feature_id FROM nwm_v30_flowlines")})
    finally:
        db.close()


def _minutes(value) -> str:
    return (datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(minutes=int(value))).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract(path, reaches: list[int]) -> dict:
    """Kansas rows from one channel_rt file: packed integers, unpacked values and statuses."""
    import netCDF4
    import numpy as np

    with netCDF4.Dataset(path) as ds:
        if getattr(ds, "model_output_type", "") != "channel_rt":
            raise FeedError("NWM_NOT_CHANNEL_RT")
        ids = ds.variables["feature_id"][:]
        wanted = np.isin(ids, np.asarray(reaches, dtype=ids.dtype))
        out = {"feature_id": ids[wanted].astype("int64"), "attrs": {k: str(getattr(ds, k)) for k in ds.ncattrs()},
               "reference_time": _minutes(ds.variables["reference_time"][0]), "valid_time": _minutes(ds.variables["time"][0])}
        for name in VARIABLES:
            var = ds.variables[name]
            var.set_auto_maskandscale(False)
            packed = var[:][wanted]
            fill, scale, offset = int(var._FillValue), np.float32(var.scale_factor), np.float32(getattr(var, "add_offset", 0.0))
            low, high = (int(x) for x in getattr(var, "valid_range", (-2**31, 2**31 - 1)))
            out[name] = (packed, fill, scale, offset, low, high)
    return out


def rows_for(data: dict, cycle: str):
    """kfm_nwm_channel_rt rows in the 2026-10-07 load's shape."""
    import numpy as np

    columns = []
    for name in VARIABLES:
        packed, fill, scale, offset, low, high = data[name]
        values = (packed.astype(np.float32) * scale + offset)
        status = np.where(packed == fill, "missing", np.where((packed < low) | (packed > high), "out_of_range", "valid"))
        columns.append((packed, values, status))
    for i, feature in enumerate(data["feature_id"]):
        row = [int(feature), "analysis_assim", cycle, data["reference_time"], data["valid_time"]]
        for packed, values, status in columns:
            state = str(status[i])
            row += [float(values[i]) if state == "valid" else None, int(packed[i]), state]
        yield tuple(row)


def nwm(ctx) -> dict:
    if not ctx.nwm_gpkg:
        raise FeedError("NWM_GEOPACKAGE_REQUIRED")
    reaches = kansas_reaches(ctx.nwm_gpkg)
    db = core.open_db(ctx)
    summary = {"runs": 0, "rows": 0}
    try:
        state = core.get_state(db, "nwm")
        day = date.fromisoformat(state.get("next_day", str(FIRST_DAY)))
        today = ctx.now().date()
        for _ in range(MAX_DAYS):
            if day > today:
                break
            url = URL.format(day=day.strftime("%Y%m%d"), hour=CYCLE_HOUR)
            fetched = ctx.fetch(url, limit=64_000_000, timeout=600, missing_ok=True)
            if fetched is None:
                if day < today - timedelta(days=2):
                    # Gone from the bucket: record the gap and move on rather than stall.
                    summary.setdefault("missing_days", []).append(str(day))
                    day += timedelta(days=1)
                    continue
                break
            with tempfile.NamedTemporaryFile(suffix=".nc") as temp:
                temp.write(fetched.body)
                temp.flush()
                data = extract(temp.name, reaches)
            cycle = f"{day:%Y-%m-%d}T{CYCLE_HOUR:02d}:00:00Z"
            rows = list(rows_for(data, cycle))
            out = io.StringIO()
            writer = csv.writer(out, lineterminator="\n")
            writer.writerow(["feature_id", *[f"{v}_packed" for v in VARIABLES]])
            writer.writerows((r[0], r[6], r[9], r[12]) for r in rows)
            path, digest = core.store_raw(ctx, "nwm", f"{day:%Y}/nwm-{day:%Y%m%d}-t{CYCLE_HOUR:02d}z-analysis-assim-channel-rt-kansas.csv.gz",
                                          core.gz(out.getvalue().encode()), url=url, fetched=fetched, original=fetched.body,
                                          extra={"kansas_reaches": len(rows), "reference_time": data["reference_time"], "valid_time": data["valid_time"],
                                                 "model": {k: data["attrs"].get(k) for k in ("NWM_version_number", "model_configuration", "model_initialization_time", "model_output_valid_time")}})
            with core.pipeline_lock(ctx):
                file_id = core.begin_source(db, ctx, "noaa-nwm-channel-rt", path, digest, url, core.receipt_for(ctx, path))
                if file_id is not None:
                    try:
                        db.executemany("INSERT INTO kfm_nwm_channel_rt VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
                        core.finish_source(db, file_id, len(rows))
                    except BaseException:
                        db.execute("ROLLBACK")
                        raise
                    summary["rows"] += len(rows)
                    summary["runs"] += 1
                day += timedelta(days=1)
                core.set_state(db, ctx, "nwm", {**state, "next_day": str(day)})
                state = core.get_state(db, "nwm")
        return {**summary, "next_day": str(day)}
    finally:
        db.close()
