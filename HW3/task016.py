# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint


def generate_numbers():
    numbers_amount = int(input('Enter amount of numbers: '))
    numbers = [randint(1, 10) for x in range(numbers_amount)]
    return numbers


def get_number_to_count():
    return int(input('Enter number to count: '))


def count_number_in_list(numbers, number):
    counter = 0
    for el in numbers:
        if el == number:
            counter += 1
    return counter


def get_numbers_and_count_n_entries():
    numbers = generate_numbers()
    print(numbers)
    number_to_count = get_number_to_count()
    entries = count_number_in_list(numbers, number_to_count)
    return entries


if __name__ == '__main__':
    print(get_numbers_and_count_n_entries())

