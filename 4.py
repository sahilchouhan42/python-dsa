#armstrong number

n=153
num=n
total = 0
nod = len(str(num))

while num>0:
    last = num % 10
    total = total + (last**nod)
    num=num//10
    
if(total==n):
    print("armstrong")
else: 
    print("not armstrong")