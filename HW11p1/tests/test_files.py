import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files


class TestFiles(unittest.TestCase):
    # define how many points it is
    @weight(20)
    # check for if a file with specified filename exists
    def test_submitted_files(self):
        """Check submitted files"""
        missing_files = check_submitted_files(['HW11p1.py'])
        for path in missing_files:
            print('Missing {0}'.format(path))
        self.assertEqual(len(missing_files), 0, 'Missing required files! Ensure that you have submitted the file with the correct name!')
        print('All required files submitted!')
