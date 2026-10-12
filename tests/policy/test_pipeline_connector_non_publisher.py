from __future__ import annotations

from pathlib import Path

from tools.validators.connector_gate.output_paths import (
    iter_connector_source_files,
    legacy_publish_target_violations,
    scan_connector_file,
    scan_python_source,
    scan_shell_source,
    scan_yaml_source,
)


def test_connector_allowlist_and_pipeline_non_publisher_boundaries(tmp_path: Path) -> None:
    repository_root = Path(__file__).resolve().parents[2]

    positive_python = (
        'from pathlib import Path\nPath("data/raw/item.json").write_bytes(payload)',
        'from pathlib import Path\nPath("data/raw/item.json").open("wb")',
        'from pathlib import Path\nPath("data/quarantine/item.json").open(mode="w")',
        'open("data/quarantine/item.json", "wb")',
        'from pathlib import Path\nPath("data/receipts/connectors/run.json").write_text(receipt)',
        'from pathlib import Path\n(Path("data") / "raw" / "item.json").write_text("x")',
        'from pathlib import Path\nroot = Path("data")\ntarget = root / "raw" / "local.json"\ntarget.write_text("x")',
        'open("data/catalog/item.json", "rb")',
        '# Path("data/published/item.json").write_text("not executed")',
        '"""open("release/item.json", "w") is documentation only"""',
        'from pathlib import Path\nPath("/tmp/connector-item.json").write_text("external")',
        'import json, sys\njson.dump({}, sys.stdout)',
        'import json, io\njson.dump({}, io.StringIO())',
        'archive.open("data/published/item.json", "w")',
        'from builtins import open as file_open\nfile_open("data/raw/x", "w")',
        'from builtins import open as file_open\nfile_open = helper\nfile_open("data/published/x", "w")',
        'from pathlib import Path\nif enabled:\n    target = Path("data/raw/x")\nelse:\n    target = Path("data/quarantine/x")\ntarget.write_text("x")',
        'import builtins\nbuiltins = helper\nbuiltins.open("data/published/x", "w")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\ntry:\n    target = Path("data/published/x")\n    target = Path("data/raw/x")\nexcept Error:\n    target = Path("data/raw/x")\ntarget.open("w")',
    )
    for case_number, source in enumerate(positive_python, start=1):
        assert not scan_python_source(
            source,
            source=f"positive-python-{case_number}.py",
            repository_root=repository_root,
        )

    forbidden_targets = (
        "data/pre_raw/item.json",
        "data/work/item.json",
        "data/processed/item.json",
        "data/catalog/item.json",
        "data/triplet/item.json",
        "data/triplets/item.json",
        "data/triplet(s)/item.json",
        "data/proofs/item.json",
        "data/registry/item.json",
        "data/published/item.json",
        "release/item.json",
        "artifacts/item.json",
    )
    for target in forbidden_targets:
        violations = scan_python_source(
            f'from pathlib import Path\nPath("{target}").write_text("x")',
            source=f"negative-{target}.py",
            repository_root=repository_root,
        )
        assert violations and all(
            "DIR-PLACE-003" in item.reason for item in violations
        ), target

    absolute_published = repository_root / "data/published/absolute.json"
    file_uri_published = absolute_published.as_uri()
    negative_python = [
        'from pathlib import Path\nPath("data/published/x").open("w")',
        'from pathlib import Path\nPath("data/published/x").open(mode="wb")',
        'open(file="data/work/x", mode="w")',
        'open(output_root, "w")',
        'from pathlib import Path\nPath(output_root).write_text("x")',
        'from pathlib import Path\n(Path("data") / "raw" / ".." / "published" / "x").write_text("x")',
        'from pathlib import Path\nroot = Path("data")\ntarget = root / "processed" / "x"\ntarget.write_bytes(b"x")',
        'TARGET = "data/raw/x"\ndef emit(TARGET):\n    open(TARGET, "w")',
        'TARGET = "data/raw/x"\nif enabled:\n    TARGET = "data/published/x"\nopen(TARGET, "w")',
        'open("data/published/x", "w")\nopen = helper',
        'from pathlib import Path\nif enabled:\n    target = Path("data/raw/x")\nelse:\n    target = Path("data/published/x")\ntarget.write_text("x")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\nfor item in values:\n    target = Path("data/published/x")\ntarget.open("w")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\nwhile enabled:\n    target = Path("data/published/x")\ntarget.touch()',
        'from pathlib import Path\ntarget = Path("data/raw/x")\ntry:\n    target = Path("data/published/x")\nexcept Error:\n    pass\ntarget.rename("data/published/moved")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\nmatch value:\n    case 1:\n        target = Path("data/published/x")\ntarget.write_bytes(b"x")',
        'from pathlib import Path\nTARGET = Path("data/raw/x")\nemit = lambda *, TARGET: TARGET.write_text("x")',
        'from pathlib import Path\nTARGET = Path("data/raw/x")\n[TARGET.write_text("x") for TARGET in [Path("data/published/x")]]',
        'from pathlib import Path\nPath("data/raw/x").open(mode=selected_mode)',
        'import subprocess\nsubprocess.run(command)',
        'import os\nos.system(command)',
        'import subprocess\nsubprocess.run(["cp", "source", "data/published/x"])',
        'import subprocess\nsubprocess.run(["bash", "-c", "cp source data/published/x"])',
        'import subprocess\nsubprocess.run(["sh", "-c", command])',
        'from subprocess import run as execute\nexecute(["cp", "source", destination])',
        'from shutil import copyfile as copy\ncopy("source", "release/x")',
        'import shutil as files\nfiles.move("source", "data/catalog/x")',
        'from pathlib import Path\nPath("source").rename("data/published/x")',
        'from pathlib import Path\nPath("data/published/x").resolve().write_text("x")',
        'from pathlib import Path\nPath("data/published/x/file").parent.mkdir()',
        'import os\nos.makedirs("data/processed/x")',
        f'open({str(absolute_published)!r}, "w")',
        f'open({file_uri_published!r}, "w")',
        'from pathlib import Path\nPath("s3://bucket/key").write_text("x")',
        'emit = open\nemit("data/published/x", "w")',
        'import builtins\nemit = helper\nif enabled:\n    emit = builtins.open\nemit("data/published/x", "w")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\nfor item in values:\n    target.write_text("x")\n    target = Path("data/published/x")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\nfor item in values:\n    target = Path("data/published/x")\nelse:\n    target.write_text("x")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\ntry:\n    target = Path("data/published/x")\n    raise Error\nexcept Error:\n    target.write_text("x")',
        'from pathlib import Path\n[T.open("w") for T in [Path("data/published/x")]]',
        'from pathlib import Path\n[T.rename("data/published/y") for T in [Path("data/raw/x")]]',
        'from pathlib import Path\nfor T in [Path("data/published/x")]:\n    T.open("w")',
        'from pathlib import Path\n(lambda T=Path("data/published/x"): T.open("w"))()',
        'f = lambda open=open: open("data/published/x", "w")',
        'from pathlib import Path\n(lambda Path=Path("data/published/x"): Path.open("w"))()',
        'from pathlib import Path\n(target := Path("data/published/x")).open("w")',
        '[emit("data/published/x", "w") for emit in [open]]',
        'def emit():\n    writer("data/published/x", "w")\nwriter = open',
        'from pathlib import Path\ndef emit():\n    target.open("w")\ntarget = Path("data/published/x")',
        'emit = open if enabled else helper\nemit("data/published/x", "w")',
        'from pathlib import Path\n(Path("data/published/x") if enabled else Path("data/raw/x")).open("w")',
        '(emit := open)("data/published/x", "w")',
        '[open("data/published/x", "w") for open in [open]]',
        'from pathlib import Path\n[Path.open("w") for Path in [Path("data/published/x")]]',
        '(emit,) = (open,)\nemit("data/published/x", "w")',
        '(open if enabled else helper)("data/published/x", "w")',
        'def emit():\n    writer("data/published/x", "w")\nwriter = open if enabled else helper',
        'from pathlib import Path\n(target,) = (Path("data/published/x"),)\ntarget.open("w")',
        'from pathlib import Path\ntarget = Path("data/raw/x")\ntarget = runtime_target\ndef emit():\n    target.open("w")',
        'emit = enabled and open\nemit("data/published/x", "w")',
        'from pathlib import Path\ntarget = enabled and Path("data/published/x")\ntarget.open("w")',
        'from pathlib import Path\n[T.open("w") for (T,) in [(Path("data/published/x"),)]]',
        '[emit("data/published/x", "w") for (emit,) in [(open,)]]',
    ]
    try:
        home_relative_repository = repository_root.relative_to(Path.home())
    except ValueError:
        pass
    else:
        tilde_published = f"~/{home_relative_repository}/data/published/tilde.json"
        negative_python.append(f'open({tilde_published!r}, "w")')
    for case_number, source in enumerate(negative_python, start=1):
        violations = scan_python_source(
            source,
            source=f"negative-python-{case_number}.py",
            repository_root=repository_root,
        )
        assert violations and all(
            "DIR-PLACE-003" in item.reason for item in violations
        ), source

    # A locally shadowed built-in and an unrelated object method are outside the
    # selected, statically recognized sink set.
    assert not scan_python_source(
        'def open(path, mode):\n    return None\nopen("data/published/x", "w")',
        source="positive-shadowed-open.py",
        repository_root=repository_root,
    )

    assert not scan_shell_source(
        "printf x > data/raw/x\nprintf x | tee data/receipts/connectors/x\n"
        "MODE=safe cp source data/quarantine/x\ninstall -tdata/raw source\n"
        "command cp source data/raw/x\nnohup cp source data/quarantine/x\n"
        "timeout 5 cp source data/receipts/x\nnice -n 5 cp source data/raw/x\n"
        "nice -n5 cp source data/quarantine/x\n"
        "env -S 'cp source data/raw/x'\n"
        "env -- -S cp source data/published/x\n"
        "install -mdead source data/raw/x\n"
        "install -gdev source data/quarantine/x\n"
        "exec cp source data/raw/x\n"
        "env -C /tmp cp source data/quarantine/x\n"
        "bash -c '( cp source data/raw/x )'\n"
        "mkdir -m 755 data/raw/x\n"
        "truncate -s 0 data/quarantine/x\n"
        "tee --output-error=warn data/raw/x\n"
        "command -v cp source data/published/x\n"
        "nohup --help cp source data/published/x\n"
        "echo x 2>&1",
        source="positive.sh",
        repository_root=repository_root,
    )
    negative_shell = (
        "printf x | tee data/published/x",
        "rsync source release/x",
        "cp source ${OUTPUT_ROOT}/x",
        "MODE=safe cp source data/published/x",
        "env -i MODE=safe cp source data/processed/x",
        "cp --target-directory=data/published data/raw/source",
        "$COMMAND source data/raw/x",
        "curl --output=data/catalog/x https://example.invalid",
        "curl -odata/catalog/x https://example.invalid",
        "wget -Odata/processed/x https://example.invalid",
        "dd if=source of=data/work/x",
        "command cp source data/published/x",
        "nohup cp source data/catalog/x",
        "timeout --foreground 5 cp source data/processed/x",
        "bash -c 'cp source release/x'",
        "nice --adjustment=5 cp source data/published/x",
        "nice -n5 cp source data/published/x",
        "env -S 'cp source data/published/x'",
        "env --split-string='cp source data/processed/x'",
        "install -d data/published/x data/raw/x",
        "env -S '' cp source data/published/x",
        "env -S '-i cp source data/published/x'",
        "env -S '-u HOME cp source data/published/x'",
        "install -d --context data/published/x data/raw/x",
        "curl -sodata/published/x https://example.invalid",
        "curl --remote-name https://example.invalid/file",
        "wget --output-document=data/published/x https://example.invalid",
        "wget -qOdata/published/x https://example.invalid",
        "exec cp source data/published/x",
        "env -C /tmp cp source data/published/x",
        "bash -c '( cp source data/published/x )'",
    )
    for case_number, command in enumerate(negative_shell, start=1):
        violations = scan_shell_source(
            command,
            source=f"negative-shell-{case_number}.sh",
            repository_root=repository_root,
        )
        assert violations and all(
            "DIR-PLACE-003" in item.reason for item in violations
        ), command

    positive_yaml = (
        "name: example\nrun: cp source data/quarantine/x\noutput_path: data/raw/x",
        "steps:\n  - run: cp source data/raw/x\n  - destination: data/receipts/x",
        'steps:\n  - {run: "cp source data/raw/x"}',
        "'run': cp source data/quarantine/x",
        "run: >\t# command\n  cp source data/raw/x\n",
        "source:\n  uri: https://example.invalid/data\n  path: upstream/item.json",
        '# example: {run: cp source data/published/x}',
        'description: safe # example {run: cp source data/published/x}',
        'description: "example syntax: {run: cp source data/published/x}"',
        'description: ["example {run: cp source data/published/x}"]',
        'steps: ["prose {run: cp source data/published/x}"]',
    )
    for case_number, document in enumerate(positive_yaml, start=1):
        assert not scan_yaml_source(
            document,
            source=f"positive-yaml-{case_number}.yaml",
            repository_root=repository_root,
        )

    negative_yaml = (
        "run: |\n  printf x > data/work/x\n",
        "destination: ${OUTPUT_ROOT}/x\n",
        "sink: [data, published, x]\n",
        "steps:\n  - run: cp source data/published/x\n",
        "outputs:\n  - destination: data/catalog/x\n",
        "steps:\n  - run: ${COMMAND}\n",
        "run: >\n  cp source\n  release/x\n",
        "run: |\n",
        "steps:\n  - {run: \"cp source data/published/x\"}\n",
        "run: > # command\n  cp source data/published/x\n",
        '"run": cp source data/published/x\n',
        'steps:\n  - {"run": "cp source data/published/x"}\n',
        "run: >\t# command\n  cp source data/published/x\n",
        '"run" : cp source data/published/x\n',
        "run: cp\n  source data/published/x\n",
    )
    for case_number, document in enumerate(negative_yaml, start=1):
        violations = scan_yaml_source(
            document,
            source=f"negative-yaml-{case_number}.yaml",
            repository_root=repository_root,
        )
        assert violations and all(
            "DIR-PLACE-003" in item.reason for item in violations
        ), document

    synthetic_runtime = tmp_path / "connectors/demo/src/run.py"
    synthetic_runtime.parent.mkdir(parents=True)
    synthetic_runtime.write_text(
        'from pathlib import Path\nPath("data/raw/x").write_text("x")',
        encoding="utf-8",
    )
    excluded_sources = (
        tmp_path / "connectors/demo/tests/test_negative.py",
        tmp_path / "connectors/demo/fixtures/forbidden.yaml",
        tmp_path / "connectors/demo/examples/example.sh",
    )
    for excluded in excluded_sources:
        excluded.parent.mkdir(parents=True, exist_ok=True)
        excluded.write_text(
            'from pathlib import Path\nPath("data/published/x").write_text("x")',
            encoding="utf-8",
        )
    assert iter_connector_source_files(tmp_path) == (synthetic_runtime,)
    assert not scan_connector_file(synthetic_runtime, tmp_path)

    synthetic_legacy_test = tmp_path / "pipelines/tests/test_legacy_canary.py"
    synthetic_legacy_test.parent.mkdir(parents=True)
    synthetic_legacy_test.write_text(
        'from pathlib import Path\nPath("data/published/x").write_text("x")',
        encoding="utf-8",
    )
    assert legacy_publish_target_violations(tmp_path)

    connector_files = iter_connector_source_files(repository_root)
    assert connector_files, "Connector output scan must not pass with an empty inventory"
    assert any(path.suffix == ".py" for path in connector_files)
    assert any(path.suffix in {".yaml", ".yml"} for path in connector_files)
    connector_violations = sorted(
        violation
        for path in connector_files
        for violation in scan_connector_file(path, repository_root)
    )
    assert not connector_violations, "\n".join(
        violation.render() for violation in connector_violations
    )

    legacy_violations = legacy_publish_target_violations(repository_root)
    assert not legacy_violations, "\n".join(legacy_violations)


def test_yaml_flow_mapping_escaped_scalar_rejection_is_bounded() -> None:
    repository_root = Path(__file__).resolve().parents[2]
    adversarial = '{run: "' + (r"\!" * 4096) + "}"

    violations = scan_yaml_source(
        adversarial,
        source="unterminated-escaped-flow-scalar.yaml",
        repository_root=repository_root,
    )

    assert len(violations) == 1
    assert violations[0].sink == "shell-parse"
    assert "DIR-PLACE-003" in violations[0].reason
