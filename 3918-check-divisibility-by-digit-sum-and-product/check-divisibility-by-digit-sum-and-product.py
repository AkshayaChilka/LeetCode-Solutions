class Solution:
    def checkDivisibility(self, n: int) -> bool:
        """original=n
        sum=0
        pro=1
        while n!=0:
            dig=n%10
            sum+=dig
            pro*=dig
            n=n//10
        total=sum+pro
        return original%total==0"""

        digit_sum = 0
        digit_product = 1
        
        for ch in str(n):
            d = int(ch)
            digit_sum += d
            digit_product *= d
        
        total = digit_sum + digit_product
        return n % total == 0

        


        