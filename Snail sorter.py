def is_valid(i, y, board):
    pass


def snail(snail_map):
    sorted_array = []
    first_row = snail_map[0]
    row = len(first_row)
    while True:
        for i in range(len(snail_map)):
            for y in range(len(snail_map)):
                valid = is_valid(i, y ,snail_map)
                if valid:
                    sorted_array.append(snail_map[i][y])



    return sorted_array


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]

print(snail(array))

# for
#     for length in range(row):
#         sorted_array.append(snail_map[0][length])
# for length_2 in range(1, row):
#     sorted_array.append(snail_map[length_2][row - 1])
# for length_3 in range(row - 2, -1, -1):
#     sorted_array.append(snail_map[row - 1][length_3])
# for length_4 in range(row - 2, 0, -1):
#     sorted_array.append(snail_map[length_4][0])