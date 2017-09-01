quater = 25
dime = 10
nickel = 5
penny = 1

change = input("change input: ")


qc = int(change) // int(quater)
post_qc = (qc) * (quater)
sub_qc = int(change) - int(post_qc)
dc = int(sub_qc) // int(dime)
post_dc = (dc) * (dime)
sub_dc = int(sub_qc) - int(post_dc)
nc = int(sub_dc) // int(nickel)
post_nc = (nc) * (nickel)
sub_nc = int(sub_dc) - int(post_nc)
pc = int(sub_nc) // int(penny)


# print(int(d10), 'tens')
print(int(qc), 'quarters')
print(int(dc), 'dimes')
print(int(nc), 'nickels')
print(int(pc), 'pennies')