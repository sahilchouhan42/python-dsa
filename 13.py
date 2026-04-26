#check if string is palindrome or not using recursion

#by loop

# def func(str):
#     left = 0
#     right = len(str)-1
#     while left>right:
#         if str[left]!=str[right]:
#             return False
#         left+=1
#         right-=1

#     return True

# print(func("nitin2"))


#recursion

def func(s, l, r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return func(s, l+1, r-1)

x=func("nitin", 0, 4)
print(x)
