class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        k_binary = (2 ** k)
        dict = {}
        
        left = 0
        right = k
        while right <= len(s):
            if s[left:right] not in dict:
                print(s[left:right])
                dict.update({s[left:right]: +1})
            left += 1
            right += 1
        print(len(dict))
        if len(dict) == k_binary:
            return True
        return False
        
# Test
def main():
    test = Solution()
    n = "00110"
    k = 2
    print(f'{test.hasAllCodes(n, k)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()