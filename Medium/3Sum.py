class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        result = []
        
        for i in range(len(nums) - 2):  # Iterate through each element as the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element
            
            left, right = i + 1, len(nums) - 1  # Two pointers: left starts after i, right starts at the end of the array
            
            while left < right:  
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:  
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element (left pointer)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element (right pointer)
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move the pointers to the next possible triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
