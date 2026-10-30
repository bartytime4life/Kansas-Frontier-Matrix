"""Independent Decimal/CSV reference; no KFM calculations or network calls.
Run: python3 tests/iem_reference_totals.py
The trace sentinel is counted, not interpreted as a measured precipitation depth.
"""
import csv
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

root = Path(__file__).parent / 'fixtures' / 'iem'
expected = {'sln-2024.csv': ('4426.4', '15.81', 28), 'gld-2024.csv': ('3748.6', '8.28', 17)}
results = []
for filename, (heat, rain, traces) in expected.items():
    with (root / filename).open() as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == len({row['day'] for row in rows}) == 214
    assert rows[0]['day'] == '2024-04-01' and rows[-1]['day'] == '2024-10-31'
    gdd = sum(max(Decimal(0), (min(Decimal(row['max_temp_f']), Decimal(86)) + max(Decimal(row['min_temp_f']), Decimal(50))) / 2 - 50) for row in rows)
    measured = sum(Decimal(row['precip_in']) for row in rows if row['precip_in'] != '0.0001')
    trace_days = sum(row['precip_in'] == '0.0001' for row in rows)
    assert (gdd, measured, trace_days) == (Decimal(heat), Decimal(rain), traces)
    results.append({'file': filename, 'days': len(rows), 'degree_days_unrounded': str(gdd), 'degree_days_display': int(gdd.quantize(Decimal(1), rounding=ROUND_HALF_UP)), 'measured_precip_in': str(measured), 'trace_days': trace_days})
print(json.dumps(results, indent=2))
