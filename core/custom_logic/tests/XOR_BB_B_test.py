import unittest
from core.custom_logic.XOR_BB_B import XOR_BB_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = XOR_BB_B()

    def test_something(self):
        self.assertEqual(self.module.execute([True, False]), [True])
        self.assertEqual(self.module.execute([True, True]), [False])
        self.assertEqual(self.module.execute([False, False]), [False])
        self.assertEqual(self.module.execute([False, True]), [True])


if __name__ == '__main__':
    unittest.main()