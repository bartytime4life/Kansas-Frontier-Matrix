package kfm.flora.usda_plants_geometry_publication
import rego.v1
deny contains "USDA_PLANTS_GEOMETRY_APPROVAL_MISSING" if not input.approval
deny contains "USDA_PLANTS_GEOMETRY_NON_HUMAN_APPROVAL" if input.approval.approver.approver_type != "human"
