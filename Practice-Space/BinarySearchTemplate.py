# Basic Binary Search for finding an element

def BinarySearch(arr, target):

    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right-left)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:         #go right
            left = mid + 1
        else:                           #go left
            right = mid -1

    return -1                   # Target is not found

## the left + (right-left)//2 avoids int overflow issues for very large numbers.
        
    