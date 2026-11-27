# Stage a Science & Labs refresh

Daily dev intake and SQL feeds retain and index provider inputs. Science & Labs reads packaged display snapshots. The date shown on the Science & Labs hub is the capture date for the bundled inputs. Its analysis window gives the date range the display can use, with missing observations still shown in each lab. A successful daily intake run cannot change either date on the app.

After the dev download, run this from the hosted app checkout using the private capture directories for the enabled lanes. Each directory must include the matching original objects and the capture receipt written by the existing preparation script. The SQL `observations.sqlite` and the daily archive are different formats.

```bash
python3 scripts/stage-science-refresh.py \
  --weather /path/private/ghcn-capture \
  --land /path/private/drought-soil-capture \
  --air /path/private/epa-capture \
  --sunlight /path/private/power-capture \
  --stage-dir /path/private/new-refresh-candidate
```

| Lane | Verified input profile | Displays |
|---|---|---|
| Weather | `prepare-daily-climate.py` GHCN station files and metadata | Heat and Rain |
| Land | `prepare-drought-and-soil.py` USDM and USCRN capture | County Drought and Soil Profile |
| Air | `prepare-daily-air-quality.py` annual EPA AirData ZIPs and index | Daily Air Quality |
| Sunlight | `prepare-sunlight.py` NASA POWER query responses and documentation | Sunlight and Sky |

Invoke only the enabled lanes. The command reads local captures, regenerates display assets offline and checks each candidate's hash, size, reporting period, and provider identity. Re-capturing identical source bytes yields `unchanged`. A changed lane stores its candidate under the lane directory and records `review-required` in `report.json`. The report distinguishes changed provider objects from changed observations within the packaged window. Review each lane against the currently deployed manifest before promoting a successor.

- **Waiting for capture.** Check the dev run's completion receipt and retry that source after its provider is ready. Keep the last verified display available.
- **Hold.** Compare the candidate reason with the dev receipt. Plan a provider retry for transient failures. Resolve invalid or missing bytes, shortened coverage, and replaced identities through review of the exact source and candidate, then stage again.
- **Review required.** Review the selected source objects, attribution and license, analytical changes, and asset hashes. Submit the generated snapshot and manifest together through the existing code and release review. Retain working older hash-addressed assets through the deployment transition.

The current generators use a 2020–2025 analysis window. A daily source revision can change observations in that window. Extending the window requires a coordinated change across the lab and report controls and the verified source captures. A successful run returns 0 for unchanged or ready-for-review lanes. Exit 2 means at least one configured lane is waiting or held. Successful siblings still appear in the report. The command never publishes, mutates SQL, or changes the dev schedule.
