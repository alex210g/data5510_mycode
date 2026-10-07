

array = [-1, -2, -3, -4, -5]

def second_largest(array):
    if len(array) < 2:
        return None  # Not enough elements for a second largest

    first = float('-inf')
    second = float('-inf')
    for num in array:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    if second == float('-inf'):
        return None  # No second largest number found
    return second

print("Second largest number: ", second_largest(array))



'''
Questions given to AI: 

1. What is the best way to find a bigger number even when the array contains negative numbers?
2. Asked AI why I was getting 0 repeatedly instead of the actual number. It then helped me look for the issue and found that I had the return statement inside the loop
3. I also asked AI if >= would be better than what I had already done for the first if statement. It said that it would not be better because it would not allow for the second largest number to be found if the first largest number is repeated.


Time Complexity: O(n) because there is one loop and it goes for the length of the array. n is equal to the length of the array. 

Second Largest means the second distinct number. 

'''