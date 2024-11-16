import unittest
from core.custom_compare.GRE_QQ_B import GRE_QQ_B
from parsers.data_types_parser import DataTypeParser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = GRE_QQ_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_rational("-1/2"), self.parser.parse_rational("-1/3")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_rational("-1/2"), self.parser.parse_rational("-2/4")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_rational("+1/9"), self.parser.parse_rational("+2/7")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_rational("+0/7"), self.parser.parse_rational("-0/9")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_rational("-0/9"), self.parser.parse_rational("+0/7")]),
                         [False])
        self.assertEqual(
            self.module.execute([self.parser.parse_rational("+100/7"), self.parser.parse_rational("+99/7")]),
            [True])


if __name__ == '__main__':
    unittest.main()
