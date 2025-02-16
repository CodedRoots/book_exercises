# A program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: 'X-DSPAM-Confidence:    0.8475'
# Counting these lines and extract the floating point values from each of the lines and compute the average of those values. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name

# identify variables
fname = input("Enter file name: ")
fh = open(fname)
count = 0
asc = 0

# for loop to skip the lines we are not interested in
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        
# counting the amount of lines
    count = count + 1  
    
# extracting the desired data and converting it to a float
    x = line[19:]
    spam_confidence = float(x)
    
# computing the average of the float data and count
    asc = asc + spam_confidence
    
# printing the desired output
print('Average spam confidence:', asc/count)
