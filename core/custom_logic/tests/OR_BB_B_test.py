import unittest
from core.custom_logic.OR_BB_B import OR_BB_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = OR_BB_B()

    def test_something(self):
        self.assertEqual(self.module.execute([True, False]), [True])
        self.assertEqual(self.module.execute([True, True]), [True])
        self.assertEqual(self.module.execute([False, False]), [False])
        self.assertEqual(self.module.execute([False, True]), [True])


if __name__ == '__main__':
    unittest.main()
