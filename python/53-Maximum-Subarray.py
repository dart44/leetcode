class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        
        for num in nums:
          if curr_sum < 0:
            curr_sum = 0
          curr_sum += num
          max_sum = max(max_sum, curr_sum)
        return max_sum
      
# Driver Code
def main():
    test = Solution()
    n = 0
    print(f'{test.name()}')
    
# Run driver code if this file is not being imported
if __name__ == '__main__':
    main()