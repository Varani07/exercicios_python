import unittest

def copy_and_add_element(value, element):
    copy = value[:]
    copy.append(element)
    return copy

class TestInequality(unittest.TestCase):
    def test_inequaliti(self):
        self.assertNotEqual(1, 3)
        self.assertNotEqual([1, 2], [2, 1])

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)
        self.assertEqual(result, [1, 2, 3, 4], "The return value isnt valid.")
        self.assertNotEqual(
            values,
            [1, 2, 3, 4]
        )

if __name__ == "__main__":
    unittest.main()