from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)
        for word in strs:
            letters = list(word)
            sl = sorted(letters)
            sorted_letters = ''.join(sl)
            dict[sorted_letters].append(word)
        return list(dict.values())
    
# Test
def main():
    test = Solution()
    n = ["eat","tea","tan","ate","nat","bat"]
    print(test.groupAnagrams(n))  # [['ate','eat','tea'],['nat','tan'],['bat']]
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()