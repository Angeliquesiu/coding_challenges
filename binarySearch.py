# BINARY SEARCH

# option 1: iterative
# time complexity: O(n/2)
# memory complexity: O(1)
# input: nums = [-1,0,3,5,9,12], target = 9
# output: 4

def binarySearch(nums, target):
    low = mid = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    # if target not in nums return -1
    return -1