import unittest
import utils


class FibonacciTestCase(unittest.TestCase):
    def test_user_results_zero(self):
        self.assertEqual(utils.get_fibonacci(
            0), 0)

    def test_user_results_one(self):
        self.assertEqual(utils.get_fibonacci(
            1), 1)

    def test_user_results_two(self):
        self.assertEqual(utils.get_fibonacci(
            2), 1)

    def test_user_results_five(self):
        self.assertEqual(utils.get_fibonacci(
            5), 5)

    def test_user_results_seven(self):
        self.assertEqual(utils.get_fibonacci(
            7), 13)

    def test_user_results_ten(self):
        self.assertEqual(utils.get_fibonacci(
            10), 55)

    def test_user_results_neg(self):
        self.assertEqual(utils.get_fibonacci(
            -1), "Not valid")

if __name__ == "__main__":
    unittest.main()
