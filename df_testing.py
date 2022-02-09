import unittest
import pandas as pd
from pandas.testing import assert_frame_equal


class DfTests(unittest.TestCase):
    """
    class for running unittests!
    """
    def setUp(self):
        """
        tests that the file can be opened
        """
        test_file_name = 'testdata.xlsx'
        try:
            data = pd.read_excel(test_file_name)
        except IOError:
            print('Unable to open file')
        self.fixture = data
        
    def test_dataFrame_constructedAsExpected(self):
        """ 
        Tests that the dataframe built is the one i actually wanted
        """
        foo = pd.DataFrame()
        assert_frame_equal(self.fixture, foo)


unittest.main()
