"""Plan/apply/restore a bounded metadata-only catalog correction by explicit IDs.

Stop catalog writers/readers and hold the operator's pipeline lock first. This
does not open payload files, reprofile content, admit data or apply placements.
The recovery journal preserves exact rows; SQLite makes each edit all-or-nothing.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sqlite3

from tools.local_data.file_io import open_regular, read_regular, write_new
from tools.local_data.intake_profile import CLASSIFIER_VERSION, classification_hints
from tools.local_data.intake_route import REVIEW_DOMAINS, work_target

SCHEMA = 'kfm-catalog-reclassification/v1'
MAX_ROWS = 1000
MAX_BYTES = 24 * 1024**2
EDIT_COLUMNS = ('domain', 'profile_json', 'decision_json')


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False) + '\n').encode()


def connection(database, *, write=False):
    database = Path(database).absolute()
    os.close(open_regular(database))
    conn = sqlite3.connect(database.as_uri() + ('?mode=rw' if write else '?mode=ro'), uri=True, timeout=5)
    conn.row_factory = sqlite3.Row
    if not write:
        conn.execute('PRAGMA query_only=ON')
    return conn


def replacement(row):
    """Only correct resolved, non-sensitive domains with unchanged review flags."""
    profile = json.loads(row['profile_json'])
    declared = json.loads(row['declared_json']) if row['declared_json'] else {}
    hints = classification_hints(declared.get('relative_path') or row['relative_path'],
                                 profile.get('structure', {}), profile.get('issues', []), declared.get('domain'))
    old_domain, new_domain = row['domain'], hints['domain']
    if old_domain == new_domain:
        return None
    decision = json.loads(row['decision_json'])
    if (not row['present'] or not old_domain or not new_domain
            or {old_domain, new_domain} & REVIEW_DOMAINS
            or profile.get('hints', {}).get('domain') != old_domain or decision.get('domain') != old_domain
            or profile.get('hints', {}).get('review_flags', []) != hints['review_flags']):
        raise ValueError('CATALOG_REVIEW_CHANGE_REQUIRES_SEPARATE_ANALYSIS')
    profile['hints'] = hints
    decision['domain'] = new_domain
    for placement in decision.get('placements', []):
        if placement.get('tier') == 'work_lane' and placement.get('action') == 'stage':
            item = dict(row, declared=declared)
            if placement.get('target') != work_target(item, old_domain):
                raise ValueError('CATALOG_WORK_TARGET_UNEXPECTED')
            placement['target'] = work_target(item, new_domain)
    after = dict(row)
    after.update(domain=new_domain, profile_json=canonical(profile).decode(), decision_json=canonical(decision).decode())
    return after


def plan(database: Path, identities: list[str]):
    if (not isinstance(identities, list) or not 0 < len(identities) <= MAX_ROWS
            or any(not isinstance(identity, str) or not 0 < len(identity) <= 128 for identity in identities)
            or len(set(identities)) != len(identities)):
        raise ValueError('CATALOG_ID_LIMIT_OR_DUPLICATE')
    changes = []
    conn = connection(database)
    try:
        conn.execute('BEGIN')
        for identity in identities:
            row = conn.execute('SELECT * FROM items WHERE id=?', (identity,)).fetchone()
            if row is None:
                raise ValueError('CATALOG_ITEM_MISSING')
            before = dict(row)
            after = replacement(before)
            if after is not None:
                changes.append({'before': before, 'after': after})
    finally:
        conn.close()
    result = {'schema': SCHEMA, 'database': str(database.absolute()), 'classifier_version': CLASSIFIER_VERSION,
              'planned_at': datetime.now(timezone.utc).isoformat(), 'selected': len(identities),
              'unchanged': len(identities) - len(changes), 'changes': changes}
    if len(canonical(result)) > MAX_BYTES:
        raise ValueError('CATALOG_PLAN_BYTE_LIMIT')
    return result


def apply(database: Path, plan_path: Path, expected_sha256: str, recovery: Path, *, restore=False):
    raw = read_regular(plan_path, MAX_BYTES)
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError('CATALOG_PLAN_PIN_CHANGED')
    value = json.loads(raw)
    changes = value.get('changes', [])
    if (value.get('schema') != SCHEMA or value.get('database') != str(database.absolute())
            or value.get('classifier_version') != CLASSIFIER_VERSION or not 0 < len(changes) <= MAX_ROWS
            or len({c['before']['id'] for c in changes}) != len(changes)):
        raise ValueError('CATALOG_PLAN_INVALID')
    for change in changes:
        # A pinned file cannot be used to change holds, byte hashes or arbitrary columns.
        if replacement(change['before']) != change['after']:
            raise ValueError('CATALOG_PLAN_NOT_REPRODUCIBLE')
    conn = connection(database, write=True)
    try:
        conn.execute('PRAGMA synchronous=FULL')
        conn.execute('BEGIN IMMEDIATE')
        for change in changes:
            current, target = (change['after'], change['before']) if restore else (change['before'], change['after'])
            row = conn.execute('SELECT * FROM items WHERE id=?', (current['id'],)).fetchone()
            if row is None or dict(row) != current:
                raise ValueError('CATALOG_ROW_CHANGED')
            conn.execute('UPDATE items SET domain=?, profile_json=?, decision_json=? WHERE id=?',
                         tuple(target[key] for key in EDIT_COLUMNS) + (current['id'],))
        # A durable exclusive journal must exist before committing any changed rows.
        write_new(recovery, raw)
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()
    return {'state': 'RESTORED' if restore else 'APPLIED', 'rows': len(changes),
            'recovery': str(recovery), 'plan_sha256': expected_sha256,
            'payload_reads': 0, 'source_admission': False, 'publication': False}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--database', type=Path, required=True)
    sub = cli.add_subparsers(dest='action', required=True)
    preview = sub.add_parser('plan')
    preview.add_argument('--ids', type=Path, required=True, help='JSON array of explicit item IDs')
    preview.add_argument('--output', type=Path, required=True)
    for action in ('apply', 'restore'):
        command = sub.add_parser(action)
        command.add_argument('--plan', type=Path, required=True)
        command.add_argument('--sha256', required=True)
        command.add_argument('--recovery', type=Path, required=True)
    args = cli.parse_args()
    if args.action == 'plan':
        value = plan(args.database, json.loads(read_regular(args.ids, MAX_BYTES)))
        raw = canonical(value)
        write_new(args.output, raw)
        print(json.dumps({'selected': value['selected'], 'changed': len(value['changes']),
                          'unchanged': value['unchanged'], 'sha256': hashlib.sha256(raw).hexdigest()}))
    else:
        print(json.dumps(apply(args.database, args.plan, args.sha256, args.recovery, restore=args.action == 'restore')))


if __name__ == '__main__':
    main()
