fname = Michele Jolie("Enter file name: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print (i)