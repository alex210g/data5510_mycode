#Medium.py work. 
#More practice on it. 

medium_list = [1, 5, 7, 3, 7, 9]

def second_largest(medium_list):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in medium_list:
        if num > largest: 
            second_largest = largest 
            largest = num
        elif num > second_largest and num < largest: 
            second_largest = num
        else: 
            continue
    return second_largest

print("Second Largest Number:", second_largest(medium_list))

