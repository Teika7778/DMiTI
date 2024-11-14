import unittest
from core.custom_compare.GREQ_ZZ_B import GREQ_ZZ_B
from parsers.data_types_parser import DataTypeParser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = GREQ_ZZ_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_integer("+1"), self.parser.parse_integer("-1")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_integer("+3"), self.parser.parse_integer("-1")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_integer("+0"), self.parser.parse_integer("-0")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_integer("-1"), self.parser.parse_integer("-0")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_integer("+1"), self.parser.parse_integer("+2")]),
                         [False])

if __name__ == '__main__':
    unittest.main()