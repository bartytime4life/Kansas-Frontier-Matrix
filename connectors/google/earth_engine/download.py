"""Finite authenticated EE product capture. No admission or publication."""
from __future__ import annotations
import calendar
import hashlib
import json
import math
from datetime import date, timedelta, datetime, timezone
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener

MAX_BYTES = 500_000_000_000
MAX_CHUNK = 32 * 1024 * 1024
SPECS = {
    "ee-cdl": ("USDA/NASS/CDL", 2008, 2024, "classes"),
    "ee-dynamic-world": ("GOOGLE/DYNAMICWORLD/V1", 2015, 2025, "dynamic"),
    "ee-sentinel2": ("COPERNICUS/S2_SR_HARMONIZED", 2017, 2025, "rgb"),
    "ee-surface-water": ("JRC/GSW1_4/GlobalSurfaceWater", None, None, "water"),
    "ee-chirps": ("UCSB-CHG/CHIRPS/DAILY", 1981, 2025, "rain"),
    "ee-terraclimate": ("IDAHO_EPSCOR/TERRACLIMATE", 1958, 2024, "pdsi"),
    "ee-3dep": ("USGS/3DEP/10m_collection", None, None, "elevation"),
    "ee-prism-monthly": ("OREGONSTATE/PRISM/ANm", 1895, 2025, "rain"),
    "ee-prism-daily": ("OREGONSTATE/PRISM/ANd", 1981, 2025, "rain"),
    "ee-landsat-mss": ("LANDSAT/LM01/C02/T1", 1972, 1978, "inventory"),
    "ee-era5": ("ECMWF/ERA5/HOURLY", 1940, 2025, "inventory"),
    "ee-era5-land": ("ECMWF/ERA5_LAND/HOURLY", 1950, 2025, "inventory"),
    **{f"ee-landsat{m}": (f"LANDSAT/{c}/C02/T1_L2", a, b, "rgb") for m,c,a,b in
       [(4,"LT04",1982,1993),(5,"LT05",1984,2012),(7,"LE07",1999,2024),(8,"LC08",2013,2025),(9,"LC09",2021,2025)]},
}

def selection(value):
    if not isinstance(value,dict) or set(value)!={"dataset","year","maxBytes"}: raise ValueError("INVALID_SELECTION")
    if not isinstance(value["dataset"],str) or value["dataset"] not in SPECS: raise ValueError("UNKNOWN_DATASET")
    asset,first,last,kind = SPECS[value["dataset"]]
    year,limit = value["year"],value["maxBytes"]
    if (first is None and year is not None) or (first is not None and (type(year) is not int or not first<=year<=last)): raise ValueError("UNSUPPORTED_YEAR")
    if type(limit) is not int or not 1_048_576<=limit<=MAX_BYTES: raise ValueError("SELECT_DOWNLOAD_LIMIT")
    return {**value,"asset":asset,"kind":kind,"period":str(year) if year else "fixed"}

def expected_dates(dataset,year):
    if dataset not in {"ee-chirps","ee-terraclimate","ee-prism-monthly","ee-prism-daily"}: return None
    if dataset in {"ee-chirps","ee-prism-daily"}: return {(date(year,1,1)+timedelta(days=i)).strftime("%Y%m%d") for i in range(366 if calendar.isleap(year) else 365)}
    return {f"{year}{month:02}" for month in range(1,13)}

def grid(dataset):
    if dataset.startswith("ee-prism-"): return "EPSG:4269",[1/24,0,-125.0208333333335,0,-1/24,49.9375000000005]
    if dataset in {"ee-chirps","ee-terraclimate"}:
        step=.05 if dataset=="ee-chirps" else 1/24
        return "EPSG:4326",[step,0,-180,0,-step,50 if dataset=="ee-chirps" else 90]
    scale=10 if dataset=="ee-dynamic-world" else 30
    return "EPSG:5070",[scale,0,-1200000,0,-scale,2400000]

def tiles(bounds,transform,size=1024):
    left,bottom,right,top=bounds
    scale,_,ox,_,negative,oy=transform
    if not all(math.isfinite(x) for x in bounds) or left>=right or bottom>=top: raise ValueError("INVALID_PROVIDER_BOUNDS")
    x0,x1=math.floor((left-ox)/scale),math.ceil((right-ox)/scale)
    y0,y1=math.floor((top-oy)/negative),math.ceil((bottom-oy)/negative)
    if (x1-x0)*(y1-y0)>4_000_000_000: raise ValueError("GRID_LIMIT")
    result=[{"dimensions":[min(size,x1-x),min(size,y1-y)],"crs_transform":[scale,0,ox+x*scale,0,negative,oy+y*negative]} for y in range(y0,y1,size) for x in range(x0,x1,size)]
    if len(result)>4096: raise ValueError("TILE_LIMIT")
    return result

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs): raise ValueError("PROVIDER_REDIRECT_REJECTED")

def fetch_tile(url,maximum):
    parsed=urlsplit(url)
    if parsed.scheme!="https" or parsed.hostname!="earthengine.googleapis.com" or parsed.port not in (None,443) or parsed.username or parsed.password or not parsed.path.startswith("/v1/"): raise ValueError("DOWNLOAD_ORIGIN_REJECTED")
    with build_opener(ProxyHandler({}),NoRedirect).open(Request(url,headers={"User-Agent":"KFM-selected-EE-candidate/1"}),timeout=90) as response:
        length=response.headers.get("Content-Length")
        if response.status!=200: raise ValueError("PROVIDER_DOWNLOAD_FAILED")
        if length is not None and int(length)>maximum: raise ValueError("DOWNLOAD_BYTE_LIMIT")
        body=response.read(maximum+1)
    if len(body)>maximum: raise ValueError("DOWNLOAD_BYTE_LIMIT")
    if body[:4] not in (b"II*\x00",b"MM\x00*",b"II+\x00",b"MM\x00+"): raise ValueError("GEOTIFF_HEADER_INVALID")
    return body

def capture(request,ee,write,update,cancelled,transport=fetch_tile):
    if cancelled(): raise ValueError("CANCELLED")
    plan=selection(request)
    dataset,year,kind=plan["dataset"],plan["year"],plan["kind"]
    kansas=ee.FeatureCollection("TIGER/2018/States").filter(ee.Filter.eq("STATEFP","20")).geometry()
    meta=None
    if kind=="water":
        inventory=[{"id":plan["asset"]}]
        image=ee.Image(plan["asset"]).select("occurrence").toFloat()
    else:
        source=ee.ImageCollection(plan["asset"]).filterBounds(kansas).sort("system:index")
        if year is not None:
            if dataset.startswith("ee-prism-"):
                suffix="0101" if dataset.endswith("daily") else "01"
                source=source.filter(ee.Filter.gte("system:index",f"{year}{suffix}")).filter(ee.Filter.lt("system:index",f"{year+1}{suffix}"))
            else: source=source.filterDate(f"{year}-01-01",f"{year+1}-01-01")
        count=source.size().getInfo()
        if type(count) is not int or not 0<count<=20_000: raise ValueError("NO_DATA_OR_SOURCE_LIMIT")
        meta=ee.Dictionary({"ids":source.aggregate_array("system:id"),"times":source.aggregate_array("system:time_start"),"labels":source.aggregate_array("system:index")}).getInfo()
        ids=meta["ids"]
        if len(ids)!=count or len(set(ids))!=count or any(not isinstance(x,str) or not x.startswith(plan["asset"]+"/") for x in ids): raise ValueError("SOURCE_INVENTORY_INCOMPLETE")
        inventory=[{"id":v} for v in ids]
        expected=expected_dates(dataset,year)
        if expected is not None:
            labels=meta["labels"]
            if dataset=="ee-chirps": labels=[datetime.fromtimestamp(t/1000,timezone.utc).strftime("%Y%m%d") for t in meta["times"]]
            if len(labels)!=len(expected) or set(labels)!=expected: raise ValueError("SOURCE_PERIOD_INCOMPLETE")
        if kind=="classes":
            if count!=1: raise ValueError("ANNUAL_IMAGE_COUNT")
            image=ee.Image(source.first()).select("cropland").toFloat()
        elif kind=="rgb":
            def clean(scene):
                if dataset=="ee-sentinel2":
                    scl=scene.select("SCL")
                    return scene.select(["B4","B3","B2"]).multiply(.0001).updateMask(scl.eq(4).Or(scl.eq(5)).Or(scl.eq(6))).resample("bilinear")
                bands=["SR_B3","SR_B2","SR_B1"] if dataset[-1] in "457" else ["SR_B4","SR_B3","SR_B2"]
                mask=scene.select("QA_PIXEL").bitwiseAnd(63).eq(0).And(scene.select("QA_RADSAT").eq(0))
                return scene.select(bands).multiply(.0000275).add(-.2).updateMask(mask).resample("bilinear")
            clean_source=source.map(clean)
            image=clean_source.median().rename(["red","green","blue"]).addBands(clean_source.select(0).count().rename("retained_count")).toFloat()
        elif kind in {"rain","pdsi"}:
            band="precipitation" if dataset=="ee-chirps" else "pdsi" if kind=="pdsi" else "ppt"
            values=source.select(band)
            if dataset.startswith("ee-prism-"):
                native=ee.Image(source.first()).select(band).projection().getInfo()
                crs,transform=grid(dataset)
                if native["crs"]!=crs or len(native["transform"])!=6 or any(abs(a-b)>1e-10 for a,b in zip(native["transform"],transform)): raise ValueError("SOURCE_GRID_CHANGED")
            data=values.mean().multiply(.01) if kind=="pdsi" else values.sum()
            image=data.updateMask(values.count().eq(len(expected))).addBands(values.count().rename("retained_count")).toFloat()
        elif kind=="dynamic":
            names=["water","trees","grass","flooded_vegetation","crops","shrub_and_scrub","built","bare","snow_and_ice"]
            labels=source.map(lambda s:s.select("label").updateMask(s.select(names).reduce(ee.Reducer.max()).gte(.6)))
            image=labels.mode().addBands(labels.count().rename("retained_count")).toFloat()
        elif kind=="elevation": image=source.select("elevation").map(lambda s:s.resample("bilinear")).mosaic().toFloat()
        else: image=None
    metadata={"schema":"kfm-ee-capture/v1","selection":plan,"boundary":"TIGER/2018/States:20","source_inventory":inventory,"source_metadata":meta,"admission":"NOT_ADMITTED","review":"UNREVIEWED","map_ready":False,"provider_checksum":None,"product":"source inventory" if kind=="inventory" else "catalog recipe map product; not all original scenes"}
    metadata["processing"]={"version":1,"float32":True,"resampling":"bilinear for RGB and elevation; nearest for other products","summary":{"classes":"single annual cropland class","rgb":"QA-masked annual median, scaled reflectance; retained observation count","rain":"annual precipitation sum in mm; complete period required; retained count","pdsi":"annual mean PDSI multiplied by 0.01; complete period required; retained count","dynamic":"annual modal class after per-scene maximum class probability >=0.6; retained count","elevation":"system:index-sorted elevation mosaic, metres","water":"1984-2021 water occurrence, percent","inventory":"source IDs and timestamps only"}[kind]}
    if cancelled(): raise ValueError("CANCELLED")
    encoded=json.dumps(metadata,sort_keys=True).encode()
    if len(encoded)>8*1024*1024 or len(encoded)>plan["maxBytes"]: raise ValueError("METADATA_LIMIT")
    write("source-inventory.json",encoded)
    total=len(encoded)
    if image is None:
        update(state="downloaded",bytes=total,completed=1,total=1,mapReady=False)
        return metadata
    crs,transform=grid(dataset)
    coords=kansas.transform(crs,1).bounds(1,crs).coordinates().getInfo()[0]
    windows=tiles([min(p[0] for p in coords),min(p[1] for p in coords),max(p[0] for p in coords),max(p[1] for p in coords)],transform)
    bands=4 if kind=="rgb" else 2 if kind in {"rain","pdsi","dynamic"} else 1
    upper=sum(w["dimensions"][0]*w["dimensions"][1]*bands*4+65536 for w in windows)+total+8*1024*1024
    if upper>plan["maxBytes"]: raise ValueError("SELECTED_LIMIT_BELOW_GRID_ESTIMATE")
    update(state="downloading",bytes=total,completed=0,total=len(windows),estimatedBytes=upper)
    image=image.clip(kansas).unmask(-9999,False).toFloat()
    metadata.update(crs=crs,grid=transform,missing_value_sentinel=-9999,files=[])
    for i,window in enumerate(windows):
        if cancelled(): raise ValueError("CANCELLED")
        params={**window,"crs":crs,"format":"GEO_TIFF","filePerBand":False}
        body=transport(image.getDownloadURL(params),min(MAX_CHUNK,plan["maxBytes"]-total))
        if cancelled(): raise ValueError("CANCELLED")
        if len(body)>min(MAX_CHUNK,plan["maxBytes"]-total): raise ValueError("DOWNLOAD_BYTE_LIMIT")
        name=f"tile-{i:04}.tif"
        write(name,body)
        total+=len(body)
        metadata["files"].append({"name":name,"bytes":len(body),"sha256":hashlib.sha256(body).hexdigest(),**window})
        update(state="downloading",bytes=total,completed=i+1,total=len(windows))
    encoded=json.dumps(metadata,sort_keys=True).encode()
    if total+len(encoded)>plan["maxBytes"]: raise ValueError("DOWNLOAD_BYTE_LIMIT")
    write("capture.json",encoded)
    update(state="downloaded",bytes=total+len(encoded),mapReady=False)
    return metadata
