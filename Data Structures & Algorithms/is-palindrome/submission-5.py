
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""

        for char in s:
            if char.isalnum() == True:
                cleaned = cleaned + char


        cleaned = cleaned.lower()

        for i in range(len(cleaned) // 2):
            if cleaned[i] == cleaned[len(cleaned) - 1 - i]:
                continue
            else:
                return False

        return True

