# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def print_powers_of_two_in_range(right_border):
    power = 0
    while 2 ** power < right_border:
        print(2 ** power, end=' ')
        power += 1
    print()


if __name__ == '__main__':
    print_powers_of_two_in_range(20000)
