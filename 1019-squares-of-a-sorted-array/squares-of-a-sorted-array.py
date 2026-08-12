class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """left = 0
        right = len(nums) - 1
        ans = [0] * len(nums)
        k = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square < right_square:
                ans[k] = right_square
                right -= 1
            else:
                ans[k] = left_square
                left += 1

            k -= 1"""


        return sorted(x * x for x in nums)

        return ans        