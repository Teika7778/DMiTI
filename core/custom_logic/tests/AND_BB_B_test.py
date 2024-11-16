import unittest
from core.custom_logic.AND_BB_B import AND_BB_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = AND_BB_B()

    def test_something(self):
        self.assertEqual(self.module.execute([True, False]), [False])
        self.assertEqual(self.module.execute([True, True]), [True])
        self.assertEqual(self.module.execute([False, False]), [False])
        self.assertEqual(self.module.execute([False, True]), [False])


if __name__ == '__main__':
    unittest.main()
