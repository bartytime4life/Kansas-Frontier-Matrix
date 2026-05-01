package fauna.gbif_review_release

deny contains "review item missing publication_package_id" if { input.kind=="review_item"; not input.doc.publication_package_id }
