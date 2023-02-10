def delete_nth(order, max_e):
    filtered_list = []
    for i, num in enumerate(order):
        if not order[:i + 1].count(num) > max_e:
            filtered_list.append(num)
    return filtered_list


print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
