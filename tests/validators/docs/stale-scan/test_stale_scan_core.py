from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path

from _support import FIXTURE_ROOT, VALIDATOR_DIR, copy_fixture, load_validator


stale_scan = load_validator()


class StaleScanCoreTests(unittest.TestCase):
    maxDiff = None

    def _scan(self, root: Path = FIXTURE_ROOT, **overrides):
        arguments = {
            "repo_root": root,
            "inputs": ("README.md", "docs"),
            "as_of": date(2026, 8, 7),
            "profile": "advisory",
            "review_window_days": 365,
            "placeholder_grace_days": 90,
            "type_windows": {},
            "git_diff": None,
            "warnings_as_errors": False,
        }
        arguments.update(overrides)
        return stale_scan.scan_stale_docs(**arguments)

    @staticmethod
    def _codes(result) -> set[str]:
        return {finding.code for finding in result.findings}

    def test_fixture_reports_expected_freshness_signals(self) -> None:
        result = self._scan()

        self.assertEqual(result.outcome, "DOC_STALE_SCAN_WARN")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.counts["documents"], 3)
        self.assertEqual(result.counts["documents_with_metadata"], 3)
        self.assertEqual(
            self._codes(result),
            {
                "IMPLEMENTATION_CLAIM_REVIEW_DUE",
                "OWNER_PLACEHOLDER_STALE",
                "REVIE]}WINDOW_EXPIRED",
                "TEMPORARY_MARKER_EXPIRED",
                "VERIFICATION_DEBT_REVIEW_DUE",
            },
        )

    def test_json_and_digest_are_deterministic(self) -> None:
        first = self._scan()
        second = self._scan()

        self.assertEqual(first.report_digest, second.report_digest)
        self.assertEqual(first.to_json(), second.to_json())
        payload = json.loads(first.to_json())
        self.assertEqual(payload["profile"], "kfm.docs.stale-scan.v1")
        self.assertTrue(payload["report_digest"].startswith("sha256:"))

    def test_fixture_matches_reviewed_snapshot(self) -> None:
        expected = json.loads(
            (FIXTURE_ROOT / "expected_stale_scan_report.json").read_text(encoding="utf-8")
        )
        actual = json.loads(self._scan().to_json())
        self.assertEqual(actual, expected)

    def test_markdown_is_explicitly_non_authoritative(self) -> None:
        report = self._scan().to_markdown()

        self.assertIn("# KFM Documentation Freshness Workbench", report)
        self.assertIn("not doctrine", report)
        self.assertIn("IMPLEMENTATION_CLAIM_REVIEW_DUE", report)
        self.assertIn("docs/expired.md", report)

    def test_missing_review_date_warns_in_advisory_profile(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("updated: 2026-07-15\n", ""),
            encoding="utf-8",
        )

        result = self._scan(root)

        self.assertIn("REVIEW_DATE_MISSING", self._codes(result))
        self.assertEqual(result.outcome, "DOC_STALE_SCAN_WARN")

    def test_missing_review_date_fails_in_bounded_required_profile(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("updated: 2026-07-15\n", ""),
            encoding="utf-8",
        )

        result = self._scan(root, profile="bounded-required")

        finding = next(item for item in result.findings if item.code == "REVIEW_DATE_MISSING")
        self.assertEqual(finding.severity, "fail")
        self.assertEqual(result.exit_code, 1)

    def test_future_review_date_fails_closed(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("2026-07-15", "2026-09-01"),
            encoding="utf-8",
        )

        result = self._scan(root)

        self.assertIn("FUTURE_REVIEW_DATE", self._codes(result))
        self.assertEqual(result.exit_code, 1)

    def test_invalid_date_fails_closed(self) -> None:
        temporary, root = copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "recent.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("2026-07-15", "2026-02-30"),
            encoding="utf-8",
        )

        result = self._scan(root)

        self.assertIn("REVIE]}Q}%9Y1%ˆ°Í•±˜¹}½‘•Ì¡É•ÍÕ±Ð¤¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡É•ÍÕ±Ð¹•á¥Ñ}½‘”°€Ä¤((€€€‘•˜Ñ•ÍÑ}É•…Ñ•‘}…™Ñ•É}É•Ù¥•Ý}‘…Ñ•}™…¥±Í}±½Í•¡Í•±˜¤€´ø9½¹”è(€€€€€€€Ñ•µÁ½É…Éä°É½½Ð€ô½Áå}™¥áÑÕÉ” ¤(€€€€€€€Í•±˜¹…‘‘±•…¹ÕÀ¡Ñ•µÁ½É…Éä¹±•…¹ÕÀ¤(€€€€€€€Ñ…É•Ð€ôÉ½½Ð€¼€‰‘½Ìˆ€¼€‰É••¹Ð¹µˆ(€€€€€€€Ñ…É•Ð¹ÝÉ¥Ñ•}Ñ•áÐ (€€€€€€€€€€€Ñ…É•Ð¹É•…‘}Ñ•áÐ¡•¹½‘¥¹œô‰ÕÑ˜´àˆ¤¹É•Á±…” ‰É•…Ñ•è€ÈÀÈØ´ÀÔ´ÀÄˆ°€‰É•…Ñ•è€ÈÀÈØ´Àà´ÀÄˆ¤°(€€€€€€€€€€€•¹½‘¥¹œô‰ÕÑ˜´àˆ°(€€€€€€€€¤((€€€€€€€É•ÍÕ±Ð€ôÍ•±˜¹}Í…¸¡É½½Ð¤((€€€€€€€Í•±˜¹…ÍÍ•ÉÑ%¸ ‰Q}=II}%9Y1%ˆ°Í•±˜¹}½‘•Ì¡É•ÍÕ±Ð¤¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡É•ÍÕ±Ð¹•á¥Ñ}½‘”°€Ä¤((€€€‘•˜Ñ•ÍÑ}ÑåÁ•}ÍÁ•¥™¥}Ý¥¹‘½Ý}¥Í}…ÁÁ±¥•¡Í•±˜¤€´ø9½¹”è(€€€€€€€É•ÍÕ±Ð€ôÍ•±˜¹}Í…¸¡ÑåÁ•}Ý¥¹‘½ÝÌõì‰ÍÑ…¹‘…Éˆè€ÄÁô¤((€€€€€€€É••¹Ð€ô¹•áÐ¡¥Ñ•´™½È¥Ñ•´¥¸É•ÍÕ±Ð¹‘½Õµ•¹ÑÌ¥˜¥Ñ•µl‰Á…Ñ ‰t€ôô€‰‘½Ì½É••¹Ð¹µˆ¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡É••¹Ñl‰É•Ù¥•Ý}Ý¥¹‘½Ý}‘…åÌ‰t°€ÄÀ¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑQÉÕ” (€€€€€€€€€€€…¹ä (€€€€€€€€€€€€€€€™¥¹‘¥¹œ¹½‘”€ôô€‰IY%]}]%9=]}aA%Iˆ…¹™¥¹‘¥¹œ¹Á…Ñ €ôô€‰‘½Ì½É••¹Ð¹µˆ(€€€€€€€€€€€€€€€™½È™¥¹‘¥¹œ¥¸É•ÍÕ±Ð¹™¥¹‘¥¹Ì(€€€€€€€€€€€€¤(€€€€€€€€¤((€€€‘•˜Ñ•ÍÑ}Ý…É¹¥¹Í}…Í}•ÉÉ½ÉÍ}ÁÉ½µ½Ñ•Í}ÕÉÉ•¹Ñ}Ý…É¹¥¹Ì¡Í•±˜¤€´ø9½¹”è(€€€€€€€É•ÍÕ±Ð€ôÍ•±˜¹}Í…¸¡Ý…É¹¥¹Í}…Í}•ÉÉ½ÉÌõQÉÕ”¤((€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡É•ÍÕ±Ð¹½ÕÑ½µ”°€‰=}MQ1}M9}%0ˆ¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑQÉÕ”¡…±°¡¥Ñ•´¹Í•Ù•É¥Ñä€ôô€‰™…¥°ˆ™½È¥Ñ•´¥¸É•ÍÕ±Ð¹™¥¹‘¥¹Ì¤¤((€€€‘•˜Ñ•ÍÑ}µ…±™½Éµ•‘}µ•Ñ…}‰±½­}‘•±•…Ñ•Í}Ý¥Ñ¡½ÕÑ}±…¥µ¥¹}™Õ±±}Á…ÉÍ”¡Í•±˜¤€´ø9½¹”è(€€€€€€€Ñ•µÁ½É…Éä°É½½Ð€ô½Áå}™¥áÑÕÉ” ¤(€€€€€€€Í•±˜¹…‘‘±•…¹ÕÀ¡Ñ•µÁ½É…Éä¹±•…¹ÕÀ¤(€€€€€€€Ñ…É•Ð€ôÉ½½Ð€¼€‰‘½Ìˆ€¼€‰É••¹Ð¹µˆ(€€€€€€€Ñ…É•Ð¹ÝÉ¥Ñ•}Ñ•áÐ (€€€€€€€€€€€Ñ…É•Ð¹É•…‘}Ñ•áÐ¡•¹½‘¥¹œô‰ÕÑ˜´àˆ¤¹É•Á±…” (€€€€€€€€€€€€€€€€ˆð„´´m-5}5Q}	1=-}XÉtˆ°€ˆð„´´m-5}5Q}	1=-}XÉuq¸ð„´´m-5}5Q}	1=-}XÉtˆ(€€€€€€€€€€€€¤°(€€€€€€€€€€€•¹½‘¥¹œô‰ÕÑ˜´àˆ°(€€€€€€€€¤((€€€€€€€É•ÍÕ±Ð€ôÍ•±˜¹}Í…¸¡É½½Ð¤((€€€€€€€Í•±˜¹…ÍÍ•ÉÑ%¸ ‰1Q}Q=}5Q}	1=,ˆ°Í•±˜¹}½‘•Ì¡É•ÍÕ±Ð¤¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑ9½Ñ%¸ ‰IY%]}]%9=]}aA%Iˆ°ì(€€€€€€€€€€€¥Ñ•´¹½‘”™½È¥Ñ•´¥¸É•ÍÕ±Ð¹™¥¹‘¥¹Ì¥˜¥Ñ•´¹Á…Ñ €ôô€‰‘½Ì½É••¹Ð¹µˆ(€€€€€€€ô¤((€€€‘•˜Ñ•ÍÑ}Á…Ñ¡}•Í…Á•}¥¹ÁÕÑ}¥Í}‘•¹¥•¡Í•±˜¤€´ø9½¹”è(€€€€€€€Ý¥Ñ Í•±˜¹…ÍÍ•ÉÑI…¥Í•Ì¡ÍÑ…±•}Í…¸¹MÑ…±•M…¹ÉÉ½È¤è(€€€€€€€€€€€Í•±˜¹}Í…¸¡¥¹ÁÕÑÌô ˆ¸¸½½ÕÑÍ¥‘”¹µˆ°¤¤((€€€Õ¹¥ÑÑ•ÍÐ¹Í­¥Á%˜¡½Ì¹¹…µ”€ôô€‰¹Ðˆ°€‰Íåµ‰½±¥Œµ±¥¹¬‰•¡…Ù¥½ÈÙ…É¥•Ì½¸]¥¹‘½ÝÌˆ¤(€€€‘•˜Ñ•ÍÑ}Íåµ‰½±¥}±¥¹­}¥¹ÁÕÑ}¥Í}‘•¹¥•¡Í•±˜¤€´ø9½¹”è(€€€€€€€Ñ•µÁ½É…Éä°É½½Ð€ô½Áå}™¥áÑÕÉ” ¤(€€€€€€€Í•±˜¹…‘‘±•…¹ÕÀ¡Ñ•µÁ½É…Éä¹±•…¹ÕÀ¤(€€€€€€€±¥¹¬€ôÉ½½Ð€¼€‰±¥¹­•¹µˆ(€€€€€€€±¥¹¬¹Íåµ±¥¹­}Ñ¼¡É½½Ð€¼€‰I5¹µˆ¤((€€€€€€€Ý¥Ñ Í•±˜¹…ÍÍ•ÉÑI…¥Í•Ì¡ÍÑ…±•}Í…¸¹MÑ…±•M…¹ÉÉ½È¤è(€€€€€€€€€€€Í•±˜¹}Í…¸¡É½½Ð°¥¹ÁÕÑÌô ‰±¥¹­•¹µˆ°¤¤((€€€‘•˜Ñ•ÍÑ}¡…¹•‘}™¥±•}É…Ñ¡•Ñ}½µ¥ÑÍ}Õ¹¡…¹•‘}Ý…É¹¥¹Ì¡Í•±˜¤€´ø9½¹”è(€€€€€€€Ñ•µÁ½É…Éä°É½½Ð€ô½Áå}™¥áÑÕÉ” ¤(€€€€€€€Í•±˜¹…‘‘±•…¹ÕÀ¡Ñ•µÁ½É…Éä¹±•…¹ÕÀ¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰¥¹¥Ðˆ°€ˆµÄ‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½¹™¥œˆ°€‰ÕÍ•È¹•µ…¥°ˆ°€‰™¥áÑÕÉ••á…µÁ±”¹¥¹Ù…±¥‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½¹™¥œˆ°€‰ÕÍ•È¹¹…µ”ˆ°€‰¥áÑÕÉ”‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰…‘ˆ°€ˆ¸‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½µµ¥Ðˆ°€ˆµÅ´ˆ°€‰‰…Í”‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€‰…Í”€ôÍÕ‰ÁÉ½•ÍÌ¹¡•­}½ÕÑÁÕÐ¡l‰¥Ðˆ°€‰É•ØµÁ…ÉÍ”ˆ°€‰!‰t°ÝõÉ½½Ð°Ñ•áÐõQÉÕ”¤¹ÍÑÉ¥À ¤(€€€€€€€É••¹Ð€ôÉ½½Ð€¼€‰‘½Ìˆ€¼€‰É••¹Ð¹µˆ(€€€€€€€É••¹Ð¹ÝÉ¥Ñ•}Ñ•áÐ¡É••¹Ð¹É•…‘}Ñ•áÐ¡•¹½‘¥¹œô‰ÕÑ˜´àˆ¤€¬€‰q¹ÕÉÉ•¹Ð¡…¹”¹q¸ˆ°•¹½‘¥¹œô‰ÕÑ˜´àˆ¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰…‘ˆ°€ˆ¸‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½µµ¥Ðˆ°€ˆµÅ´ˆ°€‰¡…¹”‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤((€€€€€€€É•ÍÕ±Ð€ôÍ•±˜¹}Í…¸¡É½½Ð°¥Ñ}‘¥™˜õ˜‰í‰…Í•ô¸¸¹!ˆ¤((€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡É•ÍÕ±Ð¹™¥¹‘¥¹Ì°€ ¤¤(€€€€€€€É••¹Ñ}‘½Œ€ô¹•áÐ¡¥Ñ•´™½È¥Ñ•´¥¸É•ÍÕ±Ð¹‘½Õµ•¹ÑÌ¥˜¥Ñ•µl‰Á…Ñ ‰t€ôô€‰‘½Ì½É••¹Ð¹µˆ¤(€€€€€€€•áÁ¥É•‘}‘½Œ€ô¹•áÐ¡¥Ñ•´™½È¥Ñ•´¥¸É•ÍÕ±Ð¹‘½Õµ•¹ÑÌ¥˜¥Ñ•µl‰Á…Ñ ‰t€ôô€‰‘½Ì½•áÁ¥É•¹µˆ¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑQÉÕ”¡É••¹Ñ}‘½l‰ÕÉÉ•¹Ð‰t¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑ…±Í”¡•áÁ¥É•‘}‘½l‰ÕÉÉ•¹Ð‰t¤((€€€‘•˜Ñ•ÍÑ}¡…¹•‘}™¥±•}É…Ñ¡•Ñ}‘½Ý¹É…‘•Í}¡¥ÍÑ½É¥…±}™…¥±ÕÉ•Ì¡Í•±˜¤€´ø9½¹”è(€€€€€€€Ñ•µÁ½É…Éä°É½½Ð€ô½Áå}™¥áÑÕÉ” ¤(€€€€€€€Í•±˜¹…‘‘±•…¹ÕÀ¡Ñ•µÁ½É…Éä¹±•…¹ÕÀ¤(€€€€€€€•áÁ¥É•€ôÉ½½Ð€¼€‰‘½Ìˆ€¼€‰•áÁ¥É•¹µˆ(€€€€€€€•áÁ¥É•¹ÝÉ¥Ñ•}Ñ•áÐ (€€€€€€€€€€€•áÁ¥É•¹É•…‘}Ñ•áÐ¡•¹½‘¥¹œô‰ÕÑ˜´àˆ¤¹É•Á±…” ‰ÕÁ‘…Ñ•è€ÈÀÈÐ´ÀÄ´ÄÔˆ°€‰ÕÁ‘…Ñ•è¥¹Ù…±¥ˆ¤°(€€€€€€€€€€€•¹½‘¥¹œô‰ÕÑ˜´àˆ°(€€€€€€€€€¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰¥¹¥Ðˆ°€ˆµÄ‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½¹™¥œˆ°€‰ÕÍ•È¹•µ…¥°ˆ°€‰™¥áÑÕÉ••á…µÁ±”¹¥¹Ù…±¥‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½¹™¥œˆ°€‰ÕÍ•È¹¹…µ”ˆ°€‰¥áÑÕÉ”‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰…‘ˆ°€ˆ¸‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½µµ¥Ðˆ°€ˆµÅ´ˆ°€‰‰…Í”‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€‰…Í”€ôÍÕ‰ÁÉ½•ÍÌ¹¡•­}½ÕÑÁÕÐ¡l‰¥Ðˆ°€‰É•ØµÁ…ÉÍ”ˆ°€‰!‰t°ÝõÉ½½Ð°Ñ•áÐõQÉÕ”¤¹ÍÑÉ¥À ¤(€€€€€€€É••¹Ð€ôÉ½½Ð€¼€‰‘½Ìˆ€¼€‰É••¹Ð¹µˆ(€€€€€€€É••¹Ð¹ÝÉ¥Ñ•}Ñ•áÐ¡É••¹Ð¹É•…‘}Ñ•áÐ¡•¹½‘¥¹œô‰ÕÑ˜´àˆ¤€¬€‰q¹ÕÉÉ•¹Ð¡…¹”¹q¸ˆ°•¹½‘¥¹œô‰ÕÑ˜´àˆ¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰…‘ˆ°€ˆ¸‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤(€€€€€€€ÍÕ‰ÁÉ½•ÍÌ¹ÉÕ¸¡l‰¥Ðˆ°€‰½µµ¥Ðˆ°€ˆµÅ´ˆ°€‰¡…¹”‰t°ÝõÉ½½Ð°¡•¬õQÉÕ”¤((€€€€€€€É•ÍÕ±Ð€ôÍ•±˜¹}Í…¸¡É½½Ð°¥Ñ}‘¥™˜õ˜‰í‰…Í•ô¸¸¹!ˆ¤((€€€€€€€¡¥ÍÑ½É¥…°€ô¹•áÐ¡¥Ñ•´™½È¥Ñ•´¥¸É•ÍÕ±Ð¹™¥¹‘¥¹Ì¥˜¥Ñ•´¹½‘”€ôô€‰IY%]}Q}%9Y1%ˆ¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡¡¥ÍÑ½É¥…°¹Í•Ù•É¥Ñä°€‰Ý…É¸ˆ¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑQÉÕ”¡¡¥ÍÑ½É¥…°¹¡¥ÍÑ½É¥…°¤(€€€€€€€Í•±˜¹…ÍÍ•ÉÑÅÕ…°¡É•ÍÕ±Ð¹•á¥Ñ}½‘”°€À¤((€€€‘•˜Ñ•ÍÑ}ÍÑ…Ñ¥}¥µÁ½ÉÑ}‰½Õ¹‘…Éå}½¹Ñ…¥¹Í}¹½}¹•ÑÝ½É­}±¥•¹Ð¡Í•±˜¤€´ø9½¹”è(€€€€€€€Í½ÕÉ”€ô€‰q¸ˆ¹©½¥¸ (€€€€€€€€€€€Á…Ñ ¹É•…‘}Ñ•áÐ¡•¹½‘¥¹œô‰ÕÑ˜´àˆ¤(€€€€€€€€€€€™½ÈÁ…Ñ ¥¸Í½ÉÑ•¡Y1%Q=I}%H¹±½ˆ ˆ¨¹Áäˆ¤¤(€€€€€€€€¤(€€€€€€€™½É‰¥‘‘•¸€ô€ ‰É•ÅÕ•ÍÑÌˆ°€‰ÕÉ±±¥ˆ¹É•ÅÕ•ÍÐˆ°€‰¡ÑÑÁàˆ°€‰…¥½¡ÑÑÀˆ°€‰Í½­•Ðˆ¤(€€€€€€€™½È¹…µ”¥¸™½É‰¥‘‘•¸è(€€€€€€€€€€€Í•±˜¹…ÍÍ•ÉÑ9½Ñ%¸¡˜‰¥µÁ½ÉÐí¹…µ•ôˆ°Í½ÕÉ”¤(€€€€€€€€€€€Í•±˜¹…ÍÍ•ÉÑ9½Ñ%¸¡˜‰™É½´í¹…µ•ôˆ°Í½ÕÉ”¤(()¥˜}}¹…µ•}|€ôô€‰}}µ…¥¹}|ˆè(€€€Õ¹¥ÑÑ•ÍÐ¹µ…¥¸ ¤