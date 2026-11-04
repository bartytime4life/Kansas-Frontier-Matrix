# Kansas Sky replay source members

These two gzip files retain original compressed member bytes from the public
adsb.lol 2026-11-03 readsb-prod-0 archive. They are offline reproducibility inputs,
not synthetic tracks and not application-served global archives.

Source: https://github.com/adsblol/globe_history_2026/releases/download/v2026.11.03-planes-readsb-prod-0/v2026.11.03-planes-readsb-prod-0.tar.aa

- `./traces/ea/trace_full_ac2fea.json`: SHA256 `4d7aca5708043651ec106e4777ccb43c9d97f2d58827967bf3bb53efcd4cd59b`
- `./traces/ea/trace_full_aae1ea.json`: SHA256 `80a8380fc978496305ae3ced954496bfe8939e4c94f64080505a7a3dd1606b53`

Downloaded 2026-11-04. Attribution: adsb.lol and its receiver contributors.
Data license: [Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/).
The prepared replay database remains available under ODbL 1.0. The public replay
JSON includes source member, compressed-byte hash, transformation and license;
its catalog pins the resulting JSON hash. The converter clips to the existing
Kansas region and selects one continuous segment. It does not infer owners,
missions, incidents, or flight purpose. Full raw members here permit inspection
of every selected original record and the transformation.

`node --test tests/kansas-sky.test.mjs` regenerates each public artifact offline
and compares its exact bytes. Public artifacts and source inputs are distinct
from internal KFM stores. No source-store migration or release-state change is
performed by the converter.
