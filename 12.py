#reverse an array using recursiion


# def reverse(nums, left, right):
#     if left>=right:
#         return
#     nums[left], nums[right] = nums[right], nums[left]
#     return reverse(nums, left+1, right-1)

# reverse(nums, 1, 5)

# print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
left= 1
right = len(nums)-2

while left<right:
    nums[left],nums[right] = nums[right], nums[left]
    left+=1
    right-=1

print(nums)

