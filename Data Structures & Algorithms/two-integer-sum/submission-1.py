class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       

        emptyHolder = {}

        for i in range(len(nums)):
            diff = target-nums[i]

            if diff in emptyHolder:
                return [emptyHolder[diff], i]
                
            emptyHolder[nums[i]] = i
        