#grading code
name=input('enter your name:')
print('hello {}'.format(name))
print('{} Please! enter marks to know grade.'.format(name))
marks=eval(input('enter your marks'))
if marks>0 and marks<100:

    if marks>79:
        print('{} You got an A,Congrats!'.format(name))
    elif marks>74:
        print('{} You got an A-,'.format(name))
    elif marks>65:
        print('{} you got B+'.format(name))
    elif marks>58:
        print('{} you got B'.format(name))
    elif marks>50:
        print('{} you got B-'.format(name))
    elif marks>45:
        print('{} you got C+'.format(name))
    elif marks>40:
        print('{} you got C'.format(name))
    elif marks>35:
        print('{} You got C-'.format(name))
    elif marks>30:
        print('{} you got D+'.format(name))
    elif marks>25:
        print('{} you got D'.format(name))
    elif marks>20:
        print('{} you got a D-'.format(name))
    elif marks<20:
        print('{} you got an E :oops!'.format(name))

    else:
        print('This line is always printed.')
else:
    print('Invalid marks,Please check the marks again{}.'.format(name))