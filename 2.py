n= 54678
num=n
count=0

while num>0:
    count+=1
    num = num//10

print(count)

#time complexity----> o(log10(n))
#space complexity----> o(1)
