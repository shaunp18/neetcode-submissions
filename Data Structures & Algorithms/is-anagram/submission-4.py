class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        shash = defaultdict(int)

        thash = defaultdict(int)

        for nums in s:
            shash[nums] += 1

        for nums in t:
            thash[nums] += 1

        for nums in shash:
            if shash.get(nums, 0) == thash.get(nums, 0):
                continue
            else:
                return False
        return True

        
        
        
        