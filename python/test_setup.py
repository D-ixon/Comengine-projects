import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    
    def test_string_concat(self):
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")

if __name__ == "__main__":
    unittest.main()