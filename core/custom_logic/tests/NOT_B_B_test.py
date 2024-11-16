import unittest
from core.custom_logic.NOT_B_B import NOT_B_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = NOT_B_B()

    def test_something(self):
        self.assertEqual(self.module.execute([True]), [False])
        self.assertEqual(self.module.execute([False]), [True])


if __name__ == '__main__':
    unittest.main()