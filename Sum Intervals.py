# def sum_of_intervals(intervals):
#     nums = []
#     for i in range(len(intervals)):
#         for num in range(intervals[i][0], intervals[i][1]):
#             if num not in nums:
#                 nums.append(num)
#     return len(nums)
import sys


# def sum_of_intervals(intervals):
#     intervals = sorted(intervals)
#     largest_gap = ()
#     largest_gap_score = 0
#     result = 0
#     for i in range(len(intervals)):
#         if intervals[i][1] - intervals[i][0] > largest_gap_score:
#             largest_gap_score = intervals[i][1] - intervals[i][0]
#             largest_gap = (intervals[i][0], intervals[i][1])
#     min = largest_gap[0]
#     max = largest_gap[1]
#     for i in range(len(intervals)):
#         lower_border = intervals[i][0]
#         higher_border = intervals[i][1]
#         if min <= lower_border <= max and min <= higher_border <= max:
#             continue
#         elif min <= lower_border <= max < higher_border:
#             max = higher_border
#         elif lower_border > min < higher_border < max:
#             min = lower_border
#         else:
#             result += higher_border - lower_border
#     return result + max-min

# def sum_of_intervals(intervals):
#     return len(set({i for a,b in intervals for i in range(a,b)}))


def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    separated_ranges = []
    start_range = intervals[0][0]
    end_range = intervals[0][1]
    result = 0
    for i in range(len(intervals) - 1):
        next_start_range = intervals[i + 1][0]
        next_end_range = intervals[i + 1][1]
        if start_range <= next_start_range <= end_range:
            if next_end_range > end_range:
                end_range = next_end_range
            else:
                next_end_range = end_range
        elif end_range < next_start_range:
            separated_ranges.append((start_range, end_range))
            start_range = next_start_range
            end_range = next_end_range
        if i == len(intervals) - 2:
            separated_ranges.append((start_range, next_end_range))
    if separated_ranges:
        for i in separated_ranges:
            x, y = i
            result += y - x
    else:
        result = end_range - start_range

    return result


# intervals = [
#     (1, 4),
#     (7, 10),
#     (3, 5),
# ]
# print(sum_of_intervals(intervals))

intervals = [
    (10, 20),
    (16, 19)

]
print(sum_of_intervals(intervals))


def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a, b in sorted(intervals):
        if top < a: top = a
        if top < b: s, top = s + b - top, b
    return s
