def unique_in_order(iterable):
    filtered_string = []
    if iterable:
        filtered_string.append(iterable[0])
        for i in range(len(iterable) - 1):
            if iterable[i + 1] != iterable[i]:
                filtered_string.append(iterable[i + 1])
    return filtered_string


print(unique_in_order(''))

# 
# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result