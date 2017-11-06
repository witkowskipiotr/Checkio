import unittest

from code_2017_11_06.split_strings import split_strings_to_two_char


class SplitStringsTest(unittest.TestCase):

    def test_basic_check(self):
        self.assertEqual(split_strings_to_two_char(text='asdfadsf'), ['as', 'df', 'ad', 'sf'])
        self.assertEqual(split_strings_to_two_char(text='asdfads_'), ['as', 'df', 'ad', 's_'])
        self.assertEqual(split_strings_to_two_char(text=''), [])
        self.assertEqual(split_strings_to_two_char(text='x_'), ['x_'])

    def test_longer_split_string(self):
        self.assertEqual(split_strings_to_two_char(
            text='jmbrmbcpaisbjjfpvszjwcjdommiylzcnbydkoabtjfgvqlaomuzonfgkkgxuexhntlfyjzu'),
            ['jm', 'br', 'mb', 'cp', 'ai', 'sb', 'jj', 'fp', 'vs', 'zj', 'wc', 'jd',
             'om', 'mi', 'yl', 'zc', 'nb', 'yd', 'ko', 'ab', 'tj', 'fg', 'vq', 'la',
             'om', 'uz', 'on', 'fg', 'kk', 'gx', 'ue', 'xh', 'nt', 'lf', 'yj', 'zu'])
        self.assertEqual(split_strings_to_two_char(text='ckbuavlpgllldudmdwug'),
                         ['ck', 'bu', 'av', 'lp', 'gl', 'll', 'du', 'dm', 'dw', 'ug'])
        self.assertEqual(split_strings_to_two_char(
            text='impmsdjhgvjtrbksab'),
            ['im', 'pm', 'sd', 'jh', 'gv', 'jt', 'rb', 'ks', 'ab'])
