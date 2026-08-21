class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        """left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left"""


        def binarySearch(left,right):
            if left>right:
                return left
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return binarySearch(mid+1,right)
            else:
                return binarySearch(left,mid-1) 
        return binarySearch(0,len(nums)-1)

        