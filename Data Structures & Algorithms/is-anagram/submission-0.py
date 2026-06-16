class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        set_s = set(s)
        set_t = set(t)

        if set_s == set_t:
            return True
        else:
            return False
