# Recursion: 

# Inception: Dream within a dream. 
#     dream within a dream 
#         dream within a dream

#Iterative version: 
# def sum_numbers(n): 
#     val = 0 
#     for i in range(1, n+1): 
#         val += i 
#     return val

# recursive version: 

def sum_numbers_rec(n): 
    if n == 1: 
        return n
    return n + sum_numbers_rec(n-1)

print(sum_numbers_rec(5))       

