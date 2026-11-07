"""Opt-in real Chromium UI checks; all files and extraction are synthetic.

Run separately from the no-network suite with KFM_INTAKE_BROWSER_TESTS=1.
Missing Playwright or a failed browser launch is an error when explicitly run.
"""

import hashlib
import json
import os
import tempfile
import threading
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlsplit

from tests.local_data.test_intake_studio import fake_extract
from tools.local_data.intake_studio.intake_server import Server, Store


@unittest.skipUnless(
    os.environ.get("KFM_INTAKE_BROWSER_TESTS") == "1",
    "Opt in with KFM_INTAKE_BROWSER_TESTS=1 and provision Playwright/Chromium",
)
class BrowserTests(unittest.TestCase):
    def test_flag_retention_reopen_restart_and_ready_denial(self):
        from playwright.sync_api import expect, sync_playwright

        with sync_playwright() as playwright:
            executable = os.environ.get("KFM_INTAKE_TEST_CHROMIUM")
            with playwright.chromium.launch(
                **({"executable_path": executable} if executable else {})
            ) as browser:
                for viewport in [
                    {"width": 1365, "height": 1000},
                    {"width": 390, "height": 844},
                ]:
                    with (
                        self.subTest(viewport=viewport),
                        tempfile.TemporaryDirectory() as root,
                    ):
                        store = Store(root, Path(root) / "missing-runtime")
                        server = Server(0, store)
                        thread = threading.Thread(
                            target=server.serve_forever, daemon=True
                        )
                        thread.start()
                        context = browser.new_context(
                            viewport=viewport, accept_downloads=True
                        )
                        page = context.new_page()
                        errors, external = [], []
                        page.on(
                            "pageerror",
                            lambda error, errors=errors: errors.append(str(error)),
                        )
                        page.on(
                            "request",
                            lambda request, external=external: (
                                external.append(request.url)
                                if urlsplit(request.url).hostname != "127.0.0.1"
                                and not request.url.startswith(("blob:", "data:"))
                                else None
                            ),
                        )
                        page.on("dialog", lambda dialog: dialog.accept())
                        try:
                            page.goto(server.origin)
                            expect(page.locator("#visible-count")).to_have_text(
                                "0 files"
                            )
                            body = b"\x89PNG\r\n\x1a\nsynthetic browser regression"
                            with patch(
                                "tools.local_data.intake_studio.intake_server.subprocess.run",
                                side_effect=fake_extract,
                            ):
                                page.locator("#files-input").set_input_files(
                                    {
                                        "name": "browser-synthetic.png",
                                        "mimeType": "image/png",
                                        "buffer": body,
                                    }
                                )
                                expect(page.locator("#review-form")).to_be_visible()
                            record_id = store.list()[0]["id"]

                            def save(status=200, page=page):
                                with page.expect_response(
                                    lambda response: (
                                        response.url.endswith("/review")
                                        and response.request.method == "POST"
                                    )
                                ) as response:
                                    page.locator("#save-review").click()
                                self.assertEqual(response.value.status, status)
                                if status == 200:
                                    expect(
                                        page.locator("#save-message")
                                    ).to_contain_text("Saved revision")

                            for name, value in {
                                "source": "Synthetic QA source",
                                "reviewer": "Synthetic QA",
                                "description": "archaeological burial location",
                            }.items():
                                page.locator(f'[name="{name}"]').fill(value)
                            for name, value in {
                                "rights": "Owned by me",
                                "sensitivity": "Public",
                                "domain": "hydrology",
                                "surface": "Reference library",
                            }.items():
                                page.locator(f'[name="{name}"]').select_option(
                                    label=value
                                )
                            save()
                            flag = page.locator(".note").filter(has_text="Review flag:")
                            expect(flag).to_have_count(1)
                            for description, decision in [
                                ("Harmless water notes", "Keep quarantined"),
                                ("", "Needs review"),
                            ]:
                                page.locator('[name="description"]').fill(description)
                                page.locator('[name="decision"]').select_option(
                                    label=decision
                                )
                                save()
                                expect(flag).to_have_count(1)

                            # Discard an unsaved edit, then reopen the saved record.
                            page.locator('[name="description"]').fill(
                                "Unsaved harmless edit"
                            )
                            page.reload()
                            page.locator("[data-file]").click()
                            expect(page.locator('[name="description"]')).to_have_value(
                                ""
                            )
                            expect(flag).to_have_count(1)

                            # Restart the server and Store with the same private inbox.
                            port = server.server_port
                            server.shutdown()
                            server.server_close()
                            thread.join(timeout=5)
                            server = Server(
                                port, Store(root, Path(root) / "missing-runtime")
                            )
                            thread = threading.Thread(
                                target=server.serve_forever, daemon=True
                            )
                            thread.start()
                            page.reload()
                            page.locator("[data-file]").click()
                            expect(flag).to_have_count(1)
                            page.locator('[name="decision"]').select_option(
                                label="Ready for integration review"
                            )
                            save(400)
                            expect(page.locator("#save-message")).to_contain_text(
                                "separate governed review"
                            )
                            self.assertEqual(
                                server.store.get(record_id)["review"]["decision"],
                                "Needs review",
                            )

                            # Export the last saved revision through the actual UI.
                            with page.expect_download() as download:
                                page.locator("#export-record").click()
                            with zipfile.ZipFile(download.value.path()) as archive:
                                proposal = json.loads(
                                    archive.read("review-proposal.json")
                                )
                                self.assertTrue(proposal["record"]["analysis"]["flags"])
                                self.assertFalse(any(proposal["authority"].values()))
                                self.assertEqual(
                                    archive.read("original/browser-synthetic.png"), body
                                )
                                for name, digest in json.loads(
                                    archive.read("checksums.json")
                                ).items():
                                    self.assertEqual(
                                        hashlib.sha256(archive.read(name)).hexdigest(),
                                        digest,
                                    )
                            self.assertEqual(errors, [])
                            self.assertEqual(external, [])
                        finally:
                            context.close()
                            server.shutdown()
                            server.server_close()
                            thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
