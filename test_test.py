import unittest
from test import calc_tashizan

class Test_tashizan(unittest.TestCase):
    def test_tashizan(self):
        """
        test method for tashizanr
        """
        value1 = 2
        value2 = 6
        expected = 8
        actual = calc_tashizan(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
