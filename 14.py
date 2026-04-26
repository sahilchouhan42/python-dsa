#fibonacci number using recursion

def func(n):
    if n==0 or n ==1:
        return n
    return func(n-1)+func(n-2)

ans = func(20)

print(ans)