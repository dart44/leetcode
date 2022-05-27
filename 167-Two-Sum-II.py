class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict = {}
        for i, number in enumerate(numbers, 1):
            complement = target - number
            if (dict.get(complement) != None):
                return (dict.get(complement), i)
            dict.update( {number: i} )

# Test
def main():
    test = Solution()
    n = [0, 0, 3, 5]
    t = 5
    print(f'{test.twoSum(n, t)}') # (2, 4)
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()