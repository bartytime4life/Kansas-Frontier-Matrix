# NOAA NEXRAD Level III original-file test samples

Retrieved October 7, 2026 UTC from the public NOAA Open Data Dissemination copy of the NEXRAD Level III archive (Unidata bucket), as referenced by NCEI's NEXRAD product page (https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar). Original bytes, used only for offline decoder regression tests, excluded from deployment assets. Data-use terms: https://registry.opendata.aws/noaa-nexrad/.

- `ddc_nst_2024_05_19_22_03_21` (key `DDC_NST_2024_05_19_22_03_21`): https://unidata-nexrad-level3.s3.amazonaws.com/DDC_NST_2024_05_19_22_03_21
  SHA-256 `ffd9fc7a57d884b68d6d9782a4883b782415f6e6dbdf02f99f86bcb6750f7ed7`; 14274 bytes.
- `ict_nmd_2024_05_06_18_47_19` (key `ICT_NMD_2024_05_06_18_47_19`): https://unidata-nexrad-level3.s3.amazonaws.com/ICT_NMD_2024_05_06_18_47_19
  SHA-256 `f311beacea490c6ca41437e7cb335b8826050ccaa4d12bccb66eb117bf7cc2b0`; 150 bytes.
- `ict_nmd_2024_05_19_23_16_04` (key `ICT_NMD_2024_05_19_23_16_04`): https://unidata-nexrad-level3.s3.amazonaws.com/ICT_NMD_2024_05_19_23_16_04
  SHA-256 `f065f2b57422e926fef56339a08ba2bb5541b8d9dd60457abc9f043b59f7687d`; 6778 bytes.
- `ict_nst_2024_05_19_23_16_04` (key `ICT_NST_2024_05_19_23_16_04`): https://unidata-nexrad-level3.s3.amazonaws.com/ICT_NST_2024_05_19_23_16_04
  SHA-256 `84f19d69069087273bfd4a10e198ef3c3f6fddc2c770e68205ab33c22600532f`; 13892 bytes.

`ICT_*_2024_05_19_23_16_04` is a Wichita volume with tornado-vortex-signature flags near McPherson County. `DDC_NST_2024_05_19_22_03_21` is a busy volume whose text table lists 34 of 38 cells. `ICT_NMD_2024_05_06_18_47_19` is an empty (no detection) product.
