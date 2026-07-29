from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

import pytest

from tools.validators.ci_readiness import (
    classify_test_source,
    classify_validator_source,
    inspect_readiness,
    render_report,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPOSITORY_ROOT / "tools/validators/ci_readiness.py"


def _write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _placeholder_roots(repository: Path) -> tuple[Path, Path]:
    test_root = repository / "tests/domain"
    validator_root = repository / "tools/validators/domain"
    _write(test_root / "comment_only.py", "# placeholder\n")
    _write(test_root / "doc_only.py", '"""Placeholder tests."""\n')
    _write(
        test_root / "test_smoke.py",
        '"""Placeholder smoke test."""\n\n'
        "def test_placeholder():\n"
        "    assert True\n",
    )
    _write(validator_root / "comment_only.py", "# placeholder\n")
    _write(validator_root / "doc_only.py", '"""Placeholder validator."""\n')
    _write(
        validator_root / "validate_stub.py",
        "def main():\n"
        "    raise NotImplementedError\n",
    )
    _write(
        validator_root / "validate_message_stub.py",
        '"""Placeholder validator."""\n\n'
        "def main():\n"
        '    raise NotImplementedError("not implemented")\n',
    )
    return test_root, validator_root


def test_allowed_placeholder_forms_are_non_vacuous(tmp_path: Path) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)

    report = inspect_readiness(
        label="Example",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert report.ok
    assert len(report.test_files) == 3
    assert len(report.validator_files) == 4
    assert render_report(report) == (
        "WORKFLOW_SKIPPED_EXPLICIT: Example",
        "WORKFLOW_HOLD: Example readiness is placeholder-only; tests=3; validators=4",
    )


def test_readme_only_sibling_roots_are_allowed_with_category_non_vacuity(
    tmp_path: Path,
) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    empty_test_root = tmp_path / "tests/documented-only"
    empty_validator_root = tmp_path / "tools/validators/documented-only"
    _write(empty_test_root / "README.md", "# Documented test lane\n")
    _write(empty_test_root / "LICENSE", "Example license text.\n")
    _write(empty_test_root / "NOTES.rst", "Documented test notes.\n")
    _write(empty_test_root / ".gitkeep", "")
    _write(empty_test_root / "EMPTY_SENTINEL", " \n\t")
    _write(empty_validator_root / "README.md", "# Documented validator lane\n")
    _write(empty_validator_root / "README", "Documented validator lane.\n")
    _write(empty_validator_root / "LICENSE", "Example license text.\n")
    _write(empty_validator_root / "NOTICE", "Example notice text.\n")
    _write(empty_validator_root / "NOTES.rst", "Documented validator notes.\n")
    _write(empty_validator_root / "design.markdown", "Documented design notes.\n")
    _write(empty_validator_root / "notes.txt", "Documented validator notes.\n")
    _write(empty_validator_root / ".gitkeep", "")
    _write(empty_validator_root / "EMPTY_SENTINEL", " \n\t")

    report = inspect_readiness(
        label="Repeated roots",
        test_roots=[empty_test_root, test_root],
        validator_roots=[empty_validator_root, validator_root],
        repository_root=tmp_path,
    )

    assert report.ok
    assert len(report.test_files) == 3
    assert len(report.validator_files) == 4


@pytest.mark.parametrize(
    "relative_path",
    (
        "test.sh",
        "test.bash",
        "test.js",
        "test.mjs",
        "test.cjs",
        "test.ts",
        "test.tsx",
        "executable",
        "policy/rules.rego",
        "schemas/test.schema.json",
    ),
)
def test_unexpected_test_sources_are_rejected(
    tmp_path: Path,
    relative_path: str,
) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    unexpected = _write(
        test_root / relative_path,
        "substantive test source\n",
    )

    report = inspect_readiness(
        label="Unexpected test source",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert not report.ok
    assert [(item.path, item.reason) for item in report.findings] == [
        (
            unexpected.relative_to(tmp_path).as_posix(),
            "unexpected_test_source",
        )
    ]


@pytest.mark.parametrize(
    "relative_path",
    (
        "validate.sh",
        "validate.bash",
        "validate.js",
        "validate.mjs",
        "validate.cjs",
        "validate.ts",
        "validate.tsx",
        "validate",
        "policy/rules.rego",
        "schemas/validator.schema.json",
    ),
)
def test_unexpected_validator_sources_are_rejected(
    tmp_path: Path,
    relative_path: str,
) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    unexpected = _write(
        validator_root / relative_path,
        "substantive validator source\n",
    )

    report = inspect_readiness(
        label="Unexpected validator source",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert not report.ok
    assert [(item.path, item.reason) for item in report.findings] == [
        (
            unexpected.relative_to(tmp_path).as_posix(),
            "unexpected_validator_source",
        )
    ]


@pytest.mark.parametrize(
    "source",
    (
        "def test_real():\n    assert True\n",
        "def test_placeholder():\n    pass\n",
        "import helper\n\ndef test_placeholder():\n    assert True\n",
        "@decorator\ndef test_placeholder():\n    assert True\n",
        "def test_placeholder():\n    assert True\n\ndef helper():\n    pass\n",
    ),
)
def test_substantive_test_forms_are_rejected(source: str) -> None:
    classification = classify_test_source(source)
    assert not classification.placeholder
    assert classification.reason == "substantive_test_module"


@pytest.mark.parametrize(
    "source",
    (
        "def main():\n    pass\n",
        "import helper\n\ndef main():\n    raise NotImplementedError\n",
        "@decorator\ndef main():\n    raise NotImplementedError\n",
        "def main():\n    raise helper()\n",
        "def main():\n    raise NotImplementedError()\n",
        "def main():\n    raise NotImplementedError\n\ndef helper():\n    pass\n",
    ),
)
def test_substantive_validator_forms_are_rejected(source: str) -> None:
    classification = classify_validator_source(source)
    assert not classification.placeholder
    assert classification.reason == "substantive_validator_module"


def test_substantive_files_report_paths_and_reasons(tmp_path: Path) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    _write(test_root / "test_real.py", "def test_real():\n    assert 2 + 2 == 4\n")
    _write(validator_root / "validate_real.py", "def main():\n    return 0\n")

    report = inspect_readiness(
        label="Example",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert not report.ok
    assert [(item.path, item.reason) for item in report.findings] == [
        ("tests/domain/test_real.py", "substantive_test_module"),
        (
            "tools/validators/domain/validate_real.py",
            "substantive_validator_module",
        ),
    ]


def test_syntax_failure_is_fail_closed(tmp_path: Path) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    _write(test_root / "test_broken.py", "def test_broken(:\n")

    report = inspect_readiness(
        label="Syntax",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    finding = next(item for item in report.findings if item.reason == "syntax_error")
    assert finding.path == "tests/domain/test_broken.py"
    assert "line 1" in finding.detail
    assert not report.ok


def test_missing_root_is_fail_closed(tmp_path: Path) -> None:
    _, validator_root = _placeholder_roots(tmp_path)

    report = inspect_readiness(
        label="Missing",
        test_roots=["tests/missing"],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert [(item.path, item.reason) for item in report.findings] == [
        ("tests/missing", "missing_root")
    ]
    assert not report.ok


def test_empty_roots_cannot_pass_vacuously(tmp_path: Path) -> None:
    test_root = tmp_path / "tests/empty"
    validator_root = tmp_path / "tools/validators/empty"
    test_root.mkdir(parents=True)
    validator_root.mkdir(parents=True)

    report = inspect_readiness(
        label="Empty",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert [item.reason for item in report.findings] == [
        "no_python_files",
        "no_python_files",
    ]
    assert not report.test_files
    assert not report.validator_files
    assert not report.ok


def test_importable_api_requires_both_root_categories(tmp_path: Path) -> None:
    report = inspect_readiness(
        label="No roots",
        test_roots=[],
        validator_roots=[],
        repository_root=tmp_path,
    )

    assert [item.reason for item in report.findings] == [
        "missing_root_argument",
        "missing_root_argument",
    ]
    assert not report.ok


def test_symlink_and_path_escape_are_fail_closed(tmp_path: Path) -> None:
    repository = tmp_path / "repository"
    outside = tmp_path / "outside"
    test_root, validator_root = _placeholder_roots(repository)
    escaped_file = _write(outside / "escaped.py", "# outside\n")
    os.symlink(escaped_file, test_root / "escaped.py")

    symlink_report = inspect_readiness(
        label="Symlink",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=repository,
    )
    escape_report = inspect_readiness(
        label="Escape",
        test_roots=[outside],
        validator_roots=[validator_root],
        repository_root=repository,
    )

    assert any(
        item.path == "tests/domain/escaped.py"
        and item.reason == "symlink_not_allowed"
        for item in symlink_report.findings
    )
    assert any(item.reason == "path_escape" for item in escape_report.findings)
    assert not symlink_report.ok
    assert not escape_report.ok


def test_diagnostics_are_deterministic_and_sorted(tmp_path: Path) -> None:
    first_test = tmp_path / "tests/z"
    second_test = tmp_path / "tests/a"
    validator_root = tmp_path / "tools/validators/domain"
    _write(first_test / "test_z.py", "def test_z():\n    assert True\n")
    _write(second_test / "test_a.py", "def test_a():\n    assert True\n")
    _write(validator_root / "placeholder.py", "# placeholder\n")

    first = inspect_readiness(
        label="Deterministic",
        test_roots=[first_test, second_test],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )
    second = inspect_readiness(
        label="Deterministic",
        test_roots=[second_test, first_test],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )

    assert first == second
    assert [item.path for item in first.findings] == [
        "tests/a/test_a.py",
        "tests/z/test_z.py",
    ]
    assert render_report(first) == render_report(second)


def test_cli_exit_polarity_and_summary(tmp_path: Path) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    test_sibling = tmp_path / "tests/documented-only"
    validator_sibling = tmp_path / "tools/validators/documented-only"
    _write(test_sibling / "README.md", "# Test lane\n")
    _write(validator_sibling / "README.md", "# Validator lane\n")
    command = [
        sys.executable,
        str(SCRIPT),
        "--label",
        "CLI Example",
        "--test-root",
        str(test_root.relative_to(tmp_path)),
        "--test-root",
        str(test_sibling.relative_to(tmp_path)),
        "--validator-root",
        str(validator_root.relative_to(tmp_path)),
        "--validator-root",
        str(validator_sibling.relative_to(tmp_path)),
    ]

    allowed = subprocess.run(
        command,
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )
    _write(test_root / "test_real.py", "def test_real():\n    assert True\n")
    denied = subprocess.run(
        command,
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )

    assert allowed.returncode == 0
    assert allowed.stderr == ""
    assert allowed.stdout.splitlines() == [
        "WORKFLOW_SKIPPED_EXPLICIT: CLI Example",
        "WORKFLOW_HOLD: CLI Example readiness is placeholder-only; tests=3; validators=4",
    ]
    assert denied.returncode == 1
    assert "substantive_test_module: tests/domain/test_real.py" in denied.stdout
    assert denied.stdout.splitlines()[-1].startswith("WORKFLOW_HOLD:")


def test_cli_diagnostics_are_bounded(tmp_path: Path) -> None:
    test_root, validator_root = _placeholder_roots(tmp_path)
    for index in range(55):
        _write(
            test_root / f"test_real_{index:02d}.py",
            f"def test_real_{index:02d}():\n    assert True\n",
        )

    report = inspect_readiness(
        label="Bounded",
        test_roots=[test_root],
        validator_roots=[validator_root],
        repository_root=tmp_path,
    )
    rendered = render_report(report)

    assert len(report.findings) == 55
    assert sum(line.startswith("CI_READINESS_REASON:") for line in rendered) == 50
    assert "CI_READINESS_OMITTED: 5" in rendered
