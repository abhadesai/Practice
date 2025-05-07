#Given an array of integers nums and an integer k, return the maximum sum of any contiguous subarray of size k

#Sliding Window - fixed size window example

def max_sum_subarray_k(nums, k):
    start = 0  # Left end of the window
    end = 0    # Right end of the window
    window_sum = 0
    max_sum = float('-inf')         #canalso take 0

    # Iterate until the end pointer reaches the end of the array
    while end < len(nums):
        # Add the current element to the window sum
        window_sum += nums[end]

        # Check if the window size is less than k
        if end - start + 1 < k:
            end += 1  # Expand the window to the right
        elif end - start + 1 == k:
            # Update max_sum if needed
            max_sum = max(max_sum, window_sum)

            # Shrink the window from the left
            window_sum -= nums[start]
            start += 1
            end += 1  # Move the right edge too

    return max_sum
