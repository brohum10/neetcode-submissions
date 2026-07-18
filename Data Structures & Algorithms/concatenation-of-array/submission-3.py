class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        runs = 0
        ans = []
        while (runs < 2):
            for i in nums:
                ans.append(i)
            runs += 1
        
        return ans
        



       