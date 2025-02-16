# A program to read through a text file and figure 
# out the distribution by hour of the day for each of the messages.

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()

for i in fhand:
    i = i.rstrip()
    if not i.startswith('From '):
        continue      
    words = i.split()
    hours = words[5]
    hours = hours.split(':')
    hours = hours[0]
    if hours not in counts:
        counts[hours] = 1
    else:
        counts[hours] = counts[hours] + 1

for k,v in sorted(counts.items()):
    print(k,v)
