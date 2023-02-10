def move_zeros(lst):
    filtered_lst = []
    count = 0
    for num in lst:
        if num != 0:
            filtered_lst.append(num)
        else:
            count += 1
    return filtered_lst + [0] * count



print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]


# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))