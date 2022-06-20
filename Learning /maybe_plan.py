"""
  Questions to ask first: 
  1. would the data be within files or in Database? 
  if Files: 
  # Importing panda into Python
  import pandas as pd 

  # Command for creating the data required 
  cols = ["UniqueCode", "Rating", "NumVotes" ] 
  df = pd.read_scv( {# FILE PATH #} )

  # Ordering through data using NumVotes parameter 
  df.sort_values(by=[ "NumVotes" ], ascending=False, inplace=True)
  df.query("'NumVotes' >= 100", inplace=True)
"""
import collections
import operator
from itertools import chain
from collections import defaultdict

# dict of key:MovieID and value: Number of Votes
library = { 
  "movie A" : 5,
  "movie D" : 10,
  "movie C" : 3,
  "movie B" : 2,
}

# dict of 
rating_library = {
  "movie A" : 3.9,
  "movie B" : 4.1,
  "movie C" : 2.9,
  "movie D" : 4.6,
}

#Getting Number of Votes 
for k in library:
  print(f'This is the Value {library[k]}')

# Getting total Amount of Movies 
# len() gives the length of the dict 
print(len(library.keys()))

# Getting the Avarage of number of votes from all Movies 
# sum() gives the total of the dict, this example spesifies values
print(sum(library.values())/len(library.keys()))

# New dict to be created with a key of Movies and a calculated (numVote/AvgNumVote)
# New numbers to be compared with ratings DataFrame
# Final dict will be created using movieID and calculated rating formula. 
# Arrange the final dict in order 

new_library = { }

for k in sorted(library):
  print( f"{k}" )

# Filter dict and create new one with required constraints 
for k, v in library.items():
  if v > 2:
    new_library[k] = v

# Sort by values using itemgetter operator, Reverse True since we require top 15
sorted_values = sorted(library.items(), key=operator.itemgetter(1), reverse=True)
sorted_dict = dict(sorted_values)

print(sorted_dict)

# Taking the first 2 values from the sorted values, must be converted back to dict to be used further. 
# [:2] dictates the amount of data to be taken. (2 for example, 15 required in actual data)
print(list(sorted_values)[:2])

# Completed Task A - Final dict will contain MovieID with overall ranking. 

# Using DataSet in Task A use the MovieID to retrieve Movie Name

name_library = { 
  "movie A" : "LotR",
  "movie D" : "Avengers",
  "movie C" : "Batman",
  "movie B" : "Superman",
}

mock_data = {
  "movie A" : 3.9, 
  "movie B" : 1.6,
  "movie C" : 1.7,
  "movie D" : 9.2
}

# 2 dicts linking to each other linked by movieID 
# Make sure Data is Arranged in order of movieID
# Use OrderedDict to rememebr order of data

comp_dict = defaultdict(list)

ordered_names = collections.OrderedDict(sorted(name_library.items()))
ordered_mock = collections.OrderedDict(sorted(mock_data.items()))

for k, v in chain(ordered_names.items(), ordered_mock.items()):
    comp_dict[k].append(v)

for k, v in comp_dict.items():
    print(k, v)

print(comp_dict)
