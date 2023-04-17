# Найдите сумму цифр трехзначного числа.

def calc_digits_sum_of_number(number):
    digits_sum = 0
    while number != 0:
        digits_sum += number % 10
        number = number // 10
    return digits_sum


print(calc_digits_sum_of_number(100))