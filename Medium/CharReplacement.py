class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        count = {}      # hashmap to keep freq count

        l = 0
        maxf = 0

        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # Check if the number of replacements needed exceeds k
            while (r-l+1) - maxf > k:
                # Shrink the window by moving the left pointer
                count[s[l]] -= 1
                l += 1

            # Update the maximum length of valid window
            res = max(res, r-l+1)

        return res