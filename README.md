Phemelo Tsogang

Solution Description:
This program reads a CSV file and find the student with the highest mark.

Structure: 
- code/: contains the main code solution
- sampleData/: contains the sample data the main code uses
- testing/: contains 2 folders: testData/ and unitTests/
    - testData/: contains the test data for both test files
    - unitTests/ contains unit test files for the functions getCols() and findTop()

How to run main program:

python code/getbest.py sampleData/bestdat0.csv



How to run getCols function test:

python -m unittest testing.unitTests.test_getbest_getCols



How to run findTop function test: 

python -m unittest testing.unitTests.test_getbest_findTop