// UI-owned, immutable device-review bindings. Not a source registry or release decision.
export const PREPARED_COLLECTIONS = [
  {
    "id": "normals",
    "title": "Monthly climate normals",
    "folder": "noaa-monthly-normals-ready-20261012",
    "period": "1991\u20132020 \u00b7 12 calendar months",
    "limitation": "Station aggregates, including provider estimates. Missing, measurement and completeness flags remain explicit. Not current weather or a continuous climate surface.",
    "sources": [
      "https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C01620"
    ],
    "manifestSha256": "5ab461ffa1b47df9dd9d0100dfa216ddd7e48c59976b54693541c615d80c0ee1",
    "fileCount": 31,
    "totalBytes": 13276343,
    "members": [
      {
        "file": "README.md",
        "bytes": 1729,
        "sha256": "f1f29490c370c7d5e4d54d8cdd100b85e1e59b82f7dffda5210a6e4d267fa80c"
      },
      {
        "file": "accuracy-review.json",
        "bytes": 945,
        "sha256": "04aff8127489e7d8720c36edbce2178eca62096886ccff0e1848b38a8595a6bf"
      },
      {
        "file": "coordinate-operation.json",
        "bytes": 271,
        "sha256": "b9bfba08d893af0293ce15de72bdd9a9eb466c4e6c9a606d56aff8983843e292"
      },
      {
        "file": "geojson/precipitation_in-01.geojson",
        "bytes": 553541,
        "sha256": "3c27b49bfd634443af94f6df4e85349937a09f0b57a04383754b8205fdc117a6"
      },
      {
        "file": "geojson/precipitation_in-02.geojson",
        "bytes": 553490,
        "sha256": "a36e013c78c5541bc2a7972f3c6836894ffb21a7cb363fdc6e3266885264cc32"
      },
      {
        "file": "geojson/precipitation_in-03.geojson",
        "bytes": 553453,
        "sha256": "89f20cf7cf6c3fd0febd08e8c220f795683ba6cf392f3615acc5d91051bcc9c9"
      },
      {
        "file": "geojson/precipitation_in-04.geojson",
        "bytes": 553374,
        "sha256": "5f0da36faac9301163bf84ad361cf06f1fa7cb5308ff4601ec2e570427d1e95d"
      },
      {
        "file": "geojson/precipitation_in-05.geojson",
        "bytes": 553417,
        "sha256": "cfb90d674f453f9cfffb6c2c818e59b7c04cf45af62a8ce0474e96fb317e93aa"
      },
      {
        "file": "geojson/precipitation_in-06.geojson",
        "bytes": 553384,
        "sha256": "aea3578f4ef8744f0195363ab495380d284a6e6ea873a51d10d853f9b144daad"
      },
      {
        "file": "geojson/precipitation_in-07.geojson",
        "bytes": 553372,
        "sha256": "5c9901b5512c2f8953141f45ac81c0651e6868f20754837ccadb2a948a39a507"
      },
      {
        "file": "geojson/precipitation_in-08.geojson",
        "bytes": 553385,
        "sha256": "ae89fa0dc5935dbf51bd4c80e713c690d7ffd487a85ff18aafa00f5523f9f39c"
      },
      {
        "file": "geojson/precipitation_in-09.geojson",
        "bytes": 553372,
        "sha256": "03546de47630e5f96d715e7a1a4c46a87d54b1fcb2823bcd0fd7459949c49601"
      },
      {
        "file": "geojson/precipitation_in-10.geojson",
        "bytes": 553960,
        "sha256": "eea5a7d4a271ec1a1d1c1cbba8bc0eddb4a1b0a7475852df329e656ed67959e2"
      },
      {
        "file": "geojson/precipitation_in-11.geojson",
        "bytes": 553988,
        "sha256": "1f848e907cd49ca2fc5f50b401ac25aba4d6e218199a3b7d55f0b0ba2e5538d4"
      },
      {
        "file": "geojson/precipitation_in-12.geojson",
        "bytes": 554097,
        "sha256": "5ebcce432beed4fa387eb70d6f9648b15f851737b9ac82176f97547dd0cc45e3"
      },
      {
        "file": "geojson/temperature_f-01.geojson",
        "bytes": 174139,
        "sha256": "e4eafca56546e39e0ffba041cee8f5a8f01b50049cb9c8c02f5f2139efc73537"
      },
      {
        "file": "geojson/temperature_f-02.geojson",
        "bytes": 174118,
        "sha256": "acdc984cb00913b08a37c4de21940164dd221988db9b29615e9c11680e5d33f7"
      },
      {
        "file": "geojson/temperature_f-03.geojson",
        "bytes": 174148,
        "sha256": "e2cff902b17cf4b3991a04f5f93240713d00606f0ec01f4dac12164e2579bb42"
      },
      {
        "file": "geojson/temperature_f-04.geojson",
        "bytes": 174124,
        "sha256": "185e77f7149c3127c8c9aaf8c3496422da79793dafe7801c099b6eb13651b70d"
      },
      {
        "file": "geojson/temperature_f-05.geojson",
        "bytes": 174154,
        "sha256": "1c3cf04ebe4efbe64babe6c10b0196903d4d032449a36147bf4dd2f6f2cd92e2"
      },
      {
        "file": "geojson/temperature_f-06.geojson",
        "bytes": 174111,
        "sha256": "8e7c4ac2db728f9d25c61f03f758f62729c19390c4204096a488a56e0b8c6d1d"
      },
      {
        "file": "geojson/temperature_f-07.geojson",
        "bytes": 174128,
        "sha256": "cbd6083384951932f3ba3ebb4a87e6ee7e8eec4ebf1b7f3734b37826001bceed"
      },
      {
        "file": "geojson/temperature_f-08.geojson",
        "bytes": 174118,
        "sha256": "cc91e0700360b3793bdc7595ec821edb629c94658d1db77134fd48ae29f1df41"
      },
      {
        "file": "geojson/temperature_f-09.geojson",
        "bytes": 174137,
        "sha256": "465e23ca87f330f5a12d3d1342955ff190a8220ccf12fe7b4ddf678b2c6c539f"
      },
      {
        "file": "geojson/temperature_f-10.geojson",
        "bytes": 174302,
        "sha256": "aa878fe34cd3780be88f2065c5272dec87817eafd7487f4e543bc80eaaa83639"
      },
      {
        "file": "geojson/temperature_f-11.geojson",
        "bytes": 174312,
        "sha256": "d6c5417a996c096944999ef62b116abf9087f93f25783addbf9fc89785a9c558"
      },
      {
        "file": "geojson/temperature_f-12.geojson",
        "bytes": 174312,
        "sha256": "6ca9964745853f2eeb5ff58acdc9f615f24791be32d2e01129169f52d2df1f41"
      },
      {
        "file": "rights-review.json",
        "bytes": 1280,
        "sha256": "c7544b53061e04f696d45001bd1e75c5a89df678e01a1b8a0ef32dbe115f2bbc"
      },
      {
        "file": "tables/precipitation_in.csv",
        "bytes": 2292089,
        "sha256": "9d6ec603f73177f37434a8bbe46e7c4b883e7432557f9068df5ec16c6522438e"
      },
      {
        "file": "tables/temperature_f.csv",
        "bytes": 2240387,
        "sha256": "65d67a28ba1d5d75511bd5e39645c4224b13ddb9bd3b8d2b5f6241317ab4209f"
      }
    ],
    "mapFiles": [
      "geojson/precipitation_in-01.geojson",
      "geojson/precipitation_in-02.geojson",
      "geojson/precipitation_in-03.geojson",
      "geojson/precipitation_in-04.geojson",
      "geojson/precipitation_in-05.geojson",
      "geojson/precipitation_in-06.geojson",
      "geojson/precipitation_in-07.geojson",
      "geojson/precipitation_in-08.geojson",
      "geojson/precipitation_in-09.geojson",
      "geojson/precipitation_in-10.geojson",
      "geojson/precipitation_in-11.geojson",
      "geojson/precipitation_in-12.geojson",
      "geojson/temperature_f-01.geojson",
      "geojson/temperature_f-02.geojson",
      "geojson/temperature_f-03.geojson",
      "geojson/temperature_f-04.geojson",
      "geojson/temperature_f-05.geojson",
      "geojson/temperature_f-06.geojson",
      "geojson/temperature_f-07.geojson",
      "geojson/temperature_f-08.geojson",
      "geojson/temperature_f-09.geojson",
      "geojson/temperature_f-10.geojson",
      "geojson/temperature_f-11.geojson",
      "geojson/temperature_f-12.geojson"
    ],
    "tableFiles": [
      "tables/precipitation_in.csv",
      "tables/temperature_f.csv"
    ]
  },
  {
    "id": "history",
    "title": "Four-station climate history",
    "folder": "noaa-ghcnd-history-ready-20261012",
    "period": "1895\u20132026 \u00b7 station coverage differs",
    "limitation": "395,117 retained observations. This kit shows station/year/element coverage and missing, trace and quality counts. Historical station moves and homogeneity are unverified. The full archive stays in the protected store.",
    "sources": [
      "https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00861"
    ],
    "manifestSha256": "6610cc280768f37a3230af5b8bf70fca8f652cadd5ad012fe79bc558b314db33",
    "fileCount": 6,
    "totalBytes": 77008,
    "members": [
      {
        "file": "README.md",
        "bytes": 1603,
        "sha256": "076f6f22691db4b9d111a408ebec44e284c34657b9c6d68e12c32f8f68cc6b8a"
      },
      {
        "file": "accuracy-review.json",
        "bytes": 921,
        "sha256": "f5d67c47ccf1930a9c0c39c3cf4be66e9c2cb3f21faed2b7d746e9959f2fb890"
      },
      {
        "file": "retained-archive-reference.json",
        "bytes": 897,
        "sha256": "b76b4f8ceb9ccbf1a667b048562f07931635ff2ccbb1b8ead16480533fde94ef"
      },
      {
        "file": "rights-review.json",
        "bytes": 1318,
        "sha256": "5228ff688dc950d65ec7355c8c8022fe2ea403e54631dcded2a2fb11bbbe3d81"
      },
      {
        "file": "station-year-coverage.csv",
        "bytes": 69782,
        "sha256": "4fff1a12288c48c58e8ca48f949f55fffa0ba68b141dde0c537421529aae2cc9"
      }
    ],
    "mapFiles": [],
    "tableFiles": [
      "station-year-coverage.csv"
    ]
  },
  {
    "id": "discharge",
    "title": "Frozen river discharge",
    "folder": "usgs-discharge-ready-20261012",
    "period": "September 29\u201330, 2026 \u00b7 193 observations",
    "limitation": "All values are provisional and stale for current conditions. Provider geometry is already WGS84; original datum labels are history. Approximate map-derived positions, not survey points. No warning or forecast use.",
    "sources": [
      "https://water.usgs.gov/data/disclaimer.html"
    ],
    "manifestSha256": "116bed573b51f194001d77af2d7e4df4fc96bd1ff0e6e8a84e88255acfc52a92",
    "fileCount": 6,
    "totalBytes": 58486,
    "members": [
      {
        "file": "README.md",
        "bytes": 1228,
        "sha256": "46ba3729cc131423461c9104d085d3496e900124dfd9dd0b3c06a97a9b79f7c1"
      },
      {
        "file": "accuracy-review.json",
        "bytes": 661,
        "sha256": "d4b53bfea87f8c2c9071084622fab441306663b93a30d3a520d2873e4b261022"
      },
      {
        "file": "captured-discharge-observations.csv",
        "bytes": 50699,
        "sha256": "27658931d571cccf0b70b6e23942f687ffae341e390f6f8280b9513247412a2d"
      },
      {
        "file": "discharge-stations-captured-20260929-30.geojson",
        "bytes": 2208,
        "sha256": "bb2d9a0cd98bbcac87266ef29f8a49f469fcc4b58e240aef2afa6f7c15d9c0c4"
      },
      {
        "file": "rights-review.json",
        "bytes": 1268,
        "sha256": "39bc18ca8386a9226d434dd1ad087314d75f1dd5da43ea1b239d7c0413fe7244"
      }
    ],
    "mapFiles": [
      "discharge-stations-captured-20260929-30.geojson"
    ],
    "tableFiles": [
      "captured-discharge-observations.csv"
    ]
  },
  {
    "id": "counties",
    "title": "Kansas county overview",
    "folder": "census-counties-reference-20261012",
    "period": "105 counties \u00b7 January 1, 2025 boundaries",
    "limitation": "Generalized statistical geography, not legal land descriptions. Maximum processing displacement 34.59 m; 4 m datum-operation accuracy is not total boundary accuracy. Preferred grid unavailable.",
    "sources": [
      "https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2025/TGRSHP2025_TechDoc_Ch1.pdf"
    ],
    "manifestSha256": "085b6abced2285cabe618b0afb6abb7af11320420448c1cd7794e820aa74f7bb",
    "fileCount": 5,
    "totalBytes": 590016,
    "members": [
      {
        "file": "README.md",
        "bytes": 2001,
        "sha256": "5cf8de85bca684cbdde5b20612b30cd43b9c5ed373dc79212aee1bd012345f5b"
      },
      {
        "file": "accuracy-review.json",
        "bytes": 1637,
        "sha256": "548aa2fca0dcf5b3c4e40e7a6040a94c9416f50592ce9d433496c78d2d2330cf"
      },
      {
        "file": "kansas-counties-2025-overview.geojson",
        "bytes": 582794,
        "sha256": "23368a570992dac6d8b2e7515835cb647c1e8a5abb9907d74d471d842058b80a"
      },
      {
        "file": "rights-review.json",
        "bytes": 1278,
        "sha256": "452308ec60a08cdd2e74bd5e5e8af68faabc282a5d06af59fe06bbb2ab603cfe"
      }
    ],
    "mapFiles": [
      "kansas-counties-2025-overview.geojson"
    ],
    "tableFiles": []
  },
  {
    "id": "wind",
    "title": "Frozen airport wind",
    "folder": "iem-wind-table-ready-20261012",
    "period": "October 5\u20136, 2026 UTC \u00b7 64 stations",
    "limitation": "9,760 observations with little provider QC. M remains missing. Directions are from true north; speeds and gusts are knots. Peak remark time differs from observation time. Not live telemetry or continuous history.",
    "sources": [
      "https://mesonet.agron.iastate.edu/disclaimer.php",
      "https://mesonet.agron.iastate.edu/request/download.phtml?network=ALL_ASOS"
    ],
    "manifestSha256": "eb2726ef5d33a343e6994ea9d63a95b15e25848e60e11c0b69e9d89af3128df9",
    "fileCount": 7,
    "totalBytes": 410702,
    "members": [
      {
        "file": "README.md",
        "bytes": 1121,
        "sha256": "2618ff193809daa883efaf3135ddb6ca3ca132763433e000b41d29c81cbd6112"
      },
      {
        "file": "accuracy-review.json",
        "bytes": 1508,
        "sha256": "760e977f8c4269297b0ccb7090483a976d86b9f284f26d3a9a472ed5e94c5f3f"
      },
      {
        "file": "capture-receipt.json",
        "bytes": 587,
        "sha256": "51a372b61da4bdf8351f91edba4faeb25900c7fcb425acf117816c0685076fe2"
      },
      {
        "file": "observations-utc.csv",
        "bytes": 398197,
        "sha256": "3fdf3ba1422153c3b82b538abdb194f5d7df547f166242ebe5b869009c7fecb6"
      },
      {
        "file": "rights-review.json",
        "bytes": 3536,
        "sha256": "341540ef893d873430177ea7206f9f5cd23d7e1d517c6136fe3c3b9c4f890589"
      },
      {
        "file": "station-coverage.csv",
        "bytes": 3750,
        "sha256": "910bd54cc6f76c30f666630e37a66c79de719fd12859420e37e0db5413ca1a22"
      }
    ],
    "mapFiles": [],
    "tableFiles": [
      "observations-utc.csv",
      "station-coverage.csv"
    ]
  },
  {
    "id": "grids",
    "title": "Offline coordinate references",
    "folder": "kfm-nadcon5-reference-ready-20261012",
    "period": "Four CONUS NADCON5 grids",
    "limitation": "Licensed dependency references only; the grids stay in the protected store. No transform, install or improved-position claim. Exact datum realization, chain, area/epoch and independent controls still need review.",
    "sources": [
      "https://cdn.proj.org/us_noaa_README.txt",
      "https://geodesy.noaa.gov/web_services/ncat/index.shtml"
    ],
    "manifestSha256": "ee774c3495f32bc406f6073b6826e7976a22afef92219d88a0862ea8ecc62f97",
    "fileCount": 5,
    "totalBytes": 11418,
    "members": [
      {
        "file": "README.md",
        "bytes": 1115,
        "sha256": "265cc75eff7851e7bc355a8c9c6dfc36a7f21f54dc4b9d8cbb2bc853fdbab4b4"
      },
      {
        "file": "accuracy-review.json",
        "bytes": 954,
        "sha256": "9bcdb6ca80f4ea206929d3f2b823ce6f9e75251506a656c8edd58f3c2c9c90c2"
      },
      {
        "file": "retained-grid-references.json",
        "bytes": 2969,
        "sha256": "9e61f5174185310cceeba26b3d6c833c834cc78984b091c8ca88a6f94a30ad35"
      },
      {
        "file": "rights-review.json",
        "bytes": 4677,
        "sha256": "b1a204d926d4e4c96d56e28cf4168eb4486a676f0fc1b4932711654b5c22635c"
      }
    ],
    "mapFiles": [],
    "tableFiles": []
  }
] as const;
