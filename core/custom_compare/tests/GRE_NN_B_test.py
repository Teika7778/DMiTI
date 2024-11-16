import unittest
from data_types import *
from core.custom_compare.GRE_NN_B import GRE_NN_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = GRE_NN_B()

    def test_something(self):
        self.assertEqual(self.module.execute([Natural([0]), Natural([1])]), [False])
        self.assertEqual(self.module.execute([Natural([0, 1, 1]), Natural([0, 0, 1])]), [True])
        self.assertEqual(self.module.execute([Natural([0, 0, 1]), Natural([0, 1, 1])]), [False])
        self.assertEqual(self.module.execute([Natural([0, 1]), Natural([0, 1])]), [False])


if __name__ == '__main__':
    unittest.main()