import unittest
from maths_hari_bahadur import addition

class MathsHariBahadurAdditionTest(unittest.TestCase):
    def test_addition(self):
        """
            Tests if it can sum all of the given arguments correctly
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(addition(1,2,3), result)


if __name__=='main':
    unittest.main()
# python -m unittest tests.test_addition