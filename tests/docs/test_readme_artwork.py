"""Focused, offline source regressions for the linked-document artwork.

These checks guard concrete accessibility/authority defects. They do not claim
browser, screen-reader, forced-colors, design approval, or release acceptance.
"""
from __future__ import annotations

import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / 'docs/brand/readme'
NS = {'s': 'http://www.w3.org/2000/svg'}
NEW = (
    'banner-brand', 'banner-changelog', 'banner-code-of-conduct',
    'banner-domain-atlas', 'banner-feature-matrix', 'banner-free-data-acquisition',
    'banner-installation', 'banner-lifecycle-law', 'banner-local-data-store',
    'banner-local-data-tools', 'banner-security', 'banner-sensitive-material',
    'banner-trust-membrane', 'banner-verification-backlog',
    'domain-constellation', 'install-paths', 'local-store-flow', 'sensitive-dispositions',
)
REUSED = ('trust-membrane', 'trust-path', 'capability-board', 'layer-stack',
          'time-depth', 'contributor-paths')
STATIC = ('banner-brand', 'banner-domain-atlas', 'banner-lifecycle-law', 'banner-trust-membrane',
          'banner-verification-backlog', 'banner-sensitive-material',
          'sensitive-dispositions', 'trust-path', 'trust-membrane', 'capability-board')


def variants(names):
    return [ART / f'kfm-{name}{mode}.svg' for name in names for mode in ('', '-dark')]


class ReadmeArtworkTests(unittest.TestCase):
    def test_autoplay_is_bounded_and_reduced_motion_is_present(self):
        for p in variants(NEW + REUSED):
            with self.subTest(asset=p.name):
                source = p.read_text()
                self.assertNotIn('infinite', source)
                animations = re.findall(r'(?<!-)animation\s*:\s*([^;}]+)', source)
                for animation in animations:
                    if animation.strip().startswith('none'):
                        continue
                    seconds = [float(n) / (1000 if unit == 'ms' else 1)
                               for n, unit in re.findall(r'([\d.]+)(ms|s)\b', animation)]
                    self.assertTrue(seconds, animation)
                    self.assertLessEqual(sum(seconds), 4, animation)
                    self.assertRegex(animation, r'\b1\b.*\b(?:both|forwards)\b')
                # Inline delays can extend autoplay beyond its declared duration.
                for delay in re.findall(r'animation-delay\s*:\s*([-\d.]+)s', source):
                    self.assertLessEqual(float(delay), 0, delay)
                if animations:
                    self.assertIn('prefers-reduced-motion: reduce', source)

    def test_governance_and_brand_signals_are_static(self):
        for p in variants(STATIC):
            with self.subTest(asset=p.name):
                source = p.read_text()
                self.assertNotRegex(source, r'\banimation\s*:|@keyframes|<animate')
        for p in variants(('banner-lifecycle-law', 'trust-path')):
            with self.subTest(asset=p.name):
                self.assertNotRegex(p.read_text(), r'class="(?:tok|t[123])(?:[\s"]|$)')
        for p in variants(('banner-verification-backlog',)):
            self.assertNotIn('class="mv"', p.read_text())

    def test_graphics_have_accessible_names_and_no_active_or_remote_content(self):
        for p in variants(NEW + REUSED):
            with self.subTest(asset=p.name):
                root = ET.parse(p).getroot()
                self.assertEqual(root.attrib.get('role'), 'img')
                ids = {e.attrib.get('id'): e for e in root.iter() if 'id' in e.attrib}
                for key in root.attrib.get('aria-labelledby', '').split():
                    self.assertTrue(''.join(ids[key].itertext()).strip())
                self.assertTrue(root.find('s:title', NS).text)
                self.assertTrue(root.find('s:desc', NS).text)
                for e in root.iter():
                    self.assertNotIn(e.tag.rsplit('}', 1)[-1], ('script', 'foreignObject', 'animate', 'animateTransform'))
                    for k, value in e.attrib.items():
                        self.assertFalse(k.startswith('on'), k)
                        if k.rsplit('}', 1)[-1] == 'href':
                            self.assertTrue(value.startswith('#'), value)
                self.assertNotRegex(p.read_text(), r'url\(\s*[\'"]?(?!#)[^\s\)]+|@import')

    def test_non_stale_artwork_does_not_borrow_reserved_colors_or_emoji(self):
        for p in variants(NEW + REUSED):
            with self.subTest(asset=p.name):
                source = p.read_text()
                for color in ('#C9A227', '#9A7A12', '#D9B440', '#DDBB55', '#E3C46A'):
                    self.assertNotIn(color, source)
                root = ET.parse(p).getroot()
                for text in root.findall('.//s:text', NS):
                    value = text.text or ''
                    if not re.search('[A-Za-z0-9]', value):
                        self.assertNotRegex(value, '[\U0001F000-\U0001FAFF\u2600-\u27BF]')

    def test_banner_does_not_invent_a_gold_brand_palette_role(self):
        for p in variants(('banner-brand',)):
            self.assertIn('mute', p.read_text())
            self.assertNotIn('>gold</text>', p.read_text())
            root = ET.parse(p).getroot()
            swatches = root.findall('.//s:g[@class="sw"]/s:rect', NS)
            self.assertEqual(swatches[-1].attrib['fill'], '#B1BAC4' if '-dark' in p.name else '#5E6E7C')

    def test_small_labels_keep_contrasting_light_and_dark_pairs(self):
        def luminance(color):
            values = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
            values = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in values]
            return sum(v * weight for v, weight in zip(values, (.2126, .7152, .0722)))

        def check(foreground, background):
            low, high = sorted((luminance(foreground), luminance(background)))
            self.assertGreaterEqual((high + .05) / (low + .05), 4.5)

        for p in variants(NEW + REUSED):
            with self.subTest(asset=p.name):
                root = ET.parse(p).getroot()
                if '-dark' not in p.name:
                    for text in root.findall('.//s:text', NS):
                        if text.attrib.get('fill') == '#9A7A12':
                            check('#9A7A12', '#FAF7F0')
                if p.name in ('kfm-banner-local-data-store-dark.svg', 'kfm-local-store-flow-dark.svg'):
                    for text in root.findall('.//s:text', NS):
                        if text.text == 'QUARANTINE' or text.text in ('1', '2', '3', '4', '5', '6', 'KFM_DATA_ROOT · private store'):
                            check(text.attrib['fill'], '#D2A06A')
                if p.name == 'kfm-trust-path.svg':
                    for text in root.findall('.//s:text', NS):
                        if text.text == 'released, reversible':
                            check(text.attrib['fill'], '#0B1F3A')
                if p.name == 'kfm-local-store-flow.svg':
                    for text in root.findall('.//s:text', NS):
                        if text.text in ('maps · photos · PDFs', 'read, never moved'):
                            check(text.attrib['fill'], '#F2E6D2')

    def test_sensitive_dispositions_and_terminal_commands_stay_visible(self):
        for p in variants(('sensitive-dispositions', 'banner-installation', 'banner-local-data-tools', 'local-store-flow', 'banner-free-data-acquisition')):
            with self.subTest(asset=p.name):
                source = p.read_text()
                for cls in ('dp', 'mt', 'ln', 'st', 'pk'):
                    self.assertNotRegex(source, rf'\.{cls}\{{[^}}]*animation:(?!none)' )
        for p in variants(('sensitive-dispositions',)):
            root = ET.parse(p).getroot()
            labels = {e.text for e in root.findall('.//s:text', NS)}
            self.assertTrue({'Restricted retention', 'Generalized representation',
                             'Omission', 'Abstention', 'Denial'} <= labels)


if __name__ == '__main__':
    unittest.main()
