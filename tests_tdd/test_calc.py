import unittest
import calc

class TestCalc(unittest.TestCase):

    # write a method (needs to start with test_) otheriwse it won't run

    def test_add(self):
        """
        Simple test for checking the add function.
        """
        result = calc.add(10, 15)
        self.assertEqual(result, 25)

if __name__ == "__main__":
    unittest.main()