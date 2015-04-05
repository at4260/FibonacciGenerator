import unittest
import controller


class CheckResult(unittest.TestCase):

    def setUp(self):
        controller.app.config['TESTING'] = True
        self.app = controller.app.test_client()

    def test_input_zero(self):
        result = self.app.get("127.0.0.1:8000/fib/0")
        self.assertEqual(0, result.data)


if __name__ == "__main__":
    unittest.main()
