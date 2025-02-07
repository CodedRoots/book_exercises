text = "X-DSPAM-Confidence:    0.8475"

# find the position of the numbers

posnum = text.find('0')

# slice the numbers and identify it as val variable

val = text[posnum:]

# convert the extracted value to a float

extval = float(val)

# print the result

print(extval)