# pay computation with 1.5 times the hourly rate for hours worked above 40 hours

# compute pay with try/except block
try:

    # prompt user for hours and rate and convert it to float
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    
    # compute pay
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
        print('Pay:', pay)
    else:
        pay = hours * rate
        print('Pay:', pay)
except:
    print('Error, please enter numeric input')
    quit()
