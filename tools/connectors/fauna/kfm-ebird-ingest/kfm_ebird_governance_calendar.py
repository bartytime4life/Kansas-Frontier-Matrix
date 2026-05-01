#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
VERSION="0.31.0"

def fail(m:str)->None: print(f"ERROR: {m}", file=sys.stderr); raise SystemExit(2)
def canon(o:Any)->str: return json.dumps(o, sort_keys=True, separators=(",",":"))
def sha(s:str)->str: return hashlib.sha256(s.encode()).hexdigest()

def parse(argv:list[str])->argparse.Namespace:
 p=argparse.ArgumentParser(prog="kfm-ebird-governance-calendar")
 p.add_argument("--version",action="version",version=VERSION)
 p.add_argument("--mode",default="build",choices=["plan","build","validate","diff","report"])
 p.add_argument("--aggregate",default="both",choices=["huc12","county","both"])
 p.add_argument("--cadence",default="quarterly",choices=["monthly","quarterly","annual","ad-hoc"])
 p.add_argument("--start-date"); p.add_argument("--end-date")
 for a in ["transparency_report","public_transparency_report","public_ecosystem_status","public_advisory_index","consumer_renewal_schedule","public_consumer_registry_index","public_consumer_status_summary","recertification_receipt","assurance_scan_report","quality_scan_report","release_receipt","root_of_trust","gate_decision","previous_calendar_manifest"]: p.add_argument(f"--{a.replace('_','-')}")
 p.add_argument("--out-dir"); p.add_argument("--public-out-dir"); p.add_argument("--dry-run",action="store_true"); p.add_argument("--force",action="store_true")
 return p.parse_args(argv)

def make_ics(cid:str, events:list[dict[str,Any]])->str:
 lines=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//KFM//eBird Governance Calendar//EN"]
 for e in events:
  uid=sha(f"{cid}:{e['event_id']}")[:24]
  dt=e['start_date'].replace("-","")
  lines += ["BEGIN:VEVENT",f"UID:{uid}",f"DTSTART;VALUE=DATE:{dt}",f"SUMMARY:{e['title']}",f"DESCRIPTION:{e['summary']}","END:VEVENT"]
 lines.append("END:VCALENDAR")
 return "\n".join(lines)+"\n"

def main()->None:
 a=parse(sys.argv[1:])
 if a.start_date and a.end_date and date.fromisoformat(a.start_date)>date.fromisoformat(a.end_date): fail("start-date must be <= end-date")
 obj={"aggregate_targets":a.aggregate,"cadence":a.cadence,"start_date":a.start_date,"end_date":a.end_date,"adapter_version":VERSION}
 cid=sha(canon(obj))[:16]
 out=Path(a.out_dir or f"data/catalog/fauna/ebird/governance-calendar/{cid}")
 pout=Path(a.public_out_dir) if a.public_out_dir else None
 if out.exists() and not a.force: fail("out-dir exists; pass --force")
 events=[{"event_id":"release_review","event_type":"release_review","title":"Release Governance Review","summary":"Public-safe governance review only; exact points remain restricted.","start_date":a.start_date or "2026-01-01","status":"scheduled","public_required_action":"Run local validation."}]
 plan={"schema_version":"v1","object_type":"KfmEbirdGovernanceCalendarPlan","calendar_id":cid,"aggregate_targets":a.aggregate,"cadence":a.cadence,"planned_event_types":["release_review"],"prohibited_event_content":["exact_coordinates","restricted_paths","suppression_receipts","suppressed_group_hashes","raw_rows","private_contact_details","secrets"],"exact_points":"restricted"}
 pub={"schema_version":"v1","object_type":"PublicKfmEbirdGovernanceCalendar","public_safe":True,"exact_points":"restricted","calendar_id":cid,"aggregate_targets":a.aggregate,"cadence":a.cadence,"events":events,"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"no_restricted_observations_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True}}
 if a.dry_run: print(json.dumps({"calendar_id":cid,"events":len(events)},indent=2)); return
 out.mkdir(parents=True, exist_ok=True)
 (out/"governance_calendar_plan.json").write_text(json.dumps(plan,indent=2)+"\n")
 (out/"governance_calendar.json").write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdGovernanceCalendar","calendar_id":cid,"events":events},indent=2)+"\n")
 (out/"governance_calendar.ics").write_text(make_ics(cid,events))
 if pout:
  pout.mkdir(parents=True, exist_ok=True)
  (pout/"public_governance_calendar.json").write_text(json.dumps(pub,indent=2)+"\n")
  (pout/"public_governance_calendar.ics").write_text(make_ics(cid,events))
  (pout/"public_governance_calendar_summary.json").write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdGovernanceCalendarSummary","calendar_id":cid,"aggregate_targets":a.aggregate,"cadence":a.cadence,"events_total":len(events),"events_due_soon":0,"events_overdue":0,"events_blocked":0,"next_public_events":[{"event_id":events[0]["event_id"],"event_type":events[0]["event_type"],"title":events[0]["title"],"due_date":events[0]["start_date"],"public_required_action":events[0]["public_required_action"]}]},indent=2)+"\n")

if __name__=="__main__": main()
