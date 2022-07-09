list = []

n = int(input("NUM>"))

for i in range(n):
    list.append(i)
    
i = 0
for i in list:
    sqr = i**2
    i+=1
    print(sqr)