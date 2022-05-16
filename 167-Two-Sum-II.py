# [-1, 0, 1, 1, 2, 3, 3, 4, 5]

# target = 9

# comparing every number to every other number is slow O(n^2)

# maybe if next number == current number, skip -- apply this at every increment for r and at the beginning of the l loop (might be problematic because we want indexes not sums)

# Two Pointer solution; left and right
# if l + r > target, move l up one and start again at new l + new r

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        return [0, 0]

# Test
def main():
    test = Solution()
    n = [0, 0, 3, 5]
    t = 5
    print(f'{test.twoSum(n, t)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()