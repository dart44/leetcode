# import profile
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        if sl == tl: return True
        else: return False
# Test
def main():
    test = Solution()
    s = "aaca"
    t = "ccac"
    print(f'{test.isAnagram(s, t)}')
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    # profile.run('main()') - test execution time
    main()