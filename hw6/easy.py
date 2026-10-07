array = [1, 2, 3, 4, 5]


def sum_of_array(array):
    sum_array = 0
    for num in array:
        sum_array += num
    return sum_array


'''

# Time complexity: O(n) because the loop does one addition to sum_array for each element. n is the size of the array.

Prompts submitted into claude: 
1. What is big o notation and how is it calculated? 

'''