def get_num():
    return int(input('enter number to sum: '))


def recursion_sum(a, b):
    if (a == 0 or b == 0):
        return 1
    return a + recursion_sum(1, b - 1)


if __name__ == '__main__':
    print(
        recursion_sum(
            get_num(), 
            get_num()
            )
        )