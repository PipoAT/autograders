import unittest
import subprocess
import math
from HW11p1 import hw_eleven_one
from gradescope_utils.autograder_utils.decorators import weight, number

class TestCases(unittest.TestCase):

    @weight(15)
    @number("1.1")
    def test_case_one(self):
        """Vo = 23, K = 0.123, m = 10"""
        result = hw_eleven_one(23, 0.123, 10)
        expected_output = 904.698
        assert math.isclose(result, expected_output, rel_tol=1e-3), "Output does not match expected output."


    @weight(15)
    @number("1.2")
    def test_case_two(self):
        """Vo = 10, K = 0.123, m = 23"""
        result = hw_eleven_one(10, 0.123, 23)
        expected_output = 392.497
        assert math.isclose(result, expected_output, rel_tol=1e-3), "Output does not match expected output."

    
    @weight(15)
    @number("1.3")
    def test_case_three(self):
        """Vo = 25, K = 0.5, m = 10"""
        result = hw_eleven_one(25, 0.5, 10)
        expected_output = 979.372
        assert math.isclose(result, expected_output, rel_tol=1e-3), "Output does not match expected output."
    

    @weight(15)
    @number("1.4")
    def test_case_four(self):
        """Vo = 100, K = 1, m = 100"""
        result = hw_eleven_one(100, 1, 100)
        expected_output = 3939.72
        assert math.isclose(result, expected_output, rel_tol=1e-3), "Output does not match expected output."