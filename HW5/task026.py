def get_raise_power():
    return int(input("Enter power: "))


def get_value_to_power():
    return int(input("Enter val to power: "))


def power_value(val, power):
    if (power == 0):
        return 1
    return val * power_value(val, power - 1)


if __name__ == "__main__":
    print(power_value(get_value_to_power(), get_raise_power()))