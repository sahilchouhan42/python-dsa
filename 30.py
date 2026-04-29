#find maximum consecutive ones

nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
count = 0
max_ones = 0
i=0
n = len(nums)

for i in range(0, n):
    if nums[i]==1:
        count+=1
    else:
        max_ones = max(max_ones, count)
        count=0

print(max(max_ones, count))

