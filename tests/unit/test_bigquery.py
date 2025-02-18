#  python -m unittest discover -s tests/unit
import re
import unittest
import pytest
import vcr
from tests.unit import mocked_bigquery
from tests.unit.testing_helpers import assert_log_msg_exists


@pytest.mark.usefixtures("mocker")
class TestBigQuery(unittest.TestCase):

    def setUp(self):
        pass

    @pytest.fixture(autouse=True)
    def init_mocker(self, mocker):
        print('init_mocker')
        self.mocker = mocker

    def test_one(self):
        from tests.unit.testing_helpers import setup_logging, setup_kensu_tracker
        setup_logging()
        setup_kensu_tracker(test_cls=self,
                            bigquery_support=True,
                            report_in_mem=False,
                            compute_stats=False  # FIXME: stats testing disabled for now... :(
                            )
        from kensu.google.cloud import bigquery as kensu_bigquery
        mocked_bigquery.mock(self.mocker)

        with vcr.use_cassette('fixtures/recorded_requests/remote_lineage_service.yaml'):
            client = kensu_bigquery.Client()
            q = client.query(mocked_bigquery.sample_sql)
            df = q.to_dataframe()
            df.to_csv('test_res_from_bigquery')

            in_ds = {
                # uri => short_name
                'bigquery://projects/psyched-freedom-306508/datasets/cf/tables/ARG-tickets': 'tables/ARG-tickets',
                'bigquery://projects/psyched-freedom-306508/datasets/cf/tables/ARG-stores': 'tables/ARG-stores'
            }
            out_ds = {
                # only suffix checked now...
                re.compile(r'"([^"]+)kensu-py/tests/unit/test_res_from_bigquery"'): 'unit/test_res_from_bigquery'
            }
            lineage_name = 'Lineage to unit/test_res_from_bigquery from tables/ARG-stores,tables/ARG-tickets'
            # p.s. these can be extracted as helpers, we'll see
            assert_log_msg_exists(lineage_name)
            for ds_uri, ds_name in ({**out_ds, **in_ds}).items():
                assert_log_msg_exists('DATA_SOURCE', ds_name, ds_uri, full_str_match=True)
                assert_log_msg_exists('SCHEMA', 'schema:' + ds_name, full_str_match=True)
            # FIXME: check that 'TestBigQuery.jsonl' contains  DATA_STATS (stats disabled now, harder to mock bigquery)



if __name__ == '__main__':
    unittest.main()
