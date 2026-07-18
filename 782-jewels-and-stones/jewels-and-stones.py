class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        count = 0
        for n in stones:
            if n in j:
                count+=1
        return count        


        