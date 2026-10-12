# `ValidatorAssuranceReport` synthetic fixtures

Valid cases cover:

- all assessable mutants killed (`PASS`);
- one unreviewed medium-risk survivor (`HOLD`);
- one high-risk survivor (`FAIL`); and
- a campaign timeout (`ERROR`).

Invalid cases bind exact finding codes for hash failures, noncanonical operators, count/rate inconsistencies, survivor-inventory and risk-count drift, inconsistent finite outcomes, forbidden universal thresholds, time-order failure, and governance overclaim.

No mutant is executed by these fixtures. All validator, test, issue, campaign, and run references are synthetic.
