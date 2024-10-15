import unittest

def multiply(a, b):
    return a * b
    # total = 0
    # for _ in range(a):
    #     total += b
    # return total

class MultiplyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)

if __name__ == "__main__":
    unittest.main()