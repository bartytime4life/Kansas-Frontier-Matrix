.PHONY: bootstrap validate-schemas test dev-up sample-ingest catalog-validate

bootstrap:
	./scripts/bootstrap.sh

validate-schemas:
	python3 ./scripts/validate_schemas.py

test:
	python3 -m unittest discover -s tests/contracts -p 'test_*.py' -v

dev-up:
	./scripts/dev_up.sh

sample-ingest:
	./scripts/sample_ingest.sh ${SOURCE}

catalog-validate:
	python3 ./scripts/catalog_validate.py
