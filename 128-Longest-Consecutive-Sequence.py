from collections import defaultdict
from itertools import count

def count_sequence(num, d) -> int:
    if num+1 in d.keys():
        return 1 + count_sequence(num+1, d)
    return 1

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dict = {}
        for num in nums:
            dict[num] = 1
        for num in nums:
            right = num
            if right+1 not in dict:
                left = right
                while left-1 in dict:
                    dict[left-1] = 1 + dict[left]
                    left -= 1
        return max(dict.values())

# Test
def main():
    test = Solution()
    n = [100,4,200,1,3,2] # 4
    print(f'Longest Sequence is {test.longestConsecutive(n)}')
    test = Solution()
    n = [1,0,-1] # 3
    print(f'Longest Sequence is {test.longestConsecutive(n)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()