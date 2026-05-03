#rearrange array elements by sign

nums = [5, 10, -3, -1, -10, 6]

#brutfull solution
# pos = [5, 10, 6]
# neg = [-3, -1, -10]

# for i in range(0, len(pos)):
#     nums[2*i] = pos[i]
#     nums[(2*i)+1] = neg[i]

# print(nums)

#optimal solution

n = len(nums)
result = [0]*n
posIndex=0
negIndex=1

for i in range(0, n):
    if nums[i]>=0:
        result[posIndex] = nums[i]
        posIndex+=2
    else:
        result[negIndex] = nums[i]
        negIndex+=2

print(result)