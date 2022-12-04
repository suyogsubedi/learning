import unittest
from mathss import multiply

class MathsHariBahadurMultiplicationTest(unittest.TestCase):
    def test_multiplication(self):
        """
            Tests if it can multiply all of the given arguments correctly
        """
        result = 5*2*5
        self.assertEqual(multiply(5,2,5),result)

if __name__=='main':
    unittest.main()