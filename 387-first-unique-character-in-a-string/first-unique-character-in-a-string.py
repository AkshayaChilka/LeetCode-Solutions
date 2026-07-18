class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = s.lower()
        for x in range(len(n)):
            if n.count(n[x])==1:
                return x
        return -1
