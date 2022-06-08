class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

s = Solution()
nums = [1, 2, 3]
print(s.containsDuplicate(nums))