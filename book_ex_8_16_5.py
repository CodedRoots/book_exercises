#This code cannot run in Python as is as there are no file in reference.
#The purpose of this code is to extract all the 'From' email addresses from a file

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
count = 0

# keeping just the lines we are interested in and counting them
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    count = count + 1
    
# splitting the emails out of the lines

    pieces = line.split()
    emails = pieces[1]
    final = emails.rstrip()
    print(final)

# last print statement with strings        
print("There were", count, "lines in the file with From as the first word")
