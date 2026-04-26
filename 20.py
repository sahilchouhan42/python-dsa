#largets element in an array
#method 1

nums = [22, 3, 45, 69, -90, 0]
# largest = nums[0]
largest = float("-inf")
n = len(nums)

for i in range(0, n):
    # largest = max(largest, nums[i])
    if nums[i]>largest:
        largest = nums[i]

print(largest)