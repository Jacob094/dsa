class Solution:
    # Set operations on the list will give us a length
    # 
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)