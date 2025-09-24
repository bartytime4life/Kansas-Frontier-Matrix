#!/usr/bin/env python3
import csv, subprocess, sys, pathlib

county = sys.argv[1]  # e.g., "pawnee"
tile_csv = pathlib.Path(f"data/sources/dem/tile_indexes/{county}_1m_tiles.csv")
raw_dir  = pathlib.Path(f"data/raw/lidar/{county}")
vrt_out  = pathlib.Path(f"data/sources/dem/processed/lidar/{county}/{county}_1m.vrt")
cog_out  = pathlib.Path(f"data/sources/dem/processed/lidar/{county}/{county}_1m_dem_cog.tif")

raw_dir.mkdir(parents=True, exist_ok=True)
vrt_out.parent.mkdir(parents=True, exist_ok=True)

urls = []
with open(tile_csv, newline="") as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        url = row.get("url", "").strip()
        if url:
            urls.append(url)

for url in urls:
    dest = raw_dir / pathlib.Path(url).name
    if not dest.exists():
        print(f"Downloading {url}")
        subprocess.check_call(["curl", "-fsSL", url, "-o", str(dest)])

tile_list = raw_dir.glob("*.tif")
tile_txt = pathlib.Path(f"/tmp/{county}_tiles.txt")
with open(tile_txt, "w") as f:
    for t in tile_list:
        f.write(str(t) + "\n")

print("Building VRT…")
subprocess.check_call([
    "gdalbuildvrt", "-r", "bilinear", "-input_file_list", str(tile_txt), str(vrt_out)
])

print("Translating to COG…")
subprocess.check_call([
    "gdal_translate", str(vrt_out), str(cog_out),
    "-of", "COG",
    "-co", "COMPRESS=DEFLATE",
    "-co", "BIGTIFF=YES",
    "-co", "NUM_THREADS=ALL_CPUS",
    "-co", "RESAMPLING=AVERAGE",
    "-co", "OVERVIEWS=IGNORE_EXISTING"
])

print("Updating registry (if available)…")
try:
    subprocess.check_call(["python", "scripts/update_registry.py", str(cog_out), f"ks_lidar_county_{county}"])
except Exception:
    print("registry update skipped.")
