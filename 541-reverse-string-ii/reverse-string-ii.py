class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """s=list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)"""




        s=list(s)

        def reverse(l,r):
            while l<r:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1

        for i in range(0,len(s),2*k):
            reverse(i, min(i+k-1, len(s)-1))
        return "".join(s)
            
