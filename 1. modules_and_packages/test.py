import unittest
from maths_hari_bahadur import addition,multiply

class MathsHariBahadurTest(unittest.TestCase):
    def test_addition(self):
        """
            Tests if it can sum all of the given arguments correctly
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(addition(1,2,3), result)
    
    def test_multiplication(self):
        """
            Tests if it can multiply all of the given arguments correctly
        """
        result = 5*2*5
        self.assertEqual(multiply(5,2,5),result)

if __name__=='main':
    unittest.main()