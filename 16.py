#bubble sort in array

nums = [1, 3, 4, 6, 8, 22]

def bubble_sort(nums):
    n=len(nums)
    is_swap = False
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True

    return is_swap

print(bubble_sort(nums))