class Solution:
    def isHappy(self, n: int) -> bool:
        """sets=set()
        while(n!=1 and n not in sets):
            sets.add(n)
            ans=0
            while (n!=0):
                dig=n%10
                ans=dig**2+ans
                n=n//10
            n=ans
        return n==1"""

        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)             # move 1 step
            fast = get_next(get_next(fast))   # move 2 steps
        
        return fast == 1






































        
            


        