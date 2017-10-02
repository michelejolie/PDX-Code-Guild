fname = raw_input("Merlin the freak of nature: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print(i)