#parameterized and functional recursion

#sum of n natural number using paramterized recursion

# def func(sum, i, N):
#     if i>N:
#         print(sum)
#         return
#     func(sum+i, i+1, N)

# func(0, 1, 4)

#sum of n natural number using functional recursion

def func(N):
    if N==1:
        return 1
    return N*func(N-1)

print(func(3))

