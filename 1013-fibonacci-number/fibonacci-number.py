class Solution:
    def fib(self, n: int) -> int:
        """if n==0:
            return 0
        if n==1:
            return 1
        a,b = 0,1
        for n in range(2,n+1):
            a,b = b,a+b
        return b"""

        """fst = 0
        sec = 1
        if(n==0):
            return 0
        for i in range(2,n+1):
            curr = fst+sec
            fst=sec
            sec=curr
        return sec"""

        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
        
        


        