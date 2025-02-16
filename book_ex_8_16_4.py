#Find all unique words in a file

fname = input('Enter the file name:')
fh = open(fname)
txt = fh.read()
txt = txt.rstrip()
words = txt.split()

lst = []

for i in words:
    if i not in lst:
        lst.append(i)
     
print(sorted(lst))
