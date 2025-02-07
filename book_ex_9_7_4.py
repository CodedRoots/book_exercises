# this code reads a file, finds the lines starting with From, identifies the email addresses at index 1, 
# creates a dictionary with each email address and the amount of times that they sent an email. Dict[email:count].
# the last print statement prints the key and value that has the biggest value (email that sent the most emails)

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
counts = dict()
bigcount = None
bigword = None

for i in fhand:
    i = i.rstrip()
    if not i.startswith('From '):
        continue
    words = i.split()
    email = words[1]
    if email not in counts:
        counts[email] = 1
    else:
        counts[email] = counts[email] + 1
 
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count
print(bigword, bigcount)
