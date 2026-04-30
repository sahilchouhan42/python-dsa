# two sum problem

nums = [5, 9, 1, 2, 4, 15, 6, 3]

n= len(nums)
target = 13
result = None
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         if nums[i]+nums[j]==target:
#             result = [i, j]
#             break

# print(result)

#optimal solution

hash_map = {}
for i in range(0, n):
    remaining = target-nums[i]
    if remaining in hash_map:
        result = [hash_map[remaining], i]
    hash_map[nums[i]] = i

print(result)
print(hash_map)

