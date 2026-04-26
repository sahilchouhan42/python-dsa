#find the second largest element in array

nums = [2, 44, 32, 55, 76, -5, 98]
largest = float('-inf')
second_largest = float('-inf')

#1st method
# for i in range(0, len(nums)):
#     if nums[i]>largest:
#         largest = nums[i]

# for j in range(0, len(nums)):
#         if nums[j]!=largest and nums[j]>second_largest:
#             second_largest = nums[j]

# print(second_largest)

#2nd method
for i in range(0, len(nums)):
     if nums[i]>largest:
          second_largest = largest
          largest = nums[i]
     elif nums[i]>second_largest and nums[i]!=largest:
          second_largest = nums[i]
    

print(second_largest)