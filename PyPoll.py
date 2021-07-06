# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


# direct path to opening files _____________

# Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
# We opted to use _with_ statement instead
# To do: Perform Analysis

#with open(file_to_load) as election_data:
 #   print(election_data)

# Close the file.
# We opted to use _with_ statement instead 
# election_data.close()

# indirect path to opening files ______________
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    

#__________________________________________

# Write to files in python

#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# This has created the .txt file "election_analysis.txt"
# Next we will add "Hello World" to the first line of this txt file.
# __________________________________________

#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() statement open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file
#outfile.write("Hello World")

# Close the file
#outfile.close()

# Using the 'with' statement can make code more clean and concise
# Instead of using the open() and close() functions

#________________________________________________

#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement to open the file as a text file
#with open(file_to_save, "w") as txt_file:
    #write some data 
 #   txt_file.write("Counties in the Election")
  #  txt_file.write("\n__________________________")
   # txt_file.write("\nArapahoe\nDenver\nJefferson")



# To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #for row in file_reader:
        #print(row)

    headers = next(file_reader)
    print(headers)  