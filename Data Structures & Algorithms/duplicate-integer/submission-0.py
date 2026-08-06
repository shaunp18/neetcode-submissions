class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = False
        x = len(nums)
        for i in range(0, x-1):
            for j in range(i+1, x):
                if (nums[i] == nums[j]):
                    a = True
        return a