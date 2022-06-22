class Solution:
    def climbStairs(self, n: int) -> int:
      ones, twos = 1, 1
      
      for i in range(n-1):
        temp = ones
        ones = ones + twos
        twos = temp
      return ones
        
          
        
# Driver Code
def main():
    test = Solution()
    n = 5
    print(f'{test.climbStairs(n)}')
    
# Run driver code if this file is not being imported
if __name__ == '__main__':
    main()