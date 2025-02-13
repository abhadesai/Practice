class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #result array with initial value of 1
        res = [1] * (len(nums))

        #Compute the prefix/postfix and store in output array
        prefix = 1                      # for the first element there is no prefix, so we need to multiply by 1 to avoid errors
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]           # this step ensures that before you move to the next elment, you already use current elem in prefix
        postfix = 1                     # no postfix for the last element
        for i in range(len(nums) - 1, -1, -1):      #start from end and decrement
            res[i] *= postfix                       #multiplying prefix*postfix
            postfix *= nums[i]          #as we move leftward, we accumulate the product of all the elements to the right of the current index for use in the next iteration
        return res