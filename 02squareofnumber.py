# n=3 The list of non-negative integers that are less than 3 is [0,1,2]
# Print the square of each number on a separate line.

n = int(input(""))

for i in range(n):
    sqr = i**2
    i += 1
    print(sqr)

    list = []

    n = int(input(""))

    for i in range(n):
        list.append(i)
        
    i = 0
    for i in list:
        sqr = i**2
        i+=1
        print(sqr)

#another method is:
n = int(input(""))
for i in range(n):
    sqr = i**2
    i += 1
    print(sqr)