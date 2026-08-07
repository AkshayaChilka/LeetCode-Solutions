class Solution:
    def mySqrt(self, x: int) -> int:
        """for i in range(1,x+1):
            if i*i==x:
                return i
            if i*i>x:
                return i-1
        return 0"""
        left =1
        right=x
        res=0
        while left<=right:
            mid=(left+right)//2
            if(mid*mid==x):
                return mid
            elif(mid*mid>x):
                right=mid-1
            else:
                res=mid
                left=mid+1
        return res



        
        