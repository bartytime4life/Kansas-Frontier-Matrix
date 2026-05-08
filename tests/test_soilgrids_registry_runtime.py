import json, sqlite3
from pathlib import Path
from tools.soilgrids.soilgrids_registry_runtime import enforce_readonly_sql, open_sqlite_readonly_immutable, build_dashboard_bundle


def _mk(tmp):
    r=tmp/'r'; r.mkdir()
    (r/'registry_manifest.json').write_text('{"schema":"RegistryManifest.v1"}\n')
    (r/'registry_snapshot.json').write_text('{"registry_snapshot_id":"snap1"}\n')
    (r/'registry_receipt.json').write_text('{"status":"success"}\n')
    (r/'openapi.json').write_text('{"openapi":"3.1.1"}\n')
    (r/'saved_queries.json').write_text('{"queries":[{"query_id":"q1","sql":"SELECT 1"}]}\n')
    db=r/'registry.sqlite'; con=sqlite3.connect(db); con.execute('create table entities(registry_entity_id text)'); con.execute("insert into entities values ('e1')"); con.commit(); con.close()
    return r, db

def test_rejects_insert_sql():
    try:
        enforce_readonly_sql('INSERT INTO x VALUES (1)')
        assert False
    except ValueError:
        assert True

def test_allows_select_sql():
    enforce_readonly_sql('SELECT 1')

def test_sqlite_opens_readonly_immutable(tmp_path):
    r, db=_mk(tmp_path)
    con=open_sqlite_readonly_immutable(db)
    assert con.execute('select 1').fetchone()[0]==1

def test_dashboard_index_written(tmp_path):
    r, db=_mk(tmp_path)
    class A: pass
    a=A(); a.registry_manifest=str(r/'registry_manifest.json'); a.registry_snapshot=str(r/'registry_snapshot.json'); a.registry_receipt=str(r/'registry_receipt.json'); a.sqlite_db=str(db); a.openapi=str(r/'openapi.json'); a.saved_queries=str(r/'saved_queries.json'); a.registry_query_contract=None; a.registry_validation_report=None; a.search_index=None; a.runtime_root=str(tmp_path/'runtime'); a.runtime_mode='build-dashboard'; a.dashboard_title='T'; a.overwrite=False
    p=build_dashboard_bundle(a)
    assert p.exists()
