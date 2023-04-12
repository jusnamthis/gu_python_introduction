# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random


def generate_coins(coins_amount):
    return [random.randrange(0, 2) for x in range(coins_amount)]


def count_minimal_coins_to_flip(coins):
    heads_coins_amount = len(list(filter(lambda x: x > 0, coins)))
    tails_coins_amount = len(list(filter(lambda x: x == 0, coins)))
    
    if (heads_coins_amount > tails_coins_amount):
        return [tails_coins_amount, 0]
    elif (tails_coins_amount >= heads_coins_amount):
        return [heads_coins_amount, 1]
    

def print_result(coins_to_flip):
    coins_side = 'tails' if coins_to_flip[1] == 0 else 'heads'
    print(f'You need to flip {coins_to_flip[0]} {coins_side}')


if __name__ == '__main__':
    coins = generate_coins(22)
    coins_to_flip = count_minimal_coins_to_flip(coins)
    print_result(coins_to_flip)