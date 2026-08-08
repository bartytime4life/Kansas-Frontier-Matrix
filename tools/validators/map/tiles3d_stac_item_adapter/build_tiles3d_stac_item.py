#!/usr/bin/env python3
"""Build an unreleased STAC Item candidate from a 3D Tiles tree hash manifest."""
from __future__ import annotations
import argparse, hashlib, json, math, re, sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[4]
HASH_SRC=ROOT/"packages/hashing/src"
if str(HASH_SRC) not in sys.path: sys.path.insert(0,str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError:
    def compute_spec_hash(value: Any) -> str:
        raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode("utf-8")
        return "sha256:"+hashlib.sha256(raw).hexdigest()

REQUEST_SCHEMA=ROOT/"schemas/contracts/v1/map/tiles3d_stac_item_adapter_request.schema.json"
FIXTURES=ROOT/"fixtures/map/tiles3d_stac_item_adapter"
CASES=FIXTURES/"expected_findings_manifest.json"
MAX_JSON_BYTES=4*1024*1024
MAX_FILE_BYTES=64*1024*1024
SHA_RE=re.compile(r"^sha256:[a-f0-9]{64}$")
SCOPE="tiles3d-stac-candidate-adapter-only"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass
@dataclass(frozen=True,order=True)
class Finding:
    code:str
    field:str
@dataclass(frozen=True)
class Result:
    item:dict[str,Any] | None
    findings:tuple[Finding,...]
    @property
    def ok(self)->bool: return self.item is not None and not self.findings
    @property
    def outcome(self)->str: return "PASS" if self.ok else "ERROR"

def _unique(pairs:list[tuple[str,Any]])->dict[str,Any]:
    out={}
    for key,value in pairs:
        if key in out: raise DuplicateKeyError(key)
        out[key]=value
    return out

def _reject(_value:str)->None: raise NonFiniteNumberError
def _finite(value:str)->float:
    parsed=float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path:Path)->tuple[dict[str,Any]|None,list[Finding]]:
    try:
        if path.is_symlink(): return None,[Finding("INPUT_SYMLINK_DENIED","/")]
        if not path.is_file(): return None,[Finding("INPUT_NOT_FILE","/")]
        if path.stat().st_size>MAX_JSON_BYTES: return None,[Finding("INPUT_TOO_LARGE","/")]
        value=json.loads(path.read_text(encoding="utf-8"),object_pairs_hook=_unique,parse_constant=_reject,parse_float=_finite)
    except (UnicodeDecodeError,json.JSONDecodeError,DuplicateKeyError,NonFiniteNumberError):
        return None,[Finding("JSON_INVALID","/")]
    except OSError:
        return None,[Finding("INPUT_READ_ERROR","/")]
    if not isinstance(value,dict): return None,[Finding("ROOT_NOT_OBJECT","/")]
    return value,[]

def _schema(value:Mapping[str,Any])->list[Finding]:
    try:
        schema=json.loads(REQUEST_SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors=list(Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(value))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError,RecursionError):
        return [Finding("REQUEST_SCHEMA_UNAVAILABLE","/")]
    return [Finding("REQUEST_SCHEMA_INVALID","/"+"/".join(str(p) for p in error.absolute_path)) for error in errors]

def _manifest_findings(value:Mapping[str,Any])->list[Finding]:
    findings=[]
    if value.get("object_type")!="Tiles3DTreeHashManifest": findings.append(Finding("MANIFEST_TYPE_INVALID","/object_type"))
    if value.get("status")!="CANDIDATE_INTEGRITY_ONLY": findings.append(Finding("MANIFEST_STATUS_INVALID","/status"))
    declared=value.get("spec_hash")
    if not isinstance(declared,str) or declared!=compute_spec_hash({k:v for k,v in value.items() if k!="spec_hash"}):
        findings.append(Finding("MANIFEST_SPEC_HASH_MISMATCH","/spec_hash"))
    governance=value.get("governance")
    if not isinstance(governance,dict) or any(governance.get(name) is not False for name in ("source_activated","promotion_authorized","release_authorized","publication_authorized")):
        findings.append(Finding("MANIFEST_AUTHORITY_OVERREACH","/governance"))
    files=value.get("files")
    if not isinstance(files,list) or not files: return findings+[Finding("MANIFEST_FILES_INVALID","/files")]
    paths=[]
    for index,entry in enumerate(files):
        if not isinstance(entry,dict):
            findings.append(Finding("MANIFEST_FILE_INVALID",f"/files/{index}")); continue
        path=entry.get("path")
        try: pure=PurePosixPath(path)
        except TypeError: pure=None
        if pure is None or not isinstance(path,str) or path.startswith("/") or str(pure)!=path or any(part in {".",".."} for part in pure.parts):
            findings.append(Finding("MANIFEST_PATH_INVALID",f"/files/{index}/path"))
        paths.append(path)
        if not isinstance(entry.get("byte_size"),int) or not 0<=entry["byte_size"]<=MAX_FILE_BYTES:
            findings.append(Finding("MANIFEST_SIZE_INVALID",f"/files/{index}/byte_size"))
        if not isinstance(entry.get("sha256"),str) or not SHA_RE.fullmatch(entry["sha256"]):
            findings.append(Finding("MANIFEST_DIGEST_INVALID",f"/files/{index}/sha256"))
        if entry.get("role") not in {"tileset","subtree","content"}:
            findings.append(Finding("MANIFEST_ROLE_INVALID",f"/files/{index}/role"))
    if paths!=sorted(paths): findings.append(Finding("MANIFEST_FILES_NOT_CANONICAL","/files"))
    if len(paths)!=len(set(paths)): findings.append(Finding("MANIFEST_PATH_DUPLICATE","/files"))
    if paths.count(value.get("tileset_path"))!=1: findings.append(Finding("MANIFEST_TILESET_BINDING_INVALID","/tileset_path"))
    if value.get("file_count")!=len(files): findings.append(Finding("MANIFEST_FILE_COUNT_MISMATCH","/file_count"))
    if value.get("total_bytes")!=sum(entry.get("byte_size",0) for entry in files if isinstance(entry,dict)):
        findings.append(Finding("MANIFEST_TOTAL_BYTES_MISMATCH","/total_bytes"))
    if value.get("tree_hash")!=compute_spec_hash(files):
        findings.append(Finding("MANIFEST_TREE_HASH_MISMATCH","/tree_hash"))
    return findings

def _asset_key(index:int,role:str)->str:
    return f"{role}-{index:04d}"

def _verify_bytes(asset_root:Path,manifest:Mapping[str,Any])->list[Finding]:
    findings=[]
    try: root=asset_root.resolve(strict=True)
    except OSError: return [Finding("ASSET_ROOT_UNAVAILABLE","/")]
    if not root.is_dir() or asset_root.is_symlink(): return [Finding("ASSET_ROOT_INVALID","/")]
    for index,entry in enumerate(manifest.get("files",[])):
        if not isinstance(entry,dict) or not isinstance(entry.get("path"),str): continue
        path=PurePosixPath(entry["path"])
        candidate=root.joinpath(*path.parts)
        try:
            if candidate.is_symlink() or not candidate.is_file():
                findings.append(Finding("ASSET_MISSING",f"/files/{index}/path")); continue
            resolved=candidate.resolve(strict=True); resolved.relative_to(root)
            size=resolved.stat().st_size
            digest=hashlib.sha256(resolved.read_bytes()).hexdigest()
        except (OSError,ValueError):
            findings.append(Finding("ASSET_READ_ERROR",f"/files/{index}/path")); continue
        if size!=entry.get("byte_size"): findings.append(Finding("ASSET_SIZE_MISMATCH",f"/files/{index}/byte_size"))
        if "sha256:"+digest!=entry.get("sha256"): findings.append(Finding("ASSET_DIGEST_MISMATCH",f"/files/{index}/sha256"))
    return findings

def build(manifest_path:Path,request_path:Path,asset_root:Path)->Result:
    manifest,mf=_read(manifest_path); request,rf=_read(request_path)
    findings=mf+rf
    if manifest is None or request is None: return Result(None,tuple(sorted(set(findings))))
    findings.extend(_schema(request))
    if not findings: findings.extend(_manifest_findings(manifest))
    if not findings: findings.extend(_verify_bytes(asset_root,manifest))
    if findings: return Result(None,tuple(sorted(set(findings))))
    assets={}
    roles={"tileset":["metadata","3d-tiles"],"subtree":["data","3d-tiles","subtree"],"content":["data","3d-tiles","content"]}
    for index,entry in enumerate(manifest["files"]):
        assets[_asset_key(index,entry["role"])]={
            "href":entry["path"],"type":entry["media_type"],"title":entry["path"],
            "roles":roles[entry["role"]],"file:checksum":entry["sha256"],"file:size":entry["byte_size"],
            "kfm:path":entry["path"],"kfm:tree_hash":manifest["tree_hash"]
        }
    manifest_hex=manifest["tree_hash"].split(":",1)[1]
    item={
        "type":"Feature","stac_version":"1.0.0","stac_extensions":[],
        "id":request["item_id"],"collection":request["collection"],
        "geometry":request["geometry"],"bbox":request["bbox"],
        "properties":{
            "datetime":request["datetime"],"created":request["created"],"updated":request["updated"],
            "kfm:evidence_ref":request["evidence_ref"],"kfm:evidence_bundle":request["evidence_bundle_ref"],
            "kfm:run_receipt":request["run_receipt_ref"],"kfm:representation_receipt":request["representation_receipt_ref"],
            "kfm:source_role":request["source_role"],"kfm:rights_status":request["rights_status"],
            "kfm:sensitivity":request["sensitivity"],"kfm:review_state":"draft","kfm:release_state":"unreleased",
            "kfm:tree_hash":manifest["tree_hash"],"kfm:manifest_spec_hash":manifest["spec_hash"],
            "kfm:spec_hash":compute_spec_hash({"manifest_spec_hash":manifest["spec_hash"],"request":request})
        },
        "license":request["license"],"providers":request["providers"],
        "links":[
            {"rel":"derived_from","href":"urn:kfm:map:tiles3d-tree:"+manifest_hex},
            {"rel":"checksum","href":manifest["tree_hash"]},
            {"rel":"commit","href":"git:"+request["tree_commit"]},
            {"rel":"manifest_uri","href":"urn:kfm:manifest:tiles3d-tree:"+manifest["spec_hash"].split(":",1)[1]}
        ],
        "assets":assets
    }
    return Result(item,())

def run_fixtures()->int:
    try: cases=json.loads(CASES.read_text(encoding="utf-8"))["cases"]
    except (OSError,UnicodeError,json.JSONDecodeError,KeyError): return 1
    passed=True
    for case in cases:
        result=build(FIXTURES/case["manifest"],FIXTURES/case["request"],FIXTURES/case["asset_root"])
        codes=sorted({finding.code for finding in result.findings})
        match=result.outcome==case["expected_outcome"] and codes==case["expected_findings"]
        if match and case.get("expected_item"):
            expected=json.loads((FIXTURES/case["expected_item"]).read_text(encoding="utf-8"))
            match=result.item==expected
        print(json.dumps({"case_id":case["case_id"],"outcome":result.outcome,"findings":codes,"suite_match":match},sort_keys=True,separators=(",",":")))
        passed=passed and match
    return 0 if passed else 1

def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser(description="Build unreleased STAC Item candidates from 3D Tiles tree manifests.")
    parser.add_argument("--fixtures",action="store_true")
    parser.add_argument("manifest",nargs="?",type=Path); parser.add_argument("request",nargs="?",type=Path)
    parser.add_argument("--asset-root",type=Path); parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv)
    if args.fixtures:
        if args.manifest or args.request: parser.error("--fixtures cannot be combined with inputs")
        return run_fixtures()
    if not args.manifest or not args.request or not args.asset_root: parser.error("manifest, request, and --asset-root are required")
    result=build(args.manifest,args.request,args.asset_root)
    if result.ok:
        payload=json.dumps(result.item,sort_keys=True,indent=2)+"\n"
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(payload,encoding="utf-8")
        else: print(payload,end="")
    else:
        print(json.dumps({"outcome":"ERROR","findings":[{"code":f.code,"field":f.field} for f in result.findings],"scope":SCOPE},sort_keys=True,separators=(",",":")))
    return 0 if result.ok else 1

if __name__=="__main__": raise SystemExit(main())
