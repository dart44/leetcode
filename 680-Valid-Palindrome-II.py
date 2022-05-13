class Solution:
    # Determine if a string is a palindrome
    def validPalindrome(self, s) -> bool:
            
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.helper(s, i + 1, j) or self.helper(s, i, j - 1)                
        return True
    
    def helper(self, s, left, right):
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True

        
# Test script
def main():
    input_value = input('Enter test string: ')
    res = Solution()
    print(res.validPalindrome(input_value))
    return res.validPalindrome(input_value)

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()