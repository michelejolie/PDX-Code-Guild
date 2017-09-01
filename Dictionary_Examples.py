my_dict = {'key1': {'some': 'thing'}, 'key2': 'value2'}

print(my_dict)

# Add Item
my_dict['key3'] = 'value3'

# print(my_dict)

# Change Value
set_thing = my_dict.setdefault('key3', ['some', 'list', 'of', 'things'])

# print(my_dict)
# print(set_thing)

my_dict.update(key1='value10', key11='value11')

print(my_dict.values())
# Delete
del my_dict['key3']

print(my_dict)

for k, v in my_dict.items():
    print('Key is: {}.'.format(k))
    print('value is: {}.'.format(v))
    print('<-------------->')



students = {
    'Watters': {'name': 'Kasey Watters', 'phone': 3333333333},
    'Magnuson': {'name': 'Tom Magnuson', 'phone': 4444444444},
    'Yeaney': {'name': 'Johny Yeaney', 'phone': 5555555555},
}

query = input("What is the last name of the person you are looking for?: ")

print(students[query]['name'])
print(students[query]['phone'])
