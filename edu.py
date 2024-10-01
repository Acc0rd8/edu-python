def triangle():
    for i in range(1, 6):
        count_spaces = (5 - i) * 2
        print((5 - i) * ' ', (9 - count_spaces) * '*', (5 - i) * ' ', sep='')

def rectangle():
    for i in range(1, 6):
        if i == 1 or i == 5:
            print(5 * '*')
        else:
            print('*', ' ' * 3, '*', sep='')


num = int(input('Введите число: '))
if num == 1:
    triangle()
else:
    rectangle()