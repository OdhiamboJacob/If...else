name=input('enter your name :')
print('my name is {} '.format(name))
marks=eval(input('Please {} Enter your marks  to know your score'.format(name)))
if marks>0 and marks<100:
    if marks>=80:
        print('{} You attained First class.\n EXCELLENT'.format(name))
    elif marks>65:
        print('{} You attained Second class upper.\n WOW GREAT'.format(name))
    elif marks>55:
        print('{} You attained Second class lower.\n VERY GOOD'.format(name))
    elif marks>40:
        print('{} You have Pass. \n GOOD'.format(name))
    elif marks>5:
        print('{} You have Fail.\n OOPS!'.format(name))
    else:
        print('I\'m just somewhere there. '.format(name))
else:
    print ('Invalid entry mr/mrs {} please try again'.format(name))