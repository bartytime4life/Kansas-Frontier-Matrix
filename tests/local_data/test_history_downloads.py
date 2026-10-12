"""History originals reuse existing candidate capture without broadening hosts."""
import unittest
from tools.local_data import public_map_catalog, public_map_downloads


class HistoryOriginalTests(unittest.TestCase):
    def test_exact_originals_only(self):
        for url in public_map_downloads.HISTORY_FILES:
            self.assertEqual(public_map_downloads.validate_url(url), url)
            for changed in (url + "?download=1", url.replace("https://", "http://"),
                            url.replace(".pdf", "-other.pdf"),
                            url.replace("https://", "https://user@"),
                            url.replace(".pdf", "/../secrets.pdf")):
                with self.assertRaisesRegex(ValueError, "ASSET_URL_NOT_ALLOWLISTED"):
                    public_map_downloads.validate_url(changed)

    def test_seed_reconciliation_adds_books_without_discovery_or_rights_promotion(self):
        seed = public_map_catalog.load_seed()
        prior = {**seed, "records": [row for row in seed["records"] if row["sourceId"] != "history-originals"],
                 "coverage": [row for row in seed["coverage"] if row["sourceId"] != "history-originals"]}
        updated = public_map_catalog.reconcile_seed(prior)
        books = [row for row in updated["records"] if row["sourceId"] == "history-originals"]
        self.assertEqual(len(books), 2)
        self.assertEqual(sum(row["assets"][0]["expectedBytes"] for row in books), 50864070)
        self.assertEqual({row["assets"][0]["url"] for row in books}, set(public_map_downloads.HISTORY_FILES))
        self.assertFalse(updated["seedAugmentation"]["discoveryRefreshed"])
        self.assertTrue(all(row["mapYear"] is None and row["bbox"] is None for row in books))
        self.assertEqual(next(row for row in books if row["id"] == "history-arnold-history")["rights"]["status"], "held")
        self.assertEqual(len(prior["records"]), len(seed["records"]) - 2)
