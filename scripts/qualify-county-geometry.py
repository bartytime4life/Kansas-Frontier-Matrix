"""Offline county geometry investigation; emits WORK candidates, never a release.

See docs/county-history-qualification.md for dependency pins and limitations.
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import zipfile

spec = importlib.util.spec_from_file_location(
    "county_qualification", Path(__file__).with_name("qualify-county-history.py"))
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def dependencies():
    import pyproj
    import shapely
    q.require(pyproj.__version__ == "3.7.2", "REQUIRES_PYPROJ_3_7_2")
    q.require(shapely.__version__ == "2.1.2", "REQUIRES_SHAPELY_2_1_2")
    q.require(shapely.geos_version >= (3, 12, 0), "REQUIRES_GEOS_3_12")
    pyproj.network.set_network_enabled(False)
    return pyproj, shapely


def coordinate_operation(wkt, extent):
    """Select the named, bounded display operation; never accept a fallback."""
    pyproj, _ = dependencies()
    from pyproj.aoi import AreaOfInterest
    from pyproj.transformer import TransformerGroup
    q.require(pyproj.CRS.from_wkt(wkt).equals(pyproj.CRS("EPSG:4269"), ignore_axis_order=True), "SOURCE_CRS")
    group = TransformerGroup(wkt, "OGC:CRS84", always_xy=True,
                             area_of_interest=AreaOfInterest(*extent), allow_ballpark=False)
    # PROJ may label an axis-normalized operation DERIVED_FROM(EPSG).
    # Retain the complete PROJJSON and check its method/parameters as well.
    candidates = [t for t in group.transformers if any(
        step.get("id", {}).get("authority") in ("EPSG", "DERIVED_FROM(EPSG)") and
        step.get("id", {}).get("code") == 1188 and
        step.get("method", {}).get("id") == {"authority": "EPSG", "code": 9603} and
        [(p.get("id", {}).get("code"), p.get("value")) for p in step.get("parameters", [])] ==
        [(8605, 0), (8606, 0), (8607, 0)]
        for step in t.to_json_dict().get("steps", []))]
    q.require(len(candidates) == 1, "EPSG_1188_UNAVAILABLE_OR_AMBIGUOUS")
    transformer = candidates[0]
    q.require(transformer.accuracy == 4.0 and not transformer.is_network_enabled,
              "COORDINATE_OPERATION_CONTRACT")
    area = transformer.area_of_use
    q.require(area.west <= extent[0] <= extent[2] <= area.east and
              area.south <= extent[1] <= extent[3] <= area.north, "OPERATION_AREA")
    return transformer, {
        "sourceCrs": "EPSG:4269", "targetCrs": "OGC:CRS84", "axisOrder": "longitude_latitude",
        "operationId": "EPSG:1188", "operationName": "NAD83 to WGS 84 (1)",
        "operationAccuracyMetres": transformer.accuracy,
        "accuracyMeaning": "Operation metadata, not historical boundary accuracy or a survey guarantee.",
        "definition": transformer.definition, "projjson": transformer.to_json_dict(),
        "networkEnabled": False, "ballparkAllowed": False,
        "limitation": "Explicit zero-translation display operation; no realization/epoch-specific or survey-grade accuracy claimed.",
    }


def individual_validity(geometries):
    _, shapely = dependencies()
    return [{"recordNumber": i + 1, "reason": str(shapely.is_valid_reason(g))}
            for i, g in enumerate(geometries)
            if g.geom_type not in ("Polygon", "MultiPolygon") or g.is_empty or not g.is_valid]


def coverage_epochs(rows, geometries):
    """Check every change in membership, including ends with no incoming version.

    A coverage may contain holes. No claim of geographic completeness is made.
    Overlap includes containment and duplicate polygons, not just overlaps().
    """
    _, shapely = dependencies()
    q.require(len(rows) == len(geometries) and not individual_validity(geometries),
              "COVERAGE_REQUIRES_VALID_POLYGONS")
    intervals = [q.interval(row) for row in rows]
    boundaries = sorted({q.FIRST, q.LAST + dt.timedelta(days=1)} |
                        {day for interval in intervals for day in interval})
    epochs = []
    for start, end in zip(boundaries, boundaries[1:]):
        indices = [i for i, (a, b) in enumerate(intervals) if a <= start < b]
        selected = [geometries[i] for i in indices]
        valid = bool(selected) and bool(shapely.coverage_is_valid(selected, gap_width=0.0))
        overlaps, invalid_records = [], []
        if selected and not valid:
            tree = shapely.STRtree(selected)
            for i, geometry in enumerate(selected):
                for j in sorted(int(j) for j in tree.query(geometry, predicate="intersects")):
                    if j > i and geometry.relate_pattern(selected[j], "2********"):
                        overlaps.append([indices[i] + 1, indices[j] + 1])
            invalid_records = [indices[i] + 1 for i, edge in enumerate(
                shapely.coverage_invalid_edges(selected, gap_width=0.0)) if not edge.is_empty]
        epochs.append({"validFrom": start.isoformat(), "validToExclusive": end.isoformat(),
                       "featureCount": len(selected), "coverageValid": valid,
                       "interiorOverlapRecordPairs": overlaps,
                       "invalidEdgeRecordNumbers": invalid_records})
    return epochs


def selected_epoch(epochs, day):
    matches = [e for e in epochs if e["validFrom"] <= day.isoformat() < e["validToExclusive"]]
    q.require(len(matches) == 1, "SELECTED_EPOCH")
    return matches[0]


def prepare(path, day):
    q.require(type(day) is dt.date and q.FIRST <= day <= q.LAST, "DATE_COVERAGE")
    # Reuse all archive, chronology, temporal, rights and identity checks.
    result = q.qualify(path, day)
    pyproj, shapely = dependencies()
    import numpy
    import shapefile
    from shapely.geometry import shape, mapping
    from shapely.ops import transform
    with zipfile.ZipFile(io.BytesIO(q.read_pinned_archive(path))) as archive:
        with shapefile.Reader(**{ext: io.BytesIO(archive.read(q.SHAPE + ext))
                                 for ext in ("shp", "shx", "dbf")}, encoding="cp1252") as reader:
            rows = [r.as_dict() for r in reader.records()]
            geometries = [shape(s.__geo_interface__) for s in reader.shapes()]
    transformer, operation = coordinate_operation(result["source"]["projectionWkt"],
                                                   result["sourceExtentNad83"])
    projection_member = next(m for m in result["members"] if m["path"] == q.SHAPE + "prj")
    operation["sourceProjectionEvidenceRef"] = {
        "artifactId": "sha256:" + projection_member["sha256"], "locatorKind": "whole_archive_member"}
    source_invalid = individual_validity(geometries)
    transformed = [shapely.orient_polygons(transform(
        lambda x, y: transformer.transform(x, y, errcheck=True), geometry), exterior_cw=False)
        for geometry in geometries]
    for source, target in zip(geometries, transformed):
        coords = shapely.get_coordinates(target)
        q.require(bool(numpy.isfinite(coords).all()) and
                  bool((abs(coords[:, 0]) <= 180).all()) and
                  bool((abs(coords[:, 1]) <= 90).all()), "OUTPUT_COORDINATES")
        q.require(shapely.get_num_coordinates(source) == shapely.get_num_coordinates(target),
                  "TRANSFORM_VERTEX_COUNT")
    target_invalid = individual_validity(transformed)
    source_epochs = coverage_epochs(rows, geometries) if not source_invalid else []
    target_epochs = coverage_epochs(rows, transformed) if not target_invalid else []
    selected = selected_epoch(target_epochs, day) if target_epochs else None
    source_selected = selected_epoch(source_epochs, day) if source_epochs else None
    ready = (not source_invalid and not target_invalid and bool(selected) and
             selected["coverageValid"] and bool(source_selected) and source_selected["coverageValid"])
    snapshot = result["snapshot"]
    # Keep the existing coordinate-free query contract intact. Extend its evidence
    # bundle only in the new geometry candidate, with the exact CRS/index members.
    bundle = {**snapshot["evidenceBundle"], "artifacts": dict(snapshot["evidenceBundle"]["artifacts"])}
    for member in result["members"]:
        if member["path"] in (q.SHAPE + "prj", q.SHAPE + "shx"):
            bundle["artifacts"]["sha256:" + member["sha256"]] = {
                "member": member["path"], "sha256": member["sha256"], "bytes": member["bytes"]}
    problem_records = sorted({n for epochs in (source_epochs, target_epochs) for e in epochs
                              for n in e["invalidEdgeRecordNumbers"]} |
                             {r["recordNumber"] for r in source_invalid + target_invalid})
    receipts = {m["path"]: m for m in result["members"]}
    diagnostics = [{"recordNumber": n, "institutionSourceId": rows[n-1]["ID"],
                    "sourceName": rows[n-1]["NAME"], "change": rows[n-1]["CHANGE"],
                    "citation": rows[n-1]["CITATION"],
                    "evidenceRefs": [{"artifactId": "sha256:" + receipts[q.SHAPE + ext]["sha256"],
                                      "recordNumber": n, "locatorKind": "shape_dbf_record_1_based"}
                                     for ext in ("shp", "dbf")]}
                   for n in problem_records]
    result["geometryQualification"] = {
        "format": "county_history_geometry_work_v1", "lifecycle": "WORK", "releaseEligible": False,
        "selectedDay": day.isoformat(), "candidateState": "WORK" if ready else "QUARANTINE",
        "individualSourceInvalid": source_invalid, "individualTransformedInvalid": target_invalid,
        "sourceCoverageEpochs": source_epochs, "transformedCoverageEpochs": target_epochs,
        "selectedEpoch": selected, "sourceRecordDiagnostics": diagnostics,
        "coverageMeaning": "Planar polygon validity and edge matching with gap_width=0; holes permitted. No geographic completeness or legal authority established.",
        "coordinateOperation": operation,
        "transforms": ["EPSG:1188 with longitude/latitude axis order", "RFC 7946 ring orientation"],
        "repairs": [], "clipping": None, "simplification": None,
        "toolchain": {"python": ".".join(map(str, sys.version_info[:3])), "pyshp": shapefile.__version__,
                      "shapely": shapely.__version__, "geos": shapely.geos_version_string,
                      "numpy": numpy.__version__, "pyproj": pyproj.__version__, "proj": pyproj.proj_version_str,
                      "projDatabaseSha256": hashlib.sha256(
                          (Path(pyproj.datadir.get_data_dir()) / "proj.db").read_bytes()).hexdigest()},
    }
    result["geometryCandidate"] = None
    if ready:
        features = []
        for record in snapshot["boundaryVersions"]:
            n = record["evidenceRefs"][0]["recordNumber"]
            geometry = mapping(transformed[n-1])
            features.append({"type": "Feature", "id": record["id"], "geometry": geometry,
                             "properties": {**record, "geometrySha256": digest(geometry)}})
        candidate = {"type": "FeatureCollection", "lifecycle": "WORK", "releaseEligible": False,
                     "selectedDay": day.isoformat(), "features": features,
                     "evidenceBundle": bundle, "coordinateOperation": operation}
        result["geometryCandidate"] = candidate
        result["geometryQualification"]["candidateSha256"] = digest(candidate)
    result["qualification"] = ("offline_geometry_passed_for_selected_day" if ready else
                               "offline_geometry_quarantined_for_selected_day")
    # These broad limitations are narrowed, not erased or promoted to release proof.
    result["notEstablished"] = [s for s in result["notEstablished"] if s not in ("topology", "datum_transformation")]
    result["notEstablished"] += ["disputed_coverage_interpretation", "geographic_completeness",
                                 "historical_positional_accuracy", "survey_grade_datum_transformation"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="Exact local KS_AtlasHCB.zip")
    parser.add_argument("--date", required=True, help="YYYY-MM-DD within mapped coverage")
    args = parser.parse_args()
    try:
        result = prepare(args.archive, q.query_date(args.date))
        print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))
    except Exception as error:
        # Do not emit a partial geometry candidate after a library/validation failure.
        print(json.dumps({"status": "ERROR", "releaseEligible": False,
                          "error": type(error).__name__ + ": " + str(error)}))
        return 1
    return 0 if result["geometryCandidate"] is not None else 2


if __name__ == "__main__":
    sys.exit(main())
