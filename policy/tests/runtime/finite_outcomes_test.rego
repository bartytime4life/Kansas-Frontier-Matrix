package kfm.runtime_test

import data.kfm.runtime

test_default_outcome_abstain {
  runtime.outcome == "ABSTAIN"
}
