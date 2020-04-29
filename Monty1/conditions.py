import random
comodity = input('enter good name')
goodcode = eval(input('please input good code to know the price'))
cake = 1
milk = 2
flour = 3
jik = 4
mandazi = 5
egg = 6
sweet = 7
book = 8
pen = 9
ndovu = 9.1
if comodity == cake or milk or flour or jik or mandazi or egg or sweet or book or pen or ndovu:
    price='the price is: sh.'
    if goodcode >= 1 and goodcode < 10:
        if goodcode == 1:
            print(f'{price}100')
        elif goodcode == 2:
            print(f'{price}50')
        elif goodcode == 3:
            print(f'{price}110')
        elif goodcode == 4:
            print(f'{price}80')
        elif goodcode == 5:
            print(f'{price}10')
        elif goodcode == 6:
            print(f'{price}15')
        elif goodcode == 7:
            print(f'{price}5')
        elif goodcode == 8:
            print(f'{price}25')
        elif goodcode == 9:
            print(f'{price}20')
        elif goodcode > 9:
            print(f'{price}130')
    else:
        print('No such range, try again')
else:
    print('invalid good name please try again')