import unittest

from oreilly.cipher_map import decode_part_text, rotate_tuple_90_degrees, recall_ciphered_password


class CheckioTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            [('X...', '..X.', 'X..X', '....'), ('itdf', 'gdce', 'aton', 'qrdi')],
            [('....', 'X..X', '.X..', '...X'), ('xhwc', 'rsqx', 'xqzz', 'fyzr')],
            [('....', '....', '....', '....'), ('xhwc', 'rsqx', 'xqzz', 'fyzr')],
            [('XXXX', 'XXXX', 'XXXX', 'XXXX'), ('xhwc', 'rsqx', 'xqzz', 'fyzr')]
        ]
        self.rotate_90 = [
            ('.X.X', '....', '..X.', '.X..'),
            ('..X.', '.X..', '....', 'X.X.'),
            ('....', '....', '....', '....'),
            ('XXXX', 'XXXX', 'XXXX', 'XXXX')
        ]
        self.value = ["icantforgetiddqd",
                      "rxqrwsfzxqxzhczy",
                      "",
                      "xhwcrsqxxqzzfyzrxhwcrsqxxqzzfyzrxhwcrsqxxqzzfyzrxhwcrsqxxqzzfyzr"]

    def test_decode_part_text_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(decode_part_text(data[0], data[1]),
                             self.value[i][:len(self.value[i])//4])

    def test_cipher_map_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(recall_ciphered_password(data[0], data[1]), self.value[i])

    def test_rotate_tuple_90_equal(self):
        for i, data in enumerate(self.data):
            self.assertEqual(rotate_tuple_90_degrees(data[0]), self.rotate_90[i])
