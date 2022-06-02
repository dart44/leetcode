class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # array sorted but pivoted on random pivor between 1 and nums.length
        # find target in O(log n) time
        # binary search, but slightly different...
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if target == nums[mid]:
                return mid
            
            # left sorted side
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # right sorted side
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1   

# Test
def main():
    test = Solution()
    n = [8,9,1,2,3,4,5]
    k = 9
    print(f'{test.search(n, k)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()