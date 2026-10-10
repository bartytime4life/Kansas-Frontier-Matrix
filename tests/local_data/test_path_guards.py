"""Regression guards for path hardening in the local-data write and intake paths.

Path checks here must stay lexical: resolving a path follows symlinks and hides
them from ``check_directory``, and intake identities are ``item_id`` digests,
not UUIDs.
"""

from pathlib import Path

import pytest

from tools.local_data import intake
from tools.local_data.file_io import write_new


def test_write_new_rejects_symlinked_parent(tmp_path):
    outside = tmp_path / "outside"
    outside.mkdir()
    store = tmp_path / "store"
    store.mkdir()
    (store / "linked").symlink_to(outside, target_is_directory=True)

    with pytest.raises(ValueError, match="SYMLINK"):
        write_new(store / "linked" / "object.json", b"{}")
    assert not list(outside.iterdir())


def test_write_new_rejects_parent_traversal(tmp_path):
    (tmp_path / "store").mkdir()
    with pytest.raises(ValueError, match="UNSAFE_PATH"):
        write_new(tmp_path / "store" / ".." / "escaped.json", b"{}")
    assert not (tmp_path / "escaped.json").exists()


def test_write_new_creates_private_directories_and_refuses_replacement(tmp_path):
    target = tmp_path / "store" / "a" / "b" / "object.json"
    write_new(target, b"first")
    assert target.read_bytes() == b"first"
    with pytest.raises(FileExistsError):
        write_new(target, b"second")
    assert target.read_bytes() == b"first"


def test_intake_identity_accepts_item_id_digests():
    identity = intake.item_id("quarantine", "usgs/objects/sha256/abc/payload")
    assert intake._validated_identity(identity) == identity


@pytest.mark.parametrize(
    "identity",
    [
        "",
        "../../etc",
        "0" * 31,
        "0" * 33,
        "A" * 32,
        "0" * 31 + "/",
        "00000000-0000-4000-8000-000000000000",
        None,
        123,
    ],
)
def test_intake_identity_rejects_non_digest_values(identity):
    with pytest.raises(intake.IntakeError, match="IDENTITY_INVALID"):
        intake._validated_identity(identity)


def test_intake_apply_rejects_traversal_before_touching_store(tmp_path):
    root = Path(tmp_path)
    with pytest.raises(intake.IntakeError, match="IDENTITY_INVALID"):
        intake.apply(root, "../" * 4 + "x", "card")
    assert not (root / "data").exists()
