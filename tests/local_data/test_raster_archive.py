"""Archive bytes, bounded inspection and measured descriptions must agree."""
import gzip
import io
import json
from pathlib import Path
import struct
import tarfile
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import raster_archive as r,ai_acceptance as ai,grounded_review as g,intake,intake_review,manage


def archive_bytes(values=(1.,2.,-9999.,4.), *, rows=2, byteorder='I', extra=None):
    header=(f'BYTEORDER {byteorder}\nLAYOUT BIL\nNROWS {rows}\nNCOLS 2\nNBANDS 1\nNBITS 32\n'
        'PIXELTYPE FLOAT\nULXMAP -100\nULYMAP 39\nXDIM 0.1\nYDIM 0.1\nNODATA -9999\n')
    files={'sample_KS.bil':struct.pack(('<' if byteorder=='I' else '>')+'f'*len(values),*values),
        'sample_KS.hdr':header.encode(),'sample.prj':b'GEOGCS["NAD83",UNIT["Degree",0.017453292519943295]]',
        'sample.info.txt':b'PRISM_DATASET_REMARKS: Modeled precipitation grid; retained Kansas window.\n'}
    files.update(extra or {})
    raw=io.BytesIO()
    with tarfile.open(fileobj=raw,mode='w') as tar:
        for name,body in files.items():
            entry=tarfile.TarInfo(name);entry.size=len(body);tar.addfile(entry,io.BytesIO(body))
    return gzip.compress(raw.getvalue())


class RasterArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'prism.tar.gz'

    def inspect(self,body=None):
        self.path.write_bytes(body or archive_bytes());return r.inspect(self.path)

    def test_full_crc_shape_projection_and_cell_checks_are_measured(self):
        x=self.inspect();i=x['inspection'];self.assertTrue(i['crc_validated']);self.assertTrue(i['structure_validated'])
        self.assertEqual(i['grid']['valid_cells'],3);self.assertEqual(i['grid']['nodata_cells'],1)
        self.assertEqual(i['grid']['stored_minimum'],1);self.assertEqual(i['grid']['stored_maximum'],4)
        self.assertAlmostEqual(i['grid']['header_coordinate_bounds'][0],-100.05)
        self.assertIn('NAD83',i['grid']['projection_wkt']);self.assertIn('Modeled precipitation',x['text'])
        self.assertFalse((self.path.parent/'sample_KS.bil').exists())

    def test_big_endian_values_are_decoded_using_the_header(self):
        self.assertEqual(self.inspect(archive_bytes(byteorder='M'))['inspection']['grid']['stored_maximum'],4)

    def test_variable_comes_from_saved_provider_metadata_and_keeps_its_interpretation_basis(self):
        body=archive_bytes(extra={'sample.info.txt':b'PRISM_DATASET_FILENAME: prism_ppt_us_25m_20261118.bil\n'})
        variable=self.inspect(body)['inspection']['provider_variable']
        self.assertEqual(variable['code'],'ppt');self.assertEqual(variable['documented_units'],'mm')
        self.assertIn('unverified',variable['interpretation_basis'])

    def test_truncated_gzip_cannot_pass_the_archive_check(self):
        x=self.inspect(archive_bytes()[:-7]);self.assertFalse(x['inspection']['structure_validated'])
        self.assertFalse(x['inspection']['crc_validated'])

    def test_shape_mismatch_nonfinite_and_all_nodata_are_held(self):
        for body in (archive_bytes(rows=3),archive_bytes((1.,float('nan'),3.,4.)),archive_bytes((-9999.,)*4)):
            with self.subTest(body=body[:4]):self.assertFalse(self.inspect(body)['inspection']['structure_validated'])

    def test_archive_expansion_limit_is_enforced(self):
        with patch.object(r,'EXPANDED_LIMIT',100):
            self.assertIn('RASTER_ARCHIVE_EXPANSION_LIMIT',self.inspect()['inspection']['issues'])

    def test_traversal_names_and_unsupported_files_are_rejected_without_extraction(self):
        for name in ('../escape.txt','/escape.txt','run.sh','C:/escape.info.txt','bad\nname.info.txt'):
            self.assertFalse(self.inspect(archive_bytes(extra={name:b'payload'}))['inspection']['structure_validated'])
        self.assertFalse((self.path.parent/'escape.txt').exists())

    def test_archive_links_are_rejected(self):
        raw=io.BytesIO()
        with tarfile.open(fileobj=raw,mode='w') as tar:
            member=tarfile.TarInfo('link.info.txt');member.type=tarfile.SYMTYPE;member.linkname='/etc/passwd';tar.addfile(member)
        self.assertIn('RASTER_ARCHIVE_UNSAFE_MEMBER',self.inspect(gzip.compress(raw.getvalue()))['inspection']['issues'])

    def test_multiple_gzip_members_are_not_reported_as_one_complete_grid(self):
        x=self.inspect(archive_bytes()+gzip.compress(b'extra'))
        self.assertIn('RASTER_ARCHIVE_TRAILING_OR_MULTIPLE_MEMBERS',x['inspection']['issues'])

    def test_packet_and_rendering_describe_metadata_not_ocr_or_verified_weather(self):
        root=Path(self.temp.name)/'store';manage.init_store(root)
        path=root/'data/raw/prism.tar.gz';path.write_bytes(archive_bytes());intake.analyze(root)
        item=intake.get_item(root,intake.item_id('raw','prism.tar.gz'));packet=ai.packet_for(root,item)
        self.assertEqual(packet['description_policy'],g.ARCHIVE_VERSION)
        self.assertFalse(any(f['id']=='gzip_inspection' for f in packet['facts']))
        selected={'title_ids':[],'passage_ids':['passage_1'],'domain':'atmosphere',
            'recommendation':'accept_local','confidence':'high','concern_codes':[]}
        result,rendering=g.render(selected,packet,g.inspection_for(packet))
        self.assertIn('Archive metadata text',result['description']);self.assertNotIn('OCR',result['description'])
        self.assertIn('not independently certified',result['description']);self.assertEqual(ai.validate_output(result,packet),result)
        self.assertEqual(rendering['version'],g.ARCHIVE_VERSION)
        result['description']=result['description'].replace('3 valid cells','4 valid cells')
        with self.assertRaisesRegex(ValueError,'SCOPE_RENDERING_CHANGED'):ai.validate_output(result,packet)

    def owner_run(self,body):
        from tools.local_data.smart_intake import SmartManager
        from tests.local_data.test_recorded_review import Reviewer
        import hashlib
        root=Path(self.temp.name)/'owner-store';manage.init_store(root)
        path=root/'data/raw/prism.tar.gz';path.write_bytes(body);intake.analyze(root)
        item=intake.get_item(root,intake.item_id('raw','prism.tar.gz'))
        bindings={item['id']:{'sha256':item['sha256'],'context':intake_review.context(item)}}
        policy={'schema':'kfm-owner-private-reference-v1','scope':'private-reference-only','requested_by':'Test owner',
            'authorized_at':manage.utc_now(),'request':'Retain this exact file privately.','items':bindings}
        raw=manage.canonical(policy);digest=hashlib.sha256(raw).hexdigest();p=root/'data/work/intake/owner-policies'/(digest+'.json');p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
        manager=SmartManager(root,Reviewer(),owner_policy=digest)
        manager.start_owner_selection(bindings);manager.thread.join(10)
        return root,path,manager,bindings

    def test_owner_request_accepts_a_valid_grid_with_model_uncertainty_retained(self):
        original=archive_bytes();root,path,manager,bindings=self.owner_run(original)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1});self.assertEqual(path.read_bytes(),original)
        item=intake.get_item(root,next(iter(bindings)))
        self.assertEqual(item['ai_review']['recommendation'],'hold')
        self.assertTrue(item['ai_review']['attribution']['archive_inspection']['structure_validated'])
        self.assertIn('REVIEWED_LOCAL_ONLY',item['decision']['holds'])

    def test_owner_request_does_not_accept_a_grid_with_invalid_shape_or_retry_it_forever(self):
        root,path,manager,bindings=self.owner_run(archive_bytes(rows=3))
        self.assertEqual(manager.status()['job']['counts'],{'held':1})
        self.assertEqual(intake.get_item(root,next(iter(bindings)))['status'],'review')
        self.assertFalse(manager.start_owner_selection(bindings))

    def test_empty_gzip_is_labeled_as_inspection_availability_and_old_rendering_remains_valid(self):
        root=Path(self.temp.name)/'empty-store';manage.init_store(root)
        path=root/'data/raw/empty.txt.gz';path.write_bytes(gzip.compress(b''));intake.analyze(root)
        packet=ai.packet_for(root,intake.get_item(root,intake.item_id('raw','empty.txt.gz')))
        self.assertEqual(packet['description_policy'],g.AVAILABILITY_VERSION)
        value={'title_ids':[],'passage_ids':['no_readable_text'],'domain':'unassigned',
            'recommendation':'hold','confidence':'low','concern_codes':[]}
        result,rendering=g.render(value,packet,g.inspection_for(packet));self.assertIn('KFM inspection:',result['description'])
        self.assertEqual(rendering['method'],'KFM-measured text availability and scope; Qwen-selected metadata context')
        self.assertNotIn('Source text (',result['description']);ai.validate_output(result,packet)
        packet['description_policy']=g.VERSION
        old,_=g.render(value,packet,g.inspection_for(packet));self.assertIn('Source text (',old['description']);ai.validate_output(old,packet)


if __name__=='__main__':unittest.main()
