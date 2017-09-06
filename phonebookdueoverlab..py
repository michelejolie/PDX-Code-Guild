brothers = {
    'Watters': {'name': 'Kasey Watters', 'phone': 3333333333},
    'Magnuson': {'name': 'Tom Magnuson', 'phone': 4444444444},
    'Yeaney': {'name': 'Johny Yeaney', 'phone': 5555555555},
}
brothers ={'lower'(): 'upper'()}

query = input("What is the last name of the brother you are looking for?: ")

print(brothers[query]['name'])
print(brothers[query]['phone'])
