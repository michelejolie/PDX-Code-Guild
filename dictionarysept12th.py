#!/usr/bin/python

# Dictionaries in Python

dict = {'Subject': 'Physics', 'Year': 2014, 'Marks': 88}

# to print complete dictionary
print("dict: ", dict)

# to print the values in the dictionary
print("dict['Subject']: ", dict['Subject'])
print("dict['Marks']: ", dict['Marks'])


# to print complete dictionary
print("dict: ", dict)

# update existing entry
dict['Year'] = 2013

# created a new key with value
dict['School'] = 'Milton High'

print("dict: ", dict)
print("dict['Year']: ", dict['Year'])
print("dict['School']: ", dict['School'])

# remove individual dictionary elements or clear the entire contents of a dictionary

# remove entry with key 'Subject'
del dict['Subject']
print("dict: ", dict)

# remove all entries in dict
dict.clear();
print("dict: ", dict)


dict = {'Subject': 'Physics', 'Year': 2014, 'Marks': 88}
aDict = {'School': 'Milton High'}

# to print complete dictionary
print("dict: ", dict)

# a shallow copy of dictionary dict
dict.copy()

# a list of dict's (key, value) tuple pairs
dict.items()
print(dict.items())

# list of dictionary dict's keys
dict.keys()
print(dict.keys())

# to add dictionary dict2's key-values pairs to dict
dict.update(aDict)
print("dict: ", dict)

# list of dictionary dict's values
dict.values()

print(dict.values())

# If we attempt to access a data item with a key, which is not part of the dictionary,
# we get an error
print("dict['Class']: ", dict['Class'])


# delete entire dictionary
#del dict ;
#print("dict: ", dict)

# after del dict dictionary does not exist any more
print("dict['Year']: ", dict['Year'])

