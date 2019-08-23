# Name: Eugene Zhuravel, Ian Wodder
# Date: 7817/2019
# Course Name:CPSC-51100-003
# Semester: Summer 2019
# Assignment: Programming Assignment 6

import sys
import os
import pandas as pd 
import re

# Entry point of application
def main(argv):
    print("CPSC-51100, Summer 2019")
    print("NAME: Eugene Zhuravel, Ian Wodder")
    print("PROGRAMMING ASSIGNMENT #6")
    print("")
    
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    location = location + os.sep + "ss13hil.csv"
    pums_data = pd.read_csv(location)
    
if __name__ == "__main__":
    main(sys.argv)