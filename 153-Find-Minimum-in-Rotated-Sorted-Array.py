# Because the array is sorted, nums[0] is the minimum
# it is then rotated between 1 and n times, moving nums[0] to nums[1], then nums[2] until looping back to nums[0] for n rotations
# if rotations < n, min = nums[0 + rotations]
# how do I figure out how many times it was rotated?
# iterate through array until nums[i] > nums [i+1]? too slow.
# answer is some sort of binary search.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        min_num = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                min_num = min(nums[left], min_num)
                break
            
            mid = left + ((right - left) // 2)
            min_num = min(nums[mid], min_num)

            if nums[left] <= nums[mid]:
                left = mid +1
            else:
                right = mid -1
        return min_num

# Test
def main():
    test = Solution()
    n = [3,4,5,1,2]
    print(f'{test.findMin(n)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()