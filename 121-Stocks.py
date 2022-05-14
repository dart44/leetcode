class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            profit = max(profit, prices[r] - prices[l])
        return profit
        
    
# Test script
def main():
    input_value = [3,2,1,3,8]
    res = Solution()
    print(res.maxProfit(input_value))
    return res.maxProfit(input_value)

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()