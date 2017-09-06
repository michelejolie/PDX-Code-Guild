def greet(name)fname = raw_input("Merlin the freak of nature: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print i
    return hello + name
print greet("hello!")
