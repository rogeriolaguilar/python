import isp_maps_template as subject
import unittest


class TestIspMapsTemplate(unittest.TestCase):
    def setUp(self):
        self.codeinfo = {
            "codefile": "isp_country_codes.csv",
            "separator": ",",
            "quote": '"',
            "plot_codes": "ISO3166-1-Alpha-2",
            "data_codes": "ISO3166-1-Alpha-3"
        }

    def test_build_country_code_converter(self):
        result = subject.build_country_code_converter(self.codeinfo)
        self.assertEqual(result['AD'], 'AND')
        self.assertEqual(result['BR'], 'BRA')


if __name__ == '__main__':
    unittest.main()