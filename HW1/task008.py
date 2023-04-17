# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 


def check_break_off_possibility(rows, columns, desired_size):
    if desired_size < rows and desired_size < columns:
        return False
    horizontal = check_horizontal_break_off_possibility(rows, columns, desired_size)
    vertical = check_horizontal_break_off_possibility(columns, rows, desired_size)
    return horizontal or vertical


def check_horizontal_break_off_possibility(rows, columns, desired_size):
    current_possible_range = 0
    for i in range(rows):
        current_possible_range += columns
        if (current_possible_range == desired_size): 
            return True
        elif (current_possible_range > desired_size):
            return False
    return False


if __name__ == '__main__':
    print(check_break_off_possibility(3, 2, 4))