# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


def calculate_possible_amount(s):
    counter = 0
    while s > counter:
        boys_possible_value = counter + counter
        if (boys_possible_value + (boys_possible_value * 2) >= s):
            return counter
        counter += 1


def print_result(whole_number, result):
    print(f'{result} {whole_number - result * 2} {result}')


if __name__ == '__main__':
    whole_number = 7
    one_boy_value = calculate_possible_amount(whole_number)
    print_result(whole_number, one_boy_value)