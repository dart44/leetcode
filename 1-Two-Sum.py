# import profile
from operator import truediv


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, (len(nums))):
                if nums[i] + nums[j] == target:
                    return (i, j)
        return (-1,-1)

# Test
def main():
    test = Solution()
    n = [3,2,3]
    t = 6
    print(f'{test.twoSum(n, t)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()