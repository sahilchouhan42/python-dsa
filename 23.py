#remove duplicates from sorted array

nums = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]

n = len(nums)
# freq_map = {}

# for i in range(0, n):
#     freq_map[nums[i]]=0
# j=0
# for k in freq_map:
#     nums[j] = k
#     j+=1

# print(j)

#another optimal solution

i=0
j=i+1

while j<n:
    if nums[j]!=nums[i]:
        i+=1
        nums[i], nums[j] = nums[j], nums[i]
    j+=1

print(i+1)
