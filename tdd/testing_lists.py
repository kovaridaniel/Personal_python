import unittest
import lists

class TestLists(unittest.TestCase):
    
    def test_ListHaveit(self):
        self.assertIn(2, (1, 2, 3, 4, 5))

    def test_ListCorrect(self):
        numbers = [2, 3, 5, 11, 123]
        for single  in lists.LessThan_Ten(numbers):
            self.assertIn(single, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
