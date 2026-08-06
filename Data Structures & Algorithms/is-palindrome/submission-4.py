
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""


        s = s.lower()

        for char in s:
            if char.isalnum():
                cleaned = cleaned + char
        if len(cleaned) == 0:
            return True
        for char in cleaned:
            for i in range(len(cleaned)):
                if (cleaned[i] == cleaned[len(cleaned) - i - 1]):
                    continue
                else:
                    return False
            return True

