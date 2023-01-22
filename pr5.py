"""
Беляева Наталья KI22-17/1Б
Практическая работа №4
Вариант 6
"""

print('образец ввода цвета: #HHHHHH»')
menu_main = ['0 - выход', '1 - ввод цвета и процента осветления']
menu = ['0 - назад', '1 - цвет осветлится', '2 - цвет затемнится']


def lighten(color: str, percent: int) -> str:
    """Функция получает код цвета и процент, на который цвет будет осветлен
    и выводит код получившегося цвета.

    Для этого из 16ичной системы переводится значение цвета и прибавляется процент от его значения.
    Затем полученные значение объединяются в вид по образцу

    param color, percent: код цвета, процент осветления
    return: строка с кодом цвета
    raises:Index error
    examples:
    >>lighten('#000000, 100')
        #FFFFFF
    >>lighten('#1A1B19, 36')
        #232422
    """
    if color == '#000000' and percent == 100:
        lighten_color = 'ffffff'
    else:
        red = min(int(color[1:3], 16) + int(color[1:3], 16) * percent // 100, 255)
        green = min(int(color[3:5], 16) + int(color[3:5], 16) * percent // 100, 255)
        blue = min(int(color[5:], 16) + int(color[5:], 16) * percent // 100, 255)
        lighten_color = hex(red)[2:] + hex(green)[2:] + hex(blue)[2:]
    return '#' + lighten_color.upper()


def darken(color: str, percent: int) -> str:
    """Функция получает код цвета и процент, на который цвет будет затемнен
    и выводит код получившегося цвета

    Для этого из 16ичной системы переводится значение звета и вычитается процент от его значения.
    Затем полученные значения объединяются в вид по образцу

    param color, percent: код цвета, процент затемнения
    return: строка с кодом цвета
    raises:Index error
    examples:
    >>darken('#FFFFFF, 100')
        #000000
    >>darken('#1A1B19, 36')
        #111210
    """
    if color == '#FFFFFF' and percent == 100:
        lighten_color = '000000'
    else:
        red = max(int(color[1:3], 16) - int(color[1:3], 16) * percent // 100, 0)
        green = max(int(color[3:5], 16) - int(color[3:5], 16) * percent // 100, 0)
        blue = max(int(color[5:], 16) - int(color[5:], 16) * percent // 100, 0)
        lighten_color = hex(red)[2:] + hex(green)[2:] + hex(blue)[2:]
    return '#' + lighten_color.upper()


def main():
    while True:
        print('\n'.join(menu_main))
        cmd = input()
        if cmd == '0':
            break
        elif cmd == '1':
            color = input('введите номер цвета по образцу ')
            percent = int(input('введите процент, на который цвет осветлится или затемнится '))
            while True:
                print('\n'.join(menu))
                cmd_task = input()
                if cmd_task == '0':
                    break
                elif cmd_task == '1':
                    print(lighten(color, percent))
                elif cmd_task == '2':
                    print(darken(color, percent))
                else:
                    print('ошибка ввода. попробуйте снова')
        else:
            print('ошибка ввода. попробуйте снова')


if __name__ == '__main__':
    main()
