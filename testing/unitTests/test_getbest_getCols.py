import unittest
import code

class TestGetCols(unittest.TestCase):

    # Tests if the function outputs the correct columns with the standard column order in the sample data file
    def test_normal_columnOrder(self):
        f = open("testing/testData/test_data_getCols_normal.csv") # Acquires the header from the test data file
        num_col, mark_col = code.getCols(f) # assigns the function output to variables for testing
        f.close() # Closes the file

        # Expected outputs of the function
        self.assertEqual(num_col, 1) # in this case, num_col should be 1 for the test to pass
        self.assertEqual(mark_col, 2)

    # Tests if the function still outputs correct columns if the column order in the data file is different
    def test_swapped_columnOrder(self):
        f = open("testing/testData/test_data_getCols_swapped.csv")
        num_col, mark_col = code.getCols(f)
        f.close()

        self.assertEqual(num_col, 2)
        self.assertEqual(mark_col, 0)


if __name__ == "__main__":
    # Runs all the test in the file when executed
    unittest.main()