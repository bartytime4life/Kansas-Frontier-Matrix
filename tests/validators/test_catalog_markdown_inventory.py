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

    def test_indented_code_is_not_visible_inventory(self) -> None:
        text = "\n".join(
            [
                "visible-before",
                "    | hidden-four-space |",
                "  \t| hidden-tab-stop |",
                "\t| hidden-tab |",
                "   | visible-three-space |",
                "    ",
                "visible-after",
            ]
        )

        self.assertEqual(
            [line for _, _, line in visible_line_spans(text)],
            [
                "visible-before",
                "   | visible-three-space |",
                "    ",
                "visible-after",
            ],
        )

    def test_unterminated_fences_fail_closed_with_stable_offsets(self) -> None:
        cases = (
            ("visible\n```example\nhidden\n", "```", len("visible\n")),
            ("  ~~~~ example\nhidden", "~~~~", 0),
        )

        for text, fence, offset in cases:
            with self.subTest(fence=fence):
                with self.assertRaisesRegex(
                    ValueError,
                    rf"^unterminated Markdown fence {fence!r} at offset {offset}$",
                ):
                    visible_line_spans(text)

    def test_backtick_fence_info_rejects_backticks_with_stable_offset(self) -> None:
        text = "visible\n```language`variant\nhidden\n```\n"

        with self.assertRaisesRegex(
            ValueError,
            rf"^backtick fence info contains backtick at offset {len('visible\n')}$",
        ):
            visible_line_spans(text)

    def test_tilde_fence_info_may_contain_backticks(self) -> None:
        text = "~~~ language`variant\nhidden\n~~~\nvisible\n"

        self.assertEqual(
            [line for _, _, line in visible_line_spans(text)],
            ["visible"],
        )

    def test_html_comment_blocks_are_not_visible_inventory(self) -> None:
        text = "\n".join(
            [
                "visible-before",
                "  <!--",
                "## Hidden inventory",
                "| hidden |",
                "  --> trailing hidden text",
                "<!-- hidden on one line -->",
                "inline <!-- remains bounded text -->",
                "visible-after",
            ]
        )

        self.assertEqual(
            [line for _, _, line in visible_line_spans(text)],
            [
                "visible-before",
                "inline <!-- remains bounded text -->",
                "visible-after",
            ],
        )

    def test_unterminated_html_comment_fails_closed_with_stable_offset(self) -> None:
        text = "visible\n<!-- hidden inventory\n| hidden |\n"

        with self.assertRaisesRegex(
            ValueError,
            rf"^unterminated Markdown HTML comment at offset {len('visible\n')}$",
        ):
            visible_line_spans(text)

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
                with self.assertRaisesRegex(ValueError, "unterminated Markdown fence"):
                    module._visible_line_spans("visible\n```example\nhidden\n")
                with self.assertRaisesRegex(
                    ValueError, "backtick fence info contains backtick"
                ):
                    module._visible_line_spans("```language`variant\n```\n")
                self.assertEqual(
                    module._visible_line_spans("    | hidden |\n| visible |\n"),
                    [(15, 26, "| visible |")],
                )
                with self.assertRaisesRegex(
                    ValueError, "unterminated Markdown HTML comment"
                ):
                    module._visible_line_spans("<!-- hidden inventory\n| hidden |\n")


if __name__ == "__main__":
    unittest.main()
