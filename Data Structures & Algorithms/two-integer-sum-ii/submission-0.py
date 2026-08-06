class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = defaultdict(int)

        for i, num in enumerate(numbers):
            complement = target - num
            
            if complement in s:
                return [s[complement]+1, i+1]
            s[num] = i

        