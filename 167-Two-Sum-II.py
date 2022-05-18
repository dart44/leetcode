class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if (dict.get(complement) != None):
                return (dict.get(complement), i+1)
            dict.update( {numbers[i]: i+1} )

# Test
def main():
    test = Solution()
    n = [0, 0, 3, 5]
    t = 5
    print(f'{test.twoSum(n, t)}') # (1, 4)
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()