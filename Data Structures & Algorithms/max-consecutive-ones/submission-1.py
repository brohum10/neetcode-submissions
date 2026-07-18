class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = actual = 0

        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            
            if (actual < count):
                actual = count
        return actual