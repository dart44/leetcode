class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(set(nums)) != len(nums):
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if (i, x) == (j, y):
                        continue
                    if x == y and abs(i - j) <= k:
                        return True
        return False
            
# Test
s = Solution()
nums = [1,2,3,1,2,3]
k = 3
print(f'{s.containsNearbyDuplicate(nums, k)}')