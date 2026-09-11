class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= defaultdict(int)

        for i,num in enumerate(nums):
            reciprocate = target - num
            if reciprocate in s:
                return [s[reciprocate],i]
            s[num] = i

           