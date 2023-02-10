intervals = [
    (1, 4),
    (2, 3),
    (3, 5)
]
print(intervals)
print("Sorted by first value", sorted(intervals))
print("Sorted by second value", sorted(intervals, key=lambda x: x[1]))

l = ()
l = (1,2)
print(l)