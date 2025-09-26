# Run a single collection with COLLECTION=name (file stem) or all if unset
# If a script doesn't implement 'build', fallback to: fetch→unpack→process→stac→validate→render
collections-build:
	@if [ -n "$(COLLECTION)" ]; then \
	  f="$(COLLECTIONS_DIR)/$(COLLECTION).sh"; \
	  if [ ! -f "$$f" ]; then echo "Collection script not found: $$f"; exit 1; fi; \
	  if grep -qE '(^|\s)build\)' "$$f"; then \
	    echo "==> $$f build"; bash "$$f" build; \
	  else \
	    echo "==> $$f (default pipeline)"; \
	    bash "$$f" fetch   || true; \
	    bash "$$f" unpack  || true; \
	    bash "$$f" process || true; \
	    bash "$$f" stac    || true; \
	    bash "$$f" validate|| true; \
	    bash "$$f" render  || true; \
	  fi; \
	else \
	  if [ -z "$(COLLECTION_SCRIPTS)" ]; then echo "No collection scripts in $(COLLECTIONS_DIR)"; exit 0; fi; \
	  set -e; \
	  for f in $(COLLECTION_SCRIPTS); do \
	    if grep -qE '(^|\s)build\)' "$$f"; then \
	      echo "==> $$f build"; bash "$$f" build; \
	    else \
	      echo "==> $$f (default pipeline)"; \
	      bash "$$f" fetch   || true; \
	      bash "$$f" unpack  || true; \
	      bash "$$f" process || true; \
	      bash "$$f" stac    || true; \
	      bash "$$f" validate|| true; \
	      bash "$$f" render  || true; \
	    fi; \
	  done; \
	fi

collections-validate:
	@if [ -n "$(COLLECTION)" ]; then \
	  f="$(COLLECTIONS_DIR)/$(COLLECTION).sh"; \
	  if [ ! -f "$$f" ]; then echo "Collection script not found: $$f"; exit 1; fi; \
	  if grep -qE '(^|\s)validate\)' "$$f"; then \
	    echo "==> $$f validate"; bash "$$f" validate; \
	  else \
	    echo "==> $$f (validate fallback)"; \
	    bash "$$f" stac || true; \
	    bash "$$f" validate || true; \
	  fi; \
	else \
	  if [ -z "$(COLLECTION_SCRIPTS)" ]; then echo "No collection scripts in $(COLLECTIONS_DIR)"; exit 0; fi; \
	  set -e; \
	  for f in $(COLLECTION_SCRIPTS); do \
	    if grep -qE '(^|\s)validate\)' "$$f"; then \
	      echo "==> $$f validate"; bash "$$f" validate; \
	    else \
	      echo "==> $$f (validate fallback)"; \
	      bash "$$f" stac || true; \
	      bash "$$f" validate || true; \
	    fi; \
	  done; \
	fi

collections-render:
	@if [ -n "$(COLLECTION)" ]; then \
	  f="$(COLLECTIONS_DIR)/$(COLLECTION).sh"; \
	  if [ ! -f "$$f" ]; then echo "Collection script not found: $$f"; exit 1; fi; \
	  if grep -qE '(^|\s)render\)' "$$f"; then \
	    echo "==> $$f render"; bash "$$f" render; \
	  else \
	    echo "==> $$f (render fallback: site-config)"; \
	    $(MAKE) site-config; \
	  fi; \
	else \
	  if [ -z "$(COLLECTION_SCRIPTS)" ]; then echo "No collection scripts in $(COLLECTIONS_DIR)"; exit 0; fi; \
	  set -e; \
	  for f in $(COLLECTION_SCRIPTS); do \
	    if grep -qE '(^|\s)render\)' "$$f"; then \
	      echo "==> $$f render"; bash "$$f" render; \
	    else \
	      echo "==> $$f (render fallback: site-config)"; \
	      $(MAKE) site-config; \
	    fi; \
	  done; \
	fi
