
from math import sqrt

#divisors of a number
#better solution
n=20
num=n
result=[]

for i in range(1, num//2):
    if num%i==0:
        result.append(i)
result.append(num)

print(result)

#optimal solution

m=36
num1=m
result1=[]

for i in range(1, int(sqrt(num1))+1):
    if num1%i==0:
        result1.append(i)
        if num1//i != i:
            result1.append(num1//i)


result1.sort()

print(result1)


