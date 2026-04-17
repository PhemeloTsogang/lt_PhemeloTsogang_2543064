#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''

    # Reads the header line and splits it into column headings
    headings = f.readline().strip().split(",")
    
    # Initializes the num_col and mark_col variables
    num_col = None
    mark_col = None
    
    # Loops through the headings and finds the student number and mark columns
    # No exception error handling is included because it is assumed 
    # that "Student Number" and "Mark" will always appear in the header
    i = 0
    for head in headings:
        if head == "Student Number":
         num_col = i # stores the index of the "Student Number" column
        elif head == "Mark":
         mark_col = i #stores the index of the "Mark" column
        # Increments the iterator to loop through the all headings
        i += 1

    return num_col, mark_col

def findTop(f, num_col, mark_col):
    ''' finds the top student in the class '''

    # Initializes the best mark and the corresponding student index (student number)
    best = -1
    best_idx = None

    # Loops through each line (one student's information)
    for line in f:
        data = line.strip().split(",") # Splits each row into a values

        mark = int(data[mark_col]) # Allocates the mark of the student using the column index

        # Updates the best mark if that specific student's mark is higher than the current best and stores the student's number
        if mark > best:
            best = mark
            best_idx = data[num_col]

    return best_idx, best 


if __name__ == "__main__": # Ensures that this code part runs when code is directly ran and not when imported during testing
    f = open(sys.argv[1]) 
    num_col, mark_col = getCols(f) # Finds the required colums within the file
    best_idx, best = findTop(f,num_col,mark_col) # Finds the student with the highest mark
    print(f"The top student was student {best_idx} with {best}") # Outputs the student number with their mark


