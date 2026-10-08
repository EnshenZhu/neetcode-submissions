class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table={}
        for i in range(len(nums)):
            if target-nums[i] in table:
                return [table[target-nums[i]],i]
            else:
                table[nums[i]]=i

# Time Complexity --> O(N)
# Space Complexity --> O(1) --> to store the target result