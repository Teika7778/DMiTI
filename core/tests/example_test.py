import unittest
from core import example as ex
from data_types import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n1 = Natural([1, 2])
        n2 = Natural([2, 1])
        m = ex.Module()
        n3 = m.execute([n1, n2])[0]
        n2.numbers[0] = 3
        self.assertNotEqual(n2.numbers, n3.numbers)  # add assertion here


if __name__ == '__main__':
    unittest.main()
