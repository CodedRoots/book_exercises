# write a program that prompts for a list of numbers and at the end prints out both max and min of the numbers

numbers= []

while True:
    nbrs = input('Enter a number: ')
    if nbrs == 'done':
        break
    try:
        fnbrs = float(nbrs)
        numbers.append(fnbrs)
    except:
        print('Invalid input')
        continue

if numbers:
    print('Maximum:', max(numbers))
    print('Minimum:', min(numbers))
else:
    print('No numbers were entered')
