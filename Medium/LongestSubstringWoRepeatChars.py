class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        res = 0
        l = 0 

        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)       #The difference right - left gives the number of characters between the two pointers, but it excludes the current character at the left pointer itself.
                                        #To include the character at left in the window, we add 1 to the result
        return res