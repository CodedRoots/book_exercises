# code cannot run as is as it does not have a file in reference
# Write a program to read through the mbox-short.txt and figure 
# out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the 
# time and then splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out 
# the counts, sorted by hour as shown below.

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