"""Local Studio administration program and data workspace configuration.

Reduced KDF cost is test-only (as in test_studio_accounts_recovery.py); the
runtime configuration is unchanged. No network or real home directory is used.
"""
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import manage
from tools.local_data.intake_studio import accounts as a
from tools.local_data.intake_studio import studio_admin as admin
from tools.local_data.intake_studio import workspace_config as wc

PASS = "Synthetic passphrase 82! only"
NEW = "Another synthetic phrase 41!"
THIRD = "Yet another synthetic phrase 7"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name); self.home.chmod(0o700)
        self.store = self.home / "store"; self.store.mkdir(mode=0o700)
        self.config = self.home / "config" / "workspace.json"
        p = patch.dict(a.KDF, {"n": 1024, "r": 8, "p": 1}); p.start(); self.addCleanup(p.stop)
        self.acc = a.Accounts(self.store)
        self.acc.bootstrap(self.acc.issue_setup_code(), "owner", PASS)
        self.owner_token = self.acc.login("owner", PASS)

    def run_cli(self, *argv, secrets=(), answers=()):
        out, err = io.StringIO(), io.StringIO()
        prompts = iter(secrets); replies = iter(answers)
        with patch.object(admin.getpass, "getpass", lambda *_: next(prompts)), \
             patch.object(admin.sys.stdin, "isatty", lambda: True), \
             patch("builtins.input", lambda *_: next(replies)), \
             patch.object(admin, "running", lambda: None), \
             contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = admin.main(["--store", str(self.store), "--config", str(self.config), *argv])
        return code, out.getvalue(), err.getvalue()


class LocalAccountTests(Base):
    def test_admin_password_change_revokes_sessions_and_signs_in(self):
        self.acc.local_set_password("owner", NEW)
        self.assertIsNone(self.acc.session(self.owner_token))
        self.assertTrue(self.acc.login("owner", NEW))
        with self.assertRaises(a.AccessError):
            self.acc.login("owner", PASS)

    def test_last_admin_cannot_be_made_temporary_or_disabled(self):
        with self.assertRaisesRegex(a.AccessError, "LAST_ACTIVE_ADMIN_MUST_REMAIN"):
            self.acc.local_set_password("owner", NEW, temporary=True)
        for change in ({"enabled": False}, {"role": "viewer"}):
            with self.subTest(change=change), self.assertRaisesRegex(a.AccessError, "LAST_ACTIVE_ADMIN_MUST_REMAIN"):
                self.acc.local_update("owner", **change)

    def test_create_temporary_then_user_must_change(self):
        self.acc.local_create("helper", "operator", PASS)
        user = self.acc.session(self.acc.login("helper", PASS))
        self.assertTrue(user["mustChangePassword"]); self.assertEqual(user["role"], "operator")
        with self.assertRaisesRegex(a.AccessError, "USERNAME_ALREADY_EXISTS"):
            self.acc.local_create("helper", "viewer", PASS)
        with self.assertRaisesRegex(a.AccessError, "INVALID_ROLE"):
            self.acc.local_create("other", "root", PASS)

    def test_create_requires_first_owner(self):
        empty = self.home / "empty"; empty.mkdir(mode=0o700)
        with self.assertRaisesRegex(a.AccessError, "CREATE_FIRST_OWNER_WITH_SETUP_CODE"):
            a.Accounts(empty).local_create("someone", "admin", PASS)

    def test_temporary_reset_and_disable_for_non_admin(self):
        self.acc.local_create("helper", "viewer", PASS)
        token = self.acc.login("helper", PASS)
        self.acc.local_set_password("helper", NEW, temporary=True)
        self.assertIsNone(self.acc.session(token))
        self.assertTrue(self.acc.session(self.acc.login("helper", NEW))["mustChangePassword"])
        self.acc.local_update("helper", enabled=False)
        with self.assertRaises(a.AccessError):
            self.acc.login("helper", NEW)

    def test_second_admin_allows_demoting_first(self):
        self.acc.local_create("second", "admin", PASS)
        self.acc.local_set_password("second", NEW)  # permanent
        self.acc.local_update("owner", role="viewer")
        self.assertEqual({u["username"]: u["role"] for u in self.acc.local_users()}, {"owner": "viewer", "second": "admin"})

    def test_unlock_clears_lockout(self):
        for _ in range(5):
            with self.assertRaises(a.AccessError):
                self.acc.login("owner", "wrong password here")
        with self.assertRaisesRegex(a.AccessError, "SIGN_IN_TEMPORARILY_LIMITED"):
            self.acc.login("owner", PASS)
        self.assertGreater(self.acc.local_unlock()["cleared"], 0)
        self.assertTrue(self.acc.login("owner", PASS))

    def test_password_set_clears_that_users_lockout(self):
        for _ in range(5):
            with self.assertRaises(a.AccessError):
                self.acc.login("owner", "wrong password here")
        self.acc.local_set_password("owner", NEW)
        self.assertTrue(self.acc.login("owner", NEW))

    def test_revoke_all_sessions(self):
        self.assertEqual(self.acc.local_revoke_sessions()["revoked"], 1)
        self.assertIsNone(self.acc.session(self.owner_token))

    def test_audit_is_attributed_and_secret_free(self):
        self.acc.local_set_password("owner", NEW)
        events = self.acc.local_audit(10)
        self.assertEqual((events[0]["actor"], events[0]["action"]), ("local-console", "local_password_set"))
        raw = json.dumps(events) + self.acc.path.read_bytes().decode("latin-1")
        self.assertNotIn(NEW, raw); self.assertNotIn(PASS, raw)


class WorkspaceConfigTests(Base):
    def test_missing_file_means_unconfigured(self):
        self.assertEqual(wc.load(self.config), {})

    def test_roundtrip_is_private(self):
        saved = wc.save({"kfm_root": str(self.home / "w"), "inbox": str(self.home / "in")}, self.config)
        self.assertEqual(wc.load(self.config), saved)
        self.assertEqual(self.config.stat().st_mode & 0o777, 0o600)
        self.assertEqual(self.config.parent.stat().st_mode & 0o777, 0o700)

    def test_invalid_values_rejected(self):
        for values in ({"kfm_root": "relative/path"}, {"kfm_root": "/a/../b"}, {"surprise": "/x"},
                       {"qwen_model": "qwen"}, {"kfm_root": "/ok\n--evil"}, {"archive_root": "/a"},
                       {"qwen_model": "bad model;rm", "qwen_digest": "sha256:1"}):
            with self.subTest(values=values), self.assertRaises(wc.ConfigError):
                wc.normalize(values)

    def test_unsafe_file_refused(self):
        wc.save({"kfm_root": "/tmp/x"}, self.config)
        self.config.chmod(0o644)
        with self.assertRaises(wc.ConfigError):
            wc.load(self.config)
        self.config.chmod(0o600)
        link = self.config.with_name("link.json"); link.symlink_to(self.config)
        with self.assertRaises(wc.ConfigError):
            wc.load(link)

    def test_server_args_fixed_order(self):
        values = {"inbox": "/in", "kfm_root": "/w", "qwen_digest": "sha256:ab", "qwen_model": "qwen3:8b"}
        self.assertEqual(wc.server_args(values),
                         ["--kfm-root", "/w", "--inbox", "/in", "--qwen-model", "qwen3:8b", "--qwen-digest", "sha256:ab"])

    def test_problems_detect_missing_and_uninitialized_store(self):
        plain = self.home / "plain"; plain.mkdir(mode=0o700)
        issues = wc.problems({"kfm_root": str(plain), "inbox": str(self.home / "missing")})
        self.assertTrue(any("not an initialized KFM data store" in i for i in issues))
        self.assertTrue(any("inbox: folder not found" in i for i in issues))
        store = self.home / "working"; manage.init_store(manage.external_root(str(store)))
        self.assertEqual(wc.problems({"kfm_root": str(store)}), [])


class CliTests(Base):
    def test_password_command_prompts_and_never_accepts_argument(self):
        code, out, _ = self.run_cli("password", "owner", secrets=[NEW, NEW])
        self.assertEqual(code, 0); self.assertIn("Password changed for owner", out)
        self.assertNotIn(NEW, out)
        self.assertTrue(self.acc.login("owner", NEW))
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            admin.parser().parse_args(["password", "owner", NEW])

    def test_password_retries_on_weak_or_mismatch_then_gives_up(self):
        code, out, err = self.run_cli("password", "owner", secrets=["short", NEW, "different value!!!", "x" * 3])
        self.assertEqual(code, 1); self.assertIn("at least 15 characters", out); self.assertIn("did not match", out)
        self.assertTrue(self.acc.login("owner", PASS))

    def test_password_refused_without_terminal(self):
        with patch.object(admin.sys.stdin, "isatty", lambda: False), contextlib.redirect_stderr(io.StringIO()) as err:
            code = admin.main(["--store", str(self.store), "password", "owner"])
        self.assertEqual(code, 1); self.assertIn("interactive terminal", err.getvalue())

    def test_unknown_user_and_friendly_last_admin_error(self):
        code, _, err = self.run_cli("password", "nobody")
        self.assertEqual(code, 1); self.assertIn("No Studio account", err)
        code, _, err = self.run_cli("disable", "owner")
        self.assertEqual(code, 1); self.assertIn("no active administrator", err)

    def test_add_user_users_and_role(self):
        self.assertEqual(self.run_cli("add-user", "helper", "--role", "operator", secrets=[PASS, PASS])[0], 0)
        self.assertEqual(self.run_cli("role", "helper", "viewer")[0], 0)
        code, out, _ = self.run_cli("users")
        self.assertIn("helper", out); self.assertIn("viewer", out); self.assertIn("temporary", out)

    def test_workspace_init_connects_new_store(self):
        target = self.home / "KFM-pipeline"
        code, out, err = self.run_cli("workspace", "init", str(target))
        self.assertEqual(code, 0, err); self.assertIn("Initialized new", out)
        self.assertEqual(wc.load(self.config), {"kfm_root": str(target)})
        self.assertTrue(manage.initialized(target))

    def test_workspace_set_refuses_unusable_path(self):
        code, _, err = self.run_cli("workspace", "set", "kfm_root", str(self.home / "missing"))
        self.assertEqual(code, 1); self.assertIn("folder not found", err)
        self.assertFalse(self.config.exists())

    def test_guided_setup_creates_store_and_optional_inbox(self):
        target = self.home / "pipeline"; inbox = self.home / "Downloads"; inbox.mkdir()
        code, out, err = self.run_cli("workspace", "setup", answers=[str(target), "y", "", "", str(inbox)])
        self.assertEqual(code, 0, err)
        self.assertEqual(wc.load(self.config), {"kfm_root": str(target), "inbox": str(inbox)})

    def test_status_reports_unconnected_workspace(self):
        code, out, _ = self.run_cli("status")
        self.assertEqual(code, 0); self.assertIn("owner", out); self.assertIn("Nothing connected", out)

    def test_unlock_and_sign_out_all(self):
        self.assertIn("Signed out 1", self.run_cli("sign-out-all")[1])
        self.assertIn("Sign-in limits cleared", self.run_cli("unlock")[1])
        self.assertIn("local_all_sessions_revoked", self.run_cli("audit")[1])

    def test_stop_ignores_unrelated_pid(self):
        state = self.home / "state"; state.mkdir()
        (state / "server.pid").write_text(str(os.getpid()))  # this test process, not Studio
        with patch.object(admin, "STATE", state):
            self.assertIsNone(admin.server_pid())
            code, out, _ = self.run_cli("stop")
        self.assertEqual(code, 0); self.assertIn("not running", out)


class LauncherTests(Base):
    def test_launcher_refuses_unusable_workspace_before_starting(self):
        from tools.local_data.intake_studio import launch_local
        wc.save({"kfm_root": str(self.home / "missing")}, self.config)
        with patch.object(wc, "CONFIG", self.config), patch.dict(os.environ, {"HOME": str(self.home)}), \
             patch.object(launch_local.subprocess, "Popen") as popen:
            with self.assertRaises(SystemExit) as stopped:
                launch_local.main()
        self.assertIn("folder not found", str(stopped.exception))
        popen.assert_not_called()

    def test_launcher_passes_saved_roots_to_server(self):
        from tools.local_data.intake_studio import launch_local
        target = self.home / "working"; manage.init_store(manage.external_root(str(target)))
        wc.save({"kfm_root": str(target)}, self.config)
        calls = []
        class Proc:
            pid = 4242
            def poll(self): return None
        def fake_popen(argv, **_):
            calls.append(argv); return Proc()
        states = iter([None, {"app": "kfm-local-intake-studio", "sourceFingerprint": "fp", "authentication": "local-accounts-required"}])
        with patch.object(wc, "CONFIG", self.config), patch.dict(os.environ, {"HOME": str(self.home)}), \
             patch.object(launch_local, "source_fingerprint", lambda: "fp"), \
             patch.object(launch_local, "running", lambda: next(states)), \
             patch.object(launch_local.subprocess, "Popen", side_effect=fake_popen), \
             patch.object(launch_local.sys, "argv", ["launch_local.py", "--no-open"]), \
             patch.object(launch_local.sys.stdout, "isatty", lambda: False), \
             contextlib.redirect_stdout(io.StringIO()):
            launch_local.main()
        self.assertEqual(calls[0][1:], [str(Path(launch_local.APP) / "private_server.py"), "--kfm-root", str(target)])


if __name__ == "__main__":
    unittest.main()
