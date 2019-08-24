# Name: Eugene Zhuravel, Ian Wodder
# Date: 7817/2019
# Course Name:CPSC-51100-003
# Semester: Summer 2019
# Assignment: Programming Assignment 6

import sys
import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Entry point of application
def main(argv):
    print("CPSC-51100, Summer 2019")
    print("NAME: Eugene Zhuravel, Ian Wodder")
    print("PROGRAMMING ASSIGNMENT #6")
    print("")
    
    # Read file save to dataframe
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    location = location + os.sep + "ss13hil.csv"
    pums_data = pd.read_csv(location)
    
    # Print Pie chart
    gp = pums_data.groupby(['HHL'])
    totalSpokenlanguages = len(pums_data["HHL"].dropna())
    
    # Get English only 
    english_only = ((len(gp.get_group(1))/totalSpokenlanguages) * 100)

    # Get Spanish
    spanish = ((len(gp.get_group(2))/totalSpokenlanguages) * 100)
    
    # Get Other Indo-European languages
    european = ((len(gp.get_group(3))/totalSpokenlanguages) * 100)
  
    # Get Asian
    asian = ((len(gp.get_group(4))/totalSpokenlanguages) * 100)
    
    # Get Other
    other = ((len(gp.get_group(5))/totalSpokenlanguages) * 100)
    
    labels = "English only", "Spanish", "Other Indo-European languages", "Asian and Pacific Island languages", "other"
    sizes = [english_only, spanish, european, asian,other]
    
    
    fig1, (ax1, ax2) = plt.subplots(ncols=2)
    ax1.pie(sizes, shadow=False, startangle=242)
    ax1.set_ylabel('HHL')
    ax1.legend(labels, loc="upper left")
    ax1.title.set_text("Household Languages")
        
    ax2.hist(pums_data["HINCP"].dropna(),bins=np.logspace(np.log10(1),np.log10(10000000), 50), facecolor='green', alpha=0.5)
    ax2.title.set_text("Distribution of Houshold Income")
    ax2.set_xscale("log")
    plt.show()

    
if __name__ == "__main__":
    main(sys.argv)