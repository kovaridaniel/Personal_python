import unittest
import mathing

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mathing.Add(2, 3), 5)
    
    def test_multiply(self):
        self.assertEqual(mathing.Multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()

