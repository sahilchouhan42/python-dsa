#check if number is palindrome or not

n=1223
num=n
rev=0
while num>0:
    last=num%10
    rev = rev*10 + last
    num = num//10


if n==rev:
        print("true")
else:
        print("false")
