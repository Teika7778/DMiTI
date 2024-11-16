import unittest
from core.custom_compare.GRE_ZZ_B import GRE_ZZ_B
from parsers.data_types_parser import DataTypeParser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = GRE_ZZ_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_integer("-1"), self.parser.parse_integer("-1")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-10"), self.parser.parse_integer("+10")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_integer("+10"), self.parser.parse_integer("-10")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-25"), self.parser.parse_integer("-1")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-0"), self.parser.parse_integer("+0")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_integer("+0"), self.parser.parse_integer("-1")]),
                         [True])


if __name__ == '__main__':
    unittest.main()