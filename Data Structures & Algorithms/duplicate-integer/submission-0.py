class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        control_set = set()
        for i in nums:
            if i in control_set: return True
            control_set.add(i)
        return False