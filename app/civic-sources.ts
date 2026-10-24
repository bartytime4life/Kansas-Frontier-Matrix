/** Application source-discovery notes, not a dataset registry or release.
 * Checks concern pages/links only; source rights and data admission remain separate.
 * Research detail and qualification sequence: docs/civic-atlas.md. */
export type CivicCategory = 'government' | 'voting' | 'money' | 'laws' | 'work-services' | 'history' | 'wellbeing';
export type CivicSource = Readonly<{id:string; title:string; organization:string; url:string; category:CivicCategory; description:string; geography:string; checkedAt:string; status:'page-verified'|'link-verified'|'needs-verification'; limitation:string; tags?:readonly string[]}>;
export const CIVIC_SOURCES: readonly CivicSource[] = [
  {
    "id": "ks-county-directory",
    "title": "Kansas.gov county directory",
    "organization": "Kansas.gov",
    "url": "https://portal.kansas.gov/government/county-list/",
    "category": "government",
    "description": "Find county and local-government reference information.",
    "geography": "county",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Two demonstrably wrong directory targets; 103 individual county sites not verified. Rights/automated reuse not established.",
    "tags": [
      "HTML links"
    ]
  },
  {
    "id": "census-ks-counties-2026",
    "title": "Census TIGERweb Kansas counties",
    "organization": "U.S. Census Bureau",
    "url": "https://tigerweb.geo.census.gov/tigerwebmain/Files/acs26/tigerweb_acs26_county_ks.html",
    "category": "government",
    "description": "Find county and local-government reference information.",
    "geography": "county",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Reference points are not county offices/polling places. Original response bytes not acquired; no raw SHA receipt.",
    "tags": [
      "HTML table"
    ]
  },
  {
    "id": "ks-city-directory",
    "title": "City list outbound from Kansas.gov",
    "organization": "League of Kansas Municipalities (linked by Kansas.gov)",
    "url": "https://www.lkm.org/",
    "category": "government",
    "description": "Find county and local-government reference information.",
    "geography": "municipality",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "League of Kansas Municipalities is an intermediary. Exact directory endpoint and current contents not retrieved. City authority must be verified.",
    "tags": [
      "HTML directory expected; not inspected"
    ]
  },
  {
    "id": "ks-county-election-offices",
    "title": "Kansas SOS county election offices",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/elections/county-election-offices.html",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "county",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Directory detail endpoint returned 403. Do not infer personalized polling assignments.",
    "tags": [
      "HTML; linked ASPX directory"
    ]
  },
  {
    "id": "ks-voterview",
    "title": "Kansas official VoterView",
    "organization": "Kansas Secretary of State",
    "url": "https://kansasvoterinfo.gov/VoterView",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "address/election",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Outbound user-directed link only. Do not collect names, birth dates, voter records, party registration, ballots or personal query responses into KFM SQL/AI.",
    "tags": [
      "Interactive lookup; no verified public bulk API"
    ]
  },
  {
    "id": "ks-voter-information",
    "title": "Kansas SOS voter information",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/elections/voter-information.html",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "state/election",
    "checkedAt": "2026-10-24",
    "status": "link-verified",
    "limitation": "Legal/procedural facts must be revalidated with source and valid dates; cite or abstain.",
    "tags": [
      "HTML"
    ]
  },
  {
    "id": "ks-election-dates",
    "title": "Kansas SOS election dates",
    "organization": "Kansas Secretary of State",
    "url": "https://www.sos.ks.gov/elections/important-election-dates.html",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "state/election",
    "checkedAt": "2026-10-24",
    "status": "link-verified",
    "limitation": "No deadline asserted here. Operational cards require same-day validation near election and unambiguous timezone.",
    "tags": [
      "HTML/PDF"
    ]
  },
  {
    "id": "ks-candidate-list",
    "title": "Kansas SOS candidate list",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/elections/elections_upcoming_candidate.aspx",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "office/district/election",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "Do not label incomplete/unofficial/campaign announcements as certified ballot. Include every verified ballot candidate equivalently; omit home addresses and private contacts.",
    "tags": [
      "ASPX table expected; not acquired"
    ]
  },
  {
    "id": "ks-election-results",
    "title": "Kansas SOS election results",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/elections/election-results.html",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "state/county/office",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Verify certified final versus unofficial election-night results; denominator, precinct scope, ballot changes and corrections.",
    "tags": [
      "HTML; linked PDF"
    ]
  },
  {
    "id": "ks-district-authority",
    "title": "Kansas SOS district maps",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/elections/district-maps.html",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "congress/state-house/state-senate/education",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Do not apply current geography to historic terms. Legal map and effective dates govern assignment; no machine geometry acquired.",
    "tags": [
      "HTML links; PDF map packets"
    ]
  },
  {
    "id": "ks-klrd-districts",
    "title": "KLRD redistricting",
    "organization": "Kansas Legislative Research Department",
    "url": "https://klrd.gov/policy-area/redistricting/",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "congress/state-house/state-senate/education",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Geospatial products need plan/version checks and geometry validation; imported map roster may lag officeholder changes.",
    "tags": [
      "HTML; PDFs; linked Google maps"
    ]
  },
  {
    "id": "ks-klrd-enacted-plans",
    "title": "KLRD enacted plans",
    "organization": "Kansas Legislative Research Department",
    "url": "https://klrd.gov/policy-area/redistricting/enacted-plans-2022/",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "political districts",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Needs direct package download rights and geometries verification.",
    "tags": [
      "HTML; linked packets"
    ]
  },
  {
    "id": "census-tiger-boundaries",
    "title": "Census TIGER/Line 2025",
    "organization": "U.S. Census Bureau",
    "url": "https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2025.html",
    "category": "voting",
    "description": "Follow official election and district information for the relevant election.",
    "geography": "county/place/legislative/school",
    "checkedAt": "2026-10-24",
    "status": "link-verified",
    "limitation": "Secondary operational geometry to validate against Kansas legal boundaries; simplified display polygons cannot determine a voter's exact district.",
    "tags": [
      "Shapefile ZIP; metadata"
    ]
  },
  {
    "id": "ks-legislature",
    "title": "Kansas Legislature",
    "organization": "Kansas Legislature",
    "url": "https://www.kslegislature.gov/b2025_26/",
    "category": "laws",
    "description": "Read legislative records and distinguish proposed bills, votes, and enacted law.",
    "geography": "state/district",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Enacted law versus proposal, amended version, effective date, jurisdiction and court orders must remain distinct. APIs not established.",
    "tags": [
      "HTML; PDFs/ODT documents"
    ]
  },
  {
    "id": "ks-legislature-votes",
    "title": "Kansas recorded votes",
    "organization": "Kansas Legislature",
    "url": "https://www.kslegislature.gov/b2025_26/votes/",
    "category": "laws",
    "description": "Read legislative records and distinguish proposed bills, votes, and enacted law.",
    "geography": "legislator/measure/chamber",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "A vote for an amendment/procedure is not automatically support for every policy. Exact action, version and absence status mandatory.",
    "tags": [
      "HTML and downloadable PDF"
    ]
  },
  {
    "id": "ks-legislature-feeds",
    "title": "Kansas Legislature RSS/Atom guidance",
    "organization": "Kansas Legislature",
    "url": "https://www.kslegislature.gov/b2025_26/feeds/rsshelp/",
    "category": "laws",
    "description": "Read legislative records and distinguish proposed bills, votes, and enacted law.",
    "geography": "state/measure/chamber",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Do not assert feed acquired or stable contract. Throttle, use conditional requests, deduplicate by source event+revision, archive evidence.",
    "tags": [
      "RSS 2.0 and Atom 1.0 documented"
    ]
  },
  {
    "id": "ks-legislature-archive",
    "title": "Kansas Legislature archives",
    "organization": "Kansas Legislature",
    "url": "https://www.kslegislature.gov/b2025_26/archive/",
    "category": "history",
    "description": "Find dated source material for historical research.",
    "geography": "state/biennium",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Coverage varies by session and document type. OCR needs source page links and confidence; absence is unknown not proof of no action.",
    "tags": [
      "Archived HTML; PDF/ODT"
    ]
  },
  {
    "id": "ks-laws",
    "title": "Kansas statutes",
    "organization": "Kansas Legislature",
    "url": "https://www.kslegislature.gov/b2025_26/laws/",
    "category": "laws",
    "description": "Read legislative records and distinguish proposed bills, votes, and enacted law.",
    "geography": "state",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "For neutral explanation not individualized legal advice. Cross-check enacted session law and amendments.",
    "tags": [
      "HTML"
    ]
  },
  {
    "id": "ks-session-laws",
    "title": "Kansas SOS session laws",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/publications/session-laws.html",
    "category": "laws",
    "description": "Read legislative records and distinguish proposed bills, votes, and enacted law.",
    "geography": "state/session/chapter",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Check chapter version; enrolled text and current codification may differ; preserve both.",
    "tags": [
      "HTML; linked PDFs"
    ]
  },
  {
    "id": "ks-state-jobs",
    "title": "Kansas state employment",
    "organization": "Kansas Department of Administration",
    "url": "https://admin.ks.gov/offices/personnel-services/jobs",
    "category": "work-services",
    "description": "Find official public services, opportunities, and project information.",
    "geography": "state/location/agency",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Current jobs not acquired. Send applications to official portal; no CVs, credentials or employment account data in civic SQL.",
    "tags": [
      "HTML; PeopleSoft job search"
    ]
  },
  {
    "id": "ks-services",
    "title": "Kansas.gov services",
    "organization": "Kansas.gov",
    "url": "https://portal.kansas.gov/services/",
    "category": "work-services",
    "description": "Find official public services, opportunities, and project information.",
    "geography": "state/service area",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "An official portal link is not proof of entitlement/availability. Payment/login flows remain off-platform.",
    "tags": [
      "HTML categorized links"
    ]
  },
  {
    "id": "ks-open-meetings",
    "title": "Kansas Public Square",
    "organization": "Kansas Public Square",
    "url": "https://publicsquare.ks.gov/",
    "category": "laws",
    "description": "Read legislative records and distinguish proposed bills, votes, and enacted law.",
    "geography": "agency/board/commission",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "No meetings acquired; confirm cancellation/timezone/participation rules with owning agency.",
    "tags": [
      "Interactive calendar; not acquired"
    ]
  },
  {
    "id": "ks-local-history",
    "title": "Kansas Historical Society counties",
    "organization": "Kansas Historical Society",
    "url": "https://www.kansashistory.gov/p/kansas-counties/11304",
    "category": "history",
    "description": "Find dated source material for historical research.",
    "geography": "current/defunct county",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Do not use modern boundary crosswalks as historic facts; archival rights and cultural sensitivity assessed item by item.",
    "tags": [
      "HTML; linked archive catalog"
    ]
  },
  {
    "id": "ks-state-documents",
    "title": "Kansas government CONTENTdm collection",
    "organization": "Kansas government digital collections",
    "url": "https://cdm16884.contentdm.oclc.org/",
    "category": "history",
    "description": "Find dated source material for historical research.",
    "geography": "Unknown until collections inspected",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "No publisher/collection/item evidence acquired, API unverified.",
    "tags": [
      "CONTENTdm; no item records retrieved"
    ]
  },
  {
    "id": "ks-infrastructure-hub",
    "title": "Kansas Infrastructure Hub resources",
    "organization": "Kansas Infrastructure Hub",
    "url": "https://www.kshub.gov/resources/state-agency-resources",
    "category": "work-services",
    "description": "Find official public services, opportunities, and project information.",
    "geography": "state/project/local",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "Do not treat resource directory as actual awards or completed projects.",
    "tags": [
      "HTML; not acquired"
    ]
  },
  {
    "id": "ks-kpdc-campaign-finance",
    "title": "Kansas campaign finance reports",
    "organization": "Kansas Public Disclosure Commission",
    "url": "https://kpdc.kansas.gov/campaign-finance/view-submitted-forms-and-reports/",
    "category": "money",
    "description": "Candidate/committee receipts, expenditures, debts and amended filings",
    "geography": "State office and district/committee jurisdiction, not donor residences",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Report form fields and sample extraction still need validation Local-office reports may be filed with county clerks/election commissioners Reported funds are not personal wealth or evidence of corruption",
    "tags": [
      "HTML index linking scanned filed forms/reports; bulk API not confirmed"
    ]
  },
  {
    "id": "ks-sos-substantial-interest",
    "title": "State Statements of Substantial Interests",
    "organization": "Kansas Secretary of State",
    "url": "https://sos.ks.gov/elections/substantial-interest-center.html",
    "category": "money",
    "description": "Public officials' disclosed business/financial interests",
    "geography": "Official office/jurisdiction only",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Statement disclosure is not a net-worth estimate Local statements are at city/county election officers Exclude home addresses, signatures, personal contact data and unnecessary family data from public derivatives",
    "tags": [
      "Public search https://sos.ks.gov/elections/ssi/examiner_entry.aspx ; search returned 403 to research tool"
    ]
  },
  {
    "id": "ks-kpdc-lobbying",
    "title": "Lobbying and public disclosure agency",
    "organization": "Kansas Public Disclosure Commission",
    "url": "https://kpdc.kansas.gov/",
    "category": "money",
    "description": "Lobbyist registrations, expenditure reports, advisory opinions",
    "geography": "State",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Detailed lobbying reports and machine interface not examined Do not imply lobbying or a donation proves unlawful influence",
    "tags": [
      "HTML; linked forms, directory and reports"
    ]
  },
  {
    "id": "fec-federal-finance",
    "title": "Federal candidate and committee finance",
    "organization": "Federal Election Commission",
    "url": "https://www.fec.gov/data/browse-data/",
    "category": "money",
    "description": "Kansas federal candidate/committee reports and summarized campaign finance",
    "geography": "Federal office and electoral district",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Names/addresses from FEC contribution reports have sale/solicitation/commercial-use restrictions; see https://www.fec.gov/updates/sale-or-use-contributor-information/ Prefer committee/candidate totals and omit individual donor addresses Keep original filings and amendments linked",
    "tags": [
      "Web data exports; OpenFEC developer entry https://api.open.fec.gov/developers/ verified; API key setup required"
    ]
  },
  {
    "id": "ks-kanview",
    "title": "KanView public expenditure and revenue downloads",
    "organization": "Kansas Department of Administration",
    "url": "https://kanview.ks.gov/DataDownload.aspx",
    "category": "money",
    "description": "Agency accounting totals and vendor payment trails",
    "geography": "State agency; vendor location is NOT service-benefit geography",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Official site calls data unaudited Accounting basis differs from budget basis; includes non-expense transactions Do not equate vendor HQ location with where expenditure benefits residents Terms and exclusion links timed out; terms review needed before automated ingestion",
    "tags": [
      "Documented downloadable form outputs; export byte format/API not tested"
    ]
  },
  {
    "id": "ks-budget-proposals",
    "title": "Governor's budget reports",
    "organization": "Kansas Division of the Budget",
    "url": "https://budget.kansas.gov/budget-report/",
    "category": "money",
    "description": "Proposed state budgets and agency program narratives",
    "geography": "State and agency/program",
    "checkedAt": "2026-10-24",
    "status": "link-verified",
    "limitation": "Label governor recommendation; not enacted appropriation or actual spending Normalize fiscal/calendar year before charts",
    "tags": [
      "PDF volumes, previous editions linked"
    ]
  },
  {
    "id": "ks-budget-comparison",
    "title": "Budget comparison reports",
    "organization": "Kansas Division of the Budget",
    "url": "https://budget.kansas.gov/comparison-reports/",
    "category": "money",
    "description": "Proposed-versus-legislative budget changes and historical time series",
    "geography": "State and agency/program",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Landing text says FY2027 summarizes '2024 Legislature'; apparent metadata inconsistency requires PDF verification Do not load stale or superseded PDF without revision provenance",
    "tags": [
      "PDFs"
    ]
  },
  {
    "id": "ks-municipal-budgets",
    "title": "Municipal adopted budgets and revenue-neutral-rate documents",
    "organization": "Kansas Department of Administration",
    "url": "https://admin.ks.gov/offices/accounts-reports/local-government/municipal-services/municipal-budgets",
    "category": "money",
    "description": "Town/county fiscal plans and property-tax hearing evidence",
    "geography": "Local government entity; join to verified entity ID and boundary",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Coverage per year/entity unmeasured A revenue-neutral-rate exceedance is not by itself a resident-specific tax estimate Needs entity crosswalk; do not assume municipality matches county",
    "tags": [
      "Linked budget/RNR documents; full file inventory not acquired"
    ]
  },
  {
    "id": "ks-procurement-contracts",
    "title": "Kansas procurement contracts",
    "organization": "Kansas Department of Administration",
    "url": "https://admin.ks.gov/offices/procurement-contracts/bidding--contracts/contracts",
    "category": "money",
    "description": "Public contract awards and procurement records",
    "geography": "Agency and actual contract service area when stated",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Detailed contract data and automation not verified Contract ceiling/award/payment are distinct measures",
    "tags": [
      "Web contract search links; API/export unknown"
    ]
  },
  {
    "id": "ks-kdor-local-rates",
    "title": "Local sales-tax rates and quarterly changes",
    "organization": "Kansas Department of Revenue",
    "url": "https://www.ksrevenue.gov/salesratechanges.html",
    "category": "money",
    "description": "Current and historical city/county/special-jurisdiction sales-tax context",
    "geography": "City, county and special tax jurisdiction",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Exact address may cross special jurisdiction; county rate alone not full rate Link statutory tax type and effective date; do not treat rate as personal tax advice KDOR copyright/terms present; licensing not reviewed",
    "tags": [
      "XLSX; latest linked file https://www.ksrevenue.gov/pdf/pub17001026.xlsx"
    ]
  },
  {
    "id": "ks-kdor-local-receipts",
    "title": "Local sales and use-tax distributions",
    "organization": "Kansas Department of Revenue",
    "url": "https://www.ksrevenue.gov/prsalesreports.html",
    "category": "money",
    "description": "City/county public-revenue history",
    "geography": "City/county",
    "checkedAt": "2026-10-24",
    "status": "link-verified",
    "limitation": "Distributions differ from economic sales activity and household tax burden File formats and values not yet parsed",
    "tags": [
      "HTML index; linked reports"
    ]
  },
  {
    "id": "ks-kdor-statistics",
    "title": "Kansas tax statistics",
    "organization": "Kansas Department of Revenue",
    "url": "https://www.ksrevenue.gov/prstatistics.html",
    "category": "money",
    "description": "Receipt series, tax expenditures, motor fuel and other fiscal context",
    "geography": "Varies by report",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Report-specific units/methods must be recorded before ingestion",
    "tags": [
      "HTML report index; files vary"
    ]
  },
  {
    "id": "ks-commerce-incentives",
    "title": "Kansas incentive transparency database",
    "organization": "Kansas Department of Commerce",
    "url": "https://www.kansascommerce.gov/dataview/transparency-explorer-home/",
    "category": "money",
    "description": "Program/recipient incentives linked to project geography",
    "geography": "Project/recipient location when actually stated",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "Do not repeat old 'real-time' marketing as measured freshness Pair with independent audit and annual reports Jobs promised versus jobs achieved must remain separate",
    "tags": [
      "Web database; research fetch exceeded 4MB; API/export unknown"
    ]
  },
  {
    "id": "ks-lpa-incentive-audit",
    "title": "Legislative Post Audit incentive-database review",
    "organization": "Kansas Legislative Division of Post Audit",
    "url": "https://www.kslpa.gov/audit-report-library/evaluating-whether-the-department-of-commerces-economic-development-transparency-database-includes-the-required-information-and-functionality/",
    "category": "money",
    "description": "Source limitations, accountability findings and correction history",
    "geography": "State program/database",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Audit says database may have changed since review; findings are historical, not proof of current deficiencies Limited scope did not verify accuracy of underlying database",
    "tags": [
      "HTML report and print report"
    ]
  },
  {
    "id": "ks-kdot-ike-projects",
    "title": "IKE projects map",
    "organization": "Kansas Department of Transportation",
    "url": "https://www.ksdot.gov/programs/eisenhower-legacy-transportation-program-ike/ike-projects-map",
    "category": "work-services",
    "description": "Transport project location, stage and cost context",
    "geography": "Project geometry/county/route",
    "checkedAt": "2026-10-24",
    "status": "needs-verification",
    "limitation": "Do not imply a working ingestion or GIS endpoint Geometry and completion require record-level validation",
    "tags": [
      "Dashboard; feature service/export not verified"
    ]
  },
  {
    "id": "census-acs-five-year",
    "title": "ACS five-year community estimates",
    "organization": "U.S. Census Bureau",
    "url": "https://www.census.gov/data/developers/data-sets/acs-5year.html",
    "category": "wellbeing",
    "description": "Income, poverty, housing cost and commuting context",
    "geography": "State/county/place/tract/block group subject to table",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Compare nonoverlapping periods; ACS period estimate is not a single-year count Keep MOE and suppression/annotation flags Do not infer individual characteristics from an area",
    "tags": [
      "Official API; all queries now require API key per current page"
    ]
  },
  {
    "id": "bls-laus",
    "title": "Local Area Unemployment Statistics",
    "organization": "U.S. Bureau of Labor Statistics",
    "url": "https://www.bls.gov/lau/",
    "category": "wellbeing",
    "description": "Resident labor force, employment and unemployment trend",
    "geography": "States/counties/metros and many cities",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Residence based; not count of jobs located in area Retain revision and seasonal-adjustment identity",
    "tags": [
      "Official tables/text/API access; source-series selection untested"
    ]
  },
  {
    "id": "bls-qcew",
    "title": "Quarterly Census of Employment and Wages",
    "organization": "U.S. Bureau of Labor Statistics",
    "url": "https://www.bls.gov/cew/additional-resources/open-data/csv-data-slices.htm",
    "category": "wellbeing",
    "description": "County industry jobs, wages and establishments",
    "geography": "County/state/metro by industry and ownership",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Workplace-based; differs from LAUS residence employment Preserve suppression and exclude suppressed values from inference",
    "tags": [
      "Documented CSV data slices by area/industry/size"
    ]
  },
  {
    "id": "bea-rpp",
    "title": "Regional price parities",
    "organization": "U.S. Bureau of Economic Analysis",
    "url": "https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area",
    "category": "wellbeing",
    "description": "Regional price-level comparison and purchasing-power context",
    "geography": "State and metropolitan area; NOT observed county series",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Cross-area price level is not local CPI inflation Never paint county-specific price levels from state/metro observation without explicit modeled label",
    "tags": [
      "Downloadable data, interactive tables; BEA API metadata access documented"
    ]
  },
  {
    "id": "bea-regional-accounts",
    "title": "BEA regional economic accounts/API",
    "organization": "U.S. Bureau of Economic Analysis",
    "url": "https://www.bea.gov/data/economic-accounts/regional",
    "category": "wellbeing",
    "description": "Regional income, GDP and employment history",
    "geography": "State/county/metro depending on table",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Current table/line availability needs API metadata check Preserve BEA withheld/not-available markers GDP and personal income are not household well-being",
    "tags": [
      "Documented API and downloadable tables; API signup https://apps.bea.gov/API/signup/"
    ]
  },
  {
    "id": "bls-kansas-cpi-context",
    "title": "BLS Kansas and Midwest inflation context",
    "organization": "U.S. Bureau of Labor Statistics",
    "url": "https://www.bls.gov/regions/mountain-plains/kansas.htm",
    "category": "wellbeing",
    "description": "Regional CPI context alongside local housing/income observations",
    "geography": "Published region/metro series, not every county",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "Do not relabel Midwest CPI as measured Kansas county cost of living Use consistent index/base and do not compare index levels across incompatible series",
    "tags": [
      "Official release links/API"
    ]
  },
  {
    "id": "ks-kdhe-brfss",
    "title": "Kansas health and well-being survey methods",
    "organization": "Kansas Department of Health and Environment",
    "url": "https://www.kdhe.ks.gov/1738/Technical-Notes",
    "category": "wellbeing",
    "description": "Understand the Kansas Behavioral Risk Factor Surveillance System survey.",
    "geography": "State and qualified survey domains",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "A county happiness series has not been established. Check the question, year, sample design, weights, and uncertainty before comparing places."
  },
  {
    "id": "oecd-wellbeing-methods",
    "title": "How to measure subjective well-being",
    "organization": "OECD",
    "url": "https://www.oecd.org/en/publications/oecd-guidelines-on-measuring-subjective-well-being-2025-update_9203632a-en.html",
    "category": "wellbeing",
    "description": "Guidance for separating life satisfaction, affect, and meaning in survey design.",
    "geography": "Measurement guidance; no Kansas observations",
    "checkedAt": "2026-10-24",
    "status": "page-verified",
    "limitation": "This is a methods reference, not a Kansas happiness dataset. Voluntary website responses cannot represent the population."
  }
];
