import unittest
from core.custom_compare.GREQ_QQ_B import GREQ_QQ_B
from parsers.data_types_parser import DataTypeParser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = GREQ_QQ_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_rational("+1/2"), self.parser.parse_rational("-1/2")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_rational("+0/2"), self.parser.parse_rational("-0/3")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_rational("+1/3"), self.parser.parse_rational("+1/4")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_rational("-1/3"), self.parser.parse_rational("-1/4")]),
                         [False])

if __name__ == '__main__':
    unittest.main()