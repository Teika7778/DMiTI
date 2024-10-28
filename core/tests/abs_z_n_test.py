import unittest
from data_types import *
from abs_z_n import abs_z_n

class abs_z_n_test(unittest.TestCase):
    def test_valid_integer(self):
        natural = Natural([1, 2, 3])
        integer = Integer(natural, is_positive=True)
        result = abs_z_n(integer)
        self.assertEqual(result, [natural])

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            abs_z_n(Rational(Integer(Natural([2])), Natural([1])))

if __name__ == '__main__':
    unittest.main()
