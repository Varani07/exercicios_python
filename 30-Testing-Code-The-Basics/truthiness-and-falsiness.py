import unittest

class TruthinessAndFalsinessTests(unittest.TestCase):
    def test_truthiness(self):
        self.assertEqual(3 < 5, True)
        self.assertTrue(3 < 5)
        self.assertTrue(1)
        self.assertTrue(["a"])

    def test_falsiness(self):
        self.assertFalse(0)
        self.assertFalse([])
        self.assertFalse("")
        self.assertFalse({})

if __name__ == "__main__":
    unittest.main()