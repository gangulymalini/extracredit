import unittest
import q1


class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(q1.sentencereverse("My name is V Tadimeti."), "Tadimeti V is name My.")
    def test_2(self):
        self.assertEqual(q1.sentencereverse("Happy Birthday To You."), "You To Birthday Happy.")
    def test_3(self):
        self.assertEqual(q1.sentencereverse("My name is Sally."), "Sally is name My.")


if __name__ == "__main__":
    unittest.main()