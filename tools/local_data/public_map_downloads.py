"""Explicit public-map originals in protected RAW storage; never map admission.

Only catalog asset identifiers are accepted. Transfers are bounded and opaque;
partial bytes remain available with an immutable receipt after cancellation.
"""
from __future__ import annotations

import copy
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import threading
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

from tools.local_data.acquisition import save_state, validate_root
from tools.local_data.candidate_capture import create_candidate
from tools.local_data.file_io import check_directory, fsync_directory, hash_regular, read_regular, write_new
from tools.local_data.manage import utc_now
from tools.local_data import public_map_catalog

MAX_BYTES = 500_000_000_000
MAX_CATALOG_BYTES = 32 * 1024 * 1024
RESERVE_BYTES = 64 * 1024 * 1024
CHUNK_BYTES = 1024 * 1024
ID = re.compile(r"[a-f0-9]{32}\Z")
SLUG = re.compile(r"[a-z0-9][a-z0-9._-]{0,127}\Z")
TERMINAL = {"downloaded", "failed", "cancelled", "interrupted"}
MAX_QUEUE = 300
PUBLIC_ENDPOINTS = {
    "www.kgs.ku.edu": ("/General/Geology/", "/Publications/"),
    "pubs.usgs.gov": ("/gq/", "/of/", "/sim/", "/imap/", "/i/", "/ds/", "/dr/"),
    "ngmdb.usgs.gov": ("/Prodesc/", "/GeMS/"),
    "mmr.osmre.gov": ("/images/",),
    "www.ncei.noaa.gov": ("/pub/data/swdi/stormevents/csvfiles/",),
}
# Verified ScienceBase attachments need an opaque, percent-encoded file token.
# Admit only these complete URLs, never arbitrary ScienceBase queries or paths.
SCIENCEBASE_FILES = {
    "https://www.sciencebase.gov/catalog/file/get/62ebd4dfd34eacf539724c47?f=__disk__13%2F9d%2F2b%2F139d2b1b15e331816a9cd156f2375e95ddf79579": "LimonQuadrangle_Shapefiles.zip",
    "https://www.sciencebase.gov/catalog/file/get/62ebd4dfd34eacf539724c47?f=__disk__9f%2F3f%2F82%2F9f3f8235d9df8d744c0cbcc87856d52199f812ef": "LimonQuadrangle_Geodatabase.zip",
    "https://www.sciencebase.gov/catalog/file/get/62ebe7ccd34eacf539724cca?f=__disk__98%2F90%2Fed%2F9890ed9fb556b9ab8f4a2e98ed75dc948f553d4c": "LamarCo_250k_GeMS.gdb.zip",
    "https://www.sciencebase.gov/catalog/file/get/62ebe7ccd34eacf539724cca?f=__disk__40%2F82%2F21%2F4082216b5addc27545bb8eabe98ab0ab19734295": "LamarCo_250k_GeMS-open.zip",
}
# These publisher endpoints stream the verified national archives directly.
# Names are local labels, except the observed Precambrian Content-Disposition.
NGMDB_FILES = {
    "https://ngmdb.usgs.gov/ngm-bin/gems_download.pl?id=4894&pid=118545": "CNGM_v2_Earth_Surface_GeMS.zip",
    "https://ngmdb.usgs.gov/ngm-bin/gems_download.pl?id=4893&pid=118545": "CNGM_v2_Quaternary_GeMS.zip",
    "https://ngmdb.usgs.gov/ngm-bin/gems_download.pl?id=4892&pid=118545": "CNGM_v2_PreQuaternary_GeMS.zip",
    "https://ngmdb.usgs.gov/ngm-bin/gems_download.pl?id=4891&pid=118545": "USGS_DR-1210_GeMS.4891.zip",
}
# Exact anonymous publisher files inspected on 2026-10-09; no URL templates accepted.
PUBLISHER_FILES = {'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1981.tif': 'chirps-v2.0.1981.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1982.tif': 'chirps-v2.0.1982.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1983.tif': 'chirps-v2.0.1983.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1984.tif': 'chirps-v2.0.1984.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1985.tif': 'chirps-v2.0.1985.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1986.tif': 'chirps-v2.0.1986.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1987.tif': 'chirps-v2.0.1987.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1988.tif': 'chirps-v2.0.1988.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1989.tif': 'chirps-v2.0.1989.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1990.tif': 'chirps-v2.0.1990.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1991.tif': 'chirps-v2.0.1991.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1992.tif': 'chirps-v2.0.1992.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1993.tif': 'chirps-v2.0.1993.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1994.tif': 'chirps-v2.0.1994.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1995.tif': 'chirps-v2.0.1995.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1996.tif': 'chirps-v2.0.1996.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1997.tif': 'chirps-v2.0.1997.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1998.tif': 'chirps-v2.0.1998.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.1999.tif': 'chirps-v2.0.1999.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2000.tif': 'chirps-v2.0.2000.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2001.tif': 'chirps-v2.0.2001.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2002.tif': 'chirps-v2.0.2002.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2003.tif': 'chirps-v2.0.2003.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2004.tif': 'chirps-v2.0.2004.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2005.tif': 'chirps-v2.0.2005.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2006.tif': 'chirps-v2.0.2006.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2007.tif': 'chirps-v2.0.2007.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2008.tif': 'chirps-v2.0.2008.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2009.tif': 'chirps-v2.0.2009.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2010.tif': 'chirps-v2.0.2010.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2011.tif': 'chirps-v2.0.2011.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2012.tif': 'chirps-v2.0.2012.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2013.tif': 'chirps-v2.0.2013.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2014.tif': 'chirps-v2.0.2014.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2015.tif': 'chirps-v2.0.2015.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2016.tif': 'chirps-v2.0.2016.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2017.tif': 'chirps-v2.0.2017.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2018.tif': 'chirps-v2.0.2018.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2019.tif': 'chirps-v2.0.2019.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2020.tif': 'chirps-v2.0.2020.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2021.tif': 'chirps-v2.0.2021.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2022.tif': 'chirps-v2.0.2022.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2023.tif': 'chirps-v2.0.2023.tif',
 'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_annual/tifs/chirps-v2.0.2024.tif': 'chirps-v2.0.2024.tif',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2008_30m_cdls.zip': '2008_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2009_30m_cdls.zip': '2009_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2010_30m_cdls.zip': '2010_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2011_30m_cdls.zip': '2011_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2012_30m_cdls.zip': '2012_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2013_30m_cdls.zip': '2013_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2014_30m_cdls.zip': '2014_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2015_30m_cdls.zip': '2015_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2016_30m_cdls.zip': '2016_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2017_30m_cdls.zip': '2017_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2018_30m_cdls.zip': '2018_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2019_30m_cdls.zip': '2019_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2020_30m_cdls.zip': '2020_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2021_30m_cdls.zip': '2021_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2022_30m_cdls.zip': '2022_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2023_30m_cdls.zip': '2023_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2024_10m_cdls.zip': '2024_10m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2024_30m_cdls.zip': '2024_30m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2025_10m_cdls.zip': '2025_10m_cdls.zip',
 'https://www.nass.usda.gov/Research_and_Science/Cropland/Release/datasets/2025_30m_cdls.zip': '2025_30m_cdls.zip'}
PINNED_FILES = {**SCIENCEBASE_FILES, **NGMDB_FILES, **PUBLISHER_FILES}


def validate_url(value):
    if isinstance(value, str) and value in PINNED_FILES:
        return value
    if (not isinstance(value, str) or len(value) > 2048 or "\\" in value or "%" in value
            or any(ord(c) <= 32 or ord(c) > 126 for c in value)):
        raise ValueError("ASSET_URL_NOT_ALLOWLISTED")
    parsed = urlsplit(value)
    if (parsed.scheme != "https" or parsed.username or parsed.password or parsed.port
            or parsed.query or parsed.fragment or parsed.hostname not in PUBLIC_ENDPOINTS
            or any(p in {".", ".."} for p in parsed.path.split("/"))
            or not any(parsed.path.startswith(p) for p in PUBLIC_ENDPOINTS[parsed.hostname])):
        raise ValueError("ASSET_URL_NOT_ALLOWLISTED")
    if parsed.hostname == "mmr.osmre.gov" and not re.fullmatch(r"/images/[0-9]{8,9}_web\.jpg", parsed.path):
        raise ValueError("ASSET_URL_NOT_ALLOWLISTED")
    # Storm Events names carry NCEI's reissue date, so they are discovered from its
    # listing; only that directory's exact bulk-CSV file pattern is admitted.
    if (parsed.hostname == "www.ncei.noaa.gov" and not
            public_map_catalog.STORM_EVENTS_FILE.fullmatch(parsed.path.removeprefix("/pub/data/swdi/stormevents/csvfiles/"))):
        raise ValueError("ASSET_URL_NOT_ALLOWLISTED")
    return value


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("ASSET_REDIRECT_DENIED")


def request_asset(url):
    validate_url(url)
    return build_opener(ProxyHandler({}), NoRedirect()).open(Request(url, headers={
        "User-Agent": "KFM-public-map-candidate/1", "Accept-Encoding": "identity",
    }), timeout=30)


def _magic(format_name, prefix):
    checks = {
        "pdf": lambda: prefix.startswith(b"%PDF-"),
        "jpeg": lambda: prefix.startswith(b"\xff\xd8\xff"),
        "geotiff": lambda: prefix[:4] in {b"II*\0", b"MM\0*", b"II+\0", b"MM\0+"},
        "zip": lambda: prefix[:4] in {b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08"},
        "gzip": lambda: prefix.startswith(b"\x1f\x8b\x08"),
    }
    format_name = {"TIFF": "geotiff", "PDF": "pdf", "JPEG": "jpeg", "ZIP": "zip", "GZIP": "gzip"}.get(format_name, format_name)
    if format_name not in checks or not checks[format_name]():
        raise ValueError("ASSET_FORMAT_MISMATCH")


@contextmanager
def durable_writer(fd):
    with os.fdopen(fd, "wb") as writer:
        try:
            yield writer
        finally:
            writer.flush()
            os.fsync(writer.fileno())


def _reason(error):
    value = str(error)
    return value if re.fullmatch(r"[A-Z][A-Z0-9_]{2,90}", value) else "PUBLIC_MAP_REQUEST_FAILED"


class PublicMapDownloads:
    def __init__(self, root):
        validate_root(root)
        self.root = root
        self.work = root / "data/work/public-map-downloads"
        self.raw = root / "data/raw/public-maps"
        self.receipts = root / "data/receipts/ingest/public-maps"
        for directory in (self.work / "jobs", self.raw, self.receipts):
            check_directory(directory, create=True)
        self.lock = threading.RLock()
        self.cancel_event = threading.Event()
        self.active = None
        self.queue = []
        self.worker = None
        self.refresh_worker = None
        self.refresh_state = {"state": "idle"}
        self.jobs = {}
        self._catalog = public_map_catalog.load_seed()
        snapshot = self.work / "catalog.json"
        if snapshot.exists() or snapshot.is_symlink():
            self._catalog = public_map_catalog.reconcile_seed(json.loads(read_regular(snapshot, MAX_CATALOG_BYTES)))
        files = list((self.work / "jobs").glob("*.json"))
        if len(files) > 1000:
            raise ValueError("JOB_HISTORY_LIMIT")
        for path in sorted(files):
            if not ID.fullmatch(path.stem):
                raise ValueError("INVALID_JOB_FILE")
            job = json.loads(read_regular(path, 64 * 1024))
            if job.get("id") != path.stem:
                raise ValueError("INVALID_JOB_FILE")
            self.jobs[path.stem] = job
            if job.get("state") not in TERMINAL:
                self.update(path.stem, state="interrupted", reason="WORKER_RESTARTED")
            # A process can stop after the terminal state is saved but before
            # its receipt is linked. Repair that gap even for terminal jobs.
            receipt = self.receipts / (path.stem + ".json")
            if receipt.exists() or receipt.is_symlink():
                read_regular(receipt, 128 * 1024)
            else:
                self._receipt(path.stem)

    def catalog(self):
        with self.lock:
            return copy.deepcopy(self._catalog)

    def health(self):
        with self.lock:
            # Queued jobs are a count, and the running job is always listed: cancelled
            # queue entries must not push it out of the window the site validates.
            jobs = [job for job in self.jobs.values() if job["id"] not in self.queue and job["id"] != self.active][-(99 if self.active else 100):]
            if self.active:
                jobs.append(self.jobs[self.active])
            return {"schema": "kfm-public-map-download-control/v1", "jobs": copy.deepcopy(jobs),
                    "active": self.active, "queued": len(self.queue), "limitBytes": MAX_BYTES, "refresh": dict(self.refresh_state)}

    def update(self, identifier, **fields):
        with self.lock:
            self.jobs[identifier].update(fields, updatedAt=utc_now())
            save_state(self.work / "jobs" / (identifier + ".json"), self.jobs[identifier])

    def _asset(self, identifier):
        found = [(record, asset) for record in self._catalog["records"] for asset in record.get("assets", [])
                 if asset.get("id") == identifier]
        if len(found) != 1:
            raise ValueError("UNKNOWN_OR_DUPLICATE_ASSET")
        record, asset = found[0]
        if asset.get("kind") != "download" or asset.get("availability") != "verified":
            raise ValueError("ASSET_NOT_VERIFIED_DOWNLOAD")
        if asset.get("format") not in {"PDF", "JPEG", "TIFF", "ZIP", "GZIP"}:
            raise ValueError("ASSET_FORMAT_UNSUPPORTED")
        validate_url(asset.get("url"))
        expected = asset.get("expectedBytes")
        if expected is not None and (type(expected) is not int or not 0 < expected <= MAX_BYTES):
            raise ValueError("ASSET_SIZE_INVALID")
        if not isinstance(record.get("id"), str) or not SLUG.fullmatch(record["id"]):
            raise ValueError("ASSET_IDENTIFIER_INVALID")
        return copy.deepcopy(record), copy.deepcopy(asset)

    def start(self, value):
        if (not isinstance(value, dict) or set(value) != {"requestId", "assetId", "maxBytes"}
                or not isinstance(value["requestId"], str) or not ID.fullmatch(value["requestId"])
                or not isinstance(value["assetId"], str) or not SLUG.fullmatch(value["assetId"])
                or type(value["maxBytes"]) is not int or not 0 < value["maxBytes"] <= MAX_BYTES):
            raise ValueError("INVALID_PUBLIC_MAP_REQUEST")
        identifier = value["requestId"]
        with self.lock:
            if identifier in self.jobs:
                prior = self.jobs[identifier]
                if prior["assetId"] != value["assetId"] or prior["maxBytes"] != value["maxBytes"]:
                    raise ValueError("REQUEST_ID_CONFLICT")
                return copy.deepcopy(prior)
            if self.active or self.queue:
                raise ValueError("DOWNLOAD_ALREADY_RUNNING")
            if len(self.jobs) >= 1000:
                raise ValueError("JOB_HISTORY_LIMIT")
            job = self._create(identifier, value["assetId"], value["maxBytes"])
            self._launch(identifier)
            return copy.deepcopy(job)

    def enqueue(self, value):
        """Queue verified files to download one after another under one maximum each.

        Every file is validated and pinned before any transfer starts. Queued jobs
        are reported as a count; after a worker restart they become interrupted.
        """
        if (not isinstance(value, dict) or set(value) != {"requestId", "assetIds", "maxBytes"}
                or not isinstance(value["requestId"], str) or not ID.fullmatch(value["requestId"])
                or not isinstance(value["assetIds"], list) or not 0 < len(value["assetIds"]) <= MAX_QUEUE
                or not all(isinstance(item, str) and SLUG.fullmatch(item) for item in value["assetIds"])
                or len(set(value["assetIds"])) != len(value["assetIds"])
                or type(value["maxBytes"]) is not int or not 0 < value["maxBytes"] <= MAX_BYTES):
            raise ValueError("INVALID_PUBLIC_MAP_QUEUE")
        batch = value["requestId"]
        identifiers = [hashlib.sha256(f"{batch}:{asset}".encode()).hexdigest()[:32] for asset in value["assetIds"]]
        with self.lock:
            # A request ID names one exact, ordered selection under one maximum.
            # Jobs reload in file-name order after a restart, so order by the stored position.
            prior = sorted((job for job in self.jobs.values() if job.get("batchId") == batch), key=lambda job: job.get("batchIndex", -1))
            if prior or any(identifier in self.jobs for identifier in identifiers):
                if ([job["id"] for job in prior] != identifiers
                        or any(job["maxBytes"] != value["maxBytes"] for job in prior)):
                    raise ValueError("REQUEST_ID_CONFLICT")
                return self._queue_summary(batch)
            if self.active or self.queue:
                raise ValueError("DOWNLOAD_ALREADY_RUNNING")
            if len(self.jobs) + len(identifiers) > 1000:
                raise ValueError("JOB_HISTORY_LIMIT")
            # Validate the whole selection before creating any job. Completed files stay
            # stored, so the queue reserves room for every file's upper bound at once.
            reserved = 0
            for asset_id in value["assetIds"]:
                expected = self._asset(asset_id)[1].get("expectedBytes")
                if expected is not None and expected > value["maxBytes"]:
                    raise ValueError("ASSET_EXCEEDS_SELECTED_LIMIT")
                reserved += expected or value["maxBytes"]
            if shutil.disk_usage(self.root).free < reserved + RESERVE_BYTES:
                raise ValueError("INSUFFICIENT_FREE_SPACE_FOR_LIMIT")
            try:
                for index, (identifier, asset_id) in enumerate(zip(identifiers, value["assetIds"])):
                    self._create(identifier, asset_id, value["maxBytes"], batch=(batch, index))
                    self.queue.append(identifier)
                self._launch(self.queue.pop(0))
            except Exception:
                # Never leave a queue with nothing running: fail what was queued.
                for identifier in self.queue:
                    self.update(identifier, state="failed", reason="PUBLIC_MAP_START_FAILED")
                    try:
                        self._receipt(identifier)
                    except Exception:
                        self.update(identifier, state="failed", reason="RECEIPT_WRITE_FAILED")
                self.queue.clear()
                raise ValueError("PUBLIC_MAP_START_FAILED") from None
            return self._queue_summary(batch)

    def cancel_queue(self):
        """Cancel every queued file and the running one; captured bytes stay for inspection."""
        with self.lock:
            cancelled = list(self.queue)
            self.queue.clear()
            for identifier in cancelled:
                self.update(identifier, state="cancelled", reason="CANCELLED")
                self._receipt(identifier)
            if self.active:
                self.cancel_event.set()
            return {"cancelledQueued": len(cancelled), "cancelling": self.active}

    def _queue_summary(self, batch):
        jobs = [job for job in self.jobs.values() if job.get("batchId") == batch]
        return {"batchId": batch, "jobs": len(jobs), "queued": sum(job["id"] in self.queue for job in jobs),
                "active": self.active, "mapReady": False}

    def _create(self, identifier, asset_id, maximum, batch=None):
        record, asset = self._asset(asset_id)
        expected = asset.get("expectedBytes")
        if expected is not None and expected > maximum:
            raise ValueError("ASSET_EXCEEDS_SELECTED_LIMIT")
        if shutil.disk_usage(self.root).free < (expected or maximum) + RESERVE_BYTES:
            raise ValueError("INSUFFICIENT_FREE_SPACE_FOR_LIMIT")
        parent = self.raw / record["id"]
        check_directory(parent, create=True)
        destination = parent / identifier
        create_candidate(destination)
        now = utc_now()
        # A record with several files (a Storm Events year) names the file, so jobs stay distinguishable.
        files = [item for item in record.get("assets", []) if item.get("kind") == "download" and item.get("availability") == "verified"]
        title = record["title"] if len(files) < 2 else f'{record["title"]} · {asset["title"]}'
        job = {"id": identifier, "assetId": asset_id, "title": title, "state": "queued",
               "bytes": 0, "expectedBytes": expected, "maxBytes": maximum, "sha256": None,
               "destination": str(destination), "mapReady": False, "createdAt": now, "updatedAt": now}
        if batch is not None:
            job["batchId"], job["batchIndex"] = batch
        self.jobs[identifier] = job
        try:
            save_state(self.work / "jobs" / (identifier + ".json"), job)
            # Pin identity independently of later catalog refreshes.
            write_new(destination / "source.json", json.dumps({"record": record, "asset": asset}, sort_keys=True).encode())
        except Exception:
            self._start_failed(identifier)
        return job

    def _launch(self, identifier):
        try:
            self.active = identifier
            self.cancel_event.clear()
            self.worker = threading.Thread(target=self.run, args=(identifier,), daemon=True)
            self.worker.start()
        except Exception:
            self.active = None
            self.worker = None
            self._start_failed(identifier)

    def _start_failed(self, identifier):
        self.update(identifier, state="failed", reason="PUBLIC_MAP_START_FAILED")
        try:
            self._receipt(identifier)
        except Exception:
            self.update(identifier, state="failed", reason="RECEIPT_WRITE_FAILED")
        raise ValueError("PUBLIC_MAP_START_FAILED") from None

    def _destination(self, job):
        directory = Path(job["destination"])
        if (not directory.is_absolute() or directory.parent.parent != self.raw
                or directory.name != job["id"] or not SLUG.fullmatch(directory.parent.name)):
            raise ValueError("JOB_DESTINATION_INVALID")
        check_directory(directory)
        return directory

    def _receipt(self, identifier):
        receipt_path = self.receipts / (identifier + ".json")
        if receipt_path.exists() or receipt_path.is_symlink():
            read_regular(receipt_path, 128 * 1024)
            return
        job = self.jobs[identifier]
        destination = self._destination(job)
        source_path = destination / "source.json"
        provider_checksum = None
        if source_path.exists() or source_path.is_symlink():
            pinned = json.loads(read_regular(source_path, 1024 * 1024))
            provider_checksum = pinned["asset"].get("providerChecksum")
        original_digest = job.get("sha256")
        files = []
        for path in sorted(destination.iterdir()):
            if path.name == "source.json":
                continue
            digest, count = hash_regular(path, job["maxBytes"])
            files.append({"name": path.name, "bytes": count, "sha256": digest})
        if job["state"] == "downloaded" and (len(files) != 1 or files[0]["name"].endswith(".part")
                or files[0]["sha256"] != original_digest or files[0]["bytes"] != job["bytes"]):
            self.update(identifier, state="failed", reason="STORED_BYTES_CHANGED")
        if files:
            self.update(identifier, bytes=files[0]["bytes"], sha256=files[0]["sha256"])
        for captured in files:
            captured["complete"] = job["state"] == "downloaded"
        receipt = {"schema": "kfm-public-map-download-receipt/v1", "job": copy.deepcopy(job), "files": files,
                   "review": "UNREVIEWED", "admission": "NOT_ADMITTED", "release": "NOT_RELEASED",
                   "providerChecksum": provider_checksum,
                   "providerChecksumVerified": False, "captureIntegrity": "sha256 and stored-byte readback",
                   "previousStoredSha256": original_digest}
        write_new(receipt_path, json.dumps(receipt, sort_keys=True).encode())

    def run(self, identifier):
        part = None
        try:
            job = self.jobs[identifier]
            destination = self._destination(job)
            source = json.loads(read_regular(destination / "source.json", 1024 * 1024))
            asset = source["asset"]
            validate_url(asset["url"])
            filename = PINNED_FILES.get(asset["url"], Path(urlsplit(asset["url"]).path).name)
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,180}", filename):
                raise ValueError("ASSET_FILENAME_INVALID")
            final = destination / filename
            part = destination / (filename + ".part")
            if self.cancel_event.is_set():
                raise ValueError("CANCELLED")
            self.update(identifier, state="downloading")
            with request_asset(asset["url"]) as response:
                if response.status != 200:
                    raise ValueError("ASSET_HTTP_STATUS_REJECTED")
                if response.geturl() != asset["url"]:
                    raise ValueError("ASSET_REDIRECT_DENIED")
                if response.headers.get("Content-Encoding", "identity").lower() != "identity":
                    raise ValueError("ASSET_CONTENT_ENCODING_REJECTED")
                length = response.headers.get("Content-Length")
                declared = None
                if length is not None:
                    if not re.fullmatch(r"[0-9]{1,15}", length):
                        raise ValueError("ASSET_CONTENT_LENGTH_INVALID")
                    declared = int(length)
                    if declared < 1 or declared > job["maxBytes"]:
                        raise ValueError("ASSET_EXCEEDS_SELECTED_LIMIT")
                    if job["expectedBytes"] is not None and declared != job["expectedBytes"]:
                        raise ValueError("ASSET_SIZE_CHANGED")
                fd = os.open(part, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o600)
                total = 0
                streamed = hashlib.sha256()
                with durable_writer(fd) as writer:
                    prefix = b""
                    while True:
                        if self.cancel_event.is_set():
                            raise ValueError("CANCELLED")
                        chunk = response.read(min(CHUNK_BYTES, job["maxBytes"] - total + 1))
                        if not chunk:
                            break
                        if total + len(chunk) > job["maxBytes"]:
                            raise ValueError("ASSET_EXCEEDS_SELECTED_LIMIT")
                        if shutil.disk_usage(self.root).free < len(chunk) + RESERVE_BYTES:
                            raise ValueError("DISK_SPACE_LOW")
                        prefix = (prefix + chunk)[:8]
                        if len(prefix) >= 8 or total + len(chunk) >= (declared or job["maxBytes"]):
                            _magic(asset["format"], prefix)
                        writer.write(chunk)
                        streamed.update(chunk)
                        total += len(chunk)
                        self.update(identifier, bytes=total)
                    _magic(asset["format"], prefix)
                    if (declared is not None and total != declared) or (job["expectedBytes"] is not None and total != job["expectedBytes"]):
                        raise ValueError("ASSET_TRUNCATED_OR_SIZE_CHANGED")
                if self.cancel_event.is_set():
                    raise ValueError("CANCELLED")
                digest, count = hash_regular(part, job["maxBytes"], expected_size=total)
                if digest != streamed.hexdigest():
                    raise ValueError("STORED_BYTES_CHANGED")
                os.link(part, final)
                part.unlink()
                fsync_directory(destination)
                self.update(identifier, state="downloaded", bytes=count, sha256=digest)
        except Exception as error:
            code = _reason(error)
            self.update(identifier, state="cancelled" if code == "CANCELLED" else "failed", reason=code)
        finally:
            try:
                self._receipt(identifier)
            except Exception:
                self.update(identifier, state="failed", reason="RECEIPT_WRITE_FAILED")
            finally:
                with self.lock:
                    self._advance()

    def _advance(self):
        """Hand the transfer slot straight to the next queued job, never leaving an idle gap."""
        while self.queue:
            try:
                self._launch(self.queue.pop(0))
                return
            except ValueError:
                continue
        self.active = None

    def cancel(self, identifier):
        with self.lock:
            if identifier != self.active:
                raise ValueError("NO_ACTIVE_DOWNLOAD")
            self.cancel_event.set()
            return {"cancelling": identifier}

    def refresh(self):
        with self.lock:
            if self.refresh_state["state"] == "running":
                return dict(self.refresh_state)
            self.refresh_state = {"state": "running"}
            self.refresh_worker = threading.Thread(target=self._refresh, daemon=True)
            self.refresh_worker.start()
            return dict(self.refresh_state)

    def _refresh(self):
        try:
            result = public_map_catalog.discover_catalog(existing=self.catalog())
            body = json.dumps(result, sort_keys=True).encode()
            if len(body) > MAX_CATALOG_BYTES:
                raise ValueError("CATALOG_BYTE_LIMIT")
            with self.lock:
                # Catalogs may exceed the smaller per-job state metadata limit.
                snapshot = self.work / "catalog.json"
                if snapshot.exists() or snapshot.is_symlink():
                    read_regular(snapshot, MAX_CATALOG_BYTES)
                temporary = self.work / ("catalog-" + os.urandom(16).hex() + ".json")
                write_new(temporary, body)
                os.replace(temporary, snapshot)
                fsync_directory(self.work)
                self._catalog = result
                self.refresh_state = {"state": "complete"}
        except Exception as error:
            with self.lock:
                self.refresh_state = {"state": "failed", "reason": _reason(error)}

    def close(self):
        """Request transfer cancellation without deleting protected originals."""
        with self.lock:
            self.queue.clear()
        self.cancel_event.set()
