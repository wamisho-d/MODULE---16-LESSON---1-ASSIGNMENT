import unittest
from app import sum_function  # Adjust the import based on your app's structure

class TestSumFunction(unittest.TestCase):
    
    def test_negative_sum(self):
        # Test for negative sum
        result = sum_function(-5, -7)
        self.assertEqual(result, -12, "Should be -12")

if __name__ == '__main__':
    unittest.main()
