import unittest


class Testsomething(unittest.TestCase):
    def setUp(self):
        self.display_test_name()

    def display_test_name(self):
        print ("Checking {}".format(self.id()))
        
    def test_what(self):

        

        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()