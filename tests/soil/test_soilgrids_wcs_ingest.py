from pathlib import Path

from tools.ingest.soil.soilgrids_wcs_ingest import fetch_soilgrids_wcs


def test_fetch_soilgrids_wcs_fixture_mode_writes_deterministic_name(tmp_path: Path) -> None:
    # Minimal TIFF-like byte sequence used as deterministic offline fixture.
    fixture = b"II*\x00\x08\x00\x00\x00\x00\x00"
    receipt = fetch_soilgrids_wcs(
        property_name="soc",
        depth="0-5cm",
        statistic="mean",
        bbox=(-97.5, 37.0, -97.0, 37.5),
        output_path=str(tmp_path / "ignored_name.tif"),
        fixture_bytes=fixture,
    )

    output_file = Path(receipt.output_path)
    assert receipt.status == "success"
    assert output_file.exists()
    assert output_file.name.startswith("soc_0-5cm_mean_")
    assert output_file.read_bytes() == fixture

    receipt_again = fetch_soilgrids_wcs(
        property_name="soc",
        depth="0-5cm",
        statistic="mean",
        bbox=(-97.5, 37.0, -97.0, 37.5),
        output_path=str(tmp_path / "another_name.tif"),
        fixture_bytes=fixture,
    )
    assert receipt.spec_hash == receipt_again.spec_hash
