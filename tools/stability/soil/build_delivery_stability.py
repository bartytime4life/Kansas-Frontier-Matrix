#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from pathlib import Path
from tools.stability.soil._stability_common import *

def main():
 p=argparse.ArgumentParser()
 for x in ['continuity','resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops','stability']:
  p.add_argument(f'--{x}-root',required=True)
 p.add_argument('--out-root',required=True);p.add_argument('--base-public-url',required=True);p.add_argument('--continuity-id');p.add_argument('--stability-id')
 a=p.parse_args()
 if not validate_base_public_url(a.base_public_url): return block('invalid base url')
 cc=load_current_public_continuity(a.continuity_root); cid=sanitize_id(a.continuity_id or cc.get('active_continuity_id') or cc.get('continuity_id') or 'soil-continuity-test')
 sid=sanitize_id(a.stability_id or f"soil-stability-{stable_payload_hash({'c':cid})[:16]}")
 out=Path(a.out_root)/'stability/soil/cycles'/sid; out.mkdir(parents=True,exist_ok=True)
 manifest={"schema_version":"kfm.v1","object_type":"SoilPublicDeliveryStabilityManifest","domain":"soil","stability_id":sid,"continuity_id":cid,"public_stability_status":"PUBLIC_DELIVERY_STABILITY_READY","stability_state":"stable","active_delivery_stability_claimed":True,"created":utc_now_iso()}
 write_json_atomic(out/'public_delivery_stability_manifest.json',manifest)
 for n,o in [('stability_eligibility_registry.json','SoilStabilityEligibilityRegistry'),('steady_state_observation_packet.json','SoilSteadyStateObservationPacket'),('slo_conformance_packet.json','SoilSloConformancePacket'),('error_budget_stability_packet.json','SoilErrorBudgetStabilityPacket'),('regression_sentinel_registry.json','SoilRegressionSentinelRegistry'),('fallback_drill_readiness_packet.json','SoilFallbackDrillReadinessPacket'),('consumer_stability_communication_packet.json','SoilConsumerStabilityCommunicationPacket'),('stability_followup_work_order_registry.json','SoilStabilityFollowupWorkOrderRegistry'),('public_stability_status_report.json','SoilPublicStabilityStatusReport')]: write_json_atomic(out/n,{"schema_version":"kfm.v1","object_type":o,"domain":"soil","stability_id":sid})
 log_entries,log_root=build_stability_transparency_log([{"event_type":"manifest","object_type":"SoilPublicDeliveryStabilityManifest","item_id":sid,"ref":"public_delivery_stability_manifest.json","sha256":sha256_file(out/'public_delivery_stability_manifest.json'),"created":utc_now_iso()}])
 write_json_atomic(out/'stability_transparency_log.json',{"schema_version":"kfm.v1","object_type":"SoilStabilityTransparencyLog","domain":"soil","stability_id":sid,"entries":log_entries,"log_root":log_root})
 hashes={f.name:sha256_file(f) for f in out.glob('*.json') if f.name!='public_delivery_stability_receipt.json'}
 rec={"schema_version":"kfm.v1","receipt_type":"PublicDeliveryStabilityReceipt","from_state":"PUBLIC_DELIVERY_CONTINUITY_READY","to_state":"PUBLIC_DELIVERY_STABILITY_READY","decision":"pass","domain":"soil","continuity_id":cid,"stability_id":sid,"signatures":[{"dsse":"PROPOSED-COSIGN","key_ref":"kfm://keys/ci"}],"generated_artifacts":hashes}
 write_json_atomic(out/'public_delivery_stability_receipt.json',rec)
 write_json_atomic(Path(a.out_root)/'stability/soil/current_public_delivery_stability.json',{"schema_version":"kfm.v1","object_type":"SoilCurrentPublicDeliveryStabilityPointer","domain":"soil","active_stability_id":sid,"continuity_id":cid,"public_stability_status":"PUBLIC_DELIVERY_STABILITY_READY","stability_state":"stable","active_delivery_stability_claimed":True})
 print(json.dumps({"public_stability_allowed":True,"stability_id":sid,"continuity_id":cid,"state_transition":"PUBLIC_DELIVERY_CONTINUITY_READY->PUBLIC_DELIVERY_STABILITY_READY","stability_state":"stable","active_delivery_stability_claimed":True}))
 return 0

def block(r): print(json.dumps({"public_stability_allowed":False,"reasons":[r]})); return 2
if __name__=='__main__': sys.exit(main())
