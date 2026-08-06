class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = defaultdict(int)

        for num in nums:
            s[num] += 1
            if s[num] > 1:
                return True
        return False