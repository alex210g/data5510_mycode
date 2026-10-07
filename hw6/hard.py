arr = [3, 10, 6, 1, 8]

def max_difference(array):
    if len(array) < 2:
        return None  # Not enough elements to find a difference

    min_num = float('inf')
    max_num = float('-inf')

    for num in array:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return max_num - min_num

print("Maximum difference: ", max_difference(arr))

# Time Complexity: O(n) because there is one loop that goes through the entire array to find the minimum and maximum values. n is equal to the length of the array.

'''
Questions given to AI:

1. Do I need to use a nested loop to find the maximum difference in an array?
    * the answer was no and looked for an alternate solution. 

'''