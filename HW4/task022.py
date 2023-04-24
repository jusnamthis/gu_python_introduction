def get_arrays_length_by_user():
    m = int(input("Enter numbers amount for first set: "))
    n = int(input("Enter numbers amount for second set: "))
    return (m, n)


def get_elems_by_user(set_len):
    print("Enter elements for your set: ")
    user_elems = []
    for i in range(1, set_len + 1):
        msg = f'{i}. elem: '
        elem = int(input(msg))
        user_elems.append(int(elem))
    return user_elems


def get_unique_elems(arr1, arr2):
    return sorted(set(arr1 + arr2))


if __name__ == "__main__":
    arrs_len = get_arrays_length_by_user()
    arr1 = get_elems_by_user(arrs_len[0])
    arr2 = get_elems_by_user(arrs_len[1])
    print(get_unique_elems(arr1, arr2))
    
