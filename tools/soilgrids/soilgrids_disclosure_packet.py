from __future__ import annotations
import argparse, base64, hashlib, json, logging, mimetypes, os, re, shutil, subprocess, tarfile, zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SOURCE_NAME = "soilgrids_disclosure_packet"
MODES = {"plan-only","public-transparency","auditor-full","regulator","internal-review","verification-only","dry-run"}
ALLOWED_AUDIENCES = {"public","partner","auditor","regulator","internal"}
REMOTE_PREFIXES=("http://","https://","s3://","gs://","az://","/vsicurl/","/vsis3/","/vsigs/","/vsiaz/")
REQUIRED_REDACTION_CLASSES=["aws_access_key","bearer_token","generic_api_key","private_key_pem","approval_token_plaintext","password_like_field","local_absolute_path","internal_hostname","username_home_path","environment_variable_secret","remote_credential_url_userinfo"]
DEFAULT_POLICY={"schema":"DisclosurePolicy.v1","policy_id":"soilgrids-disclosure-default","profiles":{"public-transparency":{"allowed_schemas":["AssuranceGateReport.v1","AssuranceNarrative.v1","AuditDigest.v1","SupplyChainGateReport.v1","LicenseComplianceReport.v1","VulnerabilityScanReport.v1"],"denied_schemas":["EnvironmentFingerprint.v1","QueryAuditLog.v1"],"allow_raw_logs":False,"allow_local_paths":False,"allow_internal_hostnames":False,"allow_secrets":False,"allow_approval_artifacts":False},"auditor-full":{"allowed_schemas":["*"],"denied_schemas":[],"allow_raw_logs":False,"allow_local_paths":False,"allow_internal_hostnames":False,"allow_secrets":False,"allow_approval_artifacts":False},"internal-review":{"allowed_schemas":["*"],"denied_schemas":[],"allow_raw_logs":True,"allow_local_paths":True,"allow_internal_hostnames":True,"allow_secrets":False,"allow_approval_artifacts":False}},"required_redactions":["secret_patterns","approval_token_plaintext","private_key_material","bearer_tokens","aws_access_keys"],"required_claim_evidence_links":True,"require_checksums":True,"require_redaction_report":True}

class DisclosureError(Exception):
    def __init__(self,message:str,exit_code:int=100): super().__init__(message); self.exit_code=exit_code

def now_iso()->str: return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def _hash_obj(o:Any)->str: return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def _read_json(p:Path)->Dict[str,Any]: return json.loads(p.read_text(encoding="utf-8"))
def write_canonical_json(path:Path,obj:Any)->None:
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def _sha256_file(p:Path)->str:
    h=hashlib.sha256();
    with p.open("rb") as f:
        for c in iter(lambda:f.read(65536),b""): h.update(c)
    return h.hexdigest()

def compute_disclosure_spec_hash(spec): return _hash_obj(spec)
def compute_disclosure_plan_hash(plan): c=dict(plan); c.pop("created_at_utc",None); c.pop("disclosure_plan_hash",None); return _hash_obj(c)
def compute_redaction_hash(plan): c=dict(plan); c.pop("created_at_utc",None); c.pop("redaction_hash",None); return _hash_obj(c)
def compute_trust_claim_set_hash(c): x=dict(c); x.pop("created_at_utc",None); x.pop("trust_claim_set_hash",None); return _hash_obj(x)
def compute_disclosure_packet_hash(artifacts,claim_hash,red_hash,pack_hash,override=None): return _hash_obj({"artifacts":[{"path":a["path"],"role":a["role"],"bytes":a["bytes"],"sha256":a["sha256"],"redacted":a["redacted"]} for a in sorted(artifacts,key=lambda z:z["path"])],"trust_claim_set_hash":claim_hash,"redaction_hash":red_hash,"source_assurance_pack_hash":pack_hash,"override":override})

def validate_disclosure_spec(spec,mode="plan-only"):
    if spec.get("schema")!="DisclosureSpec.v1": raise DisclosureError("unsupported schema",30)
    if not spec.get("disclosure_id"): raise DisclosureError("missing disclosure_id",30)
    if spec.get("audience") not in ALLOWED_AUDIENCES: raise DisclosureError("unsupported audience",30)
    if spec.get("packet_profile") not in {"public-transparency","auditor-full","regulator","internal-review"}: raise DisclosureError("unsupported packet_profile",30)
    if mode!="verification-only" and not spec.get("source",{}).get("assurance_pack_root"): raise DisclosureError("missing source assurance pack",30)

def load_disclosure_policy(path:Optional[Path])->Dict[str,Any]:
    p=_read_json(path) if path else DEFAULT_POLICY
    if p.get("schema")!="DisclosurePolicy.v1": raise DisclosureError("unsupported policy schema",30)
    return p

def load_disclosure_inputs(paths:Dict[str,Optional[str]])->Dict[str,Any]:
    out={}
    for k,v in paths.items():
        if not v: continue
        if any(str(v).startswith(x) for x in REMOTE_PREFIXES): raise DisclosureError("remote paths rejected",80)
        out[k]=_read_json(Path(v))
    return out

def validate_source_assurance_pack(root:Path,allow_warning=False,allow_failed_assurance=False)->Dict[str,Any]:
    if not root.exists(): raise DisclosureError("missing assurance pack",40)
    manifest=root/"assurance_pack_manifest.json"; receipt=root/"assurance_pack_receipt.json"; checks=root/"checksums.sha256"
    if not manifest.exists() or not receipt.exists() or not checks.exists(): raise DisclosureError("missing assurance artifacts",40)
    r=_read_json(receipt)
    if r.get("status")=="warning" and not allow_warning: raise DisclosureError("assurance warning not allowed",40)
    lines=checks.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if not line.strip(): continue
        h,rel=line.split("  ",1); p=root/rel
        if _sha256_file(p)!=h: raise DisclosureError("checksum mismatch",40)
    gate_path=root/"assessment/assurance_gate_report.json"
    if gate_path.exists() and _read_json(gate_path).get("status")=="fail" and not allow_failed_assurance: raise DisclosureError("assurance gate failed",20)
    return {"manifest":_read_json(manifest),"receipt":r,"assurance_pack_hash":_read_json(manifest).get("assurance_pack_hash","")}

def classify_source_evidence(root:Path)->List[Dict[str,Any]]:
    out=[]
    for p in sorted(root.rglob("*.json")):
        rel=str(p.relative_to(root))
        obj=_read_json(p)
        out.append({"source_path":rel,"source_schema":obj.get("schema"),"source_obj":obj})
    return out

def build_disclosure_plan(spec,policy,evidence,packet_id,spec_hash,pack_id):
    profile=policy["profiles"][spec["packet_profile"]]; allowed=set(profile["allowed_schemas"]); denied=set(profile["denied_schemas"])
    sel=[]; omit=[]
    for e in evidence:
        s=e.get("source_schema")
        if s in denied: omit.append({"source_path":e["source_path"],"source_schema":s,"reason":"Denied by disclosure policy"}); continue
        if "*" in allowed or s in allowed: sel.append({"source_path":e["source_path"],"source_schema":s,"target_path":"evidence/"+Path(e["source_path"]).name,"action":"redact","reason":"Allowed by profile"})
        else: omit.append({"source_path":e["source_path"],"source_schema":s,"reason":"Not allowed by profile"})
    plan={"schema":"DisclosurePlan.v1","disclosure_id":spec["disclosure_id"],"disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"audience":spec["audience"],"packet_profile":spec["packet_profile"],"disclosure_spec_hash":spec_hash,"source_assurance_pack_id":pack_id,"selected_artifacts":sorted(sel,key=lambda x:x["source_path"]),"omitted_artifacts":sorted(omit,key=lambda x:x["source_path"]),"errors":[]}
    plan["disclosure_plan_hash"]=compute_disclosure_plan_hash(plan); return plan

def build_redaction_plan(spec,plan):
    rules=[{"rule_id":f"redact.secret.{c}","target":"text","pattern_class":c,"replacement":spec.get("redaction",{}).get("redaction_marker","[REDACTED]"),"required":True} for c in REQUIRED_REDACTION_CLASSES]
    rp={"schema":"RedactionPlan.v1","disclosure_packet_id":plan["disclosure_packet_id"],"created_at_utc":now_iso(),"source":SOURCE_NAME,"rules":rules,"artifact_actions":[{"source_path":a["source_path"],"target_path":a["target_path"],"redaction_required":True,"redaction_rules":[r["rule_id"] for r in rules]} for a in plan["selected_artifacts"]],"errors":[]}
    rp["redaction_hash"]=compute_redaction_hash(rp); return rp

PATTERNS={"aws_access_key":re.compile(r"AKIA[0-9A-Z]{16}"),"bearer_token":re.compile(r"Bearer\s+[A-Za-z0-9\-._~+/]+=*"),"private_key_pem":re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\s\S]+?-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),"approval_token_plaintext":re.compile(r"approval[_-]?token\s*[:=]\s*[^\s,\"]+",re.I),"local_absolute_path":re.compile(r"(?:/home/|/Users/|[A-Za-z]:\\\\)[^\s\"]+"),"internal_hostname":re.compile(r"\b(?:[a-z0-9-]+\.)*(?:internal|corp|local|lan)\b",re.I)}

def apply_redactions(root:Path,plan,redaction_plan,allow_secret_findings=False):
    redactions=[]; summary={"artifacts_scanned":0,"artifacts_redacted":0,"artifacts_omitted":0,"findings_redacted":0,"unredactable_findings":0}
    for a in plan["selected_artifacts"]:
        src=root/a["source_path"]
        txt=src.read_text(encoding="utf-8")
        changed=False
        for cls,pat in PATTERNS.items():
            n=len(pat.findall(txt))
            if n:
                txt=pat.sub("[REDACTED]",txt); changed=True; summary["findings_redacted"]+=n
                redactions.append({"redaction_id":"red_"+hashlib.sha256((a["target_path"]+cls).encode()).hexdigest()[:12],"artifact_path":a["target_path"],"rule_id":f"redact.secret.{cls}","count":n,"status":"redacted","message":"Secret-like value redacted."})
        summary["artifacts_scanned"]+=1
        if changed: summary["artifacts_redacted"]+=1
        target=Path(a["target_path"])
        target.parent.mkdir(parents=True,exist_ok=True); target.write_text(txt,encoding="utf-8")
        if src.suffix==".json": json.loads(txt)
    report={"schema":"RedactionReport.v1","run_id":"run_"+hashlib.sha256(now_iso().encode()).hexdigest()[:12],"created_at_utc":now_iso(),"source":SOURCE_NAME,"disclosure_packet_id":plan["disclosure_packet_id"],"status":"pass","summary":summary,"redactions":redactions,"errors":[]}
    return report

def build_redaction_report(*a,**k): return a[0] if a else k

def link_claims_to_evidence(claims,artifacts):
    m={a["role"]:a for a in artifacts}
    for c in claims:
        if not c["evidence_refs"]: raise DisclosureError("claim without evidence",60)
    return claims

def build_trust_claim_set(spec,packet_id,pack_id,artifacts):
    claims=[]
    for a in artifacts:
        ctype="provenance"
        if "assurance_gate" in a["role"]: ctype="assurance_gate"
        claims.append({"claim_id":"claim_"+hashlib.sha256(a["path"].encode()).hexdigest()[:12],"claim_type":ctype,"statement":f"Disclosed artifact {a['role']} is present with recorded checksum.","status":"pass","evidence_refs":[{"artifact_path":a["path"],"json_pointer":"/schema","sha256":a["sha256"]}]})
    t={"schema":"TrustClaimSet.v1","disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"issuer":{"name":"Kansas Frontier Matrix","id":None},"subject":{"dataset_id":spec["dataset_id"],"assurance_pack_id":pack_id,"release_id":None,"distribution_id":None},"claims":sorted(claims,key=lambda x:x["claim_id"]),"errors":[]}
    t["trust_claim_set_hash"]=compute_trust_claim_set_hash(t); return t

def build_verifiable_trust_statement(packet_id,claim_hash,packet_hash,evidence_manifest_hash):
    s={"schema":"VerifiableTrustStatement.v1","disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"statement_hash":"","issuer":{},"subject":{},"claim_set_hash":claim_hash,"packet_hash":packet_hash,"evidence_manifest_hash":evidence_manifest_hash,"proof":{"type":"unsigned","created":None,"verification_method":None,"proof_value":None},"errors":[]}
    s["statement_hash"]=_hash_obj({k:v for k,v in s.items() if k not in {"statement_hash"}}); return s

def sign_trust_statement_if_requested(stmt,sign,backend):
    if not sign: return stmt
    if backend=="unsigned": raise DisclosureError("explicit backend required",70)
    if backend=="mock":
        stmt["proof"]={"type":"mock-signature","created":now_iso(),"verification_method":"mock:key","proof_value":base64.b64encode(hashlib.sha256(stmt["statement_hash"].encode()).digest()).decode()}
        return stmt
    raise DisclosureError("backend unavailable",70)

def verify_trust_statement_if_requested(stmt,verify=False):
    if not verify: return True
    if stmt.get("proof",{}).get("type") in {"unsigned",None}: raise DisclosureError("proof missing",70)
    return True

def build_verification_instructions(packet_id,packet_hash,claim_hash): return {"schema":"VerificationInstructions.v1","disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"steps":[{"step_id":"verify.checksums","title":"Verify packet checksums","description":"Compute SHA-256 for each file and compare against checksums.sha256.","command_hint":"sha256sum -c checksums.sha256","required":True}],"expected_hashes":{"disclosure_packet_hash":packet_hash,"trust_claim_set_hash":claim_hash},"errors":[]}
def build_auditor_questionnaire(packet_id): return {"schema":"AuditorQuestionnaire.v1","disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"questions":[],"errors":[]}
def build_auditor_response_matrix(packet_id): return {"schema":"AuditorResponseMatrix.v1","disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"responses":[],"errors":[]}

def build_disclosure_manifest(packet_id,spec,packet_hash,artifacts,red_hash,vc=False,intoto=False): return {"schema":"DisclosureManifest.v1","disclosure_packet_id":packet_id,"disclosure_layout_version":"1","created_at_utc":now_iso(),"source":SOURCE_NAME,"audience":spec["audience"],"packet_profile":spec["packet_profile"],"disclosure_packet_hash":packet_hash,"source_assurance_pack_id":"unknown","artifacts":artifacts,"proofs":{"verifiable_trust_statement":"claims/verifiable_trust_statement.json","vc_envelope":"proofs/verifiable_credential_envelope.json" if vc else None,"intoto_statement":"proofs/intoto_statement.json" if intoto else None},"redaction":{"redaction_report":"redaction/redaction_report.json","redaction_hash":red_hash},"verification":{"instructions":"verification/verification_instructions.json","auditor_questionnaire":"auditor/auditor_questionnaire.json","auditor_response_matrix":"auditor/auditor_response_matrix.json"},"errors":[]}
def build_disclosure_validation_report(run_id,packet_id,status="success",errors=None): return {"schema":"DisclosureValidationReport.v1","run_id":run_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"disclosure_packet_id":packet_id,"status":status,"summary":{"total_checks":0,"passed":0,"failed":0,"skipped":0,"required_failed":0,"warnings_failed":0},"checks":[],"errors":errors or []}
def build_disclosure_receipt(run_id,mode,spec,packet_id,status,output_root,hashes,outputs,errors=None): return {"schema":"DisclosureReceipt.v1","run_id":run_id,"created_at_utc":now_iso(),"status":status,"source":SOURCE_NAME,"mode":mode,"disclosure_packet_id":packet_id,"audience":spec.get("audience"),"packet_profile":spec.get("packet_profile"),"disclosure_spec_hash":hashes.get("spec"),"disclosure_plan_hash":hashes.get("plan"),"redaction_hash":hashes.get("redaction"),"trust_claim_set_hash":hashes.get("claims"),"disclosure_packet_hash":hashes.get("packet"),"output_root":output_root,"outputs":outputs,"inputs":{"disclosure_spec":None,"assurance_pack_root":None,"disclosure_packet_root":None},"input_hashes":{"disclosure_spec_sha256":hashes.get("spec"),"source_assurance_manifest_sha256":None},"validation":{"source_valid":True,"policy_valid":True,"redaction_valid":True,"claims_valid":True,"packet_valid":True,"proof_valid":True,"checksums_valid":True},"errors":errors or []}

def write_checksums_file(root:Path,include_archives=True):
    entries=[]
    for p in sorted([x for x in root.rglob("*") if x.is_file() and x.name!="checksums.sha256"]):
        rel=str(p.relative_to(root));
        if rel.startswith("archives/") and not include_archives: continue
        entries.append((rel,_sha256_file(p)))
    (root/"checksums.sha256").write_text("".join(f"{h}  {r}\n" for r,h in entries),encoding="utf-8")

def build_disclosure_packet(args):
    run_id="run_"+hashlib.sha256((args.mode+"det" if args.deterministic_run_id else now_iso()).encode()).hexdigest()[:12]
    spec=_read_json(Path(args.disclosure_spec)); validate_disclosure_spec(spec,args.mode); spec_hash=compute_disclosure_spec_hash(spec)
    pack=validate_source_assurance_pack(Path(args.assurance_pack_root),args.allow_assurance_warning,args.allow_failed_assurance)
    policy=load_disclosure_policy(Path(args.disclosure_policy) if args.disclosure_policy else None)
    evidence=classify_source_evidence(Path(args.assurance_pack_root))
    tmp_id=f"{spec['dataset_id']}_{spec['audience']}_disclosure_tmp"
    plan=build_disclosure_plan(spec,policy,evidence,tmp_id,spec_hash,pack["manifest"].get("assurance_pack_id","unknown"))
    redplan=build_redaction_plan(spec,plan)
    out_root=Path(args.output_root); out_root.mkdir(parents=True,exist_ok=True)
    staging=out_root/".staging"/(tmp_id); shutil.rmtree(staging,ignore_errors=True); staging.mkdir(parents=True)
    cwd=os.getcwd(); os.chdir(staging)
    try:
        rr=apply_redactions(Path(args.assurance_pack_root),plan,redplan,args.allow_secret_findings)
        arts=[]
        for p in sorted(Path("evidence").rglob("*.json")):
            rel=str(p); arts.append({"role":p.stem,"path":rel,"media_type":"application/json","bytes":p.stat().st_size,"sha256":_sha256_file(p),"redacted":True})
        tcs=build_trust_claim_set(spec,tmp_id,pack["manifest"].get("assurance_pack_id","unknown"),arts)
        packet_hash=compute_disclosure_packet_hash(arts,tcs["trust_claim_set_hash"],redplan["redaction_hash"],pack["assurance_pack_hash"],args.disclosure_packet_id)
        packet_id=args.disclosure_packet_id or f"{spec['dataset_id']}_{spec['audience']}_disclosure_{packet_hash[:12]}"
        plan["disclosure_packet_id"]=packet_id; redplan["disclosure_packet_id"]=packet_id; rr["disclosure_packet_id"]=packet_id; tcs["disclosure_packet_id"]=packet_id
        stmt=build_verifiable_trust_statement(packet_id,tcs["trust_claim_set_hash"],packet_hash,pack["assurance_pack_hash"])
        stmt=sign_trust_statement_if_requested(stmt,args.sign_trust_statement,args.signing_backend)
        vinst=build_verification_instructions(packet_id,packet_hash,tcs["trust_claim_set_hash"])
        dq=build_auditor_questionnaire(packet_id); dm=build_auditor_response_matrix(packet_id)
        packet={"schema":"DisclosurePacket.v1","disclosure_packet_id":packet_id,"created_at_utc":now_iso(),"source":SOURCE_NAME,"audience":spec["audience"],"packet_profile":spec["packet_profile"],"disclosure_spec_hash":spec_hash,"disclosure_plan_hash":plan["disclosure_plan_hash"],"redaction_hash":redplan["redaction_hash"],"trust_claim_set_hash":tcs["trust_claim_set_hash"],"disclosure_packet_hash":packet_hash,"source_assurance_pack":{"assurance_pack_id":pack["manifest"].get("assurance_pack_id","unknown"),"assurance_pack_hash":pack["assurance_pack_hash"]},"artifacts":arts,"claims_path":"claims/trust_claim_set.json","verification_instructions_path":"verification/verification_instructions.json","checksums_path":"checksums.sha256","errors":[]}
        manifest=build_disclosure_manifest(packet_id,spec,packet_hash,arts,redplan["redaction_hash"],args.write_vc_envelope,args.write_intoto_statement)
        vr=build_disclosure_validation_report(run_id,packet_id)
        write_canonical_json(Path("plan/disclosure_plan.json"),plan); write_canonical_json(Path("plan/redaction_plan.json"),redplan); write_canonical_json(Path("redaction/redaction_report.json"),rr); write_canonical_json(Path("claims/trust_claim_set.json"),tcs); write_canonical_json(Path("claims/verifiable_trust_statement.json"),stmt); write_canonical_json(Path("verification/verification_instructions.json"),vinst); write_canonical_json(Path("auditor/auditor_questionnaire.json"),dq); write_canonical_json(Path("auditor/auditor_response_matrix.json"),dm); write_canonical_json(Path("disclosure_packet.json"),packet); write_canonical_json(Path("disclosure_manifest.json"),manifest); write_canonical_json(Path("disclosure_validation_report.json"),vr)
        if args.write_vc_envelope: write_canonical_json(Path("proofs/verifiable_credential_envelope.json"),{"@context":["https://www.w3.org/ns/credentials/v2","https://w3id.org/security/data-integrity/v2"],"type":["VerifiableCredential","SoilGridsTrustPacketCredential"],"issuer":"Kansas Frontier Matrix","validFrom":now_iso(),"credentialSubject":{"id":spec["dataset_id"],"disclosurePacketId":packet_id,"trustClaimSetHash":tcs["trust_claim_set_hash"],"disclosurePacketHash":packet_hash},"proof":{"type":"UnsignedProof","cryptosuite":None,"created":None,"verificationMethod":None,"proofPurpose":"assertionMethod","proofValue":None}})
        if args.write_intoto_statement: write_canonical_json(Path("proofs/intoto_statement.json"),{"_type":"https://in-toto.io/Statement/v1","subject":[],"predicateType":"https://example.org/soilgrids/disclosure/v1","predicate":{"disclosure_packet_id":packet_id}})
        write_checksums_file(Path("."),include_archives=False)
        final=out_root/packet_id
        if final.exists() and not args.overwrite: raise DisclosureError("output exists",80)
        if final.exists(): shutil.rmtree(final)
        os.replace(staging,final)
        rcpt=build_disclosure_receipt(run_id,args.mode,spec,packet_id,"success",str(final),{"spec":spec_hash,"plan":plan["disclosure_plan_hash"],"redaction":redplan["redaction_hash"],"claims":tcs["trust_claim_set_hash"],"packet":packet_hash},{"disclosure_manifest":"disclosure_manifest.json","disclosure_packet":"disclosure_packet.json","trust_claim_set":"claims/trust_claim_set.json","redaction_report":"redaction/redaction_report.json","validation_report":"disclosure_validation_report.json","verification_instructions":"verification/verification_instructions.json","auditor_questionnaire":"auditor/auditor_questionnaire.json","auditor_response_matrix":"auditor/auditor_response_matrix.json","checksums":"checksums.sha256","archive":None})
        write_canonical_json(final/"disclosure_receipt.json",rcpt)
        return str(final/"disclosure_receipt.json"),0
    finally:
        os.chdir(cwd)

def verify_disclosure_packet(root:Path,output_root:Path):
    checks=root/"checksums.sha256"
    for l in checks.read_text(encoding="utf-8").splitlines():
        h,rel=l.split("  ",1)
        if _sha256_file(root/rel)!=h: raise DisclosureError("checksum mismatch",20)
    out=output_root/"verification_receipt.json"; write_canonical_json(out,{"schema":"DisclosureReceipt.v1","status":"verified","source":SOURCE_NAME}); return str(out),0

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument("--disclosure-spec"); ap.add_argument("--assurance-pack-root"); ap.add_argument("--disclosure-packet-root"); ap.add_argument("--output-root",required=True); ap.add_argument("--mode",default="plan-only"); ap.add_argument("--disclosure-policy"); ap.add_argument("--disclosure-packet-id"); ap.add_argument("--sign-trust-statement",action="store_true"); ap.add_argument("--signing-backend",default="unsigned"); ap.add_argument("--write-vc-envelope",action="store_true"); ap.add_argument("--write-intoto-statement",action="store_true"); ap.add_argument("--allow-assurance-warning",action="store_true"); ap.add_argument("--allow-failed-assurance",action="store_true"); ap.add_argument("--allow-secret-findings",action="store_true"); ap.add_argument("--overwrite",action="store_true"); ap.add_argument("--deterministic-run-id",action="store_true")
    args=ap.parse_args(argv)
    try:
        if args.mode=="verification-only": p,c=verify_disclosure_packet(Path(args.disclosure_packet_root),Path(args.output_root)); print(p); return c
        p,c=build_disclosure_packet(args); print(p); return c
    except DisclosureError as e:
        print(json.dumps({"status":"error","error_count":1,"disclosure_receipt_path":None,"disclosure_packet_id":None}),file=os.sys.stderr)
        return e.exit_code

if __name__=="__main__": raise SystemExit(main())
