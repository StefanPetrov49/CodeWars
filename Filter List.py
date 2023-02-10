def filter_list(l):
    filtered_list = []
    for char in l:
        if isinstance(char, int):
            filtered_list.append(char)
    return filtered_list
    # return (filtered_list.append(char) for char in l if str(char).isdigit())

print(filter_list([1, 2, 'a', 'b', '1']))