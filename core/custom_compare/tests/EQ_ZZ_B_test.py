import unittest
from parsers.data_types_parser import DataTypeParser
from core.custom_compare.EQ_ZZ_B import EQ_ZZ_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = EQ_ZZ_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_integer("-5"), self.parser.parse_integer("-5")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-0"), self.parser.parse_integer("+0")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-5"), self.parser.parse_integer("-4")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-5"), self.parser.parse_integer("+5")]),
                         [False])


if __name__ == '__main__':
    unittest.main()