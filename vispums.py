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

# Create mappings for easy TAXP transformation
mappings = np.append(np.array([0, np.nan, 1]), np.arange(50, 1050, 50))
mappings = np.append(mappings, np.arange(1100, 5100, 100))
mappings = np.append(mappings, np.array([5500, 6000, 7000, 8000, 9000, 10000]))


# Helper function for changing values
def map_taxp(x):
    try:
        return mappings[int(x)]
    except ValueError:
        return x

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
    
    
    # figure for containing all the subplots
    figure = plt.figure(figsize=(12, 8))
    # Add the ie chart subplot
    
    ax1 = figure.add_subplot(2, 2, 1)
    ax1.pie(sizes, shadow=False, startangle=242)
    ax1.axis('equal')
    ax1.pie(sizes, shadow=False, startangle=242)
    ax1.set_ylabel('HHL')
    ax1.legend(labels, loc="upper left")
    ax1.title.set_text("Household Languages")
        
    ax2 = figure.add_subplot(2, 2, 2)
    ax2.hist(pums_data["HINCP"].dropna(),bins=np.logspace(np.log10(1),np.log10(10000000), 50), facecolor='green', alpha=0.5)
    ax2.title.set_text("Distribution of Houshold Income")
    ax2.set_xscale("log")
   

    
     # Plot the household vehicle data
    # Get the household vehicles data
    vehicles = pd.DataFrame(pums_data[['VEH', 'WGTP']])
    # Remove NaN values
    vehicles.dropna(axis=0, inplace=True)
    # Group the vehicles by number and sum to account for household size
    groups = vehicles.groupby(['VEH']).sum() / 1000
    # Create plotting information
    x_points = np.array(groups['WGTP'].index.tolist())
    y_values = np.array(groups['WGTP'])
    # Add new Axes object to bottom left and set attributes
    ax3 = figure.add_subplot(2, 2, 3)
    ax3.bar(x_points, y_values, color='r')
    ax3.set_title("Vehicles Available in Households")
    ax3.set_xlabel("# of Vehicles")
    ax3.set_ylabel("Thousands of Households")
    ax3.yaxis.get_major_ticks()[0].set_visible(False)

    # Plot the scatter plot
    # Get the tax data
    data = pd.DataFrame(pums_data[['TAXP', 'VALP', 'WGTP', 'MRGP']]).dropna()
    # Map tax code to lower bound tax category
    data['TAXP'] = data['TAXP'].apply(map_taxp)
    # Get data for scatter plot and create
    x_vals = np.array(data['TAXP'])
    y_vals = np.array(data['VALP'])
    widths = np.array(data['WGTP'])
    colors = np.array(data['MRGP']).astype(float)
    ax4 = figure.add_subplot(2, 2, 4)
    sc = ax4.scatter(y_vals, x_vals, s=widths, c=colors, cmap=plt.cm.bwr, marker='o')
    ax4.set_xlim([0, 1200000])
    ax4.set_ylim([0, 10500])
    ax4.margins(x=0)
    ax4.set_title("Property Taxes vs. Property Values")
    ax4.set_xlabel("Property Value ($)")
    ax4.set_ylabel("Taxes ($)")
    ax5 = plt.colorbar(sc)
    ax5.set_label("First Mortgage Payment (Monthly $)")
    ax5.set_ticks([1250, 2500, 3750, 5000])

    # Set layout to tight, and save as png
    plt.tight_layout()
    plt.savefig("pums.png", type='png')
    plt.show()
     
if __name__ == "__main__":
    main(sys.argv)