import unittest
from core.custom_compare.GREQ_NN_B import GREQ_NN_B
from parsers.data_types_parser import DataTypeParser


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.module = GREQ_NN_B()
        self.parser = DataTypeParser()

    def test_something(self):
        self.assertEqual(self.module.execute([self.parser.parse_natural("1"), self.parser.parse_natural("1")]),
                         [True])
        self.assertEqual(self.module.execute([self.parser.parse_natural("1"), self.parser.parse_natural("2")]),
                         [False])
        self.assertEqual(self.module.execute([self.parser.parse_natural("2"), self.parser.parse_natural("1")]),
                         [True])


if __name__ == '__main__':
    unittest.main()