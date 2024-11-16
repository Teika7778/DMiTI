import unittest
from core.custom_logic.EQ_BB_B import EQ_BB_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = EQ_BB_B()

    def test_something(self):
        self.assertEqual(self.module.execute([True, False]), [False])
        self.assertEqual(self.module.execute([True, True]), [True])
        self.assertEqual(self.module.execute([False, False]), [True])
        self.assertEqual(self.module.execute([False, True]), [False])


if __name__ == '__main__':
    unittest.main()