import unittest
import strings

class TestStringMethods(unittest.TestCase):
    def test_Formatting(self):
        self.assertEqual(strings.Formatting("John", "Doe"), "His name is John Doe.")

    def test_NoSpace(self):
        self.assertEqual(strings.NoSpace("His name is John Doe."),"HisnameisJohnDoe.")

    def test_TextLenght(self):
        self.assertEqual(strings.TextLenght("His name is John Doe"), 20)

if __name__ == '__main__':
    unittest.main()
