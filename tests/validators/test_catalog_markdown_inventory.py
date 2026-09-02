from __future__ import annotations

import unittest

from tools.validators.catalog._markdown_inventory import visible_line_spans
from tools.validators.catalog import (
    validate_catalog_child_index,
    validate_catalog_domain_child_index,
    validate_catalog_domain_compatibility_redirect,
    validate_crosswalk_registry_inventory,
    validate_layer_registry_discovery_index,
    validate_source_registry_paired_discovery_index,
)


class CatalogMarkdownInventoryTests(unittest.TestCase):
    def test_visible_lines_preserve_original_offsets_and_line_endings(self) -> None:
        text = "before\r\n```example\r\ninside\r\n```\r\nafter\n"

        self.assertEqual(
            visible_line_spans(text),
            [
                (0, len("before"), "before"),
                (text.index("after"), text.index("after") + len("after"), "after"),
            ],
        )

    def test_fence_matching_respects_character_length_and_indentation(self) -> None:
        text = "\n".join(
            [
                "visible-before",
                "  ~~~~ example",
                "hidden-one",
                "```",
                "hidden-two",
                " ~~~~~ ",
                "visible-after",
            ]
        )

        self.assertEqual(
            [line for _, _, line in visible_line_spans(text)],
            ["visible-before", "visible-after"],
        )

    def test_four_space_fence_is_visible_markdown(self) -> None:
        text = "    ```\nvisible\n"

        self.assertEqual(
            [line for _, _, line in visible_line_spans(text)],
            ["    ```", "visible"],
        )

    def test_all_inventory_validators_share_the_canonical_scanner(self) -> None:
        modules = (
            validate_catalog_child_index,
            validate_catalog_domain_child_index,
            validate_catalog_domain_compatibility_redirect,
            validate_crosswalk_registry_inventory,
            validate_layer_registry_discovery_index,
            validate_source_registry_paired_discovery_index,
        )

        for module in modules:
            with self.subTest(module=module.__name__):
                self.assertIs(module._visible_line_spans, visible_line_spans)


if __name__ == "__main__":
    unittest.main()
