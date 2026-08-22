class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        sum=0
        pro=1
        while n!=0:
            dig=n%10
            sum+=dig
            pro*=dig
            n=n//10
        total=sum+pro
        return original%total==0

        


        