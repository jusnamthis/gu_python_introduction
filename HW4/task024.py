def get_whole_amount_of_garden_beds():
    beds = int(input("Beds amount: "))
    return beds


def get_amount_of_bushes_on_bed():
    bushes = int(input("Bushed on bed: "))
    return bushes


def generate_garden(beds_amount, bushes_in_bed):
    beds = []
    for i in range(beds_amount):
        bed = []
        for j in range(bushes_in_bed):
            msg = f'Enter amount of berries for the {j} bush in {i} row: '
            bed.append(int(input(msg)))
        beds.append(bed)
    return beds


def start_berries_collecting_count(beds):
    prev_row = 0
    current_row = 1
    next_row = 2
    max_collected_val = 0
    for i in range(len(beds[0])):
        tmp_val = 0

        if (next_row > 0):
            tmp_val = beds[prev_row][i] + beds[current_row][i] + beds[next_row][i]
        else:
            tmp_val = beds[prev_row][i] + beds[current_row][i]
            
        if tmp_val > max_collected_val:
            max_collected_val = tmp_val
        
        prev_row = current_row
        current_row = next_row

        if (next_row + 1 < len(beds)):
            next_row += 1
        else:
            next_row = -1
    return max_collected_val


beds = get_whole_amount_of_garden_beds()
bushes = get_amount_of_bushes_on_bed()
garden = generate_garden(beds, bushes)
print(start_berries_collecting_count(garden))
