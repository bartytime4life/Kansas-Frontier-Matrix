"""Pure Kansas-envelope NWM WORK projection from captured, verified sources.

No network, filesystem writes, admission, or publication. Channel IDs join
NOAA reference geometry explicitly. An analysis is not a gauge observation.
"""
from __future__ import annotations

from collections import Counter
import csv
from datetime import datetime, timedelta, timezone
import gzip
import io
import json
import math
import re

from connectors.noaa.src.noaa import nwm as source

MAX_OUTPUT = 64*source.MIB
VARIABLES = {"streamflow": "m3 s-1", "velocity": "m s-1", "nudge": "m3 s-1"}


class BoundedBuffer(io.BytesIO):
    def write(self, body):
        if self.tell()+len(body) > MAX_OUTPUT:
            raise ValueError("WORK_BYTE_LIMIT")
        return super().write(body)


def geometry(pages, expected_ids):
    features, seen = {}, set()
    versions = Counter()
    for page in pages:
        if (page.get("error") or page.get("exceededTransferLimit") or
                page.get("geometryType") != "esriGeometryPolyline" or
                page.get("spatialReference", {}).get("wkid") != 4326):
            raise ValueError("GEOMETRY_RESPONSE_INVALID")
        for feature in page.get("features", []):
            attrs = feature["attributes"]
            oid, fid = attrs["oid"], attrs["feature_id"]
            if (type(oid) is not int or oid in seen or not isinstance(fid, str) or
                    not re.fullmatch(r"[1-9]\d{0,11}", fid) or fid in features):
                raise ValueError("GEOMETRY_ID_INVALID_OR_DUPLICATE")
            paths = feature["geometry"]["paths"]
            if not isinstance(paths, list) or not paths or len(paths) > 500:
                raise ValueError("GEOMETRY_PATH_INVALID")
            for line in paths:
                if not 2 <= len(line) <= 10000:
                    raise ValueError("GEOMETRY_LINE_INVALID")
                for point in line:
                    if (len(point) != 2 or not all(type(v) in (int, float) and math.isfinite(v) for v in point)
                            or not -180 <= point[0] <= 180 or not -90 <= point[1] <= 90):
                        raise ValueError("GEOMETRY_COORDINATE_INVALID")
            xs = [p[0] for line in paths for p in line]
            ys = [p[1] for line in paths for p in line]
            west, south, east, north = source.BBOX
            if max(xs) < west or min(xs) > east or max(ys) < south or min(ys) > north:
                raise ValueError("GEOMETRY_OUTSIDE_SELECTION")
            seen.add(oid)
            versions[str(attrs.get("nwm_vers"))] += 1
            features[fid] = {"type": "Feature", "id": fid, "properties": attrs,
                             "geometry": {"type": "MultiLineString", "coordinates": paths}}
    if seen != set(expected_ids) or len(seen) != len(expected_ids) or not 0 < len(features) <= source.MAX_REACHES:
        raise ValueError("GEOMETRY_ID_SET_MISMATCH")
    return features, dict(versions)


def timestamp(variable):
    if variable.shape != (1,) or variable.units != "minutes since 1970-01-01 00:00:00 UTC":
        raise ValueError("NETCDF_TIME_CONTRACT")
    value = variable[:][0]
    if not math.isfinite(float(value)) or float(value) != int(value):
        raise ValueError("NETCDF_TIME_INVALID")
    return (datetime(1970, 1, 1, tzinfo=timezone.utc)+timedelta(minutes=int(value))).isoformat().replace("+00:00", "Z")


def frame(raw, spec, selected_ids):
    import netCDF4
    import numpy as np
    if not 0 < len(raw) <= source.CHANNEL_LIMIT or raw[:8] != b"\x89HDF\r\n\x1a\n":
        raise ValueError("NETCDF_BYTES_INVALID")
    with netCDF4.Dataset("capture.nc", memory=raw) as dataset:
        dataset.set_auto_maskandscale(False)
        ids_var = dataset.variables["feature_id"]
        if len(ids_var.shape) != 1 or not 0 < ids_var.shape[0] <= 3000000 or ids_var.dtype.kind not in "iu":
            raise ValueError("NETCDF_FEATURE_DIMENSION")
        ids = ids_var[:]
        order = np.argsort(ids)
        sorted_ids = ids[order]
        if (np.diff(sorted_ids) <= 0).any():
            raise ValueError("NETCDF_DUPLICATE_IDS")
        selected = np.asarray([int(fid) for fid in selected_ids], dtype=np.int64)
        offsets = np.searchsorted(sorted_ids, selected)
        if (offsets >= len(ids)).any() or not np.array_equal(sorted_ids[offsets], selected):
            raise ValueError("GEOMETRY_MODEL_ID_MISMATCH")
        positions = order[offsets]
        valid = timestamp(dataset.variables["time"])
        reference = timestamp(dataset.variables["reference_time"])
        forecast = spec["product"] == "short_range"
        if (valid != spec["valid_time"] or reference > valid or
                (forecast and reference != spec["filename_cycle_time"]) or
                dataset.model_output_valid_time.replace("_", "T")+"Z" != valid or
                dataset.model_initialization_time.replace("_", "T")+"Z" != reference or
                dataset.model_configuration != ("short_range" if forecast else "analysis_and_assimilation") or
                dataset.model_output_type != "channel_rt"):
            raise ValueError("NETCDF_TIME_OR_PRODUCT_MISMATCH")
        arrays, packing, flags = {}, {}, {}
        for name, units in VARIABLES.items():
            var = dataset.variables[name]
            if var.shape != ids_var.shape or var.units != units or var.dtype.kind not in "iu":
                raise ValueError("NETCDF_VARIABLE_CONTRACT")
            values = var[:][positions]
            scale, offset = float(var.scale_factor), float(var.add_offset)
            bounds = np.asarray(var.valid_range)
            if not all(map(math.isfinite, [scale, offset])) or scale <= 0 or bounds.shape != (2,) or bounds[0] > bounds[1]:
                raise ValueError("NETCDF_PACKING_INVALID")
            missing = (values == var._FillValue) | (values == var.missing_value)
            invalid = ~missing & ((values < bounds[0]) | (values > bounds[1]))
            status = np.where(missing, "missing", np.where(invalid, "outside_valid_range", "valid"))
            arrays[name] = (values, values.astype(np.float64)*scale+offset, status)
            packing[name] = {"units": units, "scale_factor": scale, "add_offset": offset,
                             "_FillValue": int(var._FillValue), "missing_value": int(var.missing_value),
                             "valid_range": bounds.tolist()}
            flags[name] = {"missing": int(missing.sum()), "outside_valid_range": int(invalid.sum())}
        meta = {"filename": spec["name"], "product": spec["product"], "filename_cycle_time": spec["filename_cycle_time"],
                "reference_time": reference, "valid_time": valid, "model_version": dataset.NWM_version_number,
                "source_reaches": len(ids), "selected_reaches": len(selected), "packing": packing, "flags": flags,
                "source_role": "NWM_MODELED_FORECAST_GUIDANCE" if forecast else "NWM_MODELED_ANALYSIS_GUIDANCE"}
        return meta, arrays


def subset(plan, report, reader):
    import netCDF4
    import numpy as np
    refs = report["sources"]
    features, versions = geometry((json.loads(reader(r)) for r in refs[19:]), plan["object_ids"])
    ids = sorted(features, key=int)
    geo_buffer = BoundedBuffer()
    with gzip.GzipFile(fileobj=geo_buffer, mode="wb", mtime=0) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8", newline="") as text:
            json.dump({"type": "FeatureCollection", "selection_bbox": source.BBOX,
                       "selection": plan["selection"], "features": [features[i] for i in ids]}, text, separators=(",", ":"), allow_nan=False)
    table_buffer, frames = BoundedBuffer(), []
    with gzip.GzipFile(fileobj=table_buffer, mode="wb", mtime=0) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8", newline="") as text:
            writer = csv.writer(text)
            writer.writerow(["feature_id", "product", "filename_cycle_time", "reference_time", "valid_time"]+
                            [column for name in VARIABLES for column in [name, name+"_packed", name+"_status"]])
            for spec, ref in zip(plan["models"], refs[:19]):
                meta, arrays = frame(reader(ref), spec, ids)
                meta["source_sha256"] = ref["sha256"]
                frames.append(meta)
                for index, fid in enumerate(ids):
                    row = [fid, meta["product"], meta["filename_cycle_time"], meta["reference_time"], meta["valid_time"]]
                    for name in VARIABLES:
                        packed, decoded, status = arrays[name]
                        row += [format(decoded[index], ".17g") if status[index] == "valid" else "", int(packed[index]), str(status[index])]
                    writer.writerow(row)
    summary = {"reaches": len(ids), "frames": len(frames), "rows": len(ids)*len(frames),
               "geometry_source_versions": versions, "forecast_start": frames[1]["valid_time"], "forecast_end": frames[-1]["valid_time"],
               "forecast_reference_time": frames[1]["reference_time"], "analysis_reference_time": frames[0]["reference_time"],
               "analysis_valid_time": frames[0]["valid_time"], "model_versions": sorted({f["model_version"] for f in frames}),
               "all_geometry_ids_matched": True, "geometry_version_compatibility_review": "pending",
               "software": {"netCDF4": netCDF4.__version__, "numpy": np.__version__}}
    metadata = {**summary, "selection_bbox": source.BBOX, "frames": frames, "geometry_crs": "EPSG:4326",
                "limitations": ["Envelope intersection, not an exact Kansas boundary clip.",
                                "Geometry and model version attributes are preserved; ID matching does not prove version compatibility.",
                                "One frozen run, not a live feed or historical archive; no temporal interpolation.",
                                "Model guidance is not observed discharge, an RFC forecast, or an emergency warning.",
                                "CSV decoded values use recorded packing; blank values retain packed values and quality status.",
                                "WORK candidate only; source admission, geometry review and map release remain pending."]}
    return {"kansas-envelope-flowlines.geojson.gz": geo_buffer.getvalue(),
            "kansas-envelope-streamflow.csv.gz": table_buffer.getvalue(),
            "subset-metadata.json": json.dumps(metadata, indent=2, sort_keys=True, allow_nan=False).encode()+b"\n"}, summary
