#recursion using parameters

# def func(x, N):
#     if N==0:
#         return
#     print(x)
#     func(x, N-1)


# func(15, 4)

#print 1 to N using recursion ---> head recursion

# def func(i, N):
#     if i>N:
#         return
#     print(i)
#     func(i+1,N)

# func(1, 6)

#print n to 1 using tail recurion

# def func(i, N):
#     if i>N:
#         return
#     func(i+1, N)
#     print(i)

# func(1, 6)

#skip i ---> head recursion (n to 1)

# def func(N):
#     if N==0:
#         return
#     print(N)
#     func(N-1)

# func(4)

#skip i ----> tail recursion ( 1 to N)

def func(N):
    if N==N+1:
        return
    func(N-1)
    print(N)

print(4)
