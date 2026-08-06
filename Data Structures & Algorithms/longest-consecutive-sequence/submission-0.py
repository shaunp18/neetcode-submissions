class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = defaultdict(int)
        
        # mark presence of each number
        for num in nums:
            s[num] = 1
        
        longest = 0
        
        # only start counting if it's the beginning of a sequence
        for num in nums:
            if s.get(num - 1, 0) == 0:   # means 'num' is start of a sequence
                current = num
                counter = 1
                
                while s.get(current + 1, 0) == 1:
                    current += 1
                    counter += 1
                
                longest = max(longest, counter)
        
        return longest
        