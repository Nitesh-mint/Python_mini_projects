'''Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along with 
an integer . Print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to n.
Please use list comprehensions rather than multiple loops, as a learning exercise.'''

from math import perm


x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
n = int(input("n:"))


#to create list of vlues .eg if x is 2 then x1 is [0,1,2]
x1 = [a for a in range(x+1)]
y1 = [b for b in range(y+1)]
z1 = [c for c in range(z+1)]

permutation = [[i,j,k] for i in x1 for j in y1 for k in z1 if (i+j+k) !=n]
print(permutation)