import random 

st = []
for i in range(100): 
    st.append(random.randint(1,100))

print(st)

st2: [random.randint(1,100) for x in range(200)]

print("st2: \n", st2)

st3 = [2 ** x for x in range(11)]
print ("st3: \n", st3)



