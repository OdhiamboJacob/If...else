print('Shopkeeper: Hi; Am Jak')
commodity = input('Enter good name: ')
goodcode = eval(input('Enter good code to know the price: '))
cake = 1
bread = 2
sugar = 3
milk = 4
tealeaves = 5
basin = 6
padlock = 7
jacket = 8
rubber = 9
gasmask = 10
if goodcode >= 1 and goodcode <= 10:
    if goodcode == 1:
        print('cake is 80 shillings')
    elif goodcode == 2:
        print('bread is 50 shillings')
    elif goodcode == 3:
        print('sugar is 120 shillings')
    elif goodcode == 4:
        print('milk is 100 shillings')
    elif goodcode == 5:
        print('tealeaves is 10 shillings')
    elif goodcode == 6:
        print('basin is 400 shillings')
    elif goodcode == 7:
        print('padlock is 250 shillings')
    elif goodcode == 8:
        print('jacket is 350 shillings')
    elif goodcode == 9:
        print('rubber s 25 shillings')
    elif goodcode == 10:
        print('gasmask is 50 shillings')
    else:
        print('Invalid good code try again')
else:
    print('this line is always printed; check the good code')