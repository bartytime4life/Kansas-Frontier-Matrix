#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from copy import deepcopy
from datetime import datetime, timezone
from typing import Any

SAFE_QUERY_TYPES={"taxa_in_geography","geographies_for_taxon","evidence_for_taxon_geography"}
UNSAFE_TO_REASON={"exact_coordinates":"exact_coordinates_requested","confirmed_presence":"confirmed_presence_requested"}
FORBIDDEN_FIELDS={"decimalLatitude","decimalLongitude","occurrenceLatitude","occurrenceLongitude","exact_coordinate","exactCoordinates","raw_occurrence_point"}
LIMITATIONS=[
    "GBIF occurrence aggregates are reported occurrence evidence, not confirmed species-presence determinations.",
    "Public output is generalized and does not expose exact occurrence coordinates.",
]

def canonicalize(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",",":"), ensure_ascii=False)

def with_spec_hash(obj: dict[str, Any], exclude: set[str] | None=None)->dict[str,Any]:
    out=deepcopy(obj); exclude=exclude or set(); exclude={*exclude,"created_at"}
    stable={k:v for k,v in out.items() if k not in exclude}
    out["kfm:spec_hash"]="sha256:"+hashlib.sha256(canonicalize(stable).encode()).hexdigest()
    return out

def now_iso()->str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

def _claim_hash(claim: dict[str,Any])->str:
    return "sha256:"+hashlib.sha256(canonicalize(claim).encode()).hexdigest()

def _match(claim,q):
    return (not q.get("taxon_key") or claim.get("taxon_key")==q.get("taxon_key")) and (not q.get("geography_id") or claim.get("geography_id")==q.get("geography_id"))

def build_answer(claims: list[dict[str,Any]], query: dict[str,Any]) -> tuple[dict[str,Any],dict[str,Any]]:
    created_at=now_iso()
    reason=None; matches=[]
    if query.get("query_type") in UNSAFE_TO_REASON:
        reason=UNSAFE_TO_REASON[query["query_type"]]
    elif query.get("query_type") not in SAFE_QUERY_TYPES:
        reason="invalid_query"
    else:
        for c in claims:
            if not _match(c,query):
                continue
            if c.get("rights_posture")!="public_allowed": reason="restricted_rights"; break
            if c.get("sensitivity_posture")=="restricted": reason="restricted_sensitivity"; break
            if c.get("presence_posture")!="reported_occurrence_not_confirmed_presence": reason="invalid_claim_input"; break
            if not c.get("citations"): reason="missing_citation"; break
            cit=c["citations"][0]
            if not cit.get("source_evidence_bundle_id"): reason="missing_evidence_reference"; break
            if not cit.get("download_key"): reason="missing_download_key"; break
            if not cit.get("geoprivacy_receipt_ref"): reason="missing_geoprivacy_receipt"; break
            if not cit.get("kfm:spec_hash") or not c.get("kfm:spec_hash"): reason="invalid_claim_input"; break
            matches.append(c)
        if not reason and not matches: reason="no_matching_cited_claim"

    if reason:
        answer={"answer_id":f"answer_{query['query_id']}","query_id":query["query_id"],"source_system":"GBIF","answer_posture":"abstain","summary":None,"claims":[],"ui_cards":[],"map_layers":[],"limitations":[],"abstain_reason":reason,"answer_receipt_ref":f"answer_receipt_{query['query_id']}","created_at":created_at}
    else:
        summary=f"GBIF-reported public occurrence aggregate evidence exists for {query.get('scientific_name','taxon')} in {query.get('geography_id','requested geography')}."
        answer_claims=[]
        for c in matches:
            answer_claims.append({k:c[k] for k in ["claim_id","claim_text","presence_posture","observation_count","record_count","date_range","citations"] if k in c})
        answer={"answer_id":f"answer_{query['query_id']}","query_id":query["query_id"],"source_system":"GBIF","answer_posture":"cited_answer","summary":summary,"claims":answer_claims,"ui_cards":[],"map_layers":[],"limitations":LIMITATIONS,"abstain_reason":None,"answer_receipt_ref":f"answer_receipt_{query['query_id']}","created_at":created_at}
    answer=with_spec_hash(answer,{"answer_id"})

    if answer["answer_posture"]=="cited_answer" and query.get("include_ui_cards"):
        from tools.runtime.fauna.kfm_gbif_ui_dto import build_ui_cards_and_layers
        cards,layers=build_ui_cards_and_layers(answer,query)
        answer["ui_cards"]=cards; answer["map_layers"]=layers
    answer=with_spec_hash(answer,{"answer_id"})

    receipt={"receipt_id":answer["answer_receipt_ref"],"query_id":query["query_id"],"answer_id":answer["answer_id"],"source_system":"GBIF","runtime_component":"kfm_gbif_answer_service","policy_version":"gbif_runtime_answer.v1","input_claim_count":len(claims),"matched_claim_count":len(matches),"citation_count":sum(len(c.get("citations",[])) for c in answer.get("claims",[])),"ui_card_count":len(answer.get("ui_cards",[])),"map_layer_count":len(answer.get("map_layers",[])),"redactions":["exact occurrence coordinates not emitted"],"abstain_reason":answer.get("abstain_reason"),"rights_posture_checked":True,"sensitivity_posture_checked":True,"geoprivacy_checked":True,"input_claim_hashes":sorted([_claim_hash(c) for c in claims]),"output_answer_hash":"sha256:"+hashlib.sha256(canonicalize({k:v for k,v in answer.items() if k!="created_at"}).encode()).hexdigest(),"created_at":created_at}
    receipt=with_spec_hash(receipt,{"receipt_id","answer_id"})
    return answer,receipt
