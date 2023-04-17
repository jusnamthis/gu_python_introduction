# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.


def check_if_ticket_is_lucky(ticket):
    first_half_sum = get_first_half_sum(ticket)
    second_half_sum = get_second_half_sum(ticket)
    return first_half_sum == second_half_sum


def get_first_half_sum(ticket):
    half_sum = 0
    for i in range(6):
        if (i > 2):
            half_sum += ticket % 10
        ticket = ticket // 10
    return half_sum


def get_second_half_sum(ticket):
    half_sum = 0
    for i in range(3):
        half_sum += ticket % 10
        ticket = ticket // 10
    return half_sum


if __name__ == '__main__':
    print(check_if_ticket_is_lucky(385916))