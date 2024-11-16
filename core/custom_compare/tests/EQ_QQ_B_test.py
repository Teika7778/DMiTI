import unittest
from parsers.data_types_parser import DataTypeParser
from core.custom_compare.EQ_QQ_B import EQ_QQ_B


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = EQ_QQ_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_rational("-2/4"), self.parser.parse_rational("-1/2")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_rational("+0/4"), self.parser.parse_rational("-0/5")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_rational("-5/3"), self.parser.parse_rational("+5/3")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_rational("+5/3"), self.parser.parse_rational("+5/4")]),
                         [False])


if __name__ == '__main__':
    unittest.main()