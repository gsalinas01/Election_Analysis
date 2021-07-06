# x = 0
#while x <= 5:
 #   print(x)
  #  x = x + 1

   # for item in [items]:


# prints numbers as list
# numbers = [0, 1, 2, 3, 4]
#print(numbers)

# prints numbers vertically 1 on each line
#for num in range(5):
 #   print(num)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.values():
 #   print(county)

#    print("El Paso is not the list of counties.")

#for county in counties_dict:
 #   print(county)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):

      print(voting_data[county]['county'])

for registered_voters in range(len(voting_data)):

      print(voting_data[registered_voters]['registered_voters'])

print( )
#retrieve number of registered voters from each dictionary in 
#voting_data

for i in voting_data:
    print(i['registered_voters'])


#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#using f strings to get same result as above

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes. "
  #  f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100}% of the total votes.")

#print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
