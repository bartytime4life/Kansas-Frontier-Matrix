"""Source selections cannot become invented history or model-authored scope."""
import json
import unittest

from tools.local_data import grounded_review as g


class GroundedReviewTests(unittest.TestCase):
    def setUp(self):
        self.text=('GENERAL ORDERS\n\nWAR DEPARTMENT\n\nNo. 50.\n\n'
            'The Department of Kansas is hereby restored. To include the State of Kansas.\n\n'
            'OCR dates: 1850. June 29, 185(5. Names and dates need verification.')
        self.inspection={'text_characters':len(self.text),'expanded_bytes':49152,'compressed_bytes_read':32768,
            'text_truncated':True,'crc_validated':False,'issues':[],'first_member_complete':False}
        self.packet={'facts':[{'id':'gzip_text_1','text':self.text},
            {'id':'gzip_inspection','text':json.dumps(self.inspection)}],
            'allowed_domains':['unassigned','agriculture']}
        self.value={'title_ids':['title_1'],'passage_ids':['passage_1'],'domain':'unassigned',
            'recommendation':'hold','confidence':'medium','concern_codes':['noisy_text']}

    def test_department_and_noisy_dates_remain_quoted_unverified_transcriptions(self):
        review,proof=g.render(self.value,self.packet,self.inspection)
        self.assertIn('The Department of Kansas is hereby restored',review['description'])
        self.assertNotIn('restored the State of Kansas',review['description'])
        self.assertIn('185(5',review['description'])
        self.assertIn('assertions, names and dates unverified',review['description'])
        self.assertEqual(proof['scope_text'],g.scope(self.inspection))
        g.validate_rendered(review,self.packet,self.inspection)

    def test_unreached_crc_is_not_rendered_as_invalid_or_full_decoding(self):
        review,_=g.render(self.value,self.packet,self.inspection)
        self.assertIn('CRC was not reached and was not validated',review['description'])
        self.assertNotIn('invalid CRC',review['description'])
        self.assertNotIn('fully decoded',review['description'])

    def test_complete_member_can_still_have_truncated_supplied_text(self):
        self.inspection.update(first_member_complete=True,crc_validated=True,text_truncated=True)
        text=g.scope(self.inspection)
        self.assertIn('bounded prefix',text);self.assertIn('CRC was validated',text)

    def test_detected_stream_error_does_not_assert_a_specific_crc_failure(self):
        self.inspection['issues']=['GZIP_INVALID_OR_TRUNCATED']
        text=g.scope(self.inspection)
        self.assertIn('gzip error or incomplete stream',text)
        self.assertNotIn('invalid CRC',text)

    def test_model_wire_contains_no_scope_path_or_review_date_to_misinterpret(self):
        self.packet['facts'] += [{'id':'path','text':'misleading-1901.gz'},{'id':'format','text':'gzip'}]
        wire=json.dumps(g.model_packet(self.packet))
        for forbidden in ('49152','CRC','misleading-1901','gzip_inspection'):
            self.assertNotIn(forbidden,wire)

    def test_numeric_ocr_headings_are_not_offered_as_titles(self):
        titles,_=g.choices(self.packet)
        self.assertTrue(titles)
        self.assertTrue(all(not any(c.isdigit() for c in text) for text in titles.values()))

    def test_model_cannot_inject_history_or_technical_prose(self):
        for bad in ({**self.value,'description':'The State of Kansas was restored.'},
                    {**self.value,'passage_ids':['invented_source']},
                    {**self.value,'title_ids':['1901']},
                    {**self.value,'concern_codes':['invalid CRC']}):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):g.render(bad,self.packet,self.inspection)

    def test_normalized_body_or_evidence_tampering_is_rejected(self):
        review,_=g.render(self.value,self.packet,self.inspection)
        for key,bad in [('description',review['description'].replace('Department of Kansas','State of Kansas')),
                        ('title','1867 historical document'),('concerns',['The CRC is invalid'])]:
            with self.assertRaises(ValueError):g.validate_rendered({**review,key:bad},self.packet,self.inspection)

    def test_no_readable_text_uses_explicit_placeholder_and_no_title_choices(self):
        packet={**self.packet,'facts':[]}
        value={**self.value,'title_ids':[],'passage_ids':['no_readable_text']}
        review,_=g.render(value,packet,self.inspection)
        self.assertIn('recovered no readable text',review['description'])
        self.assertEqual(g.schema(packet)['properties']['title_ids']['maxItems'],0)


if __name__=='__main__':unittest.main()
