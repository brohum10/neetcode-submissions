class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        cnt = 0
        for num in nums:
            if num:
                cnt = cnt + 1 
            else:
                cnt = 0
            
            if cnt > res:
                res = cnt
        return res