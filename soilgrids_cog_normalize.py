from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

MODULE_VERSION = "1.0.0"
REMOTE_PREFIXES = ("http://", "https://", "s3://", "gs://", "/vsicurl/", "/vsis3/", "/vsigs/")

try:
    from osgeo import gdal  # type: ignore
except Exception:
    gdal = None


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        data = {"level": record.levelname.lower(), "message": record.getMessage()}
        if isinstance(record.args, dict):
            data.update(record.args)
        if hasattr(record, "payload"):
            data.update(record.payload)
        return json.dumps(data, sort_keys=True)


def _logger() -> logging.Logger:
    logger = logging.getLogger("soilgrids_cog_normalize")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_creation_options(compression: str, predictor: int | str, blocksize: int | str, bigtiff: str, threads: int | str) -> dict[str, str]:
    opts = {
        "FORMAT": "COG",
        "COMPRESS": str(compression).upper(),
        "PREDICTOR": str(predictor),
        "BLOCKSIZE": str(blocksize),
        "BIGTIFF": str(bigtiff).upper(),
        "NUM_THREADS": str(threads),
    }
    return {k: opts[k] for k in sorted(opts)}


def compute_spec_hash(input_path: Path, input_sha256: str, creation_options: dict[str, str], source_spec_hash: str | None) -> str:
    payload = {
        "creation_options": {k: creation_options[k] for k in sorted(creation_options)},
        "input_path": str(input_path.resolve()),
        "input_sha256": input_sha256,
        "module_version": MODULE_VERSION,
        "source_receipt_spec_hash": source_spec_hash,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _parse_source_receipt(path: Path | None) -> dict[str, Any]:
    if not path:
        return {"path": None, "schema": None, "spec_hash": None}
    data = json.loads(path.read_text())
    return {"path": str(path), "schema": data.get("schema"), "spec_hash": data.get("spec_hash")}


def _translate_subprocess(input_path: Path, output_path: Path, creation_options: dict[str, str]) -> None:
    cmd = ["gdal_translate", str(input_path), str(output_path), "-of", "COG"]
    for k, v in creation_options.items():
        if k == "FORMAT":
            continue
        cmd.extend(["-co", f"{k}={v}"])
    subprocess.run(cmd, check=True, capture_output=True)


def _open_ds(path: Path):
    if gdal is None:
        raise RuntimeError("GDAL Python bindings unavailable")
    ds = gdal.Open(str(path))
    if ds is None:
        raise ValueError(f"cannot open raster: {path}")
    return ds


def _raster_semantics(ds: Any) -> dict[str, Any]:
    width, height, bands = ds.RasterXSize, ds.RasterYSize, ds.RasterCount
    gt = list(ds.GetGeoTransform() or [])
    proj = ds.GetProjectionRef() or ""
    band_types, nodata, checksums = [], [], []
    for i in range(1, bands + 1):
        b = ds.GetRasterBand(i)
        band_types.append(int(b.DataType))
        nodata.append(b.GetNoDataValue())
        checksums.append(int(b.Checksum()))
    return {
        "width": width,
        "height": height,
        "bands": bands,
        "geotransform": gt,
        "projection": proj,
        "band_types": band_types,
        "nodata": nodata,
        "checksums": checksums,
    }


def compute_semantic_raster_hash(sem: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(sem, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def normalize_to_cog(input_path: str | Path, output_dir: str | Path, source_receipt: str | Path | None = None,
                     compression: str = "DEFLATE", predictor: int = 2, blocksize: int = 512,
                     bigtiff: str = "IF_SAFER", threads: str | int = 1, overwrite: bool = False,
                     allow_non_epsg4326: bool = False, keep_temp: bool = False, receipt_dir: str | Path | None = None,
                     translate_runner: Callable[[Path, Path, dict[str, str]], None] | None = None) -> dict[str, Any]:
    run_id = hashlib.sha256(f"{Path(input_path)}|{datetime.now(timezone.utc).isoformat()}".encode()).hexdigest()[:16]
    logger = _logger()
    input_p, out_dir = Path(input_path), Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    receipt_out_dir = Path(receipt_dir) if receipt_dir else out_dir
    receipt_out_dir.mkdir(parents=True, exist_ok=True)
    receipt = {"schema": "CogReceipt.v1", "run_id": run_id, "created_at_utc": datetime.now(timezone.utc).isoformat(), "status": "error", "source": "soilgrids_cog_normalize", "errors": []}
    tmp_path = None
    try:
        logger.info("event", extra={"payload": {"event": "cog.normalize.started", "run_id": run_id, "input_path": str(input_p), "status": "started"}})
        if str(input_p).startswith(REMOTE_PREFIXES):
            raise ValueError("remote input paths are not allowed")
        if not input_p.exists() or input_p.is_dir():
            raise ValueError("input path missing or is directory")
        if input_p.stat().st_size == 0:
            raise ValueError("input file is empty")
        creation_options = canonical_creation_options(compression, predictor, blocksize, bigtiff, threads)
        src = _parse_source_receipt(Path(source_receipt)) if source_receipt else {"path": None, "schema": None, "spec_hash": None}
        in_sha = sha256_file(input_p)
        spec_hash = compute_spec_hash(input_p, in_sha, creation_options, src["spec_hash"])
        final_output = out_dir / f"{input_p.stem}_cog_{spec_hash[:12]}.tif"
        if final_output.exists() and not overwrite:
            raise FileExistsError("output exists and overwrite is false")
        ds = _open_ds(input_p)
        in_sem = _raster_semantics(ds)
        if in_sem["width"] <= 0 or in_sem["height"] <= 0 or in_sem["bands"] <= 0:
            raise ValueError("invalid raster dimensions/bands")
        if not in_sem["geotransform"]:
            raise ValueError("missing geotransform")
        if not in_sem["projection"]:
            raise ValueError("missing CRS")
        if ("4326" not in in_sem["projection"]) and not allow_non_epsg4326:
            raise ValueError("CRS is not EPSG:4326")
        logger.info("event", extra={"payload": {"event": "cog.input.validated", "run_id": run_id, "status": "ok", "spec_hash": spec_hash}})
        fd, tmp_name = tempfile.mkstemp(suffix=".tif", prefix=".tmp_cog_", dir=str(out_dir))
        os.close(fd)
        tmp_path = Path(tmp_name)
        runner = translate_runner
        if runner is None:
            if gdal is not None:
                def _runner(inp: Path, outp: Path, opts: dict[str, str]) -> None:
                    src_ds = _open_ds(inp)
                    co = [f"{k}={v}" for k, v in opts.items() if k != "FORMAT"]
                    res = gdal.Translate(str(outp), src_ds, format="COG", creationOptions=co)
                    if res is None:
                        raise RuntimeError("gdal.Translate failed")
                runner = _runner
            else:
                runner = _translate_subprocess
        logger.info("event", extra={"payload": {"event": "cog.translate.started", "run_id": run_id, "status": "started"}})
        runner(input_p, tmp_path, creation_options)
        logger.info("event", extra={"payload": {"event": "cog.translate.completed", "run_id": run_id, "status": "ok"}})
        out_ds = _open_ds(tmp_path)
        out_sem = _raster_semantics(out_ds)
        if (out_sem["width"], out_sem["height"], out_sem["bands"]) != (in_sem["width"], in_sem["height"], in_sem["bands"]):
            raise ValueError("output dimensions mismatch")
        if out_sem["projection"] != in_sem["projection"]:
            raise ValueError("output CRS mismatch")
        if any(abs(a - b) > 1e-12 for a, b in zip(out_sem["geotransform"], in_sem["geotransform"])):
            raise ValueError("output geotransform mismatch")
        meta = out_ds.GetMetadata("IMAGE_STRUCTURE") or {}
        if meta.get("LAYOUT") != "COG":
            drv = out_ds.GetDriver().ShortName
            if drv != "COG":
                raise ValueError("output is not recognizable COG layout")
        first_band = out_ds.GetRasterBand(1)
        if first_band.GetBlockSize()[0] <= 0:
            raise ValueError("output not tiled")
        ov_counts = [out_ds.GetRasterBand(i).GetOverviewCount() for i in range(1, out_ds.RasterCount + 1)]
        small = min(in_sem["width"], in_sem["height"]) < int(blocksize) * 2
        if not small and any(c == 0 for c in ov_counts):
            raise ValueError("missing overviews")
        shutil.move(str(tmp_path), str(final_output))
        tmp_path = None
        out_sha = sha256_file(final_output)
        receipt.update({"status": "success", "input_path": str(input_p.resolve()), "input_sha256": in_sha, "input_bytes": input_p.stat().st_size,
                        "output_path": str(final_output.resolve()), "output_sha256": out_sha, "output_bytes": final_output.stat().st_size,
                        "semantic_raster_hash": compute_semantic_raster_hash(out_sem), "spec_hash": spec_hash,
                        "creation_options": creation_options, "gdal": {"version": (gdal.VersionInfo() if gdal else "subprocess"), "driver": "COG"},
                        "raster": {"width": in_sem["width"], "height": in_sem["height"], "bands": in_sem["bands"], "crs": "EPSG:4326" if "4326" in in_sem["projection"] else in_sem["projection"], "geotransform": in_sem["geotransform"], "nodata": in_sem["nodata"]},
                        "source_receipt": src,
                        "validation": {"input_valid": True, "output_valid": True, "is_tiled": True, "overview_count_by_band": ov_counts,
                                       "dimension_match": True, "crs_match": True, "geotransform_match": True, "nodata_match": in_sem["nodata"] == out_sem["nodata"]}})
        logger.info("event", extra={"payload": {"event": "cog.output.validated", "run_id": run_id, "status": "ok", "output_path": str(final_output)}})
    except Exception as exc:
        receipt["errors"].append(str(exc))
        logger.error("event", extra={"payload": {"event": "cog.normalize.failed", "run_id": run_id, "status": "error", "error": str(exc)}})
        if tmp_path and tmp_path.exists() and not keep_temp:
            tmp_path.unlink()
    receipt_path = receipt_out_dir / f"cog_receipt_{run_id}.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True))
    logger.info("event", extra={"payload": {"event": "cog.receipt.written", "run_id": run_id, "status": receipt['status'], "receipt_path": str(receipt_path)}})
    return receipt


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--source-receipt")
    p.add_argument("--compression", default="DEFLATE")
    p.add_argument("--predictor", type=int, default=2)
    p.add_argument("--blocksize", type=int, default=512)
    p.add_argument("--bigtiff", default="IF_SAFER")
    p.add_argument("--threads", default="1")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--allow-non-epsg4326", action="store_true")
    p.add_argument("--keep-temp", action="store_true")
    p.add_argument("--receipt-dir")
    args = p.parse_args()
    receipt = normalize_to_cog(**vars(args))
    if receipt["status"] == "success":
        print(str((Path(args.receipt_dir) if args.receipt_dir else Path(args.output_dir)) / f"cog_receipt_{receipt['run_id']}.json"))
        return 0
    print(json.dumps(receipt), file=os.sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
