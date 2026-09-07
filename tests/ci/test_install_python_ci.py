from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/ci/install_python_ci.py"
SPEC = importlib.util.spec_from_file_location("kfm_install_python_ci", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class InstallPythonCiTests(unittest.TestCase):
    def test_all_profiles_use_hashes_and_disable_local_resolution(self) -> None:
        self.assertEqual(
            {
                "all-local-test",
                "audit-tool",
                "connectors-core",
                "geoparquet-pyarrow-25",
                "project-runtime",
                "project-test",
                "project-test-hashing",
                "project-test-hashing-test",
                "project-test-schema-registry-test",
                "project-test-wheel",
                "test-dependencies",
            },
            set(module.PROFILES),
        )
        for name, profile in module.PROFILES.items():
            with self.subTest(profile=name):
                commands = module.build_commands(name, executable="python")
                self.assertIn("--require-hashes", commands[0])
                self.assertIn("--requirement", commands[0])
                if profile.local_specs:
                    self.assertEqual(2, len(commands))
                    self.assertIn("--no-deps", commands[1])
                    self.assertIn("--no-build-isolation", commands[1])
                else:
                    self.assertEqual(1, len(commands))

    def test_committed_locks_pin_direct_dependencies(self) -> None:
        test_lock = (REPO_ROOT / "tools/ci/python-test.lock").read_text(
            encoding="utf-8"
        )
        for name in (
            "editables",
            "hatchling",
            "hypothesis",
            "jsonschema",
            "pyyaml",
            "pytest",
            "referencing",
            "rfc3339-validator",
            "rfc8785",
        ):
            self.assertIn(f"{name}==", test_lock.lower())
        audit_lock = (REPO_ROOT / "tools/ci/python-audit.lock").read_text(
            encoding="utf-8"
        )
        self.assertIn("pip-audit==2.10.1", audit_lock.lower())
        geoparquet_lock = (
            REPO_ROOT / "tools/ci/geoparquet-pyarrow-25.lock"
        ).read_text(encoding="utf-8")
        self.assertIn("pyarrow==25.0.0", geoparquet_lock.lower())

    def test_migration_manifest_is_finite_and_exact(self) -> None:
        manifest, entries = module.load_workflow_migration_manifest(REPO_ROOT)
        self.assertEqual(module.MIGRATION_SCHEMA, manifest["schema_version"])
        self.assertEqual(module.MIGRATION_ID, manifest["migration_id"])
        self.assertEqual(module.MIGRATION_ENTRY_COUNT, len(entries))
        self.assertEqual(sorted(entries), list(entries))

    def test_migration_hash_failure_reports_every_mismatched_workflow(self) -> None:
        manifest, entries = module.load_workflow_migration_manifest(REPO_ROOT)
        migration_head = module.subprocess.run(
            ("git", "rev-parse", "HEAD"),
            check=True,
            cwd=REPO_ROOT,
            stdout=module.subprocess.PIPE,
            text=True,
        ).stdout.strip()
        paths = tuple(entries)[:2]
        mismatched_entries = {
            path: {**entries[path], "current_sha256": "sha256:" + "0" * 64}
            for path in paths
        }

        with (
            mock.patch.object(
                module,
                "load_workflow_migration_manifest",
                return_value=(manifest, mismatched_entries),
            ),
            mock.patch.dict(
                module.os.environ,
                {"KFM_MIGRATION_HEAD": migration_head},
            ),
            self.assertRaises(module.InstallConfigurationError) as raised,
        ):
            module.verify_workflow_receipts()

        self.assertEqual(
            "MIGRATION_CURRENT_HASH_MISMATCH:" + ",".join(paths),
            str(raised.exception),
        )

    def test_migration_validation_checks_each_reused_profile_once(self) -> None:
        manifest, entries = module.load_workflow_migration_manifest(REPO_ROOT)
        migration_head = module.subprocess.run(
            ("git", "rev-parse", "HEAD"),
            check=True,
            cwd=REPO_ROOT,
            stdout=module.subprocess.PIPE,
            text=True,
        ).stdout.strip()
        paths = tuple(
            path
            for path, entry in entries.items()
            if entry["profiles"] == ["project-test"]
        )[:2]
        self.assertEqual(2, len(paths))
        repeated_profile_entries = {
            path: {
                **entries[path],
                "current_sha256": module._sha256_bytes(
                    (REPO_ROOT / path).read_bytes()
                ),
            }
            for path in paths
        }

        with (
            mock.patch.object(
                module,
                "load_workflow_migration_manifest",
                return_value=(manifest, repeated_profile_entries),
            ),
            mock.patch.dict(
                module.os.environ,
                {"KFM_MIGRATION_HEAD": migration_head},
            ),
            mock.patch.object(module, "validate_lockfile") as validate_lockfile,
            mock.patch.object(module, "_validate_local_specs") as validate_local_specs,
        ):
            module.verify_workflow_receipts()

        validate_lockfile.assert_called_once()
        validate_local_specs.assert_called_once_with(module.PROFILES["project-test"])

    def test_migration_validation_reads_exact_commits_in_two_batches(self) -> None:
        manifest, entries = module.load_workflow_migration_manifest(REPO_ROOT)
        migration_head = module.subprocess.run(
            ("git", "rev-parse", "HEAD"),
            check=True,
            cwd=REPO_ROOT,
            stdout=module.subprocess.PIPE,
            text=True,
        ).stdout.strip()
        paths = tuple(entries)[:2]
        selected_entries = {path: entries[path] for path in paths}
        base_workflows = {
            path: module.subprocess.run(
                ("git", "show", f'{manifest["base_commit"]}:{path}'),
                check=True,
                cwd=REPO_ROOT,
                stdout=module.subprocess.PIPE,
            ).stdout
            for path in paths
        }
        head_workflows = {path: (REPO_ROOT / path).read_bytes() for path in paths}
        selected_entries = {
            path: {
                **selected_entries[path],
                "current_sha256": module._sha256_bytes(head_workflows[path]),
            }
            for path in paths
        }

        with (
            mock.patch.object(
                module,
                "load_workflow_migration_manifest",
                return_value=(manifest, selected_entries),
            ),
            mock.patch.dict(
                module.os.environ,
                {"KFM_MIGRATION_HEAD": migration_head},
            ),
            mock.patch.object(
                module,
                "_read_commit_workflows",
                side_effect=(base_workflows, head_workflows),
            ) as read_commit_workflows,
            mock.patch.object(module, "profiles_for_workflow") as path_parser,
        ):
            module.verify_workflow_receipts()

        self.assertEqual(
            [
                mock.call(manifest["base_commit"], paths),
                mock.call(migration_head, paths),
            ],
            read_commit_workflows.call_args_list,
        )
        path_parser.assert_not_called()

    def test_commit_workflow_batch_reader_preserves_blob_boundaries(self) -> None:
        paths = (".github/workflows/a.yml", ".github/workflows/b.yaml")
        blobs = (b"name: a\n\n", b"name: b\nrun: value")
        output = b"".join(
            b"0" * 40
            + b" blob "
            + str(len(blob)).encode("ascii")
            + b"\n"
            + blob
            + b"\n"
            for blob in blobs
        )
        completed = module.subprocess.CompletedProcess(
            args=("git", "cat-file", "--batch"), returncode=0, stdout=output
        )

        with mock.patch.object(module.subprocess, "run", return_value=completed) as run:
            self.assertEqual(
                dict(zip(paths, blobs, strict=True)),
                module._read_commit_workflows("1" * 40, paths),
            )

        self.assertEqual(
            (
                "1" * 40
                + ":"
                + paths[0]
                + "\n"
                + "1" * 40
                + ":"
                + paths[1]
                + "\n"
            ).encode("ascii"),
            run.call_args.kwargs["input"],
        )
        self.assertEqual(30, run.call_args.kwargs["timeout"])

    def test_commit_workflow_batch_reader_rejects_missing_blob(self) -> None:
        completed = module.subprocess.CompletedProcess(
            args=("git", "cat-file", "--batch"),
            returncode=0,
            stdout=b"1" * 40 + b":.github/workflows/missing.yml missing\n",
        )
        with (
            mock.patch.object(module.subprocess, "run", return_value=completed),
            self.assertRaisesRegex(
                module.InstallConfigurationError,
                "MIGRATION_GIT_OUTPUT_INVALID",
            ),
        ):
            module._read_commit_workflows(
                "1" * 40, (".github/workflows/missing.yml",)
            )

    def test_lock_validation_rejects_unhashed_and_remote_sources(self) -> None:
        remote = (
            "thing @ https://example.invalid/thing.whl "
            + "\\\n    --hash=sha256:"
            + "a" * 64
            + "\n"
        )
        for content in ("pytest==9.1.1\n", remote):
            with (
                self.subTest(content=content),
                tempfile.TemporaryDirectory() as temp,
            ):
                path = Path(temp) / "unsafe.lock"
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(module.InstallConfigurationError):
                    module.validate_lockfile(path)

    def test_install_executes_argument_vectors_without_a_shell(self) -> None:
        with mock.patch.object(module.subprocess, "run") as run:
            module.install("project-test")
        self.assertEqual(2, run.call_count)
        for call in run.call_args_list:
            self.assertIsInstance(call.args[0], tuple)
            self.assertIs(call.kwargs["shell"], False)
            self.assertIs(call.kwargs["check"], True)
            self.assertEqual(REPO_ROOT, call.kwargs["cwd"])

    def test_workflows_do_not_install_python_dependencies_directly(self) -> None:
        workflows = sorted(
            path
            for pattern in ("*.yml", "*.yaml")
            for path in (REPO_ROOT / ".github/workflows").glob(pattern)
        )
        offenders = [
            workflow.relative_to(REPO_ROOT).as_posix()
            for workflow in workflows
            if "python -m pip install" in workflow.read_text(encoding="utf-8")
        ]
        self.assertEqual([], offenders)

    def test_each_migrated_workflow_selects_one_known_profile(self) -> None:
        counts: dict[str, int] = {}
        for workflow in sorted((REPO_ROOT / ".github/workflows").glob("*.yml")):
            for profile in module.profiles_for_workflow(workflow):
                counts[profile] = counts.get(profile, 0) + 1
        self.assertGreaterEqual(sum(counts.values()), 388)
        self.assertEqual(1, counts["audit-tool"])
        self.assertEqual(1, counts["all-local-test"])
        self.assertEqual(2, counts["geoparquet-pyarrow-25"])

    def test_workflow_profile_parser_accepts_logging_pipeline(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix=".install-python-profile-",
            dir=REPO_ROOT / ".github/workflows",
        ) as directory:
            workflow = Path(directory) / "profile.yml"
            workflow.write_text(
                "python tools/ci/install_python_ci.py project-test "
                '2>&1 | tee "$RUNNER_TEMP/python-bootstrap.log"\n',
                encoding="utf-8",
            )

            self.assertEqual(
                frozenset({"project-test"}),
                module.profiles_for_workflow(workflow),
            )

    def test_workflow_profile_parser_requires_executable_command_position(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix=".install-python-profile-",
            dir=REPO_ROOT / ".github/workflows",
        ) as directory:
            workflow = Path(directory) / "profile.yml"
            for prefix in ("", "run: ", "- run: "):
                with self.subTest(prefix=prefix):
                    workflow.write_text(
                        f"{prefix}python tools/ci/install_python_ci.py project-test\n",
                        encoding="utf-8",
                    )
                    self.assertEqual(
                        frozenset({"project-test"}),
                        module.profiles_for_workflow(workflow),
                    )

            workflow.write_text(
                "# python tools/ci/install_python_ci.py project-test\n",
                encoding="utf-8",
            )
            self.assertEqual(frozenset(), module.profiles_for_workflow(workflow))

            for prefix in ('run: echo "', "timeout 30 "):
                with self.subTest(rejected_prefix=prefix):
                    workflow.write_text(
                        f"{prefix}python tools/ci/install_python_ci.py project-test\n",
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(
                        module.InstallConfigurationError,
                        "WORKFLOW_PROFILE_INVOCATION_INVALID",
                    ):
                        module.profiles_for_workflow(workflow)

    def test_workflow_profile_parser_rejects_unsupported_trailing_tokens(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix=".install-python-profile-",
            dir=REPO_ROOT / ".github/workflows",
        ) as directory:
            workflow = Path(directory) / "profile.yml"
            for invocation in (
                "project-test typo",
                "project-test audit-tool",
                "project-test 2>&1",
                'project-test 2>&1 | tee "$RUNNER_TEMP/python-bootstrap.log" trailing',
                'project-test | tee "$RUNNER_TEMP/python-bootstrap.log"',
            ):
                with self.subTest(invocation=invocation):
                    workflow.write_text(
                        f"python tools/ci/install_python_ci.py {invocation}\n",
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(
                        module.InstallConfigurationError,
                        "PROFILE_UNKNOWN",
                    ):
                        module.profiles_for_workflow(workflow)

    def test_workflow_profile_parser_rejects_noncanonical_logging_paths(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix=".install-python-profile-",
            dir=REPO_ROOT / ".github/workflows",
        ) as directory:
            workflow = Path(directory) / "profile.yml"
            for log_path in (
                "../workspace-file",
                "nested/../../workspace-file",
                "./python-bootstrap.log",
                "nested/./python-bootstrap.log",
                "/absolute-looking.log",
                "nested//python-bootstrap.log",
                "nested/",
            ):
                with self.subTest(log_path=log_path):
                    workflow.write_text(
                        "python tools/ci/install_python_ci.py project-test "
                        f'2>&1 | tee "$RUNNER_TEMP/{log_path}"\n',
                        encoding="utf-8",
                    )
                    with self.assertRaisesRegex(
                        module.InstallConfigurationError,
                        "PROFILE_UNKNOWN",
                    ):
                        module.profiles_for_workflow(workflow)

    def test_workflow_profile_parser_rejects_unknown_pipelined_profile(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix=".install-python-profile-",
            dir=REPO_ROOT / ".github/workflows",
        ) as directory:
            workflow = Path(directory) / "profile.yml"
            workflow.write_text(
                "python tools/ci/install_python_ci.py project-tests "
                '2>&1 | tee "$RUNNER_TEMP/python-bootstrap.log"\n',
                encoding="utf-8",
            )

            with self.assertRaisesRegex(
                module.InstallConfigurationError,
                "PROFILE_UNKNOWN",
            ):
                module.profiles_for_workflow(workflow)


if __name__ == "__main__":
    unittest.main()
