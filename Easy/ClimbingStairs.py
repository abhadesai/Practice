class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n
        
        #Initializing array
        dp = [0] * (n+1)

        # these values are fixed when we have 1 or 2 stairs
        dp[1] , dp[2] = 1, 2

        #filling up array

        # for any given staircase number, it is a sum of the previous two staircases solution
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] # return the value of the last element, which will give the total no of ways the stairs can be reached.
        