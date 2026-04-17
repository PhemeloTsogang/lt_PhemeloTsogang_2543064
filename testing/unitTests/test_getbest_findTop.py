import unittest
import code
# All these tests assume that there is a valid (non-negative) float value in each student mark column

class TestFindTop(unittest.TestCase):

    # Tests is the function outputs the correct student number and mark with a standard data file
    def test_normal_case(self):
        f = open("testing/testData/test_data_findTop_normal.csv") #Opens the data file and stores the header in a variable
        num_col, mark_col = code.getCols(f) # Acquires the student number and corresponding mark columns
        best_idx, best = code.findTop(f, num_col, mark_col) #Acquires the highest mark in the mark column and the coresponding student number
        f.close()

        self.assertEqual(best_idx, "200001")
        self.assertEqual(best, 90)

    # Tests if the function works correctly if the first student has the highest mark
    def test_top_student_first(self):
        f = open("testing/testData/test_data_findTop_first.csv")
        num_col, mark_col = code.getCols(f)
        best_idx, best = code.findTop(f, num_col, mark_col)
        f.close()

        self.assertEqual(best_idx, "200000")
        self.assertEqual(best, 82)

    # Tests is the function still works correctly if there is only one student in the data set
    def test_single_student(self):
        f = open("testing/testData/test_data_findTop_single.csv")
        num_col, mark_col = code.getCols(f)
        best_idx, best = code.findTop(f, num_col, mark_col)
        f.close()

        self.assertEqual(best_idx, "200000")
        self.assertEqual(best, 72)


if __name__ == "___main___":
    # Runs all the test in the file when executed
    unittest.main()