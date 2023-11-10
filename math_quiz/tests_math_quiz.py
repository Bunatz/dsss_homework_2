import unittest
from math_quiz import create_rand_int, create_rand_operator, cal_result_numbers


class TestMathGame(unittest.TestCase):

    def test_create_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = create_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_create_rand_operator(self):
        operator_plus   = '+'
        operator_minus  = '-'
        operator_mult   = '*'
        list_operator   = [operator_minus,operator_mult,operator_plus]
        for _ in range(1000):  # Test a large number of trys
            rand_operator = create_rand_operator()
            self.assertTrue(rand_operator in list_operator)

    def test_cal_result_numbers(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 9, '-', '4 - 9', -5),
                (5, 3, '*', '5 * 3', 15),
                (2, 1, '-', '2 - 1', -1),
                # Test if all results with different operators are correct
            ]

            for number1, number2, operator, expected_problem, expected_answer in test_cases:
                calculation, result = cal_result_numbers(number1, number2, operator)
                self.assertTrue(result == expected_answer, f"Expected Result {expected_answer},"
                                                           f" shown Result {result}")
                # Test if the expected result the shown Result
                self.assertTrue(calculation == expected_problem, f"Expected Calculation {expected_answer}, "
                                                                 f"shown Calculation {result}")
                # Test if the expected result the shown Result

if __name__ == "__main__":
    unittest.main()
