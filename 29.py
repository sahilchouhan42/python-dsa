#find messing number in array

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n= len(nums)

# result=None

# for i in range(0, n+1):
#     if i not in nums:
#         result = i
#         break

# print(result)

#best solution

# result = None
# freq={}

# for i in range(0, n+1):
#     freq[i] = 0
# for num in nums:
#     freq[num]=1
# for k, v in freq.items():
#     if v==0:
#         result = k
#         break

# print(result)

#optimal solution

total_sum = n*(n+1)/2
array_sum = 0
for i in range(0, n):
    array_sum+=nums[i]

missing_number = total_sum - array_sum
print(missing_number)