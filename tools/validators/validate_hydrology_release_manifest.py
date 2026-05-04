import json
m=json.load(open('fixtures/domains/hydrology/release_manifests/hydrology_synthetic_streamflow.release_manifest.json'))
assert m['release_status']=='PUBLISHED_SYNTHETIC'
assert any('raw' in x for x in m['prohibited_source_paths'])
assert m['synthetic'] and m['no_network']
assert m['included_review_record_ids']
print('ok')
