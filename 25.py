#right rotate an array by k position

nums = [1, 2, 3, 4, 5, 6, 7, 8]
k=5
n=len(nums)
 
# for _ in range(0, k):
#     e = nums.pop()
#     nums.insert(0, e)

# print(nums)

# nums[:]=nums[n-k:] + nums[:n-k]

# print(nums)

def reverse(nums, left, right):
    while left<right:
        nums[left], nums[right]=nums[right], nums[left]
        left+=1
        right-=1

reverse(nums,n-k, n-1)
reverse(nums,0, n-k-1)
reverse(nums, 0, n-1)

print(nums)
