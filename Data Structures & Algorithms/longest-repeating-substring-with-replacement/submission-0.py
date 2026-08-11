class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0

        subarry = defaultdict(int)
    
        max_length = 0
        count = 0

        for right in range(len(s)):

            subarry[s[right]] += 1

            while (right-left+1 - max(subarry.values())) > k:
                subarry[s[left]] -= 1
                left+=1
                
            max_length=max(max_length, right - left + 1)   

        return max_length     

