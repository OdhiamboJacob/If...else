import math
# string methods
'''
 len() # number of characters in the string
 course.upper()
 course.lower()
 courae.find()
 course.replace()
 '....' in course
'''
# arithmetic operations
'''
 int
 float
'''
# math functions
'''
x = 2.9
print(round(x))
# If Statements
is_hot = False
is_cold =False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print('wear warm clothes')
else:
    print('Good day')
print((10/100)*1000000)
print((20/100)*1000000)
# Exe
price = 1000000
good = 10/100
bad = 20/100
'''
'''
buyer = input('key in buyer')
if buyer == 'good':
    print(good*price)
elif buyer == 'bad':
    print(bad*price)
'''
# Logical operators
# used for multiple conditions
'''
and - when both conditions are true
or - when one of the conditions is true
not - when changing the bool to otherwise
'''
'''
goodcredit = False
criminal = False
if goodcredit or criminal:
    print('give loan')
else:
    print('no loan')
'''
# comparison operators
'''
greater than - >
less than - <
equal to - ==
not equal - !=
less than or equal to - <=
greater than or equal to - >=
'''
# Exe
'''
name = 'fhdrgfc'
if len(name) >= 3 and len(name) <= 50:
    print('name looks good')
elif len(name) < 3:
    print('name must be at least three characters')
elif len(name) >= 50:
    print('name must be a maximum of 50 characters')
else:
    print('fuck off')
'''
# weight converter
'''
weight = int(input( 'weight: '))
L = 2.222
K = 0.45
unit = eval(input('lbs or kg: '))
if unit == L:
    print(weight*L)
if unit == K:
    print(weight*K)
'''
# While loops
''''
used to execute a block of code multiple times eg programmes and games.
syntax - while , condition: then codes bellow
'''
'''
i = 1
while i <= 5:
    print('1' * i) # this line alone will end up in an infinite loop coz one will remain one and less than 5 forever.
    i = i + 1
print('Done')
'''
# guessing game
'''
secret = 9
guess_count = 0
gues_limit = 3
while guess_count < gues_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret:
        print('you won')
        break
else:
    print('sorry you faild')
'''
# car game
comand = ''
started = False
while True:
    comand = input('>').lower()
    if comand == 'start':
        if started:
            print('Hell..! car is already started,,!')
        else:
            started = True
            print('Great,,! car has started...')
    elif comand == 'stop':
        if not started:
            print('crout..! car is already stopped')
        else:
            started = False
            print('wow..! car has stopped..')
    elif comand == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit
        ''')
    elif comand == 'quit':
        break
    else:
        print('sorry i do not understand you')
# for Loops
