from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # we only care about the k-th most frequent elements in nums
        # the count of the numbers is what matters, their values are just identifiers
        # sorting the array would group together equal numbers, but is that helpful?
        # assign all numbers present in nums to a key in hash map. Values = frequency
        
        frequency_table = defaultdict(int)
        for num in nums:
            # Increment entry for given 'num' each time it is found in 'nums'
            frequency_table[num] = frequency_table[num] + 1
            
        # Create a descending-order frequency hash table
        max_freqs = {i: j for i, j in sorted(frequency_table.items(), key=lambda item: item[1], reverse=True)}
        
        # Add k-th topmost elements from the descending-order frequency hash table to output
        output = []
        for x, key in enumerate(max_freqs.keys()):
            if x >= k:
                break
            output.append(key)
        return output

# Test
def main():
    test = Solution()
    n = [1,1,1,2,2,3]
    k = 2
    print(test.topKFrequent(n, k))
    
# Run test script if this file is not being imported
if __name__ == '__main__':
    main()