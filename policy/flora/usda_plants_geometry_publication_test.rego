package kfm.flora.usda_plants_geometry_publication_test
import rego.v1
import data.kfm.flora.usda_plants_geometry_publication
test_valid if {count(usda_plants_geometry_publication.deny with input as {"approval":{"approver":{"approver_type":"human"}}})==0}
