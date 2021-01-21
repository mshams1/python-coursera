################################################
## The Python Programming Language: Functions ##
################################################

def add_numbers(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

##########################################################
## The Python Programming Language: Types and Sequences ##
##########################################################

# types: str, int, float, function, tuple, list

type('This is a string')

x = (1, 'a', 2, 'b') # Tuples are an immutable data structure (cannot be altered)

x = [1, 'a', 2, 'b'] # Lists are a mutable data structure

# use append to append an object to a list
x.append(3.3) 
x1 = [1,2] + [3,4]
x2 = [1]*3

x = 'This is a string'
print(x[0])   #first character
print(x[0:1]) #first character, but we have explicitly set the end character
print(x[0:2]) #first two characters

# `split` returns a list of all the words in a string, or a list split on a specific character
firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)

q = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
print(q['Christopher Brooks']) # Retrieve a value by using the indexing operator

######################################################
## The Python Programming Language: More on Strings ##
######################################################

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

###################################
## Reading and Writing CSV files ##
###################################

import csv

%precision 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # The first three dictionaries in our list.


