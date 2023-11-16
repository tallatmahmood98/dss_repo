import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the valid operators
        valid_operators = set(['+', '-', '*'])
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, valid_operators)

    def test_perform_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (-5, 2, '+', '-5 + 2', -3),  # Test with negative numbers
            (0, 10, '*', '0 * 10', 0),  # Test with zero
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            expression, result = perform_operation(num1, num2, operator)
            expected_expression = f"{num1} {operator} {num2}"
            # Check if the generated expression and result match the expected values
            self.assertEqual(expression, expected_expression)
            self.assertEqual(result, expected_answer)

if __name__ == "__main__":
    unittest.main()
