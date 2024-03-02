import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files


class TestComments(unittest.TestCase):
    # Define how many points it is
    @weight(20)
    # Check if a file with specified filename exists
    def test_file_comments(self):
        """Check if comments exist"""
        # Check if files contain any comments
        with open('HW11p1.py', 'r') as file:
            lines = file.readlines()
            comment_exists = any(line.strip().startswith('#') for line in lines)
            self.assertTrue(comment_exists, f"File does not contain any comments.")

        print('All required files submitted and contain comments!')


