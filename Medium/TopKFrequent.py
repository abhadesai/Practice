class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}          #hashmap to count values
        freq = [[] for i in range(len(nums) + 1)]   # empty array with same size as nums

        #Initializing hashmap and array
        for num in nums:
            count[num] = 1 + count.get(num, 0)      #If num doesnt already exist in the hashmap, set default value 0
        for num, cnt in count.items():
            freq[cnt].append(num)                   # num occurs cnt times in freq array. cnt is the index.
        
        res = []
        for i in range(len(freq) - 1, 0, -1):    #loop thru array backwards. Start from last index, go till 0,, keep decrementing
            for num in freq[i]:
                res.append(num)
                if len(res) == k:                   #stop loop once k elements found
                    return res