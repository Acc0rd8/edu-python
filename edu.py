from math import e, fabs

def found_y(x):
    if -5 <= x <= 5:
        return e ** x
    elif x < -5:
        return 2 * fabs(x) - 1
    else:
        return 2 * x

x = int(input('Введите икс от -10 до 10: '))
if -10 <= x <= 10:
    print(f'y(x) = {found_y(x)}')
else:
    print('Неверный диапазон икс')