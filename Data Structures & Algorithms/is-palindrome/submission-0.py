
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= s.lower()
        cleaned = ""

        for char in a:
            if char.isalnum():
                cleaned += char
        print(cleaned)
        for i in range(len(cleaned)//2):
            if cleaned[i] == cleaned[len(cleaned) - 1- i]:
                
                continue
            else:
                
                return False
        return True
        