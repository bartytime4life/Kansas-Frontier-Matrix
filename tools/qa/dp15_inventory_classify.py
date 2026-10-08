#!/usr/bin/env python3
"""Classify the pinned scan as review aids, not policy or adoption decisions."""
import collections, csv, gzip, hashlib, io, json, pathlib, re, shutil, subprocess, sys
repo,scan,out=map(pathlib.Path,sys.argv[1:4]);out.mkdir(parents=True,exist_ok=True)
summary=json.loads((scan/'summary.json').read_text()); hits=json.loads((scan/'hits.json').read_text())
assert not summary['errors']
assert summary['commit']=='c90836cdb7a34791669907053522de0458f21ae9', 'Successor snapshot requires new semantic review/classification'
manifest={x['path']:x for x in json.loads((scan/'tree-manifest.json').read_text())}
def authority(path):
    source=path.split('::')[0]
    if '::package/' in path: return 'VENDORED_FRAMEWORK_SOURCE; not KFM adoption'
    if '::strings' in path:return 'BINARY_ASSET_OR_SYNTHETIC_FIXTURE; no executable DP authority'
    if source.endswith('.md') or '::pdftotext' in path:
        if source.startswith('contracts/'):return 'SEMANTIC_DOCUMENT; acceptance only if separately established'
        return 'GUIDANCE_OR_BOUNDARY_DOCUMENT; no DP execution/release authority'
    if source.startswith('schemas/'):return 'MACHINE_SHAPE; DP authority not established'
    if source.startswith('policy/'):return 'POLICY_SOURCE_OR_SCAFFOLD; no DP rule found'
    if source.startswith('.github/'):return 'CI_ORCHESTRATION; no DP enforcement found'
    if source.startswith(('fixtures/','tests/')) or '/tests/' in source:return 'SYNTHETIC_FIXTURE_OR_TEST; not an operative DP profile'
    if source.startswith('data/receipts/generated/'):return 'GENERATED_PROVENANCE; not a DP process/budget receipt'
    if source.startswith(('data/','release/','catalog/')):return 'DATA_OR_RELEASE_SURFACE; no DP-bearing object found'
    if source.endswith(('.lock','.toml')) or source.endswith(('package.json','package-lock.json','requirements.txt')):return 'DEPENDENCY_OR_CONFIG_SOURCE; no DP dependency admission found'
    if source.endswith(('.py','.ts','.tsx','.mjs','.sh','.rego')):return 'EXECUTABLE_SOURCE_OR_SCAFFOLD; no DP implementation found'
    return 'SUPPORTING_SOURCE_OR_CONFIG; no DP authority found'
def disposition(h):
    p=h['path'];t=h['text'];q=h['queries']
    if h['representation']=='binary-strings':return 'BINARY_LEXICAL_COINCIDENCE', 'Printable asset bytes; no DP semantic binding'
    if p.startswith('data/receipts/generated/genrec-dp-budgets-'):return 'DOCUMENTATION_PROVENANCE', 'Records authoring of guidance; no privacy expenditure or mechanism output'
    if p.startswith(('docs/sources/catalog/census/acs-estimates.md','docs/sources/catalog/census/decennial-counts.md')) and ('dp_explicit' in q or 'dp_library' in q or re.search(r'\bDP\b|\bDAS\b|disclosure.avoidance',t,re.I)):
        return 'UPSTREAM_CENSUS_CLAIM_OR_GUIDANCE', 'Repository prose about upstream disclosure controls; not KFM implementation; upstream facts not revalidated'
    if 'dp_explicit' in q or 'dp_library' in q:
        return 'DP_GUIDANCE_PROPOSAL_OR_EXCLUSION', 'DP named in human documentation; no accepted executable DP binding'
    if 'dp_alias' in q:
        if p.startswith('docs/standards/Darwin_Core.md'):return 'NON_DP_ALIAS', 'DwC-DP means Darwin Core Data Package'
        if re.search(r'\bDP[0-9]{2}',t,re.I):return 'NON_DP_ALIAS','DP05 etc. are Census data-profile variable identifiers'
        if re.search(r'\bGDP\b|\bgdp[_-]',t,re.I):return 'NON_DP_ALIAS','GDP means gross domestic product/economic measure'
        if re.search(r'\bCDP\b|\bcdp[_-]',t,re.I):return 'NON_DP_ALIAS','CDP means Census-designated place or browser Chrome DevTools Protocol'
        if re.search(r'\bDP\b|\bdp[_-](?:applied|epsilon|aggregate|budget|receipt|nois|release)',t,re.I):
            if p.startswith(('docs/domains/hydrology/','docs/domains/geology/FILE_SYSTEM_PLAN')):return 'NON_DP_ALIAS','DP is a Mermaid node for data/processed'
            if p in ('docs/architecture/ui/CONTINUITY_NOTES.md','docs/focus-mode/counties/README.md','docs/focus-mode/counties/chase_county/chase_county_focus_mode_build_plan.md'):return 'NON_DP_ALIAS','DP is a Mermaid node for EvidenceDrawerPayload, data/published or deprecated'
            return 'DP_GUIDANCE_PROPOSAL_OR_EXCLUSION','DP reference in guidance/example; no executable binding'
        return 'ADJACENT_PRIVACY_OR_NON_DP_ALIAS','Privacy-preserving wording or abbreviated non-DP token; no DP construction/accounting'
    if 'mechanism' in q:return 'NON_DP_NUMERIC_OR_GUIDANCE','Numerical tolerance, Gaussian elimination, glyph, display-jitter example, or unbound documentation term'
    return 'BROAD_NON_DP_SUPPORT', 'Generic privacy/sensitivity, access modifier, physical noise, clipping, change delta, resource budget, ledger, or composition; no DP-specific binding'

by_path=collections.defaultdict(list)
for h in hits:
    h['authority_level']=authority(h['path']);h['disposition'],h['reason']=disposition(h);by_path[h['path']].append(h)
fields=['path','line','blob','representation','authority_level','disposition','queries','matches','reason']
buf=io.StringIO();writer=csv.DictWriter(buf,fields,lineterminator='\n');writer.writeheader()
for h in hits:
    writer.writerow({**{k:h[k] for k in fields if k in h},'queries':';'.join(h['queries']), 'matches':json.dumps(h['queries'],ensure_ascii=False,separators=(',',':'))})
(out/'hits.csv.gz').write_bytes(gzip.compress(buf.getvalue().encode(),mtime=0))
index=[]
for p,rows in sorted(by_path.items()):
    source=p.split('::')[0];status='not declared in a directly readable status field'
    if source in manifest and (repo/source).suffix=='.md':
        content=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',manifest[source]['blob']]).decode(errors='replace')
        m=re.search(r'^status:\s*(.+)$',content,re.M)
        if m:status=m.group(1)
    index.append(dict(path=p,blob=rows[0]['blob'],source_status=status,authority_level=authority(p),dispositions=sorted(set(h['disposition'] for h in rows)),query_lines={q:sorted(set(h['line'] for h in rows if q in h['queries'])) for q in summary['queries'] if any(q in h['queries'] for h in rows)},hit_rows=len(rows)))
summary['authority_boundary']='Exhaustive tracked-blob visitation plus disclosed lexical inventory and source review; not a proof about untracked/deployed/remote/obfuscated machinery or permission to use DP'
summary['classification_counts']=dict(collections.Counter(h['disposition'] for h in hits))
summary['classification_coverage']=dict(input_rows=len(hits),classified_rows=sum(x['hit_rows'] for x in index),classified_paths=len(index),unclassified_rows=0)
summary['inventory']=index
summary['dependency_paths']=[p for p in manifest if re.search(r'(^|/)([^/]*\.lock|package(-lock)?\.json|pyproject\.toml|[^/]*requirements[^/]*\.(txt|in|lock)|pnpm-lock\.yaml|Cargo\.toml|go\.(mod|sum)|pom\.xml|Dockerfile[^/]*)$',p)]
assert sum(x['hit_rows'] for x in index)==len(hits)
summary['gzip_paths']=[p for p in manifest if p.endswith('.gz')]
summary['archive_paths']=[p for p in manifest if p.endswith('.tgz')]
(out/'inventory.json.gz').write_bytes(gzip.compress((json.dumps(summary,indent=2,ensure_ascii=False)+'\n').encode(),mtime=0))
summary_only={k:v for k,v in summary.items() if k!='inventory'}
(out/'summary.json').write_text(json.dumps(summary_only,indent=2,ensure_ascii=False)+'\n')
high=[h for h in hits if h['disposition'] in ('DP_GUIDANCE_PROPOSAL_OR_EXCLUSION','UPSTREAM_CENSUS_CLAIM_OR_GUIDANCE','DOCUMENTATION_PROVENANCE')]
(out/'dp-declarations.json').write_text(json.dumps(high,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(classification_counts=summary['classification_counts'],classification_coverage=summary['classification_coverage'],dp_declaration_paths=len(set(x['path'] for x in high)),files={p.name:p.stat().st_size for p in out.iterdir()}),indent=2))
