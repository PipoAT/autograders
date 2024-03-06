from contextlib import redirect_stdout
import io
import sys
import unittest
from gradescope_utils.autograder_utils.decorators import weight


class TestCases(unittest.TestCase):
    @weight(10)
    def test_case_one(self):
        """Test Case 1: Vo = 23, K = 0.123, m = 10"""
        input_values = ["23", "0.123", "10"]  # Simulated user input
        input_str = '\n'.join(input_values) + '\n'
        input_file = io.StringIO(input_str)

        output_file = io.StringIO()

        original_stdin = sys.stdin
        sys.stdin = input_file

        with redirect_stdout(output_file):
            # Here, the student's code should be run
            exec(open("HW11p1.py").read())

        sys.stdin = original_stdin

        actual_output = output_file.getvalue().strip().split('\n')[-1].split()[-1]  # Get the last word of the last line of output
        expected_output = "904.70"  # Adjust based on the expected format of the output
        self.assertEqual(expected_output, actual_output, "Output does not match expected output.")

    @weight(10)
    def test_case_two(self):
        """Test Case 2: Vo = 12, K = 0.123, m = 4"""
        input_values = ["12", "0.123", "4"]  # Simulated user input
        input_str = '\n'.join(input_values) + '\n'
        input_file = io.StringIO(input_str)

        output_file = io.StringIO()

        original_stdin = sys.stdin
        sys.stdin = input_file

        with redirect_stdout(output_file):
            # Here, the student's code should be run
            exec(open("HW11p1.py").read())

        sys.stdin = original_stdin

        actual_output = output_file.getvalue().strip().split('\n')[-1].split()[-1]  # Get the last word of the last line of output
        expected_output = "465.55"  # Adjust based on the expected format of the output
        self.assertEqual(expected_output, actual_output, "Output does not match expected output.")


    @weight(10)
    def test_case_three(self):
        """Test Case 3: Vo = 5, K = 0.5, m = 5"""
        input_values = ["5", "0.5", "5"]  # Simulated user input
        input_str = '\n'.join(input_values) + '\n'
        input_file = io.StringIO(input_str)

        output_file = io.StringIO()

        original_stdin = sys.stdin
        sys.stdin = input_file

        with redirect_stdout(output_file):
            # Here, the student's code should be run
            exec(open("HW11p1.py").read())

        sys.stdin = original_stdin

        actual_output = output_file.getvalue().strip().split('\n')[-1].split()[-1]  # Get the last word of the last line of output
        expected_output = "129.22"  # Adjust based on the expected format of the output
        self.assertEqual(expected_output, actual_output, "Output does not match expected output.")


    @weight(10)
    def test_case_four(self):
        """Test Case 4: Vo = 1234, K = 0.1, m = 5"""
        input_values = ["1234", "0.1", "5"]  # Simulated user input
        input_str = '\n'.join(input_values) + '\n'
        input_file = io.StringIO(input_str)

        output_file = io.StringIO()

        original_stdin = sys.stdin
        sys.stdin = input_file

        with redirect_stdout(output_file):
            # Here, the student's code should be run
            exec(open("HW11p1.py").read())

        sys.stdin = original_stdin

        actual_output = output_file.getvalue().strip().split('\n')[-1].split()[-1]  # Get the last word of the last line of output
        expected_output = "48619.55"  # Adjust based on the expected format of the output
        self.assertEqual(expected_output, actual_output, "Output does not match expected output.")