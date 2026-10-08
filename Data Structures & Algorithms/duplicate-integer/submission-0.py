class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val_set=set()
        for e in nums:
            if e not in val_set:
                val_set.add(e)
            else:
                return True
        return False