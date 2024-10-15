import unittest

class ObjectTypeTests(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(1, int)
        self.assertIsInstance({"a":1}, dict)
    def test_not_is_instance(self):
        self.assertNotIsInstance(5, dict)

if __name__ == "__main__":
    unittest.main()