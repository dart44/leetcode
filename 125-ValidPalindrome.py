def reverse_string(str):
        reverse = ""
        for i in str:
            reverse = i + reverse
        return reverse

class Solution:
    # Determine if a string is a palindrome
    def isPalindrome(self, s):
        st = ''.join(filter(str.isalnum, s))
        st = st.lower()
        if st == reverse_string(st):
            return True
        else:
            return False
        
# Test script
def main():
    input_value = str(input)
    res = Solution()
    return res.isPalindrome(input_value)

# Run test script if this file is not being imported
if __name__ == '__main__':
    main()