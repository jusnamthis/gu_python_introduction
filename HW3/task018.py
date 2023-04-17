# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

from task016 import generate_numbers, get_number_to_count


def get_nearest_number_to_desired_value():
    numbers = generate_numbers()
    print(numbers)
    desired_number = get_number_to_count('Enter the number to which you want to find an approximation: ')
    return find_approximation(numbers, desired_number)


def find_approximation(numbers, desired_number):
    res = numbers[0]
    for i in range(1, len(numbers)):
        if abs(desired_number - res) > abs(desired_number - numbers[i]):
            res = numbers[i]
    return res


if __name__ == '__main__':
    print(get_nearest_number_to_desired_value())