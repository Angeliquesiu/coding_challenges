# SORT BY FREQUENCY

# sort an array by frequency of the numbers
# increasing order
# decreasing order if numbers have the same frequency
# expected input: List[int]
# expected output: List[int]

# option 1: use library, which avoids counting occurences of each item for each item in the list
# O(1) with single O(n) call to build Counter 
from collections import Counter

def multiSortFreq(nums): 
    counts = Counter(nums)
    return sorted(nums, key = lambda x: (counts[x], -x))
        
# option 2: one liner
# every key call is O(n) complexity is O(n^2)
def multiSortFreq2(self, nums):
    return sorted(sorted(nums, reverse = 1), key = nums.count)
