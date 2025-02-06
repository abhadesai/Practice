from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicatesHashSet = set()

        for num in nums:
            if num not in duplicatesHashSet:
                duplicatesHashSet.add(num)
            else:
                return True
        return False

        #BruteForce - Array is not sorted

        """for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    return True
        return False"""
         