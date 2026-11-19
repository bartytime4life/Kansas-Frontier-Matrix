"""Closed NLCD candidate schemas reject vacuous objects and authority overclaims without GDAL."""
from copy import deepcopy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[4]
SCHEMAS = ROOT / 'schemas/contracts/v1/domains/habitat'
FIXTURES = ROOT / 'fixtures/domains/habitat/nlcd_ingest'


def validators():
    schemas = [json.loads((SCHEMAS / path).read_text()) for path in
               ('land_cover/class_scheme.schema.json', 'land_cover/observation.schema.json', 'land_cover_observation.schema.json')]
    registry = Registry().with_resources((schema['$id'], Resource.from_contents(schema)) for schema in schemas)
    return [Draft202012Validator(schema, registry=registry, format_checker=FormatChecker()) for schema in schemas]


def test_closed_schema_and_legacy_reference_are_strict():
    for validator in validators():
        Draft202012Validator.check_schema(validator.schema)
        assert not validator.is_valid({})
        assert not validator.is_valid({'anything': 'previously accepted'})


@pytest.mark.parametrize('name', ['base', 'changed'])
def test_both_sealed_packets_conform_without_raster_dependencies(name):
    packet = json.loads((FIXTURES / (name + '.json')).read_text())
    scheme, observation, legacy = validators()
    assert scheme.is_valid(packet['class_scheme'])
    assert observation.is_valid(packet['expected_candidate'])
    assert legacy.is_valid(packet['expected_candidate'])


@pytest.mark.parametrize('field', ['source_admitted', 'review_completed', 'policy_evaluated', 'lifecycle_write', 'promotion_authorized', 'release_authorized', 'publication_authorized', 'public_use_allowed'])
def test_false_authority_flags_are_machine_enforced(field):
    packet = json.loads((FIXTURES / 'base.json').read_text())
    scheme, observation, _ = validators()
    profile = deepcopy(packet['class_scheme'])
    candidate = deepcopy(packet['expected_candidate'])
    profile['governance'][field] = candidate['governance'][field] = True
    assert not scheme.is_valid(profile)
    assert not observation.is_valid(candidate)


def test_unknown_fields_and_invalid_times_are_not_accepted():
    packet = json.loads((FIXTURES / 'base.json').read_text())
    scheme, observation, _ = validators()
    packet['class_scheme']['new_authority'] = 'approved'
    assert not scheme.is_valid(packet['class_scheme'])
    packet['expected_candidate']['retrieved_at'] = 'not-a-time'
    assert not observation.is_valid(packet['expected_candidate'])
