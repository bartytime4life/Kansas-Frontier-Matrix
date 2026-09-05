"""Pure, strict Esri polyline -> WGS84 2D display conversion.

Native source arrays remain untouched. Curves, ambiguous dimensions and unknown
CRSs fail closed. Optional pyproj is imported only when conversion is requested.
This helper is not source-admission, rights, or publication authority.
"""
from __future__ import annotations
import math
from typing import Any

class GeometryError(ValueError):
    """Finite geometry error; source acquisition and policy are owned elsewhere."""
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def require(condition: bool, code: str) -> None:
    if not condition:
        raise GeometryError(code)


def finite_number(value: Any) -> bool:
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


SUPPORTED_WKIDS = {4326, 3857, 102100, 6923}


def polyline_to_geojson(geometry: dict[str, Any], spatial_reference: dict[str, Any], *,
                        has_z: bool, has_m: bool, maximum_vertices: int = 20_000) -> tuple[dict, dict]:
    require(type(maximum_vertices) is int and 2 <= maximum_vertices <= 100_000,
            "INVALID_VERTEX_LIMIT")
    require(isinstance(geometry, dict), "GEOMETRY_MISSING")
    require("curvePaths" not in geometry and "rings" not in geometry and "points" not in geometry,
            "UNSUPPORTED_CURVE_OR_GEOMETRY")
    require(set(geometry) <= {"paths", "spatialReference"}, "GEOMETRY_FIELDS_UNSUPPORTED")
    require(type(has_z) is bool and type(has_m) is bool, "DIMENSION_FLAGS")
    require("spatialReference" not in geometry or geometry["spatialReference"] == spatial_reference,
            "FEATURE_CRS_DRIFT")
    require(isinstance(spatial_reference, dict), "CRS_MISSING")
    require(set(spatial_reference) <= {"wkid", "latestWkid", "wkt"}, "CRS_FIELDS_UNSUPPORTED")
    native = spatial_reference.get("wkid")
    latest = spatial_reference.get("latestWkid", native)
    require(native is None or type(native) is int, "CRS_NOT_SUPPORTED")
    require(native is None or latest == native or (native, latest) == (102100, 3857),
            "CRS_ALIAS_CONFLICT")
    wkid = latest
    require(type(wkid) is int and wkid in SUPPORTED_WKIDS, "CRS_NOT_SUPPORTED")
    require(not spatial_reference.get("wkt"), "CUSTOM_CRS_REVIEW_REQUIRED")
    paths = geometry.get("paths")
    require(isinstance(paths, list) and 0 < len(paths) <= 1_000, "INVALID_PATHS")
    dimension = 2 + int(has_z) + int(has_m)
    count = 0
    for path in paths:
        require(isinstance(path, list) and len(path) >= 2, "DEGENERATE_PATH")
        count += len(path)
        require(count <= maximum_vertices, "VERTEX_BUDGET")
        for point in path:
            require(isinstance(point, list) and len(point) == dimension, "AMBIGUOUS_DIMENSION")
            require(all(finite_number(v) for v in point), "NONFINITE_COORDINATE")
        require(any(point[:2] != path[0][:2] for point in path[1:]), "DEGENERATE_PATH")
    try:
        from pyproj import CRS, Transformer, __version__, network
        require(not network.is_network_enabled(), "PROJ_NETWORK_MUST_BE_OFF")
        source = CRS.from_epsg(3857 if wkid == 102100 else wkid)
        transformer = Transformer.from_crs(source, CRS.from_epsg(4326), always_xy=True,
                                            allow_ballpark=False, only_best=True)
        converted = []
        for path in paths:
            coords = []
            for point in path:
                x, y = transformer.transform(point[0], point[1], errcheck=True)
                require(math.isfinite(x) and math.isfinite(y) and -180 <= x <= 180 and -85 <= y <= 85,
                        "OUTPUT_COORDINATE_RANGE")
                coords.append([x, y])
            converted.append(coords)
        receipt = {"engine": "pyproj", "engine_version": __version__, "input_crs": dict(spatial_reference),
                   "input_horizontal_units": [a.unit_name for a in source.axis_info[:2]],
                   "output_crs": "OGC:CRS84 longitude,latitude", "always_xy": True,
                   "operation": transformer.description, "operation_definition": transformer.definition,
                   "operation_accuracy_m": transformer.accuracy, "datum_ballpark_allowed": False,
                   "network_grids": False, "native_vertices": count, "native_parts": len(paths),
                   "display_parts": len(converted), "z_removed_for_display": has_z,
                   "m_removed_for_display": has_m, "native_z_m_preserved": True,
                   "vertical_transform": "none; no height claim", "curve_flattening": "none; curves rejected",
                   "simplification": "none", "coordinate_rounding": "none",
                   "uncertainty": "operation accuracy is not source positional accuracy"}
    except GeometryError:
        raise
    except ImportError:
        raise GeometryError("PYPROJ_UNAVAILABLE") from None
    except Exception:
        raise GeometryError("CRS_TRANSFORM_FAILED") from None
    output = {"type": "LineString", "coordinates": converted[0]} if len(converted) == 1 else {
              "type": "MultiLineString", "coordinates": converted}
    return output, receipt


def intersects_bbox(geometry: dict, bbox: tuple[float, float, float, float]) -> bool:
    """Liang-Barsky segment/rectangle intersection; no approximate bbox-only join."""
    w, s, e, n = bbox
    paths = [geometry["coordinates"]] if geometry["type"] == "LineString" else geometry["coordinates"]
    for path in paths:
        for (x0, y0), (x1, y1) in zip(path, path[1:]):
            dx, dy = x1 - x0, y1 - y0
            lo, hi = 0.0, 1.0
            possible = True
            for p, q in ((-dx, x0 - w), (dx, e - x0), (-dy, y0 - s), (dy, n - y0)):
                if p == 0:
                    if q < 0:
                        possible = False
                        break
                elif p < 0:
                    lo = max(lo, q / p)
                else:
                    hi = min(hi, q / p)
            if possible and lo <= hi:
                return True
    return False


def geodesic_length_m(geometry: dict) -> float:
    from pyproj import Geod
    geod = Geod(ellps="WGS84")
    paths = [geometry["coordinates"]] if geometry["type"] == "LineString" else geometry["coordinates"]
    result = sum(abs(geod.line_length([p[0] for p in path], [p[1] for p in path])) for path in paths)
    require(math.isfinite(result), "LENGTH_NONFINITE")
    return result
