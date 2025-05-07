class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)     #using DD so we can use a list as the value

        for s in strs:
            count = [0] * 26        #iniitalizinga a list with 26 zero's
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)     #using tuple as list cannot be key in dict

        return list(res.values())     
        