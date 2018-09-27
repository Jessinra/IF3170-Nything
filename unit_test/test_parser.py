import unittest
from file_parser import FileParser

class TestFileParser(unittest.TestCase):
   
    def setUp(self):
        self.display_test_name()

    def display_test_name(self):
        print ("Checking {}".format(self.id()))
        
    def test_parse_data(self):

        filename = "unit_test/testfile.txt"
        parsed_data = FileParser.parse_data(filename)

        expected = [{'color': 'w', 'count': 2, 'type': 'knight'},
                    {'color': 'w', 'count': 2, 'type': 'bishop'},
                    {'color': 'w', 'count': 2, 'type': 'rook'},
                    {'color': 'w', 'count': 2, 'type': 'queen'},
                    {'color': 'b', 'count': 2, 'type': 'knight'},
                    {'color': 'b', 'count': 2, 'type': 'bishop'},
                    {'color': 'b', 'count': 2, 'type': 'rook'},
                    {'color': 'b', 'count': 2, 'type': 'queen'}]

        self.assertEqual(parsed_data, expected)


if __name__ == "__main__":
    unittest.main()