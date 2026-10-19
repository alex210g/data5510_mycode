#Sort this list:

list = [3, 1, 4, 1, 5, 9]

for j in range(len(list)-s): 
    for i in range(len(list)-1):
        #compare two elements and swap if element 1 is greater 
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

print("list: ", list)

