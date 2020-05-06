import unittest
import texts

class TestTexts(unittest.TestCase):
    
    def test_Sentences(self):
        self.assertEqual(texts.Sentences("Good morning everyone!"), ["Good morning everyone!"])
        self.assertEqual(texts.Sentences("Good morning everyone! I hope you have a nice day!"), ["Good morning everyone!", "I hope you have a nice day!"])
        self.assertEqual(texts.Sentences("Good morning everyone! We have such a nice day. Am I right? Of course I am."), ["Good morning everyone!", "We have such a nice day.", "Am I right?", "Of course I am."])

if __name__ == '__main__':
    unittest.main()

