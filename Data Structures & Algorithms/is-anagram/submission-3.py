class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        p = defaultdict(int)
        l = defaultdict(int)
        for char in s:
            p[char] += 1
            
        
        for char in t:
            l[char] += 1
        print(dict(p))
        print(dict(l))
        for charact in p:
            if p.get(charact, 0) == l.get(charact,0):
                continue
            else:
                return False
        return True
        
        
        