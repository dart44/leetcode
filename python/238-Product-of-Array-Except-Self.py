import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # answer[i] = product of all nums except nums[i]
        # get product of left * product of right?
        # output = []
        # multiples = nums.copy()
        # # print(multiples)
        # for i, num in enumerate(nums):
        #     # print(num)
        #     if num == 1:
        #         output.append(math.prod(multiples))
        #         continue
        #     m = multiples[:i] + multiples[i+1:]
        #     output.append(math.prod(m))
        # return output
        
        # Initialize output array
        output = [1]*len(nums)
        # Prefix product calculation
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            output[i] *= product
        # Postfix product calculation
        product = 1
        for i in range(len(nums)-2, -1,-1):
            product *= nums[i+1]
            output[i] *= product
        return output

# Test
def main():
    test = Solution()
    n = [-1, 1, 0, -3, 3]
    print(test.productExceptSelf(n)) # [0,0,9,0,0]
    test = Solution()
    n = [1,2,3,4]
    print(test.productExceptSelf(n)) # [24,12,8,6]
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()