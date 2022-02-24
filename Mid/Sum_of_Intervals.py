def sum_of_intervals(intervals):
    i = 0
    sumAll = 0
    dictAll = {}
    for listi in intervals:
        sumAll += listi[1] - listi[0]
        intervals[i] = range(listi[0], listi[1], 1)
        for num in intervals[i]:
            if num in dictAll:
                dictAll[num] += 1
            else:
                dictAll[num] = 0
        i+=1
    sumAll -= sum(dictAll.values())
    return sumAll

print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))




# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
# Overlapping Intervals

# List containing overlapping intervals:

# [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ]

# The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.
# Examples:

# sumIntervals( [
#    [1,2],
#    [6, 10],
#    [11, 15]
# ] ); // => 9

# sumIntervals( [
#    [1,4],
#    [7, 10],
#    [3, 5]
# ] ); // => 7

# sumIntervals( [
#    [1,5],
#    [10, 20],
#    [1, 6],
#    [16, 19],
#    [5, 11]
# ] ); // => 19
