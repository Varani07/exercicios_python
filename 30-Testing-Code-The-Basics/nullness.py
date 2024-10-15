import unittest

def explicit_return_sum(a, b):
    return a + b

def implicit_return_sum(a, b):
    print(a + b)

class TestNone(unittest.TestCase):
    def test_sum_func(self):
        self.assertIsNone(implicit_return_sum(3, 4))
        self.assertIsNotNone(explicit_return_sum(3, 7))

if __name__ == "__main__":
    unittest.main()