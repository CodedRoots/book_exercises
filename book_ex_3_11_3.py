# write a program that prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

# compute grade with try/except block
while True:
    try:
        score = float(input('Enter score: '))
        if score < 0 or score > 1:
            print('Please enter a numeric value between 0 and 1.')
        else:
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            else:
                print('F')
            break
    except:
        print('Please enter a numeric value between 0 and 1.')
        
