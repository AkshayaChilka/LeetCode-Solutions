class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ans = 0

        for num in nums:
            ans ^= num

        return ans"""

        seen=set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()

        
            



                     
                 

        